import numpy as np
import matplotlib.pyplot as plt
import ml4eft.analyse.analyse as analyse
from matplotlib import animation
import os

# constants
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
architecture = [2, 30, 30, 30, 30, 30, 1]

# EFT point
cHW = 2
cHq3 = 0

# analytical decision function
x = np.linspace(mh + mz + 1e-2, 2.5, 100)
x = np.stack((x, np.zeros(len(x))), axis=-1)
f_ana = analyse.decision_function_truth(x, np.array([cHW, cHq3]), lin=True, quad=False)

# path to nn models
model_dir = '/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}'


fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))

# load the rescaling parameters (means and std)
means = []
stds = []
for i in range(0, 30):
    mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=i), 'scaling.dat'))
    means.append(mean)
    stds.append(std)

# create empty line objects
lines = []
for i in range(0, 30):
    # only attach a label to the first replica to avoid a busy legend
    if i == 1:
        lobj = ax.plot([], [], lw=1, color='C0', label=r'$\rm{NN\;replicas}$')[0]
    else:
        lobj = ax.plot([], [], lw=1, color='C0')[0]
    lines.append(lobj)

# make the first frame of the animation
f_preds_init = []
for rep_nr, line in enumerate(lines):
    path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn_1.pt')
    f_pred = analyse.make_predictions_1d_old(x, path.format(mc_run=rep_nr), architecture, cHW, cHq3, means[rep_nr],
                                         stds[rep_nr], None, None, None, None)
    if f_pred[-1] == 0.5:
        continue
    f_preds_init.append(f_pred)

# create uncertainty band and plot
f_preds_init = np.array(f_preds_init)
f_pred_up = np.percentile(f_preds_init, 84, axis=0)
f_pred_down = np.percentile(f_preds_init, 16, axis=0)
fill = ax.fill_between(x[:,0], f_pred_up, f_pred_down, color='C0', alpha=0.3, label=r'$\rm{NN\;1}\sigma\rm{-band}$')

ax.plot(x[:,0], f_ana, '--', c='red', label=r'$\rm{Truth}$')
epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)

plt.legend(loc='upper right', fontsize=15, frameon=False)
plt.ylim((0, 1))

plt.xlim(np.min(x[:,0]), np.max(x[:,0]))
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
        if os.path.isfile(path):

            f_pred = analyse.make_predictions_1d_old(x, path.format(mc_run=rep_nr), architecture, cHW, cHq3, means[rep_nr],
                                                 stds[rep_nr], None, None, None, None)
            if f_pred[-1] == 0.5:
                continue
            f_preds.append(f_pred)
            line.set_data(x[:,0], f_pred)
        else: # at the end of training

            path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt'.format(i + 1))
            f_pred = analyse.make_predictions_1d_old(x, path.format(mc_run=rep_nr), architecture, cHW, cHq3, means[rep_nr],
                                                 stds[rep_nr], None, None, None, None)
            if f_pred[-1] == 0.5:
                continue
            f_preds.append(f_pred)
            line.set_data(x[:,0], f_pred)

    epoch_text.set_text(r'$\rm{epoch\;%d}$' % i)

    f_preds = np.array(f_preds)
    f_pred_up = np.percentile(f_preds, 84, axis=0)
    f_pred_down = np.percentile(f_preds, 16, axis=0)

    path = fill.get_paths()[0]
    verts = path.vertices
    verts[1:x.shape[0]+1, 1] = f_pred_up[:]
    verts[x.shape[0] + 2:-1, 1] = f_pred_down[:][::-1]
    return lines


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=50, blit=True)

anim.save('/Users/jaco/Documents/ML4EFT/plots/29_11/anim_band_cHW_lin.gif')