import pylhe
import pandas as pd
import numpy as np
import sys, os
from pathlib import Path
import subprocess
import quad_clas.preproc.lhe_reader.compute_kinematics as lhe


event_dir = sys.argv[1]
process = sys.argv[2]
save_root = sys.argv[3]
n_rep = sys.argv[4]

def lhe_to_pandas(path_to_lhe):

    lhe_init = pylhe.readLHEInit(path_to_lhe)

    xsec = 0
    for process in lhe_init['procInfo']:
        xsec += process['xSection']

    events = []

    for e in pylhe.readLHE(path_to_lhe):
        # create particle instances
        for part in e.particles:

            if part.id in [11, 13]: # e^- or \mu^-
                l1 = lhe.Kinematics(part)
            elif part.id in [-11, -13]: # e^+ or \mu^+
                l2 = lhe.Kinematics(part)
            elif part.id in [12, 14]: # vl
                vl = lhe.Kinematics(part)
            elif part.id in [-12, -14]: # vl
                vlbar = lhe.Kinematics(part)
            elif part.id == 5: # b
                b = lhe.Kinematics(part)
            elif part.id == -5: #bbar
                bbar = lhe.Kinematics(part)

        d_eta_l_b = lhe.get_deta(l1.get_pseudorapidity(), b.get_pseudorapidity())
        d_phi_l_b = lhe.get_dphi(l1.get_phi(), b.get_phi())
        d_R_l_b = np.sqrt(d_eta_l_b ** 2 + d_phi_l_b ** 2)

        # create particle systems
        ll = l1 + l2
        v = vl + vlbar


        # append kinematics
        events.append([ll.get_inv_mass(),
                       l1.get_pt(),
                       l2.get_pt(),
                       b.get_pt(),
                       b.get_pseudorapidity(),
                       d_R_l_b,
                       v.get_pt()])

    events.insert(0, [xsec] * len(events[0]))
    df = pd.DataFrame(events, columns=['m_ll', 'pt_l1', 'pt_l2', 'pt_b', 'eta_b', 'deltaR_lb', 'Etmiss'
                                       ])

    return df

if os.path.basename(event_dir).startswith(process) is True:

    for r in range(int(n_rep)):

        run_path = os.path.join(event_dir, "job{}".format(r+1), 'Events')

        if len(os.listdir(run_path)) != 0:
            run_nrs = [int(runs.split("_", 1)[-1]) for runs in os.listdir(run_path)]
            run_nr_max = max(run_nrs)
        else:
            print(run_path)
            continue

        if run_nr_max < 10:
            lhe_path = os.path.join(run_path, 'run_0{}'.format(run_nr_max), 'unweighted_events.lhe')
        else:
            lhe_path = os.path.join(run_path, 'run_{}'.format(run_nr_max), 'unweighted_events.lhe')

        if os.path.isfile('{}.gz'.format(lhe_path)):
            subprocess.run("gunzip {}.gz".format(lhe_path), shell=True)

        df = lhe_to_pandas(lhe_path)


        event_name = os.path.basename(event_dir)
        save_dir = os.path.join(save_root, event_name)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        df.to_pickle(os.path.join(save_dir, "events_{}.pkl.gz".format(r)), compression="infer")


