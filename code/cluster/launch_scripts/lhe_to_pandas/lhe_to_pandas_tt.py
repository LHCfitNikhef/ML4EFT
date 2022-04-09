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
            if part.id == 6: # t
                t = lhe.Kinematics(part)
            elif part.id == -6: #tbar
                tbar = lhe.Kinematics(part)

        # create particle systems
        tt = t + tbar

        # append kinematics
        events.append([t.get_pt() * 1e-3,
                       tt.get_inv_mass() * 1e-3,
                       tt.get_rapidity()
                       ])

    events.insert(0, [xsec] * len(events[0]))
    df = pd.DataFrame(events, columns=['pt_t',
                                       'm_tt',
                                       'y'
                                       ])

    return df


df = lhe_to_pandas(lhe_path)
df.to_pickle(os.path.join(save_loc, "events_{}.pkl.gz".format(mc_rep)), compression="infer")

