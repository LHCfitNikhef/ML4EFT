# %%
#importing stuff
import wget
import tarfile
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import json

import ml4eft.core.classifier as classifier
import ml4eft.analyse.analyse as analyse
import ml4eft.plotting.features as features

rc('text', usetex=False)
rc('font', **{'family': 'DejaVu Sans', 'size': 22})


# %%
#defining functions for downloading remote files
def file_downloader(url, download_dir='./downloads'):

    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    file = wget.download(url, out=download_dir)
    return file

def untar(path_to_tar, destination='./downloads'):

    with tarfile.open(path_to_tar) as f:
        f.extractall(destination)

download_dir = './downloads'

# %%
#loading the training data
training_data_url = 'https://dl.dropboxusercontent.com/s/z16fz2ggbn244pl/training_data.tar.gz?dl=0'
training_data = file_downloader(training_data_url);
data_train_loc = training_data.split('.tar')[0]

untar(training_data);

# %%
# load eft events
coeff = ["ctGRe", "ctj8"]
events_eft = []
for c in coeff:
    path_to_events = os.path.join(data_train_loc, 'tt_{}_{}/events_0.pkl.gz'.format(c, c))
    events, xsec = analyse.Analyse.load_events(path_to_events)
    events_eft.append(events)

# load sm events
events_sm, xsec_sm = analyse.Analyse.load_events(os.path.join(download_dir, 'training_data/tt_sm/events_0.pkl.gz'))

# %%
#loading the runcard
path_to_runcard = 'https://dl.dropboxusercontent.com/s/v4ulo6icveh63fw/run_card_tt_llvlvlbb.json?dl=0'
runcard = file_downloader(path_to_runcard)

# %%
#open the runcard to see what the options are.
with open(runcard) as json_runcard:
    json_runcard_loaded = json.load(json_runcard)

json_runcard_loaded


# %%
# to change the runcard I can do the following
json_runcard_loaded['epochs'] = 200
json_runcard_loaded['lr'] = 0.001
json_runcard_loaded['n_batches'] = 50
json_runcard_loaded['patience'] = 10 # needs to be bigger than number of epochs



# %%
with open(runcard, 'w') as runcard_updated:
    json.dump(json_runcard_loaded, runcard_updated)



# %%
#now lets train a few models in a row.

output_dir = './models'
c_name = 'ctu8'

fitter = classifier.Fitter(json_path = runcard,
                        mc_run = 0,
                        c_name = c_name,
                        output_dir = output_dir,
                        print_log=True)
                            


