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
import pathlib

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

    def forward(self, x, c1, c2):
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


# class Classifier(nn.Module):
#     """ The decssion function :math:`g(x, c)`
#
#     Implementation of the decision boundary `g(x, c)`
#     """
#
#     def __init__(self, architecture):
#         super().__init__()
#
#         self.NN1 = MLP(architecture)
#         self.NN2 = MLP(architecture)
#         self.NN11 = MLP(architecture)
#         self.NN22 = MLP(architecture)
#
#     def forward(self, x, c1, c2):
#         """
#
#         Parameters
#         ----------
#         x: array_like
#             Input ``(N, ) torch.Tensor`` with ``N`` the number of input nodes
#
#         Returns
#         -------
#         g: Torch.Tensor
#             decision boundary between two
#
#         """
#
#         NN1_out = self.NN1(x)
#         #NN2_out = self.NN2(x)
#
#         #NN11_out = self.NN11(x)
#         #NN22_out = self.NN22(x)
#
#         #r = torch.relu(1 + c1 * NN1_out + c2 * NN2_out ** 2 + c1 ** 2 * NN11_out + c2 ** 2 * NN22_out ** 2)
#         #r = torch.relu(1 + c1 * NN1_out + c1 ** 2 * NN11_out)
#
#
#
#         r = 1 + c1 * NN1_out
#
#         g = 1 / (1 + r)
#         return g


class PreProcessing():
    """
    A feature preprocessor and data loader
    """

    def __init__(self, fitter):
        """

        Parameters
        ----------
        fitter: :py:class:`Fitter <ml4eft.core.classifier.Fitter>`
            Fitter object
        path: dict
            Dictionary with paths to the SM and EFT dataset, e.g:
            :code:`{'sm': <path_to_sm_dataset>, 'eft': <path_to_eft_dataset>}`
        """

        if fitter.scaler_type == 'robust':
            self.scaler = RobustScaler(quantile_range=(5, 95))
        elif fitter.scaler_type == 'standardise':
            self.scaler = StandardScaler()
        else:
            self.scaler = QuantileTransformer(n_quantiles=1000, output_distribution='normal')

    def preprocess(self, fitter, scaler_path):
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

        datasets_all = [dataset for dataset in fitter.path_df['data']]
        df = pd.concat(datasets_all)

        # fit the scaler transformer to the eft and sm features
        self.scaler.fit(df[fitter.features])

        n_val_points = int(fitter.val_ratio * fitter.n_dat)
        n_train_points = fitter.n_dat - n_val_points

        # rescale the sm and eft data
        data_train, data_val = [], []

        for _, row in fitter.path_df[['data', 'xsec', 'wc_val']].iterrows():
            hypothesis = 1 if sum(row['wc_val']) == 0 else 0

            events_scaled = self.scaler.transform(row['data'][fitter.features])
            df_scaled = pd.DataFrame(events_scaled, columns=fitter.features)
            event_dataset = EventDataset(df_scaled, row['xsec'], hypothesis)

            train, val = data.random_split(event_dataset, [n_train_points, n_val_points])

            training_loader = data.DataLoader(train, batch_size=int(len(train) / fitter.n_batches), shuffle=True)
            validation_loader = data.DataLoader(val, batch_size=int(len(val) / fitter.n_batches), shuffle=True)

            # TODO: len(training_loader) != self.n_batches

            data_train.append(training_loader)
            data_val.append(validation_loader)

        fitter.path_df['data_train'] = data_train
        fitter.path_df['data_val'] = data_val

        # save the scaler
        joblib.dump(self.scaler, scaler_path)

        return fitter.path_df


class EventDataset(data.Dataset):
    """
    Event loader
    """

    def __init__(self, df, xsec, hypothesis):
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

        self.events = torch.tensor(df.values)
        self.n_dat = len(self.events)
        self.weights = xsec * torch.ones(self.n_dat).unsqueeze(-1)
        self.labels = torch.ones(self.n_dat).unsqueeze(-1) if hypothesis else torch.zeros(self.n_dat).unsqueeze(-1)

    def __len__(self):
        return len(self.events)

    def __getitem__(self, idx):
        data_sample, weight_sample, label_sample = self.events[idx], self.weights[idx], self.labels[idx]
        return data_sample, weight_sample, label_sample


class Fitter:
    """
    Training class
    """

    def __init__(self, json_path, mc_run, print_log=False):
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
        self.network_size = [len(self.features)] + self.run_options['hidden_sizes'] + [1]
        self.event_data_path = pathlib.Path(self.run_options['event_data'])  # path to training data
        self.result_path = pathlib.Path(self.run_options["result_path"])

        self.mc_run = mc_run
        self.scaler = None

        self.output_dir, self.log_path = self.set_folder_structure()
        self.path_df = self.get_path_df()

        # create log file with timestamp
        t = time.localtime()
        current_time = time.strftime("%H_%M_%S", t)

        # print log to stdout when print_log is True, else only save to log file
        if print_log:
            handlers = [logging.FileHandler(self.log_path / 'training_{}.log'.format(current_time)),
                        logging.StreamHandler(sys.stdout)
                        ]
        else:
            handlers = [logging.FileHandler(self.log_path / 'training_{}.log'.format(current_time))]

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=handlers
        )

        logging.info("All directories created, ready to load the data")

        # load the training and validation data
        self.load_data()

        # copy run card to the appropriate folder
        with open(self.output_dir / 'run_card.json', 'w') as outfile:
            json.dump(self.run_options, outfile)

        # initialise model and start the training
        self.model = Classifier(self.network_size, -10)
        self.train_classifier()

    def set_folder_structure(self):

        output_dir = self.result_path / self.run_options["run_id"] / "mc_run_{}".format(self.mc_run)
        output_dir.mkdir(parents=True, exist_ok=True)

        log_path = output_dir / "log"
        log_path.mkdir(parents=True, exist_ok=True)

        return output_dir, log_path

    def get_path_df(self):

        path_sm = self.event_data_path / 'sm' / 'events_{}.pkl.gz'.format(self.mc_run)
        paths = [[[0, 0], path_sm]]

        for c_train, c_vals in self.c_train.items():
            for i, c_val in enumerate(c_vals):
                paths.append([c_val, self.event_data_path / '{}'.format(c_train) / '{}_{}'.format(c_train,
                                                                                                      i) / 'events_{}.pkl.gz'.format(
                    self.mc_run)])
                
        df = pd.DataFrame(paths, columns=['wc_val', 'paths'])
        return df

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
        events, xsec = [], []
        for path in self.path_df['paths']:
            dataset = pd.read_pickle(path, compression="infer")
            events.append(dataset.iloc[1:].sample(self.n_dat))
            xsec.append(dataset.iloc[0,0])
        self.path_df['data'] = events
        self.path_df['xsec'] = xsec

        # preprocessing of the data
        preprocessor = PreProcessing(self)
        scaler_path = self.output_dir / 'scaler.gz'
        self.path_df = preprocessor.preprocess(self, scaler_path)

    def train_classifier(self):
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
        self.model.apply(self.weight_reset)

        # path = self.path_dict['mc_path']

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
                    logging.info("Detected stagnant training, reset the weights")
                    self.model.apply(self.weight_reset)

            loss_train, loss_val = 0.0, 0.0

            # We save the model parameters at the start of each epoch
            torch.save(self.model.state_dict(), self.output_dir / 'trained_nn_{}.pt'.format(epoch))
                        
            with torch.no_grad():
                for n_minibatch, minibatch in enumerate(zip(*self.path_df['data_val'])):
                    val_loss = torch.zeros(1)
                    event_sm, weight_sm, label_sm = minibatch[0]
                    for i, [event, weight, label] in enumerate(minibatch[1:]):

                        c_val = self.path_df['wc_val'][i+1]
                        print("{}, WC {}, Minibatch {}".format(i+1, c_val, n_minibatch))
                        g_eft = self.model(event.float(), *c_val)
                        g_sm = self.model(event_sm.float(), *c_val)

                        # NN = (((1 - g_eft) / g_eft) - 1) / 100
                        # print(NN.mean())

                        loss_eft = self.loss_fn(g_eft, label, weight)
                        loss_sm = self.loss_fn(g_sm, label_sm, weight_sm)
                        val_loss += loss_eft
                        val_loss += loss_sm
                    assert val_loss.requires_grad is False
                    loss_val += val_loss.item()

            for n_minibatch, minibatch in enumerate(zip(*self.path_df['data_train'])):
                train_loss = torch.zeros(1)
                event_sm, weight_sm, label_sm = minibatch[0]
                for i, [event, weight, label] in enumerate(minibatch[1:]):
                    c_val = self.path_df['wc_val'][i + 1]

                    # print("{}, WC {}, Minibatch {}".format(i, c_val, n_minibatch))
                    g_eft = self.model(event.float(), *c_val)
                    g_sm = self.model(event_sm.float(), *c_val)

                    loss_eft = self.loss_fn(g_eft, label, weight)
                    loss_sm = self.loss_fn(g_sm, label_sm, weight_sm)
                    train_loss += loss_eft
                    train_loss += loss_sm

                optimizer.zero_grad()
                train_loss.backward()
                optimizer.step()

                loss_train += train_loss.item()

            loss_list_train.append(loss_train)
            loss_list_val.append(loss_val)

            training_status = "Epoch {epoch}, loss_tr {train_loss}, loss_val {val_loss}, Overfit counter = {overfit}". \
                format(time=datetime.datetime.now(), epoch=epoch,
                       train_loss=loss_train / self.n_batches,
                       val_loss=loss_val / self.n_batches,
                       overfit=overfit_counter)
            logging.info(training_status)


            #np.savetxt(path + 'loss.out', loss_list_train)
            #np.savetxt(path + 'loss_val.out', loss_list_val)

            # in case the maximum number of epochs is reached, save the final state
            if epoch == self.epochs:
                torch.save(self.model.state_dict(), self.output_dir / 'trained_nn.pt')
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

    def weight_reset(self, m):
        """
        Reset the weights and biases associated with the model ``m``.

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
            r = (1 - outputs) / outputs
            lagrange_mp = 50

            loss = (1 - labels) * w_e * outputs ** 2 + labels * w_e * (1 - outputs) ** 2 #+ lagrange_mp * torch.relu(-r) ** 2

        elif self.loss_type == 'direct':
            loss = -(1 - labels) * w_e * outputs - labels * (1 / (2 * self.c_train_value)) * (
                        -1 + self.c_train_value * outputs) ** 2

        # average over all the losses in the batch
        return torch.mean(loss, dim=0)
