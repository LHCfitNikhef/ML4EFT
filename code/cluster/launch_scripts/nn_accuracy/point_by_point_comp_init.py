import numpy as np
import quad_clas.analyse.analyse as analyse
import os
import pandas as pd

# Network's architecture of the pretrained models
architecture = [2, 30, 30, 30, 30, 30, 1]

path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/']}

sm_data_path = '/data/theorie/jthoeve/training_data/zh/features_mzh_y_ptz_v2/sm/events_0.pkl.gz'

n_dat = 5000
events_sm = pd.read_pickle(sm_data_path).iloc[1:, :].sample(int(n_dat), random_state=1)
events_sm['log_m_zh'] = np.log(events_sm['m_zh'])
#events_sm = events_sm.drop(['m_zh', 'pt_z'], axis=1)

luminosity = 5e3

# number of trained neural network replicas
mc_reps = 30

# location where to save the plot
plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/05_04'

fig1, fig2 = analyse.point_by_point_comp(
    events=events_sm,
    c=np.array([10, 0]),
    path_to_models=path_to_models,
    network_size=architecture,
    n_kin=2,
    lin=True,
    quad=False)

fig1.savefig(os.path.join(plot_save, 'overview_comp_chw_robust.pdf'))
fig2.savefig(os.path.join(plot_save, 'median_comp_chw_robust.pdf'))