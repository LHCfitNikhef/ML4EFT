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
import os, sys

# import own pacakges
from quad_clas.core import classifier as quad_clas
from quad_clas.core.truth import tt_prod as axs
from quad_clas.core.truth import vh_prod
from ..preproc import constants

mz = constants.mz # z boson mass [TeV]
mh = constants.mh

# matplotlib.use('PDF')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


def likelihood_ratio_truth(x, c, lin=False, quad=False):
    """
    Computes the analytic likelihood ratio r(x, c)

    Parameters
    ----------
    x : numpy.ndarray, shape=(M, N)
        Kinematic feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c : numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.

    Returns
    -------
    ratio: numpy.ndarray, shape=(M,)
        Likelihood ratio wrt the SM for the events ``x``
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

    return ratio.flatten()

def decision_function_truth(x, c, lin=False, quad=False):
    """
    Computes the analytic decission function f(x, c)

    Parameters
    ----------
    x: numpy.ndarray, shape=(M, N)
        Kinematic feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c: numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.

    Returns
    -------
    ratio: numpy.ndarray, shape=(M,)
        Decission function f for the events ``x``
    """

    ratio = likelihood_ratio_truth(x, c, lin, quad)
    f = 1 / (1 + ratio)
    return f

# def likelihood_ratio_nn(x, c, path_to_models, architecture, mc_run, lin=False, quad=False):
#     """
#     Computes the reconstructed likelihood ratio r(x, c) using the NN models
#
#     Parameters
#     ----------
#     x : torch.tensor, shape=(M, N)
#         Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
#         the invariant mass and the rapidity.
#     c : numpy.ndarray, shape=(M,)
#         EFT point in M dimensions, e.g c = (cHW, cHq3)
#     path_to_models: dict
#         Path to the nn model root directory
#     mc_run: int
#         Monte Carlo replica number
#     lin: bool, optional
#         Set to False by default. Turn on for linear corrections.
#     quad: bool, optional
#         Set to False by default. Turn on for quadratic corrections.
#     cross: bool, optional
#         Set to False by default. Turn on for cross term corrections
#
#     Returns
#     -------
#     ratio: numpy.ndarray, shape=(M,)
#         Reconstructed likelihood ratio wrt the SM for the events ``x``
#     """
#
#
#     # load the linear coefficient functions
#     n_lin = []
#     for path_to_model in path_to_models['lin']:
#         n_lin.append(coeff_function_nn(x, path_to_model, architecture, lin=True))
#     n_lin = np.array(n_lin)
#
#     if lin:
#         return 1 + np.dot(c, n_lin)
#
#     # for quadratic corrections
#     elif quad:
#         n_quad = []
#         for path_to_model in path_to_models['quad']:
#             n_quad.append(coeff_function_nn(x, path_to_model, architecture, quad=True))
#         n_quad = np.array(n_quad)
#
#         n_cross = []
#         for path_to_model in path_to_models['cross']:
#             n_cross.append(coeff_function_nn(x, path_to_model, architecture, cross=True))
#         n_cross = np.array(n_cross)
#
#         return 1 + np.dot(c, n_lin) + np.dot(c ** 2, n_quad) + np.prod(c) * n_cross

def coeff_function_nn(x, path_to_model, architecture, lin=False, quad=False, cross=False):
    """
    Computes the truth coefficient functions in the EFT expansion up to either linear or quadratic level

    Parameters
    ----------
     x : torch.tensor, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    path_to_models: dict
        Path to the nn model root directory
    architecture: list
        The architecture of the model, e.g.

            .. math::

                [n_i, 10, 15, 5, n_f],

        where :math:`n_i` and :math:`n_f` denote the number of input features and output target values respectively.
    mc_run: int
        Monte Carlo replica number
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.
    cross: bool, optional
        Set to False by default. Turn on for cross term corrections

    Returns
    -------

    """
    with torch.no_grad():

        if lin:
            nn = quad_clas.PredictorLinear(architecture)
        elif quad:
            nn = quad_clas.PredictorQuadratic(architecture)
        elif cross:
            nn = quad_clas.PredictorCross(architecture)

        path_nn = os.path.join(path_to_model, 'trained_nn.pt')
        nn.load_state_dict(torch.load(path_nn))
        mean, std = np.loadtxt(os.path.join(path_to_model, 'scaling.dat'))

        x_scaled = (x - mean) / std

        if lin:
            n_lin_out = nn.n_alpha(x_scaled.float()).numpy().flatten()
            return n_lin_out
        elif quad:
            n_quad_out = nn.n_beta(x_scaled.float()).numpy().flatten()
            return n_quad_out
        elif cross:
            n_cross_out = nn.n_gamma(x_scaled.float()).numpy().flatten()
            return n_cross_out


        # if lin:
        #
        #     n_lin = quad_clas.PredictorLinear(architecture)
        #
        #     path_nn_lin = os.path.join(path_to_models , 'trained_nn.pt')
        #     n_lin.load_state_dict(torch.load(path_nn_lin.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_lin, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_lin_out = n_lin.n_alpha(x_scaled.float()).numpy().flatten()
        #
        #     return n_lin_out
        #
        # elif quad:
        #
        #     n_lin = quad_clas.PredictorLinear(architecture)
        #
        #     path_nn_lin = os.path.join(path_to_trained_models['lin'], 'trained_nn.pt')
        #     n_lin.load_state_dict(torch.load(path_nn_lin.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_lin, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_lin_1_out = n_lin_1.n_alpha(x_scaled.float()).numpy().flatten()
        #
        #
        #
        #     path_nn_quad = path_to_models['quad']  # shape = (len(c), )
        #
        #     n_quad_1 = PredictorQuadratic(architecture)
        #
        #     path_nn_quad_1 = os.path.join(path_nn_quad[0], 'mc_run_{}', 'trained_nn.pt')
        #     n_quad_1.load_state_dict(torch.load(path_nn_quad_1.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_quad[0], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_quad_1_out = n_quad_1.n_beta(x_scaled.float()).numpy().flatten()
        #
        #     #######
        #
        #     n_quad_2 = PredictorQuadratic(architecture)
        #
        #     path_nn_quad_2 = os.path.join(path_nn_quad[1], 'mc_run_{}', 'trained_nn.pt')
        #     n_quad_2.load_state_dict(torch.load(path_nn_quad_2.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_quad[1], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_quad_2_out = n_quad_2.n_beta(x_scaled.float()).numpy().flatten()
        #
        #     return np.array([n_quad_1_out, n_quad_2_out], dtype=np.ndarray)
        #
        # else: # cross terms
        #
        #     path_nn_lin = path_to_models['lin']  # shape = (len(c), )
        #
        #     n_lin_1 = quad_clas.PredictorLinear(architecture)
        #
        #     path_nn_lin_1 = os.path.join(path_nn_lin[0], 'trained_nn.pt')
        #     n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_lin[0], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_lin_1_out = n_lin_1.n_alpha(x_scaled.float()).numpy().flatten()
        #
        #     #######
        #
        #     n_lin_2 = quad_clas.PredictorLinear(architecture)
        #
        #     path_nn_lin_2 = os.path.join(path_nn_lin[1], 'mc_run_{}', 'trained_nn.pt')
        #     n_lin_2.load_state_dict(torch.load(path_nn_lin_2.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_lin[1], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_lin_2_out = n_lin_2.n_alpha(x_scaled.float()).numpy().flatten()
        #
        #     n_cross = PredictorCross(architecture)
        #
        #     path_nn_cross = os.path.join(path_to_models['cross'], 'mc_run_{}', 'trained_nn.pt')
        #     n_cross.load_state_dict(torch.load(path_nn_cross.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_to_models['cross'], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_cross_out = n_cross.n_gamma(x_scaled.float()).numpy().flatten()
        #
        #     ########
        #
        #     path_nn_quad = path_to_models['quad']  # shape = (len(c), )
        #
        #     n_quad_1 = PredictorQuadratic(architecture)
        #
        #     path_nn_quad_1 = os.path.join(path_nn_quad[0], 'mc_run_{}', 'trained_nn.pt')
        #     n_quad_1.load_state_dict(torch.load(path_nn_quad_1.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_quad[0], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_quad_1_out = n_quad_1.n_beta(x_scaled.float()).numpy().flatten()
        #
        #     #######
        #
        #     n_quad_2 = PredictorQuadratic(architecture)
        #
        #     path_nn_quad_2 = os.path.join(path_nn_quad[1], 'mc_run_{}', 'trained_nn.pt')
        #     n_quad_2.load_state_dict(torch.load(path_nn_quad_2.format(mc_run)))
        #     mean, std = np.loadtxt(os.path.join(path_nn_quad[1], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        #     x_scaled = (x - mean) / std
        #     n_quad_2_out = n_quad_2.n_beta(x_scaled.float()).numpy().flatten()
        #
        #     return np.array([n_cross_out], dtype=np.ndarray)


def plot_heatmap(im, xlabel, ylabel, title, extent, bounds, cmap='GnBu'):
    """
    Plot and return a heatmap of ``im``

    Parameters
    ----------
    im: numpy.ndarray, shape=(M, N)
        Input array
    xlabel: str
    ylabel: str
    title: str
    extent: list
        boundaries of the heatmap, e.g. [x_0, x_1, y_1, y_2]
    bounds: list
        The boundaries of the discrete colourmap
    cmap: str
        colourmap to use, set to 'GnBu' by default

    Returns
    -------
    fig: `matplotlib.figure.Figure`
    """

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

def coeff_function_truth(x, c, lin, quad, cross):
    """
    Computes the truth coefficient functions in the EFT expansion up to either linear or quadratic level

    Parameters
    ----------
     x : numpy.ndarray, shape=(M, N)
        Kinematic feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c : numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.

    Returns
    -------

    """

    c1, c2 = c
    ratio_truth_lin = likelihood_ratio_truth(x, c, lin=True)
    # compute the mask once to select the physical region in phase space
    mask = ratio_truth_lin == 0
    coeff_lin = np.ma.masked_where(mask, (ratio_truth_lin - 1) / np.sum(c))

    if lin: # only one of the c elements can be nonzero
        return coeff_lin
    elif quad: # only one of the c elements can be nonzero
        ratio_truth_quad = likelihood_ratio_truth(x, c, quad=True)
        coeff_quad = np.ma.masked_where(mask, (ratio_truth_quad - 1 - np.sum(c) * coeff_lin) / np.sum(c) ** 2)
        return coeff_quad
    elif cross:
        ratio_truth_quad = likelihood_ratio_truth(x, c, quad=True)
        ratio_truth_quad_1 = likelihood_ratio_truth(x, np.array([c1, 0]), quad=True)
        ratio_truth_quad_2 = likelihood_ratio_truth(x, np.array([0, c2]), quad=True)
        coeff_cross = np.ma.masked_where(mask, (ratio_truth_quad - ratio_truth_quad_1 - ratio_truth_quad_2 + 1) / np.prod(c))
        return coeff_cross


def coeff_comp_rep(path_to_model, network_size, c1, c2, quad, cross):
    """
    Compares the EFT coefficient function of the individual replica stored at ``path_model`` with the truth.
    The ratio is plotted and returned as a matplotlib figure.

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
    quad: bool
        Set to True when quadratic coefficient functions are trained
    cross: bool
        Set to True when cross term coefficient functions are trained

    Returns
    -------
    `matplotlib.figure.Figure`
    """

    s = 14 ** 2
    epsilon = 1e-2
    mvh_min, mvh_max = mz + mh + epsilon, 2
    y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)

    x_spacing, y_spacing = 1e-1, 0.1
    mvh_span = np.arange(mvh_min, mvh_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)

    mvh_grid, y_grid = np.meshgrid(mvh_span, y_span)
    grid = np.c_[mvh_grid.ravel(), y_grid.ravel()]
    grid_unscaled_tensor = torch.Tensor(grid)

    # truth

    lin = True if not (quad or cross) else False # if both quad and cross are false, lin must be true

    coeff_truth = coeff_function_truth(grid, np.array([c1, c2]), lin, quad, cross)
    coeff_truth = coeff_truth.reshape(mvh_grid.shape)
    # models

    coeff_nn = coeff_function_nn(grid_unscaled_tensor, path_to_model, network_size, lin, quad, cross)
    coeff_nn = coeff_nn.reshape(mvh_grid.shape)

    if lin:
        title=r'$\rm{NN/Truth}\;(lin)$'
    elif quad:
        title=r'$\rm{NN/Truth}\;(quad)$'
    elif cross:
        title = r'$\rm{NN/Truth}\;(cross)$'

    bounds = [0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05]
    fig = plot_heatmap(coeff_truth / coeff_nn,
                       xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                       ylabel=r'$\rm{Rapidity}$',
                       title=title,
                       extent=[mvh_min, mvh_max, y_min, y_max],
                       cmap='seismic',
                       bounds=bounds)

    return fig

def coeff_comp(mc_reps, path_to_model, network_size, c1, c2, lin=False, quad=False, cross=False, path_sm_data=None):
    """
    Compares the NN and true coefficient functions in the EFT expansion and plots their ratio and pull

    Parameters
    ----------
    mc_reps: int
        Number of replicas to include
    path_model: str
        Path to models, e.g. models/model_x/mc_run_{mc_run}
    network_size: list
        Architecture of the network
    c1: float
        Value of the 1st EFT coefficient used during training
    c2: float
        Value of the 2nd EFT coefficient used during training
    path_sm_data: str, optional
        Path to sm .npy event file which will be plotted on top of the heatmap

    Returns
    -------
    `matplotlib.figure.Figure`
        Heatmap of coefficient function ratio
    `matplotlib.figure.Figure`
        Heatmap of pull
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

    coeff_truth = coeff_function_truth(grid, np.array([c1, c2]), lin, quad, cross).reshape(mvh_grid.shape)


    # models

    coeff_nns = []
    for rep_nr in range(0, mc_reps):


        coeff_nn = coeff_function_nn(x=grid_unscaled_tensor,
                          path_to_model=path_to_model.format(mc_run=rep_nr),
                          architecture=network_size,
                          lin=lin,
                          quad=quad,
                          cross=cross).reshape(mvh_grid.shape)

        coeff_nns.append(coeff_nn)

    coeff_nns = np.array(coeff_nns)
    coeff_nn_median = np.percentile(coeff_nns, 50, axis=0)
    coeff_nn_high = np.percentile(coeff_nns, 84, axis=0)
    coeff_nn_low = np.percentile(coeff_nns, 16, axis=0)
    coeff_nn_unc = (coeff_nn_high - coeff_nn_low) / 2

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
    median_ratio = coeff_truth / coeff_nn_median
    title= r'$\rm{Truth/NN\;(median)}$'

    fig1 = plot_heatmap(median_ratio,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=title,
                        extent=[mvh_min, mvh_max, y_min, y_max],
                        cmap='seismic',
                        bounds=[0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05])

    # pull
    pull = (coeff_truth - coeff_nn_median) / coeff_nn_unc

    fig2 = plot_heatmap(pull,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=r'$\rm{Pull}$',
                        extent=[mvh_min, mvh_max, y_min, y_max],
                        cmap='seismic',
                        bounds=np.linspace(-1.5, 1.5, 10))

    return fig1, fig2

def load_models(architecture, model_dir, model_nrs, epoch=-1, lin=False, quad=False, cross=False):
    """
    Load the pretrained models

    Parameters
    ----------
    architecture: list
        Arcitecture of the model
    model_dir:
        path to model directory up to mc_run (pass rep number as string format), e.g.
        /models/mc_run_{}
    model_nrs: iterable object
        An iterable that contains all the replicas that should be loaded

    Returns
    -------
    models: list
        List of loaded models
    """


    means, stds = [], []
    models = []
    for rep_nr in model_nrs:

        if lin:
            loaded_model = quad_clas.PredictorLinear(architecture)
        elif quad:
            loaded_model = quad_clas.PredictorQuadratic(architecture)
        else:
            loaded_model = quad_clas.PredictorCross(architecture)

        # load statistics of pretrained models
        mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=rep_nr), 'scaling.dat'))
        #loaded_model = quad_clas.PredictorLinear(architecture)
        if epoch != -1:
            path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn_{}.pt'.format(epoch))
            if os.path.exists(path):
                network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn_{}.pt'.format(epoch))
            else:
                network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt')
        else:
            network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt')

        # load all the parameters into the trained network and save
        loaded_model.load_state_dict(torch.load(network_path))
        models.append(loaded_model)
        means.append(mean)
        stds.append(std)

    return models, means, stds

def point_by_point_comp(mc_reps, events, c, path_to_models, network_size, lin=True, quad=False):
    """
    Make a point by point comparison between the truth and the models

    Parameters
    ----------
    mc_reps: int
        Number of replicas to include
    events: numpy.ndarray, shape=(M, N)
        Kinematic feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c: numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    path_to_models: dict
        dictionary containing the paths to the trained models for each order in the eft expansion (linear, quadratic
        and cross terms)
    network_size: list
        Network architecture

    Returns
    -------
    `matplotlib.figure.Figure`
        Overview plot of all the replicas
    `matplotlib.figure.Figure`
        Plot of the median only
    """

    r_nn = []
    for mc_run in range(mc_reps):
        r_nn_rep = likelihood_ratio_nn(torch.Tensor(events), c, path_to_models, network_size, mc_run=mc_run,
                                       lin=lin, quad=quad)
        r_nn_rep = r_nn_rep.numpy().flatten()
        r_nn.append(r_nn_rep)
    tau_nn = np.log(r_nn)

    r_truth = likelihood_ratio_truth(events, c, lin=lin, quad=quad)
    tau_truth = np.log(r_truth)

    # overview plot for all replicas
    ncols = 5
    nrows = int(np.ceil(mc_reps/ncols))

    fig1 = plt.figure(figsize=(ncols * 4, nrows * 4))

    x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)
    for i in range(int(ncols * nrows)):
        plt.subplot(nrows, ncols, i + 1)
        plt.scatter(tau_truth, tau_nn[i, :], s=5, color='k')
        plt.plot(x, x, linestyle='dashed', color='grey')
        plt.xlim((np.min(x), np.max(x)))
        plt.ylim((np.min(x), np.max(x)))

    plt.tight_layout()

    # median
    fig2, ax = plt.subplots(figsize=(8, 8))
    x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)
    plt.scatter(tau_truth, np.median(tau_nn, axis=0), s=5, color='k')
    plt.plot(x, x, linestyle='dashed', color='grey')
    plt.xlabel(r'$\tau(x, c)^{\rm{truth}}$')
    plt.ylabel(r'$\tau(x, c)^{\rm{NN}}$')
    plt.xlim((np.min(x), np.max(x)))
    plt.ylim((np.min(x), np.max(x)))
    plt.tight_layout()

    return fig1, fig2

def load_coefficients_nn(x, architecture, path_to_models, mc_reps, epoch=-1):

    n_lin = []
    n_quad = []
    n_cross = []
    for order, paths in path_to_models.items():
        if order == 'lin':
            for path in paths:
                loaded_models_lin, means, std = load_models(architecture, path, range(mc_reps), epoch=epoch, lin=True)
                n_alphas = []
                for i in range(mc_reps):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_alphas.append(loaded_models_lin[i].n_alpha(torch.tensor(x_scaled).float()).numpy().flatten())
                n_alphas = np.array(n_alphas)
                n_lin.append(n_alphas)

        if order == 'quad':
            for path in paths:
                loaded_models_quad, means, std = load_models(architecture, path, range(mc_reps), epoch=epoch, quad=True)
                n_betas = []
                for i in range(mc_reps):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_betas.append(loaded_models_quad[i].n_beta(torch.tensor(x_scaled).float()).numpy().flatten())
                n_betas = np.array(n_betas)
                n_quad.append(n_betas)

        if order == 'cross':
            for path in paths:
                loaded_models_cross, means, std = load_models(architecture, path, range(mc_reps), epoch=epoch, cross=True)
                n_gammas = []
                for i in range(mc_reps):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_gammas.append(loaded_models_cross[i].n_gamma(x_scaled.float()).numpy().flatten())
                n_gammas = np.array(n_gammas)
                n_cross.append(n_gammas)
    n_lin = np.array(n_lin)
    n_quad = np.array(n_quad)
    n_cross = np.array(n_cross)

    return n_lin, n_quad, n_cross

def make_predictions_1d(x, c, path_to_models, network_size, mc_reps=30, epoch=-1, lin=False, quad=False):

    # nn models at the specified epoch
    n_lin, n_quad, n_cross = load_coefficients_nn(x, network_size, path_to_models, mc_reps, epoch=epoch)

    # trained nn models
    n_lin_trained, n_quad_trained, n_cross_trained = load_coefficients_nn(x, network_size, path_to_models, mc_reps, epoch=-1)
    if lin:
        r = 1 + np.einsum('i, ijk', c, n_lin)
    elif quad:
        # TODO: c should have the same dimesnions as n_lin_trained
        r = 1 + np.einsum('i, ijk', c, n_lin_trained) + np.einsum('i, ijk', c ** 2, n_quad)
    return 1 / (1 + r)

def likelihood_ratio_nn(x, c, path_to_models, network_size, mc_reps=30, epoch=-1, lin=False, quad=False):

    # nn models at the specified epoch

    n_lin, n_quad, n_cross = load_coefficients_nn(x, network_size, path_to_models, mc_reps, epoch=epoch)

    # trained nn models
    n_lin_trained, n_quad_trained, n_cross_trained = load_coefficients_nn(x, network_size, path_to_models, mc_reps, epoch=-1)
    if lin:
        r = 1 + np.einsum('i, ijk', c, n_lin)
    elif quad:
        r = 1 + np.einsum('i, ijk', c, n_lin_trained) + np.einsum('i, ijk', c ** 2, n_quad)
    return r


def decision_function_nn(x, c, path_to_models, network_size, mc_reps=30, epoch=-1, lin=False, quad=False):
    """
    Computes the reconstructed decission function f(x, c)

    Parameters
    ----------
    x : torch.tensor, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c : numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    path_to_models: dict
        Path to the nn model root directory
    mc_reps: int
        Monte Carlo replica number
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.

    Returns
    -------
    f: numpy.ndarray, shape=(M,)
        Reconstructed decission function f for the events ``x``
    """

    ratio = likelihood_ratio_nn(x, c, path_to_models, network_size, mc_reps, epoch, lin=lin, quad=quad)
    f = 1 / (1 + ratio)
    return f


def make_predictions_1d_old(x, network_path, network_size, cHW, cHq3, mean, std,
                        path_lin_1=None,
                        path_lin_2=None,
                        path_quad_1=None,
                        path_quad_2=None):
    """
    Deprecated, to be removed in future versions
    """
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

