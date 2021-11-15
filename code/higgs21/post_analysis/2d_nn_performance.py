import numpy as np
import matplotlib.pyplot as plt
import torch
import copy
import os

import quad_clas.core.xsec.vh_prod as vh_prod
import quad_clas.core.quad_classifier_cluster as quad_classifier_cluster
import quad_clas.core.nn_analyse as analysis

cmap = copy.copy(plt.get_cmap("seismic"))

def coeff_comp():

    s = 14 ** 2
    mvh_min, mvh_max = 0.3, 2
    y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)

    x_spacing, y_spacing = 1e-2, 0.01
    mvh_span = np.arange(mvh_min, mvh_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)

    mvh_grid, y_grid = np.meshgrid(mvh_span, y_span)
    grid = np.c_[mvh_grid.ravel(), y_grid.ravel()]

    ratio_truth_c1 = analysis.likelihood_ratio_truth(grid, np.array([10, 0]), lin=True)
    ratio_truth_c2 = analysis.likelihood_ratio_truth(grid, np.array([0, 10]), lin=True)
    mask = ratio_truth_c1 == 0

    n_alpha = np.ma.masked_where(mask, (1 - ratio_truth_c1) / 10)
    n_beta = np.ma.masked_where(mask, (1 - ratio_truth_c2) / 10)

    cmap = copy.copy(plt.get_cmap("GnBu"))
    cmap.set_bad(color='white')

    # n_alpha
    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(n_alpha.reshape(xx.shape), extent=[mvh_min, mvh_max, y_min, y_max],
                         origin='lower', cmap=cmap, aspect=(mvh_max - mvh_min) / (y_max - y_min),
                         interpolation='quadric')

    cbar = fig.colorbar(im, ax=ax, shrink=0.9)
    cbar.minorticks_on()
    plt.xlabel(r'$m_{ZH}\;\rm{[TeV]}$')
    plt.ylabel(r'$\rm{Rapidity}$')
    plt.title(r'$n_{\alpha}$')
    plt.show()

    # n_beta
    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(n_beta.reshape(xx.shape), extent=[mvh_min, mvh_max, y_min, y_max],
                   origin='lower', cmap=cmap, aspect=(mvh_max - mvh_min) / (y_max - y_min),
                   interpolation='quadric')

    cbar = fig.colorbar(im, ax=ax, shrink=0.9)
    cbar.minorticks_on()
    plt.xlabel(r'$m_{ZH}\;\rm{[TeV]}$')
    plt.ylabel(r'$\rm{Rapidity}$')
    plt.title(r'$n_{\beta}$')

    plt.show()

coeff_comp()

#%%

def likelihood_ratio(y, mvh, c, lin, quad):
    """
    Compute the 2D analytic likelihood ratio r(x, c)
    """
    dsigma_0 = vh_prod.dsigma_dmvh_dy(y, mvh, c, 0, lin, quad) # EFT
    dsigma_1 = vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin, quad)  # SM
    ratio = dsigma_0 / dsigma_1 if dsigma_1 != 0 else 0
    return ratio

def f_analytic(mvh, y, c, lin, quad):
    r = likelihood_ratio(y, mvh, c, lin, quad)
    return 1/(1+r)

def plot_f_ana(mvh_min, mvh_max, y_min, y_max, x_spacing, y_spacing, c, lin, quad):

    # Important to include otypes = [np.float], else all the output is int by default
    vf_ana = np.vectorize(f_analytic, otypes=[np.float])
    x = np.arange(mvh_min, mvh_max, x_spacing)
    y = np.arange(y_min, y_max, y_spacing)
    xx, yy = np.meshgrid(x, y)
    Z = vf_ana(xx, yy, c, lin, quad)
    return Z

# Set up coordinates and compute f
s = 14 ** 2
mvh_min, mvh_max = 0.3, 2
y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)


x_spacing, y_spacing = 1e-2, 0.01
x_span = np.arange(mvh_min, mvh_max, x_spacing)
y_span = np.arange(y_min, y_max, y_spacing)

xx, yy = np.meshgrid(x_span, y_span)
grid_unscaled = np.c_[xx.ravel(), yy.ravel()]
grid_unscaled_tensor = torch.Tensor(grid_unscaled)

c = 2
network_size = [2, 30, 30, 30, 30, 30, 1]
model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW3_lin_30_reps/mc_run_{mc_run}'

means = []
stds = []
f_preds = []
mc_runs = 30
for rep_nr in range(1, mc_runs + 1):
    print(rep_nr)
    mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=rep_nr), 'scaling.dat'))
    loaded_model = quad_classifier_cluster.PredictorLinear(network_size)
    network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt')

    # load all the parameters into the trained network
    loaded_model.load_state_dict(torch.load(network_path))

    grid = (grid_unscaled_tensor - mean) / std

    f_pred = loaded_model.forward(grid.float(), c)
    f_pred = f_pred.view(xx.shape).detach().numpy()
    f_preds.append(f_pred)

f_preds = np.array(f_preds)
f_pred_median = np.percentile(f_preds, 50, axis=0)
f_pred_high = np.percentile(f_preds, 84, axis=0)
f_pred_low = np.percentile(f_preds, 16, axis=0)
f_pred_unc = (f_pred_high - f_pred_low)/2

f_ana = plot_f_ana(mvh_min, mvh_max, y_min, y_max, x_spacing, y_spacing, c, True, False)
f_ana = np.ma.masked_where(f_ana == 1.0, f_ana)

cmap = copy.copy(plt.get_cmap("coolwarm"))
cmap.set_bad(color='white')
#cmap = copy.copy(plt.get_cmap("Blues"))  # Can be any colormap that you want after the cm

fig, ax = plt.subplots(figsize=(8, 7))

ratio_unc = (f_ana/f_pred_low - f_ana/f_pred_high)/2
im = ax.imshow(f_ana/f_pred_median, extent=[mvh_min, mvh_max, y_min, y_max],
                     origin='lower', cmap='RdBu', aspect=(mvh_max - mvh_min) / (y_max - y_min),
                     interpolation='quadric', vmin=0.95, vmax=1.05)
# im = ax.imshow((np.abs(f_pred_median-f_ana))/f_pred_unc, extent=[mvh_min, mvh_max, y_min, y_max],
#                      origin='lower', cmap='coolwarm', aspect=(mvh_max - mvh_min) / (y_max - y_min),
#                      interpolation='quadric', vmin=0, vmax=2)
# im = ax.imshow(ratio_unc, extent=[mvh_min, mvh_max, y_min, y_max],
#                      origin='lower', cmap='coolwarm', aspect=(mvh_max - mvh_min) / (y_max - y_min),
#                      interpolation='quadric', vmin=0, vmax=0.04)
cbar = fig.colorbar(im, ax=ax, shrink=0.9, extend='max')
cbar.minorticks_on()
plt.xlabel(r'$m_{ZH}\;\rm{[TeV]}$')
plt.ylabel(r'$\rm{Rapidity}$')

#plt.title(r'$\rm{Pull}$')
plt.title(r'$\rm{Truth/NN}\;\rm{prediction}\;\rm{(median)}$')
#plt.title(r'$\rm{Truth/NN}\;\rm{prediction}\;\rm{(uncertainty)}$')
fig.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/2D_performance_median_30_reps_ext.pdf')