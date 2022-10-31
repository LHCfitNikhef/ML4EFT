"""Module containing the analytical cross-sections top-quark pair production (parton level) in the SMEFT"""

from __future__ import division
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
from scipy.integrate import quad, dblquad
from scipy import integrate
import pylhe

from ml4eft.core.truth import vh_prod

try:
    import lhapdf

    p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
except ImportError:
    print("lhapdf not found: exact models will not be available")

mt = 0.17276
s = 14 ** 2
Gf = 0.000011663787
v = 1 / np.sqrt(Gf * np.sqrt(2)) * 10 ** -3
asQCD = 0.1179
LambdaSMEFT = 1
pb_convert = 3.894E2
yt = 1

# matplotlib.use('PDF')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
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

    def sigma_part_qq(self, hats, cuGRe, ctu8, order):
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

        # kappa_22 = (2.0 / 9.0) * sqrt * (hats - mt ** 2) / (48 * np.pi * LambdaSMEFT ** 4)
        # kappa_22 = sqrt * (hats - mt ** 2) / (48 * np.pi * LambdaSMEFT ** 4)
        kappa_22 = (2.0 / 9.0) * (hats * sqrt - mt ** 2 * sqrt) / (12 * 4 * np.pi * LambdaSMEFT ** 4)

        kappa_1 = - (8 * np.sqrt(2 * np.pi) * v * mt * asQCD ** (3 / 2) * sqrt) / (9 * hats * LambdaSMEFT ** 2)
        kappa_2 = asQCD * sqrt * (2 * mt ** 2 + hats) / (27 * hats * LambdaSMEFT ** 2)
        sm = (8 * np.pi * asQCD ** 2 * (2 * mt ** 2 + hats) * sqrt) / (27 * hats ** 2)

        if order is None:
            return sm
        elif order == 'lin':
            return sm + cuGRe * kappa_1 + ctu8 * kappa_2
        elif order == 'quad':
            return sm + cuGRe ** 2 * kappa_11 + ctu8 ** 2 * kappa_22
            # return kappa_22
            # return sm + ctu8 ** 2 * kappa_22

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

            me_sq_sm = 64 * asQCD ** 2 * np.pi ** 2 * (2 * mt ** 4 + T ** 2 + 2 * mt ** 2 * (S - T - U) + U ** 2) / (
                        9 * S ** 2)

            me_sq_kappa_1 = - (128 * np.sqrt(2) * asQCD ** (3 / 2) * mt * np.pi ** (3 / 2) * (
                        2 * mt ** 2 * (S - T - U) + (T + U) ** 2) * v) / (9 * S ** 2)
            me_sq_kappa_11 = (64 * asQCD * np.pi * (
                        4 * mt ** 2 * S * U - S * U * (S + U) + 2 * mt ** 2 * (T + U) * (T + 2 * U) + mt ** 4 * (
                            3 * S - 4 * (T + 2 * U))) * v ** 2) / (9 * S ** 2)

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
            p.xfxQ(5, x1, mu) * p.xfxQ(-5, x2, mu) +
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

    pdfs_up = np.sum(
        [p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_up])
    pdfs_down = np.sum(
        [p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in
         flavor_down])

    w_e = xsec.dsigma_part_gg_dpt(hats, pt, ctGRe, cut, order) * (p.xfxQ(21, x1, mu) * p.xfxQ(21, x2, mu))
    w_e += (xsec.dsigma_part_qq_dpt(hats, pt, ctGRe, cut, order)) * pdfs_up
    w_e += (xsec.dsigma_part_qq_dpt(hats, pt, ctGRe, 0, order)) * pdfs_down

    return w_e


v_weight = np.vectorize(weight, otypes=[np.float])
v_weight.excluded.add(4)

v_weight_pt = np.vectorize(weight_pt, otypes=[np.float])
v_weight_pt.excluded.add(5)


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


def dsigma_dmtt(mtt, c=None, order=None):
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
    dsigma_dmtt = integrate.fixed_quad(dsigma_dmtt_dy_vec, y_min, y_max, args=(mtt, c, order), n=100)[0]
    return dsigma_dmtt
