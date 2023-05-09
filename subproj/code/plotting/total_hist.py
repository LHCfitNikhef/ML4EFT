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

df_hard = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/groom100000/hard/tt_sm/zcut_0.0beta_0.5job_0.pkl.gz', compression='infer')
df1 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/groom100000/event/tt_sm/zcut_0.2beta_0.5job_0.pkl.gz', compression='infer')
df2 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/groom100000/event/tt_sm/zcut_0.3beta_0.5job_0.pkl.gz', compression='infer')
df3 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/groom100000/event/tt_sm/zcut_0.4beta_0.5job_0.pkl.gz', compression='infer')
df4 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/groom100000/event/tt_sm/zcut_0.5beta_0.5job_0.pkl.gz', compression='infer')

# df_hard = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/event/tt_sm/tt_sm_1.pkl.gz')
# df1 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/event/tt_ctd8_ctd8/tt_ctd8_ctd8_1.csv')
# df2 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/event/tt_cQu8_cQu8/tt_cQu8_cQu8_1.csv')
# df3 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/output/test/tt_smrec_soft0.2.csv')
# df4 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/output/test/tt_ctd8_ctd8soft_rec0.2.csv')


coeff = ["a"]
events_shower = []
for c in coeff:
    events_shower.append(df1)
    events_shower.append(df2)
    # events_shower.append(df3)
    # events_shower.append(df4)


feature_dict = {'pt_l1': r'$p_T^{\ell}\;[\mathrm{GeV}]$',
            'pt_l2': r'$p_T^{\bar{\ell}}\;[\mathrm{GeV}]$',
            'pt_l_leading': r'$p_T^{\ell}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            'pt_l_trailing': r'$p_T^{\ell}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            'eta_l1': r'$\eta_\ell$',
            'eta_l2': r'$\eta_{\bar{\ell}}$',
            'eta_l_leading': r'$\eta_\ell\;(\mathrm{leading})$',
            'eta_l_trailing': r'$\eta_\ell\;(\mathrm{trailing})$',
            'pt_ll': r'$p_T^{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            'm_ll': r'$m_{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            'DeltaPhi_ll': r'$\Delta\phi(\ell, \bar{\ell})$',
            'DeltaEta_ll': r'$\Delta\eta(\ell, \bar{\ell})$',
            'pt_b_leading': r'$p_T^{b}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            'pt_b_trailing': r'$p_T^{b}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            'eta_b_leading': r'$\eta_{b}\;(\mathrm{leading})$',
            'eta_b_trailing': r'$\eta_{b}\;(\mathrm{trailing})$',
            'pt_bb': r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$',
            'm_bb': r'$m_{b\bar{b}}\;[\mathrm{GeV}]$'
         }

legend_labels = [r'hard',r'zcut_0.2beta_0.5', r'zcut_0.3beta_0.5']

fig = features.plot_features(df_hard, events_shower, feature_dict, legend_labels)
plt.savefig('/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/groom_Z_h_0,2,4,5.png')

