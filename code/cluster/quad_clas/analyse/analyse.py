import numpy as np
import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import csv
from scipy.ndimage.filters import gaussian_filter
from ..core import bounds as bounds


class Analyse:
    """
    This python class object analyses the z-scores that originate from
    a scan over the EFT coefficient space. Results are presented for
    the neural network (nn), truth and binned analyses.

    The (expected) exclusion limits are found by interpolating on the
    z-scores and solving the resulting polynomial for the 95% CL.
    """

    def __init__(self, root_path, truth=True, nn=True, binnings=None, extent=None, fit=True, luminosity=6, mc_runs=100):
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
            collection of binnings for which to run the analysis
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

        if binnings is not None:

            self.binnings = binnings
            self.fit = fit

            # run a binned analysis on each of the binnings
            self.binned_analyses = self.run_binned_analysis()

            # plot accuracy of Asimov method
            fig = bounds.plot_tc_accuracy(self.binned_analyses, c=np.array([1.0, 0]), n=10000)
            fig.savefig(os.path.join(self.plots_path, 'tc_comp.pdf'))
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
        """
        z_scores = []
        for i in range(1, self.mc_runs + 1):
            loc = os.path.join(path, "mc_run_{}/z_scores.dat".format(i))
            with open(loc, "r") as f:
                reader = csv.reader(f, delimiter='\t')
                for line in reader:
                    z_scores.append([float(value) for value in line])
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
            path = os.path.join(self.output_path, 'nn')
            z_scores = self.read_z_scores(path)
            z_scores = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score', 'uncertainty'])
            z_scores_grouped = z_scores.groupby(['cug', 'cuu'])
            z_scores_grouped = z_scores_grouped.apply(self.wavg)
            z_scores_grouped_nn = z_scores_grouped.reset_index()
        else:
            z_scores_grouped_nn = None

        if self.truth:
            path = os.path.join(self.output_path, 'truth')
            z_scores = self.read_z_scores(path)
            z_scores = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score'])
            z_scores_grouped = z_scores.groupby(['cug', 'cuu']).agg({'z-score': ['mean', self.stdom]})
            z_scores_grouped.columns = ['z-score', 'uncertainty']
            z_scores_grouped_truth = z_scores_grouped.reset_index()
        else:
            z_scores_grouped_truth = None

        return z_scores_grouped_truth, z_scores_grouped_nn

    def combine_analyses(self):
        """
        Finds the contours of the 95% CL.
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        cuu = np.linspace(self.extent[0, 0], self.extent[0, 1], 100)
        cug = np.linspace(self.extent[1, 0], self.extent[1, 1], 100)
        cuu_plane, cug_plane = np.meshgrid(cuu, cug)

        labels = []
        contours = []
        colors = ['C2', 'C3', 'C4']
        if self.binned_analyses is not None:
            sigma = 0.8
            for i, binnings in enumerate(self.binned_analyses):
                data_smoothed = gaussian_filter(binnings.z_scores_asi, sigma)
                contour = ax.contour(binnings.cuu_plane, binnings.cug_plane, data_smoothed, levels=np.array([1.64]), colors=colors[i % len(colors)])
                h0, _ = contour.legend_elements()
                contours.append(h0[0])
                labels.append(r'$\rm{Binning\;%d}$' % i)

        self.z_scores_truth, self.z_scores_nn = self.load_z_scores()

        ellipse_param_truth, ellipse_param_nn = self.fit_ellipse()

        if self.truth:
            cntr_truth = ax.contour(cuu_plane, cug_plane,
                                    self.ellipse(cuu_plane, cug_plane, *ellipse_param_truth),
                                    levels=[1.64],
                                    colors='C0')
            h0, _ = cntr_truth.legend_elements()
            contours.append(h0[0])
            labels.append(r'$\rm{Truth}$')

        if self.nn:
            cntr_nn = ax.contour(cuu_plane, cug_plane,
                                    self.ellipse(cuu_plane, cug_plane, *ellipse_param_nn),
                                    levels=[1.64],
                                    colors='C1')
            h0, _ = cntr_nn.legend_elements()
            contours.append(h0[0])
            labels.append(r'$\rm{NN}$')


        # plot settings
        ax.legend(contours, labels, fontsize=15, frameon=False, loc='best')
        ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
        ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
        ax.set_title(r'$\rm{Expected\;exclusion\;limits}$', fontsize=20)

        fig.savefig(os.path.join(self.plots_path, 'ellipses.pdf'))

    def fit_ellipse(self):
        """
        Fit an ellipse through the z-scores

        Returns
        -------
        tuple
            ellipse parameters for the truth and nn analysis
        """
        # solve the linear equation xsec = coeff_matrix * a for a
        if self.truth:
            cuu = self.z_scores_truth.cuu.values
            cug = self.z_scores_truth.cug.values

            eft_points = np.array([cuu, cug]).T

            z_score_truth = self.z_scores_truth['z-score'].values
            z_score_unc_truth = self.z_scores_truth['uncertainty'].values

            coeff_mat = self.coefficient_matrix(eft_points)

            a_truth, _, _, _ = np.linalg.lstsq(coeff_mat, z_score_truth, rcond=None)
        else:
            a_truth = None

        if self.nn:
            cuu = self.z_scores_nn.cuu.values
            cug = self.z_scores_nn.cug.values

            eft_points = np.array([cuu, cug]).T

            z_score_nn = self.z_scores_nn['z-score'].values
            z_score_unc_nn = self.z_scores_nn['uncertainty'].values

            coeff_mat = self.coefficient_matrix(eft_points)
            a_nn, _, _, _ = np.linalg.lstsq(coeff_mat, z_score_nn, rcond=None)
        else:
            a_nn = None

        return a_truth, a_nn

    @staticmethod
    def ellipse(x, y, a, b, c):
        return a * x ** 2 + b * y ** 2 + c * x * y

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

