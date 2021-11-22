# same pseudo-dataset in all binnings
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import torch
import os

from ..core.classifier import PredictorCross, PredictorLinear, PredictorQuadratic
from ..preproc import constants
from ..analyse import analyse
from ..core.truth import vh_prod

mz = constants.mz
mh = constants.mh

#%%


# def get_nn_ratio(x, c1, c2, mc_run):
#     path_nn_lin_1 = os.path.join(path_lin_1, 'mc_run_{}', 'trained_nn.pt')
#     path_nn_lin_2 = os.path.join(path_lin_2, 'mc_run_{}', 'trained_nn.pt')
#     # path_nn_quad_1 = os.path.join(path_quad_1, 'mc_run_{}', 'trained_nn.pt')
#     # path_nn_quad_2 = os.path.join(path_quad_2, 'mc_run_{}', 'trained_nn.pt')
#     # path_nn_cross = os.path.join(path_cross, 'mc_run_{}', 'trained_nn.pt')
#
#
#     n_lin_1 = PredictorLinear(architecture)
#     n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))
#
#     mean, std = np.loadtxt(os.path.join(path_lin_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
#
#     x_scaled = (x - mean) / std
#     n_lin_1_out = n_lin_1.n_alpha(x_scaled.float())
#
#     n_lin_1 = PredictorLinear(architecture)
#     n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))
#
#
#
#     #######
#
#     n_lin_2 = PredictorLinear(architecture)
#     n_lin_2.load_state_dict(torch.load(path_nn_lin_2.format(mc_run)))
#
#     mean, std = np.loadtxt(os.path.join(path_lin_2, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
#     x_scaled = (x - mean) / std
#     n_lin_2_out = n_lin_2.n_alpha(x_scaled.float())
#
#
#
#
#     ########
#
#     # n_quad_1 = PredictorQuadratic(architecture)
#     # n_quad_1.load_state_dict(torch.load(path_nn_quad_1.format(mc_run)))
#     #
#     # mean, std = np.loadtxt(os.path.join(path_quad_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
#     # x_scaled = (x - mean) / std
#     # n_quad_1_out = n_quad_1.n_beta(x_scaled.float()) ** 2
#     #
#     # #######
#     #
#     # n_quad_2 = PredictorQuadratic(architecture)
#     # n_quad_2.load_state_dict(torch.load(path_nn_quad_2.format(mc_run)))
#     #
#     # mean, std = np.loadtxt(os.path.join(path_quad_2, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
#     # x_scaled = (x - mean) / std
#     # n_quad_2_out = n_quad_2.n_beta(x_scaled.float()) ** 2
#     #
#     # #######
#     #
#     # n_cross = PredictorCross(architecture)
#     # n_cross.load_state_dict(torch.load(path_nn_cross.format(mc_run)))
#     #
#     # mean, std = np.loadtxt(os.path.join(path_cross, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
#     # x_scaled = (x - mean) / std
#     # n_cross_out = n_cross.n_gamma(x_scaled.float()) ** 2
#
#     r = 1 + c1 * n_lin_1_out + c2 * n_lin_2_out #+ c1 ** 2 * n_quad_1_out + c2 ** 2 * n_quad_2_out + c1 * c2 * n_cross_out
#     #r[r<0] = 1
#     return r
class Limits:



    def __init__(self, luminosity, bins, scan_domain, mc_reps, data_sm, path_save, architecture,
                 lin=False, quad=False, plot_reps=False):

        self.luminosity = luminosity
        self.bins = bins
        self.scan_domain = scan_domain
        self.mc_reps = mc_reps
        self.data_sm = data_sm
        self.lin = lin
        self.quad = quad
        self.path_save = path_save
        self.architecture = architecture

        self.q_c_truth = None
        self.q_c_nn = None
        self.q_c_nn_median = None
        self.log_likelihood_binned = None

        self.events_mvh = None
        self.events_mvh_y = None

        self.limit_setting(plot_reps)

    def limit_setting(self, plot_reps=False):

        # find expected number of events under the sm
        a_sm = vh_prod.findCoeff(np.array([mz + mh, 4]))
        nu_tot_sm = vh_prod.nu_i(a_sm, 0, 0, self.luminosity, lin=True, quad=False)
        n_tot_sm = np.random.poisson(nu_tot_sm, 1)

        # draw a subset of events with size following a Poisson distribution with mean nu_tot
        events_idx = np.random.choice(np.arange(0, len(self.data_sm)), int(nu_tot_sm), replace=False)
        self.events_mvh = self.data_sm[events_idx, 0]
        self.events_mvh_y = self.data_sm[events_idx, :]

        # compute limits
        self.log_likelihood_binned = self.binned_limits()
        self.q_c_truth, self.q_c_nn, self.q_c_nn_median = self.unbinned_limits()

        fig = self.plot_contours(plot_reps)
        fig.savefig(self.path_save)

    def unbinned_limits(self):

        c1_values, c2_values = self.scan_domain

        likelihood_scan_truth = []
        likelihood_scan_nn = []
        a = vh_prod.findCoeff(bins=np.array([mz + mh, 4]))

        color = iter(cm.tab20c(np.linspace(0, 1, mc_reps)))

        # perform a likelihood scan over domain
        for c1 in c1_values:
            for c2 in c2_values:

                # inclusive info
                nu = vh_prod.nu_i(a, c1, c2, self.luminosity, lin=self.lin, quad=self.quad)

                # differential info
                dsigma_dx = np.array(
                    [vh_prod.dsigma_dmvh_dy(y, mvh, c1, c2, lin=self.lin, quad=self.quad) for (mvh, y) in self.events_mvh_y])

                # perhaps useful for speed up:
                # likelihood = -nu + events_mvh_y.shape[0] * np.sum(np.log(dsigma_dx))

                # TODO: what to do if xsec < 0 at large enough values of c?
                if np.isnan(np.log(dsigma_dx)).any():
                    likelihood_scan_truth.append(np.nan)
                else:
                    likelihood_truth = -nu + np.sum(np.log(dsigma_dx))
                    likelihood_scan_truth.append(likelihood_truth)

                log_l_nn_reps = []
                for rep in range(mc_reps):


                    r_nn = analyse.likelihood_ratio_nn(torch.tensor(events_mvh_y), [c1, c2], path_to_models, self.architecture,
                                                    mc_run=rep, lin=self.lin, quad=self.quad).numpy().flatten()

                    #r_nn = get_nn_ratio(torch.tensor(events_mvh_y), c1, c2, rep).detach().numpy()
                    log_r = np.log(r_nn)

                    # TODO: what to do if xsec < 0 at large enough values of c?
                    if np.isnan(log_r).any():
                        log_l_nn_reps.append(np.nan)
                    else:
                        log_l_nn_reps.append(-nu + np.sum(log_r))
                likelihood_scan_nn.append(log_l_nn_reps)

        likelihood_scan_truth = np.array(likelihood_scan_truth, dtype='object')
        likelihood_scan_truth = np.reshape(likelihood_scan_truth, (len(c1_values), len(c2_values)))

        likelihood_scan_nn = np.array(likelihood_scan_nn, dtype='object')
        likelihood_scan_nn = np.reshape(likelihood_scan_nn, (len(c1_values), len(c2_values), mc_reps))

        q_c_array_truth = 2 * (- likelihood_scan_truth + np.max(likelihood_scan_truth))
        q_c_array_nn = 2 * (- likelihood_scan_nn + np.max(likelihood_scan_nn, axis=(0, 1)))
        q_c_array_nn_median = 2 * (
                - np.median(likelihood_scan_nn, axis=2) + np.max(np.median(likelihood_scan_nn, axis=2), axis=(0, 1)))

        return q_c_array_truth, q_c_array_nn, q_c_array_nn_median

    def binned_limits(self):

        c1_values, c2_values = self.scan_domain
        log_likelihood_binned = np.zeros(len(self.bins))

        for i, n_bins in enumerate(self.bins):

            if n_bins == 1:
                bins = np.array([mz + mh, 4.0])
            else:
                bins = np.linspace(mz + mh, 1.5, n_bins)
                bins = np.append(bins, 4.0)

            kappa = vh_prod.findCoeff(bins)

            n_i, _ = np.histogram(self.events_mvh, bins)

            log_likelihood = []
            for c1 in c1_values:
                for c2 in c2_values:
                    nu_i = vh_prod.nu_i(kappa, c1, c2, self.luminosity, lin=True)
                    log_l_i = n_i * np.log(nu_i) - nu_i

                    log_l_i[np.isnan(log_l_i)] = 0
                    log_likelihood.append(np.sum(log_l_i))

            log_likelihood = np.array(log_likelihood)
            log_likelihood_binned[i] = np.reshape(log_likelihood, (len(c1_values), len(c2_values)))

        return log_likelihood_binned

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
        contour = plt.contour(yy, xx, self.q_c, np.array([5.99]),
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

    # TODO: include gaussian binned limits
    # @staticmethod
    # def chi2_function(data, theory, error):
    #     return np.sum(((data - theory) / error) ** 2)

