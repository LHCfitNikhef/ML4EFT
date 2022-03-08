#%%
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn
import copy
import matplotlib as mpl
from matplotlib import cm

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

def col_cycler(cols):
    count = 0
    while True:
        yield cols[count]
        count = (count + 1)%len(cols)

def plot_contours(c_x, c_y, path_to_row_truth, path_to_row_nn, path_to_row_binned, label_legend, label_x, label_y, xsec_df):

    yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis
    fig, ax = plt.subplots(figsize=(12, 10))

    labels = []
    contours = []
    col_iter = col_cycler(['C0', 'C1', 'C2', 'C3'])
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    # flat direction
    rc = -xsec_df['chw'] / xsec_df['chwb']

    if len(path_to_row_truth) > 0:
        for i, (path, label) in enumerate(path_to_row_truth):

            # combine rows
            q_c_truth = combine_qc(c_x, c_y, path)

            # plot 95% CL interval
            contour_truth = plt.contour(xx, yy, q_c_truth, np.array([5.99]), origin='lower', linestyles='dashed',
                                        linewidths=1.5,
                                        colors=colors[i])

            contour_handle, _ = contour_truth.legend_elements()
            contours.append(contour_handle[0])

            labels.append(label)


    if len(path_to_row_nn) > 0:
        for i, (path, label) in enumerate(path_to_row_nn):
            q_c_nn = combine_qc(c_x, c_y, path)

            #q_c_nn = np.ma.masked_where(yy < rc * xx - 0.05, q_c_nn)

            contour_nn = plt.contour(xx, yy, q_c_nn,np.array([np.nanmin(q_c_nn) + 5.99]), origin='lower', linestyles='dashed',
                                     linewidths=1.5,
                                     colors=colors[i + len(path_to_row_truth)])

            contour_handle, _ = contour_nn.legend_elements()
            contours.append(contour_handle[0])

            labels.append(label)

    if len(path_to_row_binned) > 0 :
        for i, (path, label) in enumerate(path_to_row_binned):

            log_likelihood = combine_likelihood_binned(c_x, c_y, path)

            color_offset = len(path_to_row_truth) if path_to_row_truth is not None else 0

            contour_binned = ax.contour(log_likelihood, np.array([np.max(log_likelihood) - 0.5 * 5.99]),
                                        origin='lower', linestyles='dashed', linewidths=1.0, colors=colors[i + len(path_to_row_truth) + len(path_to_row_nn)],
                                        extent=(c_x.min(), c_x.max(), c_y.min(), c_y.max()))
            contour_handle, _ = contour_binned.legend_elements()
            contours.append(contour_handle[0])
            labels.append(label)

    plt.title(r'$95\%\rm{\;CL\;intervals}$')
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.scatter(0, 0, marker='+', label='SM', color='k')

    plt.plot(c_x, c_x * rc, linestyle='dotted', label=r'$\rm{flat}\;\rm{direction}$')


    plt.legend(contours, labels, fontsize=15, frameon=False, loc='best')
    plt.xlim(c_x.min(), c_x.max())
    plt.ylim(c_y.min(), c_y.max())
    # plt.xlim(-0.5, 0.3)
    # plt.ylim(-1,2)
    return fig

def plot_contours_binned(c_x, c_y, path_to_row):
    log_likelihood = combine_likelihood_binned(c_x, c_y, path_to_row)

    yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis
    fig = plt.figure(figsize=(12, 10))

    contour = plt.contour(xx, yy, log_likelihood, np.array([np.max(log_likelihood) - 5.99]),
                          origin='lower', linestyles='dashed', linewidths=1.0, colors='red')
    return fig



