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

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 26})
rc('text', usetex=True)

# tt -> llvlvlbb

# n_reps = 24
# coeff_dict = {"ctd8": r'$c_{td}^{(8)}$', "ctGRe": r'$c_{tG}$', "cQd8": r'$c_{Qd}^{(8)}$', "cQj18": r'$c_{Qq}^{(1,8)}$',
#               "cQj38": r'$c_{Qq}^{(3,8)}$', "cQu8": r'$c_{Qu}^{(8)}$', "ctj8": r'$c_{qt}^{(8)}$',
#               "ctu8": r'$c_{tu}^{(8)}$'}
#
# samples_median = '/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/nn_glob_all_quad_v8/posterior.json'
# samples_rep = '/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/nn_glob_all_env/rep_{}/posterior.json'
#
# samples_rep_all = [samples_rep.format(rep) for rep in np.arange(1, n_reps + 1)]
#
# paths_samples = [samples_median] + samples_rep_all
#
# labels = [r"$\mathrm{Unbinned}\;\mathrm{ML}\;(18\;\mathrm{features},\;\mathrm{median})$",
#           r"$\mathrm{Unbinned}\;\mathrm{ML}\;(18\;\mathrm{features},\;68\:\%\:\mathrm{C.L.\:replicas})$",
#           r'$\mathrm{SM}$']
#
# all_together= True
#
# plot_ranges = {"ctd8": (-1, 0.7), "ctGRe": (-0.3, 0.25), "cQd8": (-0.25, 0.25), "cQj18": (-0.1, 0.1),
#               "cQj38": (-0.125, 0.125), "cQu8": (-0.15, 0.1), "ctj8": (-0.2, 0.3),
#               "ctu8": (-1, 0.4)}

# zh -> llbb

n_reps = 49
coeff_dict = {"cHu": r'$c_{\varphi u}$', "cHd": r'$c_{\varphi d}$', "cHj1": r'$c_{\varphi q}^{(1)}$', "cHj3": r'$c_{\varphi q}^{(3)}$',
              "cbHRe": r'$c_{b\varphi}$', "cHW": r'$c_{\varphi W}$', "cHWB": r'$c_{\varphi WB}$'}

samples_median = '/data/theorie/jthoeve/ns_samples/zh_llbb/nn_glob_all_quad3/posterior.json'
samples_rep = '/data/theorie/jthoeve/ns_samples/zh_llbb/nn_glob_all_rep/rep_{}/posterior.json'

samples_rep_all = [samples_rep.format(rep) for rep in np.arange(1, n_reps + 1)]

paths_samples = [samples_median] + samples_rep_all

labels = [r"$\mathrm{Unbinned}\;\mathrm{ML}\;(7\;\mathrm{features},\;\mathrm{median})$",
          r"$\mathrm{Unbinned}\;\mathrm{ML}\;(7\;\mathrm{features},\;95\:\%\:\mathrm{C.L.\:replicas})$",
          r'$\mathrm{SM}$']

all_together= True


def ellipse_overview(coeff_dict, labels, paths, envelope=False, taken_together=False, colors=None, alphas=None):
    n_cols = len(coeff_dict) - 1
    n_rows = n_cols

    fig = plt.figure(figsize=(n_cols * 4, n_rows * 4))

    grid = plt.GridSpec(n_rows, n_cols, hspace=0.1, wspace=0.1)

    c1_old = "cHu"

    row_idx = -1
    col_idx = -1
    j = 1
    for (c1, c2) in itertools.combinations(coeff_dict.keys(), 2):
        if c1 != c1_old:
            row_idx += -1
            col_idx = -1 - j
            j += 1
            c1_old = c1

        ax = fig.add_subplot(grid[row_idx, col_idx])

        if c2 == 'cHj3':
            ax.set_xlim(left=-0.11, right=0.05)
        if c1 == 'cHj3':
            ax.set_ylim(bottom=-0.11, top=0.05)

        # ax.set_xlim(plot_ranges[c2])
        # ax.set_ylim(plot_ranges[c1])

        plotter = EllipsePlotter()

        dfs = []
        for path in paths:
            dfs.append(Analyse.posterior_loader(path.format(c1, c2, c1, c2)))

        if all_together:
            dfs = [dfs[0], pd.concat(dfs[1:])]


        hndls = plotter.plot(ax, dfs, coeff1=c2, coeff2=c1,
                             ax_labels=[coeff_dict[c2], coeff_dict[c1]], kde=True, envelope=envelope, taken_together=taken_together,
                             colors=['C2', 'C1'])
        if row_idx != -1:
            ax.set(xlabel=None)
            ax.tick_params(
                axis='x',  # changes apply to the x-axis
                which='both',  # both major and minor ticks are affected
                labelbottom=False)
        if col_idx != -n_cols:
            ax.set(ylabel=None)
            ax.tick_params(
                axis='y',  # changes apply to the y-axis
                which='both',  # both major and minor ticks are affected
                labelleft=False)

        col_idx -= 1

    legend = ax.legend(
        labels=labels, handles=hndls,
        bbox_to_anchor=(1, 1),
        loc='upper left', frameon=False, fontsize=24,
        handlelength=1,
        borderpad=0.5,
        handletextpad=1,
        title_fontsize=24)

    fig.suptitle(
        r"$\mathrm{Marginalised}\:95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-4}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$",
        y=0.92)

    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())

    return fig


fig_4 = ellipse_overview(coeff_dict, labels, paths_samples, envelope=True, taken_together=True)
fig_4.savefig('/data/theorie/jthoeve/ML4EFT/plots/2022/27_10/zh_reps_together_v7.pdf')
