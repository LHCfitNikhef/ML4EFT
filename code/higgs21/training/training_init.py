#%%
# import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.quad_classifier_cluster as train

# training settings
path_to_json = '/Users/jaco/Documents/ML4EFT/code/cluster/launch_scripts/run_card_cluster.json'
nn_rep = 1

output_path = '/Users/jaco/Documents/ML4EFT/code/higgs21/models' # results are stored here

train.start(path_to_json, nn_rep, output_path)