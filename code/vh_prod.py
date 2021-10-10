#%%
import vegas
import numpy as np
import lhapdf
import matplotlib.pyplot as plt
from scipy import integrate
import pylhe
from quad_clas.core.lhelib import lhe as lhe

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
s = 14 ** 2 # Collider COM energy squared [TeV^2]
mu = 91.188 # fact. scale for pdfs = Mz
mt = 0.17276 # top quark mass [TeV]
mw = 80.41900 * 10 ** -3  # w boson mass [TeV]
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125# h boson mass [TeV]
Gf = 0.0000116639 * 10 ** 6
v = 1 / np.sqrt(Gf * np.sqrt(2))  # vev [TeV]
pb_convert = 3.894E2 # conversion factor to pb

#%%

def sigma_part_vh(hats, cHW=0, cHWB=0, cHq3=0):
    pz2 = (hats ** 2 + mz ** 4 + mh ** 4 - 2 * hats * mz ** 2 - 2 * hats * mh ** 2 - 2 * mz ** 2 * mh ** 2)/(4*hats)
    pz = np.sqrt(pz2)
    sth2 = 1 - (mw / mz) ** 2
    cth2 = 1 - sth2
    Vq = 1 / 2 - 4 / 3 * sth2
    Aq = 1 / 2
    xsec_sm = (Gf * mz ** 2) ** 2 / (9 * np.pi) * (Vq ** 2 + Aq ** 2) * pz / np.sqrt(hats) * (3 * mz ** 2 + pz2)/((hats - mz ** 2) ** 2)

    LambdaSMEFT = 1
    xsec_lin_cHW = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * cth2 * Gf * mz ** 2 *(9 - 24 * sth2 + 32 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2)
    xsec_lin_cHWB = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * np.sqrt(cth2) * np.sqrt(sth2) * Gf * mz ** 2 *(9 - 24 * sth2 + 32 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2 )
    xsec_lin_cHq3 = (mz ** 2 * pz * (-3 * mz ** 2 - pz2) * cth2 * Gf * mz ** 2 * sth2 * (4 * sth2 -3))/(27 * np.sqrt(2) * cth2 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats) * sth2)

    xsec_quad_cHq3_cHq3 = (mz ** 4 * pz * (3 * mz ** 2 + pz2))/(36 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats))

    return xsec_sm + cHW * xsec_lin_cHW / LambdaSMEFT + cHWB * xsec_lin_cHWB / LambdaSMEFT + cHq3 * xsec_lin_cHq3 / LambdaSMEFT + cHq3 ** 2 * xsec_quad_cHq3_cHq3


def integrand_VH(x, mvh, cHW, cHWB, cHq3):
    """
    When integrated over the rapidity :math:`y` and the azimuthal angle :math:`theta` this
    gives the differential cross section in the invariant mass.

    Parameters
    ----------
    x: list
        [theta, y]
    mtt: float
        invariant mass
    Returns
    -------
    float
        The integrand to be integrated over :math:`y` and :math:`theta`
    """
    if mvh <= mh + mz:
        return 0
    y = x[0]
    hats = mvh ** 2
    x1 = np.sqrt(hats / s) * np.exp(y)
    x2 = np.sqrt(hats / s) * np.exp(-y)
    pdfs = p.xfxQ(2, x1, mu) * p.xfxQ(-2, x2, mu)
    #pdfs = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    return pb_convert * 2 * mvh / s * sigma_part_vh(mvh ** 2, cHW, cHWB, cHq3) * pdfs / (x1 * x2)


def dsigma_dmvh(mvh, nitn=100, neval=1000, cHW=0, cHWB=0, cHq3=0):
    """
    Computes the hadronic cross section differential in the invariant mass.
    It uses the vegas integrator.

    Parameters
    ----------
    mtt: float
        Invariant mass of the outgoing top-pair in TeV
    nitn: int
        Number of iterations of the vegas algorithm
    neval: int
        Each iteration uses no ore than ``neval`` evaluations of the integrand.

    Returns
    -------
    float
        The hadronic cross section differential in the invariant mass using
        the vegas integrator.
    """
    hats = mvh ** 2  # partonic COM energy squared [TeV^2]
    y_min = - 0.5 * np.log(s / hats)  # min rapidity
    y_max = 0.5 * np.log(s / hats)  # max rapidity

    integ = vegas.Integrator([[y_min, y_max]])
    result = integ(lambda x: integrand_VH(x, mvh, cHW, cHWB, cHq3), nitn=nitn, neval=neval)  # estimate the integral
    return result


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


def weight(sqrts, mu, x1, x2):
    """
    NP parameter: order in the EFT
    order parameter: work at one specific order
    """
    hats = sqrts ** 2
    w_ii = (sigma_part_vh(hats, 0, 0, 0)) * (p.xfxQ(2, x1, mu) * p.xfxQ(-2, x2, mu))
    return w_ii

v_weight = np.vectorize(weight, otypes=[np.float])

def dsigma_dmtt_dy(y, mtt):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if mtt == mz + mh: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mtt):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mtt / np.sqrt(s) * np.exp(y)
        x2 = mtt / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mtt / s * v_weight(mtt, 91.188, x1, x2) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0

dsigma_dmtt_dy_vec = np.vectorize(dsigma_dmtt_dy, otypes=[np.float])


def dsigma_dmtt(mvh):
    y_min, y_max = -0.5 * np.log(s / mvh), 0.5 * np.log(s / mvh)
    dsigma_dmtt = integrate.fixed_quad(dsigma_dmtt_dy_vec, y_min, y_max, args=(mvh,), n=10)[0]
    return dsigma_dmtt

#%%
lhe_path = "/Users/jaco/Documents/ML4EFT/data/events/vh_benchmark/uubarzh_smeftsim_sm.lhe"
bin_width = 10 * 10 ** -3
#hist_mg, bins_mg = mg5_reader(lhe_path, bin_width, bin_min=mh + mz)

cross_section_vh_vegas = []
x = np.arange(mz + mh + bin_width / 2, 1.0, bin_width)
cross_section_vh = [dsigma_dmtt(mvh) for mvh in x]


for mvh in x:
    #result_fq = dsigma_dmtt(mvh)
    #cross_section_vh.append(result_fq)
    result_vegas = dsigma_dmvh(mvh, nitn=50)
    cross_section_vh_vegas.append(result_vegas.mean)

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[], xlim=(0.1, 1))

#ax1.step(bins_mg[:-1], hist_mg, c='C0', where='post', label=r'$\rm{mg5}$')
ax1.plot(x, cross_section_vh, '-', c='C1', label=r'$\rm{FormCalc,\;SM,\;fq}$')
ax1.plot(x, cross_section_vh_vegas, linestyle='dashed', c='C0', label=r'$\rm{FormCalc,\;SM,\;vegas}$')
plt.yscale('log')
plt.title(r'$\rm{VH}\;\rm{production}\;\rm{benchmark,}\;\rm{LO+}\mathcal{O}\left(\Lambda^{-4}\right)$')
plt.ylabel(r'$d\sigma/dm_{HZ}\;\mathrm{[pb\:TeV^{-1}]}$')
plt.legend(frameon=False, loc='best')

ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))
#ax2.scatter(x, cross_section_vh/hist_mg[:len(x)], s=10)
ax2.hlines(1, 0.1, 1, colors='k', linestyles='dashed')

plt.ylabel(r'$\rm{num/ana}$')

plt.xlim((0.1, 1))
plt.xlabel(r'$m_{HZ}\;\mathrm{[TeV]}$')
plt.show()

plt.savefig("/Users/jaco/Documents/ML4EFT/plots/uubarzh_smeftsim_quad_cHq3_cHq3.pdf")

