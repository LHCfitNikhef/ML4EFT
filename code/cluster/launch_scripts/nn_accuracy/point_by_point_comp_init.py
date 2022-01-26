import numpy as np
import quad_clas.analyse.analyse as analyse
import os

# Network's architecture of the pretrained models
architecture = [3, 30, 30, 30, 30, 30, 1]

path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHW_3_feat/mc_run_{mc_run}',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHq3_3_feat/mc_run_{mc_run}']}

sm_data_path = '/data/theorie/jthoeve/event_generation/events_high_stats/pT/sm/events_0.npy'

n_dat = 5000
events_sm = np.load(sm_data_path)[1:n_dat + 1, :]

luminosity = 5000

# number of trained neural network replicas
mc_reps = 30

# location where to save the plot
plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/26_01/'

fig1, fig2 = analyse.point_by_point_comp(mc_reps=mc_reps,
                                         events=events_sm,
                                         c=np.array([10,0]),
                                         path_to_models=path_to_models,
                                         network_size=architecture,
                                         lin=True,
                                         quad=False)

fig1.savefig(os.path.join(plot_save, 'overview_comp_cHW.pdf'))
fig2.savefig(os.path.join(plot_save, 'median_comp_cHW.pdf'))