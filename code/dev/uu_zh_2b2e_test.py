import pylhe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import lhapdf
from matplotlib.ticker import FormatStrFormatter
import copy

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 12})
rc('text', usetex=True)

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
s = 14 ** 2
mz = 91.188 * 10 ** -3 # z boson mass [TeV]
mh = 125 * 10 ** -3 # h boson mass [TeV]
mw = 80.41900 * 10 ** -3
Gf = 0.0000116639 * 10 ** 6
mu = 91.188
pb_convert = 3.894E2


def get_inv_mass(p1, p2):
    return np.sqrt(
        sum((1 if mu == 'e' else -1) * (getattr(p1, mu) + getattr(p2, mu)) ** 2 for mu in ['e', 'px', 'py', 'pz']))


def get_pt(p):
    return np.sqrt(getattr(p, 'px') ** 2 + getattr(p, 'py') ** 2)


def get_p(p):
    return np.sqrt(getattr(p, 'px') ** 2 + getattr(p, 'py') ** 2 + getattr(p, 'pz') ** 2)


def add_p(p1, p2):
    temp = copy.deepcopy(p1)
    temp.px = p1.px + p2.px
    temp.py = p1.py + p2.py
    temp.pz = p1.pz + p2.pz
    return temp

def get_phi(p):
    p_x = getattr(p, 'px')
    p_y = getattr(p, 'py')

    if p_x / p_y > 0:
        return np.arctan(p_x / p_y)
    else:
        return np.arctan(p_x / p_y) + np.pi
    # if p_x and p_y > 0:
    #     phi = np.arctan(p_x / p_y)
    # elif p_y < 0:
    #     phi = np.arctan(p_x / p_y) + np.pi
    # else:
    #     phi = 2 * np.pi + np.arctan(p_x / p_y)
    #return phi


def get_theta(p):
    cos_theta = getattr(p, 'pz') / get_p(p)
    return np.arccos(cos_theta)


def get_eta(p):
    theta = get_theta(p)
    eta = - np.log(np.tan(theta/2))
    return eta


def get_d_phi(p1, p2):
    phi_1 = get_phi(p1)
    phi_2 = get_phi(p2)
    d_phi = np.abs(phi_2 - phi_1)
    if d_phi > np.pi:
        return 2 * np.pi - d_phi
    else:
        return d_phi


def get_d_eta(p1, p2):
    eta_1 = get_eta(p1)
    eta_2 = get_eta(p2)
    d_eta = np.abs(eta_2 - eta_1)
    return d_eta

# top flavour scheme
path_to_lhe_eft = '/Users/jaco/Documents/ML4EFT/code/dev/unweighted_events_chdd.lhe'
path_to_lhe_sm = '/Users/jaco/Documents/ML4EFT/code/dev/unweighted_events_sm_100K.lhe'

# topU31 flavour scheme
# path_to_lhe_eft = '/Users/jaco/Documents/ML4EFT/MG5_aMC_v2.7.3/bin/pp_zh_eebb_cHDD_topU3l/Events/run_01_0/unweighted_events.lhe'
# path_to_lhe_sm = '/Users/jaco/Documents/ML4EFT/MG5_aMC_v2.7.3/bin/pp_zh_eebb_sm_topU3l/Events/run_01_0/unweighted_events.lhe'


def read_events(path_to_lhe):

    found_weight = False
    data_madgraph = []

    cnt = 0
    for e in pylhe.readLHE(path_to_lhe):
        if cnt == 100000:
            break
        if not found_weight:
            tot_xsec = e.eventinfo.weight
            found_weight = True

            #data_madgraph.append([tot_xsec, tot_xsec, tot_xsec, tot_xsec, tot_xsec, tot_xsec])

        pt_z = get_pt(e.particles[2])
        pt_b1 = get_pt(e.particles[-2])
        pt_b2 = get_pt(e.particles[-1])
        m_bb = get_inv_mass(e.particles[-1], e.particles[-2])

        d_eta_bb = np.abs(get_d_eta(e.particles[-1], e.particles[-2]))
        d_phi_bb = np.abs(get_d_phi(e.particles[-1], e.particles[-2]))
        d_R_bb = np.sqrt(d_eta_bb ** 2 + d_phi_bb ** 2)

        bb_syst = add_p(e.particles[-1], e.particles[-2])
        #d_phi_z_bb = np.abs(get_d_phi(e.particles[2], bb_syst))
        d_phi_b_bb = np.abs(get_d_phi(e.particles[-1], bb_syst))
        d_phi_l_b = np.abs(get_d_phi(e.particles[-1], e.particles[-3]))

        d_eta_z_bb = np.abs(get_d_eta(e.particles[2], bb_syst))
        m_ll = get_inv_mass(e.particles[-3], e.particles[-4])

        data_madgraph.append([pt_z, pt_b1, pt_b2, m_bb, d_R_bb, d_phi_b_bb, d_eta_z_bb, m_ll, d_phi_l_b])

        cnt += 1
    data_madgraph = np.array(data_madgraph)
    return data_madgraph, tot_xsec

data_sm, xsec_sm = read_events(path_to_lhe_sm)
data_eft, xsec_eft = read_events(path_to_lhe_eft)

bin_width = 0.1

n_cols = 2
n_rows = 5
fig = plt.figure(figsize=(n_cols * 5, n_rows * 4))

x_labels = [r'$p_T^Z$',
            r'$p_T^{b_1}\;[\mathrm{GeV}]$',
            r'$p_T^{b_2}\;[\mathrm{GeV}]$',
            r'$m_{b\bar{b}}\;[\mathrm{GeV}]$',
            r'$\Delta R(b_1, b_2)$',
            r'$\Delta\phi(b, bb)$',
            r'$|\Delta \eta(Z, bb)|$',
            r'$m_{ll}$',
            r'$\Delta\phi(b, l)$'
           ]
#y_labels = [r'$1/\sigma(d\sigma/d\Delta\eta)$', r'$1/\sigma(d\sigma/d\Delta\phi)$', r'$1/\sigma(d\sigma/d\Delta R)$', r'$1/\sigma(d\sigma/dm_{b\bar{b}})\;\mathrm{[GeV^{-1}]}$',  r'$1/\sigma(d\sigma/dp_T^{b_2})\;\mathrm{[GeV^{-1}]}$',  r'$1/\sigma(d\sigma/dp_T^{b_2})\;\mathrm{[GeV^{-1}]}$']

for i in range(n_cols * n_rows - 1):
    ax = plt.subplot(n_rows, n_cols, i + 1)
    #events_sm = data_sm[1:, i]
    events_sm = data_sm[:, i]
    hist_mg_sm, bins_mg = np.histogram(events_sm,
                                    bins=np.linspace(np.min(events_sm), np.max(events_sm), 50),
                                    density=True)
    #hist_mg_sm *= xsec_sm

    events_eft = data_eft[:, i]
    hist_mg_eft, _ = np.histogram(events_eft,
                                       bins=np.linspace(np.min(events_eft), np.max(events_eft), 50),
                                       density=True)
    #hist_mg_eft *= xsec_eft

    plt.step(bins_mg[:-1], hist_mg_sm, c='C0', where='post', label= r'$\mathrm{SM}$')
    plt.step(bins_mg[:-1], hist_mg_eft, c='C1', where='post', label=r'$\mathrm{EFT}\;(\mathrm{chD}=50)$')

    plt.xlim((np.min(events_sm), np.max(events_eft)))
    #plt.xlim((np.min(events_sm), np.max(events_eft)))
    #plt.ylabel(y_labels[i])
    plt.xlabel(x_labels[i])
    plt.yscale('log')
    ax.xaxis.set_major_formatter(FormatStrFormatter(r'$%.2f$'))
    # ax.text(0.05, 0.05, r'$\mathrm{cHD}=10$',
    #      horizontalalignment='left',
    #      verticalalignment='center',
    #      transform=ax.transAxes)
    plt.legend(fontsize=10)

#plt.show()
plt.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/04_02_meeting/decay_kinematics_chD.pdf')