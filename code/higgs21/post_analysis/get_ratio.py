#%%
import random
import numpy as np
import quad_clas.core.xsec.vh_prod as vh_prod

events_sm = np.load('/Users/jaco/Documents/ML4EFT/data/events/sm/events_0.npy')
events_eft = np.load('/Users/jaco/Documents/ML4EFT/data/events/p_value_scan/cHq3_axis/events_3.npy')

luminosity = 60000
# xsec_sm = events_sm[0,0]
# xsec_eft = events_eft[0,0]*1e5
# nu_sm = xsec_sm * luminosity
# nu_eft = xsec_eft * luminosity

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
cHW = 0
cHq3 = 0.01

bins = np.array([mz + mh, 2])
a = vh_prod.findCoeff(bins)


eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
eft_point_sm = np.array([1, 0, 0, 0, 0, 0])
x_sec_eft = np.einsum('ij,i', a, eft_point)
x_sec_sm = np.einsum('ij,i', a, eft_point_sm)
nu_eft = x_sec_eft * luminosity
nu_sm = x_sec_sm * luminosity


n_exp = 100
exp_size = 1000
z_scores = []
for exp in range(n_exp):
    rnd_idx = np.array([random.randint(1, len(events_sm)-2) for dummy in range(exp_size)])
    events_sm_sub = events_sm[rnd_idx, :]
    events_eft_sub = events_eft[rnd_idx, :]

    # diff xsecs under eft
    sm_diff_xsec_H0 = [vh_prod.dsigma_dmvh(mvh, 0, 0, lin=True, quad=False) for mvh in events_eft_sub[:,0]]
    eft_diff_xsec_H0 = [vh_prod.dsigma_dmvh(mvh, 0, 0.01, lin=False, quad=True) for mvh in events_eft_sub[:,0]]

    # diff xsecs under sm
    sm_diff_xsec_H1 = [vh_prod.dsigma_dmvh(mvh, 0, 0, lin=True, quad=False) for mvh in events_sm_sub[:,0]]
    eft_diff_xsec_H1 = [vh_prod.dsigma_dmvh(mvh, 0, 0.01, lin=False, quad=True) for mvh in events_sm_sub[:,0]]

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

    z_score = (mean_tc_H1 - mean_tc_H0)/sigma_tc_H0
    z_scores.append(z_score)
z_scores = np.array(z_scores)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.hist(z_scores, 10, color='red')
plt.show()
#%%
#vh_prod.dsigma_dmvh_dy(0.3, 0.4, 0.0, 0.0, lin=True, quad=False)
#%%

# #%%
# # likelihood ratio
# r_c = dsigma_dx_eft / dsigma_dx_sm
#
# # log-likelihood ratio
# tau_c = np.log(r_c)  # tau_c.shape = (n_eft_points, n_events)
# mean_tauc_2 = np.mean(tau_c, axis=1).flatten()
# mean_tauc_sq = np.mean(tau_c ** 2, axis=1).flatten()
#
# # expected number of events
# expected_eft = np.array([nu['eft'] for nu in self.nu])
# expected_sm = np.array([nu['sm'] for nu in self.nu])
#
# mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc_2 if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc_2
# sigma_tc = np.sqrt(expected_eft * mean_tauc_sq) if hypothesis == 'eft' else np.sqrt(expected_sm * mean_tauc_sq)
#
