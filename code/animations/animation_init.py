#%%
from ml4eft.analyse.animate import Animate
import ml4eft.analyse.analyse as analyse
import ml4eft.preproc.constants as constants
import numpy as np
import pandas as pd
import os, sys
#%%
# 1D

# zh llbb

# path_to_models = {'lin': {
#     'cuu_quad': '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_llbb/ltd/model_cuu_quad_v3',
#     'cuu_quad': '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_llbb/ltd/model_cuu_quad_v3'}}

# tt
#

order = 'quad'
save_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/20_10'

path_to_models_root = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_mtt_y/2022/10/15'
path_to_models = analyse.Analyse.build_path_dict(path_to_models_root, order, prefix='model')

if order == "quad":
    del path_to_models['lin']

analyser = analyse.Analyse(path_to_models)

x = np.linspace(1.45, 3.0, 200)
x = np.stack((np.zeros(len(x)), x), axis=-1)


df = pd.DataFrame(x, columns=['y', 'm_tt'])

anim = Animate(c={'ctGRe': 0, 'ctu8': 2}, frames=10)
anim_tt = anim.make_animation_1d(analyser, df)

anim_tt.save(os.path.join(save_path, 'anim_ctu8_ctu8.gif'))

sys.exit()

# 2D

# first create a grid in phase space

mz = constants.mz
mh = constants.mh
mt = constants.mt

s = 14 ** 2
epsilon = 1e-2
mtt_min, mtt_max = 0.5, 2
y_min, y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)

x_spacing, y_spacing = 1e-2, 0.01
mtt_span = np.arange(mtt_min, mtt_max, x_spacing)
y_span = np.arange(y_min, y_max, y_spacing)

mtt_grid, y_grid = np.meshgrid(mtt_span, y_span)
grid = np.c_[y_grid.ravel(), mtt_grid.ravel()]

df = pd.DataFrame(grid, columns=['y', 'm_tt'])

anim = Animate(c={'ctgre': 2, 'cut': 0}, frames=150)

anim_tt_2d = anim.make_animation_2d(analyser, df, 'ctgre_ctgre', 'quad', 'tt', mtt_grid.shape)
anim_tt_2d.save(os.path.join(save_path, 'anim_2d_v2.gif'))

# animate_learning_2d(df, analyser, mc_reps=30,
#                     path_to_model='/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/mc_run_{mc_run}',
#                     network_size=[2, 30, 30, 30, 30, 30, 1],
#                     c1=10,
#                     c2=0,
#                     lin=True,
#                     quad=False,
#                     cross=False,
#                     path_sm_data=None)
