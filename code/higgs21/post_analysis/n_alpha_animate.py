import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.nn_analyse as analyse
import quad_clas.core.xsec.tt_prod as axs
from matplotlib import animation
import os
import quad_clas.core.xsec.vh_prod as vh_prod
from quad_clas.core.quad_classifier_cluster import PredictorCross, PredictorLinear, PredictorQuadratic
import torch

path_lin_1 = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW3_lin_30_reps/'
n_models = 30
mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
cHW = 2
cHq3 = 0
x = np.array([np.linspace(0.3, 3, 300), np.zeros(300)]).T
architecture = [2, 30, 30, 30, 30, 30, 1]

fig, ax = plt.subplots(figsize=(1.1 * 10, 1.1 * 6))

#f_ana = axs.plot_likelihood_ratio_1D(x, cHW, cHq3, lin=True, quad=False)


model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_cHW_lin_2_feat_relu/mc_run_{mc_run}'

means = []
stds = []
for i in range(1, 31):
    mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=i), 'scaling.dat'))
    means.append(mean)
    stds.append(std)


lines = []
for i in range(1, 31):
    if i == 1:
        lobj = ax.plot([], [], lw=1, color='C0', label=r'$\rm{NN\;replicas}$')[0]
    else:
        lobj = ax.plot([], [], lw=1, color='C0')[0]
    lines.append(lobj)

def get_truth_ratio(x, c1, c2, lin, quad):
    sm_diff_xsec = vh_prod.dsigma_dmvh_dy(0, x, 0, 0, lin=True, quad=False)
    eft_diff_xsec = vh_prod.dsigma_dmvh_dy(0, x, c1, c2, lin=lin, quad=quad)

    return eft_diff_xsec/sm_diff_xsec


n_alphas_init = []
for rep_nr, line in enumerate(lines):
    path = os.path.join(model_dir.format(mc_run=rep_nr + 1), 'trained_nn_{}.pt'.format(1))
    n_lin_1 = PredictorLinear(architecture)
    n_lin_1.load_state_dict(torch.load(path.format(mc_run=rep_nr)))

    x_scaled = (x - means[rep_nr]) / stds[rep_nr]
    x_scaled = torch.tensor(x_scaled)
    n_lin_1_out = n_lin_1.n_alpha(x_scaled.float())
    n_alpha = n_lin_1_out.detach().numpy().flatten()
    n_alphas_init.append(n_alpha)

n_alphas_init = np.array(n_alphas_init)
n_alpha_up = np.percentile(n_alphas_init, 84, axis=0)
n_alpha_down = np.percentile(n_alphas_init, 16, axis=0)

fill = ax.fill_between(x[:,0].flatten(), n_alpha_up, n_alpha_down, color='C0', alpha=0.3, label=r'$\rm{NN\;1}\sigma\rm{-band}$')

ana = (np.array([get_truth_ratio(mvh, 10, 0, lin=True, quad=False) for mvh in np.linspace(0.3, 3, 300)])-1)/10
ax.plot(x[:, 0], ana, linestyle='dashed', color='red',label=r'$\rm{Truth}$')

epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)

plt.legend(loc='upper right', fontsize=15, frameon=False)
plt.ylim((0, 3))
plt.xlim(np.min(x), np.max(x))
plt.ylabel(r'$n_{\alpha}\;(x, c)$')
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
    n_alphas = []

    for rep_nr, line in enumerate(lines):
        path = os.path.join(model_dir.format(mc_run=rep_nr + 1), 'trained_nn_{}.pt'.format(i + 1))
        if os.path.isfile(path):

            n_lin_1 = PredictorLinear(architecture)
            n_lin_1.load_state_dict(torch.load(path.format(mc_run=rep_nr)))

            x_scaled = (x - means[rep_nr]) / stds[rep_nr]
            x_scaled = torch.tensor(x_scaled)
            n_lin_1_out = n_lin_1.n_alpha(x_scaled.float())
            n_alpha = n_lin_1_out.detach().numpy().flatten()

            n_alphas.append(n_alpha)
            line.set_data(x[:,0].flatten(), n_alpha)
        else: # at the end of training
            path = os.path.join(model_dir.format(mc_run=rep_nr + 1), 'trained_nn.pt')
            n_lin_1 = PredictorLinear(architecture)
            n_lin_1.load_state_dict(torch.load(path.format(mc_run=rep_nr)))

            x_scaled = (x - means[rep_nr]) / stds[rep_nr]
            x_scaled = torch.tensor(x_scaled)
            n_lin_1_out = n_lin_1.n_alpha(x_scaled.float())
            n_alpha = n_lin_1_out.detach().numpy().flatten()
            n_alphas.append(n_alpha)
            line.set_data(x[:,0].flatten(), n_alpha)

    epoch_text.set_text(r'$\rm{epoch\;%d}$' % i)

    n_alphas = np.array(n_alphas)
    n_alpha_up = np.percentile(n_alphas, 84, axis=0)
    n_alpha_down = np.percentile(n_alphas, 16, axis=0)

    path = fill.get_paths()[0]
    verts = path.vertices
    verts[1:len(x)+1, 1] = n_alpha_up[:]
    verts[len(x) + 2:-1, 1] = n_alpha_down[:][::-1]

    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=400, interval=50, blit=True)

anim.save('/data/theorie/jthoeve/ML4EFT_higgs/plots/anim_band_n_alpha_lin_2_feat_relu.gif')