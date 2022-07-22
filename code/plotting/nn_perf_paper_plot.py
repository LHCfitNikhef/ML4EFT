import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

import quad_clas.analyse.analyse as analyse

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 26})
rc('text', usetex=True)

n_cols = 3
n_rows = 3

fig, ax = plt.subplots(n_rows, n_cols, figsize=(20, 20))



# path_to_models = {'lin': {
#     'ctgre': [-10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_lin'],
#     'cut': [10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_quad']},
#     'quad': {'ctgre': [-10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_quad'],
#              'cut': [10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctu1_quad']}}

path_to_models = {'lin': {
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_lin'},
    'quad': {'ctgre_ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_quad',
             'cut_cut': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctu1_quad'}}

event_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/sm/events_0.pkl.gz'
events_sm = pd.read_pickle(event_path)
events_sm = events_sm.iloc[1:,:]

analyser = analyse.Analyse(path_to_models)
analyser.build_model_dict()

#analyser.point_by_point_comp(events_sm, {'ctgre': -2, 'cut': 0}, ['y', 'm_tt'], 'tt', 'lin')



analyser.accuracy_heatmap('ctgre', 'lin', 'tt', 0.5, 0, epoch=-1, ax=ax[0, -1])
analyser.accuracy_heatmap('ctgre_ctgre', 'quad', 'tt', 0.5, 0, epoch=-1, ax=ax[1, -1])
analyser.accuracy_heatmap('cut_cut', 'quad', 'tt', 0.5, 0, epoch=-1, ax=ax[2, -1])

# for i, rep in enumerate(reps):
#     im = self.accuracy_heatmap(c_name, order, process, cut, rep, epoch, grid[i])


fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/21_07/test.pdf')