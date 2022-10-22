import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import NullFormatter

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

def plot_features(df_sm, dfs_eft, features, legend_labels):

    n_cols = 5
    n_rows = int(np.ceil(len(features) / n_cols))
    fig = plt.figure(figsize=(n_cols * 4, n_rows * 5))

    grid = plt.GridSpec(n_rows, n_cols, hspace=0.3, wspace=0.2)


    # xsec_eft = df_eft.iloc[0, 0]
    xsec_sm = df_sm.iloc[0, 0]
    #
    # df_sm = df_sm.iloc[1:, :]
    # df_eft = df_eft.iloc[1:, :]

    for i, (feature, label) in enumerate(features.items()):

        ax = fig.add_subplot(grid[i // n_cols, i % n_cols])
        #ax = plt.subplot(n_rows, n_cols, i + 1)

        #plt.legend(prop={"size":16}, frameon=False)

        hist_mg_sm, bins = np.histogram(df_sm[feature],
                                        bins=np.linspace(df_sm[feature].min(), df_sm[feature].max(), 30), density=True)


        for df_eft in dfs_eft:


            hist_mg_eft, bins = np.histogram(df_eft[feature],
                                             bins=np.linspace(df_sm[feature].min(), df_sm[feature].max(), 30),
                                             density=True)

            ax.step(bins[:-1], ((hist_mg_eft/hist_mg_sm) - 1)/10, where='post', linewidth=.7)




        #ax.set_yscale('log')
        # ax.yaxis.set_major_formatter(NullFormatter())
        # ax.yaxis.set_minor_formatter(NullFormatter())
        #ax.axes.yaxis.set_ticklabels([])
        ax.set_xlabel(label)
        ax.axhline(0)




    # ax_legend = fig.add_subplot(grid[-1, -2:])
    # for i in range(len(dfs_eft) + 1):
    #     ax_legend.plot(np.ones(10), np.ones(10))



    legend = ax.legend(
        labels=legend_labels,
        bbox_to_anchor=(1.17, 0., 1, 1),
        fontsize=20,
        handlelength=1,
        borderpad=1,
        handletextpad=1, ncol=2, frameon=False)

    # legend = ax_legend.legend(
    #     labels=labels, ncol=3, frameon=False, fontsize=12)

    #ax_legend.set_visible(False)

    bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())

    #grid.tight_layout(fig)
    #fig.tight_layout(rect=(0, bbox.y1, 1, 1), h_pad=0.5, w_pad=0.5)

    return fig