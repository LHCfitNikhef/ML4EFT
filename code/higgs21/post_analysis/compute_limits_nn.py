import torch
import numpy as np
import os
import random
from quad_clas.core.quad_classifier_cluster import PredictorCross, PredictorLinear, PredictorQuadratic
import quad_clas.core.xsec.vh_prod as vh_prod
import matplotlib.pyplot as plt

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

        n_lin_1 = PredictorLinear(architecture)
        n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_lin_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))

        x_scaled = (x-mean) / std
        n_lin_1_out = n_lin_1.n_alpha(x_scaled.float()) ** 2

        #######

        n_lin_2 = PredictorLinear(architecture)
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


mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
luminosity = 60000
bins = np.array([mz + mh, 4]) # integration domain
a = vh_prod.findCoeff(bins) # a * eft_point = xsec


events_sm = np.load('/data/theorie/jthoeve/ML4EFT_higgs/events/p_value_scan/events_0.npy')
eft_path = '/data/theorie/jthoeve/ML4EFT_higgs/events/z_scores/cHq3/events_{}.npy'

cHW = 0
n_exp = 10
exp_size = 10000

cHq3_values = [0.08, 0.06, 0.05, 0.04, 0.02, -0.04, -0.05, -0.06]
mc_runs = 10
for mc_run in range(1, mc_runs):
    z_scores = []
    for i, cHq3 in enumerate(cHq3_values):
        print(mc_run, cHq3)
        events_eft = np.load(eft_path.format(i+1))

        eft_point = np.array([1, cHW, cHW ** 2, cHq3, cHq3 ** 2, cHW * cHq3])
        eft_point_sm = np.array([1, 0, 0, 0, 0, 0])

        x_sec_eft = np.einsum('ij,i', a, eft_point)
        x_sec_sm = np.einsum('ij,i', a, eft_point_sm)

        nu_eft = x_sec_eft * luminosity
        nu_sm = x_sec_sm * luminosity

        for exp in range(n_exp):
            #print(cHq3, exp, z_scores)
            rnd_idx = np.array([random.randint(1, len(events_sm)-2) for dummy in range(exp_size)])
            events_sm_sub = events_sm[rnd_idx, :]
            events_eft_sub = events_eft[rnd_idx, :]



            ratio_H0 = get_nn_ratio(torch.tensor(events_eft_sub), cHW, cHq3, mc_run).numpy()
            ratio_H1 = get_nn_ratio(torch.tensor(events_sm_sub), cHW, cHq3, mc_run).numpy()

            # compute the log ratio
            tau_c_H0 = np.log(ratio_H0)
            tau_c_H1 = np.log(ratio_H1)

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
    np.save('/data/theorie/jthoeve/ML4EFT_higgs/code/z_scores/cHq3/nn/z_scores_{}.npy'.format(mc_run), z_scores)

