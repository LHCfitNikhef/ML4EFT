import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import itertools
import os
from matplotlib import rc
import confidence_regions

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 26})
rc('text', usetex=True)


def cornerplot(coeff_dict, path_to_samples, handles, labels, order="lin"):
    n_cols = len(coeff_dict) - 1
    n_rows = n_cols

    fig = plt.figure(figsize=(n_cols * 4, n_rows * 4))

    grid = plt.GridSpec(n_rows, n_cols, hspace=0.4, wspace=0.4)

    row_idx = -1
    col_idx = -1
    j = 1
    for i, (c1, c2) in enumerate(itertools.combinations(coeff_dict.keys(), 2)):

        if i == 0:
            c1_old = c1
        if c1 != c1_old:
            row_idx += -1
            col_idx = -1 - j
            j += 1
            c1_old = c1

        ax = fig.add_subplot(grid[row_idx, col_idx])

        ax.scatter(0, 0, c="k", marker="+", s=50, zorder=10)

        dfs = []
        for path in path_to_samples:
            if os.path.isfile(path):
                with open(path) as json_data:
                    samples = json.load(json_data)
                dfs.append(pd.DataFrame(samples))

        confidence_regions.plot_confidence_region(ax, dfs, coeff1=c2, coeff2=c1,
                                                  ax_labels=[coeff_dict[c2], coeff_dict[c1]],
                                                  order=order)

        if row_idx != -1:
            ax.set(xlabel=None)

        if col_idx != -n_cols:
            ax.set(ylabel=None)

        col_idx -= 1

    ax.legend(handles, labels, bbox_to_anchor=(1, 1), loc='upper left',
              frameon=False, fontsize=24,
              handlelength=1,
              borderpad=0.5,
              handletextpad=1,
              title_fontsize=24)

    fig.suptitle(
        r"$95\:\%\:\mathrm{C.L.\:intervals}$",
        y=0.92)

    return fig


coeff_dict = {"ctd8": r'$c_{td}^{(8)}$', "cQj18": r'$c_{Qq}^{(1,8)}$', "cQu8": r'$c_{Qu}^{(8)}$',
              "ctj8": r'$c_{qt}^{(8)}$', "ctGRe": r'$c_{tG}$'}

handles = [plt.Rectangle((0, 0), 1, 1, fc='C0', alpha=0.3, linewidth=0.5, edgecolor='C0')]
labels = [r"$\mathrm{Unbinned}\;\mathrm{ML}\;(18\;\mathrm{features})$"]


path_to_samples = ['./example/posterior_glob_lin_18.json']

fig = cornerplot(coeff_dict, path_to_samples, handles, labels, order="lin")
fig.savefig('cornerplot.pdf')
