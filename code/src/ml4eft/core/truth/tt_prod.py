"""Module containing the analytical cross-sections top-quark pair production (parton level) in the SMEFT"""

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
mt = 0.17276
s = 14 ** 2
Gf = 0.000011663787
v = 1 / np.sqrt(Gf * np.sqrt(2)) * 10 ** -3
asQCD = 0.1179
LambdaSMEFT = 1
pb_convert = 3.894E2
yt = 1

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

class crossSectionSMEFT:
    """
    Class containing the analytical differential cross-sections in the SMEFT

    """

    def sigma_part_gg(self, hats, ctGRe, cut, order):
        """
        Gluon initiated contribution to the partonic cross-section of :math:`t\\bar{t}`-production

        Parameters
        ----------
        hats: float
            partonic center of mass energy squared
        ctGRe: float
            EFT parameter :math:`c_{tG}`
        cut: float
            EFT parameter :math:`c_{ut}`
        order: str
            Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

        Returns
        -------
        float
            Partonic cross-section
        """
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
            return sm + ctGRe * kappa_1
        elif order == 'quad':
            return sm + ctGRe ** 2 * kappa_11


    def sigma_part_qq(self, hats, cuGRe, cut, order):
        """
        Quark-quark initiated contribution to the partonic cross-section of :math:`t\\bar{t}`-production

        Parameters
        ----------
        hats: float
            partonic center of mass energy squared
        ctGRe: float
            EFT parameter :math:`c_{tG}`
        cut: float
            EFT parameter :math:`c_{ut}`
        order: str
            Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

        Returns
        -------
        float
            Partonic cross-section
        """

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
            return sm + cuGRe ** 2 * kappa_11 + cut ** 2 * kappa_22

    def dsigma_part_qq_dpt(self, hats, pt, ctGRe, cut, order):
        """
        Quark-quark initiated contribution to the partonic cross-section of :math:`t\\bar{t}`-production, keeping
        info about the scattering angle

        Parameters
        ----------
        hats: float
            partonic center of mass energy squared
        ctGRe: float
            EFT parameter :math:`c_{tG}`
        cut: float
            EFT parameter :math:`c_{ut}`
        order: str
            Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

        Returns
        -------
        float
            Partonic differential cross-section in :math:`p_T^t`
        """

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
                me_sq = me_sq_sm + ctGRe * me_sq_kappa_1
            elif order == 'quad':
                me_sq = me_sq_sm + ctGRe ** 2 * me_sq_kappa_11 + cut ** 2 * me_sq_kappa_22

            return me_sq

        theta = np.arcsin(pt / pf)
        me_sq_theta = me_sq(theta)
        me_sq_pi_theta = me_sq(np.pi - theta)

        dsigma_dpT_1 = 2 * np.pi * np.tan(theta) * me_sq_theta / (64 * np.pi ** 2 * S * pi)
        dsigma_dpT_2 = 2 * np.pi * np.abs(np.tan(theta)) * me_sq_pi_theta / (64 * np.pi ** 2 * S * pi)


        return dsigma_dpT_1 + dsigma_dpT_2


    def dsigma_part_gg_dpt(self, hats, pt, ctGRe, cut, order):
        """
        Gluon initiated contribution to the partonic cross-section of :math:`t\\bar{t}`-production, keeping
        info about the scattering angle

        Parameters
        ----------
        hats: float
            partonic center of mass energy squared
        ctGRe: float
            EFT parameter :math:`c_{tG}`
        cut: float
            EFT parameter :math:`c_{ut}`
        order: str
            Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

        Returns
        -------
        float
            Partonic differential cross-section in :math:`p_T^t`
        """

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
                me_sq = me_sq_sm + ctGRe * me_sq_kappa_1
            elif order == 'quad':
                me_sq = me_sq_sm + ctGRe ** 2 * me_sq_kappa_11

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
    Convolution of the partonic-cross section with the PDFs

    Parameters
    ----------
    sqrts: float
        partonic center of mass energy
    mu: float
        Factorization scale
    x1: float 
        Momentum fraction carried by parton 1
    x2: float
        Momentum fraction carried by parton 2
    c: array_like
        EFT parameters :math:`c_{tG}` and :math:`c_{ut}`
    order: str 
        Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

    Returns
    -------
    float
        Partonic cross-section convoluted with the PDFs
    """
    ctGRe, cut = c
    hats = sqrts ** 2
    w_e = (xsec.sigma_part_gg(hats, ctGRe, cut, order)) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
    w_e += (xsec.sigma_part_qq(hats, ctGRe, 0, order)) * (
                p.xfxQ(1, x1, mu) * p.xfxQ(-1, x2, mu) +
                p.xfxQ(1, x2, mu) * p.xfxQ(-1, x1, mu) +
                p.xfxQ(3, x1, mu) * p.xfxQ(-3, x2, mu) +
                p.xfxQ(3, x2, mu) * p.xfxQ(-3, x1, mu) +
                p.xfxQ(5, x1,mu) * p.xfxQ(-5, x2, mu) +
                p.xfxQ(5, x2, mu) * p.xfxQ(-5, x1, mu)
    )

    w_e += (xsec.sigma_part_qq(hats, ctGRe, cut, order)) * (
            p.xfxQ(2, x1, mu) * p.xfxQ(-2, x2, mu) +
            p.xfxQ(2, x2, mu) * p.xfxQ(-2, x1, mu) +
            p.xfxQ(4, x1, mu) * p.xfxQ(-4, x2, mu) +
            p.xfxQ(4, x2, mu) * p.xfxQ(-4, x1, mu)
    )

    return w_e


def weight_pt(sqrts, pt, mu, x1, x2, c, order):
    """
    Convolution of the partonic-cross section with the PDFs, keeping info about the scattering angle

    Parameters
    ----------
    sqrts: float
        partonic center of mass energy
    pt: float
        Transverse momentum of the top
    mu: float
        Factorization scale
    x1: float
        Momentum fraction carried by parton 1
    x2: float
        Momentum fraction carried by parton 2
    c: array_like
        EFT parameters :math:`c_{tG}` and :math:`c_{ut}`
    order: str
        Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

    Returns
    -------
    float
        Partonic cross-section convoluted with the PDFs
    """
   
    ctGRe, cut = c
    hats = sqrts ** 2
    flavor_up = [2, 4]
    flavor_down = [1, 3, 5]

    pdfs_up = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_up])
    pdfs_down = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_down])

    w_e = xsec.dsigma_part_gg_dpt(hats, pt, ctGRe, cut, order) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
    w_e += (xsec.dsigma_part_qq_dpt(hats, pt, ctGRe, cut, order)) * pdfs_up
    w_e += (xsec.dsigma_part_qq_dpt(hats, pt, ctGRe, 0, order)) * pdfs_down

    return w_e

v_weight = np.vectorize(weight, otypes=[np.float])
v_weight.excluded.add(4)

v_weight_pt = np.vectorize(weight_pt, otypes=[np.float])
v_weight_pt.excluded.add(5)

def dsigma_dmtt_dy_dpt(y, mtt, pt, c=None, order=None):
    """
    Returns the triple differential cross-section in :math:`Y, m_{t\\bar{t}}, p_T^{t}`. Units are :math:`pb^{-1}`

    Parameters
    ----------
    y: float
        Rapidity of the top-quark pair
    mtt: float
        Invariant mass of the top-quark pair in TeV
    pt: float
        Transverse momentum of the top in TeV
    c: array_like, optional
        EFT parameters :math:`c_{tG}` and :math:`c_{ut}`. Set to zero (SM) by default.
    order: str, optional
        Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM.

    Returns
    -------
    float
        Triple differential cross-section in :math:`Y, m_{t\\bar{t}}, p_T^{t}`
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
    Returns the double differential cross-section in :math:`Y, m_{t\\bar{t}}`. Units are :math:`pb^{-1}`

    Parameters
    ----------
    y: float
        Rapidity of the top-quark pair
    mtt: float
        Invariant mass of the top-quark pair in TeV
    c: array_like, optional
        EFT parameters :math:`c_{tG}` and :math:`c_{ut}`. Set to zero (SM) by default.
    order: str, optinal
        Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

    Returns
    -------
    float
        Double differential cross-section in :math:`Y, m_{t\\bar{t}}`
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
    """
    Returns the single differential cross-section in :math:`m_{t\\bar{t}}`. Units are :math:`pb^{-1}`

    Parameters
    ----------
    mtt: float
        Invariant mass of the top-quark pair in TeV
    c: array_like, optional
        EFT parameters :math:`c_{tG}` and :math:`c_{ut}`. Set to zero (SM) by default.
    order: str, optinal
        Order of the EFT expansion, choose between 'lin' and 'quad', or leave `None` for just the SM

    Returns
    -------
    float
        Single differential cross-section in :math:`m_{t\\bar{t}}`
   """

    y_min, y_max = -0.5 * np.log(s / mtt), 0.5 * np.log(s / mtt)
    dsigma_dmtt = integrate.fixed_quad(dsigma_dmtt_dy_vec, y_min, y_max, args=(mtt, c, order), n=10)[0]
    return dsigma_dmtt



















