#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %%
import vegas
import math
import numpy as np
import lhapdf
import matplotlib.pyplot as plt
#%%
from quad_clas.core import xsec_cluster as xsec
#%%
p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
s = 14 ** 2 # Collider COM energy squared [TeV^2]
mu = 91.188 # fact. scale for pdfs = Mz
mt = 0.172 # top quark mass [TeV]
pb_convert = 3.894E2 # conversion factor to pb

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
    num = 8 * alfa_s ** 2 * np.sqrt(1 - 4 * mt ** 2 / hats) * (
                4 * mt ** 2 + hats - 4 * mt ** 2 * np.cos(theta) ** 2 + hats * np.cos(theta) ** 2)
    den = 18 * hats ** 2
    return (num / den) * 2 * np.pi * np.sin(theta)


def g(x, mtt):
    if mtt <= 2 * mt:
        return 0
    theta = x[0]
    y = x[1]
    hats = mtt ** 2
    x1 = np.sqrt(hats / s) * np.exp(y)
    x2 = np.sqrt(hats / s) * np.exp(-y)
    pdfs = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    return pb_convert * 2 * mtt / s * dsigma_dtheta_part(theta, mtt) * pdfs


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
    """
    hats = mtt ** 2  # partonic COM energy squared [TeV^2]
    y_min = - 0.5 * np.log(s / hats)  # min rapidity
    y_max = 0.5 * np.log(s / hats)  # max rapidity

    integ = vegas.Integrator([[0, np.pi], [y_min, y_max]])
    result = integ(lambda x: g(x, mtt), nitn=nitn, neval=neval)  # estimate the integral
    return result
#%%
# result =  dsigma_dmtt(0.5)
# print(result.summary())
# print('result = %s    Q = %.2f' % (result, result.Q))

x = np.linspace(0.3, 1.0, 10)
cross_section = []
for mtt in x:
    result = dsigma_dmtt(mtt)
    print(result.mean)
    cross_section.append(result.mean)


#%%

def f(x):
    dx2 = 0
    for d in range(4):
        dx2 += (x[d] - 0.5) ** 2
    return math.exp(-dx2 * 100.) * 1013.2118364296088

integ = vegas.Integrator([[-1, 1], [0, 1], [0, 1], [0, 1]])

result = integ(f, nitn=10, neval=1000)
print(result.summary())
print('result = %s    Q = %.2f' % (result, result.Q))

# %%
def f_sph(x):
    dx2 = 0
    for d in range(4):
        dx2 += (x[d] - 0.5) ** 2
    if dx2 < 0.2 ** 2:
        return math.exp(-dx2 * 100.) * 1115.3539360527281318
    else:
        return 0.0

integ = vegas.Integrator([[-1, 1], [0, 1], [0, 1], [0, 1]])

integ(f_sph, nitn=100, neval=1000)           # adapt the grid
result = integ(f_sph, nitn=100, neval=1000)  # estimate the integral
print(result.summary())
print('result = %s    Q = %.2f' % (result, result.Q))

# %%

def gauss(x):
    return 1/(np.sqrt(2*np.pi))*np.exp(-x**2/2)

integ = vegas.Integrator([[-1, 1]])
integ(gauss, nitn=10, neval=1000)           # adapt the grid
result = integ(gauss, nitn=10, neval=1000)  # estimate the integral
print(result.summary())
print('result = %s    Q = %.2f' % (result, result.Q))