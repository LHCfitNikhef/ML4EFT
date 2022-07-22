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

coeff_dict = {"cHu": r'$c_{\varphi u}$', "cHd": r'$c_{\varphi d}$', "cHj1": r'$c_{\varphi q}^{(1)}$', "cHj3": r'$c_{\varphi q}^{(3)}$',
              "cbHRe": r'$c_{b\varphi}$', "cHW": r'$c_{\varphi W}$', "cHWB": r'$c_{\varphi WB}$'}

root_quad = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_quad"
root_7_quad = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_q_7"


root_7 = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_7_feat/"
root_pt = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_pt_z/"
root_lin = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_lin"


# nn: quadratic (pt_z)
post_path_nn_quad = os.path.join(root_quad, 'nn', '{}_{}', 'posterior_{}_{}.json')

# binned: quadratic (STXS)
post_path_binned_quad = os.path.join(root_quad, 'binned', '{}_{}', 'posterior_{}_{}.json')

# nn: quadratic (7 features)
post_path_nn_quad_7_feat = os.path.join(root_7_quad, 'nn','{}_{}', 'posterior_{}_{}.json')

# binned: linear (STXS)
post_path_binned_lin = os.path.join(root_lin, 'binned', '{}_{}', 'posterior_{}_{}.json')

# nn: linear (pt_z)
post_path_nn_lin = os.path.join(root_pt, 'nn', '{}_{}', 'posterior_{}_{}.json')

# nn: linear (7 features)
post_path_nn_7 = os.path.join(root_7, 'nn', '{}_{}', 'posterior_{}_{}.json')


paths_plot_1 = [post_path_binned_quad, post_path_nn_quad, post_path_nn_quad_7_feat]
paths_plot_2 = [post_path_binned_lin, post_path_nn_lin]
paths_plot_3 = [post_path_binned_quad, post_path_nn_quad]
paths_plot_4 = [post_path_binned_lin, post_path_binned_quad, post_path_nn_lin, post_path_nn_quad]

labels_1 = [r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}:\mathrm{Quadratic}$", r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z):\mathrm{Quadratic}$",
          r"$\mathrm{ML}\;\mathrm{model}\;(7\;\mathrm{features}):\mathrm{Quadratic}$"]


labels_2 = [r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}:\mathrm{Linear}$", r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z):\mathrm{Linear}$"]

labels_3 = [r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}:\mathrm{Quadratic}$", r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z):\mathrm{Quadratic}$"]

labels_4 = [r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}:\mathrm{Linear}$", r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}:\mathrm{Quadratic}$",
            r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z):\mathrm{Linear}$",  r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z):\mathrm{Quadratic}$"
            ]

def ellipse_overview(coeff_dict, labels, paths):

    n_cols = len(coeff_dict) - 1
    n_rows = n_cols

    fig = plt.figure(figsize=(n_cols * 4, n_rows * 4))

    c1_old = "cHu"
    i = n_cols * n_rows
    j = 1
    for (c1, c2) in itertools.combinations(coeff_dict.keys(), 2):
        if c1 != c1_old:
            i -= j
            j += 1
            c1_old = c1
        ax = plt.subplot(n_rows, n_cols, i)

        plotter = EllipsePlotter()

        dfs = []
        for path in paths:
            dfs.append(Analyse.posterior_loader(path.format(c1, c2, c1, c2)))

        ax, hndls = plotter.plot(ax, dfs, coeff1=c2, coeff2=c1,
                                 ax_labels=[coeff_dict[c2], coeff_dict[c1]])
        if j!=1:
            ax.set_xlabel('')
        if not (i == n_cols * n_rows + 1 - j * n_cols):
            ax.set_ylabel('')

        i -= 1

    legend = fig.legend(
            labels=labels, handles=hndls,
            loc='upper center', frameon=False, fontsize=26)

    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())

    plt.tight_layout()

    return fig

fig_1 = ellipse_overview(coeff_dict, labels_1, paths_plot_1)
fig_2 = ellipse_overview(coeff_dict, labels_2, paths_plot_2)
fig_3 = ellipse_overview(coeff_dict, labels_3, paths_plot_3)
fig_4 = ellipse_overview(coeff_dict, labels_4, paths_plot_4)

fig_1.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/22_07/test_overview_1.pdf')
fig_2.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/22_07/test_overview_2.pdf')
fig_3.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/22_07/test_overview_3.pdf')
fig_4.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/22_07/test_overview_4.pdf')

