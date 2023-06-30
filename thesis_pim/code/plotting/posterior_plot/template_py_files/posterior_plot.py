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
import sys
import confidence_regions


rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 26})
rc('text', usetex=True)

coeff_dict_lin = {"ctd8": r'$c_{td}^{(8)}$', "cQj18": r'$c_{Qq}^{(1,8)}$', "cQu8": r'$c_{Qu}^{(8)}$', "ctj8": r'$c_{qt}^{(8)}$', "ctGRe": r'$c_{tG}$'}
coeff_dict_quad = {"ctd8": r'$c_{td}^{(8)}$', "ctGRe": r'$c_{tG}$', "cQd8": r'$c_{Qd}^{(8)}$', "cQj18": r'$c_{Qq}^{(1,8)}$', "cQj38": r'$c_{Qq}^{(3,8)}$', "cQu8": r'$c_{Qu}^{(8)}$',  "ctj8": r'$c_{qt}^{(8)}$', "ctu8": r'$c_{tu}^{(8)}$'}


order=sys.argv[1]

data1 = sys.argv[2]
data2 = sys.argv[3]
data3= sys.argv[4]

label1=sys.argv[5]
label2=sys.argv[6]
label3=sys.argv[7]

color1=sys.argv[8]
color2=sys.argv[9]
color3=sys.argv[10]


save_loc=sys.argv[11]

paths_plot = []
labels = []
colors = []

if data3 == 'None':
    paths_plot = [data1, data2]
    labels = [r"${}$".format(label1), r"${}$".format(label2),r'$\mathrm{SM}$']
    colors = [color1, color2]

else:
    paths_plot = [data1, data2, data3]
    labels = [r"${}$".format(label1), r"${}$".format(label2), r"${}$".format(label3),r'$\mathrm{SM}$']
    colors = [color1, color2, color3]

def ellipse_overview(coeff_dict, labels, paths, colors, kde=False):

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
                                 ax_labels=[coeff_dict[c2], coeff_dict[c1]],  kde=kde, colors=colors)
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
    if kde:
        fig.suptitle(r"$\mathrm{Marginalised}\:95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-4}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$", y=0.92)
    else:
        fig.suptitle(r"$\mathrm{Marginalised}\:95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-2}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$", y=0.92)

    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())



    return fig

if order == "lin":
    fig = ellipse_overview(coeff_dict_lin, labels, paths_plot, colors=colors)
    fig.savefig(save_loc)
else:
    fig = ellipse_overview(coeff_dict_quad, labels, paths_plot, colors=colors, kde=True)
    fig.savefig(save_loc)


