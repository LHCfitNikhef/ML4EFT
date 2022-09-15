# This file loads a lhe file, computes observables and stores them as a npy binary file, which is faster
# to load then the lhe file.

from ..core.lhelib import lhe
import pylhe
import numpy as np
import os


def lhe_to_npy(n_processes):
    for mc_run in range(1, 41):
        for process in range(n_processes):
            print("Loading data file {}".format(process))
            if mc_run < 10:
                root_path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{process}/bin/process_{process}/Events/run_{mc_run}'.format(
                process=process, mc_run=str(0)+str(mc_run))
            else:
                root_path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{process}/bin/process_{process}/Events/run_{mc_run}'.format(
                    process=process, mc_run=mc_run)
            path = os.path.join(root_path, 'unweighted_events.lhe')
            data = []
            for e in pylhe.readLHE(path):
                mtt = lhe.invariant_mass(e.particles[-1], e.particles[-2])
                y = lhe.rapidity(e.particles[-1], e.particles[-2])
                weight = e.eventinfo.weight
                data.append([mtt, y, weight])
            data = np.array(data)

            np.save(os.path.join(root_path, 'event_data.npy'), data)
