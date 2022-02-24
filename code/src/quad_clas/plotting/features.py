import numpy as np
import matplotlib.pyplot as plt


def plot_features(df_sm, df_eft, eft_label='', x_labels=None, y_labels=None):
    n_cols = 2
    n_rows = int(np.ceil(df_sm.shape[1] / n_cols))
    fig = plt.figure(figsize=(n_cols * 5, n_rows * 4))

    xsec_eft = df_eft.iloc[0, 0]
    xsec_sm = df_sm.iloc[0, 0]

    df_sm = df_sm.iloc[1:, :]
    df_eft = df_eft.iloc[1:, :]


    for i, kinematic in enumerate(df_sm):
        ax = plt.subplot(n_rows, n_cols, i + 1)
        hist_mg_sm, bins = np.histogram(df_sm[kinematic], bins=np.linspace(df_sm[kinematic].min(), df_sm[kinematic].max(), 30), density=True)
        plt.step(bins[:-1], hist_mg_sm, c='C0', where='post', label= r'$\mathrm{SM}$')
        plt.yscale('log')
        plt.xlabel(x_labels[i])
        plt.legend(prop={"size":7})

    for i, kinematic in enumerate(df_eft):
        ax = plt.subplot(n_rows, n_cols, i + 1)
        hist_mg_eft, bins = np.histogram(df_eft[kinematic], bins=np.linspace(df_sm[kinematic].min(), df_sm[kinematic].max(), 30), density=True)
        plt.step(bins[:-1], (xsec_eft / xsec_sm) * hist_mg_eft, c='C1', where='post', label= r'$\mathrm{EFT},\;\mathcal{O}(\Lambda^{-2}),\;$' + eft_label)
        plt.yscale('log')
        plt.xlabel(x_labels[i])
        plt.legend(prop={"size":7})

    return fig