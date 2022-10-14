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

coeff_dict = {"cHu": r'$c_{\varphi u}$', "cHd": r'$c_{\varphi d}$', "cHj1": r'$c_{\varphi q}^{(1)}$', "cHj3": r'$c_{\varphi q}^{(3)}$',
              "cbHRe": r'$c_{b\varphi}$', "cHW": r'$c_{\varphi W}$', "cHWB": r'$c_{\varphi WB}$'}

nn_glob_all_quad = os.path.join('/data/theorie/jthoeve/ns_samples/zh_llbb/nn_glob_all_quad', 'posterior.json')
nn_glob_ptz_quad = os.path.join('/data/theorie/jthoeve/ns_samples/zh_llbb/nn_glob_ptz_quad', 'posterior.json')

#binned_glob_ptz_lin = '/data/theorie/jthoeve/ns_samples/zh_llbb/binned_glob_ptz_lin/posterior.json'
binned_glob_ptz_quad = '/data/theorie/jthoeve/ns_samples/zh_llbb/binned_glob_ptz_q_v5/posterior.json'
binned_glob_deltaRbb_lin = '/data/theorie/jthoeve/ns_samples/zh_llbb/binned_glob_deltaRbb_lin/posterior.json'
paths_plot_0 = [binned_glob_ptz_quad, nn_glob_ptz_quad, nn_glob_all_quad]

labels_0 = [r"$p_T^Z\:\mathrm{(fine\:binning)}$", r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z)$", r"$\mathrm{ML}\;\mathrm{model}\;(7\;\mathrm{features})$", r'$\mathrm{SM}$']
#labels_0 = [r"$p_T^Z\in [75, 150, 250, 400, \infty)\:[\mathrm{GeV}]$", r"$\Delta R(b_1, b_2) \in [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 3.0]$", r'$\mathrm{SM}$']


def ellipse_overview(coeff_dict, labels, paths):

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

        plotter = EllipsePlotter()

        dfs = []
        for path in paths:
            dfs.append(Analyse.posterior_loader(path))

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

    fig.suptitle(r"$\mathrm{Marginalised}\:95\:\%\:\mathrm{C.L.\:intervals},\;\mathcal{O}\left(\Lambda^{-2}\right)\mathrm{at\:}L=300\:\mathrm{fb}^{-1}$", y=0.92)


    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())



    return fig

fig_0 = ellipse_overview(coeff_dict, labels_0, paths_plot_0)
#fig_1 = ellipse_overview(coeff_dict, labels_1, paths_plot_1)
#fig_2 = ellipse_overview(coeff_dict, labels_2, paths_plot_2)
#fig_3 = ellipse_overview(coeff_dict, labels_3, paths_plot_3)
# fig_4 = ellipse_overview(coeff_dict, labels_4, paths_plot_4)

#fig_1.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/18_08/zh_particle_quad_kde_7_feat.pdf')
fig_0.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/28_09/zh_llbb_glob_quad_binned_fine.pdf')
#fig_2.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/18_08/zh_particle_lin.pdf')
#fig_3.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/18_08/zh_particle_quad_kde.pdf')
# fig_4.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/18_08/test_overview_4.pdf')

