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
import pandas as pd
from joblib import dump, load
# matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import rc
from torch import nn
from sklearn.model_selection import train_test_split
import shutil
import quad_clas.analyse.analyse as analyse
from sklearn.preprocessing import StandardScaler, RobustScaler, QuantileTransformer
import joblib

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
        layers += [nn.Linear(layer_sizes[-1], output_size)]
        self.layers = nn.Sequential(
            *layers)  # nn.Sequential summarizes a list of modules into a single module, applying them in sequence

    def forward(self, x):
        out = self.layers(x)
        return out


class CustomActivationFunction(nn.Module):

    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.config = {"name": self.name}


class ConstraintActivation(CustomActivationFunction):

    def __init__(self, c):
        super().__init__()
        self.c = c

    def forward(self, x):
        if self.c > 0:
            return torch.relu(x) - 1 / self.c + 1e-6
        else:
            return - torch.relu(x) - 1 / self.c - 1e-6


class PredictorLinear(nn.Module):
    """
    Returns the function f(x,c) from the paper (Wulzer et al.) in the linear case
    """

    def __init__(self, architecture, c):
        super().__init__()
        self.c = c
        self.n_alpha = MLP(architecture)
        self.n_alpha.layers.add_module('constraint', ConstraintActivation(self.c))

    def forward(self, x):

        # add final activation function to enforce positive r

        n_alpha_out = self.n_alpha(x)
        return 1 / (1 + (1 + self.c * n_alpha_out))


class PredictorQuadratic(nn.Module):
    """
        Returns the function f(x,c) from the paper (Wulzer et al.) in the quadratic case
    """

    def __init__(self, architecture):
        super().__init__()
        self.architecture = architecture
        self.n_beta = MLP(architecture)

    def forward(self, x, c, path_lin, path_quad):
        n_beta_out = self.n_beta(x)
        n_lin = PredictorLinear(self.architecture)
        n_lin.load_state_dict(torch.load(path_lin))

        # undo quad rescaling
        dir_lin = os.path.dirname(path_lin)
        #dir_quad = dir_lin.replace('lin', 'quad')
        mean, std = np.loadtxt(os.path.join(path_quad, 'scaling.dat'))
        x_orig = (x * std) + mean

        # recale lin
        mean, std = np.loadtxt(os.path.join(dir_lin, 'scaling.dat'))
        x = (x_orig - mean) /std

        r = 1 + c * n_lin.n_alpha(x.float()) + c ** 2 * n_beta_out
        return 1 / (1 + r)

class PredictorCross(nn.Module):
    """
        Returns the function f(x,c) from the paper (Wulzer et al.) in the quadratic case
    """

    def __init__(self, architecture):
        super().__init__()
        self.architecture = architecture
        self.n_gamma = MLP(architecture)

    def forward(self, x, c1, c2, path_lin_1, path_lin_2, path_quad_1, path_quad_2, path_cross):
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

class PreProcessing():

    def __init__(self, n_dat, path, features, scaler_type):

        self.n_dat = n_dat
        self.path = path
        self.features = features

        if scaler_type == 'robust':
            self.scaler = RobustScaler(quantile_range=(5, 95))
        elif scaler_type == 'standardise':
            self.scaler = StandardScaler()
        else:
            self.scaler = QuantileTransformer(n_quantiles=1000, output_distribution='normal')

        self.load_data()

    def load_data(self):

        df_sm = pd.read_pickle(self.path['sm'], compression="infer")
        self.xsec_sm = df_sm.iloc[0, 0]
        # test
        df_sm = df_sm[(df_sm['m_tt'] < 0.5) & (df_sm['m_tt'] > 0.36)]


        #self.df_sm = df_sm.iloc[1:,:].sample(self.n_dat)
        self.df_sm = df_sm.sample(self.n_dat)

        df_eft = pd.read_pickle(self.path['eft'], compression="infer")

        # test
        self.xsec_eft = df_eft.iloc[0, 0]
        df_eft = df_eft[(df_eft['m_tt'] < 0.5) & (df_eft['m_tt'] > 0.36)]

        #self.df_eft = df_eft.iloc[1:, :].sample(self.n_dat)
        self.df_eft = df_eft.sample(self.n_dat)


    def feature_scaling(self, scaler_path):

        # add log features for pT
        # self.df_sm['log_pt_z'] = np.log(self.df_sm['pt_z'])
        # # self.df_sm['log_pt_b'] = np.log(self.df_sm['pt_b'])
        # #
        # self.df_eft['log_pt_z'] = np.log(self.df_eft['pt_z'])
        # # self.df_eft['log_pt_b'] = np.log(self.df_eft['pt_b'])
        #
        # self.df_sm['log_m_zh'] = np.log(self.df_sm['m_zh'])
        # self.df_eft['log_m_zh'] = np.log(self.df_eft['m_zh'])
        # self.df_sm['log_m_tt'] = np.log(self.df_sm['m_tt'])
        # self.df_eft['log_m_tt'] = np.log(self.df_eft['m_tt'])

        df = pd.concat([self.df_sm, self.df_eft])

        # fit the scaler transformer to the eft and sm features
        self.scaler.fit(df[self.features])

        # rescale the sm and eft data
        features_sm_scaled = self.scaler.transform(self.df_sm[self.features])
        features_eft_scaled = self.scaler.transform(self.df_eft[self.features])

        # convert transformed features to dataframe
        df_sm_scaled = pd.DataFrame(features_sm_scaled, columns=self.features)
        df_eft_scaled = pd.DataFrame(features_eft_scaled, columns=self.features)

        # import matplotlib.pyplot as plt
        # bins = np.concatenate([np.array([-2]), np.linspace(-1, 1, 20), np.array([2])])
        # kwargs = dict(histtype='stepfilled', alpha=0.3, density=False, bins=bins, ec="k")
        # plt.hist(df_sm_scaled['m_tt'].values, **kwargs, label=r'$\rm{SM}$')
        #
        # plt.xlim(-1.2, 1.2)
        # plt.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/07_06/feature_scaling_tt_v2.pdf')
        # # plt.show()
        # import pdb; pdb.set_trace()

        # save the scaler
        joblib.dump(self.scaler, scaler_path)
        #dump(robsc, open(scaler_path, 'wb'))

        return df_sm_scaled, df_eft_scaled

class EventDataset(data.Dataset):

    def __init__(self, df, preproc, xsec, path, n_dat, features, hypothesis=0):
        """
        Inputs:
            c - value of the Wilson coefficient
            hypothesis - 0 (False) if EFT and 1 (True) if SM
        """
        super().__init__()

        self.df = df
        self.xsec = xsec
        self.hypothesis = hypothesis
        self.features = features
        self.preproc = preproc

        self.events = None
        self.weights = None
        self.labels = None

        self.event_loader(path)

    def event_loader(self, path):

        n_dat = len(self.df)

        self.weights = self.xsec * torch.ones(n_dat).unsqueeze(-1)
        self.events = torch.tensor(self.df[self.features].values)
        self.labels = torch.ones(n_dat).unsqueeze(-1) if self.hypothesis else torch.zeros(n_dat).unsqueeze(-1)

        # reweight

        # events_orig = self.preproc.scaler.inverse_transform(self.events)
        # self.weights[events_orig[:, 0] > 0.8] *= 2

        logging.info("Dataset loaded from {}".format(path))

    def __len__(self):

        # Number of data points.
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
        self.lr = self.run_options["lr"]
        self.n_batches = self.run_options["n_batches"]
        self.quadratic = self.run_options['quadratic']
        self.cross_term = self.run_options['cross_term']
        self.loss_type = self.run_options['loss_type']
        self.scaler_type = self.run_options['scaler_type']
        self.patience = self.run_options['patience']
        self.n_dat = self.run_options['n_dat']
        self.epochs = self.run_options['epochs']
        self.network_size = [self.run_options['input_size']] + self.run_options['hidden_sizes'] + [
            self.run_options['output_size']]
        self.event_data_path = self.run_options['event_data']  # path to training data

        self.eft_dict = self.run_options['coeff']
        self.c1 = self.eft_dict[0]['value']
        self.c2 = self.eft_dict[1]['value']

        self.mc_run = mc_run
        self.lag_mult = self.run_options['lag_mult']

        self.features = self.run_options['features']

        output_dir = os.path.join(output_dir, time.strftime("%Y/%m/%d"))
        os.makedirs(output_dir, exist_ok=True)

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
            self.path_dict['eft_data_path'] = 'quad/{eft_coeff}/events_{mc_run}.pkl.gz'
            self.model = PredictorQuadratic(self.network_size)
        elif self.cross_term:
            self.path_dict['eft_data_path'] = 'cross_term/{eft_coeff}/events_{mc_run}.pkl.gz'
            self.model = PredictorCross(self.network_size)
        else:
            self.path_dict['eft_data_path'] = 'lin/{eft_coeff}/events_{mc_run}.pkl.gz'
            self.model = PredictorLinear(self.network_size, self.eft_value)

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

        # event files are stored at event_data_path/sm, event_data_path/lin, event_data_path/quad
        # or event_data_path/cross for sm, linear, quadratic (single coefficient) and cross terms respectively
        path_sm = os.path.join(self.event_data_path, 'sm/events_{}.pkl.gz'.format(self.mc_run))
        path_eft = os.path.join(self.event_data_path, self.path_dict['eft_data_path'].format(eft_coeff=self.eft_op, mc_run=self.mc_run))

        path_dict = {'sm': path_sm, 'eft': path_eft}

        # preprocessing of the data
        preproc = PreProcessing(self.n_dat, path_dict, self.features, self.scaler_type)

        # save the scaler
        scaler_path = os.path.join(self.path_dict['mc_path'], 'scaler.gz')
        df_sm_scaled, df_eft_scaled = preproc.feature_scaling(scaler_path)

        # We construct an eft and a sm data set for each value of c in c_values and make a list out of it
        # As of the new version of the code where only the sm and any non-zero point in EFT space are needed
        # as an input, the list seems redundant, but this functionality is kept in case one would like to train
        # on multiple EFT points.

        data_eft = EventDataset(df_eft_scaled,
                                preproc,
                                xsec=preproc.xsec_eft,
                                path=path_eft,
                                n_dat=self.n_dat,
                                features=self.features,
                                hypothesis=0)

        data_sm = EventDataset(df_sm_scaled,
                               preproc,
                               xsec=preproc.xsec_sm,
                               path=path_sm,
                               n_dat=self.n_dat,
                               features=self.features,
                               hypothesis=1)

        data_all = [data_eft, data_sm]

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

        #decay_rate = 0.96
        #scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer=optimizer)

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
        self.training_loop(optimizer=optimizer, train_loader=train_data_loader, val_loader=val_data_loader, scheduler=None)

    def training_loop(self, optimizer, train_loader, val_loader, scheduler):

        path = self.path_dict['mc_path']

        loss_list_train, loss_list_val = [], []  # stores the training loss per epoch

        # we want to be able to keep track of potential over-fitting, so introduce a counter that gets increased
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
                        if isinstance(self.model, PredictorLinear):
                            output = self.model(event.float())
                        if isinstance(self.model, PredictorQuadratic):
                            output = self.model(event.float(), self.c1 + self.c2, self.path_lin_1, self.path_dict['mc_path'])
                        if isinstance(self.model, PredictorCross):
                            output = self.model(event.float(), self.c1, self.c2, self.path_lin_1, self.path_lin_2, self.path_quad_1,
                                           self.path_quad_2)
                        loss = self.loss_fn(output, label, weight)
                        val_loss += loss
                    assert val_loss.requires_grad is False

                    loss_val += val_loss.item()


            # the * denotes the unpacking operator. It passes all the list elements
            # of train_loader as separate arguments to the zip function, e.g f(a[0], a[1]) = f(*a).
            # Here we have zip(DataLoader_1, DataLoader_2, ..) which enables looping over our mini-batches.
            for j, minibatch in enumerate(zip(*train_loader)):
                train_loss = torch.zeros(1)
                # loop over all the datasets within the minibatch and compute their contribution to the loss
                for i, [event, weight, label] in enumerate(minibatch): # i=0: eft, i=1: sm
                    if isinstance(self.model, PredictorLinear):
                        output = self.model(event.float())

                    if isinstance(self.model, PredictorQuadratic):
                        output = self.model(event.float(), self.c1 + self.c2, self.path_lin_1, self.path_dict['mc_path'])
                    if isinstance(self.model, PredictorCross):
                        output = model(event.float(), self.c1, self.c2, self.path_lin_1, self.path_lin_2, self.path_quad_1,
                                       self.path_quad_2, self.path_dict['mc_path'])
                    loss = self.loss_fn(output, label, weight)
                    train_loss += loss

                # do gradient descent after each minibatch. Move to the next epoch when all minibatches are looped over.
                optimizer.zero_grad()
                train_loss.backward()
                optimizer.step()

                loss_train += train_loss.item()

            #scheduler.step(train_loss)

            loss_list_train.append(loss_train)
            loss_list_val.append(loss_val)

            training_status = "Epoch {epoch}, Training loss {train_loss}, Validation loss {val_loss}. sign = {sign}". \
                format(time=datetime.datetime.now(), epoch=epoch, train_loss=loss_train, val_loss=loss_val, sign=output[0])
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

            if overfit_counter == self.patience:
                stopping_point = epoch - self.patience # TODO subtract an addition 0ne
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

    def loss_fn(self, outputs, labels, w_e):

        """
        :param outputs: outputs.shape = (batch_size, 1), output \in (0, 1)
        :param labels: labels.shape = (batch_size, 1), labels \in {0, 1}
        :param w_e: w_e.shape = (batch_size, 1), w_e \in [0, \infty)
        :return: contribution to loss from a sample x ~ pdf(x|H_0,1)
        """

        if self.loss_type == 'CE':

            # if any(outputs >= 1) or any(outputs <= 0):
            #     import pdb;
            #     pdb.set_trace()
            loss = - (1 - labels) * w_e * torch.log(1 - outputs) - labels * w_e * torch.log(outputs)
        elif self.loss_type == 'QC':
            loss = (1 - labels) * w_e * outputs ** 2 + labels * w_e * (1 - outputs) ** 2

        if self.lag_mult != 0:
            relu = nn.ReLU()
            penalty = lag_mult * relu((outputs - 1) / outputs) # r = (1 - f) / f, give penalty if r < 0
        else:
            penalty = 0

        # add up all the losses in the batch
        return torch.sum(loss + penalty, dim=0)





