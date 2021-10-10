#%%
import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.nn_analyse as analyse
import quad_clas.core.xsec.tt_prod as axs
import quad_clas.core.xsec.vh_prod as vh_prod
import os

model_dir = '/Users/jaco/Documents/ML4EFT/code/higgs21/models/model_cHW_lin/mc_run_4/'
path_to_model = os.path.join(model_dir, 'trained_nn.pt')

mean, std = np.loadtxt(os.path.join(model_dir, 'scaling.dat'))
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
c = 2
x = np.linspace(mh + mz + 1e-2, 2, 100)
architecture = [1, 30, 30, 30, 30, 30, 1]

f_pred = analyse.make_predictions_1d(x, path_to_model, architecture, c, mean, std)
f_ana = axs.plot_likelihood_ratio_1D(x, c)

fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))
ax = plt.axes(ylim=(0, 1))
ax.plot(x, f_ana, '--', c='red', label=r'$\rm{Truth}$')
ax.plot(x, f_pred, lw=2, label=r'$\rm{NN}$')
plt.legend()

plt.ylabel(r'$f\;(m_{VH}, c)$')
plt.xlabel(r'$m_{VH}\;[\mathrm{TeV}]$')
# plt.xlim((mtt_min, mtt_max))
plt.ylim((0, 1))
plt.show()