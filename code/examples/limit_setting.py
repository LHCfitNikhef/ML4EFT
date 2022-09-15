import numpy as np
import ml4eft.core.classifier as classifier
import ml4eft.analyse.confidence_intervals as conf_int
import ml4eft.analyse.analyse as analyse


# Network's architecture of the pretrained models
architecture = [2, 30, 30, 30, 30, 30, 1]

path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}',
                          '/Users/jaco/Documents/ML4EFT/models/lin/cHq3/mc_run_{mc_run}']}

sm_data_path = '/Users/jaco/Documents/ML4EFT/data/events_high_stats/sm/events_0.npy'

events_sm = np.load(sm_data_path)[1:, :]

luminosity = 5000

# domain of EFT parameters to scan for limit setting
cHW_values = np.linspace(-1, 1, 50)
cHq3_values = np.linspace(-3, 3, 50)
scan_domain = np.array([cHW_values, cHq3_values])

# number of bins to consider
bins = np.array([2, 5, 8, 15])

# number of trained neural network replicas
mc_reps = 30

plot_save = '/Users/jaco/Documents/ML4EFT/plots/29_11/binned_unbinned.pdf'
limits = conf_int.Limits(luminosity=luminosity,
                         bins=bins,
                         scan_domain=scan_domain,
                         path_to_models=path_to_models,
                         mc_reps=mc_reps,
                         data_sm=events_sm,
                         lin=True,
                         plot_path=plot_save,
                         architecture=architecture)