"""
Post-training analysing module to load, plot and evaluates models
"""

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np
import torch
import sys
import copy
import matplotlib.gridspec as gridspec
from matplotlib import animation
from matplotlib.ticker import NullFormatter
import os, sys
import pickle
import joblib
import json
import pandas as pd
from sklearn.cluster import KMeans
from scipy import integrate
import logging
import itertools

# import own pacakges
from ml4eft.core import classifier as classifier
from ml4eft.core.truth import tt_prod as axs
from ml4eft.core.truth import vh_prod, tt_prod
from ..preproc import constants

mz = constants.mz  # z boson mass [TeV]
mh = constants.mh
mt = constants.mt
col_s = constants.col_s

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


class Analyse:
    """
    Post-training analyser that loads and evaluates models
    """

    def __init__(self, path_to_models, order='quad', all=True):

        """
        Analyse constructor

        Parameters
        ----------
        path_to_models: dict
            Of the form {'lin': {'c1': ``<path_to_c1_models>``, 'c2': ``<path_to_c2_models>``}, 'quad': {'c1_c1': ``<path_to_c1_c1_models>``},
            {'c1_c2': ``<path_to_c1_c2_models>``}, {'c2_c2': ``<path_to_c2_c2_models>``}}
        order: str, default='quad'
            The order in the EFT expansion (choose between either 'lin' or 'quad')

        Examples
        --------
        Trained models can be loaded by creating an :class:`ml4eft.analyse.analyse.Analyse` object

        >>> analyser = Analyse(path_to_models, 'quad')

        Followed by constructing a model dictionary that contains all the models plus associated settings

        >>> analyser.build_model_dict()
        >>> analyser.model_df
                        models              idx             scalers                                       run_card              rep_paths
        lin  c1         [Classifier() ...   [rep_idx, ...]  [RobustScaler(quantile_range=(5,95)), ...]    {'name': 'c1', ...}   [<path_to_rep>, ...]
             c2         [Classifier() ...   ...             ...                                           ...                   ...
        quad c1_c1      [Classifier() ...   ...             ...                                           ...                   ...
             c1_c2      [Classifier() ...   ...             ...                                           ...                   ...
             c2_c2      [Classifier() ...   ...             ...                                           ...                   ...

        Events and the inclusive cross-section can be loaded into a DataFrame by

        >>> df, xsec = analyser.load_events('.../events_<rep>.pkl.gz')
        >>> df
                  sqrts_hat       pt_l1       pt_l2  pt_l_leading  pt_l_trailing   ...
        1       1702.356400   20.532279  308.295118    308.295118      20.532279   ...
        2       ...           ...        ...           ...             ...

        To evaluate the models on the loaded DataFrame ``df``, use:

        >>> analyser.evaluate_models(df)
        >>> analyser.models_evaluated_df['models']
        >>> analyser.models_evaluated_df['models']
        lin   c1            [[0.05130317, 0.05723376, 0.058220766, 0.04042...
              c2            [[0.074420996, 0.10293982, 0.10705493, 0.05695...
        quad  c1_c1         [[0.07958487, 0.13463444, 0.14215767, 0.049889...
              c1_c2         [[0.0005354581, 0.00042073405, 0.0004430262, -...
              c2_c2         [[0.00032746396, 0.00041523552, 0.00045115477,...

        """

        self.path_to_models = path_to_models
        self.order = order
        self.model_df = None
        self.models_evaluated_df = None
        self.coeff_truth = None
        self.all = True

    @staticmethod
    def get_event_paths(root_path):
        """
        Returns a list of paths to the DataFrames at ``root_path``

        Parameters
        ----------
        root_path: str
            path to the DataFrame directory

        Returns
        -------
        event_paths: list
            list of paths to the DataFrames at stored at ``root_path``

        Examples
        --------
        The paths to the event DataFrames stored at ``root_path`` can be loaded for 'n_rep' replicas by

        >>> analyser.get_event_paths('/training_data/tt_llvlvlbb/tt_c1')
        [/training_data/tt_llvlvlbb/tt_c1/events_0.pkl.gz', ... , /training_data/tt_llvlvlbb/tt_c1/events_<n_rep>.pkl.gz']
        """
        event_paths = [os.path.join(root_path, mc_run) for mc_run in
                       os.listdir(root_path) if mc_run.startswith('events_')]
        return event_paths

    @staticmethod
    def build_path_dict(root, order, prefix):
        """
        Construct path to model dictionary

        Parameters
        ----------
        root: str
            Path to the model root directory
        order: str
            Order of the EFT expansion, choose between 'lin' and 'quad'
        prefix: str
            For models: `prefix` = ``models``, for theory predictions: `prefix` = ``process_id`

        Returns
        -------
        path_to_models: dict
            Dictionary containing the paths to the models for each EFT ratio function
        """
        path_to_models = {}

        if prefix != 'model':
            path_to_models['sm'] = os.path.join(root, '{}_sm'.format(prefix))

        path_to_models['lin'] = {}

        if order == 'quad':
            path_to_models['quad'] = {}

        for model_dir in os.listdir(root):
            if model_dir.startswith(prefix):
                if 'sm' in model_dir:  # sm has already been added
                    continue
                # linear
                if model_dir.count('_') == 1:
                    path_to_models['lin'].update(
                        {model_dir.split("{}_".format(prefix), 1)[1]: os.path.join(root, model_dir)})

                if model_dir.count('_') == 2 and order == 'quad':
                    path_to_models['quad'].update(
                        {model_dir.split("{}_".format(prefix), 1)[1]: os.path.join(root, model_dir)})
            else:
                continue

        return path_to_models

    @staticmethod
    def posterior_loader(path):
        """Loads the posterior samples at ``path`` and converts it to a DataFrame

        Parameters
        ----------
        path: str
            Location of posterior samples (.json file)

        Returns
        -------
        df: pandas.DataFrame
            DataFrame of the posterior samples
        """
        with open(path) as json_data:
            samples = json.load(json_data)
        df = pd.DataFrame(samples)
        return df

    @staticmethod
    def load_events(event_path):
        """
        Loads a event DataFrame and splits it into the events and the inclusive cross section

        Parameters
        ----------
        event_path: str
            Path to the DataFrame (including the xsec as first row)

        Returns
        -------
        events: pandas.DataFrame
            DataFrame with events
        xsec: float
            Inclusive cross-section of the events
        """
        event_df = pd.read_pickle(event_path)
        events = event_df.iloc[1:, :]
        xsec = event_df.iloc[0, 0]

        return events, xsec

    @staticmethod
    def load_loss(path_to_loss):
        """
        Loades the losses per epoch into a list

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
        Loads training run card

        Parameters
        ----------
        path: str
            path to json model run card that stores the hyperparameter settings

        Returns
        -------
        run_card: dict
            dict with all the hyperparameter settings
        """
        with open(path) as json_data:
            run_card = json.load(json_data)
        run_card['architecture'] = [len(run_card['features'])] + run_card['hidden_sizes'] + [run_card['output_size']]

        return run_card

    def filter_out_models(self, losses):
        """
        Filter out the badly trained models based on kmeans clustering.

        Parameters
        ----------
        losses: array_like
            Losses of all the trained models

        Returns
        -------
        good_model_idx: numpy.ndarray
            Array indices of the 'good' models
        """

        if self.all:
            return np.arange(len(losses.flatten()))
        else:
            n_clusters = 2

        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(losses.reshape(-1, 1))
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

    def load_models(self, model_path, rep=None, epoch=-1):
        """
        Loads the trained models

        Parameters
        ----------
        model_path: str
            path to model directory
        rep: int, optional
            Load only a specific replica specified by ``rep``. Load all replicas by default.
        epoch: int, optional
            Model at specific epoch to load. Set to the best model by default.

        Returns
        -------
        models: array_like
            ``(N,) ndarray`` containing the loaded neural networks

        models_rep_nr: array_like
            ``(N,) ndarray`` containing the replica numbers of the loaded neural networks

        scalers: array_like
            ``(N,) ndarray`` containing the preprocessing scalers of the loaded neural networks

        run_card: dict
            training run card of the trained models

        rep_paths: array_like
            ``(N,) ndarray`` with the paths to the neural networks

        """

        # collect all replica paths when no specific replica is requested
        if rep is None:
            rep_paths = [os.path.join(model_path, mc_run) for mc_run in os.listdir(model_path) if
                         mc_run.startswith('mc_run')]
        else:
            rep_paths = [os.path.join(model_path, 'mc_run_{}'.format(rep))]

        losses_tr = []  # to store the final training losses
        losses_val = []  # to store the final validation losses

        models = []
        scalers = []

        for rep_path in rep_paths:

            path_to_run_card = os.path.join(rep_path, 'run_card.json')
            path_to_scaler = os.path.join(rep_path, 'scaler.gz')

            if not os.path.isfile(path_to_scaler):  # if model did not get trained, jump to the next one
                rep_paths.remove(rep_path)
                continue

            run_card = self.load_run_card(path_to_run_card)
            scaler = joblib.load(path_to_scaler)

            model_name = os.path.basename(model_path)
            c_name = model_name.split('model_')[1]
            c_train = run_card['c_train']

            quadratic = True if '_' in c_name else False
            if quadratic:
                c1, c2 = c_name.split('_')
                c_train_value = c_train[c1] * c_train[c2]
            else:
                c_train_value = c_train[c_name]

            loaded_model = classifier.Classifier(run_card['architecture'], c_train_value)

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
            path_to_loss_tr = os.path.join(rep_path, 'loss.out')
            path_to_loss_val = os.path.join(rep_path, 'loss_val.out')

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

        # filter out the badly trained models based on their training loss only if all replicas
        # have been included
        models_rep_nr = None

        if rep is None:
            good_model_idx = self.filter_out_models(losses_tr)
            models = models[good_model_idx]
            scalers = scalers[good_model_idx]

            # map model indices back to rep number
            models_rep_nr = []
            for idx in good_model_idx:
                rep_nr = int(os.path.basename(rep_paths[idx]).split('mc_run_', 1)[1])
                models_rep_nr.append(rep_nr)
            models_rep_nr = np.array(models_rep_nr)

            rep_paths = np.array(rep_paths)[good_model_idx]

        return models, models_rep_nr, scalers, run_card, rep_paths

    def build_model_dict(self, rep=None, epoch=-1):
        """
        Constructs a DataFrame with loaded models plus associated info

        Parameters
        ----------
        rep: int, optional
            Replica number in case a specific replica is requested
        epoch: int, optional
            Epoch to load, set to the best model by default
        """

        from collections import defaultdict

        self.model_dict = defaultdict(dict)

        for order, dict_fo in self.path_to_models.items():
            if self.order == 'lin' and order == 'quad':  # skip quadratics when running linear
                continue
            for c_name, model_path in dict_fo.items():
                pretrained_models, models_idx, scalers, run_card, rep_paths = self.load_models(model_path, rep, epoch)
                self.model_dict[order][c_name] = {'models': pretrained_models, 'idx': models_idx, 'scalers': scalers,
                                                  'run_card': run_card, 'rep_paths': rep_paths}

        self.model_df = pd.DataFrame.from_dict({(i, j): self.model_dict[i][j]
                                                for i in self.model_dict.keys()
                                                for j in self.model_dict[i].keys()},
                                               orient='index')

    def evaluate_models(self, df, rep=None, epoch=-1):
        """
        Evaluates the loaded models on a Pandas DataFrame ``df``

        Parameters
        ----------
        df: pd.DataFrame
            input to the models
        rep: int, optional
            Replica number in case a specific replica is requested.
            Set to ``None`` by default in which case all available replicas are included.
        epoch: int, optional
            Epoch number to load. Set to the best model by default.

        """

        # load models if not done already
        if rep is not None:
            self.build_model_dict(rep, epoch)
        if self.model_df is None:
            self.build_model_dict(rep, epoch)

        models_evaluated = copy.deepcopy(self.model_dict)

        for order, dict_fo in self.model_dict.items():
            for c_name, dict_c in dict_fo.items():
                models = dict_c['models']

                for i, model in enumerate(models):
                    features = dict_c['run_card']['features']
                    features_scaled = dict_c['scalers'][i].transform(df[features])
                    with torch.no_grad():
                        model_ev = model.n_alpha(torch.tensor(features_scaled).float()).numpy().flatten()
                    models_evaluated[order][c_name]['models'][i] = model_ev

                models_evaluated[order][c_name]['models'] = np.vstack(models_evaluated[order][c_name]['models'])

        self.models_evaluated_df = pd.DataFrame.from_dict({(i, j): models_evaluated[i][j]
                                                           for i in models_evaluated.keys()
                                                           for j in models_evaluated[i].keys()},
                                                          orient='index')

    def coeff_function_truth(self, df, c_name, features, process, order):
        """
        Evaluates the analytic EFT ratio functions :math:`r_{\sigma}^{(i)}` and :math:`r_{\sigma}^{(i,j)}`

        Parameters
        ----------
        df: pandas.DataFrame
            Events on which to evaluate :math:`r_{\sigma}^{(i)}` and :math:`r_{\sigma}^{(i,j)}`
        c_name: str
            Name of the EFT coefficient. Choose between 'ctgre', 'cut', 'cut_cut', 'ctgre_ctgre'
        features: list
            Kinematic features, options are ``m_tt``, ``y``
        process: str
            Supported options are 'tt' or 'ZH'
        order: str
            Order of the EFT expansion, choose between 'lin' and 'quad'

        Returns
        -------
        coeff: array_like
            ``(N,) ndarray`` with :math:`r_{\sigma}^{(i)}` or :math:`r_{\sigma}^{(i,j)}` evaluated on ``df`` depending
            on the ``order``
        """

        if c_name == 'ctGRe' and order == 'lin':
            cprime = {'ctGRe': -10, 'ctu8': 0}
        elif c_name == 'ctu8' and order == 'lin':
            cprime = {'ctGRe': 0, 'ctu8': 10}
        elif c_name == 'ctGRe_ctGRe' and order == 'quad':
            cprime = {'ctGRe': 10, 'ctu8': 0}
            c_name = 'ctGRe'
        if c_name == 'ctu8_ctu8' and order == 'quad':
            cprime = {'ctGRe': 0, 'ctu8': 10}
            c_name = 'ctu8'

        # ratio_truth_lin = self.likelihood_ratio_truth(df, cprime, features, process, order)

        ratio_truth_lin = self.likelihood_ratio_truth(df, cprime, features, process, order)
        # compute the mask once to select the physical region in phase space
        mask = ratio_truth_lin == 0

        if order == 'lin':  # only one of the c elements can be nonzero
            coeff = np.ma.masked_where(mask, (ratio_truth_lin - 1) / cprime[c_name])
            return coeff
        elif order == 'quad':  # only one of the c elements can be nonzero
            coeff = np.ma.masked_where(mask, (ratio_truth_lin - 1) / cprime[c_name] ** 2)
            return coeff

    def accuracy_heatmap(self, c_name, order, process, mx_cut=None, rep=None, epoch=-1, ax=None, text=None):
        """
        Compares the NN and true EFT ratio functions and plots their ratio and pull

        Parameters
        ----------
        c_name: str
            Name of the EFT parameter, e.g. 'ctgre'
        order: str
            Order in the EFT expansion, options are 'lin' or 'quad'
        process: str
            Specifies the process. Currently supported is 'tt' and 'ZH'
        mx_cut: list, optional
            Plot range of the invariant mass
        rep: int, optional
            Request to plot for a specific replica
        epoch: int, optional
            Request to plot for a specific epoch.
        ax: matplotlib.pyplot.axes, optional
            Axes to plot on
        text: str, optional
            Add additional text on the heatmap such as the replica number


        Returns
        -------
        matplotlib.figure.Figure
            Heatmap of EFT ratio function
        `matplotlib.figure.Figure`
            Heatmap of associated pull

        Examples
        --------
        For a single EFT coefficient :math:`c_{tG}` the likelihood ratio takes the form

        .. math::

            r_{\sigma}(x, c_{tG}) = 1 + c_{tG} r_{\sigma}^{(c_{tG})} + c_{tG}^2 r_{\sigma}^{(c_{tG}, c_{tG})}

        To plot for example the accuracy of :math:`r_{\sigma}^{(c_{tG}, c_{tG})}` by plotting its ratio to the exact
        result, one runs

        >>> fig_med, fig_pull = analyser.accuracy_heatmap('ctgre_ctgre', 'quad', 'tt')
        >>> fig_med

        .. image:: ../images/heatmap_med.png

        >>> fig_pull

        .. image:: ../images/heatmap_pull.png

        """
        s = constants.col_s ** 2
        epsilon = 1e-2

        if process == 'ZH':
            if mx_cut is None:
                mx_min, mx_max = mz + mh + epsilon, 3
            else:
                mx_min, mx_max = mx_cut

        elif process == 'tt':
            if mx_cut is None:
                mx_min, mx_max = 2 * mt + epsilon, 3
            else:
                mx_min, mx_max = mx_cut

        y_min, y_max = - np.log(np.sqrt(s) / mx_min), np.log(np.sqrt(s) / mx_min)

        x_spacing, y_spacing = 1e-2, 0.01
        mx_span = np.arange(mx_min, mx_max, x_spacing)
        y_span = np.arange(y_min, y_max, y_spacing)

        mx_grid, y_grid = np.meshgrid(mx_span, y_span)
        grid = np.c_[mx_grid.ravel(), y_grid.ravel()]

        if process == 'ZH':
            df = pd.DataFrame({'y': grid[:, 1], 'm_zh': grid[:, 0]})
        elif process == 'tt':
            df = pd.DataFrame({'y': grid[:, 1], 'm_tt': grid[:, 0]})

        # models

        self.evaluate_models(df, rep, epoch)
        nn = self.models_evaluated_df.loc[order, c_name]['models']
        nn = np.vstack(nn)
        n_models = nn.shape[0]

        nn = nn.reshape((n_models, *mx_grid.shape))

        # truth

        features = df.columns.values

        if self.coeff_truth is None:
            self.coeff_truth = self.coeff_function_truth(df, c_name, features, process, order).reshape(
                mx_grid.shape)

        xlabel = r'$m_{ZH}\;\rm{[TeV]}$' if process == 'ZH' else r'$m_{t\bar{t}}\;\rm{[TeV]}$'
        if rep is None:

            # determine median, low and high CI

            nn_median = np.percentile(nn, 50, axis=0)
            nn_high = np.percentile(nn, 84, axis=0)
            nn_low = np.percentile(nn, 16, axis=0)
            nn_unc = (nn_high - nn_low) / 2
            # median
            median_ratio = self.coeff_truth / nn_median
            title = r'$\rm{Unbinned\;exact/Unbinned\;ML}$'

            fig_1, ax_1 = plt.subplots(figsize=(10, 8))

            im_1 = self.plot_heatmap(ax[0], median_ratio,
                                     xlabel=xlabel,
                                     ylabel=r'$y_{t\bar{t}}$',
                                     title=title,
                                     extent=[mx_min, mx_max, y_min, y_max],
                                     cmap='seismic',
                                     bounds=[0.95, 0.96, 0.97, 0.98, 1.02, 1.03, 1.04, 1.05],
                                     text=text)

            # pull

            fig_2, ax_2 = plt.subplots(figsize=(10, 8))

            pull = (self.coeff_truth - nn_median) / nn_unc

            im_2 = self.plot_heatmap(ax[1], pull,
                                     xlabel=xlabel,
                                     ylabel=r'$y_{t\bar{t}}$',
                                     title=r'$\rm{Pull}$',
                                     extent=[mx_min, mx_max, y_min, y_max],
                                     cmap='seismic',
                                     bounds=np.linspace(-1.5, 1.5, 10),
                                     text=text)

            return ax[0], ax[1]
        else:
            title = r"$\mathrm{{Truth/NN}}\;(\mathrm{{rep}}\;{})$".format(rep)
            im = self.plot_heatmap(ax, self.coeff_truth / nn[0],
                                   xlabel=xlabel,
                                   ylabel=r'$y_{t\bar{t}}$',
                                   title=title,
                                   extent=[mx_min, mx_max, y_min, y_max],
                                   cmap='seismic',
                                   bounds=[0.95, 0.96, 0.97, 0.98, 1.02, 1.03, 1.04, 1.05],
                                   rep=rep)
            return im

    def plot_heatmap_overview(self, c_name, order, process, mx_cut=None, reps=None, epoch=-1):
        """
        Produces an overview of heatmaps showing in each plot the ratio between the ML model prediction and
        the analytical EFT ratio function :math:`r_{\sigma}^{(i)}` or :math:`r_{\sigma}^{(i, j)}`

        Parameters
        ----------
        c_name: str
            Name of EFT coefficient
        order: str
            Order in the EFT expansion
        process: str
            Specifies the process, choose between 'tt' and 'ZH'
        mx_cut: float, optional
            Plot range of the invariant mass
        reps: int, optional
            Number of replicas to include in the heatmap overview
        epoch: int, optional
            Specific epoch to plot at, takes the best models by default

        Returns
        -------
        fig: matplotlib.figure

        Examples
        --------
        To produce a heatmap overview of the first 20 replicas, run

        >>> analyser = Analyse(path_to_models, 'quad')
        >>> fig = analyser.plot_heatmap_overview('ctgre_ctgre', 'quad', 'tt', cut=0.5, reps=np.arange(20))
        >>> fig

        .. image:: ../images/heatmap_overview.png

        """
        from mpl_toolkits.axes_grid1 import AxesGrid

        rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 50})

        n_cols = 4
        mc_reps = len(reps)
        n_rows = int(np.ceil(mc_reps / n_cols))

        fig = plt.figure(figsize=(10 * n_cols, 10 * n_rows))

        grid = AxesGrid(fig, 111,
                        nrows_ncols=(n_rows, n_cols),
                        axes_pad=1.0,
                        cbar_mode='single',
                        cbar_location='bottom',
                        cbar_pad=1.5,
                        cbar_size=0.5
                        )

        for i, rep in enumerate(reps):
            im = self.accuracy_heatmap(c_name, order, process, mx_cut, rep, epoch, grid[i])

        grid[-1].cax.colorbar(im)
        grid.cbar_axes[0].colorbar(im)

        return fig

    def likelihood_ratio_nn(self, c, df=None, epoch=-1):
        """
        Compute the Neural Network parameterised likelihood ratio

        Parameters
        ----------
        c: dict
            Of the form {'c1': value, 'c2': value, ...}
        df: pandas.DataFrame, optional
            In case the loaded models have not been evaluated yet, one can pass ``df`` to evaluate the neural networks
        epoch: int, optional
            Specify an epoch if necessary, takes the best model by default

        Returns
        -------
        ratio: array_like
            likelihood ratio as ``(N,M) ndarray`` with ``N`` and ``M`` the number of replicas and events respectively
        """
        # update evaluated models for a new df
        if df is not None:
            self.evaluate_models(df, epoch=epoch)

        ratio = 1

        if 'lin' in self.models_evaluated_df.index:
            lin_models = self.models_evaluated_df['models'].loc["lin"]
            for c_name, c_val in c.items():
                if c_name in lin_models:
                    ratio += c_val * lin_models[c_name]

        if 'quad' in self.models_evaluated_df.index:
            quad_models = self.models_evaluated_df['models'].loc["quad"]

            for (c1, c2) in itertools.product(c.keys(), repeat=2):
                c_name = '{}_{}'.format(c1, c2)
                if c_name in quad_models:
                    ratio += c[c1] * c[c2] * quad_models['{}_{}'.format(c1, c2)]

        ratio = np.vstack(ratio)

        return ratio

    def decision_function_nn(self, c, df=None, epoch=-1):
        """
        Computes the Neural Network parameterised decision function :math:`g(x, c)`

        Parameters
        ----------
        df: pd.DataFrame
            event info
        c: dict
            EFT point
        epoch: int, optional
            Use models at a specific epoch, set to -1 (best modeL) by default

        Returns
        -------
        decision_function: numpy.ndarray
            NN decision function
        """
        ratio = self.likelihood_ratio_nn(c, df, epoch=epoch)
        decision_function = 1 / (1 + ratio)
        return decision_function

    def point_by_point_comp_med(self, df, c, features, process, order, ax, text=None):
        """
        Produces a point by point comparison of the log-likelihood ratio between the (median) ML model and the analytical
        (exact) model

        Parameters
        ----------
        df: pandas.DataFrame
            DataFrame with events
        c: dict
            Of the form {'c1': value, 'c2': value}
        features: array_like
            List of features to include in the comparison
        process: str
            Choose between ``tt`` or ``ZH``
        order: str
            Specifies the order in the EFT expansion. Must be one of ``lin``, ``quad``.
        ax: matplotlib.axes
            Axes object to plot on
        text: str
            Additonal text to put on the plot

        Examples
        --------
        >>> analyser = Analyse(path_to_models, 'quad')
        >>> fig, ax = plt.subplots()

        >>> events_sm = pd.read_pickle('<events_sm_0.pkl.gz>')
        >>> analyser.point_by_point_comp_med(events_sm, {'ctgre': 2, 'cut': 0}, ['y', 'm_tt'], 'tt', 'lin')
        >>> fig

        .. image:: ../images/pbp-med.png

        """
        r_nn = self.likelihood_ratio_nn(c, df=df)
        tau_nn = np.log(r_nn)

        r_truth = self.likelihood_ratio_truth(df, c, features, process, order)
        tau_truth = np.log(r_truth)

        fig = plt.figure(figsize=(8, 8))
        x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)

        ax.scatter(tau_truth, np.median(tau_nn, axis=0), s=2, color='red')
        ax.plot(x, x, linestyle='dashed', color='grey')
        ax.set_xlabel(r'$\log r(x, c)^{\rm{Unbinned}\;\rm{exact}}$')
        ax.set_ylabel(r'$\log r(x, c)^{\rm{Unbinned}\;\rm{ML}}$')
        ax.set_xlim((np.min(x), np.max(x)))
        ax.set_ylim((np.min(x), np.max(x)))

        if text is not None:
            ax.text(0.95, 0.1, text,
                    horizontalalignment='right',
                    verticalalignment='center',
                    transform=ax.transAxes)

        fig.tight_layout()

    def point_by_point_comp(self, df, c_name, c, features, process, order):
        """
       Produces a point by point comparison overview per replica of the log-likelihood ratio between the ML model
       and the analytical (exact) model

       Parameters
       ----------
       df: pandas.DataFrame
           DataFrame with events
       c_name: str
            name of EFT ratio function to compare, e.g. ``c1_c2``
       c: dict
           Of the form {'c1': value, 'c2': value}
       features: array_like
           List of features to include in the comparison
       process: str
           Choose between ``tt`` or ``ZH``
       order: str
           Specifies the order in the EFT expansion. Must be one of ``lin``, ``quad``.

       Examples
       --------
       >>> analyser = Analyse(path_to_models, 'quad')
       >>> fig, ax = plt.subplots()

       >>> events_sm = pd.read_pickle('<events_sm_0.pkl.gz>')
       >>> analyser.point_by_point_comp(events_sm, {'ctgre': -2, 'cut': 0}, ['y', 'm_tt'], 'tt', 'lin')
       >>> fig

       .. image:: ../images/pbp_overview.png

       """

        r_nn = self.likelihood_ratio_nn(c, df=df)
        tau_nn = np.log(r_nn)

        r_truth = self.likelihood_ratio_truth(df, c, features, process, order)
        tau_truth = np.log(r_truth)

        # overview plot for all replicas
        ncols = 5
        mc_reps = r_nn.shape[0]
        nrows = int(np.ceil(mc_reps / ncols))

        fig1 = plt.figure(figsize=(ncols * 4, nrows * 4))

        x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)

        model_idx = self.model_df.loc[order, c_name]['idx']

        for i in np.argsort(model_idx):
            ax = plt.subplot(nrows, ncols, model_idx[i] + 1)

            plt.scatter(tau_truth, tau_nn[i, :], s=2, color='k')
            plt.plot(x, x, linestyle='dashed', color='grey')
            plt.text(0.1, 0.9, r"$\mathrm{{rep}}\;{}$".format(model_idx[i]), horizontalalignment='left',
                     verticalalignment='center',
                     transform=ax.transAxes)

            plt.xlim((np.min(x), np.max(x)))
            plt.ylim((np.min(x), np.max(x)))

        plt.tight_layout()

        # median
        fig2, ax = plt.subplots(figsize=(8, 8))
        x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)

        plt.scatter(tau_truth, np.median(tau_nn, axis=0), s=2, color='k')
        plt.plot(x, x, linestyle='dashed', color='grey')
        plt.xlabel(r'$\log r(x, c)^{\rm{Unbinned}\;\rm{exact}}$')
        plt.ylabel(r'$\log r(x, c)^{\rm{Unbinned}\;\rm{ML}}$')
        plt.xlim((np.min(x), np.max(x)))
        plt.ylim((np.min(x), np.max(x)))

        plt.tight_layout()

        return fig1, fig2

    def plot_loss_overview(self, c_name, order, ax=None, rep=None, xlim=None):
        """
        Plots the loss evolution per replica and returns an overview plot

        Parameters
        ----------
        c_name: str
            name of EFT parameter
        order: str
            Specifies the order in the EFT expansion. Must be one of ``lin``, ``quad``.
        ax: matplotlib.axes, optional
            Axes object to plot on
        rep: int, optional
            Specific replica to plot

        Returns
        -------
        fig: matplotlib.figure
            Loss overview plot

        train_loss_best: array_like
            List of 'best' training losses

        Examples
        --------
        To plot a loss overview corresponding to the training of :math:`r_{\sigma}^{(c_{tG}, c_{tG})}`, run

        >>> analyser = Analyse(path_to_models, 'quad')
        >>> fig, train_losses = analyser.plot_loss_overview('ctgre_ctgre', 'quad')
        >>> fig

        .. image:: ../images/loss_overview.png

        """
        if self.model_df is None:
            self.build_model_dict()

        rep_paths = self.model_df['rep_paths'][order][c_name]

        loss_tr = []
        loss_val = []

        mc_reps = len(rep_paths)
        ncols = 5
        nrows = int(np.ceil(mc_reps / ncols))

        patience = self.model_df.loc[order, c_name]['run_card']['patience']
        model_idx = self.model_df.loc[order, c_name]['idx']

        for rep_path in rep_paths:
            path_to_loss_tr = os.path.join(rep_path, 'loss.out')
            loss_tr.append(self.load_loss(path_to_loss_tr))

            path_to_loss_val = os.path.join(rep_path, 'loss_val.out')
            loss_val.append(self.load_loss(path_to_loss_val))

        fig = plt.figure(figsize=(ncols * 4, nrows * 4))

        train_loss_best = np.array([loss[-patience] for loss in loss_tr])
        val_loss_best = np.array([loss[-patience] for loss in loss_val])

        for i in np.argsort(model_idx):

            if rep is not None:
                if model_idx[i] != rep:
                    continue
            else:
                ax = plt.subplot(nrows, ncols, model_idx[i] + 1)

            epochs = np.arange(len(loss_tr[i]))

            label_val = r'$L_{\mathrm{val}}$' if model_idx[i] == 0 else None
            label_train = r'$L_{\mathrm{tr}}$' if model_idx[i] == 0 else None

            loss_train_rep = np.array(loss_tr[i])
            loss_val_rep = np.array(loss_val[i])

            if xlim is None:
                ax.set_xlim(left=50)
                ax.set_ylim(min(loss_train_rep[-1], loss_val_rep[-1]) - 0.2 * max(loss_sigma_val, loss_sigma_tr),
                            max(loss_train_rep[-1], loss_val_rep[-1]) + 0.8 * max(loss_sigma_val, loss_sigma_tr))

                ax.plot(epochs, loss_train_rep, label=label_train)
                ax.plot(epochs, loss_val_rep, label=label_val)

            else:
                ax.plot(epochs[xlim:], loss_train_rep[xlim:], label=label_train)
                ax.plot(epochs[xlim:], loss_val_rep[xlim:], label=label_val)

            ax.axvline(epochs[-patience], 0, 0.75, color='red', linestyle='dotted')

            # ax.set_yscale('log')
            # ax.yaxis.set_major_formatter(NullFormatter())
            # ax.yaxis.set_minor_formatter(NullFormatter())
            # ax.axes.yaxis.set_ticklabels([])
            ax.set_ymargin(0.1)
            ax.set_xmargin(0)

            ax.text(0.95, 0.9, r"$\mathrm{{rep}}\;{}$".format(model_idx[i]), horizontalalignment='right',
                    verticalalignment='center',
                    transform=ax.transAxes)

            ax.set_xlabel(r'$\mathrm{Epoch}$')
            ax.set_ylabel(r'$\mathrm{Loss}$')

            med_loss_tr = np.percentile(train_loss_best, 50)
            low_loss_tr = np.percentile(train_loss_best, 16)
            high_loss_tr = np.percentile(train_loss_best, 84)
            loss_sigma_tr = np.abs((high_loss_tr - low_loss_tr) / 2)

            med_loss_val = np.percentile(val_loss_best, 50)
            low_loss_val = np.percentile(val_loss_best, 16)
            high_loss_val = np.percentile(val_loss_best, 84)
            loss_sigma_val = np.abs((high_loss_val - low_loss_val) / 2)

            # same scale (not everything visible)

            # ax.set_ylim(min(loss_train_rep[-1], loss_val_rep[-1]) - 0.2 * max(loss_sigma_val, loss_sigma_tr),
            #             min(loss_train_rep[-1], loss_val_rep[-1]) + 2 * max(loss_sigma_val, loss_sigma_tr))

            # everything visible (not the same scale)
            ax.set_ylim(min(loss_train_rep[-1], loss_val_rep[-1]) - 0.2 * max(loss_sigma_val, loss_sigma_tr),
                        max(loss_train_rep[-1], loss_val_rep[-1]) + 0.8 * max(loss_sigma_val, loss_sigma_tr))

            if model_idx[i] == 0:
                ax.legend(loc="lower left", frameon=False)

        plt.tight_layout()

        return fig, train_loss_best

    def plot_accuracy_1d(self, c, c_name, process, order, mx_cut, epoch=-1, ax=None, text=None):
        """
        Plots the decision boundary :math:`g(x,c)` as predicted by the ML model and the analytical (exact) model along
        1 dimension, i.e :x=math:`m_{tt}`

        Parameters
        ----------
        c: dict
            Of the form {'c1': value, 'c2': value}
        process: str
            Choose between ``tt`` or ``ZH``
        order: str, optional
            Specifies the order in the EFT expansion. Must be one of ``lin``, ``quad``.
        mx_cut: list
            Plot range of the invariant mass
        epoch: int, optional
            Specific epoch to plot, set to the best models by default
        ax: matplotlib.axes, optional
            Plot on an already created axes object
        text: str, optional
            Additional text to show on the plot

        Returns
        -------
        fig: matplotlib.figure
            Plot comparing the decision boundary :math:`g(x,c)` as predicted by the ML model and the analytical (exact)
            result

        Examples
        --------
        >>> analyser = Analyse(path_to_models, 'quad')
        >>> fig = analyser.plot_accuracy_1d(c={'ctgre': -2, 'cut': 0}, process='tt', order='quad', cut=0.5, text=r'$c=c_{tG}=2\;\mathrm{quadratic}$')
        >>> fig

        .. image:: ../images/decission_function_1d.png

        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        else:
            fig = plt.subplots(figsize=(10, 6))

        x = np.linspace(mx_cut[0], mx_cut[1], 200)
        x = np.stack((np.zeros(len(x)), x), axis=-1)

        if process == 'tt':
            df = pd.DataFrame(x, columns=['y', 'm_tt'])
        elif process == 'ZH':
            df = pd.DataFrame(x, columns=['y', 'm_zh'])

        features = self.model_df['run_card'][order][c_name]['features']

        f_ana_lin = self.decision_function_truth(df, c, df.columns.values, process, order)
        f_preds_nn = self.decision_function_nn(c, df, epoch=epoch)

        f_pred_up = np.percentile(f_preds_nn, 84, axis=0)
        f_pred_down = np.percentile(f_preds_nn, 16, axis=0)

        ax.fill_between(x[:, 1], f_pred_down, f_pred_up,
                        label=r"$\mathrm{Unbinned}\;\mathrm{ML}\;(m_{t\bar{t}}, y_{t\bar{t}})$",
                        alpha=0.4)

        ax.plot(x[:, 1], f_ana_lin, '--', c='red',
                label=r"$\mathrm{Unbinned}\;\mathrm{exact}\;(m_{t\bar{t}}, y_{t\bar{t}})$")

        ax.set_ylim((0, 1))
        ax.set_xlim(np.min(x[:, 1]), np.max(x[:, 1]))

        ax.set_ylabel(r'$g\;(x, c)$')
        xlabel = r'$m_{ZH}\;\rm{[TeV]}$' if process == 'ZH' else r'$m_{t\bar{t}}\;\rm{[TeV]}$'
        ax.set_xlabel(xlabel)

        if text is not None:
            ax.text(0.05, 0.1, text,
                    horizontalalignment='left',
                    verticalalignment='center',
                    transform=ax.transAxes)

        ax.legend(frameon=False)
        plt.tight_layout()

        return fig

    @staticmethod
    def likelihood_ratio_truth(events, c, features, process, order=None):
        """
        Computes the analytic likelihood ratio :math:`r(x, c)`

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
        c : dict
            EFT point with operator names specified as keys

        Returns
        -------
        ratio: numpy.ndarray
            Likelihood ratio wrt the SM
        """

        n_features = len(features)

        if process == 'ZH':
            c = np.array([c['cHW'], c['cHq3']])
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
            c = np.array([c['ctGRe'], c['ctu8']])
            if n_features == 1:
                dsigma_0 = [tt_prod.dsigma_dmtt(*x[features], c, order) for _, x in events.iterrows()]  # EFT
                dsigma_1 = [tt_prod.dsigma_dmtt(*x[features]) for _, x in
                            events.iterrows()]  # SM
            elif n_features == 2:
                dsigma_0 = [tt_prod.dsigma_dmtt_dy(*x[features], c, order) for _, x in
                            events.iterrows()]  # EFT
                dsigma_1 = [tt_prod.dsigma_dmtt_dy(*x[features]) for _, x in
                            events.iterrows()]  # SM
            elif n_features == 3:
                dsigma_0 = [tt_prod.dsigma_dmtt_dy_dpt(*x[features], c, order) for
                            index, x in
                            events.iterrows()]  # EFT
                dsigma_1 = [tt_prod.dsigma_dmtt_dy_dpt(*x[features]) for
                            index, x in
                            events.iterrows()]  # SM

        dsigma_0, dsigma_1 = np.array(dsigma_0), np.array(dsigma_1)

        ratio = np.divide(dsigma_0, dsigma_1, out=np.zeros_like(dsigma_0), where=dsigma_1 != 0)

        return ratio.flatten()

    def decision_function_truth(self, events, c, features, process, order=None):
        """
        Computes the analytic decision function

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
        decision_function: numpy.ndarray
            Truth decision function
        """
        ratio = self.likelihood_ratio_truth(events, c, features, process, order)
        decision_function = 1 / (1 + ratio)
        return decision_function

    @staticmethod
    def plot_heatmap(ax, data, xlabel, ylabel, title, extent, bounds, cmap='GnBu', rep=None, text=None):
        """
        Plot and return a heatmap of ``data``

        Parameters
        ----------
        data: numpy.ndarray, shape=(M, N)
            Input array
        xlabel: str
            x-label
        ylabel: str
            y-label
        title: str
            title of plot
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

        import matplotlib.ticker as tick

        # discrete colorbar
        cmap_copy = copy.copy(mpl.cm.get_cmap(cmap))
        norm = mpl.colors.BoundaryNorm(bounds, cmap_copy.N, extend='both')
        cmap_copy.set_bad(color='gainsboro')

        if rep is not None:
            fig = ax.figure
            rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 30})
        else:
            fig = plt.figure(figsize=(10, 8))

        im = ax.imshow(data, extent=extent, origin='lower',
                       aspect=(extent[1] - extent[0]) / (extent[3] - extent[2]) * 10 / 8, cmap=cmap_copy, norm=norm)

        if rep is not None:
            ax.text(0.95, 0.95, r"$\mathrm{{rep}}\;{}$".format(rep), horizontalalignment='right',
                    verticalalignment='top',
                    transform=ax.transAxes)
        else:

            cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_copy), ax=ax,
                                format=tick.FormatStrFormatter(r'$%.2f$'))
            ax.set_title(title, fontsize=15)
            if text is not None:
                ax.text(0.95, 0.05, text, horizontalalignment='right', verticalalignment='center',
                        transform=ax.transAxes)
            plt.tight_layout()

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        return im
