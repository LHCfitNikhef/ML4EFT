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

        bins = np.linspa/data/theorie/pherbsch/ML4EFT/code/src/ml4eft/preprocce((df_sm[feature].min()+df_sm[feature].max())/2, df_sm[feature].max(), 10)

        ax.hist(df_sm[feature], bins=bins, density=True, histtype='stepfilled', alpha=0.7, linewidth=1.5, color='k', linestyle='dashed', label='SM')

        for df_eft in dfs_eft:
            ax.hist(df_eft[feature], bins=bins, density=True, histtype='stepfilled', alpha=0.5, linewidth=.7)

        ax.set_yscale('log')
        ax.yaxis.set_major_formatter(NullFormatter())
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.axes.yaxis.set_ticklabels([])
        ax.set_xlabel(label)

    legend = ax.legend(
        labels=['SM'] + legend_labels,
        bbox_to_anchor=(1.17, 0., 1, 1),
        fontsize=20,
        handlelength=1,
        borderpad=1,
        handletextpad=1, ncol=2, frameon=False)

    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())

    return fig





