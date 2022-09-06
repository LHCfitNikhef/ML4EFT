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

def lhe_to_pandas(path_to_lhe):

    lhe_init = pylhe.readLHEInit(path_to_lhe)

    xsec = 0
    for process in lhe_init['procInfo']:
        xsec += process['xSection']

    events = []

    for e in pylhe.readLHE(path_to_lhe):

        incoming_part = []
        # create particle instances
        for part in e.particles:

            if part.status == -1.0:  # select incoming particles
                incoming_part.append(lhe.Kinematics(part))
            elif part.id in [11, 13]: # e^- or \mu^-
                l1 = lhe.Kinematics(part)
            elif part.id in [-11, -13]: # e^+ or \mu^+
                l2 = lhe.Kinematics(part)
            elif part.id == 5: # b
                b = lhe.Kinematics(part)
            elif part.id == -5: #bbar
                bbar = lhe.Kinematics(part)

        #d_eta_l_b = lhe.get_deta(l1.get_pseudorapidity(), b.get_pseudorapidity())
        #d_phi_l_b = lhe.get_dphi(l1.get_phi(), b.get_phi())
        #d_R_l_b = np.sqrt(d_eta_l_b ** 2 + d_phi_l_b ** 2)

        # create particle systems
        ll = l1 + l2
        bb = b + bbar
        system = incoming_part[0] + incoming_part[1]  # 2 incoming particles

        pt_l1 = l1.get_pt()
        pt_l2 = l2.get_pt()

        pt_leading_l = np.max([pt_l1, pt_l2])
        pt_trailing_l = np.min([pt_l1, pt_l2])

        eta_l1 = l1.get_pseudorapidity()
        eta_l2 = l2.get_pseudorapidity()
        eta_leading_l = eta_l1 if pt_l1 > pt_l2 else eta_l2
        eta_trailing_l = eta_l1 if pt_l1 < pt_l2 else eta_l2

        pt_b = b.get_pt()
        pt_bbar = bbar.get_pt()

        pt_leading_bjet = np.max([pt_b, pt_bbar])
        pt_trailing_bjet = np.min([pt_b, pt_bbar])

        eta_b = b.get_pseudorapidity()
        eta_bbar = bbar.get_pseudorapidity()
        eta_leading_bjet = eta_b if pt_b > pt_bbar else eta_bbar
        eta_trailing_bjet = eta_b if pt_b < pt_bbar else eta_bbar



        # append kinematics
        events.append([system.get_inv_mass(),
                       l1.get_pt(),
                       l2.get_pt(),
                       pt_leading_l,
                       pt_trailing_l,
                       l1.get_pseudorapidity(),
                       l2.get_pseudorapidity(),
                       eta_leading_l,
                       eta_trailing_l,
                       ll.get_pt(),
                       ll.get_inv_mass(),
                       lhe.get_dphi(l1.get_phi(), l2.get_phi()),
                       np.abs(l1.get_pseudorapidity()) - np.abs(l2.get_pseudorapidity()),
                       pt_leading_bjet,
                       pt_trailing_bjet,
                       eta_leading_bjet,
                       eta_trailing_bjet,
                       bb.get_pt(),
                       bb.get_inv_mass(),

           ])

        feature_names = ['sqrts_hat',
                         'pt_l1',
                         'pt_l2',
                         'pt_l_leading',
                         'pt_l_trailing',
                         'eta_l1',
                         'eta_l2',
                         'eta_l_leading',
                         'eta_l_trailing',
                         'pt_ll',
                         'm_ll',
                         'DeltaPhi_ll',
                         'DeltaEta_ll',
                         'pt_b_leading',
                         'pt_b_trailing',
                         'eta_b_leading',
                         'eta_b_trailing',
                         'pt_bb',
                         'm_bb']

    events.insert(0, [xsec] * len(events[0]))
    df = pd.DataFrame(events, columns=feature_names)

    return df

rep_nr = 0
if os.path.basename(event_dir).startswith(process) is True:

    job_dirs = os.listdir(event_dir)

    # loop over all jobs
    for job in job_dirs:

        #run_path = os.path.join(event_dir, job, 'Events')
        run_path = "/data/theorie/jthoeve/ML4EFT_events/tt_sm/job54/Events"
        # exclude non-job directories
        if not job.startswith('job'):
            continue

        # check for successful run
        if len(os.listdir(run_path)) == 0:
            continue
        else:
            run_nrs = [int(runs.split("_", 1)[-1]) for runs in os.listdir(run_path)]
            run_nr_max = max(run_nrs)

        # build lhe path
        if run_nr_max < 10:
            lhe_path = os.path.join(run_path, 'run_0{}'.format(run_nr_max), 'unweighted_events.lhe')
        else:
            lhe_path = os.path.join(run_path, 'run_{}'.format(run_nr_max), 'unweighted_events.lhe')

        # extract .gz file if necessary
        if os.path.isfile('{}.gz'.format(lhe_path)):
            subprocess.run("gunzip {}.gz".format(lhe_path), shell=True)

        # feed lhe file to pandas converter
        df = lhe_to_pandas(lhe_path)

        event_name = os.path.basename(event_dir)
        save_dir = os.path.join(save_root, event_name)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        df.to_pickle(os.path.join(save_dir, "events_{}.pkl.gz".format(54)), compression="infer")
        break
        rep_nr += 1


