# Author: Jaco ter Hoeve
# This file implements the training of the quadratic classifier

# !/usr/bin/env python
# coding: utf-8
import copy
import glob
from time import sleep

import sns as sns
import torch
import torch.utils.data as data
import torch.optim as optim
import pylhe
import numpy as np
import datetime
import math
# import matplotlib
import json
import os
# matplotlib.use("TkAgg")
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import animation
import xsec_cluster as ExS
from torch import nn
#from progress.bar import Bar
import sys
import pandas as pd
import shutil
import seaborn as sns

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


# print("Using torch", torch.__version__)


# eft_points = [[-2.0, 0], [-1.0, 0], [-0.5, 0], [0.5, 0], [1.0, 0], [2.0, 0], [0, -2.0], [0, -1.0], [0, -0.5],
#                       [0, 0.5], [0, 1.0], [0, 2.0], [-2.0, -2.0], [-1.0, -1.0], [-0.5, -0.5], [0.5, 0.5], [1.0, 1.0],
#                       [2.0, 2.0]]

eft_points = [[-10.0, 0], [-5.0, 0], [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0], [0, -2.0], [0, -1.0], [0, -0.5],[0, 0.5], [0, 1.0], [0, 2.0], [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],[10.0, 2.0], [0.0, 0.0]]

class MLP(nn.Module):

    def __init__(self, architecture):
        """
        Set up the NN architecture

        Inputs:
            act_fn - Object of the activation function that should be used as non-linearity in the network.
            input_size - Size of the input images in pixels
            num_classes - Number of classes we want to predict
            hidden_sizes - A list of integers specifying the hidden layer sizes in the NN
        """
        super().__init__()

        input_size = architecture[0]
        hidden_sizes = architecture[1:-1]
        output_size = architecture[-1]

        # Create the network based on the specified hidden sizes
        layers = []
        layer_sizes = [input_size] + hidden_sizes
        for layer_index in range(1, len(layer_sizes)):
            layers += [nn.Linear(layer_sizes[layer_index - 1], layer_sizes[layer_index]), nn.ReLU()]
        layers += [nn.Linear(layer_sizes[-1], output_size)]
        self.layers = nn.Sequential(
            *layers)  # nn.Sequential summarizes a list of modules into a single module, applying them in sequence

    def forward(self, x):
        out = self.layers(x)
        return out


class Predictor_linear(nn.Module):
    """
    Returns the function f(x,c) from the paper (Wulzer et al.) in the linear case
    """

    def __init__(self, architecture):
        super().__init__()
        self.n_alpha = MLP(architecture)

    def forward(self, x, c):
        n_alpha_out = self.n_alpha(x)
        return 1 / (1 + (1 + c * n_alpha_out ** 2))


class Predictor_quadratic(nn.Module):
    """
        Returns the function f(x,c) from the paper (Wulzer et al.) in the quadratic case
    """

    def __init__(self, architecture):
        super().__init__()
        self.n_12 = MLP(architecture)
        self.n_13 = MLP(architecture)
        self.n_22 = MLP(architecture)
        self.n_23 = MLP(architecture)
        self.n_33 = MLP(architecture)

    def forward(self, x, ctg, cuu):
        n_12 = self.n_12(x)
        n_13 = self.n_13(x)
        n_22 = self.n_22(x)
        n_23 = self.n_23(x)
        n_33 = self.n_33(x)
        r = (1 + n_12 * ctg + n_13 * cuu) ** 2 + (n_22 * ctg + n_23 * cuu) ** 2 + (n_33 * cuu)**2
        return 1 / (1 + r)


def loss_fn(outputs, labels, w_e):
    """
    :param outputs: outputs.shape = (batch_size, 1), output \in (0, 1)
    :param labels: labels.shape = (batch_size, 1), labels \in {0, 1}
    :param w_e: w_e.shape = (batch_size, 1), w_e \in [0, \infty)
    :return: contribution to loss from a sample x ~ pdf(x|H_0,1)
    """

    loss = (1 - labels) * w_e * outputs ** 2 + labels * w_e * (1 - outputs) ** 2
    # add up all the losses in the batch
    return torch.sum(loss, dim=0)


class EventDataset(data.Dataset):

    def __init__(self, c, path_dict, hypothesis, n_dat):
        """
        Inputs:
            c - value of the Wilson coefficient
            hypothesis - 0 (False) if EFT and 1 (True) if SM
        """
        super().__init__()

        self.c = c
        self.path_dict = path_dict
        self.hypothesis = hypothesis
        self.n_dat = n_dat

        # set instance attribute to none, initialised later in sub-initalisation methods
        self.events = None
        self.weights = None
        self.labels = None

        self.standardized = False
        self.mean = None
        self.std = None
        self.min_value = None
        self.max_value = None

        self.load_events()
        #self.find_mean_std()

    def invariant_mass(self, p1, p2):
        """
        Computes the invariant mass of an event
        """
        return np.sqrt(
            sum((1 if mu == 'e' else -1) * (getattr(p1, mu) + getattr(p2, mu)) ** 2 for mu in ['e', 'px', 'py', 'pz']))

    def rapidity(self, p1, p2):
        """
        Computes the rapidity of an event
        """
        q0 = getattr(p1, 'e') + getattr(p2, 'e')  # energy of the top quark pair in the pp COM frame
        q3 = getattr(p1, 'pz') + getattr(p2, 'pz')
        y = 0.5 * np.log((q0 + q3) / (q0 - q3))
        return y

    def rescale(self, mean, std):
        self.events = (self.events - mean) / std

    def standardize(self):
        """
        Standardize the dataset so that neurons are more likely to have nonzero gradients
        """
        self.standardized = True

        for k, v in self.data_eft.items():
            data_std = (v[0] - self.mean) / self.std
            self.data_eft_std[k] = data_std, v[1], v[2]

        self.data_sm_std = (self.data_sm[0] - self.mean) / self.std, self.data_sm[1], self.data_sm[2]

    def get_mean_std(self):
        """
        Find the mean and standard deviation of the data and save to disk
        """
        self.mean = torch.mean(self.events, dim=0)
        self.std = torch.std(self.events, dim=0)
        return self.mean, self.std


    def find_min_max(self):
        """
        Find the minimum and maximum of the data
        """

        min_values, max_values = [], []

        for c_i in self.c_values:
            dataset_eft = self.data_eft['{}'.format(c_i)][0]
            dataset_sm = self.data_sm['{}'.format(c_i)][0]
            min_value_eft, _ = torch.min(dataset_eft, dim=0)
            max_value_eft, _ = torch.max(dataset_eft, dim=0)
            min_value_sm, _ = torch.min(dataset_sm, dim=0)
            max_value_sm, _ = torch.max(dataset_sm, dim=0)

            self.min_value, _ = torch.min(torch.stack((min_value_eft, min_value_sm)), dim=0)
            min_values.append(self.min_value)

            self.max_value, _ = torch.max(torch.stack((max_value_eft, max_value_sm)), dim=0)
            max_values.append(self.max_value)

        min_values = torch.stack(min_values)
        max_values = torch.stack(max_values)

        self.min_value, _ = torch.min(min_values, dim=0)
        self.max_value, _ = torch.max(max_values, dim=0)

    # def rescale(self, low, up):
    #     """
    #     Rescale the input data to lie in the interval [low, up]
    #     inputs:
    #         - min_value.shape = (1, 2)
    #         - max_value.shape = (1, 2)
    #     """
    #
    #     self.resc = True
    #
    #     for k, v in self.data_eft.items():
    #         data_resc = low + (up - low) / (self.max_value - self.min_value) * (v[0] - self.min_value)
    #         self.data_eft_resc[k] = data_resc, v[1], v[2]
    #
    #     for k, v in self.data_sm.items():
    #         data_resc = low + (up - low) / (self.max_value - self.min_value) * (v[0] - self.min_value)
    #         self.data_sm_resc[k] = data_resc, v[1], v[2]

    def lhe_loader(self, path):
        """
        Les Houches Event file reader
        """
        weight = []
        event_data = []
        cnt = 0
        for e in pylhe.readLHE(path):
            mtt = self.invariant_mass(e.particles[-1], e.particles[-2])

            if False: #self.switch_2d:
                y = self.rapidity(e.particles[-1], e.particles[-2])
                event_data.append([mtt, y])
            else:
                event_data.append([mtt])
            weight.append(e.eventinfo.weight)

            cnt += 1
            if cnt == self.n_dat:
                break
        print("Data loaded")
        self.events = torch.tensor(event_data)
        self.weights = (torch.tensor(weight)/self.n_dat).unsqueeze(-1)
        self.labels = torch.ones(self.n_dat).unsqueeze(-1) if self.hypothesis else torch.zeros(self.n_dat).unsqueeze(-1)



    def load_events(self):
        """
        Load the datasets (eft and sm) from the les Houches event files.
        """

        if not self.hypothesis:
            path_to_sample = self.path_dict[self.c]
        else:
            path_to_sample = self.path_dict[self.c]
        self.lhe_loader(path_to_sample)



    def visualize(self):
        f1 = plt.figure()
        # f2 = plt.figure()
        ax1 = f1.add_subplot(111)
        #ax2 = f2.add_subplot(111)
        mtt = self.data_eft_std[2.0, 2.0][0][:, 0].view(-1).numpy()
        y = self.data_eft_std[2.0, 2.0][0][:, 1].view(-1).numpy()
        ax1.scatter(mtt, y)
        #ax2.hist(mtt, bins=1, range=(2000, 2500), label='sm', histtype='step')
        # for c in [0.5, 1.0, 2.0]:
        #     mtt = self.data_eft['{}'.format(c)][0][:, 0].view(-1).numpy()
        #     y = self.data_eft['{}'.format(c)][0][:, 1].view(-1).numpy()
        #     ax1.scatter(mtt, y, label='{}'.format(c))
        #     ax2.hist(mtt, bins = 1, range=(2000, 2500), label='{}'.format(c),histtype='step')

        ax1.set_xlabel(r'$m_{tt}$ (rescaled)')
        ax1.set_ylabel('y (rescaled)')
        #ax1.set_xlim(2000, 2500)


        #ax2.set_yscale('log')

        ax1.legend()
        #ax2.legend()
        plt.show()

    def __len__(self):
        # Number of data points we have.
        return self.n_dat

    def __getitem__(self, idx):
        """
        Return a tuple (eft, sm) with info on the idx-th data point of the dataset
        Outputs:
            - data tuple: (eft event, sm event)
            - label tuple: label = 0 for the eft, label = 1 for the sm
            - weight tuple: weight per event
        """

        data_sample, weight_sample, label_sample = self.events[idx], self.weights[idx], self.labels[idx]

        return data_sample, weight_sample, label_sample



def plot_training_report(train_loss, val_loss, path):


    f = plt.figure()
    plt.plot(np.array(train_loss), label='train')
    plt.plot(np.array(val_loss), label='val')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()
    f.savefig(path + 'plots/loss.pdf')


def training_loop(n_epochs, optimizer, model, train_loader, val_loader, path):

    loss_list_train, loss_list_val = [], []  # stores the training loss per epoch
    loss_val_old = 0
    overfit_counter = 0
    patience = 10

    for epoch in range(1, n_epochs + 1):
        loss_train, loss_val = 0.0, 0.0

        # We save the model parameters at the start of each epoch
        torch.save(model.state_dict(), path + 'trained_nn_{}.pt'.format(epoch))

        for minibatch in zip(*train_loader):
            train_loss = torch.zeros(1)
            n_eft_points = len(eft_points)
            for i, [event, weight, label] in enumerate(minibatch):
                ctg, cuu = eft_points[i % n_eft_points]
                output = model(event.float(), ctg, cuu)
                loss = loss_fn(output, label, weight)
                train_loss += loss

            optimizer.zero_grad()
            train_loss.backward()
            optimizer.step()

            loss_train += train_loss.item()

        with torch.no_grad():
            for minibatch in zip(*val_loader):
                val_loss = torch.zeros(1)
                n_eft_points = len(eft_points)
                for i, [event, weight, label] in enumerate(minibatch):
                    ctg, cuu = eft_points[i % n_eft_points]
                    output = model(event.float(), ctg, cuu)
                    loss = loss_fn(output, label, weight)
                    val_loss += loss
                assert val_loss.requires_grad is False

                loss_val += val_loss.item()

        loss_list_train.append(loss_train)
        loss_list_val.append(loss_val)

        print('{} Epoch {}, Training loss {}'.format(datetime.datetime.now(), epoch, loss_train),
              'Validation loss {}'.format(loss_val))

        np.savetxt(path + 'loss.out', loss_list_train)

        # in case we reach the maximum number of epochs, save the final state
        if epoch == n_epochs:
            torch.save(model.state_dict(), path + 'trained_nn.pt')
            break

        # check whether the network is overfitting by increasing the overfit_counter by one if the
        # validation loss increases during the epoch. If the counter increases for 10 epochs straight,
        # stop the training.

        if loss_val > loss_val_old and epoch > 1:
            overfit_counter += 1

        if overfit_counter == patience:
            stopping_point = epoch - patience
            shutil.copyfile(path + 'trained_nn_{}.pt'.format(stopping_point), path + 'trained_nn.pt')
            break

        loss_val_old = loss_val

    plot_training_report(loss_list_train, loss_list_val, path)


def train_classifier(path, architecture, data_train, data_val, epochs, quadratic=True):
    model = Predictor_quadratic(architecture) if quadratic else Predictor_linear(architecture)

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    n_batches = 1
    train_data_loader = [data.DataLoader(dataset_train, batch_size=int(dataset_train.__len__()/n_batches), shuffle=True) for dataset_train in data_train]
    val_data_loader = [data.DataLoader(dataset_val, batch_size=int(dataset_val.__len__()/n_batches), shuffle=False) for dataset_val in data_val]

    training_loop(
        n_epochs=epochs,
        optimizer=optimizer,
        model=model,
        train_loader=train_data_loader,
        val_loader=val_data_loader,
        path=path
    )


def f_linear(x, n_alpha, ctg):
    f_nn = [1 / (1 + 1 + ctg * n_alpha(x_i.float()).item() ** 2) for x_i in x]
    return np.array(f_nn)


def f_quadratic(x, n_alpha, n_beta, ctg):
    f_nn = [1 / (1 + (1 + ctg * n_alpha(x_i.float()).item()) ** 2 + (ctg * n_beta(x_i.float()).item()) ** 2) for x_i in
            x]
    return np.array(f_nn)

def get_pull(network_size, ctg, cuu, mtt):
    mc_runs = 42

    f_pred = []
    for i in range(1, mc_runs + 1):
        pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(i)
        mean, std = np.loadtxt(pred_path + '/scaling.dat')
        f_pred_i = get_predictions_1d(pred_path + '/trained_nn.pt', network_size, mtt, ctg, cuu, mean, std)
        f_pred.append(f_pred_i)

    f_pred = np.array(f_pred)
    f_pred_median = np.median(f_pred, axis=0)
    f_pred_std = np.std(f_pred, axis=0)

    theory = 1 / (1 + ExS.likelihood_ratio_1D_v(mtt, ctg.numpy(), cuu.numpy()))
    pull = (theory - f_pred_median)/f_pred_std
    return pull




def plot_pull_heatmap(network_size,mtt):
    plt.figure()


    ctg = np.arange(-2, 2, 0.1)
    cuu = np.arange(-2, 2, 0.1)
    # ctg = np.array([-2, -1, 1, 2])
    # cuu = np.array([-2, -1, 1, 2])
    ctg_grid, cuu_grid = np.meshgrid(ctg, cuu, indexing='xy')
    pull = get_pull(network_size, torch.from_numpy(ctg_grid), torch.from_numpy(cuu_grid), mtt)


    fig = plt.figure()
    plt.imshow(pull, extent=[np.min(ctg), np.max(ctg), np.min(cuu), np.max(cuu)], origin='lower', cmap=plt.cm.summer,
               aspect=(np.max(ctg) - np.min(ctg)) / (cuu.max() - cuu.min()), interpolation='quadric')
    plt.colorbar()
    plt.xlabel(r'$\rm{ctg}$')
    plt.ylabel(r'$\rm{cuu}$')
    plt.title(r'$\rm{Pull\:heatmap\:at\:m_{tt}=\:}$' + r'${}$'.format(mtt) + r'$\:\mathrm{TeV}$')
    fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/pull_v3.pdf')



def plot_predictions_1d(network_path, network_size, ctg, cuu, epochs):
    #animate_learning_1d(path, network_size, ctg, cuu, epochs, mean, std)

    fig = plt.figure()
    mtt_min, mtt_max = 1000, 4000
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])

    mc_runs = 42
    f_pred = []

    for i in range(1, mc_runs + 1):
        pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_7/mc_run_{}'.format(i)
        mean, std = np.loadtxt(pred_path + '/scaling.dat')
        mtt, f_pred_i = make_predictions_1d(pred_path + '/trained_nn.pt', network_size, ctg, cuu, mean, std)
        f_pred.append(f_pred_i)
    
    f_pred = np.array(f_pred)
    f_pred_median_1 = np.median(f_pred, axis=0)
    f_pred_std = np.std(f_pred, axis=0)
    
    
    # Plot the NN prediction
    nn_med_plot_1, = ax1.plot(mtt[:,0], f_pred_median_1,'--', linewidth=0.75)
    ax1.plot(mtt[:,0], f_pred_median_1 + 2*f_pred_std, color='C0', linewidth=0.75)
    ax1.plot(mtt[:, 0], f_pred_median_1 - 2 * f_pred_std, color='C0', linewidth=0.75)
    nn_band_plot_1 = ax1.fill_between(mtt[:,0], f_pred_median_1 - 2*f_pred_std, f_pred_median_1 + 2*f_pred_std, alpha=0.3)

    mc_runs = 42
    f_pred = []

    for i in range(1, mc_runs + 1):
        pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(i)
        mean, std = np.loadtxt(pred_path + '/scaling.dat')
        mtt, f_pred_i = make_predictions_1d(pred_path + '/trained_nn.pt', network_size, ctg, cuu, mean, std)
        f_pred.append(f_pred_i)

    f_pred = np.array(f_pred)
    f_pred_median_2 = np.median(f_pred, axis=0)
    f_pred_std = np.std(f_pred, axis=0)

    # Plot the NN prediction
    nn_med_plot_2, = ax1.plot(mtt[:, 0], f_pred_median_2, '--', linewidth=0.75)
    ax1.plot(mtt[:, 0], f_pred_median_2 + 2 * f_pred_std, color='C1', linewidth=0.75)
    ax1.plot(mtt[:, 0], f_pred_median_2 - 2 * f_pred_std, color='C1',linewidth=0.75)
    nn_band_plot_2 = ax1.fill_between(mtt[:, 0], f_pred_median_2 - 2 * f_pred_std, f_pred_median_2 + 2 * f_pred_std, alpha=0.3)

    # mc_runs = 42
    # f_pred = []
    #
    # for i in range(1, mc_runs + 1):
    #     pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_9/mc_run_{}'.format(i)
    #     mean, std = np.loadtxt(pred_path + '/scaling.dat')
    #     mtt, f_pred_i = make_predictions_1d(pred_path + '/trained_nn.pt', network_size, ctg, cuu, mean, std)
    #     f_pred.append(f_pred_i)
    #
    # f_pred = np.array(f_pred)
    # f_pred_median = np.median(f_pred, axis=0)
    # f_pred_std = np.std(f_pred, axis=0)

    # Plot the NN prediction
    # nn_med_plot_3, = ax1.plot(mtt[:, 0], f_pred_median, '--')
    # nn_band_plot_3 = ax1.fill_between(mtt[:, 0], f_pred_median - 2 * f_pred_std, f_pred_median + 2 * f_pred_std, alpha=0.3)
    # Compute the analytic likelihood ratio and plot

    x, y = ExS.plot_likelihood_ratio_1D(mtt_min * 10 ** -3, mtt_max * 10 ** -3, ctg, cuu)
    x = np.array(x)
    y = np.array(y)
    ana_plot, = ax1.plot(x * 1e3, y, color='red', linewidth=0.75)


    plt.ylabel(r'$f\;(m_{tt}, c)$')
    #plt.xlabel(r'$m_{tt}\;[GeV]$')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    plt.title(r'$\rm{NN\:versus\:analytical\:at\:cuu}$' + r'$\:={}$'.format(cuu) + r'$\rm{\:and\:ctg}$' + r'$\:={}$'.format(ctg))
    #plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1), (nn_band_plot_2, nn_med_plot_2), (nn_band_plot_3, nn_med_plot_3)], [r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{50K}$', r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{100K}$', r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{20K}$'])
    plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1), (nn_band_plot_2, nn_med_plot_2)],[r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{\:50K}$', r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{\:100K}$'])
    #plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1)], [r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{50K}$'])
    
    ax2 = fig.add_axes([0.15, 0.1, 0.75, 0.20])
    ax2.plot(x * 1e3, (y - f_pred_median_2) / f_pred_std )
    #ax2.plot(x * 1e3, y / f_pred_median_1, color='C0')
    #ax2.plot(x * 1e3, y / f_pred_median_2, color='C1')
    #ax2.hlines(1, mtt_min, mtt_max, linestyles='dashed', colors='black')
    plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
    #plt.ylabel(r'$\rm{theory/model}$')
    plt.ylabel(r'$\rm{pull}$')
    plt.xlim((mtt_min, mtt_max))
    #plt.ylim((0.9*(y / f_pred_median_1).min(), 1.1*(y / f_pred_median_1).max()))
    plt.ylim((1.2 * np.min((y - f_pred_median_1) / f_pred_std), 1.2 * np.max((y - f_pred_median_1) / f_pred_std)))
    #fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/' + 'pull_v2.pdf')
    fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/' + 'NNvsAna_f_band_v4.pdf')


def plot_predictions_2d(network_path, network_size, train_dataset, quadratic, ctg, epochs):
    """
    Plot several plots that gauge the performance of the NN
    :param network_path: p
    :param network_size: network architecture
    :param train_dataset:
    :param quadratic: Include Quadratic EFT (Boolean)
    :param ctg: Wilson coefficient (Float)
    :return:
    """

    animate_learning_2d(path, network_size, train_dataset, quadratic, ctg, epochs)

    if quadratic:
        xx, yy, x_span, y_span, f_pred, n_alpha_nn, n_alpha_n_beta_nn, f_ana = make_predictions_2d(
            network_path + 'trained_nn.pt', network_size, train_dataset, quadratic, ctg, False)
    else:
        xx, yy, f_pred, n_alpha_nn, f_ana = make_predictions_2d(network_path + 'trained_nn.pt', network_size,
                                                                train_dataset, quadratic, ctg)

    mtt_min, mtt_max = 1000, 4000
    s = (14 * 10 ** 3) ** 2
    y_min, y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)

    # plot the nn prediction
    fig = plt.figure()
    plt.imshow(f_pred, extent=[mtt_min, mtt_max, y_min, y_max], origin='lower', cmap=plt.cm.Blues,
               aspect=(mtt_max - mtt_min) / (y_max - y_min), interpolation='quadric')
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('y')
    plt.title(r'$f\;(x, c)$' + ' at ctG = {}'.format(ctg))
    plt.show()
    fig.savefig(network_path + 'plots/f_nn.pdf')

    # plot the analytical result
    fig = plt.figure()
    # mask values outside the physical region
    # f_ana = np.where(f_ana == 1.0, -1.0, f_ana)
    f_ana = np.ma.masked_where(f_ana == 1.0, f_ana)
    cmap = copy.copy(plt.get_cmap("Blues"))  # Can be any colormap that you want after the cm
    cmap.set_bad(color='white')

    plt.imshow(f_ana, extent=[mtt_min, mtt_max, y_min, y_max], origin='lower', cmap=cmap,
               aspect=(mtt_max - mtt_min) / (y_max - y_min), interpolation='quadric')
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('y')
    plt.title(r'$f\;(x, c)$' + ' at ctG = {}'.format(ctg))
    plt.show()
    fig.savefig(network_path + 'plots/f_ana.pdf')

    # plot the ratio analytical/nn_prediction
    fig = plt.figure()
    cmap2 = copy.copy(plt.get_cmap("seismic"))
    cmap2.set_bad(color='#c8c9cc')
    f_comp = f_ana / f_pred
    plt.imshow(f_comp, extent=[mtt_min, mtt_max, y_min, y_max], origin='lower', cmap=cmap2, vmin=0.8, vmax=1.2,
               aspect=(mtt_max - mtt_min) / (y_max - y_min), interpolation='quadric')
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('y')
    plt.title('ratio at ctG = {}'.format(ctg))
    plt.show()
    fig.savefig(network_path + 'plots/f_comp.pdf')

    fig = plt.figure()
    mtt_index = np.where(x_span == 1100)[0][0]
    plt.plot(yy[:, mtt_index], f_pred[:, mtt_index], label='NN prediction')
    plt.plot(yy[:, mtt_index], f_ana[:, mtt_index], label='analytical')
    plt.xlabel('y')
    plt.legend()
    plt.show()

def get_predictions_1d(network_path, network_size, mtt, ctg, cuu, mean, std):
    loaded_model = Predictor_quadratic(network_size)
    loaded_model.load_state_dict(torch.load(network_path))
    x = (mtt * 10**3 - mean) / std  # rescale the inputs
    x = torch.tensor([x])
    f_pred = loaded_model.forward(x.float(), ctg, cuu)
    f_pred = f_pred.detach().numpy()
    return f_pred

def make_predictions_1d(network_path, network_size, ctg, cuu, mean, std):
    """
    :param network_path: path to the saved NN to be loaded
    :param train_dataset: training data needed to find the mean and std
    :param ctg: value of the Wilson coefficient ctg
    :return: comparison between NN prediction and analytically known result for the likelihood ratio
    """

    # Be careful to use the same network architecture as during training
    loaded_model = Predictor_quadratic(network_size)
    loaded_model.load_state_dict(torch.load(network_path))

    # Set up coordinates and compute f
    mtt_min, mtt_max = 1000, 4000
    mtt = torch.arange(mtt_min, mtt_max, 10).unsqueeze(1)
    x = (mtt - mean) / std  # rescale the inputs

    f_pred = loaded_model.forward(x.float(), ctg, cuu)
    f_pred = f_pred.view(-1).detach().numpy()

    return mtt.numpy(), f_pred


def make_predictions_2d(network_path, network_size, train_dataset, quadratic, ctg, make_animation):
    """
    :param network_path: path to the saved NN to be loaded
    :param train_dataset: training data needed to find the mean and std
    :param ctg: value of the Wilson coefficient ctg
    :return: comparison between NN prediction and analytically known result for the likelihood ratio
    """

    # Be careful to use the same network architecture as during training
    if quadratic:
        loaded_model = Predictor_quadratic(network_size)
    else:
        loaded_model = Predictor_linear(network_size)

    # load all the parameters into the trained network
    loaded_model.load_state_dict(torch.load(network_path))

    # Set up coordinates and compute f
    mtt_min, mtt_max = 1000.0, 4000.0
    s = (14 * 10 ** 3) ** 2
    y_min, y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
    x_spacing, y_spacing = 10, 0.01
    x_span = np.arange(mtt_min, mtt_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)
    xx, yy = np.meshgrid(x_span, y_span)
    grid = torch.Tensor(np.c_[xx.ravel(), yy.ravel()])
    # rescale the grid
    grid = (grid - train_dataset.mean) / train_dataset.std
    # grid = -1 + 2 / (train_dataset.max_value - train_dataset.min_value) * (grid - train_dataset.min_value)

    f_pred = loaded_model.forward(grid.float(), ctg)  # TODO: why .float() needed?
    f_pred = f_pred.view(xx.shape).detach().numpy()

    n_alpha = loaded_model.n_alpha(grid.float())
    n_alpha = n_alpha.view(xx.shape).detach().numpy()

    # if make_animation is true, don't compute the analytic prediction
    if make_animation and quadratic:
        n_beta = loaded_model.n_beta(grid.float())
        n_beta = n_beta.view(xx.shape).detach().numpy()
        n_alpha_n_beta = n_alpha ** 2 + n_beta ** 2
        return xx, yy, x_span, y_span, f_pred, n_alpha, n_alpha_n_beta

    f_ana = ExS.plot_f_ana(mtt_min, mtt_max, y_min, y_max, x_spacing, y_spacing, ctg, np_order=2)

    if quadratic:
        n_beta = loaded_model.n_beta(grid.float())
        n_beta = n_beta.view(xx.shape).detach().numpy()
        n_alpha_n_beta = n_alpha ** 2 + n_beta ** 2
        return xx, yy, x_span, y_span, f_pred, n_alpha, n_alpha_n_beta, f_ana
    else:
        return xx, yy, f_pred, n_alpha, f_ana


def animate_learning_1d(path, network_size, ctg, cuu, epochs, mean, std):


    mtt_min, mtt_max = 1000, 4000
    # First set up the figure, the axis, and the plot element we want to animate
    fig, ax = plt.subplots()
    ax = plt.axes(xlim=(mtt_min, mtt_max), ylim=(0, 1))

    # Compute the analytic likelihood ratio and plot
    x, y = ExS.plot_likelihood_ratio_1D(mtt_min * 10 ** -3, mtt_max * 10 ** -3, ctg, cuu)
    x = np.array(x)
    y = np.array(y)
    ax.plot(x * 1e3, y, '--', c='red', label='Analytical result')

    plt.ylabel(r'$f\;(m_{tt}, c)$')
    plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    plt.title('NN versus analytical at ctg = {ctg} and cuu = {cuu}'.format(ctg=ctg, cuu=cuu))

    line, = ax.plot([], [], lw=2, label='NN prediction')
    epoch_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    loss_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
    loss = np.loadtxt(path + 'loss.out')
    plt.legend()

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        epoch_text.set_text('')
        loss_text.set_text('')
        return line, epoch_text, loss_text

    # animation function.  This is called sequentially
    def animate(i):
        print(i)
        x, f_pred = make_predictions_1d(path + 'trained_nn_{}.pt'.format(i + 1), network_size, ctg, cuu, mean, std)
        line.set_data(x, f_pred)
        epoch_text.set_text('epoch = {}'.format(i))
        loss_text.set_text('loss = {:.4f}'.format(loss[i]))
        return line, epoch_text, loss_text

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=epochs, interval=200, blit=True)

    anim.save(path + 'animation/training_animation.gif')


def animate_learning_2d(path, network_size, train_dataset, quadratic, ctg, epochs):
    # stopping_point = int(glob.glob(path + "/trained_nn_*.pt", recursive=False)[0][-6:-3])
    # print(stopping_point)
    # sys.exit()

    with open(path + 'stopping.txt') as f:
        stopping_point = int(f.read())

    def reference():
        mtt_min, mtt_max = 1000.0, 4000.0
        s = (14 * 10 ** 3) ** 2
        reference.y_min, reference.y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
        x_spacing = 10
        y_spacing = 0.01
        # First set up the figure, the axis, and the plot element we want to animate
        reference.f_ana = ExS.plot_f_ana(mtt_min, mtt_max, reference.y_min, reference.y_max, x_spacing, y_spacing, ctg,
                                         np_order=2)
        reference.f_ana = np.ma.masked_where(reference.f_ana == 1.0, reference.f_ana)

    reference()

    cmap = copy.copy(plt.get_cmap("seismic"))
    cmap.set_bad(color='#c8c9cc')

    fig, ax = plt.subplots()
    img = plt.imshow(np.zeros(reference.f_ana.shape), extent=[1000.0, 4000.0, reference.y_min, reference.y_max],
                     origin='lower', cmap=cmap, aspect=(4000.0 - 1000.0) / (reference.y_max - reference.y_min),
                     interpolation='quadric', vmin=0.8, vmax=1.2)
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('Rapidity y')
    plt.title('NN performance at ctG = {}'.format(ctg))
    epoch_text = ax.text(0.70, 0.95, '', transform=ax.transAxes)
    loss_text = ax.text(0.70, 0.90, '', transform=ax.transAxes)
    loss = np.loadtxt(path + 'loss.out')

    # initialization function: plot the background of each frame
    def init():
        img.set_data(np.zeros(reference.f_ana.shape))
        epoch_text.set_text('')
        loss_text.set_text('')
        return img, epoch_text, loss_text

    # animation function.  This is called sequentially

    bar = Bar('Processing', max=stopping_point)

    def animate(i):
        sys.stdout.write('\r')
        sys.stdout.flush()
        xx, yy, _, _, f_pred, n_alpha_nn, n_alpha_n_beta_nn = make_predictions_2d(
            path + 'trained_nn_{}.pt'.format(i + 1), network_size, train_dataset, quadratic, ctg, make_animation=True)
        img.set_array(reference.f_ana / f_pred)
        epoch_text.set_text('epoch = {}'.format(i))
        loss_text.set_text('loss = {:.4f}'.format(loss[i]))
        bar.next()
        return img, epoch_text, loss_text

    # call the animator.  blit=True means only re-draw the parts that have changed.
    print("Creating the animation")
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=stopping_point, interval=200, blit=True)
    bar.finish()
    anim.save(path + 'animation/training_animation.gif')


def main(path, mc_run, **run_dict):
    trained = run_dict['trained']
    quadratic = run_dict['quadratic']
    n_dat = run_dict['n_dat']
    epochs = run_dict['epochs']
    ctg = run_dict['coeff'][0]['value']
    cuu = run_dict['coeff'][1]['value']
    network_size = [run_dict['input_size']] + run_dict['hidden_sizes'] + [run_dict['output_size']]
    switch_2d = True if run_dict['input_size'] == 2 else False

    # pull = get_pull(network_size, torch.tensor([0]), torch.tensor([1]))
    # print(pull)
    # plot_pull_heatmap(network_size, 1.5)
    # sys.exit()

    if not trained:

        path_dict_eft, path_dict_sm = {}, {}
        n_eft_points = len(eft_points)

        random_sm = np.random.randint(1, 37) #TODO update the upper bound

        for i in range(n_eft_points):
            ctg, cuu = eft_points[i]
            if int(mc_run) < 10:
                path_to_data_eft = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{process}/bin/process_{process}/Events/run_{mc_run}/unweighted_events.lhe'.format(process=i, mc_run=str(0)+mc_run)
            else:
                path_to_data_eft = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{process}/bin/process_{process}/Events/run_{mc_run}/unweighted_events.lhe'.format(process=i, mc_run=mc_run)
            if random_sm < 10:    
                path_to_data_sm = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_18/bin/process_18/Events/run_{random_sm}/unweighted_events.lhe'.format(random_sm=str(0)+str(random_sm))
            else:
                path_to_data_sm = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_18/bin/process_18/Events/run_{random_sm}/unweighted_events.lhe'.format(random_sm=random_sm)
            path_dict_eft[(ctg, cuu)] = path_to_data_eft
            path_dict_sm[(ctg, cuu)] = path_to_data_sm

        c_values = path_dict_eft.keys()

        data_all = [EventDataset(c, path_dict=path_dict_eft, hypothesis=0, n_dat=n_dat) for c in c_values]
        data_all += [EventDataset(c, path_dict=path_dict_sm, hypothesis=1, n_dat=n_dat) for c in c_values]

        mean = np.mean(np.array([dataset.get_mean_std()[0].item() for dataset in data_all]))
        std = np.mean(np.array([dataset.get_mean_std()[1].item() for dataset in data_all]))

        np.savetxt(path + 'scaling.dat', np.array([mean, std]))

        for dataset in data_all:  # TODO can this be shortened?
            dataset.rescale(mean, std)

        data_split = [data.random_split(dataset, [int(len(dataset) / 2), int(len(dataset) / 2)]) for dataset in
                      data_all]
        data_train, data_val = [], []

        for dataset in data_split:
            data_train.append(dataset[0])
            data_val.append(dataset[1])

        train_classifier(path,
                         network_size,
                         data_train,
                         data_val,
                         epochs,
                         quadratic=quadratic,
                         )

    else:
        #mean, std = np.loadtxt(path + '/scaling.dat')
        plot_predictions_1d(path, network_size, ctg, cuu, epochs)


if __name__ == '__main__':
    # read the json run card

    with open(sys.argv[1]) as json_data:
        run_options = json.load(json_data)

    mc_run = sys.argv[2]
    run = run_options['name']

    order = 'quadratic' if run_options['quadratic'] else 'linear'
    path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_{}/mc_run_{}/'.format(run, mc_run)

    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(path + 'plots')
        os.makedirs(path + 'animation')

    # start the training
    main(path, mc_run, **run_options)

    # copy run card to the appropriate folder
    with open(path + 'run_card.json', 'w') as outfile:
        json.dump(run_options, outfile)




