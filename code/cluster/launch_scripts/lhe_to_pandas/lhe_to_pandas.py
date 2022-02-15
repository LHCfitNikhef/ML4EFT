import pylhe
import pandas as pd
import numpy as np
import sys, os
import quad_clas.preproc.lhe_reader.compute_kinematics as lhe

lhe_path = sys.argv[1]
save_loc = sys.argv[2]
mc_rep = sys.argv[3]


def lhe_to_pandas(path_to_lhe):

    lhe_init = pylhe.readLHEInit(path_to_lhe)
    xsec = lhe_init['procInfo'][0]['xSection']

    events = []
    for e in pylhe.readLHE(path_to_lhe):
        # create particle instances
        for part in e.particles:
            if part.id in [11, 13]: # e^- or \mu^-
                l1 = lhe.Kinematics(part)
            elif part.id in [-11, -13]: # e^+ or \mu^+
                l2 = lhe.Kinematics(part)
            elif part.id == 23: # z boson
                z = lhe.Kinematics(part)
            elif part.id == 5: # b
                b = lhe.Kinematics(part)
            elif part.id == -5: #bbar
                bbar = lhe.Kinematics(part)

        # create particle systems
        bb = b + bbar
        ll = l1 + l2

        # delta kinematics
        d_eta_b_bbar = lhe.get_deta(b.get_rapdity(), bbar.get_rapdity())

        d_phi_b_bb = lhe.get_dphi(b.get_phi(), bb.get_phi())
        d_phi_l_b = lhe.get_dphi(l1.get_phi(), b.get_phi())
        d_eta_z_bb = lhe.get_deta(z.get_rapdity(), bb.get_rapdity())

        d_phi_b_bbar = lhe.get_dphi(b.get_phi(), bbar.get_phi())
        d_R_b_bbar = np.sqrt(d_eta_b_bbar ** 2 + d_phi_b_bbar ** 2)

        # append kinematics
        events.append([z.get_pt(),
                       b.get_pt(),
                       bbar.get_pt(),
                       bb.get_inv_mass(),
                       d_R_b_bbar,
                       d_phi_b_bb,
                       d_eta_z_bb,
                       ll.get_inv_mass(),
                       d_phi_l_b
                       ])

    events.insert(0, [xsec] * len(events[0]))
    df = pd.DataFrame(events, columns=['pt_z',
                                       'pt_b',
                                       'pt_bbar',
                                       'm_bb',
                                       'deltaR_bb',
                                       'deltaPhi_b_bb',
                                       'deltaEta_z_bb',
                                       'm_ll',
                                       'deltaPhi_l_b'])

    return df


df = lhe_to_pandas(lhe_path)
df.to_pickle(os.path.join(save_loc, "events_{}.pkl.gz".format(mc_rep)), compression="infer")

