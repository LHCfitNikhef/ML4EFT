# script that plots differential xsection distributions with
# as input a pandas datafram obtained from a lhe file

import quad_clas.plotting.features as features
import pandas as pd
import os

plot_directory = '/Users/jaco/Documents/ML4EFT/plots/2022/24_02'

df_sm = pd.read_pickle("/Users/jaco/Documents/ML4EFT/training_data/zh_llbb/sm/events_0.pkl.gz")
df_eft = pd.read_pickle("/Users/jaco/Documents/ML4EFT/training_data/zh_llbb/lin/chw/events_1.pkl.gz")

x_labels = [r'$p_T^Z$',
            r'$p_T^{b_1}\;[\mathrm{GeV}]$',
            r'$p_T^{b_2}\;[\mathrm{GeV}]$',
            r'$m_{b\bar{b}}\;[\mathrm{GeV}]$',
            r'$\Delta R(b_1, b_2)$',
            r'$\Delta\phi(b, bb)$',
            r'$|\Delta \eta(Z, bb)|$',
            r'$m_{ll}$',
            r'$\Delta\phi(b, l)$'
           ]

fig = features.plot_features(df_sm, df_eft, eft_label=r'$\mathrm{cHW}=50$', x_labels=x_labels)
fig.savefig(os.path.join(plot_directory, 'chw_lin_features.pdf'))