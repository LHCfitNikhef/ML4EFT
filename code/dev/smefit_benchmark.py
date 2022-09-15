#%%
from ml4eft.core.th_predictions import TheoryPred
import numpy as np
import pandas as pd
#%% experimental data
lumi = 5E6
bins = np.array([0, 75, 150, 250, 400, 1000])
observed_data = pd.read_pickle('/Users/jaco/Documents/ML4EFT/output/fitmaker_vs_ml4eft/observed_data.pkl.gz')
n_i, _ = np.histogram(observed_data['pt_z'].values, bins)
#%%
sigma_i = n_i / lumi
stat_unc_sigma_i = np.sqrt(n_i) / lumi

#%% theory predictions
coeffs = ['chw', 'chwb']

theory_pred = TheoryPred(coeff=coeffs,
                         bins=bins,
                         kinematic='pt_z',
                         event_path='/Users/jaco/Documents/ML4EFT/training_data/zh_llbb/',
                         nreps=50)
