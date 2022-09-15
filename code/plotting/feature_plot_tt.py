# script that plots differential xsection distributions with
# as input a pandas datafram obtained from a lhe file

import ml4eft.plotting.features as features
import pandas as pd
import os

plot_directory = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/15_08'

df_sm = pd.read_pickle("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt_llvlvlbb/tt_sm/events_0.pkl.gz").iloc[1:,:]
df_eft = pd.read_pickle("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt_llvlvlbb/tt_cQj18/events_0.pkl.gz").iloc[1:,:]


coeff = ["ctGRe", "cQj18", "cQj38", "ctj8", "ctu8", "cQu8", "cQd8", "ctd8"]

dfs_eft = []
for c in coeff:
    df = pd.read_pickle("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt_llvlvlbb/tt_{}_{}/events_0.pkl.gz".format(c, c)).iloc[1:,:]
    dfs_eft.append(df)


# x_labels = [r'$p_T^{\ell}\;[\mathrm{GeV}]$',
#             r'$p_T^{\bar{\ell}}\;[\mathrm{GeV}]$',
#             r'$p_T^{l2}\;[\mathrm{GeV}]$',
#             r'$p_T^{b}\;[\mathrm{GeV}]$',
#             r'$\eta_b$',
#             r'$\Delta R(l, b)$',
#             r'$E_T^{\mathrm{miss}}\;[\mathrm{GeV}]$'
#            ]

x_labels = [r'$p_T^{\ell}\;[\mathrm{GeV}]$',
            r'$p_T^{\bar{\ell}}\;[\mathrm{GeV}]$',
            r'$p_T^{\ell}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            r'$p_T^{\ell}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            r'$\eta_\ell$',
            r'$\eta_{\bar{\ell}}$',
            r'$\eta_\ell\;(\mathrm{leading})$',
            r'$\eta_\ell\;(\mathrm{trailing})$',
            r'$p_T^{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            r'$m_{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            r'$\Delta\phi(\ell, \bar{\ell})$',
            r'$\Delta\eta(\ell, \bar{\ell})$',
            r'$p_T^{b}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            r'$p_T^{b}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            r'$\eta_{b}\;(\mathrm{leading})$',
            r'$\eta_{b}\;(\mathrm{trailing})$',
            r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$',
            r'$m_{b\bar{b}}\;[\mathrm{GeV}]$'
           ]

feature_names = ['pt_l1',
                         'pt_l2',
                         'pt_l_leading',
                         'pt_l_trailing',
                         'eta_l1',
                         'eta_l2',
                         'eta_l_leading',
                         'eta_l_trailing',
                         'pt_ll',
                         'm_ll',
                         'DeltaPhi_ll',
                         'DeltaEta_ll',
                         'pt_b_leading',
                         'pt_b_trailing',
                         'eta_b_leading',
                         'eta_b_trailing',
                         'pt_bb',
                         'm_bb']

labels = [r'$c_{tG}=-10$', r'$c_{Qq}^{(1,8)}=10$', r'$c_{Qq}^{(3,8)}=10$', r'$c_{tq}^{(8)}=10$', r'$c_{tu}^{(8)}=10$',r'$c_{Qu}^{(8)}=10$',
          r'$c_{Qd}^{(8)}=10$', r'$c_{td}^{(8)}=10$', r'$\mathrm{SM}$']
#labels = [r'$\mathrm{SM}$', r'$c_{Qd}^{(8)}=10$', r'$c_{td}^{(8)}=10$']
fig = features.plot_features(df_sm, dfs_eft, feature_names, labels=labels, x_labels=x_labels)
fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/11_09/features_tt_quad.pdf')