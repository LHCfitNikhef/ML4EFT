# script that plots differential xsection distributions with
# as input a pandas datafram obtained from a lhe file

import quad_clas.plotting.features as features
import pandas as pd
import os

plot_directory = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/15_08'

df_sm = pd.read_pickle("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/zh_llbb_final/zh_sm/events_0.pkl.gz").iloc[1:,:]

coeff = ["cHu", "cHd", "cHj1", "cHj3", "cbHRe", "cHW", "cHWB"]
dfs_eft = []
for c in coeff:
    dfs_eft.append(pd.read_pickle("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/zh_llbb_final/zh_{}/events_0.pkl.gz".format(c,c)).iloc[1:,:])



x_labels = [r'$p_T^Z\;[\mathrm{GeV}]$',
            r'$p_T^{b}\;[\mathrm{GeV}]$',
            r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$',
            r'$\Delta R(b_1, b_2)$',
            r'$\Delta\phi(b, b\bar{b})$',
            r'$|\Delta \eta(Z, b\bar{b})|$',
            r'$m_{ll}\;[\mathrm{GeV}]$',
            r'$\Delta\phi(b, l)$'
           ]

feature_list = ["pt_z", "pt_b", "pt_bbar", "deltaR_bb", "deltaPhi_b_bb", "deltaEta_z_bb", "m_ll", "deltaPhi_l_b"]

fig = features.plot_features(df_sm, dfs_eft, feature_list, labels=[r'$\mathrm{SM}$', r'$c_{\varphi u}=10$', r'$c_{\varphi d}=-10$', r'$c_{\varphi q}^{(1)}=-10$', r'$c_{\varphi q}^{(3)}=10$', r'$c_{b \varphi}=-10$', r'$c_{\varphi W}=10$',  r'$c_{\varphi WB}=10$'], x_labels=x_labels)
fig.savefig(os.path.join(plot_directory, 'zh_lin_dist.pdf'))