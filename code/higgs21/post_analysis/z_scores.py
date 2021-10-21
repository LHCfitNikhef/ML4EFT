import torch
import numpy as np
import os
from quad_clas.core.quad_classifier_cluster import PredictorCross, PredictorLinear, PredictorQuadratic
import quad_clas.core.xsec.vh_prod as vh_prod

events_sm = np.load('/data/theorie/jthoeve/ML4EFT_higgs/events/p_value_scan/events_0.npy')
events_eft = np.load('/data/theorie/jthoeve/ML4EFT_higgs/events/p_value_scan/cHq3_axis/events_1.npy')

path_lin_1 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_lin_2_feat/'
path_lin_2 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHq3_lin_2_feat/'
path_quad_1 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_quad_2_feat/'
path_quad_2 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHq3_quad_2_feat/'
path_cross = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_cHq3_2_feat/'

architecture = [2, 30, 30, 30, 30, 30, 1]
n_models = 10


def get_nn_ratio(x, c1, c2):

    path_nn_lin_1 = os.path.join(path_lin_1, 'mc_run_{}', 'trained_nn.pt')
    path_nn_lin_2 = os.path.join(path_lin_2, 'mc_run_{}', 'trained_nn.pt')

    #x = x.unsqueeze(1)
    ratios = []

    for mc_run in range(n_models):
        n_lin_1 = PredictorLinear(architecture)
        n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_lin_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        x_scaled = (x - mean) / std
        n_lin_1_out = n_lin_1.n_alpha(x_scaled.float()) ** 2

        n_lin_2 = PredictorLinear(architecture)
        n_lin_2.load_state_dict(torch.load(path_nn_lin_2.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_lin_2, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        x_scaled = (x - mean) / std
        n_lin_2_out = n_lin_2.n_alpha(x_scaled.float()) ** 2

        r = 1 + c1 * n_lin_1_out + c2 * n_lin_2_out
        ratios.append(r)

    return ratios

def get_truth_ratio(x, c1, c2, lin, quad):
    sm_diff_xsec = vh_prod.dsigma_dmvh(x, 0, 0, lin=True, quad=False)
    eft_diff_xsec = vh_prod.dsigma_dmvh(x, c1, c2, lin=lin, quad=quad)

    return eft_diff_xsec/sm_diff_xsec


ratios_nn = get_nn_ratio(torch.tensor([0.4, 0]), 1, 1)
ratios_truth = get_truth_ratio(0.4, 5, 5, lin=False, quad=True)
import pdb
pdb.set_trace()

#%%
import matplotlib.pyplot as plt
def plot_coefficients():
    path_nn_lin_1 = os.path.join(path_lin_1, 'mc_run_{}', 'trained_nn.pt')
    path_nn_lin_2 = os.path.join(path_lin_2, 'mc_run_{}', 'trained_nn.pt')
    path_nn_quad_1 = os.path.join(path_quad_1, 'mc_run_{}', 'trained_nn.pt')
    path_nn_quad_2 = os.path.join(path_quad_2, 'mc_run_{}', 'trained_nn.pt')
    path_nn_cross = os.path.join(path_cross, 'mc_run_{}', 'trained_nn.pt')
    n_alphas = []
    fig, ax = plt.subplots()
    for mc_run in range(1, n_models + 1):
        n_lin_1 = PredictorLinear(architecture)
        n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))

        mean, std = np.loadtxt(os.path.join(path_lin_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))

        x = np.array([np.linspace(0.3, 1, 100), np.zeros(100)]).T
        x_scaled = (x-mean) / std
        x_scaled = torch.tensor(x_scaled)
        n_lin_1_out = n_lin_1.n_alpha(x_scaled.float()) ** 2
        n_alpha = n_lin_1_out.detach().numpy().flatten()
        n_alphas.append(n_alpha)
    n_alphas = np.array(n_alphas)
    ax.fill_between(x[:, 0], np.percentile(n_alphas, 84, axis=0), np.percentile(n_alphas, 16, axis=0), alpha=0.5)
    #ax.plot(x[:, 0].flatten(), n_alpha, label='replica {}'.format(mc_run))

    ana = (np.array([get_truth_ratio(mvh, 10, 0, lin=True, quad=False) for mvh in np.linspace(0.3, 1, 100)])-1)/10
    ax.plot(x[:, 0], ana, linestyle='dashed', color='red')

    fig.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/n_alpha.pdf')
    import pdb
    pdb.set_trace()
plot_coefficients()
