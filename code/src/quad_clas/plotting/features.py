import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import NullFormatter

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

def plot_features(df_sm, dfs_eft, features, labels, x_labels=None, y_labels=None):
    n_cols = 4
    n_rows = int(np.ceil(len(features)/ n_cols))
    fig = plt.figure(figsize=(n_cols * 4, n_rows * 5))

    # xsec_eft = df_eft.iloc[0, 0]
    xsec_sm = df_sm.iloc[0, 0]
    #
    # df_sm = df_sm.iloc[1:, :]
    # df_eft = df_eft.iloc[1:, :]

    for i, feature in enumerate(features):
        ax = plt.subplot(n_rows, n_cols, i + 1)
        hist_mg_sm, bins = np.histogram(df_sm[feature], bins=np.linspace(df_sm[feature].min(), df_sm[feature].max(), 30), density=True)
        plt.step(bins[:-1], hist_mg_sm, where='post', linewidth=.9)
        plt.yscale('log')
        ax.yaxis.set_major_formatter(NullFormatter())
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.axes.yaxis.set_ticklabels([])
        plt.xlabel(x_labels[i])
        #plt.legend(prop={"size":16}, frameon=False)

    for df_eft in dfs_eft:
        for i, feature in enumerate(features):
            xsec_eft = df_eft.iloc[0, 0]

            ax = plt.subplot(n_rows, n_cols, i + 1)
            hist_mg_eft, bins = np.histogram(df_eft[feature], bins=np.linspace(df_sm[feature].min(), df_sm[feature].max(), 30), density=True)
            plt.step(bins[:-1], (xsec_eft / xsec_sm) * hist_mg_eft, where='post', linewidth=.7)
            plt.yscale('log')
            ax.yaxis.set_major_formatter(NullFormatter())
            ax.yaxis.set_minor_formatter(NullFormatter())
            ax.axes.yaxis.set_ticklabels([])
            plt.xlabel(x_labels[i])
            #plt.legend(prop={"size":16}, frameon=False)

    legend = fig.legend(
        labels=labels,
        loc='lower center', bbox_to_anchor=(0.5, 0), ncol=4, frameon=False)

    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())

    fig.tight_layout(rect=(0, bbox.y1, 1, 1), h_pad=0.5, w_pad=0.5)

    return fig