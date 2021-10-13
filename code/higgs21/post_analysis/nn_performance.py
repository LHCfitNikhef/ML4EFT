#%%
import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.nn_analyse as analyse
import quad_clas.core.xsec.tt_prod as axs
import quad_clas.core.xsec.vh_prod as vh_prod
import os

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
c = 2
x = np.linspace(mh + mz + 1e-2, 2, 100)
architecture = [1, 30, 30, 30, 30, 30, 1]

fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))
f_ana = axs.plot_likelihood_ratio_1D(x, c)
ax.plot(x, f_ana, '--', c='red', label=r'$\rm{Truth}$')


f_pred_nn = []
for i in range(10):
    model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_lin_2/mc_run_{}'.format(i)
    path_to_model = os.path.join(model_dir, 'trained_nn.pt')

    mean, std = np.loadtxt(os.path.join(model_dir, 'scaling.dat'))
    f_pred = analyse.make_predictions_1d(x, path_to_model, architecture, c, mean, std)
    f_pred_nn.append(f_pred)
f_pred_nn = np.array(f_pred_nn)

f_pred_med = np.percentile(f_pred_nn, 50, axis=0)
f_pred_high = np.percentile(f_pred_nn, 84, axis=0)
f_pred_low = np.percentile(f_pred_nn, 16, axis=0)

plt.fill_between(x, f_pred_high, f_pred_low, color='C0', alpha=0.4, label=r'$\rm{NN}$')
plt.plot(x, f_pred_med, color='C0', linestyle='dotted')
plt.legend()
plt.ylim((0, 1))
plt.ylabel(r'$f\;(m_{VH}, c)$')
plt.xlabel(r'$m_{VH}\;[\mathrm{TeV}]$')
fig.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/nn_rep.pdf')
