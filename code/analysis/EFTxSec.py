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
import pylhe

p = lhapdf.mkPDF("NNPDF23_lo_as_0130_qed", 0)
mt = 173.3 #Top quark mass in GeV
s = (13*10**3)**2#GeV^2
v = 125
asQCD = 0.130
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
    m_T = np.sqrt(sP/2-p_T**2)
    H_T = 2*(np.sqrt(mt**2+p_T**2))
    #return (H_T/4)**2
    return m_T

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

def invariant_mass(p1,p2):
    return np.sqrt(sum((1 if mu=='e' else -1)*(getattr(p1,mu)+getattr(p2,mu))**2 for mu in ['e','px','py','pz']))


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

    data_sm = []
    data_eft = []
    for e in pylhe.readLHE('unweighted_events_sm.lhe'):
        data_sm.append(invariant_mass(e.particles[-1],e.particles[-2]))
    for e in pylhe.readLHE('unweighted_events_eft_ctG.lhe'):
        data_eft.append(invariant_mass(e.particles[-1],e.particles[-2]))

    binWidth = 20

    hist_sm, bins_sm = np.histogram(data_sm,bins=np.arange(2*mt,np.max(data_sm),binWidth), density=True)
    hist_eft, bins_eft = np.histogram(data_eft, bins=np.arange(2*mt,np.max(data_eft),binWidth), density=True)

    hist_sm *= 518.4
    hist_eft *= 658.6
    #check area
    #20*np.sum(hist_sm)

    plt.plot(x, crossSection, label=r'$\mathrm{SM}^2\;\mathrm{(ana)}$')
    plt.plot(x, crossSectionBSM+crossSection, label=r'$\mathrm{SM}^2+\mathrm{SM}\times \mathrm{BSM\;\mathrm{(ana)}}$')

    plot_sm, = plt.plot(bins_sm[:-1]+binWidth/2, hist_sm, label = r'$\mathrm{SM}^2$')
    plot_sm.set_drawstyle('steps')

    plot_eft, = plt.plot(bins_eft[:-1]+binWidth/2, hist_eft, label = r'$\mathrm{SM}^2+\mathrm{SM}\times \mathrm{BSM}$')
    plot_eft.set_drawstyle('steps')

    plt.xlabel(r'$m_{tt}$')
    plt.ylabel(r'$d\sigma/dm_{tt}\;\mathrm{[pb\:GeV^{-1}]}$')
    plt.xlim((2*mt, 1000))
    #plt.xticks(np.arange(2*mt, 1000, step=20), labels = None)
    #ax.text(2, 6, 'test',horizontalalignment='center',verticalalignment='center')
    plt.title('SM versus EFT with ctG'+r'$=1$')
    plt.yscale('log')
    plt.legend()
    plt.show()

generateData()
