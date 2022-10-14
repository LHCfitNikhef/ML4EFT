#%%
import numpy as np
import lhapdf
from scipy import integrate

p = lhapdf.mkPDF("NNPDF31_nnlo_as_0118", 0)
s = 14 ** 2  # Collider COM energy squared [TeV^2]
mu = 91.188  # fact. scale for pdfs = Mz
mt = 0.17276  # top quark mass [TeV]
mw = 80.41900 * 10 ** -3  # w boson mass [TeV]
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125  # h boson mass [TeV]
Gf = 0.0000116639 * 10 ** 6
v = 1 / np.sqrt(Gf * np.sqrt(2))  # vev [TeV]
pb_convert = 3.894E2  # conversion factor to pb


def sigma_part_vh_up(hats, c, order):

    cHW, cHq3 = c

    pz2 = (hats ** 2 + mz ** 4 + mh ** 4 - 2 * hats * mz ** 2 - 2 * hats * mh ** 2 - 2 * mz ** 2 * mh ** 2) / (4 * hats)
    pz = np.sqrt(pz2)
    sth2 = 1 - (mw / mz) ** 2
    cth2 = 1 - sth2
    Vq = 1 / 2 - 4 / 3 * sth2
    Aq = 1 / 2
    xsec_sm = (Gf * mz ** 2) ** 2 / (9 * np.pi) * (Vq ** 2 + Aq ** 2) * pz / np.sqrt(hats) * (3 * mz ** 2 + pz2) / (
                (hats - mz ** 2) ** 2)

    LambdaSMEFT = 1
    xsec_lin_cHW = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * cth2 * Gf * mz ** 2 * (
                9 - 24 * sth2 + 32 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2)
    # xsec_lin_cHWB = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * np.sqrt(cth2) * np.sqrt(sth2) * Gf * mz ** 2 *(9 - 24 * sth2 + 32 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2 )
    xsec_lin_cHq3 = (mz ** 2 * pz * (-3 * mz ** 2 - pz2) * cth2 * Gf * mz ** 2 * sth2 * (4 * sth2 - 3)) / (
                27 * np.sqrt(2) * cth2 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats) * sth2)
    if order is None:
        return xsec_sm
    if order == 'lin':
        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3
    if order == 'quad':
        xsec_quad_cHq3_cHq3 = (mz ** 4 * pz * (3 * mz ** 2 + pz2)) / (
                    36 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats))

        xsec_quad_cHW_cHW = (cth2 ** 2 * mz ** 2 * pz * (3 * mz ** 2 + 2 * pz2) * np.sqrt(hats) * (
                    9 - 24 * sth2 + 32 * sth2 ** 2)) / (81 * np.pi * (mz ** 2 - hats) ** 2)

        xsec_quad_cHW_cHq3 = -(2 * cth2 * mz ** 4 * pz * np.sqrt(mz ** 2 + pz2) * (-3 + 4 * sth2)) / (
                    9 * np.pi * (mz ** 2 - hats) ** 2)


        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3 + \
               cHq3 ** 2 * xsec_quad_cHq3_cHq3 + cHW ** 2 * xsec_quad_cHW_cHW + cHW * cHq3 * xsec_quad_cHW_cHq3  # + cHWB * xsec_lin_cHWB / LambdaSMEFT

def sigma_part_vh_down(hats, c, order):
    cHW, cHq3 = c

    pz2 = (hats ** 2 + mz ** 4 + mh ** 4 - 2 * hats * mz ** 2 - 2 * hats * mh ** 2 - 2 * mz ** 2 * mh ** 2) / (4 * hats)
    pz = np.sqrt(pz2)
    sth2 = 1 - (mw / mz) ** 2
    cth2 = 1 - sth2
    Vq = - 1 / 2 + 2 / 3 * sth2
    Aq = -1 / 2
    xsec_sm = (Gf * mz ** 2) ** 2 / (9 * np.pi) * (Vq ** 2 + Aq ** 2) * pz / np.sqrt(hats) * (3 * mz ** 2 + pz2) / (
            (hats - mz ** 2) ** 2)

    LambdaSMEFT = 1
    xsec_lin_cHW = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * cth2 * Gf * mz ** 2 * sth2 * (
                9 - 12 * sth2 + 8 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2 * sth2)

    # xsec_lin_cHWB = (np.sqrt(2) * mz ** 2 * pz * np.sqrt(mz ** 2 + pz2) * np.sqrt(cth2) * np.sqrt(sth2) * Gf * mz ** 2 *(9 - 24 * sth2 + 32 * sth2 ** 2)) / (27 * np.pi * (mz ** 2 - hats) ** 2 )
    xsec_lin_cHq3 = (mz ** 2 * pz * (-3 * mz ** 2 - pz2) * cth2 * Gf * mz ** 2 * sth2 * (2 * sth2 - 3)) / (
                27 * np.sqrt(2) * cth2 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats) * sth2)

    if order is None:
        return xsec_sm
    if order == 'lin':
        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3
    if order == 'quad':
        xsec_quad_cHq3_cHq3 = (mz ** 4 * pz * (3 * mz ** 2 + pz2)) / (
                    36 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats))

        xsec_quad_cHW_cHW = (cth2 ** 2 * mz ** 2 * pz * (3 * mz ** 2 + 2 * pz2) * np.sqrt(hats) * (
                    9 - 12 * sth2 + 8 * sth2 ** 2)) / (81 * np.pi * (mz ** 2 - hats) ** 2)

        xsec_quad_cHW_cHq3 = -(2 * cth2 * mz ** 4 * pz * np.sqrt(mz ** 2 + pz2) * (-3 + 2 * sth2)) / (
                    9 * np.pi * (mz ** 2 - hats) ** 2)


        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3 + \
               cHq3 ** 2 * xsec_quad_cHq3_cHq3 + cHW ** 2 * xsec_quad_cHW_cHW + cHW * cHq3 * xsec_quad_cHW_cHq3  # + cHWB * xsec_lin_cHWB / LambdaSMEFT

def dsigma_part_dpt_vh_up(hats, ptv, c, order):
    cHW, cHq3 = c

    # minimum energy required to generate an event with transverse momentum ptv
    s_min = mh ** 2 + mz ** 2 + 2 * (ptv ** 2 + np.sqrt((mh ** 2 + ptv ** 2) * (mz ** 2 + ptv ** 2)))

    if hats < s_min:
        return 0

    sth2 = 1 - (mw / mz) ** 2
    cth2 = 1 - sth2

    S = hats

    pi = np.sqrt(S) / 2
    pf2 = (S ** 2 + mz ** 4 + mh ** 4 - 2 * S * mz ** 2 - 2 * S * mh ** 2 - 2 * mz ** 2 * mh ** 2) / (4 * S)

    pf = np.sqrt(pf2)

    theta = np.arcsin(ptv / pf)

    U = mz ** 2 - 2 * pi * (np.sqrt(mz ** 2 + pf2) - pf * np.cos(theta))
    T = mh ** 2 + mz ** 2 - S - U

    me_sq_uu_sm = (2 * Gf ** 2 * mz ** 4 * (9 - 24 * sth2 + 32 * sth2 ** 2) * (mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (
            27 * (mz ** 2 - S) ** 2)

    me_sq_uu_cHW = - 1 / (27 * (mz ** 2 - S) ** 2) * np.sqrt(2) * cth2 * Gf * mz ** 2 * (9 - 24 * sth2 + 32 * sth2 ** 2) * \
                   (-mz ** 6 + mh ** 4 * (mz ** 2 - T) + 3 * mz ** 4 * (-2 * S + U) + mh ** 2 * mz ** 2 * (-3 * T + U) -
                    S * T * (S + T + U) + mh ** 2 * T * (2 * S + T + U) + mz ** 2 * (- S ** 2 + (T - 2 * U) * (T + U) + S * (5 * T + U)))

    me_sq_uu_cHq3 = - (2 * np.sqrt(2) * Gf * mz ** 4 * (-3 + 4 * sth2) * (mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (9 * (mz ** 2 - S) ** 2)

    me_sq_uu = me_sq_uu_sm + cHW * me_sq_uu_cHW + cHq3 * me_sq_uu_cHq3

    dsigma_dpT_1 = 2 * np.pi * np.tan(theta) * me_sq_uu / (64 * np.pi ** 2 * S * pi)

    ######

    theta = np.pi - theta

    T = mz ** 2 - 2 * pi * (np.sqrt(mz ** 2 + pf ** 2) - pf * np.cos(theta))
    U = mh ** 2 + mz ** 2 - T - S

    me_sq_uu_sm = (2 * Gf ** 2 * mz ** 4 * (9 - 24 * sth2 + 32 * sth2 ** 2) * (
                mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (
                          27 * (mz ** 2 - S) ** 2)

    me_sq_uu_cHW = - 1 / (27 * (mz ** 2 - S) ** 2) * np.sqrt(2) * cth2 * Gf * mz ** 2 * (
                9 - 24 * sth2 + 32 * sth2 ** 2) * \
                   (-mz ** 6 + mh ** 4 * (mz ** 2 - T) + 3 * mz ** 4 * (-2 * S + U) + mh ** 2 * mz ** 2 * (-3 * T + U) -
                    S * T * (S + T + U) + mh ** 2 * T * (2 * S + T + U) + mz ** 2 * (
                                - S ** 2 + (T - 2 * U) * (T + U) + S * (5 * T + U)))

    me_sq_uu_cHq3 = - (2 * np.sqrt(2) * Gf * mz ** 4 * (-3 + 4 * sth2) * (mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (
                9 * (mz ** 2 - S) ** 2)

    me_sq_uu = me_sq_uu_sm + cHW * me_sq_uu_cHW + cHq3 * me_sq_uu_cHq3

    dsigma_dpT_2 = 2 * np.pi * np.abs(np.tan(theta)) * me_sq_uu / (64 * np.pi ** 2 * S * pi)

    return dsigma_dpT_1 + dsigma_dpT_2

def dsigma_part_dpt_vh_down(hats, ptv, c, order):
    cHW, cHq3 = c

    # minimum energy required to generate an event with transverse momentum ptv
    s_min = mh ** 2 + mz ** 2 + 2 * (ptv ** 2 + np.sqrt((mh ** 2 + ptv ** 2) * (mz ** 2 + ptv ** 2)))

    if hats < s_min:
        return 0

    sth2 = 1 - (mw / mz) ** 2
    cth2 = 1 - sth2

    S = hats

    pi = np.sqrt(S) / 2
    pf2 = (S ** 2 + mz ** 4 + mh ** 4 - 2 * S * mz ** 2 - 2 * S * mh ** 2 - 2 * mz ** 2 * mh ** 2) / (4 * S)

    pf = np.sqrt(pf2)

    theta = np.arcsin(ptv / pf)

    U = mz ** 2 - 2 * pi * (np.sqrt(mz ** 2 + pf2) - pf * np.cos(theta))
    T = mh ** 2 + mz ** 2 - S - U

    me_sq_dd_sm = (2 * Gf ** 2 * mz ** 4 * (9 - 12 * sth2 + 8 * sth2 ** 2) * (mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (
            27 * (mz ** 2 - S) ** 2)

    me_sq_dd_cHW = - 1 / (27 * (mz ** 2 - S) ** 2) * np.sqrt(2) * cth2 * Gf * mz ** 2 * (9 - 12 * sth2 + 8 * sth2 ** 2) * \
                   (-mz ** 6 + mh ** 4 * (mz ** 2 - T) + 3 * mz ** 4 * (-2 * S + U) + mh ** 2 * mz ** 2 * (-3 * T + U) -
                    S * T * (S + T + U) + mh ** 2 * T * (2 * S + T + U) + mz ** 2 * (- S ** 2 + (T - 2 * U) * (T + U) + S * (5 * T + U)))

    me_sq_dd_cHq3 = - (2 * np.sqrt(2) * Gf * mz ** 4 * (-3 + 2 * sth2) * (mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (9 * (mz ** 2 - S) ** 2)

    me_sq_dd = me_sq_dd_sm + cHW * me_sq_dd_cHW + cHq3 * me_sq_dd_cHq3

    dsigma_dpT_1 = 2 * np.pi * np.tan(theta) * me_sq_dd / (64 * np.pi ** 2 * S * pi)

    ######

    theta = np.pi - theta

    T = mz ** 2 - 2 * pi * (np.sqrt(mz ** 2 + pf ** 2) - pf * np.cos(theta))
    U = mh ** 2 + mz ** 2 - T - S

    me_sq_dd_sm = (2 * Gf ** 2 * mz ** 4 * (9 - 12 * sth2 + 8 * sth2 ** 2) * (mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (
            27 * (mz ** 2 - S) ** 2)

    me_sq_dd_cHW = - 1 / (27 * (mz ** 2 - S) ** 2) * np.sqrt(2) * cth2 * Gf * mz ** 2 * (9 - 12 * sth2 + 8 * sth2 ** 2) * \
                   (-mz ** 6 + mh ** 4 * (mz ** 2 - T) + 3 * mz ** 4 * (-2 * S + U) + mh ** 2 * mz ** 2 * (-3 * T + U) -
                    S * T * (S + T + U) + mh ** 2 * T * (2 * S + T + U) + mz ** 2 * (- S ** 2 + (T - 2 * U) * (T + U) + S * (5 * T + U)))

    me_sq_dd_cHq3 = - (2 * np.sqrt(2) * Gf * mz ** 4 * (-3 + 2 * sth2) * (mz ** 4 + mz ** 2 * (S - T - U) + T * U)) / (9 * (mz ** 2 - S) ** 2)

    me_sq_dd = me_sq_dd_sm + cHW * me_sq_dd_cHW + cHq3 * me_sq_dd_cHq3

    dsigma_dpT_2 = 2 * np.pi * np.abs(np.tan(theta)) * me_sq_dd / (64 * np.pi ** 2 * S * pi)

    return dsigma_dpT_1 + dsigma_dpT_2

def weight(sqrts, mu, x1, x2, c, order):
    """
    """
    hats = sqrts ** 2
    flavor_up = [2, 4]
    flavor_down = [1, 3, 5]

    # pdfs_up = np.sum(
    #     [p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) for pid in flavor_up])
    pdfs_up = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_up])
    pdfs_down = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_down])
    # pdfs_down = np.sum(
    #     [p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) for pid in
    #      flavor_down])

    weight_up = (sigma_part_vh_up(hats, c, order)) * pdfs_up
    weight_down = (sigma_part_vh_down(hats, c, order)) * pdfs_down
    return weight_down + weight_up

def weight_pt(sqrts, ptv, mu, x1, x2, c, order):
    """
    """
    hats = sqrts ** 2
    flavor_up = [2, 4]
    flavor_down = [1, 3, 5]

    pdfs_up = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_up])
    pdfs_down = np.sum([p.xfxQ(pid, x1, mu) * p.xfxQ(-pid, x2, mu) + p.xfxQ(-pid, x1, mu) * p.xfxQ(pid, x2, mu) for pid in flavor_down])

    weight_up = (dsigma_part_dpt_vh_up(hats, ptv, c, order)) * pdfs_up
    weight_down = (dsigma_part_dpt_vh_down(hats, ptv, c, order)) * pdfs_down
    return weight_down + weight_up

def dsigma_dmvh_dy_dpt(y, mvh, ptv, c, order):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """

    if mvh == mz + mh: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mvh):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mvh / np.sqrt(s) * np.exp(y)
        x2 = mvh / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mvh / s * v_weight_pt(mvh, ptv, 91.188, x1, x2, c, order) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0

def dsigma_dmvh_dy(y, mvh, c=None, order=None):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if c is None:
        c = np.zeros(2)

    if mvh == mz + mh: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mvh):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mvh / np.sqrt(s) * np.exp(y)
        x2 = mvh / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mvh / s * v_weight(mvh, 91.188, x1, x2, c, order) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0

def dsigma_dmvh(mvh, c, order):

    y_min, y_max = -0.5 * np.log(s / mvh), 0.5 * np.log(s / mvh)
    dsigma_dmvh = integrate.fixed_quad(dsigma_dmvh_dy_vec, y_min, y_max, args=(mvh, c, order), n=10)[0]
    return dsigma_dmvh

def sigma_bin(bins, cHW, cHq3, lin=False, quad=False):
    sigma_i = []
    for i in range(len(bins) - 1):
        temp = integrate.fixed_quad(dsigma_dmvh_vec, bins[i], bins[i + 1], args=(cHW, cHq3, lin, quad), n=400)[0]
        sigma_i.append(temp)
    sigma_i = np.array(sigma_i)
    return sigma_i

def findCoeff(bins):
    sm = sigma_bin(bins, cHW=0, cHq3=0, lin=True)
    c1_lin = (sigma_bin(bins, cHW=100, cHq3=0, lin=True, quad=False) - sm) / 100
    c2_lin = (sigma_bin(bins, cHW=0, cHq3=100, lin=True, quad=False) - sm) / 100

    c1_quad = (sigma_bin(bins, cHW=100, cHq3=0, lin=False, quad=True) - (sm + 100 * c1_lin)) / 100 ** 2
    c2_quad = (sigma_bin(bins, cHW=0, cHq3=100, lin=False, quad=True) - (sm + 100 * c2_lin)) / 100 ** 2

    c1_c2 = (sigma_bin(bins, cHW=100, cHq3=100, lin=False, quad=True) - (
                sm + 100 * c1_lin + 100 ** 2 * c1_quad + 100 * c2_lin + 100 ** 2 * c2_quad)) / 100 ** 2

    coeff = np.array([sm, c1_lin, c1_quad, c2_lin, c2_quad, c1_c2])

    return coeff

def nu_i(a, cHW, cHq3, luminosity, lin=False, quad=False):
    if lin:
        eft_point = np.array([1, cHW, 0, cHq3, 0, 0])
    if quad:
        eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
    xsec = np.einsum('ij,i', a, eft_point)
    nu = xsec * luminosity
    return nu

v_weight = np.vectorize(weight, otypes=[np.float])
v_weight.excluded.add(4)
v_weight_pt = np.vectorize(weight_pt, otypes=[np.float])
dsigma_dmvh_dy_vec = np.vectorize(dsigma_dmvh_dy, otypes=[np.float])
dsigma_dmvh_vec = np.vectorize(dsigma_dmvh, otypes=[np.float])