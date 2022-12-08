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
#loading the runcard
runcard = '/data/theorie/pherbsch/ML4EFT/subproj/code/cluster/downloads/run_card_tt_parton_ctGRe.json'
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
json_runcard_loaded['event_data"'] = '/data/theorie/pherbsch/ML4EFT/subproj/code/cluster/downloads'


# %%
with open(runcard, 'w') as runcard_updated:
    json.dump(json_runcard_loaded, runcard_updated)



# %%
#now lets train a few models in a row.

output_dir = '/data/theorie/pherbsch/ML4EFT/subproj/code/cluster/models'
c_name = 'ctGRe'

fitter = classifier.Fitter(json_path = runcard,
                        mc_run = 0,
                        c_name = c_name,
                        output_dir = output_dir,
                        print_log=True)
                            


