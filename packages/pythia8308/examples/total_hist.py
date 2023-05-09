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

df_hard = pd.read_csv('kinematics_vector_hard_no_nu_bla.csv')
df1 = pd.read_csv('kinematics_vector_with_nu_no_prun.csv')
df2 = pd.read_csv('kinematics_vector_with_nu_prun.csv')

df3 = pd.read_csv('kinematics_vector_no_nu_no_prun.csv')
df4 = pd.read_csv('kinematics_vector_no_nu_with_prun.csv')


coeff = ["a"]
events_shower = []
for c in coeff:
    events_shower.append(df1)
    # events_shower.append(df2)
    # events_shower.append(df3)
    events_shower.append(df4)


feature_dict = {'h_l_pt': r'$p_T^{\ell}\;[\mathrm{GeV}]$',
            'h_lbar_pt': r'$p_T^{\bar{\ell}}\;[\mathrm{GeV}]$',
            'h_l_pt_lead': r'$p_T^{\ell}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            'h_l_pt_trail': r'$p_T^{\ell}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            'h_l_eta': r'$\eta_\ell$',
            'h_lbar_eta': r'$\eta_{\bar{\ell}}$',
            'h_l_eta_lead': r'$\eta_\ell\;(\mathrm{leading})$',
            'h_l_eta_trail': r'$\eta_\ell\;(\mathrm{trailing})$',
            'h_ll_pt': r'$p_T^{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            'h_ll_m': r'$m_{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            'h_l_abs_diff_phi': r'$\Delta\phi(\ell, \bar{\ell})$',
            'h_l_diff_abs_eta': r'$\Delta\eta(\ell, \bar{\ell})$',
            'h_b_pt_lead': r'$p_T^{b}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            'h_b_pt_trail': r'$p_T^{b}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            'h_b_eta_lead': r'$\eta_{b}\;(\mathrm{leading})$',
            'h_b_eta_trail': r'$\eta_{b}\;(\mathrm{trailing})$',
            'h_bb_pt': r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$',
            'h_bb_m': r'$m_{b\bar{b}}\;[\mathrm{GeV}]$'
         }

legend_labels = [r'hadron_baseline', r'hadron_with_prun' , r'particle']

fig = features.plot_features(df_hard, events_shower, feature_dict, legend_labels)
plt.savefig('hard_kinematics_hadron_baseline.png')

