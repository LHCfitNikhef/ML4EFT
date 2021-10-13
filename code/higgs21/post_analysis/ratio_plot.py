#%%
import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.nn_analyse as analyse
import quad_clas.core.xsec.tt_prod as axs
import quad_clas.core.xsec.vh_prod as vh_prod
import quad_clas.core.quad_classifier_cluster as quad_classifier_cluster

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
mvh_min, mvh_max = mz + mh, 1.0
x = np.arange(mvh_min + 1e-2, mvh_max, 1e-2)

eft = np.array([vh_prod.dsigma_dmvh(mvh, 0, 12, False, True) for mvh in x])
sm = np.array([vh_prod.dsigma_dmvh(mvh, 0, 0, True, False) for mvh in x])
ratio = eft/sm
f = 1 / (1 + ratio)

#%%
# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots(figsize=(1.1*10, 1.1*6))

ax = plt.axes(ylim=(0, 1), xlim=(mvh_min, mvh_max))

# Compute the analytic likelihood ratio and plot
x_1, y_1 = axs.plot_likelihood_ratio_1D(mvh_min + 1e-2, 1, [2, 0])
x_1 = np.array(x_1)
y_1 = np.array(y_1)
ax.plot(x_1, y_1, '--', c='red', label=r'$\rm{Truth}$')
ax.plot(x, f, linestyle='dotted', c='blue', label='package')
plt.ylabel(r'$f\;(m_{tt}, c)$')
plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
plt.ylim((0, 1))
plt.legend()
plt.show()

#%%
fig = plt.figure()
plt.plot(x, eft, label='EFT')
plt.plot(x, sm, label='SM')
plt.legend()
plt.yscale('log')
plt.show()

#%%
fig = plt.figure()
plt.plot(x, eft/sm, label='ratio')
plt.legend()
plt.show()
#%%

# n_a
n_alpha = (ratio - 1)/10

network_size = [1, 30, 30, 30, 30, 30, 1]
mean = 3.249145538393696242e-01
std = 1.365107287047037377e-01
x, f_pred = analyse.make_predictions_1d('/Users/jaco/Documents/ML4EFT/code/higgs21/models/model_cHW_lin/mc_run_0/trained_nn.pt', network_size, [10, 0], mean, std)
n_alpha_pred = ((1/f_pred)-2)/10

fig = plt.figure()
plt.plot(x, n_alpha_pred, label='nalpha pred')
plt.plot(x, n_alpha, label='nalpha ana')
plt.legend()
plt.show()

#%%
import quad_clas
import torch
import copy
import quad_clas.core.quad_classifier_cluster as quad_classifier_cluster

cmap = copy.copy(plt.get_cmap("seismic"))

def likelihood_ratio(y, mvh, c, lin, quad):
    """
    Compute the 2D analytic likelihood ratio r(x, c)
    """
    dsigma_0 = vh_prod.dsigma_dmvh_dy(y, mvh, c, 0, lin, quad)
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


c=2

network_size = [2, 30, 30, 30, 30, 30, 1]
loaded_model = quad_classifier_cluster.PredictorLinear(network_size)
network_path = '/Users/jaco/Documents/ML4EFT/code/higgs21/models/model_cHW_lin/mc_run_6/trained_nn.pt'
# load all the parameters into the trained network
loaded_model.load_state_dict(torch.load(network_path))

# Set up coordinates and compute f
mtt_min, mtt_max = 0.3, 1
s = 14** 2
y_min, y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
x_spacing, y_spacing = 1e-3, 0.01

x_span = np.arange(mtt_min, mtt_max, x_spacing)
y_span = np.arange(y_min, y_max, y_spacing)
xx, yy = np.meshgrid(x_span, y_span)
grid = torch.Tensor(np.c_[xx.ravel(), yy.ravel()])
# rescale the grid
mean = np.array([3.253564295450930843e-1, -9.658987360880860740e-4])
std = np.array([1.331810233898108320e-1, 1.618454672275956518])
grid = (grid - mean) / std
# grid = -1 + 2 / (train_dataset.max_value - train_dataset.min_value) * (grid - train_dataset.min_value)

f_pred = loaded_model.forward(grid.float(), c)  # TODO: why .float() needed?
f_pred = f_pred.view(xx.shape).detach().numpy()

# n_alpha = loaded_model.n_alpha(grid.float())
# n_alpha = n_alpha.view(xx.shape).detach().numpy()



f_ana = plot_f_ana(mtt_min, mtt_max, y_min, y_max, x_spacing, y_spacing, c, True, False)
#%%
cmap = copy.copy(plt.get_cmap("seismic"))
fig, ax = plt.subplots(figsize=(8, 7))
f_ana = np.ma.masked_where(f_ana == 1.0, f_ana)
#cmap = copy.copy(plt.get_cmap("Blues"))  # Can be any colormap that you want after the cm
cmap.set_bad(color='white')
im = ax.imshow(f_ana/f_pred, extent=[mtt_min, mtt_max, y_min, y_max],
                     origin='lower', cmap='RdBu', aspect=(mtt_max - mtt_min) / (y_max - y_min),
                     interpolation='quadric', vmin=0.9, vmax=1.1)
cbar = fig.colorbar(im, ax=ax, shrink=0.9, extend='both')
cbar.minorticks_on()
plt.xlabel(r'$m_{ZH}\;\rm{[TeV]}$')
plt.ylabel(r'$\rm{Rapidity}$')

plt.title(r'$\rm{NN\;accuracy}$')
fig.savefig('/Users/jaco/Documents/ML4EFT/code/higgs21/plots/2D_performance_v2.pdf')