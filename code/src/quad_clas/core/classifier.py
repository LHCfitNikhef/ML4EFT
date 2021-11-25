# Author: Jaco ter Hoeve
# This file implements the training of the likelihood ratio

# !/usr/bin/env python
# coding: utf-8
import logging
import torch
import torch.utils.data as data
import torch.optim as optim
import numpy as np
import datetime
import json
import os
import time
# matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import rc
from torch import nn
import shutil
import quad_clas.analyse.analyse as analyse

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125

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
        layers += [nn.Linear(layer_sizes[-1], output_size), nn.ReLU()]
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
        return 1 / (1 + (1 + c * n_alpha_out))

class PredictorQuadratic(nn.Module):
    """
        Returns the function f(x,c) from the paper (Wulzer et al.) in the quadratic case
    """

    def __init__(self, architecture):
        super().__init__()
        self.architecture = architecture
        self.n_beta = MLP(architecture)

    def forward(self, x, c, path_lin):
        n_beta_out = self.n_beta(x)
        n_lin = PredictorLinear(self.architecture)
        n_lin.load_state_dict(torch.load(path_lin))

        r = 1 + c * n_lin.n_alpha(x) + c ** 2 * n_beta_out
        return 1 / (1 + r)

class PredictorCross(nn.Module):
    """
        Returns the function f(x,c) from the paper (Wulzer et al.) in the quadratic case
    """

    def __init__(self, architecture):
        super().__init__()
        self.architecture = architecture
        self.n_gamma = MLP(architecture)

    def forward(self, x, c1, c2, path_lin_1, path_lin_2, path_quad_1, path_quad_2):
        n_gamma_out = self.n_gamma(x)

        n_lin_1 = PredictorLinear(self.architecture)
        n_lin_1.load_state_dict(torch.load(path_lin_1))
        n_lin_1_out = n_lin_1.n_alpha(x)

        n_lin_2 = PredictorLinear(self.architecture)
        n_lin_2.load_state_dict(torch.load(path_lin_2))
        n_lin_2_out = n_lin_2.n_alpha(x)

        n_quad_1 = PredictorQuadratic(self.architecture)
        n_quad_1.load_state_dict(torch.load(path_quad_1))
        n_quad_1_out = n_quad_1.n_beta(x)

        n_quad_2 = PredictorQuadratic(self.architecture)
        n_quad_2.load_state_dict(torch.load(path_quad_2))
        n_quad_2_out = n_quad_2.n_beta(x)

        r = 1 + c1 * n_lin_1_out + c2 * n_lin_2_out + c1 ** 2 * n_quad_1_out + c2 ** 2 * n_quad_2_out + c1 * c2 * n_gamma_out

        return 1 / (1 + r)

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

    def event_loader(self, path):

        data = np.load(path)
        if self.n_features == 2:
            events = data[1:self.n_dat + 1, :]
            #events = np.append(events, np.log(events[:, 0]).reshape(-1, 1), axis=1)
        else:
            events = data[1:self.n_dat + 1, 0].reshape(-1, 1)
            np.append(events, np.log(events).reshape(-1, 1), axis=1)
        weights = data[0, 0] * np.ones((events.shape[0], 1))

        self.events = torch.tensor(events)
        self.weights = torch.tensor(weights)# / self.n_dat
        self.labels = torch.ones(self.n_dat).unsqueeze(-1) if self.hypothesis else torch.zeros(self.n_dat).unsqueeze(-1)

        logging.info("Dataset loaded from {}".format(path))

    def load_events(self):
        """
        Load the datasets (eft and sm) from the les Houches event files.
        """
        path_to_sample = self.path_dict[self.c]
        self.event_loader(path_to_sample)


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

class Fitter:

    def __init__(self, json_path, mc_run, output_dir):
        # read the json run card
        with open(json_path) as json_data:
            self.run_options = json.load(json_data)

        self.run = self.run_options['name']
        self.training_report = self.run_options["training_report"]
        self.lr = self.run_options["lr"]
        self.n_batches = self.run_options["n_batches"]
        self.quadratic = self.run_options['quadratic']
        self.cross_term = self.run_options['cross_term']
        self.n_dat = self.run_options['n_dat']
        self.epochs = self.run_options['epochs']
        self.network_size = [self.run_options['input_size']] + self.run_options['hidden_sizes'] + [
            self.run_options['output_size']]
        self.event_data_path = self.run_options['event_data']  # path to training data

        self.eft_dict = self.run_options['coeff']
        self.c1 = self.eft_dict[0]['value']
        self.c2 = self.eft_dict[1]['value']

        self.mc_run = mc_run

        model_path = os.path.join(output_dir, 'model_{}'.format(self.run))
        mc_path = os.path.join(model_path, 'mc_run_{}/'.format(self.mc_run))
        log_path = os.path.join(mc_path, 'logs')

        self.path_dict = {'model': model_path,
                          'mc_path': mc_path,
                          'log_path': log_path}

        if not os.path.exists(mc_path):
            os.makedirs(mc_path)
            os.makedirs(os.path.join(mc_path, 'plots'))
            os.makedirs(os.path.join(mc_path, 'animation'))
            os.makedirs(log_path)

        # single coefficients
        if self.c1 != 0 and self.c2 == 0:
            self.eft_op = self.eft_dict[0]['op']
            self.eft_value = self.c1
        if self.c1 == 0 and self.c2 != 0:
            self.eft_op = self.eft_dict[1]['op']
            self.eft_value = self.c2

        # cross terms
        if self.c1 != 0 and self.c2 != 0:
            self.eft_op = self.eft_dict[0]['op'] + "_" + self.eft_dict[1]['op']
            self.eft_value = self.c1 * self.c2

        # initialise all paths to None, unless we run at pure quadratic or cross term level
        self.path_lin_1 = self.path_lin_2 = self.path_quad_1 = self.path_quad_2 = None

        # for pure quadratic and cross terms only: build the paths to the pretraind models
        if self.quadratic:

            self.path_lin_1 = self.run_options['path_lin_1'].format(self.mc_run)
            self.model = PredictorQuadratic(self.network_size)

        elif self.cross_term:

            self.path_lin_1 = self.run_options['path_lin_1'].format(self.mc_run)
            self.path_lin_2 = self.run_options['path_lin_2'].format(self.mc_run)
            self.path_quad_1 = self.run_options['path_quad_1'].format(self.mc_run)
            self.path_quad_2 = self.run_options['path_quad_2'].format(self.mc_run)



        # build the paths to the eft event data and initialize the right model
        if self.quadratic:
            self.path_dict['eft_data_path'] = 'quad/{eft_coeff}/events_{mc_run}.npy'
            self.model = PredictorQuadratic(self.network_size)
        elif self.cross_term:
            self.path_dict['eft_data_path'] = 'cross_term/{eft_coeff}/events_{mc_run}.npy'
            self.model = PredictorCross(self.network_size)
        else:
            self.path_dict['eft_data_path'] = 'lin/{eft_coeff}/events_{mc_run}.npy'
            self.model = PredictorLinear(self.network_size)


        # create log file with timestamp
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)

        logging.basicConfig(filename=log_path + '/training_{}.log'.format(current_time), level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        logging.info("All directories created, ready to load the data")

        # load the training and validation data
        data_train, data_val = self.load_data()

        # start the training
        self.train_classifier(data_train, data_val)

        # copy run card to the appropriate folder
        with open(mc_path + 'run_card.json', 'w') as outfile:
            json.dump(self.run_options, outfile)

    def load_data(self):

        path_dict_eft, path_dict_sm = {}, {}

        # event files are stored at event_data_path/sm, event_data_path/lin, event_data_path/quad
        # or event_data_path/cross for sm, linear, quadratic (single coefficient) and cross terms respectively
        path_dict_sm[self.eft_value] = os.path.join(self.event_data_path, 'sm/events_{}.npy'.format(self.mc_run))
        path_dict_eft[self.eft_value] = os.path.join(self.event_data_path,
                                                self.path_dict['eft_data_path'].format(eft_coeff=self.eft_op, mc_run=self.mc_run))

        c_values = path_dict_eft.keys()

        # We construct an eft and a sm data set for each value of c in c_values and make a list out of it
        # As of the new version of the code where only the sm and any non-zero point in EFT space are needed
        # as an input, the list seems redundant, but this functionality is kept in case one would like to train
        # on multiple EFT points.

        data_eft = [EventDataset(c, self.network_size[0], path_dict=path_dict_eft, n_dat=self.n_dat, hypothesis=0) for c in
                    c_values]
        data_sm = [EventDataset(c, self.network_size[0], path_dict=path_dict_sm, n_dat=self.n_dat, hypothesis=1) for c in
                   c_values]
        data_all = data_eft + data_sm

        # uncomment below to plot the distribution of the training data
        # fig = plot_data(data_eft, data_sm)  # plot the event data
        # fig.savefig(os.path.join(path, 'plots/training_data.pdf'))

        # determine the mean and std of the feature(s) in our data set
        mean_list = np.array([dataset.get_mean_std()[0].numpy() for dataset in data_all])
        mean = np.mean(mean_list, axis=0)
        std_list = np.array([dataset.get_mean_std()[1].numpy() for dataset in data_all])
        std = np.mean(std_list, axis=0)

        # we save the mean and std to avoid having to reload the data when making predictions
        np.savetxt(self.path_dict['mc_path'] + 'scaling.dat', np.array([mean, std]))

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

        return data_train, data_val

    def train_classifier(self, data_train, data_val):

        # define the optimizer
        optimizer = optim.Adam(self.model.parameters(), lr=self.lr)

        # we use PyTorche's dataloader object to allow for mini-batches. After each epoch, the minibatches reshuffle.
        # we create a dataloader object for each eft point + sm and put them all in one big list called train_data_loader
        # or val_data_loader

        train_data_loader = [
            data.DataLoader(dataset_train, batch_size=int(dataset_train.__len__() / self.n_batches), shuffle=True) for
            dataset_train in data_train]
        val_data_loader = [
            data.DataLoader(dataset_val, batch_size=int(dataset_val.__len__() / self.n_batches), shuffle=False) for
            dataset_val in data_val]

        # call the training loop
        self.training_loop(optimizer=optimizer, train_loader=train_data_loader, val_loader=val_data_loader)

    def training_loop(self, optimizer, train_loader, val_loader):

        path = self.path_dict['mc_path']

        loss_list_train, loss_list_val = [], []  # stores the training loss per epoch

        # we want to be able to keep track of potential over-fitting, so introduce a counter that gets increased
        # by one whenever the the validation loss increases during an epoch
        loss_val_old = 0
        overfit_counter = 0
        patience = 50

        # outer loop that runs over the number of epochs
        iterations = 0
        for epoch in range(1, self.epochs + 1):

            # check for plateau
            if len(loss_list_train) > 10:
                # if the loss after the first epoch queals the latest loss, we reset the weights
                if loss_list_train[1] == loss_list_train[-1]:
                    logging.info("Detected stagant training, reset the weights")
                    self.model.apply(self.weight_reset)

            loss_train, loss_val = 0.0, 0.0

            # We save the model parameters at the start of each epoch
            torch.save(self.model.state_dict(), path + 'trained_nn_{}.pt'.format(epoch))

            # the * denotes the unpacking operator. It passes all the list elements
            # of train_loader as separate arguments to the zip function, e.g f(a[0], a[1]) = f(*a).
            # Here we have zip(DataLoader_1, DataLoader_2, ..) which enables looping over our mini-batches.
            for minibatch in zip(*train_loader):
                train_loss = torch.zeros(1)
                # loop over all the datasets within the minibatch and compute their contribution to the loss
                for i, [event, weight, label] in enumerate(minibatch):
                    if isinstance(self.model, PredictorLinear):
                        output = self.model(event.float(), self.c1 + self.c2)
                    if isinstance(self.model, PredictorQuadratic):
                        output = self.model(event.float(), self.c1 + self.c2, self.path_lin_1)
                    if isinstance(self.model, PredictorCross):
                        output = model(event.float(), self.c1, self.c2, self.path_lin_1, self.path_lin_2, self.path_quad_1,
                                       self.path_quad_2)
                    loss = self.loss_fn(output, label, weight)
                    train_loss += loss

                # do gradient descent after each minibatch. Move to the next epoch when all minibatches are looped over.
                optimizer.zero_grad()
                train_loss.backward()
                optimizer.step()

                loss_train += train_loss.item()

            with torch.no_grad():
                for minibatch in zip(*val_loader):
                    val_loss = torch.zeros(1)
                    for i, [event, weight, label] in enumerate(minibatch):
                        if isinstance(self.model, PredictorLinear):
                            output = self.model(event.float(), self.c1 + self.c2)
                        if isinstance(self.model, PredictorQuadratic):
                            output = self.model(event.float(), self.c1 + self.c2, self.path_lin_1)
                        if isinstance(self.model, PredictorCross):
                            output = self.model(event.float(), self.c1, self.c2, self.path_lin_1, self.path_lin_2, self.path_quad_1,
                                           self.path_quad_2)
                        loss = self.loss_fn(output, label, weight)
                        val_loss += loss
                    assert val_loss.requires_grad is False

                    loss_val += val_loss.item()

            loss_list_train.append(loss_train)
            loss_list_val.append(loss_val)

            training_status = "Epoch {epoch}, Training loss {train_loss}, Validation loss {val_loss}". \
                format(time=datetime.datetime.now(), epoch=epoch, train_loss=loss_train, val_loss=loss_val)
            logging.info(training_status)

            np.savetxt(path + 'loss.out', loss_list_train)
            np.savetxt(path + 'loss_val.out', loss_list_val)

            # in case we reach the maximum number of epochs, save the final state
            if epoch == self.epochs:
                torch.save(self.model.state_dict(), path + 'trained_nn.pt')
                break

            # check whether the network is overfitting by increasing the overfit_counter by one if the
            # validation loss increases during the epoch. If the counter increases for patience epochs straight
            # the training is stopped

            if loss_val > min(loss_list_val) and epoch > 1:
                overfit_counter += 1
            else:
                overfit_counter = 0

            if overfit_counter == patience:
                stopping_point = epoch - patience
                shutil.copyfile(path + 'trained_nn_{}.pt'.format(stopping_point), path + 'trained_nn.pt')
                break

            loss_val_old = loss_val
            iterations += 1

        # produce training report
        if self.training_report:
            logging.info("Finished training, producing training report at {}".format(path + 'plots/training_report/'))
            self.make_training_report(loss_list_train, loss_list_val)
        else:
            logging.info("Finished training")

    def make_training_report(self, train_loss, val_loss):
        """
        Produce a training report

        Parameters
        ----------
        train_loss: numpy.ndarray, shape=(M,)
            Training loss of length M
        val_loss: numpy.ndarray, shape=(M,)
            Validation loss of length M
        """

        training_report_path = self.path_dict['mc_path'] + 'plots/training_report/'
        if not os.path.exists(training_report_path):
            os.makedirs(training_report_path)

        # loss plot
        fig = self.plot_loss(train_loss, val_loss)
        fig.savefig(training_report_path + 'loss.pdf')

        # f accuracy plot
        fig = analyse.coeff_comp_rep(self.path_dict['mc_path'],
                                     self.network_size,
                                     self.c1,
                                     self.c2,
                                     self.quadratic,
                                     self.cross_term)
        fig.savefig(training_report_path + 'performance.pdf')

    def weight_reset(self, m):
        """
        Reset the weights and biases associated with the model ``m``.

        Parameters
        ----------
        m: MLP
            Model of type :py:meth:`MLP <MLP>`.
        """
        if isinstance(m, nn.Linear):
            m.reset_parameters()

    @staticmethod
    def plot_loss(train_loss, val_loss):
        """
        Plot the training and validation loss per epoch

        Parameters
        ----------
        train_loss: numpy.ndarray, shape=(M,)
            Training loss for M epochs
        val_loss: numpy.ndarray, shape=(M,)
            Validation loss for M epochs

        Returns
        -------
        fig
        """

        fig = plt.figure()
        plt.plot(np.array(train_loss[-50:]), label=r'$\rm{Train}$')
        plt.plot(np.array(val_loss[-50:]), label=r'$\rm{Val}$')
        plt.xlabel(r'$\rm{Epochs}$')
        plt.ylabel(r'$\rm{Loss}$')
        plt.legend()
        plt.yscale('log')
        plt.tight_layout()
        return fig

    @staticmethod
    def loss_fn(outputs, labels, w_e):
        #TODO: update documentation
        """
        :param outputs: outputs.shape = (batch_size, 1), output \in (0, 1)
        :param labels: labels.shape = (batch_size, 1), labels \in {0, 1}
        :param w_e: w_e.shape = (batch_size, 1), w_e \in [0, \infty)
        :return: contribution to loss from a sample x ~ pdf(x|H_0,1)
        """

        loss_CE = -(1 - labels) * w_e * torch.log(1 - outputs) - labels * w_e * torch.log(outputs)
        # loss_QC = (1 - labels) * w_e * outputs ** 2 + labels * w_e * (1 - outputs) ** 2

        # add up all the losses in the batch
        return torch.sum(loss_CE, dim=0)

# def preprocessing(data_eft, data_sm):
#
#     from statsmodels.distributions.empirical_distribution import ECDF
#
#     mvh_data = data_eft[0].events[:, 0].numpy()
#
#     median_mvh = np.percentile(mvh_data, 50)
#     spread_mvh = max(np.abs(median_mvh - np.percentile(mvh_data, 84)), np.abs(median_mvh - np.percentile(mvh_data, 16)))
#     mvh_data_rescaled = (mvh_data - median_mvh)/ spread_mvh
#
#     log_mvh_data = np.log(mvh_data)
#     median_log_mvh = np.percentile(log_mvh_data, 50)
#     spread_log_mvh = max(np.abs(median_log_mvh - np.percentile(log_mvh_data, 84)), np.abs(median_log_mvh - np.percentile(log_mvh_data, 16)))
#     log_mvh_data_rescaled = (log_mvh_data - median_log_mvh) / spread_log_mvh
#
#     # overview plots
#     nrows = 3
#     ncols = 2
#     fig = plt.figure(figsize=(ncols * 8, nrows * 6))
#
#     ax = plt.subplot(nrows, ncols, 1)
#
#     mvh_min = np.min(mvh_data) - 0.1
#     mvh_max = np.percentile(mvh_data, 84)
#     ax.hist(mvh_data, bins=np.linspace(mvh_min, 2 * mvh_max, 20), density=False)
#     #ax.set_xlim(mvh_min, 5 * mvh_max)
#     ax.set_xlabel(r'$m_{VH}$')
#
#     ax = plt.subplot(nrows, ncols, 2)
#     mvh_min_resc = np.min(mvh_data_rescaled) - 0.1
#     mvh_max_resc = np.percentile(mvh_data_rescaled, 84)
#     ax.hist(mvh_data_rescaled, bins=np.linspace(mvh_min_resc, 2 * mvh_max_resc, 20), density=False)
#     # ax.set_xlim(mvh_min, 5 * mvh_max)
#     ax.set_xlabel(r'$m_{VH}\;(\rm{rescaled})$')
#
#     ax = plt.subplot(nrows, ncols, 3)
#     ax.hist(np.log(mvh_data), bins=40, density=False)
#     ax.set_xlabel(r'$\log m_{VH}$')
#
#     ax = plt.subplot(nrows, ncols, 4)
#     ax.hist(log_mvh_data_rescaled, bins=40, density=False)
#     ax.set_xlabel(r'$\log m_{VH}\;(\rm{rescaled})$')
#
#     ax = plt.subplot(nrows, ncols, 5)
#     ecdf = ECDF(mvh_data)
#     ax.hist(ecdf.y, bins=50, density=False)
#     ax.set_xlabel(r'$\rm{eCDF}(x)$')
#
#     ax = plt.subplot(nrows, ncols, 6)
#     ecdf = ECDF(mvh_data)
#     ax.hist((ecdf.y - np.mean(ecdf.y))/np.std(ecdf.y), bins=50, density=False)
#     ax.set_xlabel(r'$\rm{eCDF}(x)\;(\rm{rescaled})$')
#     return fig


