import numpy as np
import os
import sys
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import pandas as pd
import csv
from scipy.ndimage.filters import gaussian_filter
from scipy.optimize import curve_fit
from ..core import bounds as bounds


class Analyse:
    """
    This python class object analyses the z-scores that originate from
    a scan over the EFT coefficient space. Results are presented for
    the neural network (nn), truth and binned analyses.

    The (expected) exclusion limits are found by interpolating on the
    z-scores and solving the resulting polynomial for the 95% CL.
    """

    def __init__(self, root_path, truth=True, nn=True, binnings=None, extent=None, fit=True, luminosity=6, mc_runs=100, nn_rep=40):
        """
        Parameters
        ----------
        root_path:
            path to root where the output should be stored
        truth: bool
            Includes the truth bounds
        nn: bool
            Includes the nn bounds
        binnings: list
            collection of binnings (array_like) for which to run the analysis
        extent: array_like, shape (n, 2)
            It gives the range of the EFT coefficients to scan.
        fit: bool
            This should be set to true for every new binning
        luminosity: float
            luminosity of the experiment in pb^-1
        mc_runs: int
            number of z-scores to load at each EFT point
        """

        self.root_path = root_path
        self.output_path = os.path.join(self.root_path, 'output')
        self.plots_path = os.path.join(self.output_path, 'plots')
        self.paths = {'root': self.root_path, 'output': self.output_path, 'plots': self.plots_path}

        self.truth = truth
        self.z_scores_truth = None

        self.nn = nn
        self.z_scores_nn = None

        self.luminosity = luminosity
        self.extent = extent

        self.mc_runs = mc_runs
        self.nn_rep = nn_rep

        if binnings is not None:

            self.binnings = binnings
            self.fit = fit

            # run a binned analysis on each of the binnings
            self.binned_analyses = self.run_binned_analysis()

            # plot accuracy of Asimov method
            #fig = bounds.plot_tc_accuracy(self.binned_analyses, c=np.array([0.5, 0]), n=100000)
            #fig.savefig(os.path.join(self.plots_path, 'tc_acc/asimov_comp.pdf'))
        else:
            self.binned_analyses = None

        # analyse the nn, truth and binned cases (if not None)
        self.combine_analyses()

    def run_binned_analysis(self):
        """
        Run a binned analysis

        Returns
        -------
        list
            binned analyses object for each of the binnings
        """

        binned_analyses = []

        for i, binning in enumerate(self.binnings):
            # output directory is different for each bin
            self.paths['output'] = os.path.join(self.output_path, 'binning_{}'.format(i))

            # create an analysis instance and perform the analysis
            analysis = bounds.StatAnalysis(self.paths, bins=binning, fit=self.fit, luminosity=self.luminosity)
            analysis.binned_analysis(extent=self.extent)

            # append results
            binned_analyses.append(analysis)

        return binned_analyses

    def read_z_scores(self, path):
        """
        Reads the z-scores

        Parameters
        ----------
        path: str
            location of the z-scores

        Returns
        -------
        list
            list of the z-scores
            shape = (self.mc_runs, self.nn_rep, n_eft_points, 3)
        """

        if 'nn' in path:
            z_scores = []  # shape = (self.mc_runs, self.nn_rep, n_eft_points, 3)
            for i in range(1, self.mc_runs + 1):
                z_scores_nn_rep = []  # shape = (self.nn_rep, n_eft_points, 3)

                for j in range(self.nn_rep):
                    loc = os.path.join(path, "mc_run_{}/rep_{}/z_scores.dat".format(i, j))
                    with open(loc, "r") as f:
                        reader = csv.reader(f, delimiter='\t')
                        z_scores_eft_point = []  # shape = (n_eft_points, 3)

                        for line in reader:
                            z_scores_eft_point.append([float(value) for value in line])
                        z_scores_nn_rep.append(z_scores_eft_point)

                z_scores.append(z_scores_nn_rep)

            z_scores = np.array(z_scores)
        else:
            z_scores = []
            for i in range(1, self.mc_runs + 1):
                loc = os.path.join(path, "mc_run_{}/z_scores.dat".format(i))
                with open(loc, "r") as f:
                    reader = csv.reader(f, delimiter='\t')
                    for line in reader:
                        z_scores.append([float(value) for value in line])
            z_scores = np.array(z_scores)

        return z_scores

    def load_z_scores(self):
        """
        Loads the z-scores for all the mc runs.

        Returns
        -------
        tuple
            Pandas dataframe for truth and nn
        """

        if self.nn:
            path = os.path.join(self.output_path, 'z_scores/nn_v3')
            z_scores = self.read_z_scores(path)
            z_scores_nn_df = []
            for rep in range(z_scores.shape[1]):
                # select a replica
                z_scores_rep = z_scores[:, rep, :, :]

                # average over the mc runs
                z_scores_rep_mc_avg = np.mean(z_scores_rep[:, :, -1], axis=0)
                z_scores_rep_mc_std = np.std(z_scores_rep[:, :, -1], axis=0)

                # build a pandas dataframe for each replica
                df = pd.DataFrame(np.array([z_scores_rep[:, :, 0][0], z_scores_rep[:, :, 1][0], z_scores_rep_mc_avg, z_scores_rep_mc_std]).T, columns=['cug', 'cuu', 'z-score', 'unc'])
                z_scores_nn_df.append(df)

        else:
            z_scores_nn_df = None

        if self.truth:
            path = os.path.join(self.output_path, 'z_scores/truth_v2')
            z_scores = self.read_z_scores(path)
            z_scores = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score'])
            z_scores_grouped = z_scores.groupby(['cug', 'cuu']).agg({'z-score': ['mean', self.stdom]})
            z_scores_grouped.columns = ['z-score', 'uncertainty']
            z_scores_grouped_truth = z_scores_grouped.reset_index()
        else:
            z_scores_grouped_truth = None

        return z_scores_grouped_truth, z_scores_nn_df

    def combine_analyses(self):
        """
        Finds the contours of the 95% CL.
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        cuu = np.linspace(self.extent[0, 0], self.extent[0, 1], 200)
        cug = np.linspace(self.extent[1, 0], self.extent[1, 1], 200)
        cuu_plane, cug_plane = np.meshgrid(cuu, cug)

        labels = []
        contours = []
        #colors = ['C2', 'C3', 'C4']
        if self.binned_analyses is not None:
            sigma = 0.8
            color = iter(cm.rainbow(np.linspace(0, 1, len(self.binned_analyses))))
            for i, binnings in enumerate(self.binned_analyses):
                # data_smoothed = gaussian_filter(binnings.z_scores_asi, sigma)
                c = next(color)
                data_smoothed = gaussian_filter(binnings.z_scores, sigma)
                contour = ax.contour(binnings.cuu_plane, binnings.cug_plane, data_smoothed, levels=np.array([1.64]), colors=[c])
                h0, _ = contour.legend_elements()
                contours.append(h0[0])
                labels.append(r'$\rm{%d\;bins}$' % (len(binnings.bins)-1))

        #self.z_scores_truth, self.z_scores_nn = self.load_z_scores()


        # uncomment conditions below to select z-scores of your choice
        #cond = ~((self.z_scores_nn['cug'] != 0.0) & (self.z_scores_nn['cuu'] != 0.0))
        #self.z_scores_nn = self.z_scores_nn[cond]
        #cond = ~((self.z_scores_nn['cug'] != 0.0) & (self.z_scores_nn['cuu'] != 0.0))
        #self.z_scores_nn = self.z_scores_nn[cond]
        #self.z_scores_truth = self.z_scores_truth[cond]

        # 1D analysis
        #self.analyse1d()

        # 2D analysis
        #ellipse_param_truth,  ellipse_param_nn = self.fit_ellipse()







        # if self.truth:
        #
        #
        #     cntr_truth = ax.contour(cuu_plane, cug_plane,
        #                             self.ellipse(cuu_plane, cug_plane, *ellipse_param_truth),
        #                             levels=[1.64],
        #                             colors='C0')
        #
        #     h0, _ = cntr_truth.legend_elements()
        #     contours.append(h0[0])
        #     labels.append(r'$\rm{Truth}$')
        #
        # if self.nn:
        #
        #     for ellipse_param_nn_rep in ellipse_param_nn:
        #         cntr_nn = ax.contour(cuu_plane, cug_plane,
        #                              self.ellipse(cuu_plane, cug_plane, *ellipse_param_nn_rep),
        #                              levels=[1.64],
        #                              colors='C1')
        #         h0, _ = cntr_nn.legend_elements()
        #
        #     contours.append(h0[0])
        #     labels.append(r'$\rm{NN}$')


        # plot settings
        ax.legend(contours, labels, fontsize=15, frameon=False, loc='best')
        ax.set_xlabel(r'$\rm{cHW}$', fontsize=20)
        ax.set_ylabel(r'$\rm{cHq3}$', fontsize=20)
        ax.set_title(r'$\rm{Expected\;exclusion\;limits}$', fontsize=20)

        fig.savefig('/Users/jaco/Documents/ML4EFT/code/output/zh_bin.pdf')
        #fig.savefig(os.path.join(self.plots_path, 'ellipses_diff_new_8.pdf'))

    def analyse1d(self):
        z_scores_truth = self.z_scores_truth
        z_scores_nn = self.z_scores_nn

        z_scores_nn_pcuu = z_scores_nn[(z_scores_nn['cug'] == 0) & (z_scores_nn['cuu'] > 0)]
        z_scores_nn_ncuu = z_scores_nn[(z_scores_nn['cug'] == 0) & (z_scores_nn['cuu'] < 0)]
        z_scores_nn_pcug = z_scores_nn[(z_scores_nn['cuu'] == 0) & (z_scores_nn['cug'] > 0)]
        z_scores_nn_ncug = z_scores_nn[(z_scores_nn['cuu'] == 0) & (z_scores_nn['cug'] < 0)]
        z_scores_nn_pdiag = z_scores_nn[(z_scores_nn['cuu'] > 0) & (z_scores_nn['cug'] > 0)]
        z_scores_nn_ndiag = z_scores_nn[(z_scores_nn['cuu'] < 0) & (z_scores_nn['cug'] < 0)]

        z_scores_truth_pcuu = z_scores_truth[(z_scores_truth['cug'] == 0) & (z_scores_truth['cuu'] > 0)]
        z_scores_truth_ncuu = z_scores_truth[(z_scores_truth['cug'] == 0) & (z_scores_truth['cuu'] < 0)]
        z_scores_truth_pcug = z_scores_truth[(z_scores_truth['cuu'] == 0) & (z_scores_truth['cug'] > 0)]
        z_scores_truth_ncug = z_scores_truth[(z_scores_truth['cuu'] == 0) & (z_scores_truth['cug'] < 0)]
        z_scores_truth_pdiag = z_scores_truth[(z_scores_truth['cuu'] > 0) & (z_scores_truth['cug'] > 0)]
        z_scores_truth_ndiag = z_scores_truth[(z_scores_truth['cuu'] < 0) & (z_scores_truth['cug'] < 0)]

        fig = self.interpolation(z_scores_truth_pcuu, z_scores_nn_pcuu)
        fig.savefig(os.path.join(self.plots_path, 'analysis1d_pcuu.pdf'))



    def fit_ellipse(self):
        """
        Fit an ellipse through the z-scores

        Returns
        -------
        tuple
            ellipse parameters for the truth and nn analysis
        """

        def poly2d(x, y, a, b, c, d):
            return a * x ** 2 + b * y ** 2 + c * x * y + d

        def _poly2d(M, a, b, c, d):
            x, y = M
            return poly2d(x, y, a, b, c, d)

        # solve the linear equation xsec = coeff_matrix * a for a
        if self.truth:
            cuu = self.z_scores_truth.cuu.values
            cug = self.z_scores_truth.cug.values

            eft_points = np.array([cuu, cug])
            Z = self.z_scores_truth['z-score'].values
            Z_unc = self.z_scores_truth['uncertainty'].values

            popt, pcov = curve_fit(_poly2d, eft_points, Z, sigma=Z_unc)
            perr = np.sqrt(np.diag(pcov))

            # eft_points = np.array([cuu, cug]).T
            #
            # z_score_truth = self.z_scores_truth['z-score'].values
            # z_score_unc_truth = self.z_scores_truth['uncertainty'].values
            #
            # coeff_mat = self.coefficient_matrix(eft_points)
            #
            # a_truth, _, _, _ = np.linalg.lstsq(coeff_mat, z_score_truth, rcond=None)
            a_truth, a_truth_error = popt, perr
        else:
            a_truth = None

        if self.nn:
            # fit an ellipse for each replica
            ellipse_param = []
            for rep in self.z_scores_nn:
                cuu = rep.cuu.values
                cug = rep.cug.values

                eft_points = np.array([cuu, cug])
                z_score = rep['z-score'].values
                z_score_unc = rep['unc'].values

                popt, pcov = curve_fit(_poly2d, eft_points, z_score, sigma=z_score_unc)
                perr = np.sqrt(np.diag(pcov))

                ellipse_param.append(popt)

            a_nn = ellipse_param
        else:
            a_nn = None

        return a_truth, a_nn

    def interpolation(self, z_scores_truth, z_scores_nn):

        fig, ax = plt.subplots(figsize=(10, 6))

        z_scores_nn = z_scores_nn.reset_index(drop=True)
        z_scores_truth = z_scores_truth.reset_index(drop=True)
        c = z_scores_nn.cuu.values if z_scores_nn.cuu.values[0] != 0 else z_scores_nn.cug.values

        z_score_nn = z_scores_nn['z-score'].values
        z_score_nn_unc = z_scores_nn['uncertainty'].values

        z_score_truth = z_scores_truth['z-score'].values
        z_score_truth_unc = z_scores_truth['uncertainty'].values

        ax.errorbar(c, z_score_nn, yerr=z_score_nn_unc, fmt='.', capsize=3,
                    color='C1', label=r'$\rm{z-score\;(NN)}$')

        ax.errorbar(c, z_score_truth, yerr=z_score_truth_unc, fmt='.', capsize=3,
                    color='C0', label=r'$\rm{z-score\;(truth)}$')

        popt_nn, _ = curve_fit(self.quad_pol, c, z_score_nn, sigma=z_score_nn_unc)
        popt_truth, _ = curve_fit(self.quad_pol, c, z_score_truth, sigma=z_score_truth_unc)

        epsilon = 0.1 * (np.max(c) - np.min(c))
        xmin = np.min(c) - epsilon
        xmax = np.max(c) + epsilon
        x = np.linspace(xmin, xmax, 400)

        plt.hlines(1.64, xmin, xmax, color='black', linestyle='dashed')
        # ax.plot(x, quad_pol(x, *popt_truth), color='C0', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(true)}$')
        ax.plot(x, self.quad_pol(x, *popt_truth), color='C0', linestyle='dotted')  # , label=r'$\rm{Exp\;fit\;(NN)}$')
        ax.plot(x, self.quad_pol(x, *popt_nn), color='C1', linestyle='dotted')  # , label=r'$\rm{Exp\;fit\;(NN)}$')

        idx_truth = np.argwhere(np.diff(np.sign(self.quad_pol(x, *popt_truth) - 1.64))).flatten()
        idx_nn = np.argwhere(np.diff(np.sign(self.quad_pol(x, *popt_nn) - 1.64))).flatten()

        plt.plot(x[idx_truth], self.quad_pol(x[idx_truth], *popt_truth), 'kx')
        plt.plot(x[idx_nn], self.quad_pol(x[idx_nn], *popt_nn), 'kx')

        ##### add binned curve
        z_scores_binned = []
        for c in x:
            self.binned_analyses[0].nu_i = self.binned_analyses[0].expected_entries(np.array([0, c]))
            self.binned_analyses[0].mean_tc_asi, self.binned_analyses[0].std_tc_asi = self.binned_analyses[0].find_pdf_binned_asimov()
            z_score_asi, _ = self.binned_analyses[0].p_value_asimov()
            z_scores_binned.append(z_score_asi)
        z_scores_binned = np.array(z_scores_binned)

        plt.plot(x, z_scores_binned, label=r'$\rm{z-score\;(binning\;0)}$', color='C2')

        # Plot settings
        ax.set_ylabel(r'$\rm{z-score}$', fontsize=20)
        ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
        ax.set_xlim((xmin, xmax))

        epsilon = 0.1 * (np.max(z_score_truth) - np.min(z_score_truth))
        ymin = np.min([z_score_truth.min() - epsilon, z_score_nn.min() - epsilon])
        ymax = np.max([z_score_truth.max() + epsilon, z_score_nn.max() + epsilon])

        ax.set_ylim((ymin, ymax))
        ax.legend(loc='best', fontsize=15, frameon=False)
        ax.tick_params(which='both', direction='in', labelsize=20)
        ax.tick_params(which='major', length=10)
        ax.tick_params(which='minor', length=5)
        ax.set_title(r'$\rm{Interpolation\;of\;z-score}$', fontsize=20)



        fig.tight_layout()
        return fig

    @staticmethod
    def quad_pol(x, a, b, c):
        return a * x ** 2 + b * x + c

    @staticmethod
    def ellipse(x, y, a, b, c, d):
        return a * x ** 2 + b * y ** 2 + c * x * y + d

    @staticmethod
    def stdom(x):
        return np.std(x) / np.sqrt(len(x))

    @staticmethod
    def wavg(group):
        z = group['z-score']
        sigma_z = group['uncertainty']
        z_wavg = ((z / sigma_z ** 2).sum()) / ((1 / sigma_z ** 2).sum())
        z_wavg_unc = 1 / ((1 / sigma_z ** 2).sum())
        return pd.Series({'z-score': z_wavg, 'uncertainty': z_wavg_unc})

    @staticmethod
    def coefficient_matrix(eft_points):
        matrix = []
        for c in eft_points:
            cuu = c[0]
            cug = c[1]
            row = [cuu ** 2, cug ** 2, cug * cuu]
            matrix.append(row)
        return np.array(matrix)

