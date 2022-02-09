import numpy as np
import matplotlib.pyplot as plt


def plot_features(df, x_labels=None, y_labels=None):
    n_cols = 2
    n_rows = int(np.ceil(df.shape[1] / n_cols))
    fig = plt.figure(figsize=(n_cols * 5, n_rows * 4))

    for i, kinematic in enumerate(df):
        ax = plt.subplot(n_rows, n_cols, i + 1)
        hist_mg_sm, bins_mg = np.histogram(df[kinematic], bins=np.linspace(df[kinematic].min(), df[kinematic].max(), 50))
        plt.step(bins_mg[:-1], hist_mg_sm, c='C0', where='post', label= r'$\mathrm{SM}$')
        plt.yscale('log')

    return fig