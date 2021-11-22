#%%

import quad_clas.core.classifier as classifier

# training settings
path_to_json = '/Users/jaco/Documents/ML4EFT/code/cluster/launch_scripts/run_card_lin.json'
nn_rep = 4

output_path = '/Users/jaco/Documents/ML4EFT/code/higgs21/models' # results are stored here

fitter = classifier.Fitter(path_to_json, nn_rep, output_path)