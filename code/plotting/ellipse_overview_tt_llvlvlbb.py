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
from quad_clas.analyse.analyse import Analyse
from ellipse_plotter_new import EllipsePlotter



rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 26})
rc('text', usetex=True)

coeff_dict = {"ctd8": r'$c_{td}^{(8)}$', "cQd8": r'$c_{Qd}^{(8)}$', "cQj18": r'$c_{Qq}^{(1,8)}$', "cQj38": r'$c_{Qq}^{(3,8)}$', "cQu8": r'$c_{Qu}^{(8)}$', "ctGRe": r'$c_{tG}$',  "ctj8": r'$c_{qt}^{(8)}$', "ctu8": r'$c_{tu}^{(8)}$'}

# high lumi plots

binned_path = '/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/binned_glob_mtt_quad/posterior.json'
nn_path = '/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/nn_glob_quad/posterior.json'

paths_plot_0 = [binned_path, nn_path]


labels_0 = [r"$m_{t\bar{t}}\in[1.45, 1.50, 1.60, 1.70, 2.00, \infty)\:\mathrm{GeV}$",
            r"$\mathrm{ML}\;\mathrm{model}\;(18\;\mathrm{features})$", r'$\mathrm{SM}$']

def ellipse_overview(coeff_dict, labels, paths):

    n_cols = len(coeff_dict) - 1
    n_rows = n_cols

    fig = plt.figure(figsize=(n_cols * 4, n_rows * 4))

    grid = plt.GridSpec(n_rows, n_cols, hspace=0.1, wspace=0.1)

    c1_old = "ctd8"

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

        plotter = EllipsePlotter()

        dfs = []
        for path in paths:
            dfs.append(Analyse.posterior_loader(path.format(c1, c2, c1, c2)))

        hndls = plotter.plot(ax, dfs, coeff1=c2, coeff2=c1,
                                 ax_labels=[coeff_dict[c2], coeff_dict[c1]],  kde=True)
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

    fig.suptitle(r"$\mathrm{Marginalised}\:95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-4}\right)\mathrm{at\:}L=300\:\mathrm{fb}^{-1}$", y=0.92)


    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())



    return fig

fig_0 = ellipse_overview(coeff_dict, labels_0, paths_plot_0)



fig_0.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/12_09/tt_llvlvlbb_quad_glob_nn_binned.pdf')

