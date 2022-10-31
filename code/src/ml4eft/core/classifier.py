""" Binary classifier module

"""

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
import pandas as pd
from joblib import dump, load

from matplotlib import pyplot as plt
from matplotlib import rc
from torch import nn
from sklearn.model_selection import train_test_split
import shutil
import ml4eft.analyse.analyse as analyse
from sklearn.preprocessing import StandardScaler, RobustScaler, QuantileTransformer
import joblib
import sys

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=True)


class MLP(nn.Module):
    """ Multi Layer Perceptron that serves as building block for the binary classifier

    """

    def __init__(self, architecture):
        """

        Parameters
        ----------
        architecture: array_like
            ``(N, ) ndarray`` that specifies the MLP's architecture as the number of input nodes followed
            by the number of hidden nodes in each consecutive hidden layer. The last entry must corespond
            to the number of output units.
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
            *layers)

    def forward(self, x):
        """
        Performs a forward pass of the MLP

        Parameters
        ----------
        x: array_like
            Input ``(N, ) torch.Tensor`` with ``N`` the number of input nodes

        Returns
        -------
        out: torch.Tensor

        """
        out = self.layers(x)
        return out


class CustomActivationFunction(nn.Module):
    """
    Class to construct custom activation functions
    """

    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.config = {"name": self.name}


class ConstraintActivation(CustomActivationFunction):
    """Class to transform the classifier output to ensure a positive likelihood ratio

    """

    def __init__(self, c):
        """

        Parameters
        ----------
        c: float
            Traning parameter :math:`c^{(\mathrm{tr})}` at which the EFT data set is generated
        """
        super().__init__()
        self.c = c

    def forward(self, x):
        if self.c > 0:
            return torch.relu(x) - 1 / self.c + 1e-6
        else:

            return - torch.relu(x) - 1 / self.c - 1e-6


class Classifier(nn.Module):
    """ The decssion function :math:`g(x, c)`

    Implementation of the decision boundary `g(x, c)`
    """

    def __init__(self, architecture, c):
        super().__init__()
        self.c = c
        self.n_alpha = MLP(architecture)
        self.n_alpha.layers.add_module('constraint', ConstraintActivation(self.c))

    def forward(self, x):
        """

        Parameters
        ----------
        x: array_like
            Input ``(N, ) torch.Tensor`` with ``N`` the number of input nodes

        Returns
        -------
        g: Torch.Tensor
            decision boundary between two

        """

        NN_out = self.n_alpha(x)
        g = 1 / (1 + (1 + self.c * NN_out))
        return g


class PreProcessing():
    """
    A feature preprocessor and data loader
    """

    def __init__(self, fitter, path):
        """

        Parameters
        ----------
        fitter: :py:class:`Fitter <ml4eft.core.classifier.Fitter>`
            Fitter object
        path: dict
            Dictionary with paths to the SM and EFT dataset, e.g:
            :code:`{'sm': <path_to_sm_dataset>, 'eft': <path_to_eft_dataset>}`
        """

        self.path = path

        if fitter.scaler_type == 'robust':
            self.scaler = RobustScaler(quantile_range=(5, 95))
        elif fitter.scaler_type == 'standardise':
            self.scaler = StandardScaler()
        else:
            self.scaler = QuantileTransformer(n_quantiles=1000, output_distribution='normal')

        self.load_data(fitter)

    def load_data(self, fitter):
        """
        Loads ``pandas.DataFrame`` into SM and EFT dataframes.
        """
        # sm

        df_sm_full = pd.read_pickle(self.path['sm'], compression="infer")
        df_sm_wo_xsec = df_sm_full.iloc[1:, :]

        # cross section before cuts
        self.xsec_sm = df_sm_full.iloc[0, 0]
        self.df_sm = df_sm_wo_xsec.sample(fitter.n_dat)

        # eft
        df_eft_full = pd.read_pickle(self.path['eft'], compression="infer")
        df_eft_wo_xsec = df_eft_full.iloc[1:, :]

        # cross section before cuts
        self.xsec_eft = df_eft_full.iloc[0, 0]
        self.df_eft = df_eft_wo_xsec.sample(fitter.n_dat)

    def feature_scaling(self, fitter, scaler_path):
        """

        Parameters
        ----------
        fitter: :py:class:`Fitter <ml4eft.core.classifier.Fitter>`
            Fitter object
        scaler_path: string
            Path to where preprocessing scaler must be saved
        Returns
        -------
        df_sm_scaled : pandas.DataFrame
            Rescaled SM events

        df_eft_scaled : pandas.DataFrame
            Rescaled EFT events
        """

        df = pd.concat([self.df_sm, self.df_eft])

        # fit the scaler transformer to the eft and sm features
        self.scaler.fit(df[fitter.features])

        # rescale the sm and eft data
        features_sm_scaled = self.scaler.transform(self.df_sm[fitter.features])
        features_eft_scaled = self.scaler.transform(self.df_eft[fitter.features])

        # convert transformed features to dataframe
        df_sm_scaled = pd.DataFrame(features_sm_scaled, columns=fitter.features)
        df_eft_scaled = pd.DataFrame(features_eft_scaled, columns=fitter.features)

        # save the scaler
        joblib.dump(self.scaler, scaler_path)

        return df_sm_scaled, df_eft_scaled


class EventDataset(data.Dataset):
    """
    Event loader
    """

    def __init__(self, df, xsec, path, n_dat, features, hypothesis=0):
        """
        EventDataset constructor

        Parameters
        ----------
        df: pandas.DataFrame
            Event DataFrame
        xsec: float
            inclusive cross-section
        path: str
            Path to dataset
        n_dat: int
            Number of data points
        features: array_like
            List of features to train on
        hypothesis: int
            0 for EFT and 1 for SM

        """
        super().__init__()

        self.df = df
        self.xsec = xsec
        self.hypothesis = hypothesis
        self.features = features

        self.events = None
        self.weights = None
        self.labels = None

        self.event_loader(path)

    def event_loader(self, path):
        """
        Set the weights of the evevnts, labels and convert the events to torch.Tensor,

        Parameters
        ----------
        path: str
            Path to dataset
        """
        n_dat = len(self.df)

        self.weights = self.xsec * torch.ones(n_dat).unsqueeze(-1)
        self.events = torch.tensor(self.df[self.features].values)
        self.labels = torch.ones(n_dat).unsqueeze(-1) if self.hypothesis else torch.zeros(n_dat).unsqueeze(-1)

        logging.info("Dataset loaded from {}".format(path))

    def __len__(self):
        return len(self.events)

    def __getitem__(self, idx):
        data_sample, weight_sample, label_sample = self.events[idx], self.weights[idx], self.labels[idx]
        return data_sample, weight_sample, label_sample


class Fitter:
    """
    Training class
    """

    def __init__(self, json_path, mc_run, c_name, output_dir, print_log=False):
        """
        Fitter constructor

        Parameters
        ----------
        json_path: str
            Path to json run card
        mc_run: int
            Replica number
        c_name: str
            EFT coefficient for which to learn the ratio function
        output_dir: str
            Path to where the models should be stored
        print_log: bool, optional
            Set to true to print training progress to stdout, otherwise it
            prints to a log file only
        """
        # read the json run card
        with open(json_path) as json_data:
            self.run_options = json.load(json_data)

        self.c_name = c_name
        self.process_id = self.run_options["process_id"]
        self.lr = self.run_options["lr"]
        self.n_batches = self.run_options["n_batches"]

        self.loss_type = self.run_options['loss_type']
        self.scaler_type = self.run_options['scaler_type']
        self.patience = self.run_options['patience']
        self.val_ratio = self.run_options['val_ratio']

        self.c_train = self.run_options["c_train"]

        self.n_dat = self.run_options['n_dat']
        self.epochs = self.run_options['epochs']
        self.features = self.run_options['features']
        self.network_size = [len(self.features)] + self.run_options['hidden_sizes'] + [
            self.run_options['output_size']]
        self.event_data_path = self.run_options['event_data']  # path to training data

        self.quadratic = True if '_' in self.c_name else False
        if self.quadratic:
            c1, c2 = self.c_name.split('_')
            self.c_train_value = self.c_train[c1] * self.c_train[c2]
        else:
            self.c_train_value = self.c_train[self.c_name]

        self.mc_run = mc_run

        output_dir = os.path.join(output_dir, time.strftime("%Y/%m/%d"))
        os.makedirs(output_dir, exist_ok=True)

        model_path = os.path.join(output_dir, 'model_{}'.format(self.c_name))
        mc_path = os.path.join(model_path, 'mc_run_{}/'.format(self.mc_run))
        log_path = os.path.join(mc_path, 'logs')

        self.path_dict = {'model': model_path,
                          'mc_path': mc_path,
                          'log_path': log_path}

        self.scaler = None

        if not os.path.exists(mc_path):
            os.makedirs(mc_path)
            os.makedirs(log_path)

        # initialise all paths to None, unless we run at pure quadratic or cross term level
        self.path_lin_1 = self.path_lin_2 = self.path_quad_1 = self.path_quad_2 = None

        # build the paths to the eft event data and initialize the right model
        if self.quadratic:
            self.path_dict['eft_data_path'] = '{eft_coeff}/events_{mc_run}.pkl.gz'
            self.model = Classifier(self.network_size, self.c_train_value)
        else:  # linear
            self.path_dict['eft_data_path'] = '{eft_coeff}/events_{mc_run}.pkl.gz'
            self.model = Classifier(self.network_size, self.c_train_value)

        # create log file with timestamp
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)

        # print log to stdout when print_log is True, else only save to log file
        if print_log:
            handlers = [logging.FileHandler(log_path + '/training_{}.log'.format(current_time)),
                        logging.StreamHandler(sys.stdout)
                        ]
        else:
            handlers = [logging.FileHandler(log_path + '/training_{}.log'.format(current_time))]

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=handlers
        )

        logging.info("All directories created, ready to load the data")

        # load the training and validation data
        data_train, data_val = self.load_data()

        # copy run card to the appropriate folder
        with open(mc_path + 'run_card.json', 'w') as outfile:
            json.dump(self.run_options, outfile)

        # start the training
        self.train_classifier(data_train, data_val)

    def load_data(self):
        """
        Constructs training and validation sets

        Returns
        -------
        data_train: array_like
            Training data set
        data_val: array_like
            Validation data set
        """

        # event files are stored at event_data_path/sm, event_data_path/lin, event_data_path/quad
        # or event_data_path/cross for sm, linear, quadratic (single coefficient) and cross terms respectively
        path_sm = os.path.join(self.event_data_path, self.process_id + '_sm/events_{}.pkl.gz'.format(self.mc_run))
        path_eft = os.path.join(self.event_data_path,
                                self.process_id + '_' + self.path_dict['eft_data_path'].format(eft_coeff=self.c_name,
                                                                                               mc_run=self.mc_run))

        path_dict = {'sm': path_sm, 'eft': path_eft}

        # preprocessing of the data
        preproc = PreProcessing(self, path_dict)

        # save the scaler
        scaler_path = os.path.join(self.path_dict['mc_path'], 'scaler.gz')
        df_sm_scaled, df_eft_scaled = preproc.feature_scaling(self, scaler_path)

        self.n_dat = min(len(df_eft_scaled), len(df_sm_scaled))

        # construct an eft and a sm data set for each value of c in c_values and make a list out of it
        data_eft = EventDataset(df_eft_scaled,
                                xsec=preproc.xsec_eft,
                                path=path_eft,
                                n_dat=self.n_dat,
                                features=self.features,
                                hypothesis=0)

        data_sm = EventDataset(df_sm_scaled,
                               xsec=preproc.xsec_sm,
                               path=path_sm,
                               n_dat=self.n_dat,
                               features=self.features,
                               hypothesis=1)

        data_all = [data_eft, data_sm]

        # split each data set in training and validation
        data_split = []
        for dataset in data_all:
            n_val_points = int(self.val_ratio * len(dataset))
            n_train_points = len(dataset) - n_val_points
            data_split.append(data.random_split(dataset, [n_train_points, n_val_points]))

        # collect all the training and validation sets
        data_train, data_val = [], []
        for dataset in data_split:
            data_train.append(dataset[0])
            data_val.append(dataset[1])

        return data_train, data_val

    def train_classifier(self, data_train, data_val):
        """
        Starts the training of the binary classifier

        Parameters
        ----------
        data_train: array_like
            Traning data set
        data_val: array_like
            Validation data set
        """
        # define the optimizer
        optimizer = optim.AdamW(self.model.parameters(), lr=self.lr)

        # Use PyTorche's DataLoader to allow for mini-batches. After each epoch, the minibatches reshuffle.
        # Create a dataloader object for each eft point + sm and put them all in one big list called train_data_loader
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
        """
        Optimize the classifier with `optimizer` on the training data set `train_loader`. Keeps track of potential
        overfitting through `val_loader`.

        Parameters
        ----------
        optimizer: torch.optim
            Optimizer, e.g. torch.optim.AdamW
        train_loader: array_like
            List of torch.utils.data.DataLoader objects, one for the SM and the EFT (training)
        val_loader: array_like
            List of torch.utils.data.DataLoader objects, one for the SM and the EFT (validation)
        """
        path = self.path_dict['mc_path']

        loss_list_train, loss_list_val = [], []  # stores the training loss per epoch

        # To be able to keep track of potential over-fitting, introduce a counter that gets increased
        # by one whenever the the validation loss increases during an epoch
        overfit_counter = 0

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

            # compute validation loss
            with torch.no_grad():
                for minibatch in zip(*val_loader):
                    val_loss = torch.zeros(1)
                    for i, [event, weight, label] in enumerate(minibatch):
                        if isinstance(self.model, Classifier):
                            output = self.model(event.float())

                        loss = self.loss_fn(output, label, weight)
                        val_loss += loss
                    assert val_loss.requires_grad is False

                    loss_val += val_loss.item()

            # loop over the mini-batches.
            for j, minibatch in enumerate(zip(*train_loader)):
                train_loss = torch.zeros(1)
                # loop over all the datasets within the minibatch and compute their contribution to the loss
                for i, [event, weight, label] in enumerate(minibatch):  # i=0: eft, i=1: sm
                    if isinstance(self.model, Classifier):
                        output = self.model(event.float())

                    loss = self.loss_fn(output, label, weight)
                    train_loss += loss

                # perform gradient descent after each minibatch. Move to the next epoch when all minibatches are looped over.
                optimizer.zero_grad()
                train_loss.backward()
                optimizer.step()

                loss_train += train_loss.item()

            loss_list_train.append(loss_train)
            loss_list_val.append(loss_val)

            training_status = "Epoch {epoch}, Training loss {train_loss}, Validation loss {val_loss}, Overfit counter = {overfit}". \
                format(time=datetime.datetime.now(), epoch=epoch, train_loss=loss_train, val_loss=loss_val,
                       overfit=overfit_counter)
            logging.info(training_status)

            np.savetxt(path + 'loss.out', loss_list_train)
            np.savetxt(path + 'loss_val.out', loss_list_val)

            # in case the maximum number of epochs is reached, save the final state
            if epoch == self.epochs:
                torch.save(self.model.state_dict(), path + 'trained_nn.pt')
                break

            # check whether the network is overfitting by increasing the overfit_counter by one if the
            # validation loss increases during the epoch.
            if epoch > 20:
                if loss_val > min(loss_list_val):
                    overfit_counter += 1
                else:
                    overfit_counter = 0

            if overfit_counter == self.patience:
                stopping_point = epoch - self.patience
                logging.info("Stopping point reached! Overfit counter = {}".format(overfit_counter))
                shutil.copyfile(path + 'trained_nn_{}.pt'.format(stopping_point), path + 'trained_nn.pt')
                logging.info("Backwards stopping done")
                break

            loss_val_old = loss_val
            iterations += 1

        logging.info("Finished training")

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

    def loss_fn(self, outputs, labels, w_e):
        """
        Loss function

        Parameters
        ----------
        outputs: torch.Tensor
            Output of the decision function
        labels: torch.Tensor
            Classification labels
        w_e: torch.Tensor
            Event weights

        Returns
        -------
        torch.Tensor
            Average loss of the mini-batch
        """
        if self.loss_type == 'CE':

            loss = - (1 - labels) * w_e * torch.log(1 - outputs) - labels * w_e * torch.log(outputs)

        elif self.loss_type == 'QC':
            loss = (1 - labels) * w_e * outputs ** 2 + labels * w_e * (1 - outputs) ** 2

        # average over all the losses in the batch
        return torch.mean(loss, dim=0)
