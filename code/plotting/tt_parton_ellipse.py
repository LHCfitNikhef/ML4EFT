import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from matplotlib import rc
import seaborn as sns
import matplotlib.patches as mpatches
import itertools
import os
from ml4eft.analyse.analyse import Analyse
from ellipse_plotter_new import EllipsePlotter


rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 40})
rc('text', usetex=True)

#samples_nn_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/nn/mtt_y_high/posterior.json'

samples_nn_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/tt_parton/nn_mtt_y_v3/posterior.json'
samples_truth_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/tt_parton/truth_mtt_y/posterior.json'
# samples_binned_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/binned/mzh_y/posterior.json'

samples_binned_path_1b = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/tt_parton/binned_mtt_y_1_b/posterior.json'
samples_binned_path_2b = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/tt_parton/binned_mtt_y_2_b/posterior.json'
samples_binned_path_6b = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/tt_parton/binned_mtt_y_6_b/posterior.json'

coeff_dict = {"ctGRe": r'$c_{tG}$', "ctu1": r'$c_{tu}^{1}$'}

df_nn = Analyse.posterior_loader(samples_nn_path)
df_truth = Analyse.posterior_loader(samples_truth_path)


df_binned_1b = Analyse.posterior_loader(samples_binned_path_1b)
df_binned_2b = Analyse.posterior_loader(samples_binned_path_2b)
df_binned_6b = Analyse.posterior_loader(samples_binned_path_6b)

df_plot_1 = [df_binned_1b, df_binned_6b]
#df_plot_2 = [df_binned_2b, df_binned_6b]
df_plot_2 = [df_binned_2b, df_binned_6b, df_nn, df_truth]

dfs = [df_plot_1, df_plot_2]

labels_plot_1 = [r'$m_{t\bar{t}}\in [0.5, \infty)\;\mathrm{TeV}$',
                              r'$m_{t\bar{t}}\in [0.5, 0.6, 0.8, 1.0, 1.2, 1.5, \infty)\;\mathrm{TeV}$']

# labels_plot_2 = [r'$m_{t\bar{t}}\in [0.5, 1.0, \infty)\;\mathrm{TeV}$',
#                  r'$m_{t\bar{t}}\in [0.5, 0.6, 0.8, 1.0, 1.2, 1.5, \infty)\;\mathrm{TeV}$']

labels_plot_2 = [r'$m_{t\bar{t}}\in [0.5, 1.0, \infty)\;\mathrm{TeV}$',
                 r'$m_{t\bar{t}}\in [0.5, 0.6, 0.8, 1.0, 1.2, 1.5, \infty)\;\mathrm{TeV}$',
                 r'$\mathrm{ML\;model}\;(m_{t\bar{t}}, Y)$',
                 r'$\mathrm{Analytical}\;(m_{t\bar{t}}, Y)$'
                 ]


labels = [labels_plot_1, labels_plot_2]

plotter = EllipsePlotter()

fig = plt.figure(figsize=(20, 10))
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i, df in enumerate(dfs):
    ax = fig.add_subplot(1, 2, i + 1)

    ax = plotter.plot(ax, dfs[i], coeff1="ctGRe", coeff2="ctu1",
                      ax_labels=[coeff_dict["ctGRe"], coeff_dict["ctu1"]], kde=True,
                      labels=labels[i])

# ax, hndls = plotter.plot(ax, [df_nn, df_truth, df_binned], coeff1="ctgre", coeff2="cut",
#                          ax_labels=[coeff_dict["ctgre"], coeff_dict["cut"]], samples = [True, True, True], labels=[r'$\mathrm{ML\;Model}\;(m_{t\bar{t}}, Y)$',
#                                                                                      r'$\mathrm{Analytical}\;(m_{t\bar{t}}, Y)$',
#                                                                                      r'$m_{t\bar{t}}\in [0.5, 1.0, \infty)\;\mathrm{TeV}$'])



# ax.axvline(df_nn["ctgre"].mean() - df_nn["ctgre"].std(), color='k', linestyle='dashed')
# ax.axvline(df_nn["ctgre"].mean() + df_nn["ctgre"].std(), color='k', linestyle='dashed')
# ax.axhline(df_nn["cut"].mean() + df_nn["cut"].std(), color='k', linestyle='dashed')
# ax.axhline(df_nn["cut"].mean() - df_nn["cut"].std(), color='k', linestyle='dashed')
fig.tight_layout()

fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/17_08/tt_parton_ellipse_v3.pdf')

