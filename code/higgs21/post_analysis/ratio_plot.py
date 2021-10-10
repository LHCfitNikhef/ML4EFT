#%%
import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.nn_analyse as analyse
import quad_clas.core.xsec.tt_prod as axs
import quad_clas.core.xsec.vh_prod as vh_prod

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
mvh_min, mvh_max = mz + mh, 1.0
x = np.arange(mvh_min + 1e-2, mvh_max, 1e-2)
eft = np.array([vh_prod.dsigma_dmvh(mvh, [2,0], True, False) for mvh in x])
sm = np.array([vh_prod.dsigma_dmvh(mvh, [0,0], True, False) for mvh in x])
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