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

eft_points = [[-10.0, 0], [10, 0], [0, -10], [0, 10]]
n_eft_points = len(eft_points)


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

class Classifier(nn.Module):
    """ The decssion function :math:`g(x, c)`

    Implementation of the decision boundary `g(x, c)`
    """

    def __init__(self, architecture):
        super().__init__()

        self.NN1 = MLP(architecture)
        self.NN2 = MLP(architecture)
        self.NN11 = MLP(architecture)
        self.NN22 = MLP(architecture)

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

        NN1_out = self.NN1(x)
        NN2_out = self.NN2(x)
        NN11_out = self.NN11(x)
        NN22_out = self.NN22(x)

        r = torch.relu(1 + c1 * NN1_out + c2 * NN2_out + c1 ** 2 * NN11_out + c2 ** 2 * NN22_out)
        g = 1 / (1 + r)
        return g


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

    def preprocess(self, fitter, data_dict, scaler_path):
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
        
        datasets_all = [dataset[i][1] for dataset in data_dict.values() for i in range(len(dataset))]
        df = pd.concat(datasets_all)

        # fit the scaler transformer to the eft and sm features
        self.scaler.fit(df[fitter.features])

        n_val_points = int(fitter.val_ratio * fitter.n_dat)
        n_train_points = fitter.n_dat - n_val_points

        # rescale the sm and eft data
        loaded_data_scaled = {}
        for wc, datasets_wc in data_dict.items():
            hypothesis = 1 if wc == 'sm' else 0
            temp = []
            for c_val, events, xsec in datasets_wc:
                events_scaled = self.scaler.transform(events[fitter.features])
                df_scaled = pd.DataFrame(events_scaled, columns=fitter.features)
                event_dataset = EventDataset(df_scaled, xsec, hypothesis)
                train, val = data.random_split(event_dataset, [n_train_points, n_val_points])
                temp.append([c_val, train, val])
            loaded_data_scaled[wc] = temp

        # save the scaler
        joblib.dump(self.scaler, scaler_path)

        return loaded_data_scaled


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
    
        self.output_dir, self.log_path = self.set_folder_structure()
        self.data_dict = self.get_data_dict()

        self.scaler = None

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
        data_train, data_val = self.load_data()

        # copy run card to the appropriate folder
        with open(mc_path + 'run_card.json', 'w') as outfile:
            json.dump(self.run_options, outfile)

        # start the training
        self.train_classifier(data_train, data_val)
        
    def set_folder_structure(self):

        output_dir = self.result_path / self.run_options["run_id"]
        output_dir.mkdir(parents=True, exist_ok=True)

        for c_train in self.c_train.keys():
            model_dir = output_dir / c_train / "mc_run_{}".format(self.mc_run)
            model_dir.mkdir(parents=True, exist_ok=True)

        log_path = output_dir / "log"
        log_path.mkdir(parents=True, exist_ok=True)

        return output_dir, log_path

    def get_data_dict(self):

        path_sm = self.event_data_path / 'sm' / 'events_{}.pkl.gz'.format(self.mc_run)
        data_dict = {'sm': [[0, path_sm]]}

        for c_train, c_vals in self.c_train.items():
            data_dict[c_train] = [
                [c_val, self.event_data_path / '{}'.format(c_train) / '{}_{}'.format(c_train, i) / 'events_{}.pkl.gz'.format(self.mc_run)] for
                (i, c_val) in enumerate(c_vals)]

        return data_dict

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

        loaded_data = {}
        for wc, paths in self.data_dict.items():
            dataset_wc = []
            for c_val, dataset_path in paths:
                # split cross-section from events and draw a subset
                dataset = pd.read_pickle(dataset_path, compression="infer")
                dataset_wc.append([c_val, dataset.iloc[1:].sample(self.n_dat), dataset.iloc[1, 1]])
            loaded_data[wc] = dataset_wc

        # preprocessing of the data
        preprocessor = PreProcessing(self)
        scaler_path = self.output_dir / 'scaler.gz'
        data_preprocessed = preprocessor.preprocess(self, loaded_data, scaler_path)

        return data_preprocessed

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
                    logging.info("Detected stagnant training, reset the weights")
                    self.model.apply(self.weight_reset)

            loss_train, loss_val = 0.0, 0.0

            # We save the model parameters at the start of each epoch
            torch.save(self.model.state_dict(), path + 'trained_nn_{}.pt'.format(epoch))

            # compute validation loss
            with torch.no_grad():
                for minibatch in zip(*val_loader):
                    val_loss = torch.zeros(1)
                    for i, [event, weight, label] in enumerate(minibatch):
                        c1, c2 = eft_points[i % n_eft_points]
                        if isinstance(self.model, Classifier):
                            output = self.model(event.float(), c1, c2)
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
                        if torch.any(output >= 1).item():
                            logging.info("g >= 1 detected!")

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
                format(time=datetime.datetime.now(), epoch=epoch, train_loss=loss_train/self.n_batches, val_loss=loss_val/self.n_batches,
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

        elif self.loss_type == 'direct':
            loss = -(1 - labels) * w_e * outputs - labels * (1 / (2 * self.c_train_value)) * (-1 + self.c_train_value * outputs) ** 2

        # average over all the losses in the batch
        return torch.mean(loss, dim=0)
