import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import torch
import os
import json

from ..core.classifier import PredictorCross, Classifier, PredictorQuadratic
from ..preproc import constants
from ..analyse import analyse
from ..core.truth import vh_prod
from ..core.th_predictions import TheoryPred

mz = constants.mz
mh = constants.mh


class Limits:

    def __init__(self, luminosity, bins, kinematic, scan_domain, coeffs, path_to_models, event_path, mc_reps, data_sm, plot_path, architecture, row,
                 lin=False, quad=False, plot_reps=False, save=False, save_path=None, nn=True, truth=True, binned=True):

        self.luminosity = luminosity
        self.bins = bins
        self.kinematic = kinematic
        self.scan_domain = scan_domain
        self.path_to_models = path_to_models
        self.mc_reps = mc_reps
        self.data_sm = data_sm
        self.lin = lin
        self.quad = quad
        self.plot_path = plot_path
        self.architecture = architecture
        self.row = row

        self.coeffs = coeffs
        self.event_path = event_path

        self.q_c_truth = None
        self.q_c_nn = None
        self.q_c_nn_median = None
        self.log_likelihood_binned = None

        self.events_mvh = None
        self.events_mvh_y = None


        self.nn = nn
        self.truth = truth
        self.binned = binned


        self.limit_setting(plot_reps, save=save, save_path=save_path)

    def limit_setting(self, plot_reps=False, save=False, save_path=None):

        np.random.seed(0)

        # TODO: generalise to quad
        path_to_runcard = os.path.join(self.path_to_models['lin'][0].format(mc_run=0), 'run_card.json')
        with open(path_to_runcard) as json_data:
            self.run_card = json.load(json_data)
        features = self.run_card['features']

        theory_pred = TheoryPred(self.coeffs, self.bins, self.kinematic, self.event_path, nreps=self.mc_reps)
        theory_pred_total = theory_pred.df.sum(axis=1)

        # find expected number of events under the sm
        xsec_sm = theory_pred_total['sm']
        nu_tot_sm = xsec_sm * self.luminosity
        n_tot_sm = np.random.poisson(nu_tot_sm, 1)

        # draw a subset of events with size following a Poisson distribution with mean nu_tot
        self.data_sm['log_pt_z'] = np.log(self.data_sm['pt_z'])
        self.events = self.data_sm.sample(int(n_tot_sm), random_state=1)[features]

        # compute limits
        if self.binned:
            self.log_likelihood_binned = self.binned_limits(theory_pred)
        if self.truth or self.nn:
            self.q_c_truth, self.q_c_nn, self.q_c_nn_median = self.unbinned_limits(theory_pred)

        if save and save_path is not None:
            if self.nn:
                np.save(os.path.join(save_path, 'q_c_nn_median_row_{}.npy'.format(self.row)), self.q_c_nn_median)
                np.save(os.path.join(save_path, 'q_c_nn_row_{}.npy'.format(self.row)), self.q_c_nn)
            if self.truth:
                np.save(os.path.join(save_path, 'q_c_truth_row_{}.npy'.format(self.row)), self.q_c_truth)
            if self.binned:
                np.save(os.path.join(save_path, 'q_c_binned_row_{}.npy'.format(self.row)), self.log_likelihood_binned)


    def unbinned_limits(self, theory_pred):

        c1_values, c2_values = self.scan_domain

        theory_pred_total = theory_pred.df.sum(axis=1)

        likelihood_scan_truth = []
        likelihood_scan_nn = []
        likelihood_scan_nn_med = []

        # perform a likelihood scan over domain
        q_c_array_truth = None
        q_c_array_nn = None
        q_c_array_nn_median = None

        for c1 in c1_values:
            for c2 in c2_values:

                # inclusive info
                # TODO: automatise the keys
                #xsec = theory_pred_total['sm'] + c1 * theory_pred_total['cHW'] + c2 * theory_pred_total['cHq3']
                sigma = theory_pred_total['sm'] + c1 * theory_pred_total[self.coeffs[0]] + c2 * theory_pred_total[self.coeffs[1]]
                nu = sigma * self.luminosity

                # differential info
                if self.truth:

                    # 2 features
                    # dsigma_dx = np.array([vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], c1, c2, lin=self.lin, quad=self.quad) for index, row in self.events.iterrows()])

                    # 3 features
                    dsigma_dx = np.array(
                        [vh_prod.dsigma_dmvh_dy_dpt(row['y'], row['m_zh'], row['pt_z'], c1, c2, lin=self.lin, quad=self.quad) for
                         index, row in self.events.iterrows()])

                    # dsigma_dx = np.array(
                    #     [vh_prod.dsigma_dmvh_dy(self.events.loc[i, "y"], self.events.loc[i, "m_zh"], c1, c2, lin=self.lin, quad=self.quad) for i in range(len(self.events))]

                    # perhaps useful for speed up:
                    # likelihood = -nu + events_mvh_y.shape[0] * np.sum(np.log(dsigma_dx))

                    # TODO: what to do if xsec < 0 at large enough values of c?
                    if np.isnan(np.log(dsigma_dx)).any():
                        likelihood_scan_truth.append(np.nan)
                    else:
                        likelihood_truth = -nu + np.sum(np.log(dsigma_dx))
                        likelihood_scan_truth.append(likelihood_truth)

                if self.nn:

                    r_nn = analyse.likelihood_ratio_nn(torch.tensor(self.events.values.reshape(-1, self.architecture[0])), [c1, c2],
                                                       self.path_to_models, self.architecture, lin=self.lin,
                                                       quad=self.quad, mc_reps=self.mc_reps)
                    log_r_nn = np.log(r_nn)
                    likelihood_scan_nn.append(-nu + np.sum(log_r_nn, axis=1))


        if self.truth:
            likelihood_scan_truth = np.array(likelihood_scan_truth, dtype='object')
            likelihood_scan_truth = np.reshape(likelihood_scan_truth, (len(c1_values), len(c2_values)))
            #q_c_array_truth = 2 * (- likelihood_scan_truth + np.max(likelihood_scan_truth))

        if self.nn:
            likelihood_scan_nn = np.array(likelihood_scan_nn, dtype='object')
            likelihood_scan_nn = np.reshape(likelihood_scan_nn, (len(c1_values), len(c2_values), r_nn.shape[0]))
            likelihood_scan_nn_med = np.median(likelihood_scan_nn, axis=2)
            #q_c_array_nn = 2 * (- likelihood_scan_nn + np.max(likelihood_scan_nn, axis=(0, 1)))
            # q_c_array_nn_median = 2 * (
            #         - np.median(likelihood_scan_nn, axis=2) + np.max(np.median(likelihood_scan_nn, axis=2),
            #                                                          axis=(0, 1)))
        return likelihood_scan_truth, likelihood_scan_nn, likelihood_scan_nn_med


    def binned_limits(self, theory_pred):

        c1_values, c2_values = self.scan_domain
        #log_likelihood_binned = np.zeros(len(self.bins), dtype=np.ndarray)

        n_i, _ = np.histogram(self.events[self.kinematic].values, self.bins)

        log_likelihood = []
        for c1 in c1_values:
            for c2 in c2_values:
                # TODO: make more general
                #sigma_i = theory_pred.df.loc['sm'] + c1 * theory_pred.df.loc['cHW'] + c2 * theory_pred.df.loc['cHq3']
                sigma_i = theory_pred.df.loc['sm'] + c1 * theory_pred.df.loc[self.coeffs[0]] + c2 * theory_pred.df.loc[self.coeffs[1]]
                nu_i = sigma_i * self.luminosity
                log_l_i = n_i * np.log(nu_i.values) - nu_i.values

                log_l_i[np.isnan(log_l_i)] = 0
                log_likelihood.append(np.sum(log_l_i))

        log_likelihood = np.array(log_likelihood)
        log_likelihood = np.reshape(log_likelihood, (len(c1_values), len(c2_values)))
        return log_likelihood
        #log_likelihood_binned[i] = np.reshape(log_likelihood, (len(c1_values), len(c2_values)))

        # for i, n_bins in enumerate(self.bins):
        #
        #     if n_bins == 1:
        #         bins = np.array([mz + mh, 4.0])
        #     else:
        #         bins = np.linspace(mz + mh, 1.5, n_bins)
        #         bins = np.append(bins, 4.0)
        #
        #     kappa = vh_prod.findCoeff(bins)
        #
        #     n_i, _ = np.histogram(self.events_mvh, bins)
        #
        #     log_likelihood = []
        #     for c1 in c1_values:
        #         for c2 in c2_values:
        #             nu_i = vh_prod.nu_i(kappa, c1, c2, self.luminosity, lin=True)
        #             log_l_i = n_i * np.log(nu_i) - nu_i
        #
        #             log_l_i[np.isnan(log_l_i)] = 0
        #             log_likelihood.append(np.sum(log_l_i))
        #
        #     log_likelihood = np.array(log_likelihood)
        #     log_likelihood_binned[i] = np.reshape(log_likelihood, (len(c1_values), len(c2_values)))
        #
        #return log_likelihood_binned

    def plot_contours(self, plot_reps=False):

        c1_values, c2_values = self.scan_domain
        xx, yy = np.meshgrid(c1_values, c2_values, indexing='ij')
        fig = plt.figure(figsize=(12, 10))

        x_min = []
        x_max = []
        y_min = []
        y_max = []

        color = iter(cm.tab20c(np.linspace(0, 1, len(self.bins))))
        labels = []
        contours = []

        # binned contour
        for i, log_likelihood in enumerate(self.log_likelihood_binned):
            c = next(color)
            contour = plt.contour(yy, xx, log_likelihood, np.array([np.max(log_likelihood) - 5.99]),
                                  origin='lower', linestyles='dashed', linewidths=1.0, colors=[c])

            contour_handle, _ = contour.legend_elements()
            contours.append(contour_handle[0])
            labels.append(r'$\rm{%d\;bins}$' % self.bins[i])

            min_idx_0 = np.argmax(log_likelihood) // log_likelihood.shape[1]  # axis 0
            min_idx_1 = np.argmax(log_likelihood) % log_likelihood.shape[1]  # axis 1

            plt.scatter(c2_values[min_idx_1], c1_values[min_idx_0], marker='x', color=[c])

            contour_line = contour.allsegs[0][0]
            c2_min, c1_min = np.min(contour_line, axis=0)
            c2_max, c1_max = np.max(contour_line, axis=0)

            delta_c2 = c2_max - c2_min
            delta_c1 = c1_max - c1_min

            x_min.append(max(c2_min - 0.1 * delta_c2, np.min(c2_values)))
            x_max.append(min(c2_max + 0.1 * delta_c2, np.max(c2_values)))

            y_min.append(max(c1_min - 0.1 * delta_c1, np.min(c1_values)))
            y_max.append(min(c1_max + 0.1 * delta_c1, np.max(c1_values)))

        # unbinned contours

        # individual replica ellipses
        color = iter(cm.tab20c(np.linspace(0, 1, self.mc_reps)))
        if plot_reps:
            for rep in range(self.mc_reps):
                c = next(color)
                contour_nn = plt.contour(yy, xx, self.q_c_nn[:, :, rep], np.array([5.99]),
                                         origin='lower', linestyles='solid', linewidths=0.5, colors=[c])
                contour_handle, _ = contour_nn.legend_elements()
                contours.append(contour_handle[0])
                #labels.append('rep {}'.format(rep))

        # median model ellipse
        contour_nn_med = plt.contour(yy, xx, self.q_c_nn_median, np.array([5.99]),
                                     origin='lower', linestyles='solid', linewidths=1.5, colors='blue')

        contour_handle, _ = contour_nn_med.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$\rm{NN\;\rm{(median)}}$')

        # truth ellipse
        contour = plt.contour(yy, xx, self.q_c_truth, np.array([5.99]),
                              origin='lower', linestyles='dashed', linewidths=1.5, colors='k')

        contour_handle, _ = contour.legend_elements()
        contours.append(contour_handle[0])
        labels.append(r'$\rm{Unbinned\;\rm{(truth)}}$')

        plt.title(r'$95\%\rm{\;CL\;intervals}$')
        plt.xlabel(r'$\rm{cHq3}$')
        plt.ylabel(r'$\rm{cHW}$')
        plt.scatter(0, 0, marker='+', label='SM', color='k')

        plt.legend(contours, labels, fontsize=15, frameon=False, loc='best')

        plt.xlim(min(x_min), max(x_max))
        plt.ylim(min(y_min), max(y_max))
        plt.tight_layout()

        return fig