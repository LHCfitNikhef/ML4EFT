# Author: Jaco ter Hoeve
# This file implements the training of the quadratic classifier

# !/usr/bin/env python
# coding: utf-8
import torch
import torch.utils.data as data
import torch.optim as optim
import numpy as np
import datetime
import json
import os
# matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import rc
from torch import nn

from . import nn_analyse as analyse
from quad_clas.core.xsec import tt_prod as axs

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


eft_points = [[10, 0]]


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
        return 1 / (1 + (1 + c * n_alpha_out ** 2)) # TODO try without squaring n_alpha


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

    def forward(self, x, c):

        raise NotImplementedError("Quadratic classifier not implemented yet")
        # TODO: write general method for any dimension of c, now only works for 2
        n_12 = self.n_12(x)
        n_13 = self.n_13(x)
        n_22 = self.n_22(x)
        n_23 = self.n_23(x)
        n_33 = self.n_33(x)
        r = (1 + n_12 * ctg + n_13 * cuu) ** 2 + (n_22 * ctg + n_23 * cuu) ** 2 + (n_33 * cuu)**2
        #r = 1 + n_12 ** 2 * ctg + n_13 ** 2 * cuu + n_22 ** 2 * ctg ** 2 + n_23 ** 2 * cuu ** 2 + n_33 ** 2 * cuu * ctg
        return 1 / (1 + r)


def loss_fn(outputs, labels, w_e):
    """
    :param outputs: outputs.shape = (batch_size, 1), output \in (0, 1)
    :param labels: labels.shape = (batch_size, 1), labels \in {0, 1}
    :param w_e: w_e.shape = (batch_size, 1), w_e \in [0, \infty)
    :return: contribution to loss from a sample x ~ pdf(x|H_0,1)
    """

    loss_CE = -(1 - labels) * w_e * torch.log(1 - outputs) - labels * w_e * torch.log(outputs)
    #loss_QC = (1 - labels) * w_e * outputs ** 2 + labels * w_e * (1 - outputs) ** 2
    # add up all the losses in the batch
    return torch.sum(loss_CE, dim=0)


class EventDataset(data.Dataset):

    def __init__(self, c, n_features, path_dict, n_dat, hypothesis=0):
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
        self.n_features = n_features

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

    def event_loader(self, path):

        data = np.load(path)
        if self.n_features == 2:
            events = data[1:self.n_dat + 1, :].reshape(-1, 1) # TODO: not correct shape
        else:
            events = data[1:self.n_dat + 1, 0].reshape(-1, 1)
        weights = data[0, 0] * np.ones(events.shape)

        self.events = torch.tensor(events)
        self.weights = torch.tensor(weights) / self.n_dat
        self.labels = torch.ones(self.n_dat).unsqueeze(-1) if self.hypothesis else torch.zeros(self.n_dat).unsqueeze(-1)

        print("Data loaded")


    def lhe_loader(self, path):
        """
        Les Houches Event file reader
        """
        #weight = []
        cnt = 0
        data = np.load(os.path.join(path, 'event_data.npy'))
        if self.n_features == 2:
            events = data[:self.n_dat, :-1].reshape(-1, 1)
        else:
            events = data[:self.n_dat, 0].reshape(-1, 1)
        weights = data[:self.n_dat, -1].reshape(-1, 1)

        print("mean: ", np.mean(events))
        print("mean + 5 sigma: ", np.mean(events) + 5*np.std(events))

        # for e in pylhe.readLHE(path):
        #     mtt = self.invariant_mass(e.particles[-1], e.particles[-2])
        #     if self.n_features == 2:
        #         y = self.rapidity(e.particles[-1], e.particles[-2])
        #         self.event_data.append([mtt, y])
        #     if self.n_features == 1:
        #         self.event_data.append([mtt])
        #     weight.append(e.eventinfo.weight)
        #
        #     cnt += 1
        #     if cnt == self.n_dat:
        #         break
        print("Data loaded")

        self.events = torch.tensor(events)
        self.weights = torch.tensor(weights)/self.n_dat
        self.labels = torch.ones(self.n_dat).unsqueeze(-1) if self.hypothesis else torch.zeros(self.n_dat).unsqueeze(-1)


    def load_events(self):
        """
        Load the datasets (eft and sm) from the les Houches event files.
        """
        path_to_sample = self.path_dict[self.c]
        self.event_loader(path_to_sample)
        #self.lhe_loader(path_to_sample)

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
        return len(self.events)

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


def plot_training_report(train_loss, val_loss, path, architecture, c):

    # loss plot
    fig = plt.figure()
    plt.plot(np.array(train_loss), label='train')
    plt.plot(np.array(val_loss), label='val')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()
    fig.savefig(path + 'plots/loss.pdf')

    # f accuracy plot

    # First set up the figure, the axis, and the plot element we want to animate
    fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))
    ax = plt.axes(ylim=(0, 1))

    mean, std = np.loadtxt(os.path.join(path, 'scaling.dat'))
    x, f_pred = analyse.make_predictions_1d(path + 'trained_nn.pt', architecture, c, mean, std)
    _, f_ana = axs.plot_likelihood_ratio_1D(0.3, 1.0, c)

    x = np.array(x)
    f_ana = np.array(f_ana)
    ax.plot(x, f_ana, '--', c='red', label=r'$\rm{Truth}$')
    ax.plot(x, f_pred, lw=2, label=r'$\rm{NN}$')
    plt.legend()

    plt.ylabel(r'$f\;(m_{VH}, c)$')
    plt.xlabel(r'$m_{VH}\;[\mathrm{TeV}]$')
    # plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    fig.savefig(path + 'plots/f_perf.pdf')


def training_loop(n_epochs, n_eft_points, eft_points, optimizer, model, train_loader, val_loader, path, architecture, animate):

    loss_list_train, loss_list_val = [], []  # stores the training loss per epoch

    # we want to be able to keep track of potential over-fitting, so introduce a counter that gets increased
    # by one whenever the the validation loss increases during an epoch
    loss_val_old = 0
    overfit_counter = 0
    patience = 20

    # outer loop that runs over the number of epochs
    iterations = 0
    for epoch in range(1, n_epochs + 1):
        loss_train, loss_val = 0.0, 0.0

        # We save the model parameters at the start of each epoch
        torch.save(model.state_dict(), path + 'trained_nn_{}.pt'.format(epoch))

        # the * denotes the unpacking operator. It passes all the list elements
        # of train_loader as separate arguments to the zip function, e.g f(a[0], a[1]) = f(*a).
        # Here we have zip(DataLoader_1, DataLoader_2, ..) which enables looping over our mini-batches.
        for minibatch in zip(*train_loader):
            train_loss = torch.zeros(1)
            # loop over all the datasets within the minibatch and compute their contribution to the loss
            for i, [event, weight, label] in enumerate(minibatch):
                c = sum(eft_points) #eft_points[i % n_eft_points]  # reset the argument to 0 after n_eft_points #TODO: works only for fitting one c at a time.
                output = model(event.float(), c)
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
                    c = eft_points[i % n_eft_points]
                    output = model(event.float(), c)
                    loss = loss_fn(output, label, weight)
                    val_loss += loss
                assert val_loss.requires_grad is False

                loss_val += val_loss.item()

        loss_list_train.append(loss_train)
        loss_list_val.append(loss_val)

        print('{} Epoch {}, Training loss {}'.format(datetime.datetime.now(), epoch, loss_train),
              'Validation loss {}'.format(loss_val))

        np.savetxt(path + 'loss.out', loss_list_train)
        np.savetxt(path + 'loss_val.out', loss_list_val)

        # in case we reach the maximum number of epochs, save the final state
        if epoch == n_epochs:
            torch.save(model.state_dict(), path + 'trained_nn.pt')
            break

        # check whether the network is overfitting by increasing the overfit_counter by one if the
        # validation loss increases during the epoch. If the counter increases for 10 epochs straight,
        # stop the training.

        if loss_val > loss_val_old and epoch > 1:
            overfit_counter += 1

        # if overfit_counter == patience:
        #     stopping_point = epoch - patience
        #     shutil.copyfile(path + 'trained_nn_{}.pt'.format(stopping_point), path + 'trained_nn.pt')
        #     break

        loss_val_old = loss_val
        iterations += 1

    plot_training_report(loss_list_train, loss_list_val, path, architecture, [2,0])

    if animate:
        animate_performance(path, architecture, 2, 0, iterations)


def animate_performance(path, architecture, ctg, cuu, epochs):
    mean, std = np.loadtxt(os.path.join(path, 'scaling.dat'))
    analyse.animate_learning_1d(path, architecture, ctg, cuu, epochs, mean, std)


def train_classifier(path, architecture, data_train, data_val, epochs, quadratic=True, animate=False):

    model = PredictorQuadratic(architecture) if quadratic else PredictorLinear(architecture)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    # set n_batches to the number of mini-batches you want to use
    n_batches = 1
    n_eft_points = len(data_train[0].dataset.c)
    eft_points = data_train[0].dataset.c

    # we use PyTorche's dataloader object to allow for mini-batches. After each epoch, the minibatches reshuffle.
    # we create a dataloader object for each eft point + sm and put them all in one big list train_data_loader (val_data_loader)
    train_data_loader = [data.DataLoader(dataset_train, batch_size=int(dataset_train.__len__()/n_batches), shuffle=True) for dataset_train in data_train]
    val_data_loader = [data.DataLoader(dataset_val, batch_size=int(dataset_val.__len__()/n_batches), shuffle=False) for dataset_val in data_val]

    training_loop(
        n_epochs=epochs,
        n_eft_points=n_eft_points,
        eft_points=eft_points,
        optimizer=optimizer,
        model=model,
        train_loader=train_data_loader,
        val_loader=val_data_loader,
        path=path,
        architecture=architecture,
        animate=animate,
    )

def plot_data(data_eft, data_sm):
    f_0 = data_eft[0].events.numpy().reshape(1, -1)
    f_1 = data_sm[0].events.numpy().reshape(1, -1)

    fig = plt.figure(figsize=(10, 6))
    plt.scatter(f_0, np.zeros(f_0.shape),  label='EFT')
    plt.scatter(f_1, np.ones(f_1.shape), label='SM')
    plt.legend()
    return fig

def main(path, mc_run, **run_dict):

    quadratic = run_dict['quadratic']
    n_dat = run_dict['n_dat']
    epochs = run_dict['epochs']
    network_size = [run_dict['input_size']] + run_dict['hidden_sizes'] + [run_dict['output_size']]
    eft_points = run_dict['coeff']
    event_data_path = run_dict['event_data']

    eft_point = []
    for item in eft_points:
        eft_point.append(item['value'])
        if item['value'] != 0:
            eft_coeff = item['op']
    eft_point = tuple(eft_point)

    path_dict_eft, path_dict_sm = {}, {}
    n_eft_points = len(eft_point)

    eft_data_path = 'quad/{eft_coeff}/events_{mc_run}.npy' if quadratic else 'lin/{eft_coeff}/events_{mc_run}.npy'
    path_dict_sm[eft_point] = os.path.join(event_data_path, 'sm/events_{}.npy'.format(mc_run))
    path_dict_eft[eft_point] = os.path.join(event_data_path, eft_data_path.format(eft_coeff=eft_coeff, mc_run=mc_run))#'/Users/jaco/Documents/ML4EFT/data/events/linear_cHW/events_0.npy'

    c_values = path_dict_eft.keys()

    # we construct an eft and a sm data set for each value of c in c_values and make a list out of it
    data_eft = [EventDataset(c, network_size[0], path_dict=path_dict_eft, n_dat=n_dat, hypothesis=0) for c in c_values]
    data_sm = [EventDataset(c, network_size[0], path_dict=path_dict_sm, n_dat=n_dat, hypothesis=1) for c in c_values]
    data_all = data_eft + data_sm

    fig = plot_data(data_eft, data_sm)  # plot the event data
    fig.savefig(os.path.join(path, 'plots/training_data.pdf'))

    # determine the mean and std of the feature(s) in our data set
    mean_list = np.array([dataset.get_mean_std()[0].numpy() for dataset in data_all])
    mean = np.mean(mean_list, axis=0)
    std_list = np.array([dataset.get_mean_std()[1].numpy() for dataset in data_all])
    std = np.mean(std_list, axis=0)

    # we save the mean and std to avoid having to reload the data when making predictions
    np.savetxt(path + 'scaling.dat', np.array([mean, std]))

    # rescale the training data to increase the learning speed
    for dataset in data_all:
        dataset.rescale(mean, std)

    # split each data set in training (50%) and validation (50%).
    data_split = [data.random_split(dataset, [int(len(dataset) / 2), int(len(dataset) / 2)]) for dataset in
                  data_all]

    # collect all the training and validation sets
    data_train, data_val = [], []
    for dataset in data_split:
        data_train.append(dataset[0])
        data_val.append(dataset[1])

    # start the training
    train_classifier(path,
                     network_size,
                     data_train,
                     data_val,
                     epochs,
                     quadratic=quadratic,
                     animate=run_dict['animation']
                     )

def start(json_path, mc_run, output_dir):
    # read the json run card
    with open(json_path) as json_data:
        run_options = json.load(json_data)

    run = run_options['name']
    model_path = os.path.join(output_dir, 'model_{}'.format(run))
    mc_path = os.path.join(model_path, 'mc_run_{}/'.format(mc_run))

    if not os.path.exists(mc_path):
        os.makedirs(mc_path)
        os.makedirs(os.path.join(mc_path, 'plots'))
        os.makedirs(os.path.join(mc_path, 'animation'))

    # start the training
    main(mc_path, mc_run, **run_options)

    # copy run card to the appropriate folder
    with open(mc_path + 'run_card.json', 'w') as outfile:
        json.dump(run_options, outfile)
