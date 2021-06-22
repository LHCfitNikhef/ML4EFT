# Author: Jaco ter Hoeve

# This is a python library that contains all the functions needed to read and analyse lhe-files as produced by MadGraph

import numpy as np
import pylhe


def invariant_mass(p1, p2):
    """
    Computes the invariant mass of an event
    """
    return np.sqrt(
        sum((1 if mu == 'e' else -1) * (getattr(p1, mu) + getattr(p2, mu)) ** 2 for mu in ['e', 'px', 'py', 'pz']))

def rapidity(p1, p2):
    """
    Computes the rapidity of an event
    """
    q0 = getattr(p1, 'e') + getattr(p2, 'e')  # energy of the top quark pair in the pp COM frame
    q3 = getattr(p1, 'pz') + getattr(p2, 'pz')
    y = 0.5 * np.log((q0 + q3) / (q0 - q3))
    return y

def load_events(path, n, s):
    """ Load a subset of size s from n events from the lhe file.

    Parameters
    ----------
    path: str
        Path to lhe file
    n: int
        total size of the dataset
    s:
        size of the subset
    Returns
    -------
    event_data: ndarray
        The loaded subset of events
    """

    skip = np.random.choice(n, n - s, replace=False)
    event_seq = pylhe.readLHE(path)

    event_data = []

    for i in range(n):
        e = next(event_seq)
        if i not in skip:
            mtt = invariant_mass(e.particles[-1], e.particles[-2])
            y = rapidity(e.particles[-1], e.particles[-2])
            event_data.append([mtt * 10 ** -3, y])
    event_data = np.array(event_data)
    return event_data


def total_xs(path):
    """
    Load the xsec and uncertainty from an lhe file.

    Parameters
    ----------
    path: str
        path to lhe event file

    Returns
    -------
    The total inclusive cross-section plus uncertainty
    """
    proc_info = pylhe.readLHEInit(path)['procInfo']

    xsec_proc = [proc['xSection'] for proc in proc_info]
    error_proc = [proc['error'] for proc in proc_info]

    xsec_proc = np.array(xsec_proc)
    error_proc = np.array(error_proc)

    xsec = np.sum(xsec_proc)
    xsec_error = np.sqrt(np.sum(error_proc ** 2))
    return xsec, xsec_error


# def generate_samples(c):
#     cugre = c[0]
#     cuu = c[1]
#     subprocess.call(['chmod', '+x', '/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh'])
#     subprocess.call(["/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh", '{}'.format(cugre), '{}'.format(cuu)])
#     path = "/data/theorie/jthoeve/ML4EFT/mg5_copies/mg5_test/bin/process_0/Events/run_01/unweighted_events.lhe"
#     return path