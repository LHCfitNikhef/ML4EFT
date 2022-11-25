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

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 30})
rc('text', usetex=True)

coeff_dict = {"ctGRe": r'$c_{tG}$', "ctu8": r'$c_{tu}^{(8)}$'}

# LINEAR
samples_nn_lin_mtt = '/data/theorie/pherbsch/ML4EFT/results/nn_ctu8_ctGRe_subproj/posterior.json'
# samples_nn_lin_mtt_y = '/data/theorie/jthoeve/ns_samples/tt_parton/nn_glob_lin_mtt_y/posterior.json'
# samples_nn_lin_mtt = '/data/theorie/jthoeve/ns_samples/tt_parton/nn_glob_lin_mtt/posterior.json'

# samples_binned_lin_mtt_y_c = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_lin_mtt_y_c/posterior.json'
# samples_binned_lin_mtt_c = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_lin_mtt_c/posterior.json'
# samples_binned_lin_mtt_y_f = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_lin_mtt_y_f/posterior.json'
# samples_binned_lin_mtt_f = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_lin_mtt_f/posterior.json'

# samples_truth_lin_mtt = '/data/theorie/jthoeve/ns_samples/tt_parton/truth_glob_lin_mtt/posterior.json'
# samples_truth_lin_mtt_y = '/data/theorie/jthoeve/ns_samples/tt_parton/truth_glob_lin_mtt_y/posterior.json'

# QUADRATIC
# samples_nn_quad_mtt_y_ptt = '/data/theorie/jthoeve/ns_samples/tt_parton/nn_glob_quad_all/posterior.json'
# samples_nn_quad_mtt_y = '/data/theorie/jthoeve/ns_samples/tt_parton/nn_glob_quad_mtt_y/posterior.json'
# samples_nn_quad_mtt = '/data/theorie/jthoeve/ns_samples/tt_parton/nn_glob_quad_mtt/posterior.json'

# samples_binned_quad_mtt_y_c = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_quad_mtt_y_c/posterior.json'
# samples_binned_quad_mtt_c = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_quad_mtt_c/posterior.json'
# samples_binned_quad_mtt_y_f = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_quad_mtt_y_f/posterior.json'
# samples_binned_quad_mtt_f = '/data/theorie/jthoeve/ns_samples/tt_parton/binned_glob_quad_mtt_f/posterior.json'

# samples_truth_quad_mtt = '/data/theorie/jthoeve/ns_samples/tt_parton/truth_glob_quad_mtt/posterior.json'
# samples_truth_quad_mtt_y = '/data/theorie/jthoeve/ns_samples/tt_parton/truth_glob_quad_mtt_y/posterior.json'

# PLOT 1

df_plot_1 = [Analyse.posterior_loader(samples_nn_lin_mtt)
            # ,Analyse.posterior_loader(samples_binned_lin_mtt_y_f),
            #  Analyse.posterior_loader(samples_truth_lin_mtt_y),
            #  Analyse.posterior_loader(samples_nn_lin_mtt_y)
             ]

labels_plot_1 = [r'$\mathrm{Binning}\:1\;(m_{t\bar{t}}, y_{t\bar{t}})$'
                # ,r'$\mathrm{Binning}\:2\;(m_{t\bar{t}}, y_{t\bar{t}})$',
                #  r'$\mathrm{Unbinned\;exact}\;(m_{t\bar{t}}, y_{t\bar{t}})$',
                #  r'$\mathrm{Unbinned\;ML}\;(m_{t\bar{t}}, y_{t\bar{t}})$',
                #  r'$\mathrm{SM}$'
                 ]

# # PLOT 2

# df_plot_2 = [Analyse.posterior_loader(samples_binned_quad_mtt_y_c),
#              Analyse.posterior_loader(samples_binned_quad_mtt_y_f),
#              Analyse.posterior_loader(samples_truth_quad_mtt_y),
#              Analyse.posterior_loader(samples_nn_quad_mtt_y)
#              ]

# labels_plot_2 = [r'$\mathrm{Binning}\:1\;(m_{t\bar{t}}, y_{t\bar{t}})$',
#                  r'$\mathrm{Binning}\:2\;(m_{t\bar{t}}, y_{t\bar{t}})$',
#                  r'$\mathrm{Unbinned\;exact}\;(m_{t\bar{t}}, y_{t\bar{t}})$',
#                  r'$\mathrm{Unbinned\;ML}\;(m_{t\bar{t}}, y_{t\bar{t}})$',
#                  r'$\mathrm{SM}$']

# # PLOT 3

# df_plot_3 = [Analyse.posterior_loader(samples_binned_lin_mtt_c),
#              Analyse.posterior_loader(samples_binned_lin_mtt_f),
#              Analyse.posterior_loader(samples_truth_lin_mtt),
#              Analyse.posterior_loader(samples_nn_lin_mtt)]

# labels_plot_3 = [r'$\mathrm{Binning}\:1\;(m_{t\bar{t}})$',
#                  r'$\mathrm{Binning}\:2\;(m_{t\bar{t}})$',
#                  r'$\mathrm{Unbinned\;exact}\;(m_{t\bar{t}})$',
#                  r'$\mathrm{Unbinned\;ML}\;(m_{t\bar{t}})$',
#                  r'$\mathrm{SM}$']

# # PLOT 4

# df_plot_4 = [Analyse.posterior_loader(samples_binned_quad_mtt_c),
#              Analyse.posterior_loader(samples_binned_quad_mtt_f),
#              Analyse.posterior_loader(samples_truth_quad_mtt),
#              Analyse.posterior_loader(samples_nn_quad_mtt)
#              ]

# labels_plot_4 = [r'$\mathrm{Binning}\:1\;(m_{t\bar{t}})$',
#                  r'$\mathrm{Binning}\:2\;(m_{t\bar{t}})$',
#                  r'$\mathrm{Unbinned\;exact}\;(m_{t\bar{t}})$',
#                  r'$\mathrm{Unbinned\;ML}\;(m_{t\bar{t}})$',
#                  r'$\mathrm{SM}$']

dfs = [df_plot_1
# , df_plot_2, df_plot_3, df_plot_4
]
labels = [labels_plot_1
# , labels_plot_2, labels_plot_3, labels_plot_4
 ]

titles = [
    r"$95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-2}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$"
    # ,r"$95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-4}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$",
    # r"$95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-2}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$",
    # r"$95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-4}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$"
    ]

order = [False
# , True, False, True
]

plotter = EllipsePlotter()

fig = plt.figure(figsize=(20, 20))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

n_cols, n_rows = 1,1
# 2, 2
fig = plt.figure(figsize=(n_cols * 10, n_rows * 10))
grid = plt.GridSpec(n_rows, n_cols, hspace=0.1, wspace=0.1)

for i, df in enumerate(dfs):
    row_idx = i // 2
    col_idx = i % 2
    ax = fig.add_subplot(grid[row_idx, col_idx])

    if col_idx == 1:
        ax.set_xlim(-0.22, 0.3)

        plotter.plot(ax, df, coeff1="ctGRe", coeff2="ctu8",
                     ax_labels=[coeff_dict["ctGRe"], coeff_dict["ctu8"]], kde=order[i],
                     labels=labels[i], loc="lower right")
    else:
        plotter.plot(ax, df, coeff1="ctGRe", coeff2="ctu8",
                     ax_labels=[coeff_dict["ctGRe"], coeff_dict["ctu8"]], kde=order[i],
                     labels=labels[i], loc="upper left")

    if col_idx == 1:
        ax.set(ylabel=None)
    if row_idx == 0:
        ax.set(xlabel=None)
        ax.set_title(titles[i], fontsize=25)

grid.tight_layout(fig)

fig.savefig('/data/theorie/pherbsch/ML4EFT/results/nn_ctu8_ctGRe_subproj/ctu8_ctGRe_plot')
