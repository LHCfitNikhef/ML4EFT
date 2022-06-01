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
import pickle
import joblib
import json
import pandas as pd
from sklearn.cluster import KMeans

# import own pacakges
from quad_clas.core import classifier as quad_clas
from quad_clas.core.truth import tt_prod as axs
from quad_clas.core.truth import vh_prod, tt_prod
from ..preproc import constants

mz = constants.mz # z boson mass [TeV]
mh = constants.mh
mt = constants.mt

# matplotlib.use('PDF')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


def likelihood_ratio_truth(events, c, n_kin, process, lin=False, quad=False):
    """
    Computes the analytic likelihood ratio r(x, c)

    Parameters
    ----------
    events : numpy.ndarray, shape=(M, N)
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
    # uncomment for ZH
    if process == 'ZH':
        cHW, cHq3 = c
        if n_kin == 1:
            dsigma_0 = [vh_prod.dsigma_dmvh(x['m_zh'], cHW, cHq3, lin=lin, quad=quad) for index, x in events.iterrows()]  # EFT
            dsigma_1 = [vh_prod.dsigma_dmvh(x['m_zh'], 0, 0, lin=lin, quad=quad) for index, x in
                        events.iterrows()]  # SM
        elif n_kin == 2:
            dsigma_0 = [vh_prod.dsigma_dmvh_dy(x['y'], x['m_zh'], cHW, cHq3, lin=lin, quad=quad) for index, x in
                        events.iterrows()]  # EFT
            dsigma_1 = [vh_prod.dsigma_dmvh_dy(x['y'], x['m_zh'], 0, 0, lin=lin, quad=quad) for index, x in
                        events.iterrows()]  # SM
        elif n_kin == 3:
            dsigma_0 = [vh_prod.dsigma_dmvh_dy_dpt(x['y'], x['m_zh'], x['pt_z'], cHW, cHq3, lin=lin, quad=quad) for index, x in
                        events.iterrows()]  # EFT
            dsigma_1 = [vh_prod.dsigma_dmvh_dy_dpt(x['y'], x['m_zh'], x['pt_z'], 0, 0, lin=lin, quad=quad) for index, x in
                        events.iterrows()]  # SM
        else:
            raise NotImplementedError("No more than three features are currently supported")

    if process == 'tt':

        c1, c2 = c
        if n_kin == 1:
            dsigma_0 = [tt_prod.dsigma_dmtt(x['m_tt'], c1, c2, lin, quad) for index, x in events.iterrows()]  # EFT
            dsigma_1 = [tt_prod.dsigma_dmtt(x['m_tt'], 0, 0, lin, quad) for index, x in
                        events.iterrows()]  # SM
        else:
            dsigma_0 = [tt_prod.dsigma_dmtt_dy(x['y'], x['m_tt'], c1, c2, lin, quad) for index, x in
                        events.iterrows()]  # EFT
            dsigma_1 = [tt_prod.dsigma_dmtt_dy(x['y'], x['m_tt'], 0, 0, lin, quad) for index, x in
                        events.iterrows()]  # SM

    dsigma_0, dsigma_1 = np.array(dsigma_0), np.array(dsigma_1)

    ratio = np.divide(dsigma_0, dsigma_1, out=np.zeros_like(dsigma_0), where=dsigma_1 != 0)

    return ratio.flatten()


def decision_function_truth(x, c, n_kin, process, lin=False, quad=False):
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

    ratio = likelihood_ratio_truth(x, c,  n_kin, process, lin, quad)
    f = 1 / (1 + ratio)
    return f


#TODO: coeff_function_nn can be replaced entirely by load_coefficients_nn
def coeff_function_nn(x, path_to_model, architecture, lin=False, quad=False, cross=False, animate=False, epoch=None):
    """
    Computes the nn coefficient functions in the EFT expansion up to either linear or quadratic level

    Parameters
    ----------
     x : torch.tensor, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    path_to_models: str
        Path to the nn model directory, e.g. ./model_x/mc_run_0
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

        if animate and epoch is not None:
            path_nn = os.path.join(path_to_model, 'trained_nn_{epoch}.pt'.format(epoch=epoch))
            if not os.path.exists(path_nn):
                path_nn = os.path.join(path_to_model, 'trained_nn.pt')
        else:
            path_nn = os.path.join(path_to_model, 'trained_nn.pt')
        nn.load_state_dict(torch.load(path_nn))

        scaler_path = os.path.join(path_to_model, 'scaler.gz')
        scaler = joblib.load(scaler_path)
        x_scaled = scaler.transform(x)
        x_scaled = torch.tensor(x_scaled)

        if lin:
            n_lin_out = nn.n_alpha(x_scaled.float()).numpy().flatten()
            return n_lin_out
        elif quad:
            n_quad_out = nn.n_beta(x_scaled.float()).numpy().flatten()
            return n_quad_out
        elif cross:
            n_cross_out = nn.n_gamma(x_scaled.float()).numpy().flatten()
            return n_cross_out


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


def coeff_function_truth(x, c, n_kin, process, lin, quad, cross):
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
    ratio_truth_lin = likelihood_ratio_truth(x, c, n_kin, process, lin=True)
    # compute the mask once to select the physical region in phase space
    mask = ratio_truth_lin == 0
    coeff_lin = np.ma.masked_where(mask, (ratio_truth_lin - 1) / np.sum(c))
    if lin: # only one of the c elements can be nonzero
        return coeff_lin
    elif quad: # only one of the c elements can be nonzero
        ratio_truth_quad = likelihood_ratio_truth(x, c, quad=True)
        # TODO: rewrite the below
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

    x_spacing, y_spacing = 1e-2, 0.01
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


def coeff_comp(path_to_models, network_size, c1, c2, c_train, n_kin, process, lin=False, quad=False, cross=False, path_sm_data=None):
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

    if process == 'ZH':
        mx_min, mx_max = mz + mh + epsilon, 2
    elif process == 'tt':
        mx_min, mx_max = 2 * mt + epsilon, 2

    y_min, y_max = - np.log(np.sqrt(s) / mx_min), np.log(np.sqrt(s) / mx_min)

    x_spacing, y_spacing = 1e-2, 0.01
    mx_span = np.arange(mx_min, mx_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)

    mx_grid, y_grid = np.meshgrid(mx_span, y_span)
    grid = np.c_[mx_grid.ravel(), y_grid.ravel()]

    if process == 'ZH':
        df = pd.DataFrame({'m_zh': grid[:, 0], 'y': grid[:, 1]})
    elif process == 'tt':
        df = pd.DataFrame({'m_tt': grid[:, 0], 'y': grid[:, 1]})

    # truth
    coeff_truth = coeff_function_truth(df, np.array([c1, c2]), n_kin, process, lin, quad, cross).reshape(mx_grid.shape)

    # models

    [n_lin, model_idx], n_quad, n_cross = load_coefficients_nn(df, c_train, network_size, path_to_models, epoch=-1)
    n_lin = n_lin[0,:, :].reshape((n_lin.shape[1], *mx_grid.shape))
    coeff_nn_median = np.percentile(n_lin, 50, axis=0)
    coeff_nn_high = np.percentile(n_lin, 84, axis=0)
    coeff_nn_low = np.percentile(n_lin, 16, axis=0)
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
                        extent=[mx_min, mx_max, y_min, y_max],
                        cmap='seismic',
                        bounds=[0.95, 0.96, 0.97, 0.98, 1.02, 1.03, 1.04, 1.05])

    # pull
    pull = (coeff_truth - coeff_nn_median) / coeff_nn_unc

    fig2 = plot_heatmap(pull,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=r'$\rm{Pull}$',
                        extent=[mx_min, mx_max, y_min, y_max],
                        cmap='seismic',
                        bounds=np.linspace(-1.5, 1.5, 10))

    return fig1, fig2


def load_models(c_train, model_dir, epoch=-1, lin=False, quad=False, cross=False):
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

    models = []
    losses = []

    model_dirs = [os.path.join(model_dir, mc_run) for mc_run in os.listdir(model_dir)]
    for dir in model_dirs:
        if lin:
            with open(os.path.join(dir, 'run_card.json')) as json_data:
                run_card = json.load(json_data)
                architecture = [run_card['input_size']] + run_card['hidden_sizes'] + [run_card['output_size']]
            loaded_model = quad_clas.PredictorLinear(architecture, c_train)
        elif quad:
            loaded_model = quad_clas.PredictorQuadratic(architecture)
        else:
            loaded_model = quad_clas.PredictorCross(architecture)

        if epoch != -1:
            network_path = os.path.join(dir, 'trained_nn_{}.pt'.format(epoch))
            if not os.path.isfile(network_path):
                network_path = os.path.join(dir, 'trained_nn.pt')
        else:
            network_path = os.path.join(dir, 'trained_nn.pt')

        # read the loss
        path_to_loss = os.path.join(os.path.dirname(network_path), 'loss.out')
        with open(path_to_loss) as file:
            loss = [float(line.rstrip()) for line in file]

        # store the final loss of each model
        losses.append(loss[-1])

        # load all the parameters into the trained network and save
        loaded_model.load_state_dict(torch.load(network_path))
        models.append(loaded_model)

    losses = np.array(losses)
    models = np.array(models)

    kmeans = KMeans(n_clusters=2, random_state=0).fit(losses.reshape(-1,1))
    cluster_labels = kmeans.labels_
    cluster_nr_low_loss = np.argmin(kmeans.cluster_centers_)

    model_idx = np.argwhere(cluster_labels == cluster_nr_low_loss).flatten()

    if np.std(losses[model_idx]) / np.std(losses) < 0.1: # if relative std has been reduced by a factor 10
        models_good = models[model_idx]
    else:
        sigma_loss = (np.nanpercentile(losses, 84) - np.nanpercentile(losses, 16))
        los_med = np.nanpercentile(losses, 50)

        model_idx = np.argwhere((los_med - 2 * sigma_loss < losses) & (losses < los_med + 2 * sigma_loss)).flatten()
        models_good = models[model_idx]


    # only keep models within 5 sigma


    # retrieve the rep numbers of the good models
    models_good_idx = []
    for idx in model_idx:
        mc_idx = int(os.path.basename(model_dirs[idx]).split('mc_run_', 1)[1])
        models_good_idx.append(mc_idx)

    return models_good, models_good_idx


def load_coefficients_nn(df, c_train, path_to_models, epoch=-1):
    """
    Loads in the nn models at specified in ``path_to_models`` and returns a tuple of length 3
    with the linear, quadratic and cross term coefficient functions.

    Parameters
    ----------
    x : pandas.DataFrame, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    architecture: list
        The architecture of the model, e.g.

            .. math::

                [n_i, 10, 15, 5, n_f],

        where :math:`n_i` and :math:`n_f` denote the number of input features and output target values respectively.
    path_to_models: dict
        Dictionary with the paths to the nn models for lin, quad and cross
    mc_reps: int
        Number of replicas to load
    epoch: int
        Set to the best model be default, but pass a specific epoch if needed

    Returns
    -------
    n_lin, n_quad, n_cross: numpy.ndarray, shape = (2 or 1, mc_reps, len(x))
    """

    n_lin = []
    n_quad = []
    n_cross = []

    for order, paths in path_to_models.items():
        if order == 'lin':
            for coeff, path in paths.items():
                loaded_models_lin, model_idx = load_models(c_train[coeff], path, epoch=epoch, lin=True)
                n_alphas = []
                for i, loaded_model in enumerate(loaded_models_lin):
                    path_to_model = os.path.join(path, 'mc_run_{}'.format(model_idx[i]))
                    with open(os.path.join(path_to_model, 'run_card.json')) as json_data:
                        features = json.load(json_data)['features']
                    scaler_path = os.path.join(path_to_model, 'scaler.gz')
                    scaler = joblib.load(scaler_path)
                    features_scaled = scaler.transform(df[features])

                    with torch.no_grad():
                        n_alphas.append(loaded_model.n_alpha(torch.tensor(features_scaled).float()).numpy().flatten())

                n_alphas = np.array(n_alphas)
                n_lin.append(n_alphas)

        if order == 'quad':
            for path in paths:
                loaded_models_quad, means, std = load_models(architecture, path, range(mc_reps), epoch=epoch, quad=True)
                n_betas = []
                for i in range(len(loaded_models_quad)):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_betas.append(loaded_models_quad[i].n_beta(torch.tensor(x_scaled).float()).numpy().flatten())
                n_betas = np.array(n_betas)
                n_quad.append(n_betas)

        if order == 'cross':
            for path in paths:
                loaded_models_cross, means, std = load_models(architecture, path, range(mc_reps), epoch=epoch, cross=True)
                n_gammas = []
                for i in range(len(loaded_models_cross)):
                    x_scaled = (x - means[i]) / std[i]
                    with torch.no_grad():
                        n_gammas.append(loaded_models_cross[i].n_gamma(x_scaled.float()).numpy().flatten())
                n_gammas = np.array(n_gammas)
                n_cross.append(n_gammas)

    n_rep_min = min([n_lin_i.shape[0] for n_lin_i in n_lin])

    n_lin_matched = np.zeros((len(n_lin), n_rep_min, len(df)))
    for i, n_lin_i in enumerate(n_lin):
        rnd_idx = np.random.choice(np.arange(n_lin_i.shape[0]), n_rep_min, replace=False)
        n_lin_matched[i] = n_lin[i][rnd_idx, :]

    #n_lin = np.array(n_lin)
    n_quad = np.array(n_quad)
    n_cross = np.array(n_cross)

    return [n_lin_matched, model_idx], n_quad, n_cross


def point_by_point_comp(events, c, c_train, path_to_models, n_kin, process, lin=True, quad=False, epoch=-1):
    """
    Make a point by point comparison between the truth and the models

    Parameters
    ----------
    mc_reps: int
        Number of replicas to include
    events: pandas.DataFrame, shape=(M, N)
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
    r_nn, model_idx = likelihood_ratio_nn(events, c, c_train, path_to_models, lin=lin, quad=quad, epoch=epoch)
    tau_nn = np.log(r_nn)

    r_truth = likelihood_ratio_truth(events, c, process=process, lin=lin, quad=quad, n_kin=n_kin)
    tau_truth = np.log(r_truth)

    # mzh = events['m_zh'].values
    # mask = np.argwhere(mzh > 1.0).flatten()
    # mask_comp = np.setdiff1d(np.arange(len(events)), mask)

    # overview plot for all replicas
    ncols = 5
    mc_reps = r_nn.shape[0]
    nrows = int(np.ceil(mc_reps/ncols))

    fig1 = plt.figure(figsize=(ncols * 4, nrows * 4))

    x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)
    for i in range(mc_reps):
        ax = plt.subplot(nrows, ncols, i + 1)
        #plt.scatter(tau_truth[mask_comp], tau_nn[i, mask_comp], s=2, color='k')
        #plt.scatter(tau_truth[mask], tau_nn[i, mask], s=2, color='k')
        plt.scatter(tau_truth, tau_nn[i,:], s=2)
        plt.plot(x, x, linestyle='dashed', color='grey')
        plt.text(0.1, 0.9, 'rep {}'.format(model_idx[i]), horizontalalignment='left',
                 verticalalignment='center',
                 transform=ax.transAxes)
        # plt.xlim((0, 6))
        # plt.ylim((0, 6))
        plt.xlim((np.min(x), np.max(x)))
        plt.ylim((np.min(x), np.max(x)))

    plt.tight_layout()

    # median
    fig2, ax = plt.subplots(figsize=(8, 8))
    x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)
    #x= np.linspace(0, 6, 100)
    # plt.scatter(tau_truth[mask], np.median(tau_nn, axis=0)[mask], s=5, color='k')
    # plt.scatter(tau_truth[mask_comp], np.median(tau_nn, axis=0)[mask_comp], s=5, color='k')
    plt.scatter(tau_truth, np.median(tau_nn, axis=0), s=2, color='k')
    plt.plot(x, x, linestyle='dashed', color='grey')
    plt.xlabel(r'$\tau(x, c)^{\rm{truth}}$')
    plt.ylabel(r'$\tau(x, c)^{\rm{NN}}$')
    plt.xlim((np.min(x), np.max(x)))
    plt.ylim((np.min(x), np.max(x)))
    plt.tight_layout()
    # plt.xlim((0, 6))
    # plt.ylim((0, 6))
    return fig1, fig2


def likelihood_ratio_nn(df, c, train_parameters, path_to_models, epoch=-1, lin=False, quad=False):
    """
    Computes the likelihood ratio using the nn models

    Parameters
    ----------
     x : torch.tensor, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c: numpy.ndarray
        EFT paramters
    architecture: list
        The architecture of the model, e.g.

            .. math::

                [n_i, 10, 15, 5, n_f],

        where :math:`n_i` and :math:`n_f` denote the number of input features and output target values respectively.
    path_to_models: dict
        Dictionary with the paths to the nn models for lin, quad and cross
    mc_reps: int
        Number of replicas to load
    epoch: int
        Set to the best model be default, but pass a specific epoch if needed
    lin: bool
        Set to True for linear corrections
    quad: bool
        Set to True for quadratic corrections

    Returns
    -------
    numpy.ndarray, shape=(mc_reps, M)
    """
    # nn models at the specified epoch
    [n_lin_matched, model_idx], n_quad, n_cross = load_coefficients_nn(df, train_parameters, path_to_models, epoch=epoch)

    if lin:
        r = 1 + np.einsum('i, ijk', c, n_lin_matched)
    elif quad:

        # TODO: c should have the same dimesnions as n_lin_trained
        # trained nn models
        n_lin_trained, n_quad_trained, n_cross_trained = load_coefficients_nn(x, network_size, path_to_models, mc_reps,
                                                                              epoch=-1)

        lin_cor = np.einsum('i, ijk', c, n_lin_trained)
        if len(n_cross_trained) > 0: # if cross terms are available
            quadratic_cor = np.einsum('i, ijk', c ** 2, n_quad_trained) + np.prod(c) * n_cross
        else:
            quadratic_cor = np.einsum('i, ijk', c ** 2, n_quad)
        r = 1 + lin_cor + quadratic_cor
    return r, model_idx


def decision_function_nn(df, c, train_parameters, path_to_models, network_size, epoch=-1, lin=False, quad=False):
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
    ratio, model_idx = likelihood_ratio_nn(df, c, train_parameters, path_to_models, network_size, epoch, lin=lin, quad=quad)
    f = 1 / (1 + ratio)
    return f

def accuracy_1d(c, path_to_models, network_size, mc_reps, epoch, lin, quad):

    fig, ax = plt.subplots(figsize=(10,6))

    x = np.linspace(mh + mz + 1e-2, 2.5, 100)
    x = np.stack((x, np.zeros(len(x))), axis=-1)

    x_nn = np.stack((np.log(np.linspace(mh + mz + 1e-2, 2.5, 100)), np.zeros(len(x))), axis=-1)

    f_ana_lin = decision_function_truth(x, c, lin=True)
    f_preds_nn = decision_function_nn(x_nn, c, path_to_models, network_size, mc_reps, epoch, lin, quad)

    f_pred_up = np.percentile(f_preds_nn, 84, axis=0)
    f_pred_down = np.percentile(f_preds_nn, 16, axis=0)

    ax.fill_between(x[:, 0], f_pred_down, f_pred_up, label=r'$\rm{NN}\;\mathcal{O}\left(\Lambda^{-2}\right)$', alpha=0.4)

    ax.plot(x[:, 0], f_ana_lin, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-2}\right)$')

    # single replica
    #ax.plot(x[:, 0], f_preds_nn[0,:], '--', c='blue', label=r'$\rm{NN}\;\mathcal{O}\left(\Lambda^{-2}\right)$')

    plt.ylim((0, 1))
    plt.xlim(np.min(x[:, 0]), np.max(x[:, 0]))
    plt.ylabel(r'$f\;(x, c)$')
    plt.xlabel(r'$m_{ZH}\;[\mathrm{TeV}]$')
    plt.legend()
    plt.tight_layout()
    return fig
