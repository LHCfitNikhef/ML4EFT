import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.nn_analyse as analyse
import quad_clas.core.xsec.tt_prod as axs
from matplotlib import animation
import os

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
c = 2
x = np.linspace(mh + mz + 1e-2, 2, 100)
architecture = [1, 30, 30, 30, 30, 30, 1]

fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))
f_ana = axs.plot_likelihood_ratio_1D(x, c)
ax.plot(x, f_ana, '--', c='red', label=r'$\rm{Truth}$')

model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_lin_2/mc_run_{mc_run}'

means = []
stds = []
for i in range(10):
    mean, std = np.loadtxt(os.path.join(model_dir.format(i), 'scaling.dat'))
    means.append(mean)
    stds.append(std)


nn_predictions = [ax.plot([], [], lw=2) for i in range(10)]
epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)

plt.legend(loc='upper right', fontsize=15, frameon=False)

# initialization function: plot the background of each frame
def init():
    for line in nn_predictions:
        line.set_data([], [])
    epoch_text.set_text('')
    return line, epoch_text

# animation function.  This is called sequentially
def animate(i):
    print(i)
    path = os.path.join(model_dir, 'trained_nn_{}.pt'.format(i+1))
    for rep in range(10):
        f_pred = analyse.make_predictions_1d(path.format(mc_run=rep), architecture, c, means[rep], stds[rep])
        nn_predictions[rep].set_data(x, f_pred)
    epoch_text.set_text(r'$\rm{epoch\;%d}$'%i)

    return nn_predictions, epoch_text

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=10, interval=200, blit=True)

anim.save('/data/theorie/jthoeve/ML4EFT_higgs/plots/anim.gif')