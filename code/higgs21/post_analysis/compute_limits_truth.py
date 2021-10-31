#%%
import random
import numpy as np
import quad_clas.core.xsec.vh_prod as vh_prod

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
luminosity = 60000
bins = np.array([mz + mh, 4]) # integration domain
a = vh_prod.findCoeff(bins) # a * eft_point = xsec


events_sm = np.load('/Users/jaco/Documents/ML4EFT/data/events/sm/events_0.npy')
eft_path = '/Users/jaco/Documents/ML4EFT/data/z_scores/cHq3/events_{}.npy'
z_scores = []
cHW = 0
n_exp = 10
exp_size = 10000

cHq3_values = [0.08, 0.06, 0.05, 0.04, 0.02, -0.04, -0.05, -0.06]
for i, cHq3 in enumerate(cHq3_values):

    events_eft = np.load(eft_path.format(i+1))

    eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
    eft_point_sm = np.array([1, 0, 0, 0, 0, 0])

    x_sec_eft = np.einsum('ij,i', a, eft_point)
    x_sec_sm = np.einsum('ij,i', a, eft_point_sm)

    nu_eft = x_sec_eft * luminosity
    nu_sm = x_sec_sm * luminosity

    for exp in range(n_exp):
        print(cHq3, exp)
        rnd_idx = np.array([random.randint(1, len(events_sm)-2) for dummy in range(exp_size)])
        events_sm_sub = events_sm[rnd_idx, :]
        events_eft_sub = events_eft[rnd_idx, :]

        # diff xsecs under eft
        sm_diff_xsec_H0 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin=True, quad=False) for (mvh, y) in events_eft_sub]
        eft_diff_xsec_H0 = [vh_prod.dsigma_dmvh_dy(y, mvh, cHW, cHq3, lin=False, quad=True) for (mvh, y) in events_eft_sub]

        # diff xsecs under sm
        sm_diff_xsec_H1 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin=True, quad=False) for (mvh, y) in events_sm_sub]
        eft_diff_xsec_H1 = [vh_prod.dsigma_dmvh_dy(y, mvh, cHW, cHq3, lin=False, quad=True) for (mvh, y) in events_sm_sub]

        # cast all the list to arrays
        sm_diff_xsec_H0 = np.array(sm_diff_xsec_H0)
        eft_diff_xsec_H0 = np.array(eft_diff_xsec_H0)
        sm_diff_xsec_H1 = np.array(sm_diff_xsec_H1)
        eft_diff_xsec_H1 = np.array(eft_diff_xsec_H1)

        # compute the log ratio
        tau_c_H0 = np.log(eft_diff_xsec_H0 / sm_diff_xsec_H0)
        tau_c_H1 = np.log(eft_diff_xsec_H1 / sm_diff_xsec_H1)

        mean_tau_c_H0 = np.mean(tau_c_H0)
        mean_tau_c_H1 = np.mean(tau_c_H1)

        mean_tau_c_sq_H0 = np.mean(tau_c_H0 ** 2)
        mean_tau_c_sq_H1 = np.mean(tau_c_H1 ** 2)

        mean_tc_H1 = nu_eft - nu_sm - nu_sm * mean_tau_c_H1
        mean_tc_H0 = nu_eft - nu_sm - nu_eft * mean_tau_c_H0

        sigma_tc_H0 = np.sqrt(nu_eft * mean_tau_c_sq_H0)
        sigma_tc_H1 = np.sqrt(nu_sm * mean_tau_c_sq_H1)

        z_score = (mean_tc_H1 - mean_tc_H0) / sigma_tc_H0
        z_scores.append(z_score)

z_scores = np.array(z_scores)
z_scores = np.reshape(z_scores, (len(cHq3_values), -1))

np.save('/Users/jaco/Documents/ML4EFT/code/output/limits/z_scores_truth_cHq3_v2.npy', z_scores)
