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
from matplotlib.ticker import NullFormatter
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
# TODO: update to 50 for heatmap overview plot
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


class Analyse:

    def __init__(self, path_to_models):

        self.path_to_models = path_to_models
        self.model_df = None
        self.coeff_truth = None

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

    def load_models(self, c_train, model_path, order, rep=None, epoch=-1):
        """

        Parameters
        ----------
        c_train: float
            EFT value used during training
        model_path: str
            path to model directory
        order: str
            Specifies the order in the EFT expansion. Must be one of ``lin``, ``quad`` or ``cross``.
        reps: int, optional
            Number of specific replicas to include
        epoch: int, optional
            Epoch number to load. Set to the best model by default.

        Returns
        -------

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

        return models, models_rep_nr, scalers, run_card, rep_paths

    def build_model_dict(self, rep=None, epoch=-1):
        """
        Construct a model dictionary that stores all the info about the models

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
            for c_name, [c_train, model_path] in dict_fo.items():
                pretrained_models, models_idx, scalers, run_card, rep_paths = self.load_models(c_train, model_path, order, rep, epoch)
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

        Returns
        -------
        models_evaluated:dict
            Evaluated model dictionary
        """

        # load models if not done already
        if rep is not None:
            self.build_model_dict(rep, epoch)
        if self.model_df is None:
            self.build_model_dict(rep, epoch)


        models_evaluated = copy.deepcopy(self.model_dict)

        # models = models_evaluated.loc[:]['models'].values
        # scalers = models_evaluated.loc[:]['scalers'].values
        # feature_names = models_evaluated.loc[:]['run_card'].values[0]['features']
        # features_scaled =

        for order, dict_fo in self.model_dict.items():
            for c_name, dict_c in dict_fo.items():
                models = dict_c['models']

                for i, model in enumerate(models):
                    features = dict_c['run_card']['features']
                    features_scaled = dict_c['scalers'][i].transform(df[features])
                    with torch.no_grad():
                        model_ev = model.n_alpha(torch.tensor(features_scaled).float()).numpy().flatten()
                    models_evaluated[order][c_name]['models'][i] = model_ev

        models_evaluated_df = pd.DataFrame.from_dict({(i, j): models_evaluated[i][j]
                                                for i in models_evaluated.keys()
                                                for j in models_evaluated[i].keys()},
                                               orient='index')
        return models_evaluated_df

    def coeff_function_truth(self, df, c_name, features, process, order):

        # create c dict

        c = {}
        for k, v in self.path_to_models[order].items():
            c[k] = v[0] if k == c_name else 0

        ratio_truth_lin = self.likelihood_ratio_truth(df, c, features, process, order)
        # compute the mask once to select the physical region in phase space
        mask = ratio_truth_lin == 0

        coeff_lin = np.ma.masked_where(mask, (ratio_truth_lin - 1) / c[c_name])
        if order == 'lin':  # only one of the c elements can be nonzero
            return coeff_lin
        # elif order == 'quad':  # only one of the c elements can be nonzero
        #     ratio_truth_quad = likelihood_ratio_truth(x, c, quad=True)
        #     # TODO: rewrite the below
        #     coeff_quad = np.ma.masked_where(mask, (ratio_truth_quad - 1 - np.sum(c) * coeff_lin) / np.sum(c) ** 2)
        #     return coeff_quad
        # elif order == 'cross':
        #     ratio_truth_quad = likelihood_ratio_truth(x, c, quad=True)
        #     ratio_truth_quad_1 = likelihood_ratio_truth(x, np.array([c1, 0]), quad=True)
        #     ratio_truth_quad_2 = likelihood_ratio_truth(x, np.array([0, c2]), quad=True)
        #     coeff_cross = np.ma.masked_where(mask,
        #                                      (ratio_truth_quad - ratio_truth_quad_1 - ratio_truth_quad_2 + 1) / np.prod(
        #                                          c))
        #     return coeff_cross

    def accuracy_heatmap(self, c_name, order, process, cut=None, rep=None, epoch=-1, ax=None):
        """
        Compares the NN and true coefficient functions in the EFT expansion and plots their ratio and pull

        Parameters
        ----------

        Returns
        -------
        `matplotlib.figure.Figure`
            Heatmap of coefficient function ratio
        `matplotlib.figure.Figure`
            Heatmap of pull
        """
        s = constants.col_s ** 2
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
            df = pd.DataFrame({'y': grid[:, 1], 'm_zh': grid[:, 0]})
        elif process == 'tt':
            df = pd.DataFrame({'y': grid[:, 1], 'm_tt': grid[:, 0]})

        # models

        models_evaluated_df = self.evaluate_models(df, rep, epoch)
        nn = models_evaluated_df.loc[order, c_name]['models']
        nn = np.vstack(nn)
        n_models = nn.shape[0]

        nn = nn.reshape((n_models, *mx_grid.shape))

        # truth

        features = df.columns.values

        if self.coeff_truth is None:
            self.coeff_truth = self.coeff_function_truth(df, c_name, features, process, order).reshape(
                mx_grid.shape)

        # TODO: add option to overlay events as points on the heatmap

        xlabel = r'$m_{ZH}\;\rm{[TeV]}$' if process == 'ZH' else r'$m_{t\bar{t}}\;\rm{[TeV]}$'
        if rep is None:

            # determine median, low and high CI

            nn_median = np.percentile(nn, 50, axis=0)
            nn_high = np.percentile(nn, 84, axis=0)
            nn_low = np.percentile(nn, 16, axis=0)
            nn_unc = (nn_high - nn_low) / 2
            # median
            median_ratio = self.coeff_truth / nn_median
            title = r'$\rm{Truth/NN\;(median)}$'

            fig_1, ax_1 = plt.subplots(figsize=(10, 8))

            im_1 = self.plot_heatmap(ax_1, median_ratio,
                                xlabel=xlabel,
                                ylabel=r'$\rm{Rapidity}$',
                                title=title,
                                extent=[mx_min, mx_max, y_min, y_max],
                                cmap='seismic',
                                bounds=[0.95, 0.96, 0.97, 0.98, 1.02, 1.03, 1.04, 1.05])

            # pull

            fig_2, ax_2 = plt.subplots(figsize=(10, 8))

            pull = (self.coeff_truth - nn_median) / nn_unc

            im_2 = self.plot_heatmap(ax_2, pull,
                                xlabel=xlabel,
                                ylabel=r'$\rm{Rapidity}$',
                                title=r'$\rm{Pull}$',
                                extent=[mx_min, mx_max, y_min, y_max],
                                cmap='seismic',
                                bounds=np.linspace(-1.5, 1.5, 10))

            return fig_1, fig_2
        else:
            title = r"$\mathrm{{Truth/NN}}\;(\mathrm{{rep}}\;{})$".format(rep)
            im = self.plot_heatmap(ax, self.coeff_truth / nn[0],
                              xlabel=xlabel,
                              ylabel=r'$\rm{Rapidity}$',
                              title=title,
                              extent=[mx_min, mx_max, y_min, y_max],
                              cmap='seismic',
                              bounds=[0.95, 0.96, 0.97, 0.98, 1.02, 1.03, 1.04, 1.05],
                              rep=rep)
            return im

    def plot_heatmap_overview(self, c_name, order, process, cut=None, reps=None, epoch=-1):

        from mpl_toolkits.axes_grid1 import AxesGrid

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
            im = self.accuracy_heatmap(c_name, order, process, cut, rep, epoch, grid[i])

        grid[-1].cax.colorbar(im)
        grid.cbar_axes[0].colorbar(im)

        return fig

    def likelihood_ratio_nn(self, df, c, epoch=-1):
        """
           Computes NN likelihood ratio

           Parameters
           ----------
           df: pd.DataFrame
               event info
           c: numpy.ndarray
               EFT point

           Returns
           -------
           ratio: numpy.ndarray
               NN likelihood ratio
           """

        models_evaluated = self.evaluate_models(df, epoch=epoch)

        ratio = 1

        if 'lin' in models_evaluated.index:
            lin_models = models_evaluated['models'].loc["lin"]
            for c_name, nn_lin in lin_models.iteritems():
                ratio += c[c_name] * nn_lin

        if 'quad' in models_evaluated.index:
            quad_models = models_evaluated['models'].loc["quad"]
            for i, (_, nn_quad) in enumerate(quad_models.iteritems()):
                ratio += c[i] ** 2 * nn_quad

        ratio = np.vstack(ratio)

        return ratio

    def decision_function_nn(self, df, c, epoch=-1):
        """
        Computes NN decision function

        Parameters
        ----------
        df: pd.DataFrame
            event info
        c: numpy.ndarray
            EFT point

        Returns
        -------
        decision_function: numpy.ndarray
            NN decision function
        """
        ratio = self.likelihood_ratio_nn(df, c, epoch=epoch)
        decision_function = 1 / (1 + ratio)
        return decision_function

    def point_by_point_comp(self, df, c, features, process):

        r_nn = self.likelihood_ratio_nn(df, c)
        tau_nn = np.log(r_nn)

        order = self.model_df.index[-1][0]  # last index, first column gives the order

        r_truth = self.likelihood_ratio_truth(df, c, features, process, order)
        tau_truth = np.log(r_truth)

        # overview plot for all replicas
        ncols = 5
        mc_reps = r_nn.shape[0]
        nrows = int(np.ceil(mc_reps / ncols))

        fig1 = plt.figure(figsize=(ncols * 4, nrows * 4))

        x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)

        for k, v in c.items():
            if v != 0:
                model_idx = self.model_df.loc[order, k]['idx']

        for i in np.argsort(model_idx):
            ax = plt.subplot(nrows, ncols, model_idx[i] + 1)

            # plt.scatter(tau_truth[mask_comp], tau_nn[i, mask_comp], s=2, color='k')
            # plt.scatter(tau_truth[mask], tau_nn[i, mask], s=2, color='red')

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

        # plt.scatter(tau_truth[mask_comp], np.median(tau_nn, axis=0)[mask_comp], s=5, color='k')
        # plt.scatter(tau_truth[mask], np.median(tau_nn, axis=0)[mask], s=5, color='red')

        plt.scatter(tau_truth, np.median(tau_nn, axis=0), s=2, color='k')
        plt.plot(x, x, linestyle='dashed', color='grey')
        plt.xlabel(r'$\tau(x, c)^{\rm{truth}}$')
        plt.ylabel(r'$\tau(x, c)^{\rm{NN}}$')
        plt.xlim((np.min(x), np.max(x)))
        plt.ylim((np.min(x), np.max(x)))
        plt.tight_layout()

        return fig1, fig2

    def plot_loss_overview(self):

        if self.model_df is None:
            self.build_model_dict()

        loss_tr = []
        loss_val = []
        figs = []
        for (order, c_name), rep_paths in self.model_df['rep_paths'].iteritems():

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

            for i in np.argsort(model_idx):
                ax = plt.subplot(nrows, ncols, model_idx[i] + 1)
                epochs = np.arange(len(loss_tr[i]))

                label_val = r'$L_{\mathrm{val}}$' if i == 0 else None
                label_train = r'$L_{\mathrm{tr}}$' if i == 0 else None

                loss_train_rep = np.array(loss_tr[i])
                loss_val_rep = np.array(loss_val[i])

                ax.plot(epochs, loss_train_rep, label=label_train)
                ax.plot(epochs, loss_val_rep, label=label_val)
                ax.axvline(epochs[-patience], 0, 0.75, color='red', linestyle='dotted')

                # ax.set_yscale('log')
                # ax.yaxis.set_major_formatter(NullFormatter())
                # ax.yaxis.set_minor_formatter(NullFormatter())
                # ax.axes.yaxis.set_ticklabels([])
                ax.set_ymargin(0.1)
                ax.set_xmargin(0)

                ax.text(0.9, 0.9, r"$\mathrm{{rep}}\;{}$".format(model_idx[i]), horizontalalignment='right',
                        verticalalignment='center',
                        transform=ax.transAxes)

                ax.set_xlim(left=10)

                med_loss = np.percentile(train_loss_best, 50)
                low_loss = np.percentile(train_loss_best, 16)
                high_loss = np.percentile(train_loss_best, 84)
                loss_sigma = np.abs((high_loss - low_loss) / 2)

                ax.set_ylim(loss_train_rep[-1] - 0.2 * loss_sigma, loss_train_rep[-1] + 0.8 * loss_sigma)

                signif = (train_loss_best[i] - med_loss) / loss_sigma

                ax.text(0.9, 0.8, r"$Z={:.2f}$".format(signif), horizontalalignment='right',
                        verticalalignment='center',
                        transform=ax.transAxes)

                if i == 0:
                    ax.legend(loc="lower left", frameon=False)

            plt.tight_layout()
            figs.append(fig)

        return figs

    def plot_accuracy_1d(self, c, process, order, cut, epoch=-1):

        fig, ax = plt.subplots(figsize=(10, 6))

        x = np.linspace(cut, 3.0, 200)
        x = np.stack((np.zeros(len(x)), x), axis=-1)

        if process == 'tt':
            df = pd.DataFrame(x, columns=['y', 'm_tt'])
        elif process == 'ZH':
            df = pd.DataFrame(x, columns=['y', 'm_zh'])

        f_ana_lin = self.decision_function_truth(df, c, df.columns.values, process, order)

        f_preds_nn = self.decision_function_nn(df, c, epoch=epoch)

        f_pred_up = np.percentile(f_preds_nn, 84, axis=0)
        f_pred_down = np.percentile(f_preds_nn, 16, axis=0)

        ax.fill_between(x[:, 1], f_pred_down, f_pred_up, label=r'$\rm{NN}\;\mathcal{O}\left(\Lambda^{-2}\right)$',
                        alpha=0.4)

        ax.plot(x[:, 1], f_ana_lin, '--', c='red', label=r'$\rm{Truth}\;\mathcal{O}\left(\Lambda^{-2}\right)$')

        # single replica
        # ax.plot(x[:, 0], f_preds_nn[0,:], '--', c='blue', label=r'$\rm{NN}\;\mathcal{O}\left(\Lambda^{-2}\right)$')

        plt.ylim((0, 1))
        plt.xlim(np.min(x[:, 1]), np.max(x[:, 1]))

        plt.ylabel(r'$g\;(x, c)$')
        xlabel = r'$m_{ZH}\;\rm{[TeV]}$' if process == 'ZH' else r'$m_{t\bar{t}}\;\rm{[TeV]}$'
        plt.xlabel(xlabel)
        plt.legend()
        plt.tight_layout()
        return fig

    @staticmethod
    def likelihood_ratio_truth(events, c, features, process, order=None):
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
            c = np.array([c['ctgre'], c['cut']])
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
    def plot_heatmap(ax, data, xlabel, ylabel, title, extent, bounds, cmap='GnBu', rep=None):
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


        # discrete colorbar
        cmap_copy = copy.copy(mpl.cm.get_cmap(cmap))
        norm = mpl.colors.BoundaryNorm(bounds, cmap_copy.N, extend='both')
        cmap_copy.set_bad(color='gainsboro')

        # continuous colormap

        # cmap = copy.copy(plt.get_cmap(cmap))
        # cmap.set_bad(color='white')
        # cmap.set_over("#FFAF33")
        # cmap.set_under("#FFAF33")

        if rep is not None:
            fig = ax.figure
            rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 50})
        else:
            fig = plt.figure(figsize=(10,8))

        im = ax.imshow(data, extent=extent,
                  origin='lower', aspect=(extent[1] - extent[0]) / (extent[-1] - extent[-2]), cmap=cmap_copy, norm=norm)

        if rep is not None:
            ax.text(0.95, 0.95, r"$\mathrm{{rep}}\;{}$".format(rep), horizontalalignment='right',
                     verticalalignment='top',
                     transform=ax.transAxes)
        else:
            cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_copy), ax=ax)
            ax.set_title(title)
            plt.tight_layout()

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        return im


#TODO: coeff_function_nn can be replaced entirely by load_coefficients_nn
# def coeff_function_nn(x, path_to_model, architecture, lin=False, quad=False, cross=False, animate=False, epoch=None):
#     """
#     Computes the nn coefficient functions in the EFT expansion up to either linear or quadratic level
#
#     Parameters
#     ----------
#      x : torch.tensor, shape=(M, N)
#         Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
#         the invariant mass and the rapidity.
#     path_to_models: str
#         Path to the nn model directory, e.g. ./model_x/mc_run_0
#     architecture: list
#         The architecture of the model, e.g.
#
#             .. math::
#
#                 [n_i, 10, 15, 5, n_f],
#
#         where :math:`n_i` and :math:`n_f` denote the number of input features and output target values respectively.
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
#
#     """
#     with torch.no_grad():
#
#         if lin:
#             nn = quad_clas.PredictorLinear(architecture)
#         elif quad:
#             nn = quad_clas.PredictorQuadratic(architecture)
#         elif cross:
#             nn = quad_clas.PredictorCross(architecture)
#
#         if animate and epoch is not None:
#             path_nn = os.path.join(path_to_model, 'trained_nn_{epoch}.pt'.format(epoch=epoch))
#             if not os.path.exists(path_nn):
#                 path_nn = os.path.join(path_to_model, 'trained_nn.pt')
#         else:
#             path_nn = os.path.join(path_to_model, 'trained_nn.pt')
#         nn.load_state_dict(torch.load(path_nn))
#
#         scaler_path = os.path.join(path_to_model, 'scaler.gz')
#         scaler = joblib.load(scaler_path)
#         x_scaled = scaler.transform(x)
#         x_scaled = torch.tensor(x_scaled)
#
#         if lin:
#             n_lin_out = nn.n_alpha(x_scaled.float()).numpy().flatten()
#             return n_lin_out
#         elif quad:
#             n_quad_out = nn.n_beta(x_scaled.float()).numpy().flatten()
#             return n_quad_out
#         elif cross:
#             n_cross_out = nn.n_gamma(x_scaled.float()).numpy().flatten()
#             return n_cross_out

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

