# Author: Jaco ter Hoeve
# This files contains the analytical cross sections in the eft as obtained through FeynCalc
#%%
from __future__ import division
import lhapdf
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
from scipy.integrate import quad, dblquad
from scipy import integrate
import pylhe

from quad_clas.core.xsec import vh_prod

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
mt = 0.17276  # 172 #Top quark mass plot_mg5_ana_mttin GeV
s = 14 ** 2  # (14*10**3)**2#GeV^2
Gf = 0.0000116637
v = 1 / np.sqrt(Gf * np.sqrt(2)) * 10 ** -3  # 1/np.sqrt(Gf*np.sqrt(2))
asQCD = 0.1179
LambdaSMEFT = 1  # 10**3
pb_convert = 3.894E2
yt = 0.9922828427689138

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

# Partonic cross sections

class crossSectionSMEFT:
    """
    A class that contains all EFT cross sections...

    """

    def sigma_part_gg(self, hats, cuGRe, cuu):  # TODO: fix the gluon gluon contribution
        if np.sqrt(hats) == 2 * mt:
            return 0

        sqrt = np.sqrt(1 - 4 * mt ** 2 / hats)
        kappa_11 = ((v ** 2 * yt ** 2 * asQCD) / (24 * LambdaSMEFT ** 4 * hats ** 3)) * (
                    6 * np.sqrt(hats ** 5 * (hats - 4 * mt ** 2)) + hats * mt ** 2 * (
                        -3 * np.sqrt(hats * (hats - 4 * mt ** 2)) - 8 * hats * np.log(1 - sqrt) + 8 * hats * np.log(sqrt + 1)))
        kappa_1 = (np.sqrt(np.pi) * v * yt * mt * asQCD) / (6 * LambdaSMEFT ** 2 * hats ** 2 * np.sqrt(2)) * (
                    9 * np.sqrt(hats * asQCD * (hats - 4 * mt ** 2)) + 8 * hats * np.sqrt(asQCD) * (
                        np.log(1 - np.sqrt(1 - 4 * mt ** 2 / hats)) - np.log(np.sqrt(1 - 4 * mt ** 2 / hats) + 1)))
        sm = (-np.pi * asQCD ** 2) / (12 * hats ** 3) * (
                    4 * mt ** 4 * (np.log(1 - sqrt) - np.log(sqrt + 1)) + mt ** 2 * (
                        31 * np.sqrt(hats * (hats - 4 * mt ** 2)) + 16 * hats * np.log(1 - sqrt) - 16 * hats * np.log(
                    sqrt + 1)) + hats * (7 * np.sqrt(hats * (hats - 4 * mt ** 2)) + 4 * hats * np.log(
                1 - sqrt) - 4 * hats * np.log(sqrt + 1)))
        return sm + cuGRe * kappa_1 + cuGRe ** 2 * kappa_11

    def sigma_part_qq(self, hats, cuGRe, cuu):
        if np.sqrt(hats) == 2 * mt:
            return 0

        sqrt = np.sqrt(1 - 4 * mt ** 2 / hats)
        kappa_11 = sqrt * (8 * np.pi * v ** 2 * yt ** 2 * asQCD * (8 * mt ** 2 + hats)) / (
                    108 * np.pi * LambdaSMEFT ** 4 * hats)
        kappa_22 = sqrt * (9 * hats * (hats - mt ** 2)) / (108 * np.pi * LambdaSMEFT ** 4 * hats)
        kappa_1 = - (8 * np.sqrt(2 * np.pi) * v * yt * mt * asQCD ** (3 / 2) * sqrt) / (9 * hats * LambdaSMEFT ** 2)
        sm = (8 * np.pi * asQCD ** 2 * (2 * mt ** 2 + hats) * sqrt) / (27 * hats ** 2)
        return sm + cuGRe * kappa_1 + cuGRe ** 2 * kappa_11 + cuu ** 2 * kappa_22

xsec = crossSectionSMEFT()

def weight(sqrts, mu, x1, x2, cuGRe, cuu):
    """
    NP parameter: order in the EFT
    order parameter: work at one specific order
    """
    hats = sqrts ** 2
    #w_ii = (xsec.sigma_part_gg(hats, cuGRe, cuu)) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
    w_ii = (xsec.sigma_part_qq(hats, cuGRe, 0)) * (
                p.xfxQ(1, x1, mu) * p.xfxQ(-1, x2, mu) + p.xfxQ(3, x1, mu) * p.xfxQ(-3, x2, mu) + p.xfxQ(5, x1,
                                                                                                         mu) * p.xfxQ(
            -5, x2, mu))
    w_ii += (xsec.sigma_part_qq(hats, cuGRe, cuu)) * (
                p.xfxQ(2, x1, mu) * p.xfxQ(-2, x2, mu) + p.xfxQ(4, x1, mu) * p.xfxQ(-4, x2, mu))
    # w_ii += 2*(xsec.sigma_part_qq(hats, cuGRe, cuu))*np.sum([p.xfxQ(pid, x1, mu)*p.xfxQ(-pid, x2, mu) for pid in p.flavors()[:5]])
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
        return weight(mtt, 91.188, x1, x2, 1, order="NHO", NP=None) / weight(mtt, 91.188, x1, x2, 1, order="SM",
                                                                             NP=None)
    else:
        return 0

def dsigma_dx(x, cug, cuu):
    """
        Compute the doubly differential cross section in mtt and y at any order NP
        """
    mtt, y = x
    if mtt == 2 * mt: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mtt):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mtt / np.sqrt(s) * np.exp(y)
        x2 = mtt / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mtt / s * v_weight(mtt, 91.188, x1, x2, cug, cuu) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0


v_weight = np.vectorize(weight, otypes=[np.float])


def dsigma_dmtt_dy(y, mtt, cuGRe, cuu):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if mtt == 2 * mt: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mtt):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mtt / np.sqrt(s) * np.exp(y)
        x2 = mtt / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mtt / s * v_weight(mtt, 91.188, x1, x2, cuGRe, cuu) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0


dsigma_dmtt_dy_vec = np.vectorize(dsigma_dmtt_dy, otypes=[np.float])


def dsigma_dmtt(mtt, cuGRe, cuu):
    y_min, y_max = -0.5 * np.log(s / mtt), 0.5 * np.log(s / mtt)
    dsigma_dmtt = integrate.fixed_quad(dsigma_dmtt_dy_vec, y_min, y_max, args=(mtt, cuGRe, cuu), n=10)[0] #TODO: n=100 previously, does n= 10 also give good performances?
    return dsigma_dmtt

#%%


def likelihood_ratio(y, mtt, cuGRe, cuu):
    """
    Compute the 2D analytic likelihood ratio r(x, c)
    """
    dsigma_0 = dsigma_dmtt_dy(y, mtt, cuGRe, cuu)  # EFT
    dsigma_1 = dsigma_dmtt_dy(y, mtt, 0, 0)  # SM
    ratio = dsigma_0 / dsigma_1 if dsigma_1 != 0 else 0
    return ratio


def likelihood_ratio_1D(mtt, c):
    """
    Compute the 1D analytic likelihood ratio r(x, c)
    """
    dsigma_0 = vh_prod.dsigma_dmvh(mtt, c, lin=True, quad=False)  # EFT
    dsigma_1 = vh_prod.dsigma_dmvh(mtt, c=0, lin=True, quad=False)  # SM
    ratio = dsigma_0 / dsigma_1 if dsigma_1 != 0 else 0
    return ratio



def renScale(theta, sqrts):
    sP = sqrts ** 2
    p_T = np.sqrt((sP / 4) - mt ** 2) * np.sin(theta)
    m_T = np.sqrt(sP / 4 - p_T ** 2)
    H_T = 2 * (np.sqrt(mt ** 2 + p_T ** 2))
    # return (H_T/4)
    return 91.188


def diffCross(sqrts, cuGRe, cuu):
    """Continuous version"""
    mtt = sqrts
    if sqrts >= 2 * mt:
        return dsigma_dmtt(mtt, cuGRe, cuu)
    else:
        return 0


def invariant_mass(p1, p2):
    return np.sqrt(
        sum((1 if mu == 'e' else -1) * (getattr(p1, mu) + getattr(p2, mu)) ** 2 for mu in ['e', 'px', 'py', 'pz']))


def rapidity(p1, p2):
    # Follow P&S page 565
    q0 = getattr(p1, 'e') + getattr(p2, 'e')  # energy of the top quark pair in the pp COM frame
    q3 = getattr(p1, 'pz') + getattr(p2, 'pz')
    y = 0.5 * np.log((q0 + q3) / (q0 - q3))
    return y


def crossSection(binWidth, mtt_max, cuGRe, cuu):
    """
    Computes the analytical differential cross section in M(tt)

    Parameters
    ----------
    binWidth: float
        binwidth of the MG5 events
    mtt_max: float
        plot goes from [2*mt, mtt_max]
    cuGRe: float
        wilson coefficient cug
    cuu: float
        wilson coefficient cuu

    Returns
    -------
    tuple
        two array_like objects, mtt and dsigma/dmtt
    """
    x = np.arange(2 * mt + binWidth / 2, mtt_max, binWidth)
    y = np.array([diffCross(mtt, cuGRe, cuu) for mtt in x])
    return x, y


def plotData(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path):
    """
    Create a plot that shows the mg5 histogram in m_tt on top of the analytical (exact) result.
    This allows for a visual cross-check of the analytical result.
    :param binWidth: binwidth in TeV
    :param mtt_max: maximum m_tt in TeV
    :param cuGRe: eft parameter cuGRe
    :param cuu: eft parameter cuu
    :param path_to_file: path to lhe file
    :param save_path: path where the plot should be stored
    """

    # compute the analytical result
    #x, y = crossSection(binWidth, mtt_max, cuGRe, cuu)
    x, y_sm = crossSection(binWidth, mtt_max, 0, 0)

    # load the madgraph result
    data_madgraph = []
    found_weight = False
    for e in pylhe.readLHE(path_to_file):
        data_madgraph.append(invariant_mass(e.particles[-1], e.particles[-2]) * 10 ** -3)
        if found_weight == False:
            weight = e.eventinfo.weight
            found_weight = True

    # make a histogram from the mg5 data
    hist_mg, bins_mg = np.histogram(data_madgraph, bins=np.arange(2 * mt, np.max(data_madgraph), binWidth),
                                    density=True)
    hist_mg *= weight

    # show analytical result and mg5 in one plot
    fig = plt.figure(figsize=(10, 6))
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[], xlim=(2 * mt, mtt_max))
    #ax1.plot(x, y, '-', c='red', label=r'$\rm{Ana}$')
    ax1.plot(x, y_sm, '-', c='orange', label=r'$\rm{SM}$')
    ax1.step(bins_mg[:-1], hist_mg, where='post', label=r'$\rm{mg5}$')
    ax1.text(0.05, 0.12, r'$\rm{cuu} = %.2f $' % cuu, fontsize=20, transform=ax1.transAxes)
    ax1.text(0.05, 0.05, r'$\rm{cug} = %.2f $' % cuGRe, fontsize=20, transform=ax1.transAxes)
    #plt.title('Analytic versus mg5 at ' + r'$ctg={}$'.format(cuGRe) + ' and ' + r'$cuu={}$'.format(cuu))

    plt.yscale('log')
    plt.ylabel(r'$d\sigma/dm_{tt}\;\mathrm{[pb\:TeV^{-1}]}$')
    plt.legend(frameon=False, loc='best')

    # add a subplot that shows the ratio analytical/madgraph
    ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))
    ax2.scatter(x, hist_mg[:len(x)] / y_sm, s=10)
    ax2.hlines(1, 2 * mt, mtt_max, colors='k', linestyles='dashed')

    plt.ylabel(r'$\rm{num/ana}$')
    plt.xlim((2 * mt, mtt_max))

    # ax3 = fig.add_axes([0.15, 0.1, 0.75, 0.20], ylim = (0.8*(y/y_sm).min(), 1.1*(y/y_sm).max()))
    # ax3.plot(x, y/y_sm, '-')

    plt.xlabel(r'$m_{tt}\;\mathrm{[TeV]}$')
    # plt.ylabel('BSM/SM')
    # plt.xlim((2*mt, mtt_max))

    plt.show()
    fig.savefig(save_path)


def plot_xsec_ana(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path):
    """
    Create a plot that shows the mg5 histogram in m_tt on top of the analytical (exact) result.
    This allows for a visual cross-check of the analytical result.
    :param binWidth: binwidth in TeV
    :param mtt_max: maximum m_tt in TeV
    :param cuGRe: eft parameter cuGRe
    :param cuu: eft parameter cuu
    :param path_to_file: path to lhe file
    :param save_path: path where the plot should be stored
    """

    # compute the analytical result
    x, y = crossSection(binWidth, mtt_max, cuGRe, cuu)
    _, y_sm = crossSection(binWidth, mtt_max, 0, 0)


    # show analytical result and mg5 in one plot
    fig, ax = plt.subplots(figsize=(10,8))
    ax.plot(x, y, '-', c='C0', label=r'$\rm{EFT}$')
    ax.plot(x, y_sm, '-', c='C1', label=r'$\rm{SM}$')
    ax.text(0.05, 0.12, r'$\rm{cuu} = %.2f $' % cuu, fontsize=20, transform=ax.transAxes)
    ax.text(0.05, 0.05, r'$\rm{cug} = %.2f $' % cuGRe, fontsize=20, transform=ax.transAxes)
    #plt.title(r'$\rm{Analytic\;xsec\;in\;the\;EFT\;at\;cug=0.1\;and\;cuu=0}$')
    plt.yscale('log')
    plt.ylabel(r'$d\sigma/dm_{tt}\;\mathrm{[pb\:TeV^{-1}]}$')
    plt.legend(frameon=False, loc='best')
    plt.xlim((2 * mt, mtt_max))

    # ax3 = fig.add_axes([0.15, 0.1, 0.75, 0.20], ylim = (0.8*(y/y_sm).min(), 1.1*(y/y_sm).max()))
    # ax3.plot(x, y/y_sm, '-')

    plt.xlabel(r'$m_{tt}\;\mathrm{[TeV]}$')
    # plt.ylabel('BSM/SM')
    # plt.xlim((2*mt, mtt_max))

    #plt.show()
    fig.savefig(save_path)


def plot_likelihood_ratio():
    y_max = np.log(np.sqrt(s) / (2 * mt))
    y_min = -y_max

    # Important to include otypes = [np.float], else all the output is int by default
    vlikelihood_ratio = np.vectorize(likelihood_ratio, otypes=[np.float])

    fig = plt.figure()
    mtt_max = 2.500
    mtt_min = 2 * mt
    x = np.arange(mtt_min, mtt_max, 10 ** -3)
    y = np.arange(y_min, y_max, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = vlikelihood_ratio(Y, X, 10.0, NP=1)

    Z_mask = np.ma.masked_equal(Z, 0)
    mean = Z_mask.mean()
    std = Z_mask.std()

    im = plt.imshow(Z, cmap=plt.cm.Blues, aspect=(mtt_max - mtt_min) / (y_max - y_min),
                    extent=[mtt_min, mtt_max, y_min, y_max], vmin=mean - 3 * std, vmax=mean + 3 * std,
                    interpolation='quadric', origin='lower')
    plt.colorbar(im)

    plt.ylabel(r'Rapidity $Y = \log\sqrt{x_1/x_2}$')
    plt.xlabel(r'$m_{tt}\;\mathrm{[TeV]}$')
    plt.title('Likelihood ratio')

    # plt.title(r'$pdf(x|H_1(c=10^{%d}))$'%(-3+3))
    plt.show()
    fig.savefig('likelihood_ratio_EFT_Linear.pdf')


def plot_likelihood_ratio_1D(x, c):
    y = [1 / (1 + likelihood_ratio_1D(x_i, c)) for x_i in x]
    return np.array(y)

likelihood_ratio_1D_v = np.vectorize(likelihood_ratio_1D, otypes=[np.float])

def f_analytic(mtt, y, cuGRe, cuu):
    r = likelihood_ratio(y, mtt, cuGRe, cuu)
    return 1/(1+r)

def plot_f_ana(mtt_min, mtt_max, y_min, y_max, x_spacing, y_spacing, ctg, cuu):

    # Important to include otypes = [np.float], else all the output is int by default
    vf_ana = np.vectorize(f_analytic, otypes=[np.float])
    x = np.arange(mtt_min*10**-3, mtt_max*10**-3, x_spacing*10**-3)
    y = np.arange(y_min, y_max, y_spacing)
    xx, yy = np.meshgrid(x, y)
    Z = vf_ana(xx, yy, ctg, cuu)
    return Z


