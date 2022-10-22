import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import os

import ml4eft.analyse.analyse as analyse

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 19})
rc('text', usetex=True)


#fig = plt.figure(figsize=(16, 8.533))
fig = plt.figure(figsize=(16, 10))
grid = plt.GridSpec(2, 3, hspace=0.4, wspace=0.4)

ax_1 = fig.add_subplot(grid[0, 0])
ax_2 = fig.add_subplot(grid[0, 1])
ax_3 = fig.add_subplot(grid[0, 2])
ax_4 = fig.add_subplot(grid[1, 0])
ax_5 = fig.add_subplot(grid[1, 1:])

order = 'quad'
c_name = 'ctGRe_ctGRe'

# path_to_models = {'lin': {
#     'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe'},
#     'quad': {'ctgre_ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe_ctGRe',
#              'cut_cut': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctu1_ctu1'}}

path_to_models_root = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_mtt_y/2022/10/15'
path_to_models = analyse.Analyse.build_path_dict(path_to_models_root, 'quad', prefix='model')
del path_to_models['lin']


path_to_runcard = os.path.join(path_to_models[order][c_name], 'mc_run_0', 'run_card.json')

analyser = analyse.Analyse(path_to_models)
analyser.build_model_dict()



event_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/observed_data/tt_parton_sm/events_0.pkl.gz'
events_sm = pd.read_pickle(event_path)
events_sm = events_sm.iloc[1:, :].sample(1000)

analyser.plot_loss_overview('ctGRe_ctGRe', 'quad', ax=ax_4, rep=27)

analyser.point_by_point_comp_med(events_sm, {'ctGRe': 2, 'ctu8': 0}, ['y', 'm_tt'], 'tt', 'quad', ax=ax_1, text=r'$c=c_{tG}=2\;\rm{(quadratic)}$')

analyser.plot_accuracy_1d(c={'ctGRe': 2, 'ctu8': 0}, c_name='ctGRe_ctGRe', process='tt', order='quad', mx_cut=[1.45, 3], epoch=-1, ax=ax_5, text=r'$c=c_{tG}=2\;\rm{(quadratic)}$')



path_to_models_root = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_mtt/2022/10/16'
path_to_models = analyse.Analyse.build_path_dict(path_to_models_root, order='quad', prefix='model')

#fig1, ax = plt.subplots(figsize=(10, 10))
ax_2, ax_3 = analyser.accuracy_heatmap('ctGRe_ctGRe', 'quad', 'tt', mx_cut=[1.45, 3], epoch=-1, ax=[ax_2, ax_3], text=r'$c_{tG}\cdot c_{tG}$')
#fig1.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/16_10/nn_accuracy_overview_test.pdf')
# for i, rep in enumerate(reps):
#     im = self.accuracy_heatmap(c_name, order, process, cut, rep, epoch, grid[i])
grid.tight_layout(fig)
fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/16_10/nn_accuracy_overview.pdf')

#fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/21_07/test.pdf')