"""Module to plot feature distributions"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import NullFormatter

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


def plot_features(df_sm, dfs_eft, features, legend_labels):
    """
    Produces a plot showing the distribution of the training features

    Parameters
    ----------
    df_sm: pd.DataFrame
        Standard Model events
    dfs_eft: list
        List of panda dataframes with EFT events
    features: dict
        Of the form {'kinematic_feature': 'latex_string' }
    legend_labels: list
        List of legend elements


    Returns
    -------
    matplotlib.figure.Figure
        Figure showing the distribution of the kinematic features under the SM and the EFT
    """
    n_cols = 5
    n_rows = int(np.ceil(len(features) / n_cols))
    fig = plt.figure(figsize=(n_cols * 4, n_rows * 5))

    grid = plt.GridSpec(n_rows, n_cols, hspace=0.3, wspace=0.2)

    for i, (feature, label) in enumerate(features.items()):

        ax = fig.add_subplot(grid[i // n_cols, i % n_cols])

        hist_mg_sm, bins = np.histogram(df_sm[feature].iloc[1:],
                                        bins=np.linspace(df_sm[feature].min(), df_sm[feature].max(), 20), density=True)

        for df_eft in dfs_eft:
            hist_mg_eft, bins = np.histogram(df_eft[feature].iloc[1:],
                                             bins=np.linspace(df_sm[feature].min(), df_sm[feature].max(), 20),
                                             density=True)

            ax.step(bins[:-1], df_eft.iloc[0, 0] * hist_mg_eft , where='post',
                    linewidth=.7)
            ax.step(bins[:-1], (df_eft.iloc[0,0] / df_sm.iloc[0,0]) * (hist_mg_eft / hist_mg_sm), where='post', linewidth=.7)

        ax.axhline(0, color='k')
        ax.set_ylim(-5, 10)
        #ax.step(bins[:-1], df_sm.iloc[0,0] * hist_mg_sm, where='post', linewidth=1.5, color='k', linestyle='dashed')

        #ax.set_yscale('log')
        #ax.yaxis.set_major_formatter(NullFormatter())
        #ax.yaxis.set_minor_formatter(NullFormatter())
        #ax.axes.yaxis.set_ticklabels([])
        ax.set_xlabel(label)

        if i % n_cols == 0:
            ax.set_ylabel(r'$r(x, c)$')
        else:
            ax.tick_params(axis='y', which='both', labelleft=False)

    legend = ax.legend(
        labels=legend_labels,
        bbox_to_anchor=(1.17, 0., 1, 1),
        fontsize=20,
        handlelength=1,
        borderpad=1,
        handletextpad=1, ncol=2, frameon=False)

    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())

    return fig
