#!/usr/bin/env python
# coding: utf-8
import torch
import torch.utils.data as data
import torch.optim as optim
import pylhe
import numpy as np
import datetime
import math
# import matplotlib
# matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import animation
import EFTxSec_v2 as ExS
from torch import nn
import sys
# print("Using torch", torch.__version__)


class MLP(nn.Module):
    def __init__(self, num_inputs, num_hidden, num_outputs):
        super().__init__()
        self.fc1 = nn.Linear(num_inputs, num_hidden)
        self.fc2 = nn.Linear(num_hidden, num_hidden)
        self.fc3 = nn.Linear(num_hidden, num_hidden)
        self.fc4 = nn.Linear(num_hidden, num_hidden)
        self.fc5 = nn.Linear(num_hidden, num_outputs)
        # self.fc6 = nn.Linear(num_hidden, num_hidden)
        # self.fc7 = nn.Linear(num_hidden, num_outputs)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.relu(x)
        x = self.fc4(x)
        x = self.relu(x)
        x = self.fc5(x)
        return x


class Predictor_linear(nn.Module):
    def __init__(self, num_inputs, num_hidden, num_outputs):
        super().__init__()
        self.n_alpha = MLP(num_inputs, num_hidden, num_outputs)
        
    def forward(self, x, c):
        n_alpha_out = self.n_alpha(x)
        return 1 / (1 + (1 + c*n_alpha_out**2))


class Predictor_quadratic(nn.Module):
    def __init__(self, num_inputs, num_hidden, num_outputs):
        super().__init__()
        self.n_alpha = MLP(num_inputs, num_hidden, num_outputs)
        self.n_beta = MLP(num_inputs, num_hidden, num_outputs)

    def forward(self, x, c):
        n_alpha_out = self.n_alpha(x)
        n_beta_out = self.n_beta(x)
        r = (1+c*n_alpha_out)**2 + (c*n_beta_out)**2
        return 1 / (1 + r)


def loss_fn(outputs, labels, w_e):
    # outputs.shape = (batch_size, 1), output \in (0, 1)
    # labels.shape = (batch_size, 1), labels \in {0, 1}
    # w_e.shape = (batch_size, 1), w_e \in [0, \infty)
    loss = (1 - labels)*w_e*outputs**2 + labels*w_e*(1 - outputs)**2
    # add up all the losses in the batch
    return torch.sum(loss, dim=0)


class EventDataset(data.Dataset):
    
    def __init__(self, n_dat, train):
        """
        Inputs: 
            c - value of the Wilson coefficient 
        """
        super().__init__()
        self.train = train
        self.resc = False
        self.standardized = False
        self.mean = None
        self.std = None
        self.min_value = None
        self.max_value = None
        self.n_dat = n_dat
        self.n_val = None
        self.n_train = None
        self.data_eft_resc, self.data_sm_resc = {}, {}
        self.data_eft_std, self.data_sm_std = {}, {}
        self.data_eft, self.data_sm = {}, {}
        self.c_values = [-15, -10, -5, 5, 10, 15] # TODO: raise error when not complete
        self.load_events()
        self.find_min_max()
        self.find_mean_std()
        
    def invariant_mass(self, p1, p2):
        """
        Computes the invariant mass of an event
        """
        return np.sqrt(sum((1 if mu=='e' else -1)*(getattr(p1,mu)+getattr(p2,mu))**2 for mu in ['e','px','py','pz']))

    def rapidity(self, p1, p2): 
        """
        Computes the rapidity of an event
        """
        q0 = getattr(p1, 'e') + getattr(p2, 'e') # energy of the top quark pair in the pp COM frame
        q3 = getattr(p1, 'pz') + getattr(p2, 'pz')
        y = 0.5*np.log((q0 + q3)/(q0 - q3))
        return y  
    
    def standardize(self):
        """
        Standardize the dataset so that neurons are more likely to have nonzero gradients
        """
        self.standardized = True
        self.resc = False

        for k, v in self.data_eft.items():
            data_std = (v[0] - self.mean)/self.std
            self.data_eft_std[k] = data_std, v[1], v[2]

        for k, v in self.data_sm.items():
            data_std = (v[0] - self.mean)/self.std
            self.data_sm_std[k] = data_std, v[1], v[2]
    
    def find_mean_std(self):
        """
        Find the mean and standard deviation of the data
        """
        dataset = []    
        for c_i in self.c_values:
            dataset.append(torch.cat((self.data_eft['{}'.format(c_i)][0], self.data_sm['{}'.format(c_i)][0])))
        dataset = torch.cat(dataset)
        self.mean = torch.mean(dataset, dim=0)
        self.std = torch.std(dataset, dim=0)

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
            data_resc = low + (up - low)/(self.max_value - self.min_value)*(v[0] - self.min_value)
            self.data_eft_resc[k] = data_resc, v[1], v[2]

        for k, v in self.data_sm.items():
            data_resc = low + (up - low)/(self.max_value - self.min_value)*(v[0] - self.min_value)
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
            weight.append(e.eventinfo.weight)
            event_data.append([mtt])
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
        
        # path_eft_dict = {'5': 'lhe_cut/eft_5_cut.lhe', '10': 'lhe_cut/eft_10_cut.lhe', '30': 'lhe_cut/eft_30_cut.lhe'}
        # # path_eft_dict = {'5': 'eft_5.lhe', '10': 'eft_lo_30.lhe'}
        # path_sm_dict = {'5': 'lhe_cut/sm_5_cut.lhe', '10': 'lhe_cut/sm_10_cut.lhe', '30': 'lhe_cut/sm_30_cut.lhe'}

        # path_eft_dict = {'5': 'linear_1000_500K/eft_5.lhe', '10': 'linear_1000_500K/eft_10.lhe', '15': 'linear_1000_500K/eft_15.lhe'}
        # path_sm_dict = {'5': 'linear_1000_500K/sm_5.lhe', '10': 'linear_1000_500K/sm_10.lhe', '15': 'linear_1000_500K/sm_15.lhe'}

        path_eft_dict = {'-5': 'quadratic/eft_m5.lhe', '-10': 'quadratic/eft_m10.lhe',
                         '-15': 'quadratic/eft_m15.lhe', '5': 'quadratic/eft_5.lhe', '10': 'quadratic/eft_10.lhe',
                         '15': 'quadratic/eft_15.lhe'}
        path_sm_dict = {'-5': 'quadratic/sm_5.lhe', '-10': 'quadratic/sm_10.lhe',
                        '-15': 'quadratic/sm_15.lhe', '5': 'quadratic/sm_5.lhe', '10': 'quadratic/sm_10.lhe',
                        '15': 'quadratic/sm_15.lhe'}

        # set the seed for reproducibility and to make sure the training and validation sets do not overlap
        torch.manual_seed(0)

        print("Loading eft data...\n")
        cnt = 0                                   
        for c, path in path_eft_dict.items():
            print("Progress: {:.2f}".format(cnt/len(path_eft_dict)))
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
                weights_train = weights_full[train_indices]/self.n_train
                labels_train = labels_full[train_indices]
                self.data_eft[c] = dataset_train, weights_train, labels_train
            else:
                val_indices = shuffled_indices[-self.n_val:]
                dataset_val = dataset_full[val_indices]
                weights_val = weights_full[val_indices]/self.n_val
                labels_val = labels_full[val_indices]
                self.data_eft[c] = dataset_val, weights_val, labels_val
        print("EFT data loaded successfully!\n")

        cnt = 0
        print("Loading sm data...\n") 
        for c, path in path_sm_dict.items():
            print("Progress: {:.2f}".format(cnt/len(path_sm_dict)))
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
                weights_train = weights_full[train_indices]/self.n_train
                labels_train = labels_full[train_indices]
                self.data_sm[c] = dataset_train, weights_train, labels_train
            else:
                val_indices = shuffled_indices[-self.n_val:]
                dataset_val = dataset_full[val_indices]
                weights_val = weights_full[val_indices]/self.n_val
                labels_val = labels_full[val_indices]
                self.data_sm[c] = dataset_val, weights_val, labels_val
        print("SM data loaded successfully!")

    def visualize(self):
        # fig = plt.figure()
        # for coeff, dataset in self.data_eft.items():
        #     mtt = dataset[0].view(-1).numpy()
        #     plt.scatter(mtt, np.zeros(len(mtt)), label=coeff)
        data_sm = self.data_sm['5'][0].view(-1).numpy()
        data_eft_15 = self.data_eft['15'][0].view(-1).numpy()
        # plt.hist(data_eft_5, bins=int((2.5- 2 * 0.172) / 0.05), range=(1000, 2500), histtype='step', label='0')
        # plt.hist(data_eft_15, bins=int((2.5 - 2 * 0.172) / 0.05), range=(1000, 2500), histtype='step', label='15')
        plt.scatter(data_sm, np.ones(len(data_sm)), label='sm')
        plt.scatter(data_eft_15, np.zeros(len(data_eft_15)), label='15')
        #plt.xlim((1000, 2500))
        plt.legend()
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
        if self.resc:
            data_tuple = (self.data_eft_resc['5'][0][idx], self.data_sm_resc['5'][0][idx], self.data_eft_resc['10'][0][idx],self.data_sm_resc['10'][0][idx], self.data_eft_resc['15'][0][idx], self.data_sm_resc['15'][0][idx])
            weight_tuple = (self.data_eft_resc['5'][1][idx], self.data_sm_resc['5'][1][idx], self.data_eft_resc['10'][1][idx],self.data_sm_resc['10'][1][idx], self.data_eft_resc['15'][1][idx], self.data_sm_resc['15'][1][idx])
            label_tuple = (self.data_eft_resc['5'][2][idx], self.data_sm_resc['5'][2][idx], self.data_eft_resc['10'][2][idx],self.data_sm_resc['10'][2][idx], self.data_eft_resc['15'][2][idx], self.data_sm_resc['15'][2][idx])
        elif self.standardized:
            data_tuple = (self.data_eft_std['-15'][0][idx], self.data_sm_std['-15'][0][idx], self.data_eft_std['-10'][0][idx], self.data_sm_std['-10'][0][idx], self.data_eft_std['-5'][0][idx], self.data_sm_std['-5'][0][idx], self.data_eft_std['5'][0][idx], self.data_sm_std['5'][0][idx], self.data_eft_std['10'][0][idx], self.data_sm_std['10'][0][idx], self.data_eft_std['15'][0][idx], self.data_sm_std['15'][0][idx])
            weight_tuple = (self.data_eft_std['-15'][1][idx], self.data_sm_std['-15'][1][idx], self.data_eft_std['-10'][1][idx], self.data_sm_std['-10'][1][idx], self.data_eft_std['-5'][1][idx], self.data_sm_std['-5'][1][idx], self.data_eft_std['5'][1][idx], self.data_sm_std['5'][1][idx], self.data_eft_std['10'][1][idx], self.data_sm_std['10'][1][idx], self.data_eft_std['15'][1][idx], self.data_sm_std['15'][1][idx])
            label_tuple = (self.data_eft_std['-15'][2][idx], self.data_sm_std['-15'][2][idx], self.data_eft_std['-10'][2][idx], self.data_sm_std['-10'][2][idx], self.data_eft_std['-5'][2][idx], self.data_sm_std['-5'][2][idx], self.data_eft_std['5'][2][idx], self.data_sm_std['5'][2][idx], self.data_eft_std['10'][2][idx], self.data_sm_std['10'][2][idx], self.data_eft_std['15'][2][idx], self.data_sm_std['15'][2][idx])
        else:
            data_tuple = (self.data_eft['10'][0][idx], self.data_sm['10'][0][idx])
            weight_tuple = (self.data_eft['10'][1][idx], self.data_sm['10'][1][idx])
            label_tuple = (self.data_eft['10'][2][idx], self.data_sm['10'][2][idx])

        return data_tuple, weight_tuple, label_tuple


def plot_training_report(train_loss, val_loss):
    f = plt.figure()
    plt.plot(np.array(train_loss), label='train')
    plt.plot(np.array(val_loss), label='val')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()
    plt.show()
    f.savefig('loss.pdf')


def training_loop(n_epochs, optimizer, model, train_loader, val_loader, c_values, path, make_animation=False):
    loss_list_train, loss_list_val = [], []  # stores the training loss per epoch
    for epoch in range(1, n_epochs + 1):
        loss_train, loss_val = 0.0, 0.0
        for (training_data, train_weights, train_labels), (val_data, val_weights, val_labels) in zip(train_loader, val_loader):

            train_loss, val_loss = torch.zeros(1), torch.zeros(1)

            # TODO: rewrite using zip function
            for i, train_data in enumerate(training_data):
                c_i = c_values[math.floor(i/2)]
                label_i = train_labels[i].unsqueeze(1)
                weight_i = train_weights[i].unsqueeze(1)
                output = model(train_data.float(), c_i)
                loss_i = loss_fn(output, label_i, weight_i)
                train_loss += loss_i

            with torch.no_grad():
                for i, val_data in enumerate(val_data):
                    c_i = c_values[math.floor(i/2)]
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

        print('{} Epoch {}, Training loss {}'.format(datetime.datetime.now(), epoch, loss_train/len(train_loader)),
              'Validation loss {}'.format(loss_val/len(val_loader)))
        loss_list_train.append(loss_train/len(train_loader))
        loss_list_val.append(loss_val/len(val_loader))

        # save the intermediate weights during training when animate is true
        if make_animation:
            torch.save(model.state_dict(), 'trained_nn/' + path + '_{}.pt'.format(epoch))
        if not make_animation:
            torch.save(model.state_dict(), path)

    plot_training_report(loss_list_train, loss_list_val)
    np.savetxt('loss.out', loss_list_train)



# def visualize(data_eft, data_sm):
#     fig, ax = plt.subplots(facecolor='w')
#     mtt_eft = data_eft.numpy()
#     mtt_sm = data_sm.numpy()
#     # plt.hist(mtt_eft, 10, range=(1000, 2500), histtype='step', label='EFT_hist')
#     # plt.hist(mtt_sm, 10, range=(1000, 2500), label='SM_hist')
#     plt.scatter(mtt_eft, np.zeros(len(mtt_eft)), label='EFT')
#     plt.scatter(mtt_sm, np.ones(len(mtt_sm)), label='SM')
#     plt.legend()
#     plt.show()


# def likelihood_ratio_nn(loaded_model, x, c):
#     alpha_x = loaded_model.n_alpha
#     ratio = 1.0 + c*alpha_x(x)
#     return ratio


# def f(loaded_model, x, c):
#     ratio = likelihood_ratio_nn(loaded_model, x, c)
#     return 1/(1+ratio)


def train_classifier(path, train_dataset, val_dataset, epochs, quadratic=True, make_animation=False):
    if quadratic:
        model = Predictor_quadratic(num_inputs=1, num_hidden=30, num_outputs=1)
    else:
        model = Predictor_linear(num_inputs=1, num_hidden=30, num_outputs=1)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    # train_data_loader = data.DataLoader(train_dataset, batch_size=train_dataset.__len__(), shuffle=True)
    # val_data_loader = data.DataLoader(val_dataset, batch_size=val_dataset.__len__(), shuffle=False)

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
        make_animation=make_animation,
    )


def f_linear(x, n_alpha, ctg):
    f_nn = [1 / (1 + 1 + ctg * n_alpha(x_i.float()).item() ** 2) for x_i in x]
    return np.array(f_nn)


def f_quadratic(x, n_alpha, n_beta, ctg):
    f_nn = [1 / (1 + (1 + ctg * n_alpha(x_i.float()).item()) ** 2 + (ctg*n_beta(x_i.float()).item())**2)for x_i in x]
    return np.array(f_nn)

def n_alpha(mtt, train_dataset):
    mtt = torch.tensor([mtt])
    loaded_model = Predictor_quadratic(num_inputs=1, num_hidden=30, num_outputs=1)
    n_alpha_trained = loaded_model.n_alpha
    mtt_rescaled = (mtt - train_dataset.mean) / train_dataset.std
    return n_alpha_trained(mtt_rescaled.float()).item()



def n_beta(mtt, train_dataset):
    mtt = torch.tensor([mtt])
    loaded_model = Predictor_quadratic(num_inputs=1, num_hidden=30, num_outputs=1)
    n_beta_trained = loaded_model.n_beta
    mtt_rescaled = (mtt - train_dataset.mean) / train_dataset.std
    return n_beta_trained(mtt_rescaled.float()).item()



def plot_predictions(network_path, train_dataset, quadratic, ctg):
    if quadratic:
        mtt, f_pred, n_alpha_nn, n_alpha_n_beta_nn = make_predictions(network_path, train_dataset, quadratic, ctg)
        n_alpha_n_beta_nn = np.array(n_alpha_n_beta_nn)
    else:
        mtt, f_pred, n_alpha_nn = make_predictions(network_path, train_dataset, quadratic, ctg)
    n_alpha_nn = np.array(n_alpha_nn)

    fig = plt.figure()
    mtt_min, mtt_max = 1000, 4000
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])

    # Plot the NN prediction
    ax1.plot(mtt, f_pred, label='NN prediction')

    # Compute the analytic likelihood ratio and plot
    x, y = ExS.plot_likelihood_ratio_1D(mtt_min * 10 ** -3, mtt_max * 10 ** -3, ctg, np_order=2 if quadratic else 1)
    x = np.array(x)
    y = np.array(y)
    ax1.plot(x * 1e3, y, '--', c='red', label='Analytical result')

    plt.ylabel(r'$f\;(m_{tt}, c)$')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    plt.title('NN versus analytical at ctG = {}'.format(ctg))
    plt.legend()

    ax2 = fig.add_axes([0.15, 0.1, 0.75, 0.20])
    ax2.plot(x * 1e3, y / f_pred)
    plt.xlabel(r'$m_{tt}\;[GeV]$')
    plt.ylabel('ana/NN')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim(((y / f_pred).min(), (y / f_pred).max()))

    plt.show()
    fig.savefig('NNvsAna_v13.pdf')

    # Compare r_NN to r_ana
    fig = plt.figure()
    n_alpha_ana = np.array([ExS.n_alpha_ana_1D(mtt_i*1e-3) for mtt_i in mtt])
    n_alpha_n_beta_ana = np.array([ExS.n_alpha_n_beta_ana_1D(mtt_i*1e-3) for mtt_i in mtt])
    plt.plot(mtt, 1 + 2*ctg*n_alpha_ana + ctg**2*n_alpha_n_beta_ana, '--', c='red', label='Analytical result')
    plt.plot(mtt, 1 + 2*ctg*n_alpha_nn + ctg**2*n_alpha_n_beta_nn, '-', label='NN')
    plt.legend()
    plt.title('Likelihood ratio: NN versus analytical at c = {}'.format(ctg))
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel(r'$r\;(m_{tt}, c)$')
    plt.show()

    # Compare n_alpha to alpha
    n_alpha_ana = np.array([ExS.n_alpha_ana_1D(mtt_i * 1e-3) for mtt_i in mtt])
    plt.plot(mtt, n_alpha_ana, '--', c='red', label='Analytical result')
    plt.plot(mtt, n_alpha_nn, '-', label='NN')
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel(r'$\alpha(m_{tt})$')
    plt.legend()
    plt.title('reconstruction of alpha')
    plt.show()

    # Compare n_alpha**2 + n_beta**2 to alpha**2 + beta**2
    n_alpha_n_beta_ana = np.array([ExS.n_alpha_n_beta_ana_1D(mtt_i * 1e-3) for mtt_i in mtt])
    plt.plot(mtt, n_alpha_n_beta_ana, '--', c='red', label='Analytical result')
    plt.plot(mtt, n_alpha_n_beta_nn, '-', label='NN')
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel(r'$\alpha(m_{tt})^2+\beta(m_{tt})^2$')
    plt.legend()
    plt.title('reconstruction of alpha and beta')
    plt.show()

    # show r(x,c) as a function of c at fixed mtt and compare analytical and NN
    n_alpha_ana = ExS.n_alpha_ana_1D(2500*1e-3)
    # n_alpha_nn = n_alpha(1010, train_dataset)

    n_alpha_n_beta_ana = ExS.n_alpha_n_beta_ana_1D(2500*1e-3)
    # n_beta_nn = n_beta(1010, train_dataset)


    ctg_range = np.arange(-15, 15, 1)
    r_ana = 1 + 2*ctg_range*n_alpha_ana + ctg_range**2*n_alpha_n_beta_ana
    # print("ana: ", 1 + 2*5*n_alpha_ana + 5**2*n_alpha_n_beta_ana)
    r_nn = 1 + 2*ctg_range*n_alpha_nn[15] + ctg_range**2*n_alpha_n_beta_nn[15]
    # print("NN:", r_nn)

    plt.plot(ctg_range, r_ana, c='red', label='Ana')
    plt.plot(ctg_range, r_nn, label='NN')
    plt.xlabel(r'c')
    plt.ylabel(r'$r(m_{tt}=2.5, c)$')
    # plt.scatter(np.array([5, 1 + 2*5*n_alpha_nn + 5**2*n_alpha_n_beta_nn]), c='k')
    # plt.scatter(np.array([10, 1 + 2*10*n_alpha_nn + 10**2*n_alpha_n_beta_nn]), c='k')
    # plt.scatter(np.array([15, 1 + 2*15*n_alpha_nn + 15**2*n_alpha_n_beta_nn]), c='k')
    plt.legend()
    plt.show()


def make_predictions(network_path, train_dataset, quadratic, ctg):
    """
    :param network_path: path to the saved NN to be loaded
    :param train_dataset: training data needed to find the mean and std
    :param ctg: value of the Wilson coefficient ctg
    :return: comparison between NN prediction and analytically known result for the likelihood ratio
    """

    # Be careful to use the same network architecture as during training
    if quadratic:
        loaded_model = Predictor_quadratic(num_inputs=1, num_hidden=30, num_outputs=1)
    else:
        loaded_model = Predictor_linear(num_inputs=1, num_hidden=30, num_outputs=1)
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
        n_alpha_n_beta = [n_alpha_trained(x_i.float()).item()**2 + n_beta_trained(x_i.float()).item()**2  for x_i in x]
        return mtt.numpy(), f_pred, n_alpha, n_alpha_n_beta
    else:
        f_pred = f_linear(x, n_alpha_trained, ctg)
        n_alpha = [n_alpha_trained(x_i.float()).item() for x_i in x]
        return mtt.numpy(), f_pred, n_alpha


def animate_learning(train_dataset):
    mtt_min, mtt_max = 1000, 4000
    # First set up the figure, the axis, and the plot element we want to animate
    fig, ax = plt.subplots()
    ax = plt.axes(xlim=(mtt_min, mtt_max), ylim=(0, 1))

    # Compute the analytic likelihood ratio and plot
    x, y = ExS.plot_likelihood_ratio_1D(mtt_min*10**-3, mtt_max*10**-3, ctg=5, np_order=2)
    x = np.array(x)
    y = np.array(y)
    ax.plot(x*1e3, y, '--', c='red', label='Analytical result')

    plt.ylabel(r'$f\;(m_{tt}, c)$')
    plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
    plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    plt.title('NN versus analytical at ctG = 5')
    plt.legend()

    line, = ax.plot([], [], lw=2, label='NN prediction')
    epoch_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    loss_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
    loss = np.loadtxt('loss.out')

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        epoch_text.set_text('')
        loss_text.set_text('')
        return line, epoch_text, loss_text

    # animation function.  This is called sequentially
    def animate(i):
        x, f_pred = make_predictions('trained_nn/quadratic/QC_quadratic_100K_3hidden_neg_v2_{}.pt'.format(i+1), train_dataset)
        line.set_data(x, f_pred)
        epoch_text.set_text('epoch = {}'.format(i))
        loss_text.set_text('loss = {:.4f}'.format(loss[i]))
        return line, epoch_text, loss_text

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=70, interval=200, blit=True)

    anim.save('training_animation_v2.gif')
    plt.show()



def main(trained, path, n_dat, epochs, make_animation, quadratic, ctg):
    train_dataset = EventDataset(n_dat, train=True)
    val_dataset = EventDataset(n_dat, train=False)

    train_dataset.rescale(-1, 1)
    val_dataset.rescale(-1, 1)
    train_dataset.standardize()
    val_dataset.standardize()  # standardize the validation set by the same mean and variance

    # train_dataset.visualize()
    # sys.exit()
    # Uncomment to use rescaled data between [0.1, 0.9]
    # train_dataset.resc = True
    # val_dataset.resc = True

    # visualize(train_dataset.data_eft['10'][0], train_dataset.data_sm['10'][0])
    if trained:  # classifier is trained already
        if make_animation:
            animate_learning(train_dataset)
        else:
            plot_predictions(path, train_dataset, quadratic, ctg)
    else:
        train_classifier(path,
                         train_dataset,
                         val_dataset,
                         epochs,
                         quadratic=quadratic,
                         make_animation=make_animation,
                         )


if __name__ == '__main__':
    trained = False
    path = 'trained_nn/quadratic/QC_quadratic_100K_3hidden_neg_v3.pt'
    main(trained, '', n_dat=100000, epochs=500, make_animation=False, quadratic=True, ctg=5)



