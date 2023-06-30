import wget
import tarfile
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

import ml4eft.core.classifier as classifier
import ml4eft.analyse.analyse as analyse
import ml4eft.plotting.features as features
import features2vs2

# feature_dict = {'pt_l1': r'$p_T^{\ell}\;[\mathrm{GeV}]$',
#             'pt_l2': r'$p_T^{\bar{\ell}}\;[\mathrm{GeV}]$',
#             'pt_l_leading': r'$p_T^{\ell}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
#             'pt_l_trailing': r'$p_T^{\ell}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
#             'eta_l1': r'$\eta_\ell$',
#             'eta_l2': r'$\eta_{\bar{\ell}}$',
#             'eta_l_leading': r'$\eta_\ell\;(\mathrm{leading})$',
#             'eta_l_trailing': r'$\eta_\ell\;(\mathrm{trailing})$',
#             'pt_ll': r'$p_T^{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
#             'm_ll': r'$m_{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
#             'DeltaPhi_ll': r'$|\Delta\phi(\ell, \bar{\ell})|$',
#             'DeltaEta_ll': r'$\Delta\eta(\ell, \bar{\ell})$',
#             'pt_b_leading': r'$p_T^{b}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
#             'pt_b_trailing': r'$p_T^{b}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
#             'eta_b_leading': r'$\eta_{b}\;(\mathrm{leading})$',
#             'eta_b_trailing': r'$\eta_{b}\;(\mathrm{trailing})$',
#             'pt_bb': r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$',
#             'm_bb': r'$m_{b\bar{b}}\;[\mathrm{GeV}]$'
#          }
feature_dict = {'pt_bb': r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$'}

legend_labels = [r'$\mathrm{Particle}\; \mathrm{lvl} \;\mathrm{sm}$',
                 r'$\mathrm{Hadron}\; \mathrm{lvl} \;\mathrm{sm} \; z_{cut} = 0 \; \beta = 0$',
                 r'$\mathrm{Hadron}\; \mathrm{lvl} \;\mathrm{sm} \; z_{cut} = 0.2 \; \beta = 0.5$',
                 r'$\mathrm{Hadron}\; \mathrm{lvl} \;\mathrm{sm} \; z_{cut} = 0.4 \; \beta = 0$']

df1 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/thesis_pim/data/groom_analysis/combined/0_0_hard_combined.pkl.gz', compression='infer')
df2 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/thesis_pim/data/groom_analysis/combined/0_0_event_combined.pkl.gz', compression='infer')
df3 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/thesis_pim/data/groom_analysis/combined/0.2_0.5_event_combined.pkl.gz', compression='infer')
df4 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/thesis_pim/data/groom_analysis/combined/0.4_0_event_combined.pkl.gz', compression='infer')

fig = features2vs2.plot_features_groom(df1,df2,df3,df4, feature_dict, legend_labels)

plt.savefig('/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/groom_check.png')
