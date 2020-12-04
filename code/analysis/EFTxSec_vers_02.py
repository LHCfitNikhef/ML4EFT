from __future__ import division
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
asQCD = 0.1184
LambdaSMEFT = 10**3

#Partonic cross sections

#SM
def dsigmadThetaqqSM(sqrts, theta):
    sP = sqrts**2
    g = np.sqrt(4*np.pi*asQCD)
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    Me2 = 4*g**4*(-4*u*mt**2+6*mt**4-4*t*mt**2+t**2+u**2)/(9*sP**2)
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

# def sigma_part_qq(sqrts, cSMEFT):
#     hats = sqrts**2
#     num = np.sqrt(1-4*mt**2/hats)*(cSMEFT*8*np.sqrt(2*np.pi)*hats*v*mt*asQCD**(3/2)+np.pi*LambdaSMEFT**2*asQCD**2*(4*mt**2+3*hats))
#     den = 36*LambdaSMEFT**2*hats**2
#     return num/den
def sigma_part_gg(sqrts, cSMEFT):#correct
    hats = sqrts**2
    num = asQCD**(3/2)*(np.sqrt(2*np.pi)*cSMEFT*hats*v*mt*(16*hats*np.arctanh(np.sqrt(1-4*mt**2/hats))-9*np.sqrt(hats*(hats-4*mt**2)))+8*np.pi*LambdaSMEFT**2*np.sqrt(asQCD)*(4*hats*mt**2+mt**4+hats**2)*np.arctanh(np.sqrt(1-4*mt**2/hats))-31*np.pi*LambdaSMEFT**2*mt**2*np.sqrt(hats*asQCD*(hats-4*mt**2))-7*np.pi*LambdaSMEFT**2*hats*np.sqrt(hats*asQCD*(hats-4*mt**2)))
    den = 12*LambdaSMEFT**2*hats**3
    return num/den

def sigma_part_qq(sqrts, cSMEFT):#correct
    hats = sqrts**2
    num = 8*asQCD**(3/2)*np.sqrt(1-4*mt**2/hats)*(3*np.sqrt(2*np.pi)*cSMEFT*hats*v*mt+np.pi*LambdaSMEFT**2*np.sqrt(asQCD)*(2*mt**2+hats))
    den = 27*LambdaSMEFT**2*hats**2
    return num/den


    
def dsigmadThetaggSM(sqrts, theta):
    sP = sqrts**2
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    g = np.sqrt(4*np.pi*asQCD)
    num = g**4*(-mt**4*(3*t**2+14*t*u+3*u**2)+mt**2*(7*t**2*u+t**3+7*t*u**2+u**3)+6*mt**8-t*u*(t**2+u**2))*(18*mt**2*(t+u)-18*mt**4+sP**2-9*(t**2+u**2))
    den = 48*sP**2*(t-mt**2)**2*(u-mt**2)**2
    Me2 = num/den
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

#EFT
def dsigmadThetaqqEFT(sqrts, theta, cSMEFT):
    sP = sqrts**2
    g = np.sqrt(4*np.pi*asQCD)
    Me2 = cSMEFT*(16*np.sqrt(2)*g**3*v*mt)/(9*LambdaSMEFT**2)
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

def dsigmadThetaggEFT(sqrts, theta, cSMEFT):
    sP = sqrts**2
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    g = np.sqrt(4*np.pi*asQCD)
    Me2 = (cSMEFT*g**3*v*mt*(-18*mt**2*(t+u)+18*mt**4-sP**2+9*(t**2+u**2)))/(6*np.sqrt(2)*LambdaSMEFT**2*(mt**2-t)*(mt**2-u))
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

#print("python: ", integrate.quad(lambda theta: dsigmadThetaggSM(400, theta) + dsigmadThetaggEFT(400, theta, 1), 0, np.pi)[0])
#print("math: ", sigma_part_gg(400, 1))

#Hadronic cross sections

#SM
def diffCrossHadronicSMQuark(sqrts):
    sP = sqrts**2
    integrand = lambda y, theta:(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts)))*dsigmadThetaqqSM(sqrts, theta)+(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts))+p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts))+p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts))+p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts)))*dsigmadThetaqqSM(sqrts, np.pi-theta)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossBSMqq = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossBSMqq

def diffCrossHadronicSMGluon(sqrts):
    sP = sqrts**2
    integrand = lambda y, theta:(s/sP)*p.xfxQ(21, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))*dsigmadThetaggSM(sqrts, theta)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossBSMgg = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossBSMgg

#BSM
def diffCrossHadronicBSMQuark(sqrts, cSMEFT):
    sP = sqrts**2
    integrand = lambda y, theta:(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts)))*dsigmadThetaqqEFT(sqrts, theta, cSMEFT)+(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts))+p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts))+p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts))+p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(np.pi-theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(np.pi-theta, sqrts)))*dsigmadThetaqqEFT(sqrts, np.pi-theta,cSMEFT)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossBSMqq = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossBSMqq

def diffCrossHadronicBSMGluon(sqrts, cSMEFT):
    sP = sqrts**2
    integrand = lambda y, theta:(s/sP)*p.xfxQ(21, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))*dsigmadThetaggEFT(sqrts, theta, cSMEFT)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossBSMgg = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossBSMgg


def renScale(theta, sqrts):
    sP = sqrts**2
    p_T = np.sqrt((sP/4)-mt**2)*np.sin(theta)
    m_T = np.sqrt(sP/4-p_T**2)
    H_T = 2*(np.sqrt(mt**2+p_T**2))
    #return (H_T/4)
    return 91.188    

def diffCrossSM(sqrts):
    if sqrts >= 2*mt:
        return diffCrossHadronicSMQuark(sqrts)+ diffCrossHadronicSMGluon(sqrts)
    else:
        return 0

def diffCrossBSM(sqrts, cSMEFT):
    """Continuous version"""
    if sqrts >= 2*mt:
        return diffCrossHadronicBSMQuark(sqrts, cSMEFT)+diffCrossHadronicBSMGluon(sqrts, cSMEFT)
    else:
        return 0

def invariant_mass(p1,p2):
    return np.sqrt(sum((1 if mu=='e' else -1)*(getattr(p1,mu)+getattr(p2,mu))**2 for mu in ['e','px','py','pz']))

def rapidity(p1, p2): 
    #Follow P&S page 565
    q0 = getattr(p1, 'e') + getattr(p2, 'e') #energy of the top quark pair in the pp COM frame
    q3 = getattr(p1, 'pz') + getattr(p2, 'pz')
    y = 0.5*np.log((q0 + q3)/(q0-q3))
    return y    


def generateData(binWidth, mtt_max, cSMEFT):
    crossSection = []
    crossSectionBSM = []
    cnt = 0
    shat = np.arange(2*mt+binWidth/2, mtt_max, binWidth)
    for shat_i in shat:
        sys.stdout.write("progress: %d%%   \r" % (cnt*100./(len(shat))) )
        sys.stdout.flush() 
        crossSection.append(diffCrossSM(shat_i))
        crossSectionBSM.append(diffCrossBSM(shat_i, cSMEFT))
        cnt += 1
    crossSection = np.array(crossSection)
    crossSectionBSM = np.array(crossSectionBSM)
    return shat, crossSection, crossSectionBSM
    #plot(shat, crossSection, crossSectionBSM)

def plotData(binWidth, mtt_max, cSMEFT):
    x, crossSection, crossSectionBSM = generateData(binWidth, mtt_max, cSMEFT)

    data_sm = []
    data_eft_smint = []
    data_eft_int = []
    
    # for e in pylhe.readLHE('lhe_events/SM_10E6.lhe'):
    #     data_sm.append(invariant_mass(e.particles[-1],e.particles[-2]))
    for e in pylhe.readLHE('lhe_events/NHO_10E6.lhe'):
        data_eft_smint.append(invariant_mass(e.particles[-1],e.particles[-2]))
    # for e in pylhe.readLHE('lhe_events/INT_10E6.lhe'):
    #     data_eft_int.append(invariant_mass(e.particles[-1],e.particles[-2]))    


    #hist_sm, bins_sm = np.histogram(data_sm,bins=np.arange(2*mt,np.max(data_sm),binWidth), density=True)
    hist_eft_smint, bins_eft_smint = np.histogram(data_eft_smint, bins=np.arange(2*mt,np.max(data_eft_smint),binWidth), density=True)
    #hist_eft_int, bins_eft_int = np.histogram(data_eft_int, bins=np.arange(2*mt,np.max(data_eft_int),binWidth), density=True)
   
    #hist_sm *= 590.424998#only sm
    hist_eft_smint *= 792.776627#smeft up to lambdaˆ-2 107.244201 (quark only)
    #hist_eft_int *=155.8959861#only interference term
    
    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.35, 0.75, 0.55], xticklabels=[], xlim=(2*mt, 1000), ylim = (10**-2, 6))
    
    #plt.plot(x, crossSection, '--', label=r'$\mathrm{SM}^2\;\mathrm{(ana)}$')
    ax1.plot(x, crossSectionBSM + crossSection, '--' , label=r'$\mathrm{SM}^2+\mathrm{SM}\times \mathrm{BSM\;\mathrm{(ana)}}$')
    #plt.plot(x, crossSectionBSM, '--', label=r'$\mathrm{SM}\times \mathrm{BSM\;\mathrm{(ana)}}$')
   
    #plot_sm, = plt.plot(bins_sm[:-1], hist_sm, label = r'$\mathrm{SM}^2$')
    #plot_sm.set_drawstyle('steps')

    ax1.step(bins_eft_smint[:-1], hist_eft_smint, where ='post', label = r'$\mathrm{SM}^2+\mathrm{SM}\times \mathrm{BSM}$')
    plt.title('Analytic SMEFT versus MadGraph with ctG'+r'$=1$')

    plt.yscale('log')
    plt.ylabel(r'$d\sigma/dm_{tt}\;\mathrm{[pb\:GeV^{-1}]}$')
    plt.legend()

    ax2 = fig.add_axes([0.1, 0.1, 0.75, 0.2], ylim = (0.9, 1.1) )
    ax2.scatter(x, hist_eft_smint[:len(x)]/(crossSectionBSM+crossSection), s = 10)
    ax2.hlines(1, 2*mt, 1000, colors='k', linestyles ='dashed')

    # plot_eft_int, = plt.plot(bins_eft_int[:-1], hist_eft_int, label = r'$\mathrm{SM}\times \mathrm{BSM}$')
    # plot_eft_int.set_drawstyle('steps')

    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('num/ana ratio')
    plt.xlim((2*mt, 1000))
    
    plt.show()

def doubleDiffxSecgg(sqrts, y, cSMEFT):
    sP = sqrts**2
    if (np.abs(y) < 0.5*np.log(s/sP)):
        dsigmadmttdY = 0.3894*(10**9)*(2*sqrts/s)*integrate.quad(lambda theta: (s/sP)*(dsigmadThetaggEFT(sqrts, theta,cSMEFT) + dsigmadThetaggSM(sqrts, theta))*(p.xfxQ(21, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))), 0, np.pi)[0]
        return dsigmadmttdY
    else:
        return 0

def doubleDiffxSecqq(sqrts, y, cSMEFT):
    sP = sqrts**2
    if (np.abs(y) < 0.5*np.log(s/sP)):
        dsigmadmttdY = 0.3894*(10**9)*(2*sqrts/s)*integrate.quad(lambda theta: (s/sP)*(dsigmadThetaqqEFT(sqrts, theta, cSMEFT) + dsigmadThetaqqSM(sqrts, theta))*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                    +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                    +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                    +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                    +p.xfxQ(5, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-5, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))), 0, np.pi)[0]
        return dsigmadmttdY
    else:
        return 0


    # sP = sqrts**2
    # sigmaPartqq = integrate.quad(lambda theta: dsigmadThetaqqEFT(sqrts, theta, cSMEFT) + dsigmadThetaqqSM(sqrts, theta), 0, np.pi)[0]
    # if (np.abs(y) < 0.5*np.log(s/sP)):
    #     dsigmadmttdY = 0.3894*(10**9)*(2*sqrts/s)*sigmaPartqq*(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), sP)
    #                 +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), sP)
    #                 +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), sP)
    #                 +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), sP)
    #                 +p.xfxQ(5, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-5, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts)))
    #     return dsigmadmttdY
    # else:
    #     return 0


def plot2Ddist(coeffs, xSec):
    vdoubleDiffxSecgg = np.vectorize(doubleDiffxSecgg)
    vdoubleDiffxSecqq = np.vectorize(doubleDiffxSecqq)
    npar = len(coeffs)
    gs = int(np.sqrt(npar))+1
    nrows, ncols = gs, gs
    plt.figure(figsize=(nrows*4, ncols*3))
    cnt=1
    for i in range(npar):
        print(i)
        ax = plt.subplot(ncols, nrows, cnt)
        ax.set_ylabel(r'Rapidity $Y = \log\sqrt{x_1/x_2}$')
        ax.set_xlabel(r'$m_{tt}\;\mathrm{GeV}$')
        ax.set_title(r'$pdf(x|H_1(c=10^{%d}))$'%(-3+i))

        x = np.arange(2*mt,3*mt,1)
        Ymax = np.log(np.sqrt(s)/(2*mt))
        Ymin = - 0.99*Ymax
        y = np.arange(Ymin, Ymax, 0.1)
        X,Y = np.meshgrid(x, y)
        Z = (vdoubleDiffxSecgg(X,Y, coeffs[i]) + vdoubleDiffxSecqq(X,Y,coeffs[i]))/xSec[i]
        im = ax.imshow(Z, cmap=plt.cm.Blues, aspect = 23.7, vmax=10**-3, vmin=0, extent=[2*mt, 3*mt, Ymin, Ymax])
        plt.colorbar(im)
        cnt+=1
    plt.tight_layout()
    plt.show()
