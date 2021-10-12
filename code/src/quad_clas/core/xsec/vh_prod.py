#%%
import numpy as np
import lhapdf
from scipy import integrate

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
s = 14 ** 2  # Collider COM energy squared [TeV^2]
mu = 91.188  # fact. scale for pdfs = Mz
mt = 0.17276  # top quark mass [TeV]
mw = 80.41900 * 10 ** -3  # w boson mass [TeV]
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125  # h boson mass [TeV]
Gf = 0.0000116639 * 10 ** 6
v = 1 / np.sqrt(Gf * np.sqrt(2))  # vev [TeV]
pb_convert = 3.894E2  # conversion factor to pb


def sigma_part_vh_up(hats, c1, c2, c3, lin, quad):
    cHW = c1
    cHq3 = c2
    cHB = c3
    pz2 = (hats ** 2 + mz ** 4 + mh ** 4 - 2 * hats * mz ** 2 - 2 * hats * mh ** 2 - 2 * mz ** 2 * mh ** 2) / (4 * hats)
    pz = np.sqrt(pz2)
    sth2 = 1 - (mw / mz) ** 2
    cth2 = 1 - sth2
    sth = np.sqrt(sth2)
    cht = np.sqrt(cth2)
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

    xsec_lin_cHB = xsec_lin_cHW * ( sth2 / cth2)


    if lin:
        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3 + cHB * xsec_lin_cHB
    if quad:
        xsec_quad_cHq3_cHq3 = (mz ** 4 * pz * (3 * mz ** 2 + pz2)) / (
                    36 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats))

        xsec_quad_cHW_cHW = (cth2 ** 2 * mz ** 2 * pz * (3 * mz ** 2 + 2 * pz2) * np.sqrt(hats) * (
                    9 - 24 * sth2 + 32 * sth2 ** 2)) / (81 * np.pi * (mz ** 2 - hats) ** 2)

        xsec_quad_cHW_cHq3 = -(2 * cth2 * mz ** 4 * pz * np.sqrt(mz ** 2 + pz2) * (-3 + 4 * sth2)) / (
                    9 * np.pi * (mz ** 2 - hats) ** 2)

        xsec_quad_cHB_cHB = xsec_quad_cHW_cHW * (sth2 ** 2 /cth2 ** 2)

        xsec_quad_cHW_cHB = 2 * xsec_quad_cHW_cHW * ((cth2 * sth2) /cth2 ** 2)


        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3 + \
               cHq3 ** 2 * xsec_quad_cHq3_cHq3 + cHW ** 2 * xsec_quad_cHW_cHW + cHW * cHq3 * xsec_quad_cHW_cHq3 + cHB ** 2 * xsec_quad_cHB_cHB + cHB * cHW * xsec_quad_cHW_cHB


def sigma_part_vh_down(hats, c1, c2, lin, quad):
    cHW = c1
    cHq3 = c2
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

    xsec_lin_cHB = xsec_lin_cHW * (sth2 / cth2)

    if lin:
        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3
    if quad:
        xsec_quad_cHq3_cHq3 = (mz ** 4 * pz * (3 * mz ** 2 + pz2)) / (
                    36 * np.pi * (mz ** 2 - hats) ** 2 * np.sqrt(hats))

        xsec_quad_cHW_cHW = (cth2 ** 2 * mz ** 2 * pz * (3 * mz ** 2 + 2 * pz2) * np.sqrt(hats) * (
                    9 - 12 * sth2 + 8 * sth2 ** 2)) / (81 * np.pi * (mz ** 2 - hats) ** 2)

        xsec_quad_cHW_cHq3 = -(2 * cth2 * mz ** 4 * pz * np.sqrt(mz ** 2 + pz2) * (-3 + 2 * sth2)) / (
                    9 * np.pi * (mz ** 2 - hats) ** 2)

        xsec_quad_cHB_cHB = xsec_quad_cHW_cHW * (sth2 ** 2 / cth2 ** 2)

        xsec_quad_cHW_cHB = 2 * xsec_quad_cHW_cHW * ((cth2 * sth2) / cth2 ** 2)

        return xsec_sm + cHW * xsec_lin_cHW + cHq3 * xsec_lin_cHq3 + \
               cHq3 ** 2 * xsec_quad_cHq3_cHq3 + cHW ** 2 * xsec_quad_cHW_cHW + cHW * cHq3 * xsec_quad_cHW_cHq3  # + cHWB * xsec_lin_cHWB / LambdaSMEFT

def weight(sqrts, mu, x1, x2, c1, c2, lin, quad):
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


    weight_up = (sigma_part_vh_up(hats, c1, c2, lin, quad)) * pdfs_up
    weight_down = (sigma_part_vh_down(hats, c1, c2, lin, quad)) * pdfs_down
    return weight_down + weight_up


def dsigma_dmvh_dy(y, mvh, c1, c2, lin, quad):
    """
    Compute the doubly differential cross section in mtt and y at any order NP
    """
    if mvh == mz + mh: return 0  # if at threshold return zero

    if np.abs(y) < np.log(np.sqrt(s) / mvh):  # check whether x = {mtt, y} falls inside the physically allowed region
        x1 = mvh / np.sqrt(s) * np.exp(y)
        x2 = mvh / np.sqrt(s) * np.exp(-y)
        dsigma_dmtt_dy = 2 * mvh / s * v_weight(mvh, 91.188, x1, x2, c1, c2, lin, quad) / (x1 * x2)
        return pb_convert * dsigma_dmtt_dy
    else:
        return 0


def dsigma_dmvh(mvh, c, lin, quad):
    y_min, y_max = -0.5 * np.log(s / mvh), 0.5 * np.log(s / mvh)
    c1 = c
    c2 = 0
    dsigma_dmtt = integrate.fixed_quad(dsigma_dmtt_dy_vec, y_min, y_max, args=(mvh, c1, c2, lin, quad), n=10)[0]
    return dsigma_dmtt


def sigma_bin(bins, cHW, cHq3, lin=True, quad=True):
    sigma_i = []
    for i in range(len(bins) - 1):
        temp = integrate.fixed_quad(dsigma_dmvh_vec, bins[i], bins[i + 1], args=(cHW, cHq3, lin, quad), n=10)[0]
        sigma_i.append(temp)
    sigma_i = np.array(sigma_i)
    return sigma_i


def findCoeff(bins):
    sm = sigma_bin(bins, cHW=0, cHq3=0)
    cHW_lin = (sigma_bin(bins, cHW=10, cHq3=0, lin=True, quad=False) - sm) / 10
    cHq3_lin = (sigma_bin(bins, cHW=0, cHq3=10, lin=True, quad=False) - sm) / 10

    cHW_quad = (sigma_bin(bins, cHW=10, cHq3=0, lin=False, quad=True) - (sm + 10 * cHW_lin)) / 10 ** 2
    cHq3_quad = (sigma_bin(bins, cHW=0, cHq3=10, lin=False, quad=True) - (sm + 10 * cHq3_lin)) / 10 ** 2

    cHW_cHq3 = (sigma_bin(bins, cHW=10, cHq3=10, lin=False, quad=True) - (
                sm + 10 * cHW_lin + 10 ** 2 * cHW_quad + 10 * cHq3_lin + 10 ** 2 * cHq3_quad)) / 10 ** 2

    coeff = np.array([sm, cHW_lin, cHW_quad, cHq3_lin, cHq3_quad, cHW_cHq3])
    return coeff


def nu_i(a, cHW, cHq3, luminosity):
    eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
    xsec = np.einsum('ij,i', a, eft_point)
    nu = xsec * luminosity
    return nu

v_weight = np.vectorize(weight, otypes=[np.float])
dsigma_dmtt_dy_vec = np.vectorize(dsigma_dmvh_dy, otypes=[np.float])
dsigma_dmvh_vec = np.vectorize(dsigma_dmvh, otypes=[np.float])