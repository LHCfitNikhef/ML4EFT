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

coeff_dict = {"ctd8": r'$c_{td}^{(8)}$', "cQj18": r'$c_{Qq}^{(1,8)}$', "cQu8": r'$c_{Qu}^{(8)}$', "ctj8": r'$c_{qt}^{(8)}$', "ctGRe": r'$c_{tG}$'}


binned_path_ptll_etal = '/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/binned_glob_etalptll_l2/posterior.json'
nn_path_pt_ll_eta_l = '/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/nn_glob_ptll_etal_lin2/posterior.json'
nn_path_all = '/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/nn_glob_all_lin_5c/posterior.json'


paths_plot_0 = [binned_path_ptll_etal, nn_path_pt_ll_eta_l, nn_path_all]

labels_0 = [r"$\mathrm{Binned}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)$",
            r"$\mathrm{Unbinned}\;\mathrm{ML}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)$",
            r"$\mathrm{Unbinned}\;\mathrm{ML}\;(18\;\mathrm{features})$",
            r'$\mathrm{SM}$']

paths_plot_1 = [binned_path_ptll_etal, nn_path_pt_ll_eta_l]

labels_1 = [r"$\mathrm{Binned}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)$",
            r"$\mathrm{Unbinned}\;\mathrm{ML}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)$",
            r'$\mathrm{SM}$']

paths_plot_2 = [nn_path_pt_ll_eta_l, nn_path_all]

labels_2 = [r"$\mathrm{Unbinned}\;\mathrm{ML}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)$",
            r"$\mathrm{Unbinned}\;\mathrm{ML}\;(18\;\mathrm{features})$",
            r'$\mathrm{SM}$']

colors = ['C1', 'C2']



def ellipse_overview(coeff_dict, labels, paths, colors):

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
                                 ax_labels=[coeff_dict[c2], coeff_dict[c1]],  kde=False, colors=colors)
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

    fig.suptitle(r"$\mathrm{Marginalised}\:95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-2}\right)\mathrm{at\:}\mathcal{L}=300\:\mathrm{fb}^{-1}$", y=0.92)


    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())



    return fig

# fig_0 = ellipse_overview(coeff_dict, labels_0, paths_plot_0)
# fig_0.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/23_10/tt_glob_lin_binned_nn_all_v2.pdf')
#
# fig_1 = ellipse_overview(coeff_dict, labels_1, paths_plot_1)
# fig_1.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/23_10/tt_glob_lin_binned_nn_ptll_etal.pdf')

fig_2 = ellipse_overview(coeff_dict, labels_2, paths_plot_2, colors=colors)
fig_2.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/23_10/tt_glob_lin_nn_ptll_etal.pdf')
