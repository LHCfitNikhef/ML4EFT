import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import os

from . import analyse
from ..preproc import constants


# constants
mz = constants.mz
mh = constants.mh

path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW', '/Users/jaco/Documents/ML4EFT/models/lin/cHq3'],
                  'quad': []}

class Animate:

    def __init__(self, architecture, c, path_to_models, mc_runs, save_path, lin=False, quad=False):

        self.architecture = architecture
        self.c = c
        self.path_to_models = path_to_models
        self.lin = lin
        self.quad = quad
        self.mc_runs = mc_runs
        self.save_path = save_path

        self.make_animation()

    def make_animation(self):
        cHW, cHq3 = self.c

        # analytical decision function
        x = np.linspace(mh + mz + 1e-2, 2.5, 100)
        x = np.stack((x, np.zeros(len(x))), axis=-1)
        f_ana = analyse.decision_function_truth(x, np.array([cHW, cHq3]), lin=self.lin, quad=self.quad)
        f_ana_quad = analyse.decision_function_truth(x, np.array([cHW, cHq3]), quad=True)

        fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))

        # load the rescaling parameters (means and std)
        means = []
        stds = []
        for i in range(0, self.mc_runs):
            mean, std = np.loadtxt(os.path.join(self.path_to_models.format(mc_run=i), 'scaling.dat'))
            means.append(mean)
            stds.append(std)

        # create empty line objects
        lines = []
        for i in range(0, self.mc_runs):
            # only attach a label to the first replica to avoid a busy legend
            if i == 1:
                lobj = ax.plot([], [], lw=1, color='C0', label=r'$\rm{NN\;replicas}$')[0]
            else:
                lobj = ax.plot([], [], lw=1, color='C0')[0]
            lines.append(lobj)

        # make the first frame of the animation

        path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}'],
                          'quad': ['/Users/jaco/Documents/ML4EFT/models/quad/cHW/mc_run_{mc_run}']}

        #f_preds_lin_init = analyse.make_predictions_1d(x, np.array([2]), path_to_models, architecture, epoch=1, lin=True)
        f_preds_quad_init = analyse.make_predictions_1d(x, np.array([2]), path_to_models, self.architecture, epoch=1, lin=True)

        # create uncertainty band and plot
        f_preds_quad_init_up = np.percentile(f_preds_quad_init, 84, axis=0)
        f_preds_quad_init_down = np.percentile(f_preds_quad_init, 16, axis=0)

        fill = ax.fill_between(x[:, 0], f_preds_quad_init_up, f_preds_quad_init_down, color='C0', alpha=0.3,
                               label=r'$\rm{NN\;1}\sigma\rm{-band}$')

        ax.plot(x[:, 0], f_ana, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-2}\right)$')
        ax.plot(x[:, 0], f_ana_quad, '--', c='orange', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-4}\right)$')
        epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)

        plt.legend(loc='upper right', fontsize=15, frameon=False)
        plt.ylim((0, 1))

        plt.xlim(np.min(x[:, 0]), np.max(x[:, 0]))
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
            f_preds_quad = analyse.make_predictions_1d(x, np.array([2]), path_to_models, self.architecture, epoch=i+1,
                                                            lin=True)
            for rep_nr, line in enumerate(lines):
                line.set_data(x[:, 0], f_preds_quad[rep_nr, :])

            epoch_text.set_text(r'$\rm{epoch\;%d}$' % i)


            f_pred_up = np.percentile(f_preds_quad, 84, axis=0)
            f_pred_down = np.percentile(f_preds_quad, 16, axis=0)

            path = fill.get_paths()[0]
            verts = path.vertices
            verts[1:x.shape[0] + 1, 1] = f_pred_up[:]
            verts[x.shape[0] + 2:-1, 1] = f_pred_down[:][::-1]
            return lines

        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=200, interval=50, blit=True)

        anim.save(self.save_path)

