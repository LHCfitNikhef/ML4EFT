# This module contains all necessary functions to analyse and process the models


# import standard packages
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np
import torch
import sys
import copy
import matplotlib.gridspec as gridspec
from matplotlib import animation
import os

# import own pacakges
from quad_clas.core import classifier as quad_clas
from quad_clas.core.truth import tt_prod as axs
from quad_clas.core.truth import vh_prod

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125

# matplotlib.use('PDF')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


def likelihood_ratio_truth(x, c, lin=False, quad=False):
    """
    Compute the 1D analytic likelihood ratio r(x, c)

    Parameters
    ----------
    x : numpy.ndarray, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c : numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.
    """

    n_kin = x.shape[1]
    cHW, cHq3 = c

    if n_kin == 1:
        dsigma_0 = [vh_prod.dsigma_dmvh(x_i, cHW, cHq3, lin=lin, quad=quad) for x_i in x]  # EFT
        dsigma_1 = [vh_prod.dsigma_dmvh(x_i, 0, 0, lin=lin, quad=quad) for x_i in x]  # SM
    elif n_kin == 2:
        dsigma_0 = [vh_prod.dsigma_dmvh_dy(y, mvh, cHW, cHq3, lin=lin, quad=quad) for (mvh, y) in x]  # EFT
        dsigma_1 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin=lin, quad=quad) for (mvh, y) in x]  # SM
    else:
        raise NotImplementedError("No more than two features are currently supported")

    dsigma_0, dsigma_1 = np.array(dsigma_0), np.array(dsigma_1)

    ratio = np.divide(dsigma_0, dsigma_1, out=np.zeros_like(dsigma_0), where=dsigma_1 != 0)
    # ratio = dsigma_0 / dsigma_1

    return ratio.flatten()


def decision_function_truth(x, c, lin=False, quad=False):
    ratio = likelihood_ratio_truth(x, c, lin, quad)
    return 1 / (1 + ratio)


def likelihood_ratio_nn(x, c, path_to_models, architecture, mc_run, lin=False, quad=False):
    """

    Parameters
    ----------
    x : numpy.ndarray, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c : numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    path_to_models: dict
        Path to the nn model root directory
    mc_run: int
        Monte Carlo replica number
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.

    Returns
    -------

    """
    cHW, cHq3 = c

    path_nn_lin = path_to_models['lin']  # shape = (len(c), )
    # path_nn_quad = path_to_models['quad'] # shape = (len(c), )
    # path_nn_cross = path_to_models['cross'] # TODO: shape

    with torch.no_grad():
        n_lin_1 = quad_clas.PredictorLinear(architecture)

        path_nn_lin_1 = os.path.join(path_nn_lin[0], 'mc_run_{}', 'trained_nn.pt')
        n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))
        mean, std = np.loadtxt(os.path.join(path_nn_lin[0], 'mc_run_{}'.format(mc_run), 'scaling.dat'))

        x_scaled = (x - mean) / std
        n_lin_1_out = n_lin_1.n_alpha(x_scaled.float())

        #######

        n_lin_2 = quad_clas.PredictorLinear(architecture)

        path_nn_lin_2 = os.path.join(path_nn_lin[1], 'mc_run_{}', 'trained_nn.pt')
        n_lin_2.load_state_dict(torch.load(path_nn_lin_2.format(mc_run)))
        mean, std = np.loadtxt(os.path.join(path_nn_lin[1], 'mc_run_{}'.format(mc_run), 'scaling.dat'))

        x_scaled = (x - mean) / std
        n_lin_2_out = n_lin_2.n_alpha(x_scaled.float())

        ########

        # n_quad_1 = PredictorQuadratic(architecture)
        # n_quad_1.load_state_dict(torch.load(path_nn_quad_1.format(mc_run)))
        #
        # mean, std = np.loadtxt(os.path.join(path_quad_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        # x_scaled = (x - mean) / std
        # n_quad_1_out = n_quad_1.n_beta(x_scaled.float()) ** 2
        #
        # #######
        #
        # n_quad_2 = PredictorQuadratic(architecture)
        # n_quad_2.load_state_dict(torch.load(path_nn_quad_2.format(mc_run)))
        #
        # mean, std = np.loadtxt(os.path.join(path_quad_2, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        # x_scaled = (x - mean) / std
        # n_quad_2_out = n_quad_2.n_beta(x_scaled.float()) ** 2
        #
        # #######
        #
        # n_cross = PredictorCross(architecture)
        # n_cross.load_state_dict(torch.load(path_nn_cross.format(mc_run)))
        #
        # mean, std = np.loadtxt(os.path.join(path_cross, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        # x_scaled = (x - mean) / std
        # n_cross_out = n_cross.n_gamma(x_scaled.float()) ** 2

    # r = 1 + c1 * n_lin_1_out + c2 * n_lin_2_out #+ c1 ** 2 * n_quad_1_out + c2 ** 2 * n_quad_2_out + c1 * c2 * n_cross_out

    # r = 1 + cHW * n_lin_1_out + cHq3 * n_lin_2_out
    r = 1 + cHq3 * n_lin_2_out
    # lin_nn = [n_lin_1_out, n_lin_2_out]

    return r  # , [lin_nn]


def decision_function_nn(x, c, mc_run, lin=False, quad=False):
    ratio = likelihood_ratio_nn(x, c, lin, quad)
    return 1 / (1 + ratio)


def plot_heatmap(im, xlabel, ylabel, title, extent, bounds, cmap='GnBu'):
    # discrete colorbar
    cmap_copy = copy.copy(mpl.cm.get_cmap(cmap))

    norm = mpl.colors.BoundaryNorm(bounds, cmap_copy.N, extend='both')

    cmap_copy.set_bad(color='gainsboro')

    # continious colormap

    # cmap = copy.copy(plt.get_cmap(cmap))
    # cmap.set_bad(color='white')
    # cmap.set_over("#FFAF33")
    # cmap.set_under("#FFAF33")

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(im, extent=extent,
              origin='lower', cmap=cmap_copy, aspect=(extent[1] - extent[0]) / (extent[-1] - extent[-2]), norm=norm)

    cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_copy), ax=ax)

    cbar.minorticks_on()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    return fig


def coeff_comp_rep(path_model, network_size, c1, c2):
    """
    Compares the EFT coefficient function of the replica stored at ``path_model`` with the truth. The ratio is plotted
    and returned as a matplotlib figure.

    Parameters
    ----------
    path_model: str
        Path to model replica
    network_size: list
        The architecture of the model, e.g.

        .. math::

            [n_i, 10, 15, 5, n_f],

        where :math:`n_i` and :math:`n_f` denote the number of input features and output target values respectively.

    c1: float
        Value of the 1st EFT coefficient used during training
    c2: float
        Value of the 2nd EFT coefficient used during training

    Returns
    -------
    `matplotlib.figure.Figure`
    """

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

    # truth
    if c1 != 0:
        ratio_truth_c1 = likelihood_ratio_truth(grid, np.array([10, 0]), lin=True)
        mask = ratio_truth_c1 == 0
        coeff_truth = np.ma.masked_where(mask, (ratio_truth_c1 - 1) / 10)
        coeff_truth = coeff_truth.reshape(mvh_grid.shape)
        title = r'$n_1^{\rm{truth}}/n_1^{\rm{NN}}\;\rm{(median)}$'
    elif c2 != 0:
        ratio_truth_c2 = likelihood_ratio_truth(grid, np.array([0, 10]), lin=True)
        mask = ratio_truth_c2 == 0
        coeff_truth = np.ma.masked_where(mask, (ratio_truth_c2 - 1) / 10)
        coeff_truth = coeff_truth.reshape(mvh_grid.shape)
        title = r'$n_2^{\rm{truth}}/n_2^{\rm{NN}}\;\rm{(median)}$'
    else:
        loggin.info("c1 and c2 cannot both be zero.")

    # models

    mean, std = np.loadtxt(os.path.join(path_model, 'scaling.dat'))
    loaded_model = quad_clas.PredictorLinear(network_size)
    network_path = os.path.join(path_model, 'trained_nn.pt')

    # load all the parameters into the trained network
    loaded_model.load_state_dict(torch.load(network_path))
    grid = (grid_unscaled_tensor - mean) / std

    coeff_nn = loaded_model.n_alpha(grid.float())
    coeff_nn = coeff_nn.view(mvh_grid.shape).detach().numpy()

    bounds = [0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05]
    fig = plot_heatmap(coeff_truth / coeff_nn,
                       xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                       ylabel=r'$\rm{Rapidity}$',
                       title=title,
                       extent=[mvh_min, mvh_max, y_min, y_max],
                       cmap='seismic',
                       bounds=bounds)

    return fig


def coeff_comp(path_sm_data):
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

    # truth
    ratio_truth_c1 = analysis.likelihood_ratio_truth(grid, np.array([10, 0]), lin=True)
    ratio_truth_c2 = analysis.likelihood_ratio_truth(grid, np.array([0, 10]), lin=True)
    mask = ratio_truth_c1 == 0

    n_alpha_truth = np.ma.masked_where(mask, (ratio_truth_c1 - 1) / 10)
    n_alpha_truth = n_alpha_truth.reshape(mvh_grid.shape)

    n_beta_truth = np.ma.masked_where(mask, (ratio_truth_c2 - 1) / 10)
    n_beta_truth = n_beta_truth.reshape(mvh_grid.shape)

    # models

    network_size = [2, 30, 30, 30, 30, 30, 1]
    model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/17_11/model_final_lin_cHW/mc_run_{mc_run}'

    n_betas = []
    mc_runs = 30
    for rep_nr in range(0, mc_runs):

        mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=rep_nr), 'scaling.dat'))
        loaded_model = quad_classifier_cluster.PredictorLinear(network_size)
        network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt')

        # load all the parameters into the trained network
        loaded_model.load_state_dict(torch.load(network_path))
        grid = (grid_unscaled_tensor - mean) / std

        n_beta = loaded_model.n_alpha(grid.float())
        n_beta = n_beta.view(mvh_grid.shape).detach().numpy()

        n_betas.append(n_beta)

    n_betas = np.array(n_betas)
    n_beta_median = np.percentile(n_betas, 50, axis=0)
    n_beta_high = np.percentile(n_betas, 84, axis=0)
    n_beta_low = np.percentile(n_betas, 16, axis=0)
    n_beta_unc = (n_beta_high - n_beta_low) / 2

    # visualise sm events
    if path_sm_data is not None:
        path_dict_sm = {0: path_sm_data}
        data_sm = quad_classifier_cluster.EventDataset(c=0,
                                                       n_features=2,
                                                       path_dict=path_dict_sm,
                                                       n_dat=500,
                                                       hypothesis=1)
        sm_events = data_sm.events.numpy()
    else:
        sm_events = None

    # median
    fig1 = plot_heatmap(n_alpha_truth / n_beta_median,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=r'$n_1^{\rm{truth}}/n_1^{\rm{NN}}\;\rm{(median)}$',
                        extent=[mvh_min, mvh_max, y_min, y_max],
                        cmap='seismic',
                        bounds=[0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05])

    fig1.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/17_11/n_beta_ratio_v6.pdf')

    # pull
    fig2 = plot_heatmap((n_alpha_truth - n_beta_median) / n_beta_unc,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=r'$\rm{Pull}$',
                        extent=[mvh_min, mvh_max, y_min, y_max],
                        cmap='seismic',
                        bounds=np.linspace(-1.5, 1.5, 10))

    fig2.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/17_11/n_beta_ratio_pull_v3.pdf')


def load_models(architecture, model_dir, model_nrs):
    models = []
    for rep_nr in model_nrs:
        # load statistics of pretrained models
        mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=rep_nr), 'scaling.dat'))
        loaded_model = quad_clas.PredictorLinear(architecture)
        network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt')

        # load all the parameters into the trained network and save
        loaded_model.load_state_dict(torch.load(network_path))
        models.append(loaded_model)

    return models


def make_predictions_1d(x, network_path, network_size, cHW, cHq3, mean, std,
                        path_lin_1=None,
                        path_lin_2=None,
                        path_quad_1=None,
                        path_quad_2=None):
    # Set up coordinates and compute f
    x_unscaled = torch.from_numpy(x)
    # x_unscaled = torch.cat((x_unscaled, torch.zeros(len(x_unscaled), 1)), dim=1)
    x = (x_unscaled - mean) / std  # rescale the inputs

    # Be careful to use the same network architecture as during training

    if path_quad_1 is None:
        loaded_model = quad_clas.PredictorLinear(network_size)
        loaded_model.load_state_dict(torch.load(network_path))
        f_pred = loaded_model.forward(x.float(), cHW + cHq3)
    elif path_quad_2 is None:
        loaded_model = quad_clas.PredictorQuadratic(network_size)
        loaded_model.load_state_dict(torch.load(network_path))
        f_pred = loaded_model.forward(x.float(), cHW ** 2 + cHq3 ** 2, path_lin_1)
    else:
        loaded_model = quad_clas.PredictorCross(network_size)
        loaded_model.load_state_dict(torch.load(network_path))
        f_pred = loaded_model.forward(x.float(), cHW, cHq3, path_lin_1, path_lin_2, path_quad_1, path_quad_2)

    f_pred = f_pred.view(-1).detach().numpy()

    return f_pred



