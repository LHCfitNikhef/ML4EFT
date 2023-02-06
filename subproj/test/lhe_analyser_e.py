import pylhe
import pandas as pd
import numpy as np
import sys, os
import subprocess
import ml4eft.preproc.lhe_reader as lhe

path_to_lhe = "/data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/unweighted_events.lhe.gz"

def lhe_to_pandas(lhe_file):

    lhe_init = pylhe.read_lhe_init(path_to_lhe)

    xsec = 0
    for process in lhe_init['procInfo']:
        xsec += process['xSection']

    events = []

    for e in pylhe.read_lhe(path_to_lhe):
        # create particle instances
        for part in e.particles:
            if part.id == 6: # t
                t = lhe.Kinematics(part)

            elif part.id == -6: #tbar
                tbar = lhe.Kinematics(part)

        # create particle systems
        tt = t + tbar
        px, py, pz, e = tt.get_pxpypze()
        # append kinematics
        events.append([px * 1e-3,py* 1e-3,pz* 1e-3,e*1e-3,
                       t.get_pt() * 1e-3,
                       tt.get_inv_mass() * 1e-3,
                       tbar.get_inv_mass() * 1e-3
                       ])

    # events.insert(0, [xsec] * len(events[0])) #for now I don't want the crossec
    df = pd.DataFrame(events, columns=["tt_px","tt_py","tt_pz","tt_e",
                                       'pt_t',
                                       'm_tt','m_tbar'
                                       ])

    return df

output = lhe_to_pandas(path_to_lhe)
print(output)