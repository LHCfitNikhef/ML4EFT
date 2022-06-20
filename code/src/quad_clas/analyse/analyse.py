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
from scipy import integrate
import logging

# import own pacakges
from quad_clas.core import classifier as quad_clas
from quad_clas.core.truth import tt_prod as axs
from quad_clas.core.truth import vh_prod, tt_prod
from ..preproc import constants

mz = constants.mz # z boson mass [TeV]
mh = constants.mh
mt = constants.mt
col_s = constants.col_s

# matplotlib.use('PDF')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


class Analyse:

    def __init__(self, path_to_models):

        self.path_to_models = path_to_models
        self.model_dict = {}

        # logging.basicConfig(filename=log_path + '/training_{}.log'.format(current_time), level=logging.INFO,
        #                     format='%(asctime)s:%(levelname)s:%(message)s')

    @staticmethod
    def load_loss(path_to_loss):
        """

        Parameters
        ----------
        path_to_loss: str
            Path to loss file

        Returns
        -------
        loss: list
            list of losses per epoch
        """
        with open(path_to_loss) as f:
            loss = [float(line.rstrip()) for line in f]
        return loss

    @staticmethod
    def load_run_card(path):
        """
        Parameters
        ----------
        path: str
            path to json model run card that stores the hyperparameter settings

        Returns
        -------
        run_card: dict
            dictionary with all the hyperparameter settings
        """
        with open(path) as json_data:
            run_card = json.load(json_data)
        run_card['architecture'] = [run_card['input_size']] + run_card['hidden_sizes'] + [run_card['output_size']]

        return run_card

    @staticmethod
    def filter_out_models(losses):
        """
        Filter out the badly trained models based on kmeans clustering.

        Parameters
        ----------
        losses: numpy.ndarray

        Returns
        -------
        good_model_idx: numpy.ndarray
            Array indices of the good models
        """

        kmeans = KMeans(n_clusters=2, random_state=0).fit(losses.reshape(-1, 1))
        cluster_labels = kmeans.labels_
        cluster_nr_low_loss = np.argmin(kmeans.cluster_centers_)

        # find model indices in the low loss cluster
        good_model_idx = np.argwhere(cluster_labels == cluster_nr_low_loss).flatten()

        # if relative std has not been reduced by a factor 10, select only models within +- 4 sigma
        if np.std(losses[good_model_idx]) / np.std(losses) > 0.1:

            sigma_loss = (np.nanpercentile(losses, 84) - np.nanpercentile(losses, 16)) / 2
            los_med = np.nanpercentile(losses, 50)

            good_model_idx = np.argwhere(
                (los_med - 4 * sigma_loss < losses) & (losses < los_med + 4 * sigma_loss)).flatten()

        return good_model_idx

    def load_models(self, c_train, model_path, order, epoch):
        """

        Parameters
        ----------
        c_train: float
            EFT value used during training
        model_path: str
            path to model directory
        order: str
            Specifies the order in the EFT expansion. Must be one of ``lin``, ``quad`` or ``cross``.
        epoch: int
            Epoch number to load

        Returns
        -------

        """
        # collect all replica paths
        rep_paths = [os.path.join(model_path, mc_run) for mc_run in os.listdir(model_path) if
                      mc_run.startswith('mc_run')]

        losses_tr = []  # to store the final training losses
        losses_val = []  # to store the final validation losses

        models = []
        scalers = []

        for rep_path in rep_paths:

            path_to_run_card = os.path.join(rep_path, 'run_card.json')
            path_to_scaler = os.path.join(rep_path, 'scaler.gz')

            run_card = self.load_run_card(path_to_run_card)
            scaler = joblib.load(path_to_scaler)

            if order == 'lin':
                loaded_model = quad_clas.PredictorLinear(run_card['architecture'], c_train)
            elif order == 'quad':
                pass
            elif order == 'cross':
                pass
            else:
                print("Please select one of ['lin', 'quad', 'cross'] as order in the runcard")

            # build path to model config file
            if epoch != -1:  # if specific epoch is requested
                network_path = os.path.join(rep_path, 'trained_nn_{}.pt'.format(epoch))
                if not os.path.isfile(network_path):
                    network_path = os.path.join(rep_path, 'trained_nn.pt')
            else:
                network_path = os.path.join(rep_path, 'trained_nn.pt')

            # load the model
            loaded_model.load_state_dict(torch.load(network_path))

            # read the losses
            path_to_loss_tr = os.path.join(os.path.dirname(network_path), 'loss.out')
            path_to_loss_val = os.path.join(os.path.dirname(network_path), 'loss_val.out')

            loss_tr = self.load_loss(path_to_loss_tr)
            loss_val = self.load_loss(path_to_loss_val)

            # load all the parameters into the trained network and save
            losses_tr.append(loss_tr[-run_card['patience']])
            losses_val.append(loss_val[-run_card['patience']])

            models.append(loaded_model)
            scalers.append(scaler)

        losses_tr = np.array(losses_tr)
        losses_val = np.array(losses_val)
        models = np.array(models)
        scalers = np.array(scalers)

        # filter out the badly trained models based on their training loss

        good_model_idx = self.filter_out_models(losses_tr)
        models = models[good_model_idx]
        scalers = scalers[good_model_idx]

        # map model indices back to rep number
        models_rep_nr = []
        for idx in good_model_idx:
            rep_nr = int(os.path.basename(rep_paths[idx]).split('mc_run_', 1)[1])
            models_rep_nr.append(rep_nr)
        models_rep_nr = np.array(models_rep_nr)

        return models, models_rep_nr, scalers, run_card

    def build_model_dict(self, epoch=-1):
        """
        Construct a model dictionary that stores all the info about the models

        Parameters
        ----------
        epoch: int, optional
            Epoch to load, set to the best model by default
        """
        for order, dict_fo in self.path_to_models.items():
            for c_name, [c_train, model_path] in dict_fo.items():
                pretrained_models, models_idx, scalers, run_card = self.load_models(c_train, model_path, order, epoch)
                self.model_dict[order] = {c_name: {'models': pretrained_models, 'idx': models_idx, 'scalers': scalers,
                                                   'run_card': run_card}}

    def likelihood_ratio_truth(self, events, c, features, process, order=None):
        """
        Computes the analytic likelihood ratio r(x, c)

        Parameters
        ----------
        order: str, optional
            Specifies the order in the EFT expansion. Must be one of ``lin``, ``quad``.
        process: str
            Choose between ``tt`` or ``ZH``
        features: list
            List of kinematic labels
        events : pd.DataFrame
            Pandas DataFrame with the events
        c : numpy.ndarray, shape=(M,)
            EFT point in M dimensions, e.g c = (cHW, cHq3)


        Returns
        -------
        ratio: numpy.ndarray
            Likelihood ratio wrt the SM 
        """

        n_features = len(features)

        if process == 'ZH':
            if n_features == 1:
                dsigma_0 = [vh_prod.dsigma_dmvh(*x[features], c, order) for index, x in
                            events.iterrows()]  # EFT
                dsigma_1 = [vh_prod.dsigma_dmvh(*x[features]) for index, x in
                            events.iterrows()]  # SM
            elif n_features == 2:
                dsigma_0 = [vh_prod.dsigma_dmvh_dy(*x[features], c, order) for index, x in
                            events.iterrows()]  # EFT
                dsigma_1 = [vh_prod.dsigma_dmvh_dy(*x[features]) for index, x in
                            events.iterrows()]  # SM
            elif n_features == 3:
                dsigma_0 = [vh_prod.dsigma_dmvh_dy_dpt(*x[features], c, order) for
                            index, x in
                            events.iterrows()]  # EFT
                dsigma_1 = [vh_prod.dsigma_dmvh_dy_dpt(*x[features]) for
                            index, x in
                            events.iterrows()]  # SM
            else:
                raise NotImplementedError("No more than three features are currently supported")

        if process == 'tt':

            if n_features == 1:
                dsigma_0 = [tt_prod.dsigma_dmtt(*x[features], c, order) for _, x in events.iterrows()]  # EFT
                dsigma_1 = [tt_prod.dsigma_dmtt(*x[features]) for _, x in
                            events.iterrows()]  # SM
            else:
                dsigma_0 = [tt_prod.dsigma_dmtt_dy(*x[features], c, order) for _, x in
                            events.iterrows()]  # EFT
                dsigma_1 = [tt_prod.dsigma_dmtt_dy(*x[features]) for _, x in
                            events.iterrows()]  # SM

        dsigma_0, dsigma_1 = np.array(dsigma_0), np.array(dsigma_1)

        ratio = np.divide(dsigma_0, dsigma_1, out=np.zeros_like(dsigma_0), where=dsigma_1 != 0)

        return ratio.flatten()


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


def coeff_comp_rep(path_to_model, network_size, c1, c2, lin, quad, cross, cut=None):
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

    if process == 'ZH':
        mx_min = mz + mh + epsilon if cut is None else cut
        mx_max = 2
    elif process == 'tt':
        mx_min = 2 * mt + epsilon if cut is None else cut
        mx_max = 2

    y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)

    x_spacing, y_spacing = 1e-2, 0.01
    mvh_span = np.arange(mvh_min, mvh_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)

    mvh_grid, y_grid = np.meshgrid(mvh_span, y_span)
    grid = np.c_[mvh_grid.ravel(), y_grid.ravel()]

    if process == 'ZH':
        df = pd.DataFrame({'m_zh': grid[:, 0], 'y': grid[:, 1]})
    elif process == 'tt':
        df = pd.DataFrame({'m_tt': grid[:, 0], 'y': grid[:, 1]})

    # truth


    coeff_truth = coeff_function_truth(grid, np.array([c1, c2]), lin, quad, cross)
    coeff_truth = coeff_truth.reshape(mvh_grid.shape)
    # models

    [coeff_nn, model_idx], n_quad, n_cross = load_coefficients_nn(df, path_to_models, epoch)

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
                       xlabel=r'$m_{t\bar{t}}\;\rm{[TeV]}$',
                       ylabel=r'$\rm{Rapidity}$',
                       title=title,
                       extent=[mx_min, mx_max, y_min, y_max],
                       cmap='seismic',
                       bounds=bounds)

    return fig


def coeff_comp(path_to_models, c1, c2, c_train, n_kin, process, lin=False, quad=False, cross=False, path_sm_data=None, cut=None):
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
        mx_min = mz + mh + epsilon if cut is None else cut
        mx_max = 2
    elif process == 'tt':
        mx_min = 2 * mt + epsilon if cut is None else cut
        mx_max = 2

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

    [n_lin, model_idx], n_quad, n_cross = load_coefficients_nn(df, path_to_models, epoch=-1)

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

    xlabel = r'$m_{ZH}\;\rm{[TeV]}$' if process == 'ZH' else r'$m_{t\bar{t}}\;\rm{[TeV]}$'
    fig1 = plot_heatmap(median_ratio,
                        xlabel=xlabel,
                        ylabel=r'$\rm{Rapidity}$',
                        title=title,
                        extent=[mx_min, mx_max, y_min, y_max],
                        cmap='seismic',
                        bounds=[0.95, 0.96, 0.97, 0.98, 1.02, 1.03, 1.04, 1.05])

    # pull
    pull = (coeff_truth - coeff_nn_median) / coeff_nn_unc

    fig2 = plot_heatmap(pull,
                        xlabel=xlabel,
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
    scalers = []

    # collect all model directories
    model_dirs = [os.path.join(model_dir, mc_run) for mc_run in os.listdir(model_dir) if mc_run.startswith('mc_run')]

    for dir in model_dirs:
        if lin:
            with open(os.path.join(dir, 'run_card.json')) as json_data:
                run_card = json.load(json_data)
                architecture = [run_card['input_size']] + run_card['hidden_sizes'] + [run_card['output_size']]
                patience = run_card['patience']
            loaded_model = quad_clas.PredictorLinear(architecture, c_train)

            scaler_path = os.path.join(dir, 'scaler.gz')
            scaler = joblib.load(scaler_path)
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

        # store the optimal training loss of each model
        losses.append(loss[-patience])

        # load all the parameters into the trained network and save
        loaded_model.load_state_dict(torch.load(network_path))
        models.append(loaded_model)
        scalers.append(scaler)

    losses = np.array(losses)
    models = np.array(models)
    scalers = np.array(scalers)

    kmeans = KMeans(n_clusters=2, random_state=0).fit(losses.reshape(-1,1))
    cluster_labels = kmeans.labels_
    cluster_nr_low_loss = np.argmin(kmeans.cluster_centers_)

    # find model indices in the low loss cluster
    idx_low_loss = np.argwhere(cluster_labels == cluster_nr_low_loss).flatten()

    if np.std(losses[idx_low_loss]) / np.std(losses) < 0.1: # if relative std has been reduced by a factor 10
        models_good = models[idx_low_loss]

        scalers = scalers[idx_low_loss]
    else: # don't select models based on clustering
        sigma_loss = (np.nanpercentile(losses, 84) - np.nanpercentile(losses, 16))
        los_med = np.nanpercentile(losses, 50)

        idx_low_loss = np.argwhere((los_med - 2 * sigma_loss < losses) & (losses < los_med + 2 * sigma_loss)).flatten()
        models_good = models[idx_low_loss]
        scalers = scalers[idx_low_loss]

    # retrieve the rep numbers of the models in the low loss cluster
    models_idx = []
    for idx in idx_low_loss:
        mc_idx = int(os.path.basename(model_dirs[idx]).split('mc_run_', 1)[1])
        models_idx.append(mc_idx)
    models_idx = np.array(models_idx) # original indexing

    return models_good, models_idx, scalers


def load_coefficients_nn(df, path_to_models, epoch=-1):
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
            for coeff, [c_train, path] in paths.items():
                loaded_models_lin, model_idx, scalers = load_models(c_train, path, epoch=epoch, lin=True)
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
            n_lin = np.array(n_lin)

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

    n_quad = np.array(n_quad)
    n_cross = np.array(n_cross)

    return [n_lin, model_idx], n_quad, n_cross


def plot_loss_overview(path_to_models, order, op):

    model_dir_base = path_to_models[order][op][-1]
    model_dirs = [os.path.join(model_dir_base, mc_run) for mc_run in os.listdir(model_dir_base) if mc_run.startswith('mc_run')]

    mc_reps = len(model_dirs)

    # patience
    # TODO: create training object so that the runcard does not to be loaded every time
    with open(os.path.join(model_dirs[0], 'run_card.json')) as json_data:
        patience = json.load(json_data)['patience']

    # load training and validation losses
    loss_train = []
    loss_val = []
    for i in range(mc_reps):
        with open(os.path.join(model_dir_base, 'mc_run_{}'.format(i), 'loss.out')) as f:
            loss_train.append([float(line) for line in f.read().splitlines()])
        with open(os.path.join(model_dir_base, 'mc_run_{}'.format(i), 'loss_val.out')) as f:
            loss_val.append([float(line) for line in f.read().splitlines()])

    ncols = 5
    nrows = int(np.ceil(mc_reps / ncols))

    fig = plt.figure(figsize=(ncols * 4, nrows * 4))

    from matplotlib.ticker import NullFormatter

    train_loss_best = np.array([loss[-patience] for loss in loss_train])

    for i in range(mc_reps):
        ax = plt.subplot(nrows, ncols, i + 1)
        epochs = np.arange(len(loss_train[i]))

        label_val = r'$L_{\mathrm{val}}$' if i == 0 else None
        label_train = r'$L_{\mathrm{tr}}$' if i == 0 else None

        loss_train_rep = np.array(loss_train[i])
        loss_val_rep = np.array(loss_val[i])

        #ratio_train = np.log(loss_train_rep[10:]) - np.log(loss_train_rep[:-10])
        #ratio_val = np.log(loss_val_rep[10:]) - np.log(loss_val_rep[:-10])

        # ax.plot(epochs[10:], ratio_train, label=label_train)
        # ax.plot(epochs[10:], ratio_val, label=label_val)
        ax.plot(epochs, loss_train_rep, label=label_train)
        ax.plot(epochs, loss_val_rep, label=label_val)
        ax.axvline(epochs[-patience], 0, 0.75, color='red', linestyle='dotted')

        #ax.set_yscale('log')
        # ax.yaxis.set_major_formatter(NullFormatter())
        # ax.yaxis.set_minor_formatter(NullFormatter())
        # ax.axes.yaxis.set_ticklabels([])
        ax.set_ymargin(0.1)
        ax.set_xmargin(0)

        ax.text(0.9, 0.9, r"$\mathrm{{rep}}\;{}$".format(i), horizontalalignment='right',
                 verticalalignment='center',
                 transform=ax.transAxes)


        #ymax = loss_val[i][min([50, epochs[-patience] - 20])]
        #ymin = min(np.log10(loss_train[i])) - 0.1 * (np.log10(ymax) - min(np.log10(loss_train[i])))
        #ax.set_ylim(top=ymax)
        #ax.set_ylim(10 ** ymin, ymax)
        ax.set_xlim(left=10)

        #ax.set_ylim(min([np.min(loss_val_rep[-patience - 50:]), np.min(loss_train_rep[-patience -50:])]), max([np.max(loss_val_rep[-patience-50:]), np.max(loss_train_rep[-patience - 50:]) ]))
        #ax.set_ylim(-0.001, 0.001)

        med_loss = np.percentile(train_loss_best, 50)
        low_loss = np.percentile(train_loss_best, 16)
        high_loss = np.percentile(train_loss_best, 84)
        loss_sigma = np.abs((high_loss - low_loss)/2)

        #ax.set_ylim(np.percentile(train_loss_best, 16), np.percentile(train_loss_best, 84))
        #ax.set_ylim(loss_train_rep[-1], loss_val_rep[-patience] + 0.5)
        ax.set_ylim(loss_train_rep[-1] - 0.2 * loss_sigma, loss_train_rep[-1] + 0.8 * loss_sigma)

        signif = (train_loss_best[i] - med_loss) / loss_sigma

        ax.text(0.9, 0.8, r"$Z={:.2f}$".format(signif), horizontalalignment='right',
                verticalalignment='center',
                transform=ax.transAxes)

        #ax.fill_between(epochs, low_loss, high_loss, alpha=0.3)
        #ax.axhline(med_loss, 0, 1, color='k', linestyle='dotted')

        if i == 0:
            ax.legend(loc="lower left", frameon=False)

    plt.tight_layout()

    fig_delta = plt.figure(figsize=(ncols * 4, nrows * 4))

    for i in range(mc_reps):
        ax = plt.subplot(nrows, ncols, i + 1)
        epochs = np.arange(len(loss_train[i]))

        label_val = r'$L_{\mathrm{val}}$' if i == 0 else None
        label_train = r'$L_{\mathrm{tr}}$' if i == 0 else None

        loss_train_rep = np.array(loss_train[i])
        loss_val_rep = np.array(loss_val[i])

        ratio_train = loss_train_rep[10:] - loss_train_rep[:-10]
        ratio_val = loss_val_rep[10:] - loss_val_rep[:-10]

        ax.plot(epochs[10:][-patience - 50:], ratio_train[-patience - 50:], label=label_train)
        ax.plot(epochs[10:][-patience - 50:], ratio_val[-patience - 50:], label=label_val)
        ax.axvline(epochs[-patience], 0, 0.75, color='red', linestyle='dotted')

        ax.set_ymargin(0.1)
        ax.set_xmargin(0)

        ax.text(0.9, 0.9, r"$\mathrm{{rep}}\;{}$".format(i), horizontalalignment='right',
                verticalalignment='center',
                transform=ax.transAxes)


        #ax.set_xlim(left=10)

        ax.set_ylim(-0.03, 0.03)


        if i == 0:
            ax.legend(loc="lower left", frameon=False)

    plt.tight_layout()

    #loss_ana = analytical_loss([10, 0])

    fig_loss_dist, ax = plt.subplots(figsize=(10, 6))
    kwargs = dict(histtype='stepfilled', alpha=0.3, density=False, bins=20, ec="k")
    ax.hist(train_loss_best, **kwargs, label=r'$\rm{Training}\;\rm{loss}$')
    plt.xlabel(r'$L_{\mathrm{tr}}$')
    plt.ylabel(r'$n_{\mathrm{rep}}$')


    return fig, fig_loss_dist, fig_delta


def analytical_loss(c):

    def integrand(y, m_x):

        # convert features to pandas dataframe
        df = pd.DataFrame({'m_zh': [m_x], 'y': [y]})

        # analytical decision function
        g = decision_function_truth(df, c, n_kin=2, process='ZH', lin=True, quad=False)

        # diff xsec in EFT
        dsigma_dx_eft = vh_prod.dsigma_dmvh_dy(y, m_x, -10, 0, True, False)

        # diff xsec in SM
        dsigma_dx_sm = vh_prod.dsigma_dmvh_dy(y, m_x, 0, 0, True, False)

        return - dsigma_dx_eft * np.log(1 - g) - dsigma_dx_sm * np.log(g)

    loss = integrate.dblquad(integrand, 0.25, 2.0, lambda m_x: -np.log(np.sqrt(col_s)/m_x), lambda m_x:np.log(np.sqrt(col_s)/m_x))

    return loss[0]


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

    # mzh = events['m_tt'].values
    # mask = np.argwhere(mzh < 0.5).flatten()
    # mask_comp = np.setdiff1d(np.arange(len(events)), mask)

    # overview plot for all replicas
    ncols = 5
    mc_reps = r_nn.shape[0]
    nrows = int(np.ceil(mc_reps/ncols))

    fig1 = plt.figure(figsize=(ncols * 4, nrows * 4))

    x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)

    #for i in range(mc_reps):

    for i in np.argsort(model_idx):
        ax = plt.subplot(nrows, ncols, model_idx[i] + 1)
        # plt.scatter(tau_truth[mask_comp], tau_nn[i, mask_comp], s=2, color='k')
        # plt.scatter(tau_truth[mask], tau_nn[i, mask], s=2, color='red')
        plt.scatter(tau_truth, tau_nn[i,:], s=2, color='k')
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

    # plt.scatter(tau_truth[mask_comp], np.median(tau_nn, axis=0)[mask_comp], s=5, color='k')
    # plt.scatter(tau_truth[mask], np.median(tau_nn, axis=0)[mask], s=5, color='red')
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
    [n_lin_matched, model_idx], n_quad, n_cross = load_coefficients_nn(df, path_to_models, epoch=epoch)

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


def decision_function_nn(df, c, train_parameters, path_to_models, epoch=-1, lin=False, quad=False):
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
    ratio, model_idx = likelihood_ratio_nn(df, c, train_parameters, path_to_models, epoch, lin=lin, quad=quad)
    f = 1 / (1 + ratio)
    return f

def accuracy_1d(c, path_to_models, c_train, process, epoch, lin, quad, cut):

    fig, ax = plt.subplots(figsize=(10,6))

    x = np.linspace(cut, 3.0, 200)
    x = np.stack((x, np.zeros(len(x))), axis=-1)

    if process == 'tt':
        df = pd.DataFrame(x, columns=['m_tt', 'y'])
    elif process == 'ZH':
        df = pd.DataFrame(x, columns=['m_zh', 'y'])

    f_ana_lin = decision_function_truth(df, c, n_kin=2, process=process, lin=True, quad=False)

    f_preds_nn = decision_function_nn(df, c, c_train,
                                 path_to_models,
                                 lin=True, quad=False)

    f_pred_up = np.percentile(f_preds_nn, 84, axis=0)
    f_pred_down = np.percentile(f_preds_nn, 16, axis=0)

    ax.fill_between(x[:, 0], f_pred_down, f_pred_up, label=r'$\rm{NN}\;\mathcal{O}\left(\Lambda^{-2}\right)$', alpha=0.4)

    ax.plot(x[:, 0], f_ana_lin, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-2}\right)$')

    # single replica
    #ax.plot(x[:, 0], f_preds_nn[0,:], '--', c='blue', label=r'$\rm{NN}\;\mathcal{O}\left(\Lambda^{-2}\right)$')

    plt.ylim((0, 1))
    plt.xlim(np.min(x[:, 0]), np.max(x[:, 0]))
    #plt.xlim(np.min(x[:, 0]), 0.5)

    plt.ylabel(r'$f\;(x, c)$')
    xlabel = r'$m_{ZH}\;\rm{[TeV]}$' if process == 'ZH' else r'$m_{t\bar{t}}\;\rm{[TeV]}$'
    plt.xlabel(xlabel)
    plt.legend()
    plt.tight_layout()
    return fig
