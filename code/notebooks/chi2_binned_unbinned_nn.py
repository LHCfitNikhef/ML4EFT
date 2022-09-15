# same pseudo-dataset in all binnings

import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.truth.vh_prod as vh_prod
from quad_clas.core.classifier import PredictorCross, Classifier, PredictorQuadratic
import os
import torch

path_lin_1 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW3_lin_30_reps/'
path_lin_2 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHq3_lin_2_feat/'
path_quad_1 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_quad_2_feat/'
path_quad_2 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHq3_quad_2_feat/'
path_cross = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_cHq3_2_feat/'

n_models = 10
architecture = [2, 30, 30, 30, 30, 30, 1]

def get_nn_ratio(x, c1, c2, mc_run):
    path_nn_lin_1 = os.path.join(path_lin_1, 'mc_run_{}', 'trained_nn.pt')
    path_nn_lin_2 = os.path.join(path_lin_2, 'mc_run_{}', 'trained_nn.pt')
    path_nn_quad_1 = os.path.join(path_quad_1, 'mc_run_{}', 'trained_nn.pt')
    path_nn_quad_2 = os.path.join(path_quad_2, 'mc_run_{}', 'trained_nn.pt')
    path_nn_cross = os.path.join(path_cross, 'mc_run_{}', 'trained_nn.pt')

    with torch.no_grad():
        n_lin_1 = Classifier(architecture)
        n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_lin_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))

        x_scaled = (x - mean) / std
        n_lin_1_out = n_lin_1.n_alpha(x_scaled.float()) ** 2

        #######

        n_lin_2 = Classifier(architecture)
        n_lin_2.load_state_dict(torch.load(path_nn_lin_2.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_lin_2, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        x_scaled = (x - mean) / std
        n_lin_2_out = n_lin_2.n_alpha(x_scaled.float()) ** 2

        ########

        n_quad_1 = PredictorQuadratic(architecture)
        n_quad_1.load_state_dict(torch.load(path_nn_quad_1.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_quad_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        x_scaled = (x - mean) / std
        n_quad_1_out = n_quad_1.n_beta(x_scaled.float()) ** 2

        #######

        n_quad_2 = PredictorQuadratic(architecture)
        n_quad_2.load_state_dict(torch.load(path_nn_quad_2.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_quad_2, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        x_scaled = (x - mean) / std
        n_quad_2_out = n_quad_2.n_beta(x_scaled.float()) ** 2

        #######

        n_cross = PredictorCross(architecture)
        n_cross.load_state_dict(torch.load(path_nn_cross.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_cross, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        x_scaled = (x - mean) / std
        n_cross_out = n_cross.n_gamma(x_scaled.float()) ** 2

    r = 1 + c1 * n_lin_1_out + c2 * n_lin_2_out + c1 ** 2 * n_quad_1_out + c2 ** 2 * n_quad_2_out + c1 * c2 * n_cross_out

    return r

events_sm = np.load('/data/theorie/jthoeve/event_generation/events/sm/events_0.npy')
pseudo_data_full = events_sm[1:, :]
luminosity = 60000

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
bins = np.array([mz+mh, 4])
a = vh_prod.findCoeff(bins)
nu_tot = vh_prod.nu_i(a, 0, 0, luminosity, quad=True)
n_tot = np.random.poisson(nu_tot, 1)
pseudo_data_idx = np.random.choice(np.arange(0, len(pseudo_data_full)), int(nu_tot), replace=False)
pseudo_data = pseudo_data_full[pseudo_data_idx, 0]
pseudo_data_2_feat = pseudo_data_full[pseudo_data_idx, :]
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125



def chi2_function(data, theory):
    return np.sum((data-theory) ** 2 / data)


cHW_values = np.linspace(-0.3, 0.3, 10)
cHq3_values = np.linspace(-0.3, 0.3, 10)
# nrows = 3
# ncols = 2
# fig = plt.figure(figsize=(ncols * 8, nrows * 6))
# for i, n_bins in enumerate([2, 5, 10, 15, 20]):
#     ax = plt.subplot(nrows, ncols, i + 1)
#     if n_bins == 1:
#         bins = np.array([mz+mh, 4.0])
#     else:
#         bins = np.linspace(mz + mh, 1.5, n_bins)
#         bins = np.append(bins, 4.0)
#     a = vh_prod.findCoeff(bins)
#
#     n_i, _ = np.histogram(pseudo_data, bins)
#     #nu_i_sm = vh_prod.nu_i(a, 0, 0, luminosity, quad=True)
#
#     #pseudo_data_binned = np.random.poisson(nu_i_sm, len(nu_i_sm))
#     chi2_values = []
#     for cHW in cHW_values:
#         for cHq3 in cHq3_values:
#             nu_i = vh_prod.nu_i(a, cHW, cHq3, luminosity, quad=True)
#             chi2_values.append(chi2_function(n_i, nu_i))
#     chi2_values = np.array(chi2_values)
#     chi2_values = np.reshape(chi2_values, (len(cHW_values), len(cHq3_values)))
#
#     xx, yy = np.meshgrid(cHW_values, cHq3_values, indexing='ij')
#     plt.contourf(yy, xx, chi2_values, np.array([np.min(chi2_values), np.min(chi2_values) + 2.3]), colors='C0',
#                  origin='lower', alpha=0.5)
#     plt.contourf(yy, xx, chi2_values, np.array([np.min(chi2_values) + 2.3, np.min(chi2_values) + 5.99]), colors='C2',
#                  origin='lower', alpha=0.5)
#     plt.contour(yy, xx, chi2_values, np.array([np.min(chi2_values) + 2.3]), colors='k',
#                 origin='lower')
#
#     contour = plt.contour(yy, xx, chi2_values, np.array([np.min(chi2_values) + 5.99]), colors='k',
#                           origin='lower')
#
#     plt.xlabel('cHq3')
#     plt.ylabel('cHW')
#
#     min_idx_0 = np.argmin(chi2_values) // chi2_values.shape[1]  # axis 0
#     min_idx_1 = np.argmin(chi2_values) % chi2_values.shape[1]  # axis 1
#     plt.scatter(cHq3_values[min_idx_1], cHW_values[min_idx_0], marker='x', label=r'$\chi^2_{\rm{min}}$', color='k')
#     plt.scatter(0, 0, marker='o', label='SM', color='k')
#     plt.legend()
#
#     contour_line = contour.allsegs[0][0]
#     cHq3_min, cHW_min = np.min(contour_line, axis=0)
#     cHq3_max, cHW_max = np.max(contour_line, axis=0)
#     delta_cHq3 = cHq3_max - cHq3_min
#     delta_cHW = cHW_max - cHW_min
#     x_min = cHq3_min - 0.1 * delta_cHq3
#     x_max = cHq3_max + 0.1 * delta_cHq3
#
#     plt.xlim(max(x_min, np.min(cHq3_values)), min(x_max, np.max(cHq3_values)))
#     plt.ylim(max(cHW_min - 0.1 * delta_cHW, np.min(cHW_values)), min(cHW_max + 0.1 * delta_cHW, np.max(cHW_values)))
#
#     plt.title(r'$\chi^2_{\rm{binned}}\;(%d\;\rm{bins})$' % n_bins)

#ax = plt.subplot(3, 2, 6)
# plr analysis
fig = plt.figure()
likelihood_scan = []
a = vh_prod.findCoeff(np.array([mz + mh, 4]))
mc_run = 1
for cHW in cHW_values:
    print(cHW)
    for cHq3 in cHq3_values:
        nu = vh_prod.nu_i(a, cHW, cHq3, luminosity, quad=True)
        log_r = get_nn_ratio(torch.tensor(pseudo_data_2_feat), cHW, cHq3, mc_run).numpy()
        log_l = -nu + np.sum(log_r)
        likelihood_scan.append(log_l)

likelihood_scan = np.array(likelihood_scan)
likelihood_scan = np.reshape(likelihood_scan, (len(cHW_values), len(cHq3_values)))

cHW_idx_hat = np.argmax(likelihood_scan) // likelihood_scan.shape[1] # axis 0
cHq3_idx_hat = np.argmax(likelihood_scan) % likelihood_scan.shape[1]
cHW_hat = cHW_values[cHW_idx_hat]
cHq3_hat = cHq3_values[cHq3_idx_hat]

q_c_array = 2 * (- likelihood_scan + np.max(likelihood_scan))

xx, yy = np.meshgrid(cHW_values, cHq3_values, indexing='ij')
plt.contourf(yy, xx, q_c_array, np.array([np.min(q_c_array), np.min(q_c_array) + 2.3]), colors='C0',
             origin='lower', alpha=0.5)
plt.contourf(yy, xx, q_c_array, np.array([np.min(q_c_array) + 2.3, np.min(q_c_array) + 5.99]), colors='C2', origin='lower', alpha=0.5)
plt.contour(yy, xx, q_c_array, np.array([np.min(q_c_array) + 2.3]), colors='k',
            origin='lower')

contour = plt.contour(yy, xx, q_c_array, np.array([np.min(q_c_array) + 5.99]), colors='k',
             origin='lower')
plt.xlabel('cHq3')
plt.ylabel('cHW')



min_idx_0 = np.argmin(q_c_array) // q_c_array.shape[1] # axis 0
min_idx_1 = np.argmin(q_c_array) % q_c_array.shape[1] # axis 1
plt.scatter(cHq3_values[min_idx_1], cHW_values[min_idx_0], marker='x', label=r'$\chi^2_{\rm{min}}$', color='k')
plt.scatter(0, 0, marker='o', label='SM', color='k')
plt.legend()


plt.savefig('/data/theorie/jthoeve/Lunteren/nn_bounds.pdf')