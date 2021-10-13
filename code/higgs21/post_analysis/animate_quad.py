import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.nn_analyse as analyse
import quad_clas.core.xsec.tt_prod as axs
from matplotlib import animation
import os

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
c = 2
x = np.linspace(0.3, 1.2, 100)
architecture = [1, 30, 30, 30, 30, 30, 1]

fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))
f_ana = axs.plot_likelihood_ratio_1D(x, c, quad=True)
f_ana_lin = axs.plot_likelihood_ratio_1D(x, c, lin=True)
ax.plot(x, f_ana, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-4}\right)$')
ax.plot(x, f_ana_lin, '--', c='C1', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-2}\right)$')

model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW3_quad_4/mc_run_{mc_run}'

means = []
stds = []
for i in range(10):
    mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=i), 'scaling.dat'))
    means.append(mean)
    stds.append(std)


lines = []
for i in range(10):
    if i == 0:
        lobj = ax.plot([], [], lw=1, color='C0', label=r'$\rm{NN\;replicas}$')[0]
    else:
        lobj = ax.plot([], [], lw=1, color='C0')[0]
    lines.append(lobj)

f_preds_init = []
for rep_nr, line in enumerate(lines):
    path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn_{}.pt'.format(1))
    path_lin = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_lin_3/mc_run_{mc_run}/trained_nn.pt'.format(mc_run=rep_nr)
    f_pred = analyse.make_predictions_1d(x, path.format(mc_run=rep_nr), architecture, c, means[rep_nr], stds[rep_nr], path_lin)
    f_preds_init.append(f_pred)
f_preds_init = np.array(f_preds_init)
f_pred_up = np.percentile(f_preds_init, 84, axis=0)
f_pred_down = np.percentile(f_preds_init, 16, axis=0)
fill = ax.fill_between(x, f_pred_up, f_pred_down, color='C0', alpha=0.3, label=r'$\rm{NN\;1}\sigma\rm{-band}$')

epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)

plt.legend(loc='upper right', fontsize=15, frameon=False)
plt.ylim((0, 1))
plt.xlim(np.min(x), np.max(x))
plt.ylabel(r'$f\;(x, c)$')
plt.xlabel(r'$m_{ZH}\;[\mathrm{TeV}]$')

# initialization function: plot the background of each frame
def init():
    for line in lines:
        line.set_data([], [])
    epoch_text.set_text('')
    return lines

# animation function.  This is called sequentially
def animate(i):
    print(i)
    f_preds = []

    for rep_nr, line in enumerate(lines):
        path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn_{}.pt'.format(i + 1))
        path_lin = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_lin_3/mc_run_{mc_run}/trained_nn.pt'.format(
            mc_run=rep_nr)

        if os.path.isfile(path):
            f_pred = analyse.make_predictions_1d(x, path.format(mc_run=rep_nr), architecture, c, means[rep_nr], stds[rep_nr], path_lin)
            f_preds.append(f_pred)
            line.set_data(x, f_pred)
        else: # at the end of training
            path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt'.format(i + 1))
            f_pred = analyse.make_predictions_1d(x, path.format(mc_run=rep_nr), architecture, c, means[rep_nr],
                                                 stds[rep_nr], path_lin)
            f_preds.append(f_pred)
            line.set_data(x, f_pred)

    epoch_text.set_text(r'$\rm{epoch\;%d}$' % i)

    f_preds = np.array(f_preds)
    f_pred_up = np.percentile(f_preds, 84, axis=0)
    f_pred_down = np.percentile(f_preds, 16, axis=0)

    path = fill.get_paths()[0]
    verts = path.vertices
    verts[1:len(x)+1, 1] = f_pred_up[:]
    verts[len(x) + 2:-1, 1] = f_pred_down[:][::-1]

    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=50, blit=True)

anim.save('/data/theorie/jthoeve/ML4EFT_higgs/plots/anim_band_quad_cHW_v2.gif')