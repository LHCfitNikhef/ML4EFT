#%%
import quad_clas.analyse.animate as animate
import quad_clas.core.classifier as classifier
import numpy as np
import torch
import quad_clas.analyse.analyse as analyse
import os
from quad_clas.preproc import constants
#%%

# constants
mz = constants.mz
mh = constants.mh
#%%
architecture=[2, 30, 30, 30, 30, 30, 1]
n_quad = classifier.PredictorQuadratic(architecture)

path_nn_quad = '/Users/jaco/Documents/ML4EFT/models/quad/model_quad_cHW/mc_run_0/trained_nn.pt'
n_quad.load_state_dict(torch.load(path_nn_quad))
mean, std = np.loadtxt('/Users/jaco/Documents/ML4EFT/models/quad/model_quad_cHW/mc_run_0/scaling.dat')

x = np.linspace(mh + mz + 1e-2, 2.5, 100)
x = np.stack((x, np.zeros(len(x))), axis=-1)

x_scaled = (x - mean) / std
n_quad_1_out = n_quad.forward(torch.tensor(x).float(), 2, '/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_0/trained_nn.pt')


#%%

animator = animate.Animate(architecture=[2, 30, 30, 30, 30, 30, 1],
                           c=np.array([2, 0]),
                           path_to_models='/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}',
                           mc_runs=30,
                           save_path='/Users/jaco/Documents/ML4EFT/plots/25_11/cHW_lin_v7.gif',
                           lin=True)

#%%
x = np.linspace(mh + mz + 1e-2, 2.5, 100)
x = np.stack((x, np.zeros(len(x))), axis=-1)

architecture = [2, 30, 30, 30, 30, 30, 1]
path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}',
                          '/Users/jaco/Documents/ML4EFT/models/lin/cHq3/mc_run_{mc_run}'],
                  'quad': ['/Users/jaco/Documents/ML4EFT/models/quad/cHW/mc_run_{mc_run}']}

loaded_models_lin, means, std = analyse.load_models(architecture, path_to_models['lin'][0], range(30), lin=True)
n_models = len(loaded_models_lin)

f_preds = []
n_alphas = []
for i in range(n_models):
    x_scaled = (x - means[i]) / std[i]
    with torch.no_grad():
        n_alphas.append(loaded_models_lin[i].n_alpha(torch.tensor(x_scaled).float()).numpy().flatten())
n_alphas = np.array(n_alphas)
r = 1 + 2 * n_alphas
#%%
x = np.linspace(mh + mz + 1e-2, 2.5, 100)
x = np.stack((x, np.zeros(len(x))), axis=-1)

architecture = [2, 30, 30, 30, 30, 30, 1]
# path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}',
#                           '/Users/jaco/Documents/ML4EFT/models/lin/cHq3/mc_run_{mc_run}'],
#                   'quad': ['/Users/jaco/Documents/ML4EFT/models/quad/cHW/mc_run_{mc_run}']}

path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}'],
                  'quad': ['/Users/jaco/Documents/ML4EFT/models/quad/cHW/mc_run_{mc_run}']}
mc_reps = 30


def load_coefficients_nn(x, architecture, path_to_models, mc_reps, epoch=-1):

    n_lin = []
    n_quad = []
    n_cross = []
    for order, paths in path_to_models.items():
        if order == 'lin':
            for path in paths:
                loaded_models_lin, means, std = analyse.load_models(architecture, path, range(mc_reps), epoch=epoch, lin=True)
                n_alphas = []
                for i in range(mc_reps):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_alphas.append(loaded_models_lin[i].n_alpha(torch.tensor(x_scaled).float()).numpy().flatten())
                n_alphas = np.array(n_alphas)
                n_lin.append(n_alphas)

        if order == 'quad':
            for path in paths:
                loaded_models_quad, means, std = analyse.load_models(architecture, path, range(mc_reps), epoch=epoch, quad=True)
                n_betas = []
                for i in range(mc_reps):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_betas.append(loaded_models_quad[i].n_beta(torch.tensor(x_scaled).float()).numpy().flatten())
                n_betas = np.array(n_betas)
                n_quad.append(n_betas)

        if order == 'cross':
            for path in paths:
                loaded_models_cross, means, std = analyse.load_models(architecture, path, range(mc_reps), epoch=epoch, cross=True)
                n_gammas = []
                for i in range(mc_reps):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_gammas.append(loaded_models_cross[i].n_gamma(torch.tensor(x_scaled).float()).numpy().flatten())
                n_gammas = np.array(n_gammas)
                n_cross.append(n_gammas)
    n_lin = np.array(n_lin)
    n_quad = np.array(n_quad)
    n_cross = np.array(n_cross)

    return n_lin, n_quad, n_cross

def make_predictions_1d(x, c, path_to_models, network_size, epoch=-1, lin=False, quad=False):
    n_lin, n_quad, n_cross = load_coefficients_nn(x, network_size, path_to_models, mc_reps, epoch=epoch)
    if lin:
        r = 1 + np.einsum('i, ijk', c, n_lin)
    elif quad:
        r = 1 + np.einsum('i, ijk', c, n_lin) + np.einsum('i, ijk', c ** 2, n_quad)
    return 1 / (1 + r)

#f = make_predictions_1d(x, np.array([2]), path_to_models, architecture)


#%%
n_lin, n_quad, n_cross = load_coefficients_nn(x, architecture, path_to_models, mc_reps)
#%%
f_preds_lin = make_predictions_1d(x, np.array([2]), path_to_models, architecture, epoch=1, lin=True)
f_preds_quad = make_predictions_1d(x, np.array([2]), path_to_models, architecture, epoch=1, quad=True)
#%%
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,6))
for f_lin, f_quad in zip(f_preds_lin, f_preds_quad):
    plt.plot(x[:,0], f_lin)
    plt.plot(x[:,0], f_quad)
plt.show()