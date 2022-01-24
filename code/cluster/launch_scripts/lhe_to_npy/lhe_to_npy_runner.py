import pylhe
import sys, os
import numpy as np

data_madgraph = []
found_weight = False
path_to_lhe = sys.argv[1]
save_loc = sys.argv[2]
mc_rep = sys.argv[3]

def get_pt(p):
    pT = np.sqrt(getattr(p, 'px') ** 2 + getattr(p, 'py') ** 2)
    return pT

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

for e in pylhe.readLHE(path_to_lhe):
    if not found_weight:
        tot_xsec = e.eventinfo.weight
        found_weight = True
        data_madgraph.append([tot_xsec, tot_xsec, tot_xsec]) # quick and dirty
    mvh = invariant_mass(e.particles[-1], e.particles[-2]) * 10 ** -3
    yvh = rapidity(e.particles[-1], e.particles[-2])
    ptz = get_pt(e.particles[-2]) * 10 ** -3
    data_madgraph.append([mvh, yvh, ptz])
data_madgraph = np.array(data_madgraph)
np.save(os.path.join(save_loc, "events_{}.npy".format(mc_rep)), data_madgraph)