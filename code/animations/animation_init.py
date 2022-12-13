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
save_path = '/data/theorie/jthoeve/ML4EFT/plots/2022/02_11'

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



# 2D

# s = 14 ** 2
# mtt_min, mtt_max = 1.45, 3.1
# y_min, y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
#
# x_spacing, y_spacing = 1e-2, 0.01
# mtt_span = np.arange(mtt_min, mtt_max, x_spacing)
# y_span = np.arange(y_min, y_max, y_spacing)
#
# mtt_grid, y_grid = np.meshgrid(mtt_span, y_span)
# grid = np.c_[y_grid.ravel(), mtt_grid.ravel()]
#
# df = pd.DataFrame(grid, columns=['y', 'm_tt'])
#
# anim = Animate(c={'ctGRe': 2, 'ctu8': 0}, frames=300)
#
# anim_tt = anim.make_animation_2d(analyser, df, 'ctu8_ctu8', 'quad', 'tt', mtt_grid.shape, text=r'$c_{tu}^{(8)}\cdot c_{tu}^{(8)}$')
# anim_tt.save(os.path.join(save_path, 'anim_ctu8_ctu8_2d.gif'))


