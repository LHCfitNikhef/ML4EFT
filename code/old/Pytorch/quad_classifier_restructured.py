#!/usr/bin/env python
# coding: utf-8
import torch
import torch.utils.data as data
import torch.optim as optim
import pylhe
import numpy as np
import datetime
import matplotlib.pyplot as plt
import math
from torch import nn
import sys
# print("Using torch", torch.__version__)


class MLP(nn.Module):
    def __init__(self, num_inputs, num_hidden, num_outputs):
        super().__init__()
        self.fc1 = nn.Linear(num_inputs, num_hidden)
        self.fc2 = nn.Linear(num_hidden, num_hidden)
        self.fc3 = nn.Linear(num_hidden, num_outputs)
        self.relu = nn.Tanh()
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        # x = self.fc2(x)
        # x = self.relu(x)
        # x = self.fc2(x)
        # x = self.relu(x)
        # x = self.fc2(x)
        # x = self.relu(x)
        x = self.fc3(x)
        return x


class Predictor(nn.Module):
    def __init__(self, num_inputs, num_hidden, num_outputs):
        super().__init__()
        self.n_alpha = MLP(num_inputs, num_hidden, num_outputs)
        self.n_beta = MLP(num_inputs, num_hidden, num_outputs)
        
    def forward(self, x, c):
        n_alpha_out = self.n_alpha(x)
        n_beta_out = self.n_beta(x)
        return 1 / (1 + (1 + c*n_alpha_out)**2 + (c*n_beta_out)**2)


def loss_fn(outputs, labels, w_e):
    # outputs.shape = (batch_size, 1), output \in (0, 1)
    # labels.shape = (batch_size, 1), labels \in {0, 1}
    # w_e.shape = (batch_size, 1), w_e \in [0, \infty)
    loss = (1 - labels)*w_e*outputs**2 + labels*w_e*(1 - outputs)**2
    # add up all the losses in the batch
    return torch.sum(loss, dim = 0)


class EventDataset(data.Dataset):
    
    def __init__(self, train):
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
        self.n_val = None
        self.n_train = None
        self.data_eft_resc, self.data_sm_resc = {}, {}
        self.data_eft_std, self.data_sm_std = {}, {}
        self.data_eft, self.data_sm = {}, {}
        self.c_values = [5, 10, 30]
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
            y = self.rapidity(e.particles[-1], e.particles[-2])
            weight.append(e.eventinfo.weight)
            event_data.append([mtt, y, np.log(mtt)])
            # event_data.append([mtt, y])
            cnt += 1
            if cnt == 50:
                break
        event_data = torch.tensor(event_data)
        n_events = event_data.size()[0]
        weight = (1/n_events)*torch.tensor(weight)
        
        return event_data, weight
    
    def load_events(self):
        """
        Load the datasets (eft and sm) from the les Houches event files. 
        """
        print("Loading training data...\n") if self.train is True else print("Loading validation set...\n")
        
        # path_eft_dict = {'5': 'lhe_cut/eft_5_cut.lhe', '10': 'lhe_cut/eft_10_cut.lhe', '30': 'lhe_cut/eft_30_cut.lhe'}
        # # path_eft_dict = {'5': 'eft_5.lhe', '10': 'eft_lo_30.lhe'}
        # path_sm_dict = {'5': 'lhe_cut/sm_5_cut.lhe', '10': 'lhe_cut/sm_10_cut.lhe', '30': 'lhe_cut/sm_30_cut.lhe'}

        path_eft_dict = {'5': 'eft_5.lhe', '10': 'eft_10.lhe', '30': 'eft_30.lhe'}
        path_sm_dict = {'5': 'sm_5.lhe', '10': 'sm_10.lhe', '30': 'sm_m50.lhe'}

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
            self.n_val = int(0.2 * n_events)
            self.n_train = n_events - self.n_val

            shuffled_indices = torch.randperm(n_events)

            if self.train:
                train_indices = shuffled_indices[:-self.n_val]
                dataset_train = dataset_full[train_indices]
                weights_train = weights_full[train_indices]
                labels_train = labels_full[train_indices]
                self.data_eft[c] = dataset_train, weights_train, labels_train
            else:
                val_indices = shuffled_indices[-self.n_val:]
                dataset_val = dataset_full[val_indices]
                weights_val = weights_full[val_indices]
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
            self.n_val = int(0.2 * n_events)
            self.n_train = n_events - self.n_val

            shuffled_indices = torch.randperm(n_events)

            if self.train:
                train_indices = shuffled_indices[:-self.n_val]
                dataset_train = dataset_full[train_indices]
                weights_train = weights_full[train_indices]
                labels_train = labels_full[train_indices]
                self.data_sm[c] = dataset_train, weights_train, labels_train
            else:
                val_indices = shuffled_indices[-self.n_val:]
                dataset_val = dataset_full[val_indices]
                weights_val = weights_full[val_indices]
                labels_val = labels_full[val_indices]
                self.data_sm[c] = dataset_val, weights_val, labels_val
        print("SM data loaded successfully!")

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
            data_tuple = (self.data_eft_resc['5'][0][idx], self.data_sm_resc['5'][0][idx], self.data_eft_resc['10'][0][idx], self.data_sm_resc['10'][0][idx],self.data_eft_resc['30'][0][idx], self.data_sm_resc['30'][0][idx])
            weight_tuple = (self.data_eft_resc['5'][1][idx], self.data_sm_resc['5'][1][idx], self.data_eft_resc['10'][1][idx], self.data_sm_resc['10'][1][idx], self.data_eft_resc['30'][1][idx], self.data_sm_resc['30'][1][idx])
            label_tuple = (self.data_eft_resc['5'][2][idx], self.data_sm_resc['5'][2][idx], self.data_eft_resc['10'][2][idx], self.data_sm_resc['10'][2][idx], self.data_eft_resc['30'][2][idx], self.data_sm_resc['30'][2][idx])
        elif self.standardized:
            data_tuple = (self.data_eft_std['5'][0][idx], self.data_sm_std['5'][0][idx], self.data_eft_std['10'][0][idx], self.data_sm_std['10'][0][idx],self.data_eft_std['30'][0][idx], self.data_sm_std['30'][0][idx])
            weight_tuple = (self.data_eft_std['5'][1][idx], self.data_sm_std['5'][1][idx], self.data_eft_std['10'][1][idx], self.data_sm_std['10'][1][idx], self.data_eft_std['30'][1][idx], self.data_sm_std['30'][1][idx])
            label_tuple = (self.data_eft_std['5'][2][idx], self.data_sm_std['5'][2][idx], self.data_eft_std['10'][2][idx], self.data_sm_std['10'][2][idx], self.data_eft_std['30'][2][idx], self.data_sm_std['30'][2][idx])
        else:
            data_tuple = (self.data_eft['5'][0][idx], self.data_sm['5'][0][idx], self.data_eft['10'][0][idx], self.data_sm['10'][0][idx], self.data_eft['30'][0][idx], self.data_sm['30'][0][idx])
            weight_tuple = (self.data_eft['5'][1][idx], self.data_sm['5'][1][idx], self.data_eft['10'][1][idx], self.data_sm['10'][1][idx], self.data_eft['30'][1][idx], self.data_sm['30'][1][idx])
            label_tuple = (self.data_eft['5'][2][idx], self.data_sm['5'][2][idx], self.data_eft['10'][2][idx], self.data_sm['10'][2][idx], self.data_eft['30'][2][idx], self.data_sm['30'][2][idx])

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


def training_loop(n_epochs, optimizer, model, train_loader, val_loader, c_values, path):
    loss_list_train, loss_list_val = [], []  # stores the training loss per epoch
    for epoch in range(1, n_epochs + 1):
        loss_train, loss_val = 0.0, 0.0
        cnt = 0
        for (training_data, train_weights, train_labels), (val_data, val_weights, val_labels) in zip(train_loader, val_loader):
            print(cnt)
            cnt += 1
            # training_data.shape = (6, batch_size, 2)
            # weights.shape = (6, batch_size, 1)
            # labels.shape = (6, batch_size, 1)

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

        torch.save(model.state_dict(), path)
    plot_training_report(loss_list_train, loss_list_val)


def visualize(data, labels):
    fig, ax = plt.subplots(facecolor='w')
    for i in range(len(data)):
        mtt = data[i].data[:,0].numpy()
        y = data[i].data[:,1].numpy()
        ax.scatter(mtt, y, label = 'c = %d'%(labels[i]))
        # plt.xlabel(r'$\log(m_{tt})\;\mathrm{(rescaled)}$')
        # plt.ylabel(r'$y\;$'+'(rescaled)')
        plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
        plt.ylabel(r'$y$')
        plt.title('SM and EFT NLO samples')
        plt.legend()
    plt.show()
    fig.savefig('SM_EFT_NLO_samples_30.pdf')


# visualize([val_dataset.data_eft_std['10'][0], val_dataset.data_sm_std['10'][0]], [10, 0])
# visualize([train_dataset.data_eft_std['10'][0], train_dataset.data_sm_std['10'][0]], [10, 0])


def likelihood_ratio_nn(loaded_model, x, c):
    alpha_x = loaded_model.n_alpha
    beta_x = loaded_model.n_beta
    ratio = (1.0 + c*alpha_x(x))**2 + (c*beta_x(x))**2
    return ratio


def f(loaded_model, x, c):
    ratio = likelihood_ratio_nn(loaded_model, x, c)
    return 1/(1+ratio)


def train_classifier(path, train_dataset, val_dataset):
    model = Predictor(num_inputs=3, num_hidden=70, num_outputs=1)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    train_data_loader = data.DataLoader(train_dataset, batch_size=train_dataset.__len__(), shuffle=True)
    val_data_loader = data.DataLoader(val_dataset, batch_size=val_dataset.__len__(), shuffle=False)


    # train_data_loader = data.DataLoader(train_dataset, batch_size=int(train_dataset.__len__()/4), shuffle=True)
    # val_data_loader = data.DataLoader(val_dataset, batch_size=int(val_dataset.__len__()/4), shuffle=False)

    training_loop(
        n_epochs=500,
        optimizer=optimizer,
        model=model,
        train_loader=train_data_loader,
        val_loader=val_data_loader,
        c_values=train_dataset.c_values,
        path=path
    )


def make_predictions(network_path, train_dataset, val_dataset):
    loaded_model = Predictor(num_inputs=3, num_hidden=20, num_outputs=1)
    loaded_model.load_state_dict(torch.load(network_path))

    fig, ax = plt.subplots(facecolor='w')
    mt = 172
    s = (14 * 10 ** 3) ** 2
    y_max = np.log(np.sqrt(s) / (2 * mt))
    y_min = -y_max
    mtt = torch.arange(2*mt, 1000, 1)
    y = torch.arange(y_min, y_max, 0.01)
    Z = []

    for i in range(len(y)):
        print(i / len(y))
        for j in range(len(mtt)):
            mtt_j = mtt[j].item()
            mtt_log_j = np.log(mtt[j].item())
            y_i = y[i].item()
            x_features = (torch.tensor([mtt_j, y_i, mtt_log_j]) - train_dataset.mean) / train_dataset.std
            r_pred = likelihood_ratio_nn(loaded_model, x_features.float(), 10).item()
            if np.abs(y_i) > np.log(np.sqrt(s)/mtt_j):
                r_pred = 0
            Z.append(r_pred)
    Z = np.array(Z)
    Z = np.reshape(Z, (len(y), len(mtt)))
    im = plt.imshow(Z, cmap=plt.cm.Blues, aspect=(1000 - 2*mt) / (y_max - y_min), extent=[2*mt, 1000, y_min, y_max], origin='lower')
    plt.colorbar(im)

    plt.ylabel(r'Rapidity $Y = \log\sqrt{x_1/x_2}$')
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.title(r'$r(x,c)$ ')

    mtt_sm = torch.cat((train_dataset.data_sm['5'][0][:, 0], train_dataset.data_sm['10'][0][:, 0])).numpy()
    y_sm = torch.cat((train_dataset.data_sm['5'][0][:, 1], train_dataset.data_sm['10'][0][:, 1])).numpy()

    mtt_5 = train_dataset.data_eft['5'][0][:, 0].numpy()
    y_5 = train_dataset.data_eft['5'][0][:, 1].numpy()

    mtt_10 = train_dataset.data_eft['10'][0][:, 0].numpy()
    y_10 = train_dataset.data_eft['10'][0][:, 1].numpy()

    # ax.scatter(mtt_sm, y_sm, c='orange', label='SM', s=10)
    # ax.scatter(mtt_5, y_5, c='red', label='EFT 5', s=10)
    # ax.scatter(mtt_10, y_10, c='green', label='EFT 10', s=10)
    plt.xlim(mtt.min(), mtt.max())
    plt.ylim(y.min(), y.max())
    #plt.legend()
    plt.show()
    fig.savefig('likelihood_ratio.pdf')


def main(trained, path):
    train_dataset = EventDataset(train=True)
    val_dataset = EventDataset(train=False)

    train_dataset.rescale(0.1, 0.9)
    val_dataset.rescale(0.1, 0.9)
    train_dataset.standardize()
    val_dataset.standardize()  # standardize the validation set by the same mean and variance

    # train_dataset.resc = True
    # val_dataset.resc = True

    visualize([train_dataset.data_eft['30'][0], train_dataset.data_eft['10'][0], train_dataset.data_sm['10'][0]], [30, 10, 0])


    if trained:  # classifier is trained already
        make_predictions(path, train_dataset, val_dataset)
    else:
        train_classifier(path, train_dataset, val_dataset)


if __name__ == '__main__':
    trained = False
    path = 'QC_fit.pt'
    main(trained, path)



