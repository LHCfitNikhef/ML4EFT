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

def plot_contours(c_x, c_y, path_to_row_truth, path_to_row_truth_2, path_to_row_nn, label_legend, label_x, label_y, xsec_df, binned=False, path_to_row_binned=None, path_to_row_binned_2=None,
                  path_to_row_binned_3=None, path_to_row_binned_4=None):

    yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis
    fig, ax = plt.subplots(figsize=(12, 10))

    labels = []
    contours = []

    if path_to_row_truth is not None:
        q_c_truth = combine_qc(c_x, c_y, path_to_row_truth)

        # contour_truth = plt.contourf(xx, yy, q_c_truth, np.array([0, 5.99]), origin='lower',
        #                          colors='C0', alpha=0.2)
        contour_truth = plt.contour(xx, yy, q_c_truth, np.array([5.99]), origin='lower', linestyles='dashed',
                                    linewidths=1.5,
                                    colors='k')

        contour_handle, _ = contour_truth.legend_elements()
        contours.append(contour_handle[0])

        labels.append(r'$\rm{Truth}\;(3\;\rm{features})$')

        q_c_truth_2 = combine_qc(c_x, c_y, path_to_row_truth_2)

        # contour_truth = plt.contourf(xx, yy, q_c_truth, np.array([0, 5.99]), origin='lower',
        #                          colors='C0', alpha=0.2)
        contour_truth = plt.contour(xx, yy, q_c_truth_2, np.array([5.99]), origin='lower', linestyles='dashed',
                                    linewidths=1.5,
                                    colors='blue')

        contour_handle, _ = contour_truth.legend_elements()
        contours.append(contour_handle[0])

        labels.append(r'$\rm{Truth}\;(2\;\rm{features})$')


    rc = -xsec_df['chw'] / xsec_df['cHq3']
    if path_to_row_nn is not None:
        q_c_nn = combine_qc(c_x, c_y, path_to_row_nn)

        q_c_nn = np.ma.masked_where(yy < rc * xx - 0.05, q_c_nn)

        contour_nn = plt.contour(xx, yy, q_c_nn,np.array([np.nanmin(q_c_nn) + 5.99]), origin='lower', linestyles='dashed',
                                 linewidths=1.5,
                                 colors='red')

        contour_handle, _ = contour_nn.legend_elements()
        contours.append(contour_handle[0])

        labels.append(r'$\rm{NN}$')

    plt.title(r'$95\%\rm{\;CL\;intervals}$')
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.scatter(0, 0, marker='+', label='SM', color='k')


    # norm = mpl.colors.Normalize(vmin=np.nanmin(q_c_nn), vmax= np.nanmax(q_c_nn))#mpl.colors.BoundaryNorm(bounds, cmap_copy.N, extend='both')
    # cmap = 'GnBu'
    # cmap_copy = copy.copy(mpl.cm.get_cmap(cmap))
    # cmap_copy.set_bad(color='gainsboro')
    #
    # xsec = xsec_df['sm'] * np.ones(xx.shape) + xsec_df['chw'] * xx + xsec_df['chwb'] * yy
    # xsec_masked = np.ma.masked_where(xsec < 0, xsec)
    #
    # #im = ax.imshow(xsec_masked, origin='lower', extent=(c_x.min(), c_x.max(), c_y.min(), c_y.max()))
    # im = ax.imshow(q_c_nn, origin='lower', extent=(c_x.min(), c_x.max(), c_y.min(), c_y.max()), cmap=cmap_copy)
    # cbar = plt.colorbar(mpl.cm.ScalarMappable(norm = norm, cmap=cmap_copy), ax=ax)

    #idx_q_c_min = np.argwhere(q_c_nn == 0)
    #plt.scatter(c_x[idx_q_c_min[0, 1]], c_y[idx_q_c_min[0, 0]], marker='x', color='k')


    plt.plot(c_x, c_x * rc, linestyle='dotted', label=r'$\rm{flat}\;\rm{direction}$')

    if binned:

        log_likelihood_2 = combine_likelihood_binned(c_x, c_y, path_to_row_binned_2)
        contour_binned = ax.contour(log_likelihood_2, np.array([np.max(log_likelihood_2) - 0.5 * 5.99]),
                                    origin='lower', linestyles='dashed', linewidths=1.0, colors='C0',
                                    extent=(c_x.min(), c_x.max(), c_y.min(), c_y.max()))
        contour_handle, _ = contour_binned.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$1\;\rm{bin}$')

        # log_likelihood_4 = combine_likelihood_binned(c_x, c_y, path_to_row_binned_4)
        # contour_binned = ax.contour(log_likelihood_4, np.array([np.max(log_likelihood_4) - 0.5 * 5.99]),
        #                             origin='lower', linestyles='dashed', linewidths=1.0, colors='C1',
        #                             extent=(-1, 0.5, -2, 3))
        # contour_handle, _ = contour_binned.legend_elements()
        # contours.append(contour_handle[0])
        # labels.append(r'$2\;\rm{bins}$')
        #
        # log_likelihood_3 = combine_likelihood_binned(c_x, c_y, path_to_row_binned_3)
        # contour_binned = ax.contour(log_likelihood_3, np.array([np.max(log_likelihood_3) - 0.5 * 5.99]),
        #                             origin='lower', linestyles='dashed', linewidths=1.0, colors='C2',
        #                             extent=(-1, 0.5, -2, 3))
        # contour_handle, _ = contour_binned.legend_elements()
        # contours.append(contour_handle[0])
        # labels.append(r'$4\;\rm{bins}$')
        #
        log_likelihood = combine_likelihood_binned(c_x, c_y, path_to_row_binned)
        # extent = (x_min, x_max, y_min, y_max) = (cHW, cHq3)
        contour_binned = ax.contour(log_likelihood, np.array([np.max(log_likelihood) - 0.5 * 5.99]),
                              origin='lower', linestyles='dashed', linewidths=1.0, colors='C4', extent=(c_x.min(), c_x.max(), c_y.min(), c_y.max()))
        contour_handle, _ = contour_binned.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$5\;\rm{bins}$')




    plt.legend(contours, labels, fontsize=15, frameon=False, loc='best')
    # plt.xlim(c_x.min(), c_x.max())
    # plt.ylim(c_y.min(), c_y.max())
    plt.xlim(-0.5, 0.3)
    plt.ylim(-1,2)
    return fig

def plot_contours_binned(c_x, c_y, path_to_row):
    log_likelihood = combine_likelihood_binned(c_x, c_y, path_to_row)

    yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis
    fig = plt.figure(figsize=(12, 10))

    contour = plt.contour(xx, yy, log_likelihood, np.array([np.max(log_likelihood) - 5.99]),
                          origin='lower', linestyles='dashed', linewidths=1.0, colors='red')
    return fig



