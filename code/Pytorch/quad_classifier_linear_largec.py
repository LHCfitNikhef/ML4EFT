#!/usr/bin/env python
# coding: utf-8

import torch
print("Using torch", torch.__version__)

from torch import nn
from functools import reduce
import torch.utils.data as data
import torch.optim as optim
import pylhe
import numpy as np
import datetime
import sys
import matplotlib.pyplot as plt
import math

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 10)
        #self.fc2 = nn.Linear(15, 15)
        #self.fc3 = nn.Linear(32, 32)
        self.fc2 = nn.Linear(10, 1)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        #x = self.relu(x)
        #x = self.fc3(x)
        #x = self.relu(x)
        #x = self.fc3(x)
        return x

class Predictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.n_alpha = MLP()
        self.n_beta = MLP()
        
    def forward(self, x, c):
        n_alpha_out = self.n_alpha(x)
        n_beta_out = self.n_beta(x)
        return 1 / (1 + (1 + c*n_alpha_out)**2 + (c*n_beta_out)**2)

def loss_fn(outputs, labels, weights):
    # outputs.shape = (batch_size, 1), output \in (0, 1)
    # labels.shape = (batch_size, 1), labels \in {0, 1}
    
    #loss = weights*(labels - outputs)**2
    loss = (1-labels)*weights*outputs**2 + labels*weights*(1-outputs)**2
    #add up all the losses in the batch and divide by the length of the minibatch, i.e. average 
    #over the number of datapoint in the mini-batch
    return torch.sum(loss, dim = 0)

class eventDataset(data.Dataset):
    
    def __init__(self, train):
        """
        Inputs: 
            c - value of the Wilson coefficient 
        """
        super().__init__()
        self.train = train
        self.resc = False
        self.c_values = [5, 10]
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
        q0 = getattr(p1, 'e') + getattr(p2, 'e') #energy of the top quark pair in the pp COM frame
        q3 = getattr(p1, 'pz') + getattr(p2, 'pz')
        y = 0.5*np.log((q0 + q3)/(q0 - q3))
        return y  
    
    def standardize(self, mean, std):
        """
        Standardize the dataset so that neurons are more likely to have nonzero gradients
        """
        self.std = True
        self.resc = False
        
        self.data_eft_std = {}
        for k, v in self.data_eft.items():
            data_std = (v[0] - mean)/std
            self.data_eft_std[k] = data_std, v[1], v[2]

        self.data_sm_std = {}
        for k, v in self.data_sm.items():
            data_std = (v[0] - mean)/std
            self.data_sm_std[k] = data_std, v[1], v[2]
    
    def find_mean_std(self):
        """
        Find the mean and standard deviation of the data
        """
        dataset = []    
        for c_i in self.c_values:
            dataset.append(torch.cat((self.data_eft['{}'.format(c_i)][0], self.data_sm['{}'.format(c_i)][0])))
        dataset = torch.cat(dataset)
        self.mean = torch.mean(dataset, dim = 0)
        self.std = torch.std(dataset, dim = 0)
        
    
    def find_min_max(self):
        """
        Find the minimum and maximum of the data
        """
        
        min_values, max_values = [], []
        
        for c_i in self.c_values:
            dataset_eft = self.data_eft['{}'.format(c_i)][0]
            dataset_sm = self.data_sm['{}'.format(c_i)][0]
            min_value_eft, _ = torch.min(dataset_eft, dim = 0)
            max_value_eft, _ = torch.max(dataset_eft, dim = 0)
            min_value_sm, _ = torch.min(dataset_sm, dim = 0)
            max_value_sm, _ = torch.max(dataset_sm, dim = 0)

            min_value, _ = torch.min(torch.stack((min_value_eft, min_value_sm)), dim = 0)
            min_values.append(min_value)

            max_value, _ = torch.max(torch.stack((max_value_eft, max_value_sm)), dim = 0)
            max_values.append(max_value)

        min_values = torch.stack(min_values) 
        max_values = torch.stack(max_values)

        self.min_value, _ = torch.min(min_values, dim = 0)
        self.max_value, _ = torch.max(max_values, dim = 0)        
        
    
    def rescale(self, low, up, min_value, max_value):
        """
        Rescale the input data to lie in the interval [low, up]
        inputs:
            - min_value.shape = (1, 2)
            - max_value.shape = (1, 2)
        """
        self.std = False
        self.resc = True
        
        self.data_eft_resc = {}
        for k, v in self.data_eft.items():
            data_resc = low + (up - low)/(max_value - min_value)*(v[0] - min_value)
            self.data_eft_resc[k] = data_resc, v[1], v[2]

        self.data_sm_resc = {}
        for k, v in self.data_sm.items():
            data_resc = low + (up - low)/(max_value - min_value)*(v[0] - min_value)
            self.data_sm_resc[k] = data_resc, v[1], v[2]
       
        
    def lhe_loader(self, path):
        """
        Les Houches Event file reader
        """
        weight = []
        data = []
        for e in pylhe.readLHE(path):
            mtt = self.invariant_mass(e.particles[-1], e.particles[-2])
            y = self.rapidity(e.particles[-1], e.particles[-2])
            weight.append(e.eventinfo.weight)
            data.append([mtt, y])
        data = torch.tensor(data)
        n_events = data.size()[0]
        weight = (1/n_events)*torch.tensor(weight)
        
        return data, weight
    
    def load_events(self):
        """
        Load the datasets (eft and sm) from the les Houches event files. 
        """
        print("Loading data...\n")
        
        path_eft_dict = {'5': 'eft_5.lhe', '10': 'eft_10.lhe'}#, '15': 'eft_15.lhe'}#, '20': 'eft_20.lhe', '-20': 'eft_m20.lhe', '50': 'eft_50.lhe', '-50': 'eft_m50.lhe'}
        path_sm_dict = {'5': 'sm_5.lhe', '10': 'sm_10.lhe'}#, '15': 'sm_15.lhe'}#, '20': 'sm_20.lhe', '-20': 'sm_m20.lhe', '50': 'sm_50.lhe', '-50': 'sm_m50.lhe'}
            
        #load the data as dictionaries
        self.data_eft, self.data_sm = {}, {}

        print("Loading eft data...\n")
        cnt = 0                                   
        for c, path in path_eft_dict.items():
            print("Progress: ", cnt/6) 
            cnt += 1                               
            dataset, weights = self.lhe_loader(path)
            label = torch.zeros(dataset.size()[0])
            self.data_eft[c] = dataset, weights, label
        print("EFT data loaded successfully!\n")
        cnt = 0                                   
        print("Loading sm data...\n") 
        for c, path in path_sm_dict.items():
            print("Progress: ", cnt/6) 
            cnt += 1                                
            dataset, weights = self.lhe_loader(path)
            label = torch.ones(dataset.size()[0])
            self.data_sm[c] = dataset, weights, label
        print("SM data loaded successfully!")
        
        #Total number of events in the dataset (the same for eft and sm)
        self.n_events = self.data_eft['5'][0].size()[0]
         
  
    def __len__(self):
        # Number of data points we have. Alternatively self.data.shape[0], or self.label.shape[0]
        #return self.n_train if self.train else self.n_val
        return self.n_events
    
    def __getitem__(self, idx):
        """
        Return a tuple (eft, sm) with info on the idx-th data point of the dataset
        Outputs:
            - data tuple: (eft event, sm event)
            - label tuple: label = 0 for the eft, label = 1 for the sm
            - weight tuple: weight per event
        """          
        if self.resc:
            data_tuple = (self.data_eft_resc['5'][0][idx], self.data_sm_resc['5'][0][idx], self.data_eft_resc['10'][0][idx], self.data_sm_resc['10'][0][idx])
            weight_tuple = (self.data_eft_resc['5'][1][idx], self.data_sm_resc['5'][1][idx], self.data_eft_resc['10'][1][idx], self.data_sm_resc['10'][1][idx])
            label_tuple = (self.data_eft_resc['5'][2][idx], self.data_sm_resc['5'][2][idx], self.data_eft_resc['10'][2][idx], self.data_sm_resc['10'][2][idx])
        elif self.std:
            data_tuple = (self.data_eft_std['5'][0][idx], self.data_sm_std['5'][0][idx], self.data_eft_std['10'][0][idx], self.data_sm_std['10'][0][idx])
            weight_tuple = (self.data_eft_std['5'][1][idx], self.data_sm_std['5'][1][idx], self.data_eft_std['10'][1][idx], self.data_sm_std['10'][1][idx])
            label_tuple = (self.data_eft_std['5'][2][idx], self.data_sm_std['5'][2][idx], self.data_eft_std['10'][2][idx], self.data_sm_std['10'][2][idx])


        else:
            data_tuple = (self.data_eft['5'][0][idx], self.data_sm['5'][0][idx], self.data_eft['10'][0][idx], self.data_sm['10'][0][idx])
            weight_tuple = (self.data_eft['5'][1][idx], self.data_sm['5'][1][idx], self.data_eft['10'][1][idx], self.data_sm['10'][1][idx])
            label_tuple = (self.data_eft['5'][2][idx], self.data_sm['5'][2][idx], self.data_eft['10'][2][idx], self.data_sm['10'][2][idx])



        return data_tuple, weight_tuple, label_tuple


# In[14]:


train_dataset.resc = True
train_dataset.std = False


# In[13]:


#train_dataset.data_eft['5'][0]
#train_dataset.data_sm_resc['5'][0]
visualize([train_dataset.data_eft_std['10'][0], train_dataset.data_sm_std['10'][0]], [10, 0])


# In[8]:


train_dataset = eventDataset(train = True)


# In[11]:


#Rescale the data to lie between 0.1 and 0.9
min_value = train_dataset.min_value
max_value = train_dataset.max_value

mean = train_dataset.mean
std = train_dataset.std

train_dataset.rescale(0.1, 0.9, min_value, max_value)
train_dataset.standardize(mean, std)


# In[42]:


#data can be accessed by first providing the value of c as the first element and then 0, 1, 2 indicate the data, weights and labels respectively.
train_dataset.data_sm_std['10'][0], train_dataset.data_eft['5'][0], len(train_dataset)


# In[16]:


train_dataset.resc


# In[20]:


train_data_loader = data.DataLoader(train_dataset, batch_size= int(5*10**5), shuffle = True)
c_values = train_dataset.c_values
loss_list_train = []


# In[21]:


n_epochs = 100

for epoch in range(1, n_epochs + 1):
    loss_train = 0.0
    cnt = 0
    #test = True #uncomment to turn on the shuffle test
    for training_data, weights, labels in train_data_loader:
        #shuffle test: uncomment lines below
#         if test == True:
#             print("epoch %d "%epoch, training_data[0][1])
#             test = False
        print(cnt)
        cnt += 1
        #training_data.shape = (6, batch_size, 2)
        #weights.shape = (6, batch_size, 1)
        #labels.shape = (6, batch_size, 1)
        
        
    
        loss = torch.zeros(1)
        for i, train_data in enumerate(training_data):
            c_i = c_values[math.floor(i/2)]
            label_i = labels[i].unsqueeze(1)
            weight_i = weights[i].unsqueeze(1)
            output = model(train_data[i].float(), c_i)
            loss += loss_fn(output, label_i, weight_i)
                
        optimizer.zero_grad()
        
        loss.backward()
        
        optimizer.step()
        
        loss_train += loss.item()
        
    print('{} Epoch {}, Training loss {}'.format(datetime.datetime.now(), epoch, loss_train/len(train_data_loader)))
    loss_list_train.append(loss_train/len(train_data_loader))


# In[ ]:


#train_dataset = eventDataset(train = True)
#val_dataset = eventDataset(train = False)


# In[9]:


def visualize(data, labels):
    #fig = plt.figure()
    fig, ax = plt.subplots(facecolor='w')
    for i in range(len(data)):
        mtt = data[i].data[:,0].numpy()
        y = data[i].data[:,1].numpy()
        ax.scatter(mtt, y, label = 'c = %d'%(labels[i]))
        plt.xlabel(r'$m_{tt}\;\mathrm{(rescaled)}$')# + '(rescaled)')
        plt.ylabel(r'$y\;$'+'(rescaled)')
        plt.legend()
    plt.show()
    fig.savefig("training_data_rescaled.png", bbox_inches='tight', dpi=300)
    
    


# In[18]:


model = Predictor()
optimizer = optim.Adam(model.parameters(), lr = 1e-5)#optim.SGD(model.parameters(), lr=0.001, momentum = 0.1)#optim.Adam(model.parameters(), lr = 1e-3)


# In[ ]:


#next(iter(model.parameters()))


# In[ ]:


# training_loop(
#     n_epochs = 100,
#     optimizer = optimizer,
#     model = model,
#     train_loader = (train_data_loader_5, train_data_loader_m5, train_data_loader_20, train_data_loader_m20, train_data_loader_50, train_data_loader_m50),
#     val_loader = (val_data_loader_5, val_data_loader_m5, val_data_loader_20, val_data_loader_m20, val_data_loader_50, val_data_loader_m50)
# )


# In[22]:


plt.plot(np.array(loss_list_train), label = 'train')
#plt.plot(np.array(loss_list_val), label = 'val')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()


# In[ ]:


torch.save(model.state_dict(), 'QC.pt')


# In[ ]:


loaded_model = Predictor()
loaded_model.load_state_dict(torch.load('QC.pt'))


# In[ ]:


def likelihood_ratio(x, c):
    alpha_x = loaded_model.n_alpha
    ratio = 1.0 + c*alpha_x(x)
    return ratio.item()

def f_classifier(x, c):
    return 1/(1 + likelihood_ratio(x, c))

def n_alpha_out(x):
    alpha_x = loaded_model.n_alpha
    return alpha_x(x).item()


# In[ ]:


n_alpha_out(torch.tensor([(400-mean_mtt)/std_mtt, (0.06-mean_y)/std_y]))


# In[ ]:


(400-mean_mtt)/std_mtt


# In[ ]:


(0.06-mean_y)/std_y


# In[ ]:




