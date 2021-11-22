#%%

import numpy as np
import quad_clas.analyse.confidence_intervals as conf_int

architecture = [2, 30, 30, 30, 30, 30, 1]
path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW',
                          '/Users/jaco/Documents/ML4EFT/models/lin/cHq3']}

path_save = '/data/theorie/jthoeve/ML4EFT_higgs/code/binned_unbinned/binned_unbinned_v28.pdf'
events_sm = np.load('/Users/jaco/Documents/ML4EFT/data/events/sm/events_0.npy')[1:, :]
luminosity = 5000
cHW_values = np.linspace(-1, 1, 50)
cHq3_values = np.linspace(-3, 3, 50)
scan_domain = np.array([cHW_values, cHq3_values])
bins = np.array([2, 5, 8, 15])
mc_reps = 30

#%%
limits = conf_int.Limits(luminosity=luminosity,
                bins=bins,
                scan_domain=scan_domain,
                mc_reps=mc_reps,
                data_sm=events_sm,
                lin=True,
                path_save=path_save,
                architecture=architecture)