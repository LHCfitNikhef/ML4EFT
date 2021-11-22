#%%

import numpy as np
import quad_clas.core.classifier as classifier
import quad_clas.analyse.confidence_intervals as conf_int
import quad_clas.analyse.analyse as analyse

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
                         path_to_models=path_to_models,
                         mc_reps=mc_reps,
                         data_sm=events_sm,
                         lin=True,
                         plot_path=path_save,
                         architecture=architecture)
#%%

# retrieve sm dataset
path_sm_data = '/Users/jaco/Documents/ML4EFT/data/events/sm/events_0.npy'
path_dict_sm = {0: path_sm_data}
data_sm = classifier.EventDataset(c=0,
                                  n_features=2,
                                  path_dict=path_dict_sm,
                                  n_dat=1000,
                                  hypothesis=1)

sm_events = data_sm.events.numpy()

fig1, fig2 = analyse.point_by_point_comp(mc_reps=mc_reps,
                            events=sm_events,
                            c=np.array([2,0]),
                            path_to_models=path_to_models,
                            network_size=architecture,
                            lin=True,
                            quad=False)

fig1.savefig('/Users/jaco/Documents/ML4EFT/plots/22_11/overview_point_by_point.pdf')
fig2.savefig('/Users/jaco/Documents/ML4EFT/plots/22_11/median_point_by_point.pdf')

