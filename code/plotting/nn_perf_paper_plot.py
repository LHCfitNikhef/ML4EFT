import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

import quad_clas.analyse.analyse as analyse

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 19})
rc('text', usetex=True)


fig = plt.figure(figsize=(16, 10))
grid = plt.GridSpec(2, 3, hspace=0.4, wspace=0.4)

ax_1 = fig.add_subplot(grid[0, 0])
ax_2 = fig.add_subplot(grid[0, 1])
ax_3 = fig.add_subplot(grid[0, 2])
ax_4 = fig.add_subplot(grid[1, 0])
ax_5 = fig.add_subplot(grid[1, 1:])


# path_to_models = {'lin': {
#     'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe'},
#     'quad': {'ctgre_ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe_ctGRe',
#              'cut_cut': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctu1_ctu1'}}

path_to_models = {
    'quad': {'ctgre_ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe_ctGRe',
             'cut_cut': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctu1_ctu1'}}

# path_to_models = {'lin': {
#     'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe'}}

event_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/tt_sm/events_0.pkl.gz'
events_sm = pd.read_pickle(event_path)
events_sm = events_sm.iloc[1:, :].sample(5000)

analyser = analyse.Analyse(path_to_models)
analyser.build_model_dict()

analyser.plot_loss_overview('ctgre_ctgre', 'quad', ax=ax_4)

analyser.point_by_point_comp_med(events_sm, {'ctgre': 2, 'cut': 0}, ['y', 'm_tt'], 'tt', 'quad', ax=ax_1, text=r'$c=c_{tG}=2\;\rm{(quadratic)}$')

analyser.plot_accuracy_1d({'ctgre': 2, 'cut': 0}, 'tt', 'quad', cut=0.5, epoch=-1, ax=ax_5, text=r'$c=c_{tG}=2\;\rm{(quadratic)}$')

path_to_models = {'lin': {
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe'},
    'quad': {'ctgre_ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctGRe_ctGRe',
             'cut_cut': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctu1_ctu1'}}

analyser = analyse.Analyse(path_to_models)
analyser.build_model_dict()

analyser.accuracy_heatmap('ctgre_ctgre', 'quad', 'tt', 0.5, epoch=-1, ax=[ax_2, ax_3], text=r'$c_{tG}\cdot c_{tG}$')
#analyser.accuracy_heatmap('ctgre_ctgre', 'quad', 'tt', 0.5, 0, epoch=-1, ax=ax[1, -1])
#analyser.accuracy_heatmap('cut_cut', 'quad', 'tt', 0.5, 0, epoch=-1, ax=ax[2, -1])

# for i, rep in enumerate(reps):
#     im = self.accuracy_heatmap(c_name, order, process, cut, rep, epoch, grid[i])
grid.tight_layout(fig)
fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/16_08/test.pdf')

#fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/21_07/test.pdf')