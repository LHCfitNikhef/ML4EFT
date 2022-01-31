import pylhe
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import lhapdf
from matplotlib.ticker import FormatStrFormatter

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 14})
rc('text', usetex=True)

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
s = 13 ** 2
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


def get_phi(p):
    p_x = getattr(p, 'px')
    p_y = getattr(p, 'py')
    if p_x and p_y > 0:
        phi = np.arctan(p_x / p_y)
    elif p_y < 0:
        phi = np.arctan(p_x / p_y) + np.pi
    else:
        phi = 2 * np.pi + np.arctan(p_x / p_y)
    return phi


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
    return d_phi


def get_d_eta(p1, p2):
    eta_1 = get_eta(p1)
    eta_2 = get_eta(p2)
    d_eta = np.abs(eta_2 - eta_1)
    return d_eta

path_to_lhe_eft = '/Users/jaco/Documents/ML4EFT/MG5_aMC_v2.7.3/bin/uu_zh_eebb_cdhre_quad/Events/run_01_0/unweighted_events.lhe'
path_to_lhe_sm = '/Users/jaco/Documents/ML4EFT/MG5_aMC_v2.7.3/bin/uu_zh_eedd_sm/Events/run_01_0/unweighted_events.lhe'
#path_to_lhe = '/Users/jaco/Documents/ML4EFT/MG5_aMC_v2.7.3/bin/uu_zh_2b2e/Events/run_01/unweighted_events.lhe'



def read_events(path_to_lhe):

    found_weight = False
    data_madgraph = []

    for e in pylhe.readLHE(path_to_lhe):
        if not found_weight:
            tot_xsec = e.eventinfo.weight
            found_weight = True
            data_madgraph.append([tot_xsec, tot_xsec, tot_xsec, tot_xsec])

        d_eta_bb = np.abs(get_d_eta(e.particles[-1], e.particles[-2]))
        d_phi_bb = np.abs(get_d_phi(e.particles[-1], e.particles[-2]))
        d_R_bb = np.sqrt(d_eta_bb ** 2 + d_phi_bb ** 2)
        m_bb = get_inv_mass(e.particles[-1], e.particles[-2])
        data_madgraph.append([d_eta_bb, d_phi_bb, d_R_bb, m_bb])
    data_madgraph = np.array(data_madgraph)
    return data_madgraph

data_sm = read_events(path_to_lhe_sm)
data_eft = read_events(path_to_lhe_eft)

bin_width = 0.1

n_cols = 2
n_rows = 2
fig = plt.figure(figsize=(n_cols * 6, n_rows * 4))

x_labels = [r'$|\Delta\eta(b_1, b_2)|$', r'$\Delta\phi(b_1, b_2)$', r'$\Delta R(b_1, b_2)$', r'$m_{b\bar{b}}\;[\mathrm{GeV}]$']
y_labels = [r'$d\sigma/d\Delta\eta\;\mathrm{[pb]}$', r'$d\sigma/d\Delta\phi\;\mathrm{[pb]}$', r'$d\sigma/d\Delta R\;\mathrm{[pb]}$', r'$d\sigma/dm_{b\bar{b}}\;\mathrm{[pb\:GeV^{-1}]}$']

for i in range(n_cols * n_rows):
    ax = plt.subplot(n_rows, n_cols, i + 1)
    events_sm = data_sm[1:, i]
    hist_mg_sm, bins_mg = np.histogram(events_sm,
                                    bins=np.linspace(np.min(events_sm), np.max(events_sm), 40),
                                    density=True)
    #hist_mg_sm *= data_sm[0, 0]

    events_eft = data_eft[1:, i]
    hist_mg_eft, _ = np.histogram(events_eft,
                                       bins=np.linspace(np.min(events_eft), np.max(events_eft), 40),
                                       density=True)
    #hist_mg_eft *= data_eft[0, 0]

    plt.step(bins_mg[:-1], hist_mg_sm, c='C0', where='post', label= r'$\mathrm{SM}$')
    plt.step(bins_mg[:-1], hist_mg_eft, c='C1', where='post', label=r'$\mathrm{EFT}$')
    plt.xlim((np.min(events_sm), np.max(events_eft)))
    plt.ylabel(y_labels[i])
    plt.xlabel(x_labels[i])
    plt.yscale('log')
    ax.xaxis.set_major_formatter(FormatStrFormatter(r'$%.2f$'))
    plt.legend()

#plt.show()
plt.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/31_01/decay_kinematics_bb.pdf')