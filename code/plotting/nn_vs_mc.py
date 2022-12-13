import ml4eft.plotting.features as features
import ml4eft.analyse.analyse as analyse
import ml4eft.core.th_predictions as theory_pred

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



########
df_sm = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt_llvlvlbb/tt_sm/events_0.pkl.gz')
df_eft = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt_llvlvlbb/tt_cQj38/events_0.pkl.gz')

hist_2d_eft, eta_edges, pt_ll_edges = np.histogram2d(df_eft.iloc[1:, :][['eta_l1']].values.flatten(), df_eft.iloc[1:, :][['pt_ll']].values.flatten(), bins=[np.linspace(-2.5, 2.5, 10), np.linspace(10, np.max(df_eft.iloc[1:, :][['pt_ll']].values.flatten()), 100)], density=True)
hist_2d_sm, _, _ = np.histogram2d(df_sm.iloc[1:, :][['eta_l1']].values.flatten(), df_sm.iloc[1:, :][['pt_ll']].values.flatten(), bins=[np.linspace(-2.5, 2.5, 10), np.linspace(10, np.max(df_sm.iloc[1:, :][['pt_ll']].values.flatten()), 100)], density=True)

hist_mg_ratio = ((df_eft.iloc[0,0] * hist_2d_eft) / (df_sm.iloc[0,0] * hist_2d_sm) - 1) / 10

_xx, _yy = np.meshgrid((eta_edges + (eta_edges[1]-eta_edges[0])/2)[:-1], (pt_ll_edges + (pt_ll_edges[1]-pt_ll_edges[0])/2)[:15], indexing='ij')
x, y = _xx.ravel(), _yy.ravel()


bottom = np.zeros_like(x)




fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
#import pdb; pdb.set_trace()
ax.bar3d(x, y, bottom, eta_edges[1]-eta_edges[0], pt_ll_edges[1]-pt_ll_edges[0], hist_mg_ratio[:, :15].ravel(), shade=True, alpha=0.7)


###########


order = 'lin'
path_to_models_root = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_llvlvlbb_pt_ll_eta_l_v7/2022/10/06'

path_to_models = analyse.Analyse.build_path_dict(path_to_models_root, order, prefix='model')
nn_analyser = analyse.Analyse(path_to_models, order)

eta_l_span = np.linspace(-2.5, 2.5, 100)
pt_ll_span = np.linspace(0, 450, 50)
eta_l_grid, pt_ll_grid = np.meshgrid(eta_l_span, pt_ll_span)
grid = np.c_[eta_l_grid.ravel(), pt_ll_grid.ravel()]
df = pd.DataFrame({'pt_ll': grid[:, 1], 'eta_l1': grid[:, 0]})

nn_analyser.evaluate_models(df)
models_evaluated = nn_analyser.models_evaluated_df['models']

nn_analyser.models_evaluated_df['models'] = models_evaluated.apply(lambda row: np.median(row, axis=0))

nn_cQj38 = nn_analyser.models_evaluated_df['models']['lin', 'cQj38'].reshape(eta_l_grid.shape)

########


ax.plot_surface(eta_l_grid, pt_ll_grid, nn_cQj38, cmap='viridis', alpha=0.5)
ax.set_xlabel(r'$\eta_l$')
ax.set_ylabel(r'$p_T^{\ell\bar{\ell}}$')
ax.set_zlabel(r'$\mathrm{NN}$')

fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/20_10/nn_vs_mc.pdf')
#nn.reshape(eta_l_grid.shape)