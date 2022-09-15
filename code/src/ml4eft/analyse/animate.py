import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import os
import pandas as pd
import matplotlib as mpl
import copy
import sys
from . import analyse
from ..preproc import constants


# constants
mz = constants.mz
mh = constants.mh
mt = constants.mt


class Animate:

    def __init__(self, c, frames):

        self.c = c
        self.frames = frames


    def make_animation_1d(self, analyser, df):

        g_ana = analyser.decision_function_truth(df, self.c, df.columns.values, process='tt', order='quad')
        #f_ana_lin = analyse.decision_function_truth(df, self.c, n_kin=2, process='tt', lin=True, quad=False)
        #f_ana_quad = analyse.decision_function_truth(df, self.c, quad=True)

        fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))

        # make the first frame of the animation

        #f_preds_lin_init = analyse.likelihood_ratio_nn(x, np.array([2]), path_to_models, architecture, epoch=1, lin=True)


        # load models and evaluate them
        analyser.build_model_dict(epoch=1)
        analyser.evaluate_models(df, epoch=1)

        # decission function at first epoch
        g_nn_init = analyser.decision_function_nn(self.c, epoch=1)

        # f_preds_lin_init = analyse.decision_function_nn(df, self.c, self.c_train,
        #                                                 self.path_to_models,
        #                                                 epoch=1,
        #                                                 lin=self.lin,
        #                                                 quad=self.quad)


        # create empty line objects
        lines = []
        n_reps = g_nn_init.shape[0]


        for i in range(0, n_reps):
            # only attach a label to the first replica to avoid a busy legend
            if i == 1:
                lobj = ax.plot([], [], lw=1, color='C0', label=r"$\mathrm{ML}\;\mathrm{model}\;(m_{t\bar{t}}, Y)$")[0]
            else:
                lobj = ax.plot([], [], lw=1, color='C0')[0]
            lines.append(lobj)

        # create uncertainty band and plot
        g_preds_init_up = np.percentile(g_nn_init, 84, axis=0)
        g_preds_init_down = np.percentile(g_nn_init, 16, axis=0)


        fill = ax.fill_between(df['m_tt'], g_preds_init_up, g_preds_init_down, color='C0', alpha=0.3,
                               label=r"$\mathrm{ML}\;\mathrm{model}\;1\sigma\mathrm{-band}\;(m_{t\bar{t}}, Y)$")

        ax.plot(df['m_tt'], g_ana, '--', c='red', label=r"$\mathrm{Analytical}\;(m_{t\bar{t}}, Y)$")
        #ax.plot(x[:, 0], f_ana_lin, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-4}\right)$')
        #ax.plot(x[:, 0], f_ana_quad, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-4}\right)$')
        epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)

        plt.legend(loc='upper right', fontsize=15, frameon=False)
        plt.ylim((0, 1))

        #plt.xlim(np.min(x[:, 0]), 0.5)
        plt.xlim(0.5, df['m_tt'].max())
        #plt.xlim(np.min(x[:, 0]), np.max(x[:, 0]))
        plt.ylabel(r'$g\;(x, c)$')
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

            analyser.build_model_dict(epoch=i+1)
            analyser.evaluate_models(df)
            g_preds_nn = analyser.decision_function_nn(self.c)

            for rep_nr, line in enumerate(lines):
                line.set_data(df['m_tt'], g_preds_nn[rep_nr, :])

            epoch_text.set_text(r'$\rm{epoch\;%d}$' % i)


            g_pred_up = np.percentile(g_preds_nn, 84, axis=0)
            g_pred_down = np.percentile(g_preds_nn, 16, axis=0)

            path = fill.get_paths()[0]

            verts = path.vertices
            verts[1:len(df) + 1, 1] = g_pred_up[:]
            verts[len(df) + 2:-1, 1] = g_pred_down[:][::-1]
            return lines

        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=self.frames, interval=50, blit=True)

        return anim

    def make_animation_2d(self, analyser, df, c_name, order, process, shape):

        coeff_function_ana = analyser.coeff_function_truth(df, c_name, df.columns.values, process, order).reshape(shape)
        np.ma.masked_where(coeff_function_ana == 1.0, coeff_function_ana) # necessary?

        def load_coeff_nn_rep(analyser, df, epoch, order):

            analyser.build_model_dict(epoch=epoch)
            analyser.evaluate_models(df)

            coeff_nn = analyser.models_evaluated_df.loc[order, c_name]['models']

            coeff_nn_median = np.percentile(coeff_nn, 50, axis=0)
            return coeff_nn_median

        cmap = copy.copy(plt.get_cmap("seismic"))
        cmap.set_bad(color='#c8c9cc')

        fig, ax = plt.subplots(figsize=(10, 8))

        cmap_copy = copy.copy(mpl.cm.get_cmap(cmap))
        bounds = [0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05]
        norm = mpl.colors.BoundaryNorm(bounds, cmap_copy.N, extend='both')

        cmap_copy.set_bad(color='gainsboro')

        img = plt.imshow(np.zeros(coeff_function_ana.shape),
                         extent=[df['m_tt'].min() * 10 ** 3, 2000.0, df['y'].min(), df['y'].max()],
                         origin='lower', cmap=cmap_copy,
                         aspect=(2000.0 -df['m_tt'].min() * 10 ** 3) / ( df['y'].max() - df['y'].min()),
                         interpolation='quadric', norm=norm)

        cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_copy), ax=ax)
        cbar.minorticks_on()
        title = r'$\rm{Truth/NN\;(median)}$'
        xlabel = r'$m_{t\bar{t}}\;\rm{[GeV]}$'
        ylabel = r'$\rm{Rapidity}$'
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.tight_layout()

        # plt.colorbar()

        # plt.title('NN performance at ctG = {}'.format(ctg))
        epoch_text = ax.text(0.95, 0.95, '', transform=ax.transAxes, horizontalalignment='right')

        # loss_text = ax.text(0.70, 0.90, '', transform=ax.transAxes)
        # loss = np.loadtxt(path + 'loss.out')

        # initialization function: plot the background of each frame
        def init():
            img.set_data(np.zeros(coeff_function_ana.shape))
            epoch_text.set_text('')
            # loss_text.set_text('')
            return img, epoch_text  # , loss_text

        # animation function.  This is called sequentially

        def animate(epoch):
            sys.stdout.write('\r')
            sys.stdout.flush()
            print(epoch)

            median_nn_epoch = load_coeff_nn_rep(analyser, df, epoch, order).reshape(shape)

            ratio_epoch = coeff_function_ana / median_nn_epoch
            img.set_array(ratio_epoch)

            epoch_text.set_text(r'$\rm{Epoch}\;%d$' % epoch)
            # loss_text.set_text('loss = {:.4f}'.format(loss[i]))
            return img, epoch_text  # , loss_text

        # call the animator.  blit=True means only re-draw the parts that have changed.
        print("Creating the animation")
        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                       frames=self.frames, interval=150, blit=True)
        return anim
        #anim.save('/Users/jaco/Documents/ML4EFT/plots/2022/talk_juan/animations/training_animation_chq3.gif')

