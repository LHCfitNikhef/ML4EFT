import numpy as np
import ml4eft.analyse.analyse as analyse
import os
import pandas as pd

# Network's arch1tecture of the pretrained models
#architecture = [2, 30, 30, 30, 30, 30, 30, 30, 30, 1]
architecture = [2, 100, 100, 100, 1]

# best models for chq3

# path_to_models = {'lin': {
#     'chw': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh/model_chq3_lin_deep_v7',
#     'chq3': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh/model_chq3_lin_deep_v7'}}

# best models for chw
# path_to_models = {'lin': {
#     'chw': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh/model_chw_lin',
#     'chq3': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh/model_chq3_lin_deep_v7'}}

# tt

path_to_models = {'lin': {
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/07/model_ctgre_lin_v9',
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/07/model_ctgre_lin_v9'}}


#sm_data_path = '/data/theorie/jthoeve/training_data/zh/features_mzh_y_ptz_v2/sm/events_0.pkl.gz'
#sm_data_path = '/data/theorie/jthoeve/event_generation/events_high_stats/pT/sm/events_0.npy'

# ttbar

sm_data_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l/sm/events_0.pkl.gz'


n_dat = 5000
events_sm = pd.read_pickle(sm_data_path).iloc[1:, :].sample(int(n_dat), random_state=1)

events_sm = events_sm[(events_sm['m_tt'] < 0.5)]
#events_sm = events_sm.drop(columns='pt_t')
#events_sm['y'] = 0

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
plot_save = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/07_06'

# fig1, fig2 = analyse.point_by_point_comp(
#     events=events_sm,
#     c=np.array([0, 10]),
#     path_to_models=path_to_models,
#     network_size=architecture,
#     c_train={
#         "cuu_quad": 100.0,
#         "cuu_quad": 100.0
#     },
#     n_kin=2,
#     process='tt',
#     lin=True,
#     quad=False)
#events_sm['y'] = 0
fig1, fig2 = analyse.point_by_point_comp(
    events=events_sm,
    c=np.array([-2, 0]),
    path_to_models=path_to_models,
    c_train={
        "ctgre": -10.0,
        "cuu": 0
    },
    n_kin=2,
    process='tt',
    lin=True,
    quad=False,
    epoch=300)

fig1.savefig(os.path.join(plot_save, 'overview_comp_ctgre_lin_v9.pdf'))
fig2.savefig(os.path.join(plot_save, 'median_comp_ctgre_lin_v9.pdf'))