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

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
mt = 172 #Top quark mass in GeV
s = (13*10**3)**2#GeV^2
Gf = 0.0000116637
v = 1/np.sqrt(Gf*np.sqrt(2))
print(v)
asQCD = 0.1184
cSMEFT = 1
LambdaSMEFT = 10**3

def partonicCrossGluon_dtheta(sqrts, theta):
    def dsigmadt(sqrts, t):
        s = sqrts**2
        u = 2*mt**2 -t-s
        Mss = (4/s**2)*(t-mt**2)*(u-mt**2)
        Mtt = 2/((t-mt**2)**2)*((t-mt**2)*(u-mt**2)-2*mt**2*(u+mt**2))
        Mtu = (4*mt**2/((t-mt**2)*(u-mt**2)))*(s-4*mt**2)
        Mst = 4/(s*(t-mt**2))*(mt**4-t*(s+t))
        Muu = 2/((u-mt**2)**2)*((u-mt**2)*(t-mt**2)-2*mt**2*(t+mt**2))
        Msu = 4/(s*(u-mt**2))*(mt**4-u*(s+u))
        dsigmadt = 0.3894*(10**9)*(np.pi*asQCD**2)/(64*s**2)*(12*Mss +16/3*(Mtt+Muu)-(2/3)*Mtu+6*(Mst + Msu))
        return dsigmadt

    t = mt**2 - 2*(sqrts/2)**2-2*(sqrts/2)*np.sqrt((sqrts/2)**2-mt**2)*np.cos(theta)
    #print("Value of t: ", t)
    dtdtheta = sqrts*np.sqrt((sqrts/2)**2-mt**2)*np.sin(theta)
    dsigmadtheta = dsigmadt(sqrts, t)*dtdtheta
    return dsigmadtheta

theta = np.linspace(0, np.pi, 100)

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
                +p.xfxQ(5, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-5, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts)))*asQCD**2*np.sqrt(1-4*mt**2/s)*(-4*np.cos(theta)**2*mt**2+4*mt**2+s*np.cos(theta)**2+s)/(18*s**2)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossSM = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossSM

def renScale(theta, sqrts):
    sP = sqrts**2
    p_T = np.sqrt((sP/4)-mt**2)*np.sin(theta)
    m_T = np.sqrt(sP/2-p_T**2)
    H_T = 2*(np.sqrt(mt**2+p_T**2))
    return (H_T/2)


def diffCrossSM(sqrts):
    if sqrts >= 2*mt:
        return diffCrossHadronicSMQuark(sqrts)+ diffCrossHadronicSMGluon(sqrts)
    else:
        return 0

def partonicCrossGluonBSM_dtheta(sqrts, theta):
    s = sqrts**2
    gs = np.sqrt(4*np.pi*asQCD)
    num = -cSMEFT*v*mt*asQCD**(3/2)*np.sqrt(1-4*mt**2/s)*(-36*np.cos(theta)**2*mt**2 + 9*s*np.cos(theta)**2+7*s)
    den = 24*np.sqrt(2*np.pi)*LambdaSMEFT**2*s**2*(np.cos(theta)*np.sqrt(1-4*mt**2/s)-1)*(np.cos(theta)*np.sqrt(1-4*mt**2/s)+1)
    dsigmadtheta = 2*np.pi*np.sin(theta)*(num/den)
    return dsigmadtheta

def diffCrossHadronicBSMGluon(sqrts):
    sP = sqrts**2
    def integrand(y, theta):
        result = []
        for yi in y:
            value = (s/sP)*(p.xfxQ(21, np.sqrt(sP/s)*np.exp(yi), renScale(theta, sqrts))*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-yi), renScale(theta, sqrts)))*partonicCrossGluonBSM_dtheta(sqrts, theta)
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
    diffCrossSM = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*res_fixed_quad
    return diffCrossSM

def diffCrossHadronicBSMQuark(sqrts):
    sP = sqrts**2
    gs = np.sqrt(4*np.pi*asQCD)
    integrand = lambda y, theta:(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(5, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-5, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts)))*(2*np.sqrt(2/np.pi)*cSMEFT*v*mt*asQCD**(3/2)*np.sqrt(1-4*mt**2/s))/(9*LambdaSMEFT**2*s)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossBSM = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossBSM


def diffCrossBSM(sqrts):
    """Continuous version"""
    if sqrts >= 2*mt:
        return diffCrossHadronicBSMGluon(sqrts)#+diffCrossHadronicBSMQuark(sqrts)
    else:
        return 0

def invariant_mass(p1,p2):
    return np.sqrt(sum((1 if mu=='e' else -1)*(getattr(p1,mu)+getattr(p2,mu))**2 for mu in ['e','px','py','pz']))


def generateData():
    crossSection = []
    crossSectionBSM = []
    x = np.arange(2*mt, 2500, 10)
    for i in x:
        print(i)
        #crossSection.append(diffCrossSM(i))
        crossSectionBSM.append(diffCrossBSM(i))
    #crossSection = np.array(crossSection)
    crossSectionBSM = np.array(crossSectionBSM)
    #xsecSM = integrate.quad(lambda x: diffCrossSM(x), 2*mt, 4000)[0]
    xsecBSM = integrate.quad(lambda x: diffCrossBSM(x), 2*mt, 5000)[0]
    #print("xsec SM: ", xsecSM)
    print("xsec BSM: ", xsecBSM)
    plot(x, crossSection, crossSectionBSM)

def plot(x, crossSection, crossSectionBSM):

    data_sm = []
    data_eft = []
    for e in pylhe.readLHE('lhe_events/unweighted_events_sm.lhe'):
        data_sm.append(invariant_mass(e.particles[-1],e.particles[-2]))
    for e in pylhe.readLHE('lhe_events/unweighted_events_eft_ggtt.lhe'):
        data_eft.append(invariant_mass(e.particles[-1],e.particles[-2]))

    binWidth = 20

    hist_sm, bins_sm = np.histogram(data_sm,bins=np.arange(2*mt,np.max(data_sm),binWidth), density=True)
    hist_eft, bins_eft = np.histogram(data_eft, bins=np.arange(2*mt,np.max(data_eft),binWidth), density=True)

    hist_sm *= 459.4
    hist_eft *= 110.5
    #check area
    #20*np.sum(hist_sm)

    #plt.plot(x, crossSection, label=r'$\mathrm{SM}^2\;\mathrm{(ana)}$')
    #plt.plot(x, crossSectionBSM+crossSection, '--', label=r'$\mathrm{SM}^2+\mathrm{SM}\times \mathrm{BSM\;\mathrm{(ana)}}$')
    plt.plot(x, crossSectionBSM, '--', label=r'$\mathrm{SM}^2+\mathrm{SM}\times \mathrm{BSM\;\mathrm{(ana)}}$')

    #plot_sm, = plt.plot(bins_sm[:-1]+binWidth/2, hist_sm, label = r'$\mathrm{SM}^2$')
    #plot_sm.set_drawstyle('steps')

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
