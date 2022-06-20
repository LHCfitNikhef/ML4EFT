import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import os
import pandas as pd

from . import analyse
from ..preproc import constants


# constants
mz = constants.mz
mh = constants.mh
mt = constants.mt


class Animate:

    def __init__(self, architecture, c, c_train, path_to_models, save_path, frames, lin=False, quad=False):

        self.architecture = architecture
        self.c = c
        self.path_to_models = path_to_models
        self.lin = lin
        self.quad = quad
        self.save_path = save_path
        self.frames = frames
        self.c_train = c_train
        #self.make_animation()

    def make_animation(self):
        cHW, cHq3 = self.c

        # analytical decision function
        #x = np.linspace(mh + mz + 1e-2, 2.5, 100)
        #x = np.linspace(2 * mt + 1e-2, 3.0, 200)
        x = np.linspace(0.5, 3.0, 200)
        x = np.stack((x, np.zeros(len(x))), axis=-1)
        #x = np.stack((x, 2* np.ones(len(x))), axis=-1)

        df = pd.DataFrame(x, columns=['m_tt', 'y'])
        f_ana_lin = analyse.decision_function_truth(df, self.c, n_kin=2, process='tt', lin=True, quad=False)
        #f_ana_quad = analyse.decision_function_truth(df, self.c, quad=True)

        fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))

        # make the first frame of the animation

        #f_preds_lin_init = analyse.likelihood_ratio_nn(x, np.array([2]), path_to_models, architecture, epoch=1, lin=True)

        f_preds_lin_init = analyse.decision_function_nn(df, self.c, self.c_train,
                                                        self.path_to_models,
                                                        epoch=1,
                                                        lin=self.lin,
                                                        quad=self.quad)


        # create empty line objects
        lines = []
        n_reps = f_preds_lin_init.shape[0]
        for i in range(0, n_reps):
            # only attach a label to the first replica to avoid a busy legend
            if i == 1:
                lobj = ax.plot([], [], lw=1, color='C0', label=r'$\rm{NN\;replicas}$')[0]
            else:
                lobj = ax.plot([], [], lw=1, color='C0')[0]
            lines.append(lobj)

        # create uncertainty band and plot
        f_preds_quad_init_up = np.percentile(f_preds_lin_init, 84, axis=0)
        f_preds_quad_init_down = np.percentile(f_preds_lin_init, 16, axis=0)


        fill = ax.fill_between(x[:, 0], f_preds_quad_init_up, f_preds_quad_init_down, color='C0', alpha=0.3,
                               label=r'$\rm{NN\;1}\sigma\rm{-band}$')

        ax.plot(x[:, 0], f_ana_lin, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-2}\right)$')
        #ax.plot(x[:, 0], f_ana_lin, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-4}\right)$')
        #ax.plot(x[:, 0], f_ana_quad, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-4}\right)$')
        epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)

        plt.legend(loc='upper right', fontsize=15, frameon=False)
        plt.ylim((-0.5, 1.5))
        #plt.xlim(np.min(x[:, 0]), 0.5)
        plt.xlim(0.5, np.max(x[:, 0]))
        #plt.xlim(np.min(x[:, 0]), np.max(x[:, 0]))
        plt.ylabel(r'$f\;(x, c)$')
        #plt.xlabel(r'$m_{ZH}\;[\mathrm{TeV}]$')
        plt.xlabel(r'$m_{t\bar{t}}\;[\mathrm{TeV}]$')
        plt.tight_layout()

        # initialization function: plot the background of each frame
        def init():
            for line in lines:
                line.set_data([], [])
            epoch_text.set_text('')
            return lines

        # animation function.  This is called sequentially
        def animate(i):
            print(i)
            f_preds_nn = analyse.decision_function_nn(df, self.c, self.c_train, self.path_to_models, epoch=i + 1,
                                                       lin=self.lin, quad=self.quad)
            for rep_nr, line in enumerate(lines):
                line.set_data(x[:, 0], f_preds_nn[rep_nr, :])

            epoch_text.set_text(r'$\rm{epoch\;%d}$' % i)


            f_pred_up = np.percentile(f_preds_nn, 84, axis=0)
            f_pred_down = np.percentile(f_preds_nn, 16, axis=0)

            path = fill.get_paths()[0]
            verts = path.vertices
            verts[1:x.shape[0] + 1, 1] = f_pred_up[:]
            verts[x.shape[0] + 2:-1, 1] = f_pred_down[:][::-1]
            return lines

        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=self.frames, interval=50, blit=True)

        anim.save(self.save_path)

