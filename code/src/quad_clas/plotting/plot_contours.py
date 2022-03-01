#%%
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

def combine_qc(c_x, c_y, path):
    q_c = np.zeros((len(c_y), len(c_x)))
    for row, cHWB in enumerate(c_y):
        values = np.load(os.path.join(path.format(row)),
                         allow_pickle=True).flatten()
        q_c[row, :] = values
    q_c = 2 * (- q_c + np.nanmax(q_c))
    return q_c

def combine_likelihood_binned(c_x, c_y, path):
    likelihood = np.zeros((len(c_y), len(c_x)))
    for row, cHWB in enumerate(c_y):
        values = np.load(os.path.join(path.format(row)),
                         allow_pickle=True).flatten()
        likelihood[row, :] = values
    return likelihood

def plot_contours(c_x, c_y, path_to_row_truth, path_to_row_nn, label_legend, label_x, label_y, xsec_df, binned=False, path_to_row_binned=None, path_to_row_binned_2=None,
                  path_to_row_binned_3=None, path_to_row_binned_4=None):

    yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis
    fig, ax = plt.subplots(figsize=(12, 10))

    q_c_truth = combine_qc(c_x, c_y, path_to_row_truth)
    q_c_nn = combine_qc(c_x, c_y, path_to_row_nn)

    # from scipy.ndimage.filters import gaussian_filter
    # q_c_truth = gaussian_filter(q_c_truth, sigma=.6)

    # contour_truth = plt.contourf(xx, yy, q_c_truth, np.array([0, 5.99]), origin='lower',
    #                          colors='C0', alpha=0.2)
    contour_truth = plt.contour(xx, yy, q_c_truth, np.array([5.99]), origin='lower', linestyles='dashed',
                                 linewidths=1.5,
                                 colors='k')

    # contour_nn = plt.contourf(xx, yy, q_c_nn, np.array([0, 5.99]), origin='lower',
    #                           colors='C1', alpha=0.2)

    contour_nn = plt.contour(xx, yy, q_c_nn, np.array([5.99]), origin='lower', linestyles='dashed',
                              linewidths=1.5,
                              colors='red')

    #seaborn.heatmap(q_c_nn)
    from matplotlib import cm
    #norm = cm.colors.Normalize(vmax=abs(q_c_nn).max(), vmin=-abs(q_c_nn).max())
    #cmap = cm.PRGn
    #im = ax.imshow(q_c_nn, origin='lower', extent =(-0.5, -0.10, -1.0, 1.5), cmap=cmap, norm=norm, aspect='auto')
    #fig.colorbar(im, ax=ax)


    labels = []
    contours = []

    contour_handle, _ = contour_truth.legend_elements()
    contours.append(contour_handle[0])

    labels.append(r'$\rm{Truth}$')

    contour_handle, _ = contour_nn.legend_elements()
    contours.append(contour_handle[0])

    labels.append(r'$\rm{NN}$')

    plt.title(r'$95\%\rm{\;CL\;intervals}$')
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.scatter(0, 0, marker='+', label='SM', color='k')
    #idx_q_c_min = np.argwhere(q_c_nn == 0)
    #plt.scatter(c_x[idx_q_c_min[0, 1]], c_y[idx_q_c_min[0, 0]], marker='x', color='k')

    #rc = -xsec_df['chwb'] / xsec_df['chw']
    #plt.plot(c_x, c_y * rc, linestyle='dotted', label=r'$\rm{flat}\;\rm{direction}$')
    # cHW_values = np.linspace(-1, 0.5, 100)
    # cHq3_values = np.linspace(-2, 3, 100)

    if binned:
        log_likelihood_2 = combine_likelihood_binned(c_x, c_y, path_to_row_binned_2)
        contour_binned = ax.contour(log_likelihood_2, np.array([np.max(log_likelihood_2) - 0.5 * 5.99]),
                                    origin='lower', linestyles='dashed', linewidths=1.0, colors='C0',
                                    extent=(-1, 0.5, -2, 3))
        contour_handle, _ = contour_binned.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$1\;\rm{bin}$')

        log_likelihood_4 = combine_likelihood_binned(c_x, c_y, path_to_row_binned_4)
        contour_binned = ax.contour(log_likelihood_4, np.array([np.max(log_likelihood_4) - 0.5 * 5.99]),
                                    origin='lower', linestyles='dashed', linewidths=1.0, colors='C1',
                                    extent=(-1, 0.5, -2, 3))
        contour_handle, _ = contour_binned.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$2\;\rm{bins}$')

        log_likelihood_3 = combine_likelihood_binned(c_x, c_y, path_to_row_binned_3)
        contour_binned = ax.contour(log_likelihood_3, np.array([np.max(log_likelihood_3) - 0.5 * 5.99]),
                                    origin='lower', linestyles='dashed', linewidths=1.0, colors='C2',
                                    extent=(-1, 0.5, -2, 3))
        contour_handle, _ = contour_binned.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$4\;\rm{bins}$')

        log_likelihood = combine_likelihood_binned(c_x, c_y, path_to_row_binned)
        contour_binned = ax.contour(log_likelihood, np.array([np.max(log_likelihood) - 0.5 * 5.99]),
                              origin='lower', linestyles='dashed', linewidths=1.0, colors='C4', extent=(-1, 0.5, -2, 3))
        contour_handle, _ = contour_binned.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$6\;\rm{bins}$')


    plt.legend(contours, labels, fontsize=15, frameon=False, loc='best')
    plt.xlim(-0.5, 0.3)
    plt.ylim(-1.5, 2.3)
    return fig

def plot_contours_binned(c_x, c_y, path_to_row):
    log_likelihood = combine_likelihood_binned(c_x, c_y, path_to_row)

    yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis
    fig = plt.figure(figsize=(12, 10))

    contour = plt.contour(xx, yy, log_likelihood, np.array([np.max(log_likelihood) - 5.99]),
                          origin='lower', linestyles='dashed', linewidths=1.0, colors='red')
    return fig



