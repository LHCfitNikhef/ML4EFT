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
asQCD = 0.1184
#cSMEFT = 1
LambdaSMEFT = 10**3

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

def dsigmadThetaqq(sqrts, theta, cSMEFT):
    sP = sqrts**2
    g = np.sqrt(4*np.pi*asQCD)
    Me2 = cSMEFT*(16*np.sqrt(2)*g**3*v*mt)/(9*LambdaSMEFT**2)
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

def diffCrossHadronicBSMQuark(sqrts):
    sP = sqrts**2
    integrand = lambda y, theta:(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))
                +p.xfxQ(5, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(-5, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts)))*dsigmadThetaqq(sqrts, theta)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossBSMqq = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossBSMqq

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


def dsigmadThetagg(sqrts, theta, cSMEFT):
    sP = sqrts**2
    t = mt**2-(sP/2)*(1-np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    u = mt**2-(sP/2)*(1+np.cos(theta)*np.sqrt(1-4*mt**2/sP))
    g = np.sqrt(4*np.pi*asQCD)
    Me2 = (cSMEFT*g**3*v*mt*(-18*mt**2*(t+u)+18*mt**4-sP**2+9*(t**2+u**2)))/(6*np.sqrt(2)*LambdaSMEFT**2*(mt**2-t)*(mt**2-u))
    phaseSpaceFac = (1/(64*np.pi**2*sP))*np.sqrt(1-(4*mt**2)/sP)
    dsigmadOmega = phaseSpaceFac*Me2
    dsigmadTheta = 2*np.pi*np.sin(theta)*dsigmadOmega
    return dsigmadTheta

def diffCrossHadronicBSMGluon(sqrts):
    sP = sqrts**2
    integrand = lambda y, theta:(s/sP)*p.xfxQ(21, np.sqrt(sP/s)*np.exp(y), renScale(theta, sqrts))*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-y), renScale(theta, sqrts))*dsigmadThetagg(sqrts, theta)
    #factor 2*np.sqrt(sP) comes from the chain rule
    diffCrossBSMgg = 0.3894*(10**9)*(2*np.sqrt(sP)/s)*integrate.dblquad(integrand,0, np.pi, lambda theta: -0.5*np.log(s/sP), lambda theta : 0.5*np.log(s/sP))[0]
    return diffCrossBSMgg

def renScale(theta, sqrts):
    sP = sqrts**2
    p_T = np.sqrt((sP/4)-mt**2)*np.sin(theta)
    m_T = np.sqrt(sP/4-p_T**2)
    #H_T = 2*(np.sqrt(mt**2+p_T**2))
    #return (H_T/2)**2
    return (mt**2+p_T**2)

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
    x = np.arange(2*mt, 500, 20)
    for i in x:
        print(i)
        #crossSection.append(diffCrossSM(i))
        crossSectionBSM.append(diffCrossBSM(i))
    #crossSection = np.array(crossSection)
    crossSectionBSM = np.array(crossSectionBSM)
    #xsecSM = integrate.quad(lambda x: diffCrossSM(x), 2*mt, 4000)[0]
    #xsecBSM = integrate.quad(lambda x: diffCrossBSM(x), 2*mt, 5000)[0]
    #print("xsec SM: ", xsecSM)
    #print("xsec BSM: ", xsecBSM)
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
    hist_eft *= 110.478
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

#generateData()

def doubleDiffxSecgg(sqrts, y, cSMEFT):
    sP = sqrts**2
    sigmaPartgg = integrate.quad(lambda theta: dsigmadThetagg(sqrts, theta,cSMEFT) + dsigmadThetaggSM(sqrts, theta), 0, np.pi)[0]
    if (np.abs(y) < 0.5*np.log(s/sP)):
        dsigmadmttdY = 0.3894*(10**9)*(2*sqrts/s)*sigmaPartgg*(s/sP)*p.xfxQ(21, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(21, np.sqrt(sP/s)*np.exp(-y), sP)
        return dsigmadmttdY
    else:
        return 0

def doubleDiffxSecqq(sqrts, y, cSMEFT):
    sP = sqrts**2
    sigmaPartqq = integrate.quad(lambda theta: dsigmadThetaqq(sqrts, theta, cSMEFT) + dsigmadThetaqqSM(sqrts, theta), 0, np.pi)[0]
    if (np.abs(y) < 0.5*np.log(s/sP)):
        dsigmadmttdY = 0.3894*(10**9)*(2*sqrts/s)*sigmaPartqq*(s/sP)*(p.xfxQ(1, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(-1, np.sqrt(sP/s)*np.exp(-y), sP)
                    +p.xfxQ(2, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(-2, np.sqrt(sP/s)*np.exp(-y), sP)
                    +p.xfxQ(3, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(-3, np.sqrt(sP/s)*np.exp(-y), sP)
                    +p.xfxQ(4, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(-4, np.sqrt(sP/s)*np.exp(-y), sP)
                    +p.xfxQ(5, np.sqrt(sP/s)*np.exp(y), sP)*p.xfxQ(-5, np.sqrt(sP/s)*np.exp(-y), sP))
        return dsigmadmttdY
    else:
        return 0

# def test(x,y):
#     return y*(x+3)
#
# testv = np.vectorize(test)
# x = np.ones(5)
# y = np.arange(1,4,1)
# X, Y = np.meshgrid(x,y)
# print (testv(X,Y))


#print("value", doublyDiffxSecgg(3*mt, -0.25*np.log(s/(2*mt)**2)))

vdoubleDiffxSecgg = np.vectorize(doubleDiffxSecgg)
vdoubleDiffxSecqq = np.vectorize(doubleDiffxSecqq)


coeffs=np.array([0.001, 0.01, 0.1, 1, 10, 100])
#xSec = np.array([344.3, 345.9, 354.7, 443.9,1350, 1.039*10**4])
xSec = 443.9
npar = len(coeffs)
gs = int(np.sqrt(npar))+1
nrows, ncols = 3, 2
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
    Z = (vdoubleDiffxSecgg(X,Y, coeffs[i]) + vdoubleDiffxSecqq(X,Y,coeffs[i]))/xSec
    im = ax.imshow(Z, cmap=plt.cm.Blues, aspect = 23.7, vmax=10**-3, vmin=0, extent=[2*mt, 3*mt, Ymin, Ymax])
    plt.colorbar(im)
    cnt+=1

plt.tight_layout()
plt.show()





#

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_ylabel(r'Rapidity $Y = \sqrt{\log x_1/x_2}$')
# ax.set_xlabel(r'$m_{tt}$')
# ax.set_title(r'$pdf(x|H_1)$')
# x = np.arange(2*mt,3*mt,1)
# Ymax = np.log(np.sqrt(s)/(2*mt))
# Ymin = - 0.99*Ymax
# y = np.arange(Ymin, Ymax, 0.1)
# X,Y = np.meshgrid(x, y) # grid of point
# Z = (vdoubleDiffxSecgg(X,Y) + vdoubleDiffxSecqq(X,Y))/xSec # evaluation of the function on the grid
#
# # #print(np.max(Z))
# im = ax.imshow(Z, cmap=plt.cm.Blues, vmax=Z.max(), vmin=Z.min(), aspect = 100, extent=[2*mt, 3*mt, Ymin, Ymax]) # drawing the function
# # #adding the Contour lines with labels
# # #cset = plt.contour(Z,np.arange(-1,1.5,0.2),linewidths=2)
# # #clabel(cset,inline=True,fmt='%1.1f',fontsize=10)
# plt.colorbar(im) # adding the colobar on the right
# # # latex fashion title
# #
# plt.show()



# doublyDiffxSecggResult = [[0] * 10 for i in range(10)]
# sqrts = np.linspace(2*mt, 3*mt, 10)
# for i in range(len(sqrts)):
#     y = np.linspace(0, 0.5*np.log(s/sqrts[i]**2), 10)
#     for j in range(len(y)):
#         doublyDiffxSecggResult[i][j] = doublyDiffxSecgg(sqrts[i],y[j])
# print(doublyDiffxSecggResult)
