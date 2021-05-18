# Author: Jaco ter Hoeve
# This file computes the expected number of events under either the SM (H_1) or the SMEFT (H_0)
# by fitting a quadratic polynomial to the madgraph xsecs


import pylhe
import numpy as np
from matplotlib import pyplot as plt
import os,sys

import bounds_2 as bnds

#eft_points = [[-10.0, 0], [-5.0, 0], [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0], [0, -2.0], [0, -1.0], [0, -0.5],[0, 0.5], [0, 1.0], [0, 2.0], [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],[10.0, 2.0], [0.0, 0.0]]
eft_points = [[-10.0, 0], [-5.0, 0], [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0], [0, -10.0], [0, -5.0], [0, -1.0], [0, 1.0], [0, 5.0], [0, 10.0], [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],[10.0, 2.0], [0.0, 0.0]]
luminosity = 6

def coefficient_matrix():
    coeff_mat = []
    for cugre, cuu in eft_points:
        row = [1, cugre, cugre**2, cuu, cuu**2, cugre*cuu]
        coeff_mat.append(row)
    coeff_mat = np.array(coeff_mat)
    return coeff_mat


def construct_dataset():
    data = []
    data_sigma = []
    for i, eft_point in enumerate(eft_points):
        path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{}/bin/process_{}/Events/run_01/unweighted_events.lhe'.format(i, i)
        y, sigma_y = load_datapoint(path)
        data.append(y)
        data_sigma.append(sigma_y)
    data = np.array(data)
    data_sigma = np.array(data_sigma)
    return data, data_sigma


def load_datapoint(path):
    """
    Load the xsec and uncertainty from an lhe file.

    Parameters
    ----------
    path: str
        path to lhe event file

    Returns
    -------
    The total xsec and uncertainty
    """
    proc_info = pylhe.readLHEInit(path)['procInfo']
    xsec_proc = []
    error_proc = []
    for proc in proc_info:
        xsec_proc.append(proc['xSection'])
        error_proc.append(proc['error'])
    xsec_proc = np.array(xsec_proc)
    error_proc = np.array(error_proc)
    xsec = np.sum(xsec_proc)
    xsec_error = np.sqrt(np.sum(error_proc**2))
    return xsec, xsec_error

def xsec_binned(bins, path_xsec):
    """

    Parameters
    ----------
    bins: 1darray
        bins = [x_0, x_1, ..., x_nbins]

    Returns
    -------
    dataset: 2darray
        dataset.shape() = (len(eft_points), len(bins))
        The cross section in bin i and eft coefficient c
    """
    dataset = []

    for i, eft_point in enumerate(eft_points):
        #  path to lhe file
        path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{}/bin/process_{}/Events/run_01/unweighted_events.lhe'.format(i, i)
        if i > 5 and i < 12:
            path = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/cuu/eft_{}.lhe'.format(i-5)
        n_tot = 100000
        data = bnds.load_data(path, n=n_tot, s=n_tot)
        n_i, _ = np.histogram(data, bins=bins)

        xsec, _ = load_datapoint(path)
        sigma_i = n_i/n_tot * xsec
        dataset.append(sigma_i)

    dataset = np.array(dataset)  # dataset.shape = (len(eft_points), len(bins))

    #  write the dataset to a separate file
    # path_file = "/data/theorie/jthoeve/ML4EFT/quad_clas/xsec_bin.npy"
    os.makedirs(path_xsec)
    with open(os.path.join(path_xsec, "xsec_bin.npy"), 'wb') as f:
        np.save(f, dataset)


def expected_events_binned(c, bins, path):
    """

    Parameters
    ----------
    c: ndarray
        array that specifies the point in eft parameter space
    bins: 1darray
        bins = [x_0, x_1, ..., x_nbins]
    path: str
        the location where to write output

    Returns
    -------
    The number of expected countings in each bin at the specified point in EFT parameter space
    """

    # path = /data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3

    # path to file that stores the inclusive xsec per bin
    path_xsec_binned = os.path.join(path, "xsec_bin.npy")
    #
    # # create the directory and file if they do not exist
    # if not os.path.isfile(path_xsec_binned):
    #     xsec_binned(bins, path)
    # else:
    #     # open the xsec per bin file and load into dataset
    #     with open(path_xsec_binned, 'rb') as f:
    #         dataset = np.load(f)

    with open(path_xsec_binned, 'rb') as f:
        dataset = np.load(f)


    # build the matrix of coefficients
    coeff_mat = coefficient_matrix()

    # solve the linear equation xsec = coeff_matrix * a for a
    a, _, _, _ = np.linalg.lstsq(coeff_mat, dataset, rcond=None)

    # find the x_sec per bin at the specified point in eft parameter space
    cugre, cuu = c[0], c[1]
    eft_point = np.array([1, cugre, cugre ** 2, cuu, cuu ** 2, cugre * cuu])
    x_sec = np.einsum('ij,i', a, eft_point)

    return x_sec*luminosity



# def construct_dataset_binned(nbins):
#     data = []
#
#     for i in nbins:
#         data_bin = []
#         for j in eft_points:
#             cugre, cuu = j
#             sigma_i =
#             data_bin.append([[cugre, cuu], sigma_i])
#     return data


# def expected_nevents_bin(bins, c):
#     """
#
#     Parameters
#     ----------
#     bin: 1darray
#         bins = [x_0, x_1, ..., x_nbins]
#     data: 1darray
#         Monte Carlo data used to estimate N_i
#     c: float
#         eft coefficient
#
#     Returns
#     -------
#     Expected number of events N_i in the specified bins at a given eft coefficient c.
#     """
#
#     nbins = len(bins)
#     sigma_bin = construct_dataset_binned(nbins)
#
#     # total number of events
#     n_tot = len(data)
#     n_i, _ = np.histogram(data, bins=bins)





def expected_nevents(c):
    cugre = c[0]
    cuu = c[1]
    data, data_sigma = construct_dataset()
    coeff_mat = coefficient_matrix()
    a, _, _, _ = np.linalg.lstsq(coeff_mat, data, rcond=None)
    c = np.array([1, cugre, cugre**2, cuu, cuu**2, cugre*cuu])
    xsec = np.dot(a, c)
    luminosity = 6 # pb^-1
    return xsec*luminosity
    #print("The cross-section at (cugre, cuu) = ({}, {}) is: ".format(cugre, cuu), xsec)


if __name__ == '__main__':



    # expected_events_binned(c, bins, path_output)
    bins = np.array([300, 400, 500, 600, 4000])
    path_output = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_2_v3'
    #xsec_binned(bins, path_output)
    path_xsec_binned = os.path.join(path_output, "xsec_bin.npy")
    with open(path_xsec_binned, 'rb') as f:
        dataset = np.load(f)

    n_data_last_bin = luminosity*dataset[6:12][:, 3]



    n_i_bin_0 = []
    cuu = np.linspace(-11, 11, 100)
    for c in cuu:
        n_i_bin_0.append(expected_events_binned(np.array([0, c]), bins, path_output)[3])
    n_i_bin_0 = np.array(n_i_bin_0)

    plt.figure(figsize=(10, 6))
    ax = plt.subplot(111)



    ax.scatter(np.array([-10, -5, -1, 1, 5, 10]), n_data_last_bin, color='C0')
    ax.set_title(r'$\rm{Expected\;countings\;bin\;4}$', fontsize=20)


    ax.plot(cuu, n_i_bin_0, color='C1')
    # ax.set_ylabel(r'$\rm{\chi^2}$', fontsize=20)
    ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
    # ax.set_xlim((0.38, 1.42))
    # ax.set_xlim((0, 5))
    # ax.set_ylim((0, 0))

    plt.tight_layout()

    # plt.show()
    plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/n_i_pred.pdf')

    #print(n_i_bin_0)


