#%%
import random
import numpy as np
import quad_clas.core.xsec.vh_prod as vh_prod

events_sm = np.load('/Users/jaco/Documents/ML4EFT/data/events/sm/events_0.npy')
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
bins = np.array([mz + mh, 4])
a = vh_prod.findCoeff(bins)
z_scores = []
for i, cHq3 in enumerate([0.06, 0.05, 0.04, -0.04, -0.05, -0.06]):
    events_eft = np.load('/Users/jaco/Documents/ML4EFT/code/MG5_aMC_v2.7.3/MG5_aMC_v2_7_3/bin/p_value_scan_cHq3/Events/events_{}.npy'.format(i+1))

    luminosity = 60000
    # xsec_sm = events_sm[0,0]
    # xsec_eft = events_eft[0,0]*1e5
    # nu_sm = xsec_sm * luminosity
    # nu_eft = xsec_eft * luminosity


    cHW =0
    #cHq3 = 0.06




    eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
    eft_point_sm = np.array([1, 0, 0, 0, 0, 0])
    x_sec_eft = np.einsum('ij,i', a, eft_point)
    x_sec_sm = np.einsum('ij,i', a, eft_point_sm)
    nu_eft = x_sec_eft * luminosity
    nu_sm = x_sec_sm * luminosity


    n_exp = 10
    exp_size = 10000

    for exp in range(n_exp):
        print(z_scores)
        rnd_idx = np.array([random.randint(1, len(events_sm)-2) for dummy in range(exp_size)])
        events_sm_sub = events_sm[rnd_idx, :]
        events_eft_sub = events_eft[rnd_idx, :]

        # diff xsecs under eft
        sm_diff_xsec_H0 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin=True, quad=False) for (mvh, y) in events_eft_sub]
        eft_diff_xsec_H0 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, cHq3, lin=False, quad=True) for (mvh, y) in events_eft_sub]

        # diff xsecs under sm
        sm_diff_xsec_H1 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin=True, quad=False) for (mvh, y) in events_sm_sub]
        eft_diff_xsec_H1 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, cHq3, lin=False, quad=True) for (mvh, y) in events_sm_sub]

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
z_scores = np.reshape(z_scores, (n_exp, -1))
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
