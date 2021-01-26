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
mt = 0.172  # 172 #Top quark mass in GeV
s = 14**2  # (14*10**3)**2#GeV^2
Gf = 0.0000116637
v = 1/np.sqrt(Gf*np.sqrt(2))*10**-3  # 1/np.sqrt(Gf*np.sqrt(2))
asQCD = 0.1184
LambdaSMEFT = 1  # 10**3
pb_convert = 3.894E8

#Partonic cross sections

def sigma_part_gg(sqrts, cSMEFT):#correct
    if sqrts == 2*mt:
        return 0
    hats = sqrts**2
    num = asQCD**(3/2)*(np.sqrt(2*np.pi)*cSMEFT*hats*v*mt*(16*hats*np.arctanh(np.sqrt(1-4*mt**2/hats))-9*np.sqrt(hats*(hats-4*mt**2)))+8*np.pi*LambdaSMEFT**2*np.sqrt(asQCD)*(4*hats*mt**2+mt**4+hats**2)*np.arctanh(np.sqrt(1-4*mt**2/hats))-31*np.pi*LambdaSMEFT**2*mt**2*np.sqrt(hats*asQCD*(hats-4*mt**2))-7*np.pi*LambdaSMEFT**2*hats*np.sqrt(hats*asQCD*(hats-4*mt**2)))
    den = 12*LambdaSMEFT**2*hats**3
    return num/den

def sigma_part_gg_SM(sqrts):
    if sqrts == 2*mt:
        return 0
    hats = sqrts**2
    num = np.pi*asQCD**2*(8*(4*hats*mt**2+mt**4+hats**2)*np.arctanh(np.sqrt(1-4*mt**2/hats))-31*mt**2*np.sqrt(hats*(hats-4*mt**2))-7*hats*np.sqrt(hats*(hats-4*mt**2)))
    den = 12*hats**3
    return num/den

def sigma_part_gg_LO(sqrts, cSMEFT):
    if sqrts == 2*mt:
        return 0
    hats = sqrts**2
    num = np.sqrt(np.pi/2)*cSMEFT*v*mt*asQCD**(3/2)*np.sqrt(1-4*mt**2/hats)*(16*np.sqrt(hats/(hats-4*mt**2))*np.arctanh(np.sqrt(1-4*mt**2/hats))-9)
    den = 6*LambdaSMEFT**2*hats
    return num/den

def sigma_part_gg_NLO(sqrts, cSMEFT):
    if sqrts == 2*mt:
        return 0
    hats = sqrts**2
    num = cSMEFT**2*v**2*asQCD*np.sqrt(1-4*mt**2/hats)*(mt**2*(16*np.sqrt(hats/(hats-4*mt**2))*np.arctanh(np.sqrt(1-4*mt**2/hats))-3)+6*hats)
    den = 24*LambdaSMEFT**4*hats
    return num/den

def sigma_part_qq_SM(sqrts):
    if sqrts == 2*mt:
        return 0
    hats = sqrts**2
    num = 8*np.pi*asQCD**2*(2*mt**2+hats)*np.sqrt(1-4*mt**2/hats)
    den = 27*hats**2
    return num/den

def sigma_part_qq_LO(sqrts, cSMEFT):
    if sqrts == 2*mt:
        return 0
    hats = sqrts**2
    num = 8*np.sqrt(2*np.pi)*cSMEFT*v*mt*asQCD**(3/2)*np.sqrt(1-4*mt**2/hats)
    den = 9*LambdaSMEFT**2*hats
    return num/den

def sigma_part_qq_NLO(sqrts, cSMEFT):
    if sqrts == 2*mt:
        return 0
    hats = sqrts**2
    num = 2*cSMEFT**2*v**2*asQCD*(8*mt**2+hats)*np.sqrt(1-4*mt**2/hats)
    den = 27*LambdaSMEFT**4*hats
    return num/den

def weight(sqrts, mu, x1, x2, cSMEFT, order, NP):
    """
    NP parameter: order in the EFT
    order parameter: work at one specific order
    """
    if NP == 0:
        w_ii = sigma_part_gg_SM(sqrts)*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))  
        #Uncomment line below to turn on quark contribution 
        w_ii += 2*sigma_part_qq_SM(sqrts)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    if NP == 1:
        w_ii = (sigma_part_gg_SM(sqrts)+sigma_part_gg_LO(sqrts, cSMEFT))*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))  
        #Uncomment line below to turn on quark contribution 
        w_ii += 2*(sigma_part_qq_SM(sqrts)+sigma_part_qq_LO(sqrts, cSMEFT))*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    if NP == 2:
        w_ii = (sigma_part_gg_SM(sqrts)+sigma_part_gg_LO(sqrts, cSMEFT)+sigma_part_gg_NLO(sqrts, cSMEFT))*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))  
        #Uncomment line below to turn on quark contribution 
        w_ii += 2*(sigma_part_qq_SM(sqrts)+sigma_part_qq_LO(sqrts, cSMEFT)+sigma_part_qq_NLO(sqrts, cSMEFT))*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    if order == "SM":
        w_ii = sigma_part_gg_SM(sqrts)*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))  
        #Uncomment line below to turn on quark contribution 
        w_ii += 2*sigma_part_qq_SM(sqrts)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    if order == "NHO":
        w_ii = sigma_part_gg_LO(sqrts, cSMEFT)*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))
        #Uncomment line below to turn on quark contribution 
        w_ii += 2*sigma_part_qq_LO(sqrts, cSMEFT)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])#Factor of two accounts of pi - theta contribution
    if order == "HO":
        w_ii = sigma_part_gg_NLO(sqrts, cSMEFT)*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))  
        #Uncomment line below to turn on quark contribution 
        w_ii += 2*sigma_part_qq_NLO(sqrts, cSMEFT)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    return w_ii

def n_alpha_ana(mtt, y):
    """
    :param mtt: invariant mass of the top-quark pair
    :param y: rapidity of the top-quark pair
    :return: r(x,c) = 1 + c*n_alpha at the linear level in the EFT. This function gives n_alpha (analytically).
    """
    x1 = mtt / np.sqrt(s) * np.exp(y)
    x2 = mtt / np.sqrt(s) * np.exp(-y)
    if np.abs(y) < np.log(np.sqrt(s) / mtt):
        return weight(mtt, 91.188, x1, x2, 1, order="NHO", NP=None)/weight(mtt, 91.188, x1, x2, 1, order="SM", NP=None)
    else:
        return 0


v_weight = np.vectorize(weight, otypes=[np.float])


def dsigma_dmtt_dy(y, mtt, cSMEFT, order = None, NP = None):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if mtt == 2*mt: return 0 #if at threshold return zero
    
    if np.abs(y) < np.log(np.sqrt(s)/mtt): #check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mtt/np.sqrt(s)*np.exp(y)
        x2 = mtt/np.sqrt(s)*np.exp(-y)
        dsigma_dmtt_dy = 2*mtt/s*v_weight(mtt, 91.188, x1, x2, cSMEFT, order, NP)/(x1*x2)
        return pb_convert*dsigma_dmtt_dy
    else:
        return 0

def dsigma_dmtt(mtt, cSMEFT, order = None, NP = None):
    y_min, y_max = -0.5 * np.log(s / mtt), 0.5 * np.log(s / mtt)
    dsigma_dmtt = integrate.quad(dsigma_dmtt_dy, y_min, y_max, args = (mtt, cSMEFT, order, NP))[0]
    return dsigma_dmtt

def likelihood_ratio(y, mtt, cSMEFT, order = None, NP = None):
    """
    Compute the 2D analytic likelihood ratio r(x, c)
    """
    dsigma_0 = dsigma_dmtt_dy(y, mtt, cSMEFT, order, NP)#EFT
    dsigma_1 = dsigma_dmtt_dy(y, mtt, 0, order=None, NP=0)#SM
    ratio = dsigma_0/dsigma_1 if dsigma_1 != 0 else 0
    return ratio

def likelihood_ratio_1D(mtt, cSMEFT, order = None, NP = None):
    """
    Compute the 1D analytic likelihood ratio r(x, c)
    """
    dsigma_0 = dsigma_dmtt(mtt, cSMEFT, order, NP)#EFT
    dsigma_1 = dsigma_dmtt(mtt, 0, order=None, NP=0)#SM
    ratio = dsigma_0/dsigma_1 if dsigma_1 != 0 else 0
    return ratio


def renScale(theta, sqrts):
    sP = sqrts**2
    p_T = np.sqrt((sP/4)-mt**2)*np.sin(theta)
    m_T = np.sqrt(sP/4-p_T**2)
    H_T = 2*(np.sqrt(mt**2+p_T**2))
    #return (H_T/4)
    return 91.188    

def diffCross(sqrts, cSMEFT, order = None, NP = None):
    """Continuous version"""
    mtt = sqrts
    if sqrts >= 2*mt:
        return dsigma_dmtt(mtt, cSMEFT, order, NP) 
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

def crossSection(binWidth, mtt_max, cSMEFT, order = None, NP = None):
    """
    Compute the analytical differential cross section in M(tt)
    inputs:
        - binWidth = bin width of the MG5 events
        - mtt_max = plot goes from [2*mt, mtt_max]
        - cSMEFT = Value of ctG in TeV^-2
    outputs:
        - (x,y) with x = m_tt and y = dsigma/dmtt
    """
    x = np.arange(2*mt + binWidth / 2, mtt_max, binWidth)
    y = np.array([diffCross(mtt, cSMEFT, order, NP) for mtt in x])
    return x, y

def plotData(binWidth, mtt_max, cSMEFT, order = None, NP = None):
    """
    Plot the differential cross section in M(tt) and compare it with the MG5 result
    inputs: 
        - binWidth = bin width of the MG5 events
        - mtt_max = plot goes from [2*mt, mtt_max]
        - cSMEFT = Value of ctG in TeV^-2
    """
    
    #compute the analytical result
    x, y = crossSection(binWidth, mtt_max, cSMEFT, order, NP)
    _, y_sm = crossSection(binWidth, mtt_max, 0, NP = 0)

    #load the madgraph result
    data_madgraph = []
    found_weight = False
    for e in pylhe.readLHE('lhe_events/eft_50.lhe'):
        data_madgraph.append(invariant_mass(e.particles[-1],e.particles[-2]))
        if found_weight == False:
            weight = e.eventinfo.weight
            found_weight = True
    print("madgraph xsec = ", weight)
    hist_mg, bins_mg = np.histogram(data_madgraph, bins = np.arange(2*mt, np.max(data_madgraph), binWidth), density = True)
    hist_mg *= weight
    
    #show analytical result and mg5 in one plot
    fig = plt.figure()
    
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels = [], xlim = (2 * mt, 2500))
    ax1.plot(x, y, '-', c='red', label='EFT NLO')
    ax1.plot(x, y_sm, '-', c='orange', label='SM')
    
    # ax1.step(bins_mg[:-1], hist_mg, where ='post', label = 'EFT NLO (mg5)')
    plt.title('Energy growing effects at c'+r'$=10$')

    plt.yscale('log')
    plt.ylabel(r'$d\sigma/dm_{tt}\;\mathrm{[pb\:GeV^{-1}]}$')
    plt.legend()

    #add a subplot that shows the ratio analytical/madgraph
    # ax2 = fig.add_axes([0.1, 0.25, 0.75, 0.10], ylim = (0.9, 1.1) )
    # ax2.scatter(x, hist_mg[:len(x)]/(y), s = 10)
    # ax2.hlines(1, 2*mt, mtt_max, colors='k', linestyles ='dashed')

    
    # plt.ylabel('num/ana')
    # plt.xlim((2*mt, mtt_max))

    ax3 = fig.add_axes([0.15, 0.1, 0.75, 0.20], ylim = (0.8*(y/y_sm).min(), 1.1*(y/y_sm).max()))
    ax3.plot(x, y/y_sm, '-')

    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('BSM/SM')
    plt.xlim((2*mt, mtt_max))
    
    plt.show()
    fig.savefig('energy_growing_effects.pdf')

def plot_likelihood_ratio():
    
    y_max = np.log(np.sqrt(s)/(2*mt))
    y_min = -y_max

    # Important to include otypes = [np.float], else all the output is int by default
    vlikelihood_ratio = np.vectorize(likelihood_ratio, otypes=[np.float])

    fig = plt.figure()
    mtt_max = 2.500
    mtt_min = 2*mt
    x = np.arange(mtt_min, mtt_max, 10**-3)
    y = np.arange(y_min, y_max, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = vlikelihood_ratio(Y, X, 10.0, NP=1)

    Z_mask = np.ma.masked_equal(Z,0)
    mean = Z_mask.mean()
    std = Z_mask.std()
    
    im = plt.imshow(Z, cmap = plt.cm.Blues, aspect = (mtt_max-mtt_min)/(y_max-y_min), extent=[mtt_min, mtt_max, y_min, y_max], vmin = mean - 3*std, vmax = mean + 3*std, interpolation='quadric', origin='lower')
    plt.colorbar(im)

    plt.ylabel(r'Rapidity $Y = \log\sqrt{x_1/x_2}$')
    plt.xlabel(r'$m_{tt}\;\mathrm{[TeV]}$')
    plt.title('Likelihood ratio: Linear EFT')

    #plt.title(r'$pdf(x|H_1(c=10^{%d}))$'%(-3+3))
    plt.show()
    fig.savefig('likelihood_ratio_EFT_Linear.pdf')


def plot_likelihood_ratio_1D(mtt_min, mtt_max, ctg, np_order=None):
    x = np.arange(mtt_min, mtt_max, 10 ** -2)
    #print(likelihood_ratio_1D(2.0, 10, NP=1))
    # sys.exit()
    y = [1/(1+likelihood_ratio_1D(x_i, ctg, NP=np_order)) for x_i in x]
    # fig = plt.figure()
    # plt.plot(x, y)
    # plt.xlabel(r'$m_{tt}\;\mathrm{[TeV]}$')
    # plt.ylabel(r'$r(m_{tt}, c)$')
    # plt.title('Likelihood ratio: Linear EFT marginalised, c = 10')
    # plt.show()
    # fig.savefig('likelihood_ratio_1D_v2.pdf')
    return x, y



# plotData(15, 2500, 10, NP = 2)
#plot_likelihood_ratio()
#plot_likelihood_ratio_1D()

#print(dsigma_dmtt(400, 1, NP = 1))

# x = np.arange(0.75, 2.5, 10**-3)[1:]
# n_alpha = np.array([n_alpha_ana(x_i, 0) for x_i in x])
# fig = plt.figure()
# plt.plot(x, 1+10*n_alpha)
# plt.xlabel(r'$m_{tt}\;\mathrm{[TeV]}$')
# plt.ylabel(r'$r = 1+10*n_\alpha$')
# plt.title('Analytic likelihood ratio at y=0 and ctG = 10')
# plt.ylim(3.2, 3.6)
# plt.show()
# fig.savefig('n_alpha.pdf')

