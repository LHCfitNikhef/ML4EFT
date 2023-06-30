import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import NullFormatter
from matplotlib.lines import Line2D
from scipy.ndimage import uniform_filter1d
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from sklearn.gaussian_process import GaussianProcessRegressor, kernels


rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

normalise = False
yscale = 'log'

main_color = ['C0','C1','C3','C2']
linestyles = ['-', '-', '-', '-']
ratio_color = ['C1', 'C2']

main_color_groom = ['black', 'C1','C2','C0']

ratio_color_groom = ['C1','C2','C0']


def plot_features_groom(df1, df2, df3, df4, features, legend_labels):
    n_cols = 1
    n_rows = 2
    fig = plt.figure(figsize=( 11.4, 8))
    grid = plt.GridSpec(n_rows, n_cols, hspace=0.5, wspace=0.1, height_ratios=[3, 1]*(n_rows//2))
    

    for i, (feature, label) in enumerate(features.items()):
        ax = fig.add_subplot(grid[i // n_cols * 2, i % n_cols])
        min_val = df1[feature].min()
        max_val = df1[feature].max()

        bins=np.linspace(min_val, max_val, 30)

        hist_mg_df1, bins = np.histogram(df1[feature], bins=bins, density=normalise)
        hist_mg_df1_norm, bins = np.histogram(df1[feature], bins=bins, density=True)

        ax.step(bins[:-1], hist_mg_df1, where='post', linewidth=1,color=main_color_groom[0],linestyle='--')

        hist_mg_df2, bins = np.histogram(df2[feature], bins=bins, density=normalise)
        hist_mg_df2_norm, bins = np.histogram(df2[feature], bins=bins, density=True)
        ax.step(bins[:-1], hist_mg_df2, where='post', linewidth=.7,color=main_color_groom[1])

        hist_mg_df3, bins = np.histogram(df3[feature], bins=bins, density=normalise)
        hist_mg_df3_norm, bins = np.histogram(df3[feature], bins=bins, density=True)
        ax.step(bins[:-1], hist_mg_df3, where='post', linewidth=.7,color=main_color_groom[2])

        hist_mg_df4, bins = np.histogram(df4[feature], bins=bins, density=normalise)
        hist_mg_df4_norm, bins = np.histogram(df4[feature], bins=bins, density=True)
        ax.step(bins[:-1], hist_mg_df4, where='post', linewidth=.7,color=main_color_groom[3])

        if (yscale == "log"):
            ax.set_yscale('log')
        ax.yaxis.set_major_formatter(NullFormatter())
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.axes.yaxis.set_ticklabels([])
        ax.set_xlabel(label)

        # Adjust subplot parameters to create space for the legend
        plt.subplots_adjust(right=0.54)

        
        eps = 1e-8

        ax_ratio = fig.add_subplot(grid[i // n_cols * 2 + 1, i % n_cols])

        ratio1 = np.where(hist_mg_df1_norm>eps, hist_mg_df2_norm / hist_mg_df1_norm, 1)

        ratio2 = np.where(hist_mg_df1_norm>eps, hist_mg_df3_norm / hist_mg_df1_norm, 1)

        ratio3 = np.where(hist_mg_df1_norm>eps, hist_mg_df4_norm / hist_mg_df1_norm, 1)


        ax_ratio.step(bins[:-1], ratio1, where='post', linewidth=.7, color=ratio_color_groom[0])
        ax_ratio.step(bins[:-1], ratio2, where='post', linewidth=.7, color=ratio_color_groom[1])
        ax_ratio.step(bins[:-1], ratio3, where='post', linewidth=.7, color=ratio_color_groom[2])


        # Draw a horizontal line at y=1
        ax_ratio.axhline(1, color='grey',linewidth=.7)

        # Get current y-axis limits
        lower, upper = ax_ratio.get_ylim()

        # Check if they are out of the desired range
        if lower < 0.2 or upper > 1.8:
            ax_ratio.set_ylim([0.2, 1.8])

        # Create custom legend handles
        main_legend_handles = [Line2D([0], [0], color=c, linewidth=1, linestyle='--' if i == 0 else '-') for i, c in enumerate(main_color_groom)]


        legend_main = fig.legend(
            handles=main_legend_handles,
            labels=legend_labels,
            bbox_to_anchor=(0.58, 0.5), 
            loc='center left',
            fontsize=20,
            handlelength=1,
            borderpad=1,
            handletextpad=1, 
            ncol=1, 
            frameon=False)


    return fig


def plot_features(df1, df2, df3, df4, features, legend_labels):
    n_cols = 5
    n_rows = int(np.ceil(len(features) / n_cols)) * 2
    fig = plt.figure(figsize=(n_cols * 6, n_rows * 4))

    grid = plt.GridSpec(n_rows, n_cols, hspace=0.5, wspace=0.2, height_ratios=[3, 1]*(n_rows//2))

    for i, (feature, label) in enumerate(features.items()):
        ax = fig.add_subplot(grid[i // n_cols * 2, i % n_cols])
        min_val = df1[feature].min()
        max_val = df1[feature].max()

        bins=np.linspace(min_val, max_val, 30)

        hist_mg_df1, bins = np.histogram(df1[feature], bins=bins, density=normalise)
        hist_mg_df1_norm, bins = np.histogram(df1[feature], bins=bins, density=True)

        ax.step(bins[:-1], hist_mg_df1, where='post', linewidth=.7,color=main_color[0],linestyle=linestyles[0])

        hist_mg_df2, bins = np.histogram(df2[feature], bins=bins, density=normalise)
        hist_mg_df2_norm, bins = np.histogram(df2[feature], bins=bins, density=True)
        ax.step(bins[:-1], hist_mg_df2, where='post', linewidth=.7,color=main_color[1],linestyle=linestyles[1])

        hist_mg_df3, bins = np.histogram(df3[feature], bins=bins, density=normalise)
        hist_mg_df3_norm, bins = np.histogram(df3[feature], bins=bins, density=True)
        ax.step(bins[:-1], hist_mg_df3, where='post', linewidth=.7,color=main_color[2],linestyle=linestyles[2])

        hist_mg_df4, bins = np.histogram(df4[feature], bins=bins, density=normalise)
        hist_mg_df4_norm, bins = np.histogram(df4[feature], bins=bins, density=True)
        ax.step(bins[:-1], hist_mg_df4, where='post', linewidth=.7,color=main_color[3],linestyle=linestyles[3])

        if (yscale == "log"):
            ax.set_yscale('log')
        ax.yaxis.set_major_formatter(NullFormatter())
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.axes.yaxis.set_ticklabels([])
        ax.set_xlabel(label)
        
        eps = 1e-8

        ax_ratio = fig.add_subplot(grid[i // n_cols * 2 + 1, i % n_cols])
        np.seterr(divide='ignore', invalid='ignore')
        ratio1 = np.where(hist_mg_df1_norm>eps, hist_mg_df2_norm / hist_mg_df1_norm, 1)

        ratio2 = np.where(hist_mg_df3_norm>eps, hist_mg_df4_norm / hist_mg_df3_norm, 1)

        ax_ratio.step(bins[:-1], ratio1, where='post', linewidth=.7, color=ratio_color[0])
        ax_ratio.step(bins[:-1], ratio2, where='post', linewidth=.7, color=ratio_color[1])

        # Draw a horizontal line at y=1
        ax_ratio.axhline(1, color='grey',linewidth=.7)

        # Get current y-axis limits
        lower, upper = ax_ratio.get_ylim()

        # Check if they are out of the desired range
        if lower < 0.2 or upper > 1.8:
            ax_ratio.set_ylim([0.2, 1.8])

        # Create custom legend handles
        main_legend_handles = [Line2D([0], [0], color=c, linewidth=1) for c in main_color]


        # Adjust the x, y of the bbox_to_anchor to position the legends
        legend_main = fig.legend(
            handles=main_legend_handles,  # Use custom handles
            labels=legend_labels,
            bbox_to_anchor=(0.9, 0.2),  # Adjust as needed
            loc='lower right',
            fontsize=20,
            handlelength=1,
            borderpad=1,
            handletextpad=1, 
            ncol=2, 
            frameon=False)


    return fig



        # eps = 1e-8

        # ax_ratio = fig.add_subplot(grid[i // n_cols * 2 + 1, i % n_cols])

        # ratio1 = np.where(hist_mg_df1>eps, hist_mg_df2_norm / hist_mg_df1_norm, 1)
        # ax_ratio.step(bins[:-1], ratio1, where='post', linewidth=.7, color='blue')

        # ratio2 = np.where(hist_mg_df3>eps, hist_mg_df4_norm
        # / hist_mg_df3_norm, 1)
        # ax_ratio.step(bins[:-1], ratio2, where='post', linewidth=.7, color='red')





