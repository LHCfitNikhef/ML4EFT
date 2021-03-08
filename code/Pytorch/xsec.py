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
pb_convert = 3.894E2

#Partonic cross sections

def sigma_qq(sqrts, cuGRe, cuu1):
    hats = sqrts**2
    vev = 246.21961912951551
    asQCD = 0.1179
    yt = 0.9922828427689138
    yu = 1.2406408983676737E-5
    Lambda = 1000
    a = np.sqrt(1-4*mt**2/hats)

    sm = 8*np.pi*asQCD**2*(2*mt**2+hats)*a/(27*hats**2)

    kappa_cuGRe_cuGRe = 2*vev**2*asQCD*a*(2*mt**2*(4*yt**2+yu**2)+s*(yt**2+yu**2))/(27*LambdaSMEFT**4*hats)
    kappa_cuGRe = 8*np.sqrt(2*np.pi)*vev*yt*mt*asQCD**(3/2)*a/(9*Lambda**2*s)

    kappa_cuu1_cuu1 = (s-mt**2)*a/(12*np.pi*LambdaSMEFT**4)
    kappa_cuu1 = (4*asQCD*(2*mt**2+hats)*a)/(27*LambdaSMEFT**2*hats)

    kappa_cuu1_cuGRe = (2*np.sqrt(2/np.pi)*vev*yt*mt*np.sqrt(asQCD)*a)/(9*LambdaSMEFT**4)

    sigma = sm + cuu1*kappa_cuu1 + cuGRe*kappa_cuGRe + cuu1**2*kappa_cuu1_cuu1 + cuGRe**2*kappa_cuGRe_cuGRe + cuu1*cuGRe*kappa_cuu1_cuGRe
    return sigma



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


def weight(sqrts, mu, x1, x2, cSMEFT, order=None, NP=None):
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
        w_ii = sigma_part_gg_SM(sqrts) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
        # Uncomment line below to turn on quark contribution
        w_ii += 2 * sigma_part_qq_SM(sqrts) * np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    if order == "NHO":
        w_ii = sigma_part_gg_LO(sqrts, cSMEFT) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
        # #Uncomment line below to turn on quark contribution
        # w_ii += 2*sigma_part_qq_LO(sqrts, cSMEFT)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])#Factor of two accounts of pi - theta contribution
        # #Uncomment line below to turn on quark contribution
        w_ii += 2*sigma_part_qq_LO(sqrts, cSMEFT)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])#Factor of two accounts of pi - theta contribution
    if order == "HO":
        w_ii = sigma_part_gg_NLO(sqrts, cSMEFT)*(p.xfxQ(21, x1, mu)*p.xfxQ(21, x2, mu))
        #Uncomment line below to turn on quark contribution
        w_ii += 2*sigma_part_qq_NLO(sqrts, cSMEFT)*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
    return w_ii

def n_alpha_ana(y, mtt):
    """
    :param mtt: invariant mass of the top-quark pair
    :param y: rapidity of the top-quark pair
    :return: r(x,c) = (1 + c*n_alpha)**2 + (c*n_beta)**2 at the linear level in the EFT. This function gives n_alpha (analytically).
    """
    x1 = mtt / np.sqrt(s) * np.exp(y)
    x2 = mtt / np.sqrt(s) * np.exp(-y)
    if np.abs(y) < np.log(np.sqrt(s) / mtt):
        return weight(mtt, 91.188, x1, x2, 1, order="NHO")/(weight(mtt, 91.188, x1, x2, 1, order="SM"))
    else:
        return 0

def n_alpha_n_beta_ana(y, mtt):
    """
    :param mtt: invariant mass of the top-quark pair
    :param y: rapidity of the top-quark pair
    :return: r(x,c) = (1 + c*n_alpha)**2 + (c*n_beta)**2 at the linear level in the EFT. This function gives n_alpha**2 + n_beta**2 (analytically).
    """
    x1 = mtt / np.sqrt(s) * np.exp(y)
    x2 = mtt / np.sqrt(s) * np.exp(-y)
    if np.abs(y) < np.log(np.sqrt(s) / mtt):
        return weight(mtt, 91.188, x1, x2, 1, order="HO") / weight(mtt, 91.188, x1, x2, 1, order="SM")
    else:
        return 0


def numerator(y, mtt):
    if np.abs(y) < np.log(np.sqrt(s) / mtt):
        return weight(mtt, 91.188, mtt / np.sqrt(s) * np.exp(y), mtt / np.sqrt(s) * np.exp(-y), 1, order="NHO")
    else:
        return 0

def n_alpha_n_beta_ana_num(y, mtt):
    if np.abs(y) < np.log(np.sqrt(s) / mtt):
        return weight(mtt, 91.188, mtt / np.sqrt(s) * np.exp(y), mtt / np.sqrt(s) * np.exp(-y), 1, order="HO")
    else:
        return 0

def n_alpha_n_beta_ana_den(y, mtt):
    if np.abs(y) < np.log(np.sqrt(s) / mtt):
        return weight(mtt, 91.188, mtt / np.sqrt(s) * np.exp(y), mtt / np.sqrt(s) * np.exp(-y), 1, order="SM")
    else:
        return 0


def denominator(y, mtt):
    if np.abs(y) < np.log(np.sqrt(s) / mtt):
        return weight(mtt, 91.188, mtt / np.sqrt(s) * np.exp(y), mtt / np.sqrt(s) * np.exp(-y), 1, order="SM")
    else:
        return 0


def n_alpha_ana_1D(mtt):
    y_min, y_max = -0.5 * np.log(s / mtt), 0.5 * np.log(s / mtt)
    return (integrate.quad(numerator, y_min, y_max, args=mtt)[0])/(2*integrate.quad(denominator, y_min, y_max, args=mtt)[0])


def n_alpha_n_beta_ana_1D(mtt):
    y_min, y_max = -0.5 * np.log(s / mtt), 0.5 * np.log(s / mtt)
    n_alpha_n_beta = (integrate.quad(n_alpha_n_beta_ana_num, y_min, y_max, args=mtt)[0])/(integrate.quad(n_alpha_n_beta_ana_den, y_min, y_max, args=mtt)[0])
    return n_alpha_n_beta

# x = np.arange(1, 4, 0.1)
# y = np.array([n_alpha_ana_1D(x_i) for x_i in x])
# n_alpha_n_beta = np.array([n_alpha_n_beta_ana_1D(x_i) for x_i in x])
# ctg = 5
# r = 1 + 2*ctg*n_alpha + ctg**2*n_alpha_n_beta
# mtt = 2.25
# y_min, y_max = -0.5 * np.log(s / mtt), 0.5 * np.log(s / mtt)
# x = np.arange(y_min, y_max, 0.1)
# y = np.array([n_alpha_ana(x_i, mtt) for x_i in x])
# plt.plot(x, y)
# plt.show()


# print(1+10*n_alpha_ana(0, 2.5))

v_weight = np.vectorize(weight, otypes=[np.float64])

x_coord = []
y_coord = []
def dsigma_dmtt_dy(y, mtt, cSMEFT, order = None, NP = None):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if mtt == 2*mt: return 0 #if at threshold return zero

    if np.abs(y) < 0.9 * np.log(np.sqrt(s)/mtt): #check whether x = {mtt, y} falls inside the physically allowed region
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

def f_analytic(mtt, y, cSMEFT, order = None, NP = None):
    r = likelihood_ratio(y, mtt, cSMEFT, order, NP)
    return 1/(1+r)


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
    _, y_sm = crossSection(binWidth, mtt_max, 5, NP = 2)

    #load the madgraph result
    # data_madgraph = []
    # found_weight = False
    # for e in pylhe.readLHE('lhe_events/eft_50.lhe'):
    #     data_madgraph.append(invariant_mass(e.particles[-1],e.particles[-2]))
    #     if found_weight == False:
    #         weight = e.eventinfo.weight
    #         found_weight = True
    # print("madgraph xsec = ", weight)
    # hist_mg, bins_mg = np.histogram(data_madgraph, bins = np.arange(2*mt, np.max(data_madgraph), binWidth), density = True)
    # hist_mg *= weight

    #show analytical result and mg5 in one plot
    fig = plt.figure()

    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels = [], xlim = (2 * mt, 2.500))
    ax1.plot(x, y, '-', c='red', label='EFT NLO')
    ax1.plot(x, y_sm, '-', c='orange', label='SM')

    # ax1.step(bins_mg[:-1], hist_mg, where ='post', label = 'EFT NLO (mg5)')
    plt.title('Energy growing effects at c'+r'$=10$')

    plt.yscale('log')
    plt.ylabel(r'$d\sigma/dm_{tt}\;\mathrm{[pb\:TeV^{-1}]}$')
    plt.legend()

    #add a subplot that shows the ratio analytical/madgraph
    # ax2 = fig.add_axes([0.1, 0.25, 0.75, 0.10], ylim = (0.9, 1.1) )
    # ax2.scatter(x, hist_mg[:len(x)]/(y), s = 10)
    # ax2.hlines(1, 2*mt, mtt_max, colors='k', linestyles ='dashed')


    # plt.ylabel('num/ana')
    # plt.xlim((2*mt, mtt_max))

    ax3 = fig.add_axes([0.15, 0.1, 0.75, 0.20], ylim = (0.8*(y/y_sm).min(), 1.1*(y/y_sm).max()))
    ax3.plot(x, y/y_sm, '-')

    plt.xlabel(r'$m_{tt}\;\mathrm{[TeV]}$')
    plt.ylabel('BSM/SM')
    plt.xlim((2*mt, mtt_max))

    plt.show()
    fig.savefig('energy_growing_effects.pdf')

def plot_f_ana(mtt_min, mtt_max, y_min, y_max, x_spacing, y_spacing, ctg, np_order=None):

    # Important to include otypes = [np.float], else all the output is int by default
    vf_ana = np.vectorize(f_analytic, otypes=[np.float])
    x = np.arange(mtt_min*10**-3, mtt_max*10**-3, x_spacing*10**-3)
    y = np.arange(y_min, y_max, y_spacing)
    xx, yy = np.meshgrid(x, y)
    Z = vf_ana(xx, yy, ctg, NP=np_order)
    return Z


def plot_likelihood_ratio_1D(mtt_min, mtt_max, ctg, np_order=None):
    x = np.arange(mtt_min, mtt_max, 100*1e-3)
    y = [1/(1+likelihood_ratio_1D(x_i, ctg, NP=np_order)) for x_i in x]
    return x, y




