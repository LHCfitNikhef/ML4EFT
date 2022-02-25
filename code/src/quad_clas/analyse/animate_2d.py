import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
import os
import torch
import copy
import sys

from . import analyse
from ..preproc import constants

# constants
mz = constants.mz
mh = constants.mh

def animate_learning_2d(mc_reps, path_to_model, network_size, c1, c2, lin=False, quad=False, cross=False, path_sm_data=None):

    # we first define our grid
    s = 14 ** 2
    epsilon = 1e-2
    mvh_min, mvh_max = mz + mh + epsilon, 2
    y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)

    x_spacing, y_spacing = 1e-2, 0.01
    mvh_span = np.arange(mvh_min, mvh_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)

    mvh_grid, y_grid = np.meshgrid(mvh_span, y_span)
    grid = np.c_[mvh_grid.ravel(), y_grid.ravel()]
    grid_unscaled_tensor = torch.Tensor(grid)

    # compute truth
    #coeff_truth = coeff_function_truth(grid, np.array([c1, c2]), lin, quad, cross).reshape(mvh_grid.shape)

    def load_coeff_nn_rep(epoch):
        coeff_nns = []

        # at a given epoch, loop over all the replicas
        for rep_nr in range(0, mc_reps):
            coeff_nn = analyse.coeff_function_nn(x=grid_unscaled_tensor,
                                                 path_to_model=path_to_model.format(mc_run=rep_nr),
                                                 architecture=network_size,
                                                 lin=lin,
                                                 quad=quad,
                                                 cross=cross,
                                                 animate=True,
                                                 epoch=epoch+1).reshape(mvh_grid.shape)

            coeff_nns.append(coeff_nn)

        coeff_nns = np.array(coeff_nns)
        coeff_nn_median = np.percentile(coeff_nns, 50, axis=0)
        return coeff_nn_median
        #coeff_nn_high = np.percentile(coeff_nns, 84, axis=0)
        #coeff_nn_low = np.percentile(coeff_nns, 16, axis=0)
        #coeff_nn_unc = (coeff_nn_high - coeff_nn_low) / 2

    def reference():
        mtt_min, mtt_max = mvh_min * 10**3, 2000.0
        s = (14 * 10 ** 3) ** 2
        reference.y_min, reference.y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
        x_spacing = 10
        y_spacing = 0.01
        # First set up the figure, the axis, and the plot element we want to animate
        reference.f_ana = analyse.coeff_function_truth(grid, np.array([c1, c2]), lin, quad, cross).reshape(mvh_grid.shape)
        reference.f_ana = np.ma.masked_where(reference.f_ana == 1.0, reference.f_ana)

    reference()

    cmap = copy.copy(plt.get_cmap("seismic"))
    cmap.set_bad(color='#c8c9cc')

    fig, ax = plt.subplots(figsize=(10, 8))

    cmap_copy = copy.copy(mpl.cm.get_cmap(cmap))
    bounds = [0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05]
    norm = mpl.colors.BoundaryNorm(bounds, cmap_copy.N, extend='both')

    cmap_copy.set_bad(color='gainsboro')

    img = plt.imshow(np.zeros(reference.f_ana.shape), extent=[mvh_min* 10**3, 2000.0, reference.y_min, reference.y_max],
                     origin='lower', cmap=cmap_copy, aspect=(2000.0 - mvh_min* 10**3) / (reference.y_max - reference.y_min),
                     interpolation='quadric', norm=norm)

    cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_copy), ax=ax)
    cbar.minorticks_on()
    title = r'$\rm{Truth/NN\;(median)}$'
    xlabel = r'$m_{ZH}\;\rm{[GeV]}$'
    ylabel = r'$\rm{Rapidity}$'
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()

    # plt.colorbar()

    #plt.title('NN performance at ctG = {}'.format(ctg))
    epoch_text = ax.text(0.95, 0.95, '', transform=ax.transAxes, horizontalalignment='right')
    #loss_text = ax.text(0.70, 0.90, '', transform=ax.transAxes)
    #loss = np.loadtxt(path + 'loss.out')

    # initialization function: plot the background of each frame
    def init():
        img.set_data(np.zeros(reference.f_ana.shape))
        epoch_text.set_text('')
        #loss_text.set_text('')
        return img, epoch_text#, loss_text

    # animation function.  This is called sequentially

    def animate(epoch):
        sys.stdout.write('\r')
        sys.stdout.flush()
        print(epoch)

        median_nn_epoch = load_coeff_nn_rep(epoch)
        ratio_epoch = reference.f_ana/median_nn_epoch
        img.set_array(ratio_epoch)

        epoch_text.set_text(r'$\rm{Epoch}\;%d$'%epoch)
        #loss_text.set_text('loss = {:.4f}'.format(loss[i]))
        return img, epoch_text#, loss_text

    # call the animator.  blit=True means only re-draw the parts that have changed.
    print("Creating the animation")
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=150, interval=150, blit=True)
    anim.save('/Users/jaco/Documents/ML4EFT/plots/2022/talk_juan/animations/training_animation_chq3.gif')

