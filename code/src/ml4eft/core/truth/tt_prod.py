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

from ml4eft.core.truth import vh_prod

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
mt = 0.17276  # 172 #Top quark mass plot_mg5_ana_mttin GeV
s = 14 ** 2  # (14*10**3)**2#GeV^2
Gf = 0.000011663787
v = 1 / np.sqrt(Gf * np.sqrt(2)) * 10 ** -3  # 1/np.sqrt(Gf*np.sqrt(2))
asQCD = 0.1179
LambdaSMEFT = 1  # 10**3
pb_convert = 3.894E2
yt = 1#0.9922828427689138

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

# Partonic cross sections

class crossSectionSMEFT:
    """
    A class that contains all EFT cross sections...

    """

    def sigma_part_gg(self, hats, cuGRe, cuu, order):  # TODO: fix the gluon gluon contribution
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

        if order is None:
            return sm
        elif order == 'lin':
            return sm + cuGRe * kappa_1
        elif order == 'quad':
            return sm + cuGRe ** 2 * kappa_11


    def sigma_part_qq(self, hats, cuGRe, cuu, order):
        if np.sqrt(hats) == 2 * mt:
            return 0

        sqrt = np.sqrt(1 - 4 * mt ** 2 / hats)
        kappa_11 = sqrt * (8 * np.pi * v ** 2 * yt ** 2 * asQCD * (8 * mt ** 2 + hats)) / (
                    108 * np.pi * LambdaSMEFT ** 4 * hats)
        kappa_22 = sqrt * ((hats - mt ** 2)) / (48 * np.pi * LambdaSMEFT ** 4 )
        kappa_1 = - (8 * np.sqrt(2 * np.pi) * v * mt * asQCD ** (3 / 2) * sqrt) / (9 * hats * LambdaSMEFT ** 2)
        sm = (8 * np.pi * asQCD ** 2 * (2 * mt ** 2 + hats) * sqrt) / (27 * hats ** 2)

        if order is None:
            return sm
        elif order == 'lin':
            return sm + cuGRe * kappa_1
        elif order == 'quad':
            return sm + cuGRe ** 2 * kappa_11 + cuu ** 2 * kappa_22

    def dsigma_part_qq_dpt(self, hats, pt, cuGRe, cuu, order):

        # minimum energy required to generate an event with transverse momentum ptv
        s_min = 4 * mt ** 2 + 4 * pt ** 2

        if hats < s_min:
            return 0

        S = hats

        pi = np.sqrt(S) / 2
        pf2 = (S - 4 * mt ** 2) / 4

        pf = np.sqrt(pf2)

        def me_sq(theta):
            U = mt ** 2 - 2 * pi * (np.sqrt(mt ** 2 + pf2) - pf * np.cos(theta))
            T = 2 * mt ** 2 - S - U

            me_sq_sm = 64 * asQCD ** 2 * np.pi ** 2 * (2 * mt ** 4 + T ** 2 + 2 * mt ** 2 * (S-T-U) + U ** 2) / (9 * S ** 2)

            me_sq_kappa_1 = - (128 * np.sqrt(2) * asQCD ** (3/2) * mt * np.pi ** (3/2) * (2 * mt ** 2 * (S-T-U) + (T+U) ** 2) * v)/(9 * S ** 2)
            me_sq_kappa_11 = (64 * asQCD * np.pi * (4 * mt ** 2 * S * U - S * U * (S + U) + 2 * mt ** 2 * (T + U) * (T + 2 * U) + mt ** 4  * (3 * S - 4 * (T + 2 * U))) * v ** 2)/(9 * S ** 2)

            me_sq_kappa_22 = (U - mt ** 2) ** 2

            if order is None:
                me_sq = me_sq_sm
            elif order == 'lin':
                me_sq =  me_sq_sm + cuGRe * me_sq_kappa_1
            elif order == 'quad':
                me_sq =  me_sq_sm + cuGRe ** 2 * me_sq_kappa_11 + cuu ** 2 * me_sq_kappa_22

            return me_sq

        theta = np.arcsin(pt / pf)
        me_sq_theta = me_sq(theta)
        me_sq_pi_theta = me_sq(np.pi - theta)

        dsigma_dpT_1 = 2 * np.pi * np.tan(theta) * me_sq_theta / (64 * np.pi ** 2 * S * pi)
        dsigma_dpT_2 = 2 * np.pi * np.abs(np.tan(theta)) * me_sq_pi_theta / (64 * np.pi ** 2 * S * pi)


        return dsigma_dpT_1 + dsigma_dpT_2


    def dsigma_part_gg_dpt(self, hats, pt, cuGRe, cuu, order):

        # minimum energy required to generate an event with transverse momentum ptv
        s_min = 4 * mt ** 2 + 4 * pt ** 2

        if hats < s_min:
            return 0

        S = hats

        pi = np.sqrt(S) / 2
        pf2 = (S - 4 * mt ** 2) / 4

        pf = np.sqrt(pf2)

        def me_sq(theta):

            U = mt ** 2 - 2 * pi * (np.sqrt(mt ** 2 + pf2) - pf * np.cos(theta))
            T = 2 * mt ** 2 - S - U

            me_sq_sm = -1 / (3 * S ** 2 * (mt ** 2 - T) ** 2 * (mt ** 2 - U) ** 2) * 2 * asQCD ** 2 * np.pi ** 2 * (
                        -36 * mt ** 10 * T -
                        mt ** 2 * (S * T * (15 * S ** 3 - 35 * S ** 2 * T - 84 * S * T ** 2 + 14 * T ** 3) + (-S ** 4 +
                                                                                                              27 * S ** 3 * T - 126 * S ** 2 * T ** 2 + 99 * S * T ** 3 + 72 * T ** 4) * U + (
                                               30 * S ** 3 +
                                               184 * S ** 2 * T + 119 * S * T ** 2 + 72 * T ** 3) * U ** 2 +
                                   S * (51 * S + 292 * T) * U ** 3 + 36 * (S + T) * U ** 4) +
                        2 * mt ** 8 * (
                                    7 * S ** 2 + S * (-31 * T + 101 * U) + 9 * (6 * T ** 2 + 3 * T * U + U ** 2)) +
                        mt ** 6 * (S ** 2 * (230 * T - 201 * U) + S * (20 * T ** 2 - 169 * T * U - 411 * U ** 2) -
                                   36 * (3 * T ** 3 + 5 * T ** 2 * U + T * U ** 2 + U ** 3)) +
                        T * (S ** 4 * (8 * T - U) + S ** 3 * U * (-3 * T + 14 * U) +
                             18 * T * U ** 2 * (2 * T ** 2 - T * U + U ** 2) +
                             S ** 2 * (-8 * T ** 3 - 20 * T ** 2 * U + 34 * T * U ** 2 + 35 * U ** 3) +
                             S * U * (14 * T ** 3 + 43 * T ** 2 * U + 47 * T * U ** 2 + 36 * U ** 3)) +
                        mt ** 4 * (7 * S ** 4 + S ** 3 * (-51 * T + 62 * U) +
                                   S ** 2 * (-240 * T ** 2 - 81 * T * U + 262 * U ** 2) +
                                   S * (56 * T ** 3 + 52 * T ** 2 * U + 487 * T * U ** 2 + 245 * U ** 3) +
                                   18 * (2 * T ** 4 + 11 * T ** 3 * U + 3 * T ** 2 * U ** 2 + 3 * T * U ** 3 + U ** 4)))

            me_sq_kappa_1 = (1 / (3 * S ** 2 * (mt ** 2 - T) ** 2 * (mt ** 2 - U) ** 2)) * np.sqrt(2) * asQCD ** (
                    3 / 2) * mt * np.pi ** (
                                    3 / 2) * (288 * mt ** 12 + 12 * mt ** 10 * (79 * S - 84 * T - 72 * U) +
                                              72 * T ** 2 * U ** 2 * (T + U) * (2 * T + U) + S ** 4 * (
                                                          64 * T ** 2 + 15 * T * U + 32 * U ** 2) +
                                              2 * S * T * U * (
                                                          4 * T ** 3 + 175 * T ** 2 * U + 143 * T * U ** 2 + 8 * U ** 3) +
                                              2 * S ** 3 * (8 * T ** 3 + 2 * T ** 2 * U + 85 * T * U ** 2 + 20 * U ** 3) +
                                              S ** 2 * (
                                                          -48 * T ** 4 - 179 * T ** 3 * U + 262 * T ** 2 * U ** 2 + 83 * T * U ** 3 + 8 * U ** 4) +
                                              2 * mt ** 8 * (-734 * S ** 2 - 9 * S * (119 * T + 55 * U) +
                                                             36 * (18 * T ** 2 + 39 * T * U + 13 * U ** 2)) +
                                              mt ** 6 * (183 * S ** 3 + S ** 2 * (2971 * T + 1307 * U) +
                                                         2 * S * (751 * T ** 2 + 876 * T * U - 103 * U ** 2) -
                                                         144 * (
                                                                     5 * T ** 3 + 23 * T ** 2 * U + 19 * T * U ** 2 + 3 * U ** 3)) +
                                              mt ** 4 * (111 * S ** 4 + S ** 3 * (-267 * T + 131 * U) -
                                                         2 * S ** 2 * (1157 * T ** 2 + 718 * T * U + 138 * U ** 2) +
                                                         12 * S * (
                                                                     -25 * T ** 3 - 60 * T ** 2 * U + 77 * T * U ** 2 + 22 * U ** 3) +
                                                         72 * (
                                                                     2 * T ** 4 + 23 * T ** 3 * U + 39 * T ** 2 * U ** 2 + 15 * T * U ** 3 + U ** 4)) +
                                              mt ** 2 * (S ** 3 * (T - 2 * U) * (236 * T + 41 * U) - S ** 4 * (
                                143 * T + 79 * U) -
                                                         144 * T * U * (
                                                                     2 * T ** 3 + 8 * T ** 2 * U + 6 * T * U ** 2 + U ** 3) +
                                                         S ** 2 * (
                                                                     659 * T ** 3 + 900 * T ** 2 * U - 562 * T * U ** 2 + 93 * U ** 3) -
                                                         2 * S * (
                                                                     4 * T ** 4 + 25 * T ** 3 * U + 534 * T ** 2 * U ** 2 + 275 * T * U ** 3 + 8 * U ** 4))) * v

            me_sq_kappa_11 = -(1 / (3 * S ** 2 * (mt ** 2 - T) ** 2 * (mt ** 2 - U) ** 2)) * asQCD * np.pi * (
                        864 * mt ** 14 + 4 * mt ** 12 * (89 * S - 612 * T - 576 * U) +
                        mt ** 10 * (-1440 * S ** 2 + S * (-778 * T + 392 * U) +
                                    72 * (34 * T ** 2 + 87 * T * U + 29 * U ** 2)) -
                        mt ** 8 * (173 * S ** 3 + S ** 2 * (-3033 * T + 76 * U) +
                                   S * (-374 * T ** 2 + 867 * T * U + 1469 * U ** 2) +
                                   144 * (7 * T ** 3 + 41 * T ** 2 * U + 37 * T * U ** 2 + 5 * U ** 3)) +
                        S * T * U * (4 * S ** 4 + S ** 3 * (3 * T + 28 * U) +
                                     S ** 2 * (-59 * T ** 2 + 40 * T * U - 11 * U ** 2) +
                                     S * (-64 * T ** 3 + 46 * T ** 2 * U + 76 * T * U ** 2 - 71 * U ** 3) - (T + U) * (
                                                 6 * T ** 3 -
                                                 31 * T ** 2 * U - 38 * T * U ** 2 + 36 * U ** 3)) +
                        mt ** 6 * (280 * S ** 4 + S ** 3 * (231 * T + 1297 * U) +
                                   S ** 2 * (-2530 * T ** 2 + 1161 * T * U + 1151 * U ** 2) +
                                   S * (163 * T ** 3 + 824 * T ** 2 * U + 2643 * T * U ** 2 + 958 * U ** 3) +
                                   72 * (2 * T ** 4 + 31 * T ** 3 * U + 63 * T ** 2 * U ** 2 + 23 * T * U ** 3 + U ** 4)) +
                        mt ** 4 * (4 * S ** 5 - S ** 4 * (309 * T + 220 * U) -
                                   S ** 3 * (37 * T ** 2 + 1819 * T * U + 711 * U ** 2) +
                                   S ** 2 * (617 * T ** 3 - 494 * T ** 2 * U - 2201 * T * U ** 2 - 610 * U ** 3) -
                                   144 * T * U * (2 * T ** 3 + 10 * T ** 2 * U + 8 * T * U ** 2 + U ** 3) -
                                   S * (121 * T ** 4 + 439 * T ** 3 * U + 1406 * T ** 2 * U ** 2 + 1233 * T * U ** 3 +
                                        273 * U ** 4)) +
                        mt ** 2 * (-4 * S ** 5 * (T + U) + 72 * T ** 2 * U ** 2 * (T + U) * (2 * T + U) +
                                   S ** 4 * (157 * T ** 2 - 39 * T * U + 100 * U ** 2) +
                                   S ** 3 * (163 * T ** 3 + 437 * T ** 2 * U + 407 * T * U ** 2 + 235 * U ** 3) +
                                   S ** 2 * (
                                               8 * T ** 4 + 313 * T ** 3 * U + 356 * T ** 2 * U ** 2 + 558 * T * U ** 3 + 167 * U ** 4) +
                                   S * (
                                               6 * T ** 5 + 96 * T ** 4 * U + 207 * T ** 3 * U ** 2 + 206 * T ** 2 * U ** 3 + 271 * T * U ** 4 +
                                               36 * U ** 5))) * v ** 2

            if order is None:
                me_sq = me_sq_sm
            elif order == 'lin':
                me_sq =  me_sq_sm + cuGRe * me_sq_kappa_1
            elif order == 'quad':
                me_sq =  me_sq_sm + cuGRe ** 2 * me_sq_kappa_11

            return me_sq

        theta = np.arcsin(pt / pf)

        me_sq_theta = me_sq(theta)
        me_sq_pi_theta = me_sq(np.pi - theta)

        dsigma_dpT_1 = 2 * np.pi * np.tan(theta) * me_sq_theta / (64 * np.pi ** 2 * S * pi)
        dsigma_dpT_2 = 2 * np.pi * np.abs(np.tan(theta)) * me_sq_pi_theta / (64 * np.pi ** 2 * S * pi)

        return dsigma_dpT_1 + dsigma_dpT_2



xsec = crossSectionSMEFT()

def weight(sqrts, mu, x1, x2, c, order):
    """
    NP parameter: order in the EFT
    order parameter: work at one specific order
    """

    cuGRe, cuu = c
    hats = sqrts ** 2
    w_ii = (xsec.sigma_part_gg(hats, cuGRe, cuu, order)) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
    w_ii += (xsec.sigma_part_qq(hats, cuGRe, 0, order)) * (
                p.xfxQ(1, x1, mu) * p.xfxQ(-1, x2, mu) +
                p.xfxQ(1, x2, mu) * p.xfxQ(-1, x1, mu) +
                p.xfxQ(3, x1, mu) * p.xfxQ(-3, x2, mu) +
                p.xfxQ(3, x2, mu) * p.xfxQ(-3, x1, mu) +
                p.xfxQ(5, x1,mu) * p.xfxQ(-5, x2, mu) +
                p.xfxQ(5, x2, mu) * p.xfxQ(-5, x1, mu)
    )

    w_ii += (xsec.sigma_part_qq(hats, cuGRe, cuu, order)) * (
            p.xfxQ(2, x1, mu) * p.xfxQ(-2, x2, mu) +
            p.xfxQ(2, x2, mu) * p.xfxQ(-2, x1, mu) +
            p.xfxQ(4, x1, mu) * p.xfxQ(-4, x2, mu) +
            p.xfxQ(4, x2, mu) * p.xfxQ(-4, x1, mu)
    )

    return w_ii


def weight_pt(sqrts, pt, mu, x1, x2, c, order):
    """
    """
    cuGRe, cuu = c
    hats = sqrts ** 2
    flavor_up = [2, 4]
    flavor_down = [1, 3, 5]

    pdfs_up = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_up])
    pdfs_down = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_down])

    weight = xsec.dsigma_part_gg_dpt(hats, pt, cuGRe, cuu, order) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
    weight += (xsec.dsigma_part_qq_dpt(hats, pt, cuGRe, cuu, order)) * pdfs_up
    weight += (xsec.dsigma_part_qq_dpt(hats, pt, cuGRe, 0, order)) * pdfs_down

    return weight

v_weight = np.vectorize(weight, otypes=[np.float])
v_weight.excluded.add(4)

v_weight_pt = np.vectorize(weight_pt, otypes=[np.float])
v_weight_pt.excluded.add(5)

def dsigma_dmtt_dy_dpt(y, mtt, pt, c=None, order=None):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if c is None:
        c = np.zeros(2)
    if mtt == 2 * mt: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mtt):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mtt / np.sqrt(s) * np.exp(y)
        x2 = mtt / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mtt / s * v_weight_pt(mtt, pt, 91.188, x1, x2, c, order) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0


def dsigma_dmtt_dy(y, mtt, c=None, order=None):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """

    if c is None:
        c = np.zeros(2)
    if mtt == 2 * mt: return 0  # if at threshold return zero
    if np.abs(y) < np.log(np.sqrt(s) / mtt):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mtt / np.sqrt(s) * np.exp(y)
        x2 = mtt / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mtt / s * v_weight(mtt, 91.188, x1, x2, c, order) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0


dsigma_dmtt_dy_vec = np.vectorize(dsigma_dmtt_dy, otypes=[np.float])
dsigma_dmtt_dy_vec.excluded.add(2)


def dsigma_dmtt(mtt, c, order):
    y_min, y_max = -0.5 * np.log(s / mtt), 0.5 * np.log(s / mtt)
    dsigma_dmtt = integrate.fixed_quad(dsigma_dmtt_dy_vec, y_min, y_max, args=(mtt, c, order), n=10)[0]
    return dsigma_dmtt

#%%

# remove below?



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


def plot_likelihood_ratio_1D(x, cHW, cHq3, lin=False, quad=False):
    y = [1 / (1 + likelihood_ratio_1D(x_i, cHW, cHq3, lin=lin, quad=quad)) for x_i in x]
    return np.array(y)


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


