from __future__ import division
#import lhapdf
import lhapdf
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
from scipy import integrate
import csv
from scipy.optimize import minimize
from scipy import optimize
import matplotlib.patches as patches
import matplotlib.colors
import sys

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
mt = 173.3 #Top quark mass in GeV
s = (13*10**3)**2#GeV^2
v = 125
asQCD = 0.118
cSMEFT = 100*10**(-6)

def partonicCrossGluon_dtheta(sqrts, theta):
    def disgmadt(sqrts, t):
        s = sqrts**2
        u = 2*mt**2 -t-s
        Mss = (4/s**2)*(t-mt**2)*(u-mt**2)
        Mtt = 2/((t-mt**2)**2)*((t-mt**2)*(u-mt**2)-2*mt**2*(u+mt**2))
        Mtu = 4*mt**2/((t-mt**2)*(u-mt**2))*(s-4*mt**2)
        Mst = 4/(s*(t-mt**2))*(mt**4-t*(s+t))
        Muu = 2/((u-mt**2)**2)*((u-mt**2)*(t-mt**2)-2*mt**2*(t+mt**2))
        Msu = 4/(s*(u-mt**2))*(mt**4-u*(s+u))
        dsigmadt = 0.3894*(10**9)*(np.pi*asQCD**2)/(64*s**2)*(12*Mss +16/3*(Mtt+Muu)-(2/3)*Mtu+6*(Mst + Msu))
        return dsigmadt

    t = mt**2 - 2*(sqrts/2)**2-2*(sqrts/2)*np.sqrt((sqrts/2)**2-mt**2)*np.cos(theta)

    dtdtheta = sqrts*np.sqrt((sqrts/2)**2-mt**2)*np.sin(theta)
    dsigmadtheta = disgmadt(sqrts, t)*dtdtheta
    return dsigmadtheta

def diffCrossHadronicSMGluon(sqrts):
    sP = sqrts**2
    def integrand(y, theta):
        result = []
        for yi in y:
            value = (s/sP)*(p.xfxQ(21, np.sqrt(sP/s)*np.exp(yi), renScale(theta, sqrts))*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-yi), renScale(theta, sqrts)))*partonicCrossGluon_dtheta(sqrts, theta)
            result.append(value)
        return np.array(result)
    #factor 2*np.sqrt(sP) comes from the chain rule
    def fint_fixed_quad(theta):
        result = []
        for thetai in theta:
            value = integrate.fixed_quad(integrand, -0.5*np.log(s/sP), 0.5*np.log(s/sP), args=(thetai,), n = 15)[0]
            result.append(value)
        return result

    res_fixed_quad = integrate.fixed_quad(lambda theta: fint_fixed_quad(theta), 0, np.pi, n = 15)[0]
    diffCrossSM = (2*np.sqrt(sP)/s)*res_fixed_quad
    return diffCrossSM

def diffCrossHadronicSMQuark(sqrts):
    sP = sqrts**2
    integrand = lambda y, theta:(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(5, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-5, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts)))*(2*np.pi)*np.sin(theta)*(2/9)*((asQCD**2)/(4*sP))*np.sqrt(1-4*mt**2/sP)*(1+4*mt**2/sP+(1-4*mt**2/sP)*(np.cos(theta)**2))
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossSM = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossSM

def renScale(theta, sqrts):
    sP = sqrts**2
    p_T = np.sqrt((sP/4)-mt**2)*np.sin(theta)
    H_T = 2*(np.sqrt(mt**2+p_T**2))
    return (H_T/4)**2

def diffCrossSM(sqrts):
    if sqrts >= 2*mt:
        return diffCrossHadronicSMQuark(sqrts)+ diffCrossHadronicSMGluon(sqrts)
    else:
        return 0

def diffCrossBSM(sqrts):
    """Continuous version"""
    sP = sqrts**2
    partonicCross = (45/(128*np.sqrt(2)))*(v*mt/sP)*(4*asQCD/np.sqrt(np.pi))**(3/2)*np.sqrt(1-4*mt**2/sP)*np.real(cSMEFT)
    integrand = lambda y: (s/sP)*(p.xfxQ(21, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-y), sP))
    diffCrossBSM = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*partonicCross*integrate.quad(integrand, -0.5*np.log(s/sP), 0.5*np.log(s/sP))[0]
    return diffCrossBSM

def generateData():
    crossSection = []
    crossSectionBSM = []
    x = np.arange(2*mt, 2500, 10)
    for i in x:
        print(i)
        crossSection.append(diffCrossHadronicSMGluon(i)+diffCrossHadronicSMQuark(i))
        crossSectionBSM.append(diffCrossBSM(i))
    crossSection = np.array(crossSection)
    crossSectionBSM = np.array(crossSectionBSM)
    plot(x, crossSection, crossSectionBSM)

def plot(x, crossSection, crossSectionBSM):
    fig = plt.figure(figsize=(8.2,5))
    grid = plt.GridSpec(4,1)
    plt.subplot(grid[:3,:])

    plt.plot(x, crossSection, label='SM')
    plt.plot(x, crossSectionBSM+crossSection, label='EFT')
    plt.ylabel(r'$d\sigma/d\sqrt{\^{s}}\;\mathrm{[pb\:GeV^{-1}]}$')
    plt.xlim((0, 2500))
    plt.title('SM versus EFT with OtG')
    plt.yscale('log')
    plt.legend()

    plt.subplot(grid[-1,:])

    plt.plot(x, (crossSectionBSM+crossSection)/crossSection)
    plt.ylim((-3, 2.8))
    plt.xlim((0, 2500))
    plt.axhline(y=0, color='k', linestyle ='--', linewidth = 0.5)
    plt.ylabel('BSM/SM')
    plt.subplots_adjust(hspace = 0.5)

    plt.xlabel(r'$\sqrt{\^{s}}\;\mathrm{[GeV]}$')
    plt.show()

generateData()
