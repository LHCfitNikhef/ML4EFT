import numpy as np
import quad_clas.analyse.analyse as analyse
import os
import pandas as pd

# Network's arch1tecture of the pretrained models
architecture = [2, 30, 30, 30, 30, 30, 1]

# path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_ptz_robust_scaler/model_chw_lin/',
#                           '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_ptz_robust_scaler/model_chw_lin/']}

path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/test_zh/model_chw_lin_robust',
                         '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/test_zh/model_chw_lin_robust']}

sm_data_path = '/data/theorie/jthoeve/training_data/zh/features_mzh_y_ptz_v2/sm/events_0.pkl.gz'
#sm_data_path = '/data/theorie/jthoeve/event_generation/events_high_stats/pT/sm/events_0.npy'

# ttbar

#sm_data_path = '/data/theorie/jthoeve/training_data/tt/U35/sm/events_0.pkl.gz'

n_dat = 5000
events_sm = pd.read_pickle(sm_data_path).iloc[1:, :].sample(int(n_dat), random_state=1)

#events_sm = events_sm.drop(columns='y')

#events_sm['log_m_tt'] = np.log(events_sm['m_tt'])
#events_sm['log_m_tt'] = np.log(events_sm['pt_z'])

# events_sm = np.load(sm_data_path)[1:n_dat + 1, :]
# df = pd.DataFrame(events_sm, columns=['m_zh', 'y', 'pt_z'])
# df['log_m_zh'] = np.log(df['m_zh'])
# events_sm = df

#events_sm = events_sm.drop(['m_zh', 'pt_z'], axis=1)

luminosity = 5e3

# number of trained neural network replicas
mc_reps = 1

# location where to save the plot
plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/14_04'

fig1, fig2 = analyse.point_by_point_comp(
    events=events_sm,
    c=np.array([2, 0]),
    path_to_models=path_to_models,
    network_size=architecture,
    n_kin=2,
    process='ZH',
    lin=True,
    quad=False)

fig1.savefig(os.path.join(plot_save, 'overview_comp_chw_robust_mask.pdf'))
fig2.savefig(os.path.join(plot_save, 'median_comp_chw_robust_mask.pdf'))