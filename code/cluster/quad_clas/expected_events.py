import pylhe
import numpy as np
from matplotlib import pyplot as plt

eft_points = [[-10.0, 0], [-5.0, 0], [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0], [0, -2.0], [0, -1.0], [0, -0.5],[0, 0.5], [0, 1.0], [0, 2.0], [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],[10.0, 2.0], [0.0, 0.0]]


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


def main():
    data, data_sigma = construct_dataset()
    print(data, data_sigma)


if __name__ == '__main__':
    main()
