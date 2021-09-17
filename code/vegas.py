#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import vegas
import math
import numpy as np
import lhapdf
import matplotlib.pyplot as plt
from scipy import integrate
#%%
from quad_clas.core import xsec_cluster as xsec
from quad_clas.core.lhelib import lhe as lhe
#%%
p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
s = 14 ** 2 # Collider COM energy squared [TeV^2]
mu = 91.188 # fact. scale for pdfs = Mz
mt = 0.17276 # top quark mass [TeV]
mw = 80.379 * 10 ** -3  # w boson mass [TeV]
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125# h boson mass [TeV]
Gf = 0.0000116637 * 10 ** 6
v = 1 / np.sqrt(Gf * np.sqrt(2))  # vev [TeV]
pb_convert = 3.894E2 # conversion factor to pb
#%%
# ttbar production
def dsigma_dtheta_part(theta, mtt):
    """
    Returns the differential partonic cross section  :math:`d\sigma/d\theta` for top-pair production. The cross section differential in the
    azimuthal angle  :math:`\theta` is obtained by computing

     .. math::

        \frac{d\sigma}{d\Omega} = 2\pi\sin\theta \frac{d\sigma}{d\theta}

    Parameters
    ----------
    theta: float
        azimuthal angle between :math:`0` and :math:`\pi`
    mtt: float
        invariant mass of the outgoing top-pair

    Returns
    -------
    float
        Differential cross section :math:`d\sigma/d\theta` for top-pair production.
    """
    hats = mtt ** 2
    alfa_s = 0.118
    num = alfa_s ** 2 * np.sqrt(1 - 4 * mt ** 2 / hats) * (
                4 * mt ** 2 + hats - 4 * mt ** 2 * np.cos(theta) ** 2 + hats * np.cos(theta) ** 2)
    den = 18 * hats ** 2
    return (num / den) * 2 * np.pi * np.sin(theta)


def integrand(x, mtt):
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
    if mtt <= 2 * mt:
        return 0
    theta = x[0]
    y = x[1]
    hats = mtt ** 2
    x1 = np.sqrt(hats / s) * np.exp(y)
    x2 = np.sqrt(hats / s) * np.exp(-y)
    pdfs = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    return pb_convert * 2 * mtt / s * dsigma_dtheta_part(theta, mtt) * pdfs / (x1 * x2)


def dsigma_dmtt(mtt, nitn=100, neval=1000):
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
    hats = mtt ** 2  # partonic COM energy squared [TeV^2]
    y_min = - 0.5 * np.log(s / hats)  # min rapidity
    y_max = 0.5 * np.log(s / hats)  # max rapidity

    integ = vegas.Integrator([[0, np.pi], [y_min, y_max]])
    result = integ(lambda x: integrand(x, mtt), nitn=nitn, neval=neval)  # estimate the integral
    return result

#%%
def dsigma_dmtt_dblfq(mtt):
    """
    Computes the hadronic cross section differential in the invariant mass.
    It uses the dblquad integration module from scipy.

    Parameters
    ----------
    mtt: float
        Invariant mass of the outgoing top-pair in TeV

    Returns
    -------
    float
        The hadronic cross section differential in the invariant mass
        using the dbl quad integration module form scipy.
    """
    hats = mtt ** 2
    y_min = - 0.5 * np.log(s / hats)  # min rapidity
    y_max = 0.5 * np.log(s / hats)  # max rapidity
    result, _ = integrate.dblquad(lambda theta, y: g([theta, y], mtt=mtt), y_min, y_max, lambda y: 0, lambda y: np.pi)
    return result
#%%
# result =  dsigma_dmtt(0.5)
# print(result.summary())
# print('result = %s    Q = %.2f' % (result, result.Q))
x, y_fq = xsec.crossSection(10 * 10 ** -3, 1.0, 0, 0)
cross_section_vegas = []
cross_section_dblfq = []
for mtt in x:
    result_vegas = dsigma_dmtt(mtt, nitn = 50)
    cross_section_vegas.append(result_vegas.mean)

    result_dblfq = dsigma_dmtt_dblfq(mtt)
    cross_section_dblfq.append(result_dblfq)

    print("Vegas: ", result_vegas.mean, "\t", "Dbl quad: ", result_dblfq)



#%%
def dsigma_dtheta_part_vh(theta, mvh):
    """
    Returns the differential partonic cross section  :math:`d\sigma/d\theta` for VH associated production. The cross section differential in the
    azimuthal angle  :math:`\theta` is obtained by computing

     .. math::

        \frac{d\sigma}{d\Omega} = 2\pi\sin\theta \frac{d\sigma}{d\theta}

    Parameters
    ----------
    theta: float
        azimuthal angle between :math:`0` and :math:`\pi`
    mtt: float
        invariant mass of the outgoing vh

    Returns
    -------
    float
        Differential cross section :math:`d\sigma/d\theta` for VH associated production.
    """
    hats = mvh ** 2


    cth = mw / mz
    sth = np.sqrt(1 - (mw / mz) ** 2)
    alfa_w = 1 / 132.507#0.118 / sth ** 2
    pi = np.sqrt(hats) / 2
    pf = np.sqrt(mh ** 4 - 2 * mh ** 2 * (mz ** 2 + hats) + (mz ** 2 - hats) ** 2) / (2*np.sqrt(hats))
    Ea = pi
    Ez = np.sqrt(mz ** 2 + pf ** 2)
    Eh = np.sqrt(mh ** 2 + pf ** 2)
    T = mz ** 2 - 2 * (Ea * Ez - pi * pf * np.cos(theta))
    U = mh ** 2 - 2 * (Ea * Eh - pi * pf * np.cos(theta))

    #SM = (np.pi ** 2 * alfa_w ** 2 * mw ** 2 * (8 * sth ** 2 * (4 * sth ** 2 - 3) + 9) * (mz ** 4 + mz ** 2 * (hats - T - U) + T * U))/(27 * cth ** 6 * mz ** 2 * sth ** 4 * (mz ** 2 - hats) ** 2)

    SM = (4 * np.pi * alfa_w) ** 2 * mz ** 2 / (4 * cth ** 2) * (1 / (hats - mz ** 2) ** 2) * (
                1 / 4 - 2 / 3 * sth ** 2 + 8 / 9 * sth ** 4) * (T * U / mz ** 2 - U - T + hats + mz ** 2)

    #SM = (2 * np.pi * alfa_w ** 2 * mw ** 2 * (32 * sth ** 2 - 24 * sth ** 2 + 9) * (mz ** 4 + mz ** 2 * (hats-T-U) + T * U))/(27 * cth ** 6 * mz ** 2 * sth ** 4 * (mz ** 2 - hats)**2)
    # SM = (np.pi ** 3 * alfa_s ** 3 * (32 * sth ** 4 - 24 * sth ** 2 + 9) * v ** 2 * (
    #             mz ** 4 + mz ** 2 * (hats - T - U) + T * U)) / (
    #             27 * cth ** 6 * mz ** 2 * sth ** 6 * (mz ** 2 - hats) ** 2)
    prefac = 1 / (64 * np.pi ** 2 * hats) * (pf / pi)

    return prefac * SM

def integrand_VH(x, mvh):
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
    theta = x[0]
    y = x[1]
    hats = mvh ** 2
    x1 = np.sqrt(hats / s) * np.exp(y)
    x2 = np.sqrt(hats / s) * np.exp(-y)
    pdfs = p.xfxQ(2, x1, mu) * p.xfxQ(-2, x2, mu)
    #pdfs = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    return pb_convert * 2 * mvh / s * dsigma_dtheta_part_vh(theta, mvh) * pdfs / (x1 * x2)


def dsigma_dmvh(mvh, nitn=100, neval=1000):
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

    integ = vegas.Integrator([[0, np.pi], [y_min, y_max]])
    result = integ(lambda x: integrand_VH(x, mvh), nitn=nitn, neval=neval)  # estimate the integral
    return result

#%%
cross_section_vh_vegas = []
x = np.linspace(mz + mh, 1, 100)
for mvh in x:
    result_vegas = dsigma_dmvh(mvh, nitn = 50)
    print(result_vegas)
    cross_section_vh_vegas.append(result_vegas.mean)


#%%
plt.plot(x, cross_section_vh_vegas, label='vegas')
#plt.plot(x, y_fq, label='fixed quad')
plt.legend()
plt.yscale('log')
plt.show()

#%%
#madgraph
import pylhe
path_to_file = '/Users/jaco/Documents/ML4EFT/code/unweighted_events.lhe'
data_madgraph = []
found_weight = False
for e in pylhe.readLHE(path_to_file):
    data_madgraph.append(lhe.invariant_mass(e.particles[-1], e.particles[-2]) * 10 ** -3)
    if found_weight == False:
        weight = e.eventinfo.weight
        found_weight = True
hist_mg, bins_mg = np.histogram(data_madgraph, bins=np.arange(mh + mz, np.max(data_madgraph), 10 * 10 ** -3),
                                    density=True)
hist_mg *= weight

#%%
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[], xlim=(0.1, 1))
ax1.plot(x, cross_section_vh_vegas, '-', c='red', label=r'$\rm{FormCalc}$')
#ax1.plot(x, cross_section_vh_vegas_ellis, '-', c='C2', label=r'$\rm{Ellis}$')
ax1.step(bins_mg[:-1], hist_mg, where='post', label=r'$\rm{mg5}$')

plt.yscale('log')
plt.ylabel(r'$d\sigma/dm_{HZ}\;\mathrm{[pb\:TeV^{-1}]}$')
plt.legend(frameon=False, loc='best')

ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))
#ax2.scatter(x, hist_mg[:len(x)] / y_sm, s=10)
ax2.hlines(1, 0.1, 1, colors='k', linestyles='dashed')

plt.ylabel(r'$\rm{num/ana}$')
plt.xlim((0.1, 1))

# ax3 = fig.add_axes([0.15, 0.1, 0.75, 0.20], ylim = (0.8*(y/y_sm).min(), 1.1*(y/y_sm).max()))
# ax3.plot(x, y/y_sm, '-')

plt.xlabel(r'$m_{HZ}\;\mathrm{[TeV]}$')

plt.show()

#%%
def sigma_part_vh_ellis(hats):
    pz2 = (hats ** 2 + mw ** 4 + mh ** 4 - 2 * hats * mw ** 2 - 2 * hats * mh ** 2 - 2 * mw ** 2 * mh ** 2)
    pz = np.sqrt(pz2)
    sth2 = 1 - (mw / mz) ** 2
    Vq = 1 / 2 - 4 / 3 * sth2
    Aq = 1/ 2
    xsec = (Gf * mz ** 2) ** 2 / (9 * np.pi) * (Vq ** 2 + Aq ** 2) * pz / np.sqrt(hats) * (3 * mz ** 2 + pz2)/((hats - mz ** 2) ** 2)
    return xsec

def integrand_VH_ellis(x, mvh):
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
    return pb_convert * 2 * mvh / s * sigma_part_vh_ellis(mvh ** 2) * pdfs / (x1 * x2)

def dsigma_dmvh_ellis(mvh, nitn=100, neval=1000):
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
    result = integ(lambda x: integrand_VH_ellis(x, mvh), nitn=nitn, neval=neval)  # estimate the integral
    return result

#%%
cross_section_vh_vegas_ellis = []
x = np.linspace(mz + mh, 1, 100)
for mvh in x:
    result_vegas = dsigma_dmvh_ellis(mvh, nitn = 50)
    print(result_vegas)
    cross_section_vh_vegas_ellis.append(result_vegas.mean)


#%%
plt.plot(x, cross_section_vh_vegas_ellis, label='vegas')
#plt.plot(x, y_fq, label='fixed quad')
plt.legend()
plt.yscale('log')
plt.show()