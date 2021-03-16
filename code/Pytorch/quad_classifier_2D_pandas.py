# Author: Jaco ter Hoeve
# This file implements the training of the quadratic classifier

# !/usr/bin/env python
# coding: utf-8
import copy
import glob
from time import sleep

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
from matplotlib import pyplot as plt
from matplotlib import animation
import xsec_cuu as ExS
from torch import nn
from progress.bar import Bar
import sys
import shutil


# print("Using torch", torch.__version__)


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
        self.n_alpha = MLP(architecture)
        self.n_beta = MLP(architecture)

    def forward(self, x, c):
        n_alpha_out = self.n_alpha(x)
        n_beta_out = self.n_beta(x)
        r = (1 + c * n_alpha_out) ** 2 + (c * n_beta_out) ** 2
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

    def __init__(self, path, n_dat, switch_2d, train, quadratic, trained):
        """
        Inputs:
            c - value of the Wilson coefficient
        """
        super().__init__()
        self.train = train
        self.switch_2d = switch_2d
        self.trained = trained
        self.path = path
        self.resc = False
        self.standardized = False
        self.mean = None
        self.std = None
        self.min_value = None
        self.max_value = None
        self.n_dat = n_dat
        self.n_val = None
        self.n_train = None
        self.quadratic = quadratic
        self.data_eft_resc, self.data_sm_resc = {}, {}
        self.data_eft_std, self.data_sm_std = {}, {}
        self.data_eft, self.data_sm = {}, {}
        self.c_values = [-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]  # TODO: raise error when not complete
        # only load data when the model has not been trained yet
        if not self.trained:
            self.load_events()
        # self.find_min_max()
        self.find_mean_std()

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

    def standardize(self):
        """
        Standardize the dataset so that neurons are more likely to have nonzero gradients
        """
        self.standardized = True

        for k, v in self.data_eft.items():
            data_std = (v[0] - self.mean) / self.std
            self.data_eft_std[k] = data_std, v[1], v[2]

        for k, v in self.data_sm.items():
            data_std = (v[0] - self.mean) / self.std
            self.data_sm_std[k] = data_std, v[1], v[2]

    def find_mean_std(self):
        """
        Find the mean and standard deviation of the data and save to disk
        """
        if not self.trained:  # if the nn still has to be trained
            dataset = []
            for c_i in self.c_values:
                dataset.append(torch.cat((self.data_eft['{}'.format(c_i)][0], self.data_sm['{}'.format(c_i)][0])))
            dataset = torch.cat(dataset)
            self.mean = torch.mean(dataset, dim=0)
            self.std = torch.std(dataset, dim=0)

            rescale_factor = torch.stack((self.mean, self.std))
            torch.save(rescale_factor, path + 'rescale.pt')
        else:  # nn has already been trained, load rescale factor
            self.mean, self.std = torch.load(path + 'rescale.pt')

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

    def rescale(self, low, up):
        """
        Rescale the input data to lie in the interval [low, up]
        inputs:
            - min_value.shape = (1, 2)
            - max_value.shape = (1, 2)
        """

        self.resc = True

        for k, v in self.data_eft.items():
            data_resc = low + (up - low) / (self.max_value - self.min_value) * (v[0] - self.min_value)
            self.data_eft_resc[k] = data_resc, v[1], v[2]

        for k, v in self.data_sm.items():
            data_resc = low + (up - low) / (self.max_value - self.min_value) * (v[0] - self.min_value)
            self.data_sm_resc[k] = data_resc, v[1], v[2]

    def lhe_loader(self, path):
        """
        Les Houches Event file reader
        """
        weight = []
        event_data = []
        cnt = 0
        for e in pylhe.readLHE(path):
            mtt = self.invariant_mass(e.particles[-1], e.particles[-2])

            if self.switch_2d:
                y = self.rapidity(e.particles[-1], e.particles[-2])
                event_data.append([mtt, y])
            else:
                event_data.append([mtt])
            weight.append(e.eventinfo.weight)

            cnt += 1
            if cnt == self.n_dat:
                break
        event_data = torch.tensor(event_data)
        weight = torch.tensor(weight)
        return event_data, weight


    def load_events(self):
        """
        Load the datasets (eft and sm) from the les Houches event files.
        """
        print("Loading training data...\n") if self.train is True else print("Loading validation set...\n")

        path_eft_dict = {'-2.0': 'cuu/eft_1.lhe', '-1.0': 'cuu/eft_2.lhe',
                         '-0.5': 'cuu/eft_3.lhe', '0.5': 'cuu/eft_4.lhe', '1.0': 'cuu/eft_5.lhe',
                         '2.0': 'cuu/eft_6.lhe'}
        path_sm_dict = {'-2.0': 'cuu/sm.lhe', '-1.0': 'cuu/sm.lhe',
                        '-0.5': 'cuu/sm.lhe', '0.5': 'cuu/sm.lhe', '1.0': 'cuu/sm.lhe',
                        '2.0': 'cuu/sm.lhe'}

        # set the seed for reproducibility and to make sure the training and validation sets do not overlap
        torch.manual_seed(0)

        print("Loading eft data...\n")
        cnt = 0
        for c, path in path_eft_dict.items():
            print("Progress: {:.2f}".format(cnt / len(path_eft_dict)))
            cnt += 1

            dataset_full, weights_full = self.lhe_loader(path)
            labels_full = torch.zeros(dataset_full.size()[0])

            n_events = dataset_full.size()[0]
            self.n_val = int(0.5 * n_events)
            self.n_train = n_events - self.n_val

            shuffled_indices = torch.randperm(n_events)

            if self.train:
                train_indices = shuffled_indices[:-self.n_val]
                dataset_train = dataset_full[train_indices]
                weights_train = weights_full[train_indices] / self.n_train
                labels_train = labels_full[train_indices]
                self.data_eft[c] = dataset_train, weights_train, labels_train
            else:
                val_indices = shuffled_indices[-self.n_val:]
                dataset_val = dataset_full[val_indices]
                weights_val = weights_full[val_indices] / self.n_val
                labels_val = labels_full[val_indices]
                self.data_eft[c] = dataset_val, weights_val, labels_val
        print("EFT data loaded successfully!\n")

        cnt = 0
        print("Loading sm data...\n")
        for c, path in path_sm_dict.items():
            print("Progress: {:.2f}".format(cnt / len(path_sm_dict)))
            cnt += 1
            dataset_full, weights_full = self.lhe_loader(path)
            labels_full = torch.ones(dataset_full.size()[0])

            n_events = dataset_full.size()[0]
            self.n_val = int(0.5 * n_events)
            self.n_train = n_events - self.n_val

            shuffled_indices = torch.randperm(n_events)

            if self.train:
                train_indices = shuffled_indices[:-self.n_val]
                dataset_train = dataset_full[train_indices]
                weights_train = weights_full[train_indices] / self.n_train
                labels_train = labels_full[train_indices]
                self.data_sm[c] = dataset_train, weights_train, labels_train
            else:
                val_indices = shuffled_indices[-self.n_val:]
                dataset_val = dataset_full[val_indices]
                weights_val = weights_full[val_indices] / self.n_val
                labels_val = labels_full[val_indices]
                self.data_sm[c] = dataset_val, weights_val, labels_val
        print("SM data loaded successfully!")

    def visualize(self):
        f1 = plt.figure()
        f2 = plt.figure()
        ax1 = f1.add_subplot(111)
        ax2 = f2.add_subplot(111)
        mtt = self.data_sm['1.0'][0][:, 0].view(-1).numpy()
        ax2.hist(mtt, bins=1, range=(2000, 2500), label='sm', histtype='step')
        for c in [0.5, 1.0, 2.0]:
            mtt = self.data_eft['{}'.format(c)][0][:, 0].view(-1).numpy()
            y = self.data_eft['{}'.format(c)][0][:, 1].view(-1).numpy()
            ax1.scatter(mtt, y, label='{}'.format(c))
            ax2.hist(mtt, bins = 1, range=(2000, 2500), label='{}'.format(c),histtype='step')

        ax1.set_xlabel(r'$m_{tt}$ (rescaled)')
        ax1.set_ylabel('y (rescaled)')
        ax1.set_xlim(2000, 2500)


        #ax2.set_yscale('log')

        ax1.legend()
        ax2.legend()
        plt.show()

    def __len__(self):
        # Number of data points we have.
        return self.n_train if self.train else self.n_val

    def __getitem__(self, idx):
        """
        Return a tuple (eft, sm) with info on the idx-th data point of the dataset
        Outputs:
            - data tuple: (eft event, sm event)
            - label tuple: label = 0 for the eft, label = 1 for the sm
            - weight tuple: weight per event
        """
        data_tuple = (
            self.data_eft_std['-2.0'][0][idx], self.data_sm_std['-2.0'][0][idx], self.data_eft_std['-1.0'][0][idx],
            self.data_sm_std['-1.0'][0][idx], self.data_eft_std['-0.5'][0][idx], self.data_sm_std['-0.5'][0][idx],
            self.data_eft_std['0.5'][0][idx], self.data_sm_std['0.5'][0][idx], self.data_eft_std['1.0'][0][idx],
            self.data_sm_std['1.0'][0][idx], self.data_eft_std['2.0'][0][idx], self.data_sm_std['2.0'][0][idx])
        weight_tuple = (
            self.data_eft_std['-2.0'][1][idx], self.data_sm_std['-2.0'][1][idx], self.data_eft_std['-1.0'][1][idx],
            self.data_sm_std['-1.0'][1][idx], self.data_eft_std['-0.5'][1][idx], self.data_sm_std['-0.5'][1][idx],
            self.data_eft_std['0.5'][1][idx], self.data_sm_std['0.5'][1][idx], self.data_eft_std['1.0'][1][idx],
            self.data_sm_std['1.0'][1][idx], self.data_eft_std['2.0'][1][idx], self.data_sm_std['2.0'][1][idx])
        label_tuple = (
            self.data_eft_std['-2.0'][2][idx], self.data_sm_std['-2.0'][2][idx], self.data_eft_std['-1.0'][2][idx],
            self.data_sm_std['-1.0'][2][idx], self.data_eft_std['-0.5'][2][idx], self.data_sm_std['-0.5'][2][idx],
            self.data_eft_std['0.5'][2][idx], self.data_sm_std['0.5'][2][idx], self.data_eft_std['1.0'][2][idx],
            self.data_sm_std['1.0'][2][idx], self.data_eft_std['2.0'][2][idx], self.data_sm_std['2.0'][2][idx])

        return data_tuple, weight_tuple, label_tuple


def plot_training_report(train_loss, val_loss, path):


    f = plt.figure()
    plt.plot(np.array(train_loss), label='train')
    plt.plot(np.array(val_loss), label='val')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()
    f.savefig(path + 'plots/loss.pdf')


def training_loop(n_epochs, optimizer, model, train_loader, val_loader, c_values, path):

    loss_list_train, loss_list_val = [], []  # stores the training loss per epoch

    for epoch in range(1, n_epochs + 1):
        loss_train, loss_val = 0.0, 0.0

        # We save the model parameters at the start of each epoch
        torch.save(model.state_dict(), path + 'trained_nn_{}.pt'.format(epoch))

        for (training_data, train_weights, train_labels), (val_data, val_weights, val_labels) in zip(train_loader,
                                                                                                     val_loader):

            train_loss, val_loss = torch.zeros(1), torch.zeros(1)

            # TODO: rewrite using zip function
            for i, train_data in enumerate(training_data):
                c_i = c_values[math.floor(i / 2)]
                label_i = train_labels[i].unsqueeze(1)
                weight_i = train_weights[i].unsqueeze(1)
                output = model(train_data.float(), c_i)
                loss_i = loss_fn(output, label_i, weight_i)
                train_loss += loss_i

            with torch.no_grad():
                for i, val_data in enumerate(val_data):
                    c_i = c_values[math.floor(i / 2)]
                    label_i = val_labels[i].unsqueeze(1)
                    weight_i = val_weights[i].unsqueeze(1)
                    output = model(val_data.float(), c_i)
                    loss_i = loss_fn(output, label_i, weight_i)
                    val_loss += loss_i
                assert val_loss.requires_grad is False

            optimizer.zero_grad()

            train_loss.backward()

            optimizer.step()

            loss_train += train_loss.item()
            loss_val += val_loss.item()

        print('{} Epoch {}, Training loss {}'.format(datetime.datetime.now(), epoch, loss_train / len(train_loader)),
              'Validation loss {}'.format(loss_val / len(val_loader)))

        loss_list_train.append(loss_train / len(train_loader))
        loss_list_val.append(loss_val / len(val_loader))

        np.savetxt(path + 'loss.out', loss_list_train)

    plot_training_report(loss_list_train, loss_list_val, path)


def train_classifier(path, architecture, train_dataset, val_dataset, epochs, quadratic=True):
    model = Predictor_quadratic(architecture) if quadratic else Predictor_linear(architecture)

    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    train_data_loader = data.DataLoader(train_dataset, batch_size=int(train_dataset.__len__()), shuffle=True)
    val_data_loader = data.DataLoader(val_dataset, batch_size=int(val_dataset.__len__()), shuffle=False)

    training_loop(
        n_epochs=epochs,
        optimizer=optimizer,
        model=model,
        train_loader=train_data_loader,
        val_loader=val_data_loader,
        c_values=train_dataset.c_values,
        path=path,
    )


def f_linear(x, n_alpha, ctg):
    f_nn = [1 / (1 + 1 + ctg * n_alpha(x_i.float()).item() ** 2) for x_i in x]
    return np.array(f_nn)


def f_quadratic(x, n_alpha, n_beta, ctg):
    f_nn = [1 / (1 + (1 + ctg * n_alpha(x_i.float()).item()) ** 2 + (ctg * n_beta(x_i.float()).item()) ** 2) for x_i in
            x]
    return np.array(f_nn)


def plot_predictions_1d(network_path, network_size, train_dataset, quadratic, ctg, epochs):
    animate_learning_1d(path, network_size, train_dataset, quadratic, ctg, epochs)

    if quadratic:
        mtt, f_pred, n_alpha_nn, n_alpha_n_beta_nn = make_predictions_1d(network_path + 'trained_nn.pt', network_size,
                                                                         train_dataset, quadratic, ctg)
        n_alpha_n_beta_nn = np.array(n_alpha_n_beta_nn)
    else:
        mtt, f_pred, n_alpha_nn = make_predictions_1d(network_path + 'trained_nn.pt', network_size, train_dataset,
                                                      quadratic, ctg)
    n_alpha_nn = np.array(n_alpha_nn)

    fig = plt.figure()
    mtt_min, mtt_max = 1000, 4000
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])

    # Plot the NN prediction
    ax1.plot(mtt, f_pred, label='NN prediction')

    # Compute the analytic likelihood ratio and plot
    x, y = ExS.plot_likelihood_ratio_1D(mtt_min * 10 ** -3, mtt_max * 10 ** -3, 0, ctg)
    x = np.array(x)
    y = np.array(y)
    ax1.plot(x * 1e3, y, '--', c='red', label='Analytical result')

    plt.ylabel(r'$f\;(m_{tt}, c)$')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    plt.title('NN versus analytical at cuu = {}'.format(ctg))
    plt.legend()

    ax2 = fig.add_axes([0.15, 0.1, 0.75, 0.20])
    ax2.plot(x * 1e3, y / f_pred)
    plt.xlabel(r'$m_{tt}\;[GeV]$')
    plt.ylabel('ana/NN')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim(((y / f_pred).min(), (y / f_pred).max()))

    fig.savefig(network_path + 'plots/NNvsAna_f.pdf')

    # Compare r_NN to r_ana
    # fig = plt.figure()
    # n_alpha_ana = np.array([ExS.n_alpha_ana_1D(mtt_i * 1e-3) for mtt_i in mtt])
    # n_alpha_n_beta_ana = np.array([ExS.n_alpha_n_beta_ana_1D(mtt_i * 1e-3) for mtt_i in mtt])
    # plt.plot(mtt, 1 + 2 * ctg * n_alpha_ana + ctg ** 2 * n_alpha_n_beta_ana, '--', c='red', label='Analytical result')
    # plt.plot(mtt, 1 + 2 * ctg * n_alpha_nn + ctg ** 2 * n_alpha_n_beta_nn, '-', label='NN')
    # plt.legend()
    # plt.title('Likelihood ratio: NN versus analytical at c = {}'.format(ctg))
    # plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    # plt.ylabel(r'$r\;(m_{tt}, c)$')
    #
    # fig.savefig(network_path + 'plots/likelihoodratio_reconstructed.pdf')
    #
    # fig = plt.figure()
    # # Compare n_alpha to alpha
    # n_alpha_ana = np.array([ExS.n_alpha_ana_1D(mtt_i * 1e-3) for mtt_i in mtt])
    # plt.plot(mtt, n_alpha_ana, '--', c='red', label='Analytical result')
    # plt.plot(mtt, n_alpha_nn, '-', label='NN')
    # plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    # plt.ylabel(r'$\alpha(m_{tt})$')
    # plt.legend()
    # plt.title('reconstruction of alpha')
    #
    # fig.savefig(network_path + 'plots/alpha_reconstructed.pdf')
    #
    # fig = plt.figure()
    # # Compare n_alpha**2 + n_beta**2 to alpha**2 + beta**2
    # n_alpha_n_beta_ana = np.array([ExS.n_alpha_n_beta_ana_1D(mtt_i * 1e-3) for mtt_i in mtt])
    # plt.plot(mtt, n_alpha_n_beta_ana, '--', c='red', label='Analytical result')
    # plt.plot(mtt, n_alpha_n_beta_nn, '-', label='NN')
    # plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    # plt.ylabel(r'$\alpha(m_{tt})^2+\beta(m_{tt})^2$')
    # plt.legend()
    # plt.title('reconstruction of alpha and beta')
    #
    # fig.savefig(network_path + 'plots/alpha_beta_reconstructed.pdf')
    #
    # # show r(x,c) as a function of c at fixed mtt and compare analytical and NN
    # fig = plt.figure()
    # n_alpha_ana = ExS.n_alpha_ana_1D(2500 * 1e-3)
    # # n_alpha_nn = n_alpha(1010, train_dataset)
    #
    # n_alpha_n_beta_ana = ExS.n_alpha_n_beta_ana_1D(2500 * 1e-3)
    # # n_beta_nn = n_beta(1010, train_dataset)
    #
    # ctg_range = np.arange(-15, 15, 1)
    # r_ana = 1 + 2 * ctg_range * n_alpha_ana + ctg_range ** 2 * n_alpha_n_beta_ana
    # # print("ana: ", 1 + 2*5*n_alpha_ana + 5**2*n_alpha_n_beta_ana)
    # r_nn = 1 + 2 * ctg_range * n_alpha_nn[15] + ctg_range ** 2 * n_alpha_n_beta_nn[15]
    # # print("NN:", r_nn)
    #
    # plt.plot(ctg_range, r_ana, c='red', label='Ana')
    # plt.plot(ctg_range, r_nn, label='NN')
    # plt.xlabel(r'c')
    # plt.ylabel(r'$r(m_{tt}=2.5, c)$')
    # # plt.scatter(np.array([5, 1 + 2*5*n_alpha_nn + 5**2*n_alpha_n_beta_nn]), c='k')
    # # plt.scatter(np.array([10, 1 + 2*10*n_alpha_nn + 10**2*n_alpha_n_beta_nn]), c='k')
    # # plt.scatter(np.array([15, 1 + 2*15*n_alpha_nn + 15**2*n_alpha_n_beta_nn]), c='k')
    # plt.legend()
    #
    # fig.savefig(network_path + 'plots/ratio_parabola.pdf')
    #

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


def make_predictions_1d(network_path, network_size, train_dataset, quadratic, ctg):
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
    loaded_model.load_state_dict(torch.load(network_path))

    # Set up coordinates and compute f
    mtt_min, mtt_max = 1000, 4000
    mtt = torch.arange(mtt_min, mtt_max, 100).unsqueeze(1)
    # x = -1 + 2 / (train_dataset.max_value - train_dataset.min_value) * (mtt - train_dataset.min_value)
    x = (mtt - train_dataset.mean) / train_dataset.std  # rescale the inputs
    n_alpha_trained = loaded_model.n_alpha
    if quadratic:
        n_beta_trained = loaded_model.n_beta
        f_pred = f_quadratic(x, n_alpha_trained, n_beta_trained, ctg)
        n_alpha = [n_alpha_trained(x_i.float()).item() for x_i in x]
        n_alpha_n_beta = [n_alpha_trained(x_i.float()).item() ** 2 + n_beta_trained(x_i.float()).item() ** 2 for x_i in
                          x]
        return mtt.numpy(), f_pred, n_alpha, n_alpha_n_beta
    else:
        f_pred = f_linear(x, n_alpha_trained, ctg)
        n_alpha = [n_alpha_trained(x_i.float()).item() for x_i in x]
        return mtt.numpy(), f_pred, n_alpha


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


def animate_learning_1d(path, network_size, train_dataset, quadratic, ctg, epochs):


    mtt_min, mtt_max = 1000, 4000
    # First set up the figure, the axis, and the plot element we want to animate
    fig, ax = plt.subplots()
    ax = plt.axes(xlim=(mtt_min, mtt_max), ylim=(0, 1))

    # Compute the analytic likelihood ratio and plot
    x, y = ExS.plot_likelihood_ratio_1D(mtt_min * 10 ** -3, mtt_max * 10 ** -3, 0, ctg)
    x = np.array(x)
    y = np.array(y)
    ax.plot(x * 1e3, y, '--', c='red', label='Analytical result')

    plt.ylabel(r'$f\;(m_{tt}, c)$')
    plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    plt.title('NN versus analytical at cuu = {}'.format(ctg))

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
        x, f_pred, _, _ = make_predictions_1d(path + 'trained_nn_{}.pt'.format(i + 1), network_size, train_dataset,
                                              quadratic, ctg)
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


def main(path, **run_dict):
    trained = run_dict['trained']
    quadratic = run_dict['quadratic']
    n_dat = run_dict['n_dat']
    epochs = run_dict['epochs']
    ctg = run_dict['coeff'][0]['value']
    network_size = [run_dict['input_size']] + run_dict['hidden_sizes'] + [run_dict['output_size']]
    switch_2d = True if run_dict['input_size'] == 2 else False

    train_dataset = EventDataset(path, n_dat, switch_2d, train=True, quadratic=quadratic, trained=trained)
    val_dataset = EventDataset(path, n_dat, switch_2d, train=False, quadratic=quadratic, trained=trained)

    train_dataset.standardize()
    val_dataset.standardize()  # standardize the validation set by the same mean and variance

    #train_dataset.visualize()

    if trained:  # classifier is trained already
        if switch_2d:
            plot_predictions_2d(path, network_size, train_dataset, quadratic, ctg, epochs)
        else:
            plot_predictions_1d(path, network_size, train_dataset, quadratic, ctg, epochs)
    else:
        train_classifier(path,
                         network_size,
                         train_dataset,
                         val_dataset,
                         epochs,
                         quadratic=quadratic,
                         )


if __name__ == '__main__':
    # read the json run card
    with open(sys.argv[1]) as json_data:
        run_options = json.load(json_data)

    order = 'quadratic' if run_options['quadratic'] else 'linear'
    path = 'results/trained_nn/{}/run_{}/'.format(order, run_options['name'])

    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(path + 'plots')
        os.makedirs(path + 'animation')

    # start the training
    main(path, **run_options)

    # copy run card to the appropriate folder
    with open(path + 'run_card.json', 'w') as outfile:
        json.dump(run_options, outfile)




