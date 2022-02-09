import pylhe
import pandas as pd
import quad_clas.preproc.lhe_reader.compute_kinematics as lhe

path_to_lhe = '/Users/jaco/Documents/ML4EFT/MG5_aMC_v2.7.3/bin/pp_zh_llbb_sm_narrow_width/Events/run_66/unweighted_events.lhe'

events = []
for e in pylhe.readLHE(path_to_lhe):

    # create particle instances
    l1 = lhe.Kinematics(e.particles[-4])
    l2 = lhe.Kinematics(e.particles[-3])
    z_boson = lhe.Kinematics(e.particles[2])
    b = lhe.Kinematics(e.particles[-1])
    bbar = lhe.Kinematics(e.particles[-2])

    # create particle systems
    bb = b + bbar
    l_b = l1 + b
    ll = l1 + l2

    events.append([bb.get_inv_mass(), ll.get_inv_mass()])

df = pd.DataFrame(events, columns = ['mbb', 'mll'])


import numpy as np
import matplotlib.pyplot as plt

hist_mg_sm, bins_mg = np.histogram(df['mll'], bins=np.linspace(df['mll'].min(), df['mll'].max(), 50))
plt.step(bins_mg[:-1], hist_mg_sm, c='C0', where='post', label= r'$\mathrm{SM}$')
plt.yscale('log')
plt.show()