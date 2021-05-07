# Author: Jaco ter Hoeve
# This file computes the expected number of events under either the SM (H_1) or the SMEFT (H_0)
# by fitting a quadratic polynomial to the madgraph xsecs


import pylhe
import numpy as np
from matplotlib import pyplot as plt
import sys

import bounds_2 as bnds

eft_points = [[-10.0, 0], [-5.0, 0], [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0], [0, -2.0], [0, -1.0], [0, -0.5],[0, 0.5], [0, 1.0], [0, 2.0], [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],[10.0, 2.0], [0.0, 0.0]]

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

def construct_dataset_binned(bins):
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
        path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{}/bin/process_{}/Events/run_01/unweighted_events.lhe'.format(i, i)

        n_tot = 10000
        data = bnds.load_data(path, n=n_tot, s=n_tot)
        n_i, _ = np.histogram(data, bins=bins)

        xsec, _ = load_datapoint(path)
        sigma_i = n_i/n_tot * xsec
        dataset.append(sigma_i)

    dataset = np.array(dataset)  # dataset.shape = (len(eft_points), len(bins))

    #  write the dataset to a separate file
    path_file = "/data/theorie/jthoeve/ML4EFT/quad_clas/xsec_bin.npy"
    with open(path_file, 'wb') as f:
        np.save(f, dataset)


def expected_events_binned(c):
    cugre = c[0]
    cuu = c[1]

    path_file = "/data/theorie/jthoeve/ML4EFT/quad_clas/xsec_bin.npy"
    with open(path_file, 'rb') as f:
        dataset = np.load(f)
    coeff_mat = coefficient_matrix()
    a, _, _, _ = np.linalg.lstsq(coeff_mat, dataset, rcond=None)
    c = np.array([1, cugre, cugre ** 2, cuu, cuu ** 2, cugre * cuu])
    xsec = np.einsum('ij,i', a, c)
    luminosity = 6   # pb^-1
    return xsec*luminosity


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
    cugre = 0
    cuu = 0
    nevents = expected_nevents(np.array([cugre, cuu]))

    bins = np.array([300, 400, 500, 4000])
    data_loaded = True
    if not data_loaded:
        construct_dataset_binned(bins)
    xsec = expected_events_binned(np.array([cugre, cuu]))
    print("sum over bins ", np.sum(xsec))
    print("total xsec ", np.sum(nevents))


