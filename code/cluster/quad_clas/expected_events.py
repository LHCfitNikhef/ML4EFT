# Author: Jaco ter Hoeve
# This file computes the expected number of events under either the SM (H_1) or the SMEFT (H_0)


import pylhe
import numpy as np
from matplotlib import pyplot as plt

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


def expected_nevents(c):
    cugre = c[0]
    cuu = c[1]
    data, data_sigma = construct_dataset()
    coeff_mat = coefficient_matrix()
    a, _, _, _ = np.linalg.lstsq(coeff_mat, data, rcond=None)
    c = np.array([1, cugre, cugre**2, cuu, cuu**2, cugre*cuu])
    xsec = np.dot(a, c)
    luminosity = 6*10**6 # pb^-1
    return xsec*luminosity
    #print("The cross-section at (cugre, cuu) = ({}, {}) is: ".format(cugre, cuu), xsec)


if __name__ == '__main__':
    cugre = -5
    cuu = -1
    nevents = expected_nevents(cugre, cuu)

