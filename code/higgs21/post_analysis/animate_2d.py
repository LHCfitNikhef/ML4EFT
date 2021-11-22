import copy
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import sys, os
import torch

import quad_clas.core.truth.vh_prod as vh_prod
import quad_clas.core.classifier as quad_classifier_cluster
from quad_clas.core.truth import tt_prod as axs

def likelihood_ratio(y, mvh, c, lin, quad):
    """
    Compute the 2D analytic likelihood ratio r(x, c)
    """
    dsigma_0 = vh_prod.dsigma_dmvh_dy(y, mvh, c, 0, lin, quad) # EFT
    dsigma_1 = vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin, quad)  # SM
    ratio = dsigma_0 / dsigma_1 if dsigma_1 != 0 else 0
    return ratio

def f_analytic(mvh, y, c, lin, quad):
    r = likelihood_ratio(y, mvh, c, lin, quad)
    return 1/(1+r)

def plot_f_ana(mvh_min, mvh_max, y_min, y_max, x_spacing, y_spacing, c, lin, quad):

    # Important to include otypes = [np.float], else all the output is int by default
    vf_ana = np.vectorize(f_analytic, otypes=[np.float])
    x = np.arange(mvh_min, mvh_max, x_spacing)
    y = np.arange(y_min, y_max, y_spacing)
    xx, yy = np.meshgrid(x, y)
    Z = vf_ana(xx, yy, c, lin, quad)
    return Z



s = 14 ** 2
mvh_min, mvh_max = 0.3, 2
y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)
c=2

network_size = [2, 30, 30, 30, 30, 30, 1]
model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW3_lin_2_feat/mc_run_{mc_run}'
mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=0), 'scaling.dat'))

x_spacing, y_spacing = 1e-2, 0.01
x_span = np.arange(mvh_min, mvh_max, x_spacing)
y_span = np.arange(y_min, y_max, y_spacing)

xx, yy = np.meshgrid(x_span, y_span)
grid_unscaled = torch.Tensor(np.c_[xx.ravel(), yy.ravel()])


def reference():
    reference.y_min, reference.y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)
    x_spacing = 1e-2
    y_spacing = 0.01
    # First set up the figure, the axis, and the plot element we want to animate
    reference.f_ana = plot_f_ana(mvh_min, mvh_max, y_min, y_max, x_spacing, y_spacing, c, True, False)
    reference.f_ana = np.ma.masked_where(reference.f_ana == 1.0, reference.f_ana)

reference()

cmap = copy.copy(plt.get_cmap("seismic"))
cmap.set_bad(color='#c8c9cc')
#cmap.set_bad(color='white')

fig, ax = plt.subplots(figsize=(8,8))
img = plt.imshow(np.zeros(reference.f_ana.shape), extent=[0.3, 2.0, reference.y_min, reference.y_max],
                 origin='lower', cmap=cmap, aspect=(2.0 - 0.3) / (reference.y_max - reference.y_min),
                 interpolation='quadric', vmin=0.8, vmax=1.2)
cbar = fig.colorbar(img, ax=ax, shrink=0.8, extend='both')
cbar.minorticks_on()
plt.xlabel(r'$m_{ZH}\;\rm{[TeV]}$')
plt.ylabel(r'$\rm{Rapidity}$')
plt.title(r'$\rm{Truth/NN}\;\rm{prediction}$')
epoch_text = ax.text(0.65, 0.90, '', transform=ax.transAxes)
#loss_text = ax.text(0.70, 0.90, '', transform=ax.transAxes)
#loss = np.loadtxt(path + 'loss.out')

# initialization function: plot the background of each frame
def init():
    img.set_data(np.zeros(reference.f_ana.shape))
    epoch_text.set_text('')
    #loss_text.set_text('')
    return img, epoch_text#, loss_text

# animation function.  This is called sequentially

def animate(i):
    print(i)
    sys.stdout.write('\r')
    sys.stdout.flush()


    loaded_model = quad_classifier_cluster.PredictorLinear(network_size)
    network_path = os.path.join(model_dir.format(mc_run=0), 'trained_nn_{}.pt'.format(i+1))

    # load all the parameters into the trained network
    if os.path.isfile(network_path):
        loaded_model.load_state_dict(torch.load(network_path))
    else:
        network_path = os.path.join(model_dir.format(mc_run=0), 'trained_nn.pt')
        loaded_model.load_state_dict(torch.load(network_path))

    grid = (grid_unscaled - mean) / std

    f_pred = loaded_model.forward(grid.float(), c)
    f_pred = f_pred.view(xx.shape).detach().numpy()

    img.set_array(reference.f_ana / f_pred)
    epoch_text.set_text(r'$\rm{epoch=%d}$'%i)
    #loss_text.set_text('loss = {:.4f}'.format(loss[i]))
    return img, epoch_text#, loss_text

# call the animator.  blit=True means only re-draw the parts that have changed.
print("Creating the animation")
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=250, interval=50, blit=True)
anim.save('/data/theorie/jthoeve/ML4EFT_higgs/plots/training_2d_v3.gif')
