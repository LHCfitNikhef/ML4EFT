# Author: Jaco ter Hoeve
# This file implements the training of the quadratic classifier

# !/usr/bin/env python
# coding: utf-8
import copy
import torch
import torch.utils.data as data
import torch.optim as optim
import pylhe
import numpy as np
import datetime
import json
import os
# matplotlib.use("TkAgg")
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
from torch import nn
import sys
import shutil

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


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


class PredictorLinear(nn.Module):
    """
    Returns the function f(x,c) from the paper (Wulzer et al.) in the linear case
    """

    def __init__(self, architecture):
        super().__init__()
        self.n_alpha = MLP(architecture)

    def forward(self, x, c):
        n_alpha_out = self.n_alpha(x)
        return 1 / (1 + (1 + c * n_alpha_out ** 2))


class PredictorQuadratic(nn.Module):
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

    def __init__(self, c, path_dict, n_dat, hypothesis=0):
        """
        Inputs:
            c - value of the Wilson coefficient
            hypothesis - 0 (False) if EFT and 1 (True) if SM
        """
        super().__init__()

        self.event_data = []
        self.c = c
        self.path_dict = path_dict
        self.hypothesis = hypothesis
        self.n_dat = n_dat

        self.events = None
        self.weights = None
        self.labels = None

        self.standardized = False
        self.mean = None
        self.std = None
        self.min_value = None
        self.max_value = None

        self.load_events()

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

    def lhe_loader(self, path):
        """
        Les Houches Event file reader
        """
        weight = []
        cnt = 0
        for e in pylhe.readLHE(path):
            mtt = self.invariant_mass(e.particles[-1], e.particles[-2])

            if False: #self.switch_2d:
                y = self.rapidity(e.particles[-1], e.particles[-2])
                self.event_data.append([mtt, y])
            else:
                self.event_data.append([mtt])
            weight.append(e.eventinfo.weight)

            cnt += 1
            if cnt == self.n_dat:
                break
        print("Data loaded")
        self.events = torch.tensor(self.event_data)
        self.weights = (torch.tensor(weight)/self.n_dat).unsqueeze(-1)
        self.labels = torch.ones(self.n_dat).unsqueeze(-1) if self.hypothesis else torch.zeros(self.n_dat).unsqueeze(-1)

    def load_events(self):
        """
        Load the datasets (eft and sm) from the les Houches event files.
        """
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


def main(path, mc_run, **run_dict):
    quadratic = run_dict['quadratic']
    n_dat = run_dict['n_dat']
    epochs = run_dict['epochs']
    network_size = [run_dict['input_size']] + run_dict['hidden_sizes'] + [run_dict['output_size']]
    switch_2d = True if run_dict['input_size'] == 2 else False

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

    data_all = [EventDataset(c, path_dict=path_dict_eft, n_dat=n_dat, hypothesis=0) for c in c_values]
    data_all += [EventDataset(c, path_dict=path_dict_sm, n_dat=n_dat, hypothesis=1) for c in c_values]

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


if __name__ == '__main__':
    # read the json run card

    with open(sys.argv[1]) as json_data:
        run_options = json.load(json_data)

    mc_run = sys.argv[2]
    run = run_options['name']

    order = 'quadratic' if run_options['quadratic'] else 'linear'
    path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_{}/mc_run_{}/'.format(run, mc_run)
    # TODO: make the paths more general, or include a warning at least

    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(path + 'plots')
        os.makedirs(path + 'animation')

    # start the training
    main(path, mc_run, **run_options)

    # copy run card to the appropriate folder
    with open(path + 'run_card.json', 'w') as outfile:
        json.dump(run_options, outfile)




