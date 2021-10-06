# %%
import vegas
import math
import numpy as np
import lhapdf
import matplotlib.pyplot as plt
from scipy import integrate
import pylhe
import random
from quad_clas.core import xsec_cluster as xsec
from quad_clas.core.lhelib import lhe as lhe
import sys

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
s = 14 ** 2  # Collider COM energy squared [TeV^2]
mu = 91.188  # fact. scale for pdfs = Mz
mt = 0.17276  # top quark mass [TeV]
mw = 80.41900 * 10 ** -3  # w boson mass [TeV]
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125  # h boson mass [TeV]
Gf = 0.0000116639 * 10 ** 6
v = 1 / np.sqrt(Gf * np.sqrt(2))  # vev [TeV]
pb_convert = 3.894E2  # conversion factor to pb


# %%

def sigma_part_vh(hats, cHW, cHq3, lin, quad):
    pz2 = (hats ** 2 + mz ** 4 + mh ** 4 - 2 * hats * mz ** 2 - 2 * hats * mh ** 2 - 2 * mz ** 2 * mh ** 2) / (4 * hats)
    pz = np.sqrt(pz2)
    sth2 = 1 - (mw / mz) ** 2
    cth2 = 1 - sth2
    Vq = 1 / 2 - 4 / 3 * sth2
    Aq = 1 / 2
    xsec_sm = (Gf * mz ** 2) ** 2 / (9 * np.pi) * (Vq ** 2 + Aq ** 2) * pz / np.sqrt(hats) * (3 * mz ** 2 + pz2) / (
                (hats - mz ** 2) ** 2)

    LambdaSMEFT = 1
    xsec_lin_cHW = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * cth2 * Gf * mz ** 2 * (
                9 - 24 * sth2 + 32 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2)
    # xsec_lin_cHWB = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * np.sqrt(cth2) * np.sqrt(sth2) * Gf * mz ** 2 *(9 - 24 * sth2 + 32 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2 )
    xsec_lin_cHq3 = (mz ** 2 * pz * (-3 * mz ** 2 - pz2) * cth2 * Gf * mz ** 2 * sth2 * (4 * sth2 - 3)) / (
                27 * np.sqrt(2) * cth2 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats) * sth2)

    if lin:
        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3
    if quad:
        xsec_quad_cHq3_cHq3 = (mz ** 4 * pz * (3 * mz ** 2 + pz2)) / (
                    36 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats))

        xsec_quad_cHW_cHW = (cth2 ** 2 * mz ** 2 * pz * (3 * mz ** 2 + 2 * pz2) * np.sqrt(hats) * (
                    9 - 24 * sth2 + 32 * sth2 ** 2)) / (81 * np.pi * (mz ** 2 - hats) ** 2)

        xsec_quad_cHW_cHq3 = -(2 * cth2 * mz ** 4 * pz * np.sqrt(mz ** 2 + pz2) * (-3 + 4 * sth2)) / (
                    9 * np.pi * (mz ** 2 - hats) ** 2)

        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3 + \
               cHq3 ** 2 * xsec_quad_cHq3_cHq3 + cHW ** 2 * xsec_quad_cHW_cHW + cHW * cHq3 * xsec_quad_cHW_cHq3  # + cHWB * xsec_lin_cHWB / LambdaSMEFT


# %%
def weight(sqrts, mu, x1, x2, cHW, cHq3, lin, quad):
    """
    NP parameter: order in the EFT
    order parameter: work at one specific order
    """
    hats = sqrts ** 2
    w_ii = (sigma_part_vh(hats, cHW, cHq3, lin, quad)) * (p.xfxQ(2, x1, mu) * p.xfxQ(-2, x2, mu))
    return w_ii


v_weight = np.vectorize(weight, otypes=[np.float])


def dsigma_dmvh_dy(y, mvh, cHW, cHq3, lin, quad):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if mvh == mz + mh: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mvh):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mvh / np.sqrt(s) * np.exp(y)
        x2 = mvh / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mvh / s * v_weight(mvh, 91.188, x1, x2, cHW, cHq3, lin, quad) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0


dsigma_dmtt_dy_vec = np.vectorize(dsigma_dmvh_dy, otypes=[np.float])


def dsigma_dmvh(mvh, cHW, cHq3, lin, quad):
    y_min, y_max = -0.5 * np.log(s / mvh), 0.5 * np.log(s / mvh)
    dsigma_dmtt = integrate.fixed_quad(dsigma_dmtt_dy_vec, y_min, y_max, args=(mvh, cHW, cHq3, lin, quad), n=10)[0]
    return dsigma_dmtt


def mg5_reader(path_to_lhe, bin_width, bin_min):
    data_madgraph = []
    found_weight = False
    for e in pylhe.readLHE(path_to_lhe):
        data_madgraph.append(lhe.invariant_mass(e.particles[-1], e.particles[-2]) * 10 ** -3)
        if found_weight == False:
            weight = e.eventinfo.weight
            found_weight = True
    hist_mg, bins_mg = np.histogram(data_madgraph, bins=np.arange(bin_min, np.max(data_madgraph), bin_width),
                                    density=True)
    hist_mg *= weight
    return hist_mg, bins_mg


# %%

# full = integrate.dblquad(dsigma_dmvh_dy, 0.3, 0.4, lambda x:  -0.5 * np.log(s / x), lambda x: 0.5 * np.log(s / x))
# half = integrate.dblquad(dsigma_dmvh_dy, 0.3, 0.4, lambda x:  0, lambda x: 0.5 * np.log(s / x))
# %%
dsigma_dmvh_vec = np.vectorize(dsigma_dmvh, otypes=[np.float])


def sigma_bin(bins, cHW, cHq3, lin=True, quad=True):
    sigma_i = []
    for i in range(len(bins) - 1):
        temp = integrate.fixed_quad(dsigma_dmvh_vec, bins[i], bins[i + 1], args=(cHW, cHq3, lin, quad), n=10)[0]
        sigma_i.append(temp)
    sigma_i = np.array(sigma_i)
    return sigma_i


# %%
bins = np.linspace(mz + mh, 1, 10)
lin = True
quad = False
a = (sigma_bin(bins, cHW=10, cHq3=0) - sigma_bin(bins, cHW=0, cHq3=0)) / 10


# %%

def findCoeff(bins):
    sm = sigma_bin(bins, cHW=0, cHq3=0)
    cHW_lin = (sigma_bin(bins, cHW=10, cHq3=0, lin=True, quad=False) - sm) / 10
    cHq3_lin = (sigma_bin(bins, cHW=0, cHq3=10, lin=True, quad=False) - sm) / 10

    cHW_quad = (sigma_bin(bins, cHW=10, cHq3=0, lin=False, quad=True) - (sm + 10 * cHW_lin)) / 10 ** 2
    cHq3_quad = (sigma_bin(bins, cHW=0, cHq3=10, lin=False, quad=True) - (sm + 10 * cHq3_lin)) / 10 ** 2

    cHW_cHq3 = (sigma_bin(bins, cHW=10, cHq3=10, lin=False, quad=True) - (
                sm + 10 * cHW_lin + 10 ** 2 * cHW_quad + 10 * cHq3_lin + 10 ** 2 * cHq3_quad)) / 10 ** 2

    coeff = np.array([sm, cHW_lin, cHW_quad, cHq3_lin, cHq3_quad, cHW_cHq3])
    return coeff


def nu_i(bins, cHW, cHq3, luminosity):
    a = findCoeff(bins)
    eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
    xsec = np.einsum('ij,i', a, eft_point)
    nu = xsec * luminosity
    return nu


# %%
lhe_path = "/Users/jaco/Documents/ML4EFT/data/events/vh_benchmark/uubarzh_smeftsim_sm.lhe"
bin_width = 10 * 10 ** -3
# hist_mg, bins_mg = mg5_reader(lhe_path, bin_width, bin_min=mh + mz)

cross_section_vh_vegas = []
x = np.arange(mz + mh + bin_width / 2, 1.0, bin_width)
cross_section_vh = [dsigma_dmtt(mvh) for mvh in x]

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[], xlim=(0.1, 1))

# ax1.step(bins_mg[:-1], hist_mg, c='C0', where='post', label=r'$\rm{mg5}$')
ax1.plot(x, cross_section_vh, '-', c='C1', label=r'$\rm{FormCalc,\;SM}$')

plt.yscale('log')
plt.title(r'$\rm{VH}\;\rm{production}\;\rm{benchmark,}\;\rm{LO+}\mathcal{O}\left(\Lambda^{-4}\right)$')
plt.ylabel(r'$d\sigma/dm_{HZ}\;\mathrm{[pb\:TeV^{-1}]}$')
plt.legend(frameon=False, loc='best')

ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))
# ax2.scatter(x, cross_section_vh/hist_mg[:len(x)], s=10)
ax2.hlines(1, 0.1, 1, colors='k', linestyles='dashed')

plt.ylabel(r'$\rm{num/ana}$')

plt.xlim((0.1, 1))
plt.xlabel(r'$m_{HZ}\;\mathrm{[TeV]}$')
plt.show()

plt.savefig("/Users/jaco/Documents/ML4EFT/plots/uubarzh_smeftsim_quad_cHq3_cHq3.pdf")

# %%
#unbinned plr

# 1. choose a value of c
# 2a. generate a dataset using madgraph: 1M events
# 2b. pick a subset 1K
# 3. Evaluate log L on a grid of c values and subtract L_max
# 4. Compute q and store
# 5. repeat steps 2-4

bins = np.linspace(mz + mh, 1, 2)
a = findCoeff(bins)
cHq3, cHW = 1, 1
eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
xsec = np.einsum('ij,i', a, eft_point)
luminosity = 3000
nu = xsec * luminosity

# ntot = np.random.poisson(nu, 1)
# %%
data_madgraph = []
found_weight = False
path_to_lhe = "/Users/jaco/Documents/ML4EFT/data/events/vh_benchmark/uubarzh_smeftsim_full.lhe"
for e in pylhe.readLHE(path_to_lhe):

    if not found_weight:
        tot_xsec = e.eventinfo.weight
        found_weight = True
    data_madgraph.append(lhe.invariant_mass(e.particles[-1], e.particles[-2]) * 10 ** -3)
data_madgraph = np.array(data_madgraph)
np.save("/Users/jaco/Documents/ML4EFT/data/events/vh_benchmark/mvh_smeftsim.npy", data_madgraph)
# %%
def log_l(ntot, nu, tot_xsec, events, cHW, cHq3):
    event_prob = np.array([dsigma_dmvh(event, cHW, cHq3, lin=False, quad=True) for event in events])
    event_prob /= tot_xsec
    log_l = ntot * np.log(nu) - nu + np.sum(np.log(event_prob))
    return log_l

def log_l_scan(ntot, events):
    cHq3 = 1
    cHWs = np.linspace(0.95, 1.05, 20);
    scanned_l = []
    bins = np.linspace(mz + mh, 1, 2)
    a = findCoeff(bins)
    for cHW in cHWs:
        event_prob = np.array([dsigma_dmvh(event, cHW, cHq3, lin=False, quad=True) for event in events])
        eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
        tot_xsec = np.einsum('ij,i', a, eft_point)
        nu = tot_xsec * luminosity
        event_prob /= tot_xsec
        log_l = ntot * np.log(nu) - nu + np.sum(np.log(event_prob))
        scanned_l.append(log_l)
    return np.max(scanned_l)
#%%
bins = np.linspace(mz + mh, 1, 2)
a = findCoeff(bins)
eft_point = np.array([1, 1, 1, 1, 1, 1])
tot_xsec = np.einsum('ij,i', a, eft_point)
#%%
#tot_xsec = 0.35705
data_madgraph = np.load("/Users/jaco/Documents/ML4EFT/data/events/vh_benchmark/mvh_smeftsim.npy")
nu = tot_xsec * luminosity

# simulate an experiment
log_l_list = []
n_exp = 10
exp = 0
#%%
while exp < n_exp:
    print(exp)
    ntot = np.random.poisson(nu, 1)
    events = np.random.choice(data_madgraph, ntot)
    log_l_num = log_l(ntot, nu, tot_xsec, events, 1, 1)
    log_l_den = log_l_scan(ntot, events)

    log_l_value = -2 * (log_l_num -log_l_den)
    log_l_list.append(log_l_value)
    exp += 1

# %%

# binned PLR without systematics
binning_2 = np.linspace(mz + mh, 1, 6) # 5 bins
nu_i_eft = nu_i(binning_2, 1, 1, 3000) # eft
nu_i_sm = nu_i(binning_2, 0, 0, 3000) # sm
#%%
q_list, q_list_alt, t_asimov = sample_dist(100000, nu_i_eft, nu_i_sm)
#%%
def sample_dist(n_exp, nu_i, nu_i_alt):

    q_list = []
    for i in range(n_exp):
        n_i = np.random.poisson(nu_i, len(nu_i))
        if 0 in n_i:
            continue
        q = 2 * np.sum(n_i * np.log(n_i / nu_i) + nu_i - n_i)
        q_list.append(q)

    q_list_alt = []
    for i in range(n_exp):
        n_i_alt = np.random.poisson(nu_i_alt, len(nu_i_alt))
        if 0 in n_i_alt:
            continue
        q = 2 * np.sum(n_i_alt * np.log(n_i_alt / nu_i) + nu_i - n_i_alt)
        q_list_alt.append(q)

    t_asimov = 2 * np.sum(nu_i_alt * np.log(nu_i_alt / nu_i) + nu_i - nu_i_alt)

    return q_list, q_list_alt, t_asimov


#%%
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(q_list, bins=70, density=True, alpha=0.3)
ax.hist(q_list_alt, bins=70, density=True, alpha=0.3)
plt.show()