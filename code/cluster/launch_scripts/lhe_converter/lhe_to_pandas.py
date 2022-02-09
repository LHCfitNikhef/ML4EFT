import pylhe
import pandas as pd
import numpy as np
import quad_clas.plotting.features as features
import quad_clas.preproc.lhe_reader.compute_kinematics as lhe


path_to_lhe = '/Users/jaco/Documents/ML4EFT/MG5_aMC_v2.7.3/bin/pp_zh_llbb_sm_narrow_width/Events/run_66/unweighted_events.lhe'

events = []
for e in pylhe.readLHE(path_to_lhe):

    # create particle instances
    l1 = lhe.Kinematics(e.particles[-4])
    l2 = lhe.Kinematics(e.particles[-3])
    z = lhe.Kinematics(e.particles[2])
    b = lhe.Kinematics(e.particles[-1])
    bbar = lhe.Kinematics(e.particles[-2])

    # create particle systems
    bb = b + bbar
    l_b = l1 + b
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

df = pd.DataFrame(events, columns=['pt_z',
                                   'pt_b',
                                   'pt_bbar',
                                   'm_bb',
                                   'deltaR_bb',
                                   'deltaPhi_b_bb',
                                   'deltaEta_z_bb',
                                   'm_ll',
                                   'deltaPhi_l_b'])

fig = features.plot_features(df)
fig.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/09_02/features.pdf')
