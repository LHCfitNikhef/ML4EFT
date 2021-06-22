import numpy as np
import matplotlib
# matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib import rc
import os
from scipy.stats import norm
import math

# import own modules
from . import xsec_cluster as axs
from . import analyse
from .lhelib import lhe

# matplotlib.use('PDF')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)


def write_log(log):
    with open("/data/theorie/jthoeve/ML4EFT/quad_clas/bounds_log.txt", "a") as f:
        f.write(log + "\n")


class StatAnalysis:
    """
    This python class object constructs the pdf of the test statistics tc using either the NN reconstructed likelihood
    ratio or the analytical likelihood ratio. It also computes the expected exclusion limits that follow from a
    binned analysis, using the asymptotic distributions based on the Asimov dataset.
    """

    # points in EFT parameter space used to find the dependence of the cross section on the Wilson coefficients
    eft_points = [[0, -10.0], [0, -5.0], [0, -1.0], [0, 1.0], [0, 5.0], [0, 10.0], [-10.0, 0], [-5.0, 0], [-1.0, 0],
                  [1.0, 0], [5.0, 0], [10.0, 0], [-2.0, -10.0], [-1.0, -5.0], [-0.5, -1.0], [0.5, 1.0], [1.0, 5.0],
                  [2.0, 10.0], [0.0, 0.0]]

    def __init__(self, paths, dict_int=None, nn=False, bins=None, truth=False, fit=True, mc_run=None, luminosity=600):
        """

        Parameters
        ----------
        paths: dict
            dictionary that contains the paths to the root directory, output directory and plot directory.
        dict_int: dict
            dictionary with eft coefficients as values and corresponding lhe-file paths as values.
        nn: bool
            includes a nn analysis
        bins: list
            collection of binnings (array_like) for which to run the analysis
        truth: bool
            includes a truth analysis
        fit: bool
            should be set to true for each new run/binning. This is needed to find how the expected number of events
            varies with the Wilson coefficients.
        mc_run: int
            picks a unique replica
        luminosity: float
            luminosity of the experiment in pb^{-1}
        """
        # TODO: use same naming convention as used in analyse/analyse.py
        self.path_root = paths['root']
        self.path_output = paths['output']
        self.path_plots = paths['plots']

        # make output directories
        for i, path in enumerate(paths.values()):
            if i == 0:  # skip the root directory (already created)
                continue
            if not os.path.exists(path):
                os.makedirs(path)

        self.luminosity = luminosity

        if bins is None:

            self.data_eft = None
            self.data_sm = None
            self.nu = None
            self.mean_tc_eft = None
            self.sigma_tc_eft = None
            self.mean_tc_sm = None
            self.sigma_tc_sm = None
            self.z_score = None
            self.nn_rep = None

            self.nn = nn
            self.mc_run = mc_run
            self.truth = truth
            self.dict_int = dict_int

            if fit is True:
                self.xsec, self.xsec_sigma = self.xsec_unbinned()
            else:
                self.xsec = self.load_xsec_unbinned()
            self.find_pdf()
        else:
            self.bins = bins

            # for each new binning the cross section in each bin has to be fitted first
            if fit is True:
                self.xsec_binned()

            self.nu_i = None

            self.mean_tc_binned_mc = None
            self.mean_tc_asi = None

            self.std_tc_binned_mc = None
            self.std_tc_asi = None

            self.tc_data = None
            self.z_score_binned_mc = None

            self.cuu_plane = None
            self.cug_plane = None
            # self.p_values_asi = None
            # self.z_scores_asi = None
            self.p_values = None
            self.z_scores = None

    # binned methods

    def xsec_binned(self):
        """
        Creates a numpy ndarray with the cross section in each bin for all the the eft points
        in the list self.eft_points and save it.
        """

        # define an empty list dataset that is going to be filled with the cross section in each bin
        dataset = []

        for i in range(len(self.eft_points)):
            # TODO: make this more general
            #  path to lhe file
            path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{}/bin/process_{}/Events/run_01/unweighted_events.lhe'.format(
                i, i)
            if 5 < i < 12:
                path = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/cuu/eft_{}.lhe'.format(i - 5)

            n_tot = 100000
            data = lhe.load_events(path, n=n_tot, s=n_tot)
            n_bin, _ = np.histogram(data, bins=self.bins)

            # total inclusive cross-section
            xsec, _ = lhe.total_xs(path)

            # the cross section in bin i is computed by multiplying the ratio of the number of events
            # in each bin over the total number of events with the total cross section
            sigma_bin = n_bin / n_tot * xsec

            # append the cross section per bin to the list dataset.
            dataset.append(sigma_bin)

        dataset = np.array(dataset)  # dataset.shape = (len(eft_points), len(bins))

        with open(os.path.join(self.path_output, "xsec_bin.npy"), 'wb') as f:
            np.save(f, dataset)

    def expected_events_binned(self, c):
        """
        Computes the expected number of events in each of the bins at the eft point c

        Returns
        -------
        float
            The number of expected events in each bin at the specified point c
        """

        path_xsec_binned = os.path.join(self.path_output, "xsec_bin.npy")
        with open(path_xsec_binned, 'rb') as f:
            dataset = np.load(f)

        # build the matrix of coefficients
        coeff_mat = self.coefficient_matrix()

        # solve the linear equation xsec = coeff_matrix * a for a

        # TODO: rewrite the below so that the fit does not have to be done each time the function is called
        a, _, _, _ = np.linalg.lstsq(coeff_mat, dataset, rcond=None)

        # find the x_sec per bin at the specified point in eft parameter space
        cuu, cug = c[0], c[1]
        eft_point = np.array([1, cug, cug ** 2, cuu, cuu ** 2, cug * cuu])
        x_sec = np.einsum('ij,i', a, eft_point)
        return x_sec * self.luminosity

    def coefficient_matrix(self):
        """
        Constructs a matrix of eft coefficients that is needed to determine the expected number of events

        Returns
        -------
        array_like
            coefficient matrix
        """
        coeff_mat = []
        for cuu, cug in self.eft_points:
            row = [1, cug, cug ** 2, cuu, cuu ** 2, cug * cuu]
            coeff_mat.append(row)
        coeff_mat = np.array(coeff_mat)
        return coeff_mat

    def plot_binned_analysis(self, path_save):
        """
        Produces a heatmap of the asymptotic z-scores in the 2D eft plane

        Parameters
        ----------
        path_save: str
            location where the heatmap should be saved
        """
        plt.figure(figsize=(8, 6))
        ax = plt.subplot(111)
        aspect = (self.cuu_plane.max() - self.cuu_plane.min()) / (self.cug_plane.max() - self.cug_plane.min())
        ax.contour(self.cuu_plane, self.cug_plane, self.z_scores_asi, levels=np.array([1.64]))

        # from imshow doc: The first two dimensions (M, N) define the rows and columns of the image. Without transposing cuu
        # would create the rows, whereas we want cuu on the horizontal axis.
        im = ax.imshow(self.z_scores_asi.T, interpolation='hanning', origin='lower', vmin=0, vmax=2, cmap='BuGn',
                       extent=[self.cuu_plane.min(), self.cuu_plane.max(), self.cug_plane.min(), self.cug_plane.max()],
                       aspect=aspect)

        ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
        ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
        plt.colorbar(im)
        ax.set_title(r'$\rm{z-score\;(asymptotic)}$', fontsize=20)
        plt.savefig(path_save)

    def binned_analysis(self, extent=None, exact=False):
        """
        Computes the z-score and p-value in the 2D EFT plane

        Parameters
        ----------
        extent: array_like, shape (n, 2)
            The range of the eft parameters to scan
        exact: bool, default=False
            Option to compute the bounds exactly using mc sampling. It is set to False by default.

        Returns
        -------
        cuu_plane: (M, N) ndarray
            coordinate meshgrid for cuu
        cug_plane: (M, N) ndarray
            coordinate meshgrid for cug
        p_values_asi: (M, N) ndarray
            p values evaluated on the (M,N) grid
        z_scores_asi: (M, N) ndarray
            z scores evaluated on the (M,N) grid
        """
        # p_values_asi = []
        # z_scores_asi = []
        p_values = []
        z_scores = []
        if extent is None:
            cuu_list = np.linspace(-5, 5, 20)
            cug_list = np.linspace(-0.15, 1, 10)
        else:
            cuu_min, cuu_max = extent[0, :]
            cug_min, cug_max = extent[1, :]
            cuu_list = np.linspace(cuu_min, cuu_max, 200)
            cug_list = np.linspace(cug_min, cug_max, 200)

        for cug in cug_list:
            for cuu in cuu_list:
                c = np.array([cuu, cug])
                self.nu_i = self.expected_entries(c)

                # if exact:
                #     self.mean_tc_binned_mc, self.std_tc_binned_mc, self.tc_data, self.z_score_binned_mc = self.find_bound_binned_mc()

                self.mean_tc, self.std_tc = self.find_pdf_binned()
                z_score, p_value = self.p_value()

                # self.mean_tc_asi, self.std_tc_asi = self.find_pdf_binned_asimov()
                # z_score_asi, p_value_asi = self.p_value_asimov()

                p_values.append(p_value)
                z_scores.append(z_score)

                # p_values_asi.append(p_value_asi)
                # z_scores_asi.append(z_score_asi)

        # p_values_asi = np.array(p_values_asi)
        # z_scores_asi = np.array(z_scores_asi)
        p_values = np.array(p_values)
        z_scores = np.array(z_scores)

        # TODO: how to document this in sphinx?
        # self.p_values_asi = np.reshape(p_values_asi, (len(cug_list), len(cuu_list)))
        # self.z_scores_asi = np.reshape(z_scores_asi, (len(cug_list), len(cuu_list)))

        self.p_values = np.reshape(p_values, (len(cug_list), len(cuu_list)))
        self.z_scores = np.reshape(z_scores, (len(cug_list), len(cuu_list)))
        self.cuu_plane, self.cug_plane = np.meshgrid(cuu_list, cug_list)

        # idx = np.argwhere(np.diff(np.sign(p_values_asi - 0.05))).flatten()

    def find_pdf_binned(self):
        # tc_mean_sm_asi = self.t_c_asimov('sm', self.nu_i['eft'], self.nu_i['sm'])
        # tc_mean_eft_asi = self.t_c_asimov('eft', self.nu_i['eft'], self.nu_i['sm'])
        # tc_std_sm_asi = np.sqrt(2 * self.t_c_asimov('sm', self.nu_i['eft'], self.nu_i['sm']))
        # tc_std_eft_asi = np.sqrt(-2 * self.t_c_asimov('eft', self.nu_i['eft'], self.nu_i['sm']))
        nu_eft = np.sum(self.nu_i['eft'])
        nu_sm = np.sum(self.nu_i['sm'])

        mean_tc_sm = nu_eft - nu_sm - np.sum(self.nu_i['sm'] * np.log(self.nu_i['eft'] / self.nu_i['sm']))
        mean_tc_eft = nu_eft - nu_sm - np.sum(self.nu_i['eft'] * np.log(self.nu_i['eft'] / self.nu_i['sm']))

        std_tc_sm = np.sqrt(np.sum(np.square(np.log(self.nu_i['eft'] / self.nu_i['sm']) * np.sqrt(self.nu_i['sm']))))
        std_tc_eft = np.sqrt(np.sum(np.square(np.log(self.nu_i['eft'] / self.nu_i['sm']) * np.sqrt(self.nu_i['eft']))))

        mean_tc = {'sm': mean_tc_sm, 'eft': mean_tc_eft}
        std_tc = {'sm': std_tc_sm, 'eft': std_tc_eft}

        return mean_tc, std_tc

    def expected_entries(self, c):
        """

        Parameters
        ----------
        c: array_like, shape = (n, )
            n wilson coefficient(s)
        Returns
        -------
        dict
            dictionary with expected number of events per bin for both the sm and the eft
        """
        nu_i_eft = self.expected_events_binned(c).astype(int)
        nu_i_sm = self.expected_events_binned(np.zeros(len(c))).astype(int)
        nu_i = {'sm': nu_i_sm, 'eft': nu_i_eft}
        return nu_i

    def find_pdf_binned_mc(self, hypothesis, n_tc):
        """
        Constructs a histogram of the distribution of the binned test statistic using mc sampling.

        Parameters
        ----------
        hypothesis: str
            sm or eft
        n_tc: int
            number of samples in the histogram of tc

        Returns
        -------
        tuple
            mean, standard deviation, tc samples
        """
        path_sm = '/data/theorie/jthoeve/ML4EFT/quad_clas/sm_events.lhe'

        # total number of expected events is found by taking the sum over the binned expected countings
        expected_eft = np.sum(self.nu_i['eft'])
        expected_sm = np.sum(self.nu_i['sm'])

        # comment out below to run the cross-check using MC data with nu_i equal to parent nu_i

        # event_data_tot_sm = load_data(path_sm, n, s=n)
        # event_data_tot_eft = load_data(path_eft, n, s=n)
        #
        # n_i_parent_sm, _ = np.histogram(event_data_tot_sm, bins=bins)
        # xsec_sm, _ = exp_nevents.load_datapoint(path_sm)
        # nu_sm = luminosity * xsec_sm
        # nu_i_parent_sm = (n_i_parent_sm / n) * nu_sm
        #
        # n_i_parent_eft, _ = np.histogram(event_data_tot_eft, bins=bins)
        # xsec_eft, _ = exp_nevents.load_datapoint(path_eft)
        # nu_eft = luminosity * xsec_eft
        # nu_i_parent_eft = (n_i_parent_eft / n) * nu_eft
        #
        # expected_eft = np.sum(nu_i_parent_eft)
        # expected_sm = np.sum(nu_i_parent_sm)

        tc_data = []
        for i in range(n_tc):

            # # total number of expected events
            # n_exp_tot = expected_eft if hypothesis == 'eft' else expected_sm
            #
            # # the size of the dataset is drawn from a Poisson dist with mean n_exp_tot
            # size_dataset = np.random.poisson(n_exp_tot, 1)

            # # draw size_dataset events at random
            # event_data = np.random.choice(event_data_tot_sm, size=size_dataset, replace=False) if hypothesis == 'sm' else np.random.choice(event_data_tot_eft, size=size_dataset, replace=False)
            #
            # # find how many events fall into each bin
            # n_i, _ = np.histogram(event_data, bins=bins)

            if hypothesis == 'eft':
                n_i = np.random.poisson(self.nu_i['eft'], len(self.nu_i['eft']))
            else:
                n_i = np.random.poisson(self.nu_i['sm'], len(self.nu_i['sm']))

            tc = expected_eft - expected_sm - np.sum(n_i * np.log(self.nu_i['eft'] / self.nu_i['sm']))
            tc_data.append(tc)
        tc_data = np.array(tc_data)

        # find mean and variance of tc dist
        mean_tc_binned = np.mean(tc_data)
        std_tc_binned = np.std(tc_data)
        return mean_tc_binned, std_tc_binned, tc_data

    def find_pdf_binned_asimov(self):
        """
        Computes the mean and standard deviation of the asymptotic distribution of the binned test statistic.

        Returns
        -------
        tuple
            Two dictionaries with the mean and standard deviation of the asymptotic distribution
            for both the sm and the eft.
        """

        tc_mean_sm_asi = self.t_c_asimov('sm', self.nu_i['eft'], self.nu_i['sm'])
        tc_mean_eft_asi = self.t_c_asimov('eft', self.nu_i['eft'], self.nu_i['sm'])
        tc_std_sm_asi = np.sqrt(2 * self.t_c_asimov('sm', self.nu_i['eft'], self.nu_i['sm']))
        tc_std_eft_asi = np.sqrt(-2 * self.t_c_asimov('eft', self.nu_i['eft'], self.nu_i['sm']))

        mean_asi = {'sm': tc_mean_sm_asi, 'eft': tc_mean_eft_asi}
        std_asi = {'sm': tc_std_sm_asi, 'eft': tc_std_eft_asi}
        return mean_asi, std_asi

    def find_bound_binned_mc(self, n_tc):
        """
        Computes the mean and standard deviation of the exact distribution of the binned test statistic.
        It also computes the z-score.

        Parameters
        ----------
        n_tc: int
            number of samples

        Returns
        -------
        tuple
            mean, standard deviation, tc samples and z-score
        """
        mean_tc_binned_sm, std_tc_binned_sm, tc_data_sm = self.find_pdf_binned_mc(hypothesis='sm', n_tc=n_tc)
        mean_tc_binned_eft, std_tc_binned_eft, tc_data_eft = self.find_pdf_binned_mc(hypothesis='eft', n_tc=n_tc)
        z_score_binned = (mean_tc_binned_sm - mean_tc_binned_eft) / std_tc_binned_eft

        mean = {'sm': mean_tc_binned_sm, 'eft': mean_tc_binned_eft}
        std = {'sm': std_tc_binned_sm, 'eft': std_tc_binned_eft}
        tc_data = {'sm': tc_data_sm, 'eft': tc_data_eft}

        return mean, std, tc_data, z_score_binned

    def p_value(self):
        """
        Computes the z-score and p-value using the asymptotic distribution

        Returns
        -------
        tuple
            z-score, p-value
        """
        z_score = (self.mean_tc['sm'] - self.mean_tc['eft']) / self.std_tc['eft']
        p_value = 1 - norm.cdf(z_score)
        return z_score, p_value


    def p_value_asimov(self):
        """
        Computes the z-score and p-value using the asymptotic distribution

        Returns
        -------
        tuple
            z-score, p-value
        """
        z_score = (self.mean_tc_asi['sm'] - self.mean_tc_asi['eft']) / self.std_tc_asi['eft']
        p_value = 1 - norm.cdf(z_score)
        return z_score, p_value

    def plot_tc_binned(self, c, n_tc=10000, ax=None):
        """

        Parameters
        ----------
        c: array_like, shape = (n, )
            eft point
        n_tc:
            number of samples that make up the histogram
        ax: ax object
            empty ax object

        Returns
        -------
        ax object
        """

        self.nu_i = self.expected_entries(c)

        self.mean_tc_binned_mc, self.std_tc_binned_mc, self.tc_data, self.z_score_binned_mc = self.find_bound_binned_mc(
            n_tc=n_tc)
        #self.mean_tc_asi, self.std_tc_asi = self.find_pdf_binned_asimov()
        mean_tc, std_tc = self.find_pdf_binned()

        # x = np.linspace(self.mean_tc_asi['eft'] - 4 * self.std_tc_asi['eft'],
        #                  self.mean_tc_asi['sm'] + 4 * self.std_tc_asi['sm'], 400)
        # tc_asi_eft = self.gauss(x, self.mean_tc_asi['eft'], self.std_tc_asi['eft'])
        # tc_asi_sm = self.gauss(x, self.mean_tc_asi['sm'], self.std_tc_asi['sm'])

        # create plots
        ax.hist(self.tc_data['eft'], bins=80, label=r'$\rm{Exact\;(EFT)}$', density=True, color='C0', alpha=0.5, align='mid')
        ax.hist(self.tc_data['sm'], bins=80, label=r'$\rm{Exact\;(SM)}$', density=True, color='C1', alpha=0.5, align='mid')
        #ax.plot(x, tc_asi_eft, label=r'$\rm{Asymptotic\;(EFT)}$', color='C0')
        #ax.plot(x, tc_asi_sm, label=r'$\rm{Asymptotic\;(SM)}$', color='C1')

        std_tc_sm = np.sqrt(np.sum(np.square(np.log(self.nu_i['eft'] / self.nu_i['sm']) * np.sqrt(self.nu_i['sm']))))
        std_tc_eft = np.sqrt(np.sum(np.square(np.log(self.nu_i['eft'] / self.nu_i['sm']) * np.sqrt(self.nu_i['eft']))))

        x = np.linspace(mean_tc['eft'] - 4 * std_tc['eft'],
                        mean_tc['sm'] + 4 * std_tc['sm'], 400)
        tc_eft = self.gauss(x, mean_tc['eft'], std_tc_eft)
        tc_sm = self.gauss(x, mean_tc['sm'], std_tc_sm)

        ax.plot(x, tc_eft, label=r'$\rm{Asymptotic\;(EFT)}$', color='C0')
        ax.plot(x, tc_sm, label=r'$\rm{Asymptotic\;(SM)}$', color='C1')

        # ax.plot(x, self.gauss(x, self.mean_tc_asi['eft'], np.log(self.nu_i['eft']/self.nu_i['sm'])*np.sqrt(self.nu_i['eft'])), label=r'$\rm{Poisson\;(EFT)}$', color='C3', linestyle='dashed')
        # ax.plot(x, self.gauss(x, self.mean_tc_asi['sm'],
        #                       np.log(self.nu_i['eft'] / self.nu_i['sm']) * np.sqrt(self.nu_i['sm'])),
        #         label=r'$\rm{Poisson\;(SM)}$', color='C3', linestyle='dashed')
        #
        # ax.plot(x, self.gauss(x, self.mean_tc_asi['eft'],np.sqrt(-2*self.t_c_asimov('eft', self.nu_i['eft'], self.nu_i['sm']))),
        #         label=r'$\rm{Poisson2\;(EFT)}$', color='C2')
        # ax.plot(x, self.gauss(x, self.mean_tc_asi['sm'],
        #                       np.sqrt(2 * self.t_c_asimov('sm', self.nu_i['eft'], self.nu_i['sm']))),
        #         label=r'$\rm{Poisson2\;(SM)}$', color='C2')

        # plot settings
        ax.set_xlabel(r'$t_c$', fontsize=20)
        ax.set_title(r'$\rm{Asymptotic\;versus\;exact\;(binned\;analysis)}$', fontsize=20)
        ax.legend(loc='upper left', fontsize=15, frameon=False)
        plt.tight_layout()

        #z_score = (self.mean_tc_asi['sm'] - self.mean_tc_asi['eft']) / self.std_tc_asi['eft']
        z_score = (mean_tc['sm'] - mean_tc['eft']) / std_tc['eft']
        ax.text(0.05, 0.19, r'$\rm{z-score} = %.2f$' % z_score, fontsize=20, transform=ax.transAxes)
        ax.text(0.05, 0.12, r'$\rm{cuu} = %.2f $' % c[0], fontsize=20, transform=ax.transAxes)
        ax.text(0.05, 0.05, r'$\rm{cug} = %.2f $' % c[1], fontsize=20, transform=ax.transAxes)

        return ax

    @staticmethod
    def gauss(x, mean, sigma):
        return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))

    @staticmethod
    def t_c_asimov(hypothesis, nu_i_eft, nu_i_sm):
        """
        Computes the binned test statistic with the Asimov dataset under either the SM or the EFT.

        Parameters
        ----------
        hypothesis: str
            the hypothesis under which t_c is to be computed
        nu_i_eft: float
            expected number of entries in bin i under the EFT
        nu_i_sm: float
            expected number of entries in bin i under the SM

        Returns
        -------
        float
            The binned test statistic under either the EFT or the SM depending on the hypothesis evaluated using the
            Asimov dataset.
        """
        nu_c = np.sum(nu_i_eft)
        nu_0 = np.sum(nu_i_sm)
        if hypothesis == 'eft':
            t_ac = nu_c - nu_0 - np.sum(nu_i_eft * np.log(nu_i_eft / nu_i_sm))
            return t_ac
        else:
            t_ac = nu_c - nu_0 - np.sum(nu_i_sm * np.log(nu_i_eft / nu_i_sm))
            return t_ac

    # truth and nn methods

    def xsec_unbinned(self):
        """
        Computes the total cross section for each of the eft points in eft_points.

        Returns
        -------
        tuple
            two lists, the first containing the cross sections, and the second the associated uncertainties.
        """
        data = []
        data_sigma = []

        for i, eft_point in enumerate(self.eft_points):
            # TODO: make the path reference more general!
            # path to lhe file
            path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{}/bin/process_{}/Events/run_01/unweighted_events.lhe'.format(
                i, i)
            if 5 < i < 12:
                path = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/cuu/eft_{}.lhe'.format(i - 5)
            y, sigma_y = lhe.total_xs(path)
            data.append(y)
            data_sigma.append(sigma_y)
        data = np.array(data)
        data_sigma = np.array(data_sigma)

        with open(os.path.join(self.path_output, "xsec_unbinned.npy"), 'wb') as f:
            np.save(f, data)

        return data, data_sigma

    def load_xsec_unbinned(self):
        """
        Loads the total cross section for each of the eft points in the unbinned analysis.

        Returns
        -------
        array_like
            array with the total cross section for each the eft points.
        """
        path_xsec_binned = os.path.join(self.path_output, "xsec_unbinned.npy")
        with open(path_xsec_binned, 'rb') as f:
            xsec = np.load(f)
        return xsec

    def expected_nevents(self, c):
        """
        Computes the expected number of events in the unbinned analysis for the specified value of the Wilson
        coefficient c.

        Parameters
        ----------
        c: array_like
            point in eft space

        Returns
        -------
        dict
            expected number of events in the sm and the eft (at point c).
        """
        # TODO: change the order
        cugre = c[0]
        cuu = c[1]

        # build the matrix of coefficients
        coeff_mat = self.coefficient_matrix()

        a, _, _, _ = np.linalg.lstsq(coeff_mat, self.xsec, rcond=None)
        c = np.array([1, cugre, cugre ** 2, cuu, cuu ** 2, cugre * cuu])
        xsec_eft = np.dot(a, c)

        cugre, cuu = 0, 0
        c = np.array([1, cugre, cugre ** 2, cuu, cuu ** 2, cugre * cuu])
        xsec_sm = np.dot(a, c)

        nu = {'sm': xsec_sm * self.luminosity, 'eft': xsec_eft * self.luminosity}
        return nu

    def get_tc_truth(self, hypothesis):
        """
        Computes the mean and standard deviation of the extended log likelihood ratio test statistic tc using the
        analytic likelihood ratio.

        Parameters
        ----------
        hypothesis: str
            sm or eft

        Returns
        -------
        tuple
            mean of tc, standard deviation of tc
            both have shape = (n eft points, )
        """
        dsigma_dmtt_eft = []
        dsigma_dmtt_sm = []
        for i, (cug, cuu) in enumerate(self.dict_int.keys()):
            if hypothesis == 'eft':
                dsigma_dmtt_eft.append([axs.dsigma_dmtt(mtt, cug, cuu) for mtt in self.data_eft[i]])
                dsigma_dmtt_sm.append([axs.dsigma_dmtt(mtt, 0, 0) for mtt in self.data_eft[i]])
            else:  # hypothesis = sm
                dsigma_dmtt_eft.append([axs.dsigma_dmtt(mtt, cug, cuu) for mtt in self.data_sm])

        if hypothesis == 'eft':
            dsigma_dmtt_sm = np.array(dsigma_dmtt_sm)
        else:  # hypothesis = sm
            dsigma_dmtt_sm = np.array([axs.dsigma_dmtt(mtt, 0, 0) for mtt in self.data_sm])
            dsigma_dmtt_sm = np.expand_dims(dsigma_dmtt_sm, axis=0)

        dsigma_dmtt_eft = np.array(dsigma_dmtt_eft)

        # likelihood ratio
        r_c = dsigma_dmtt_eft / dsigma_dmtt_sm

        # log-likelihood ratio
        tau_c = np.log(r_c)  # tau_c.shape = (n_eft_points, n_events)
        mean_tauc_2 = np.mean(tau_c, axis=1).flatten()
        mean_tauc_sq = np.mean(tau_c ** 2, axis=1).flatten()

        # expected number of events
        expected_eft = np.array([nu['eft'] for nu in self.nu])
        expected_sm = np.array([nu['sm'] for nu in self.nu])

        mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc_2 if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc_2
        sigma_tc = np.sqrt(expected_eft * mean_tauc_sq) if hypothesis == 'eft' else np.sqrt(expected_sm * mean_tauc_sq)

        return mean_tc, sigma_tc

    def get_tc_truth_full_diff(self, hypothesis):
        """
        Computes the mean and standard deviation of the extended log likelihood ratio test statistic tc using the
        analytic likelihood ratio.

        Parameters
        ----------
        hypothesis: str
            sm or eft

        Returns
        -------
        tuple
            mean of tc, standard deviation of tc
            both have shape = (n eft points, )
        """
        dsigma_dx_eft = []
        dsigma_dx_sm = []
        for i, (cug, cuu) in enumerate(self.dict_int.keys()):
            if hypothesis == 'eft':
                dsigma_dx_eft.append([axs.dsigma_dx(x, cug, cuu) for x in self.data_eft[i]])
                dsigma_dx_sm.append([axs.dsigma_dx(x, 0, 0) for x in self.data_eft[i]])
            else:  # hypothesis = sm
                dsigma_dx_eft.append([axs.dsigma_dx(x, cug, cuu) for x in self.data_sm])

        if hypothesis == 'eft':
            dsigma_dx_sm = np.array(dsigma_dx_sm)
        else:  # hypothesis = sm
            dsigma_dx_sm = np.array([axs.dsigma_dx(x, 0, 0) for x in self.data_sm])
            dsigma_dx_sm = np.expand_dims(dsigma_dx_sm, axis=0)

        dsigma_dx_eft = np.array(dsigma_dx_eft)

        # likelihood ratio
        r_c = dsigma_dx_eft / dsigma_dx_sm

        # log-likelihood ratio
        tau_c = np.log(r_c)  # tau_c.shape = (n_eft_points, n_events)
        mean_tauc_2 = np.mean(tau_c, axis=1).flatten()
        mean_tauc_sq = np.mean(tau_c ** 2, axis=1).flatten()

        # expected number of events
        expected_eft = np.array([nu['eft'] for nu in self.nu])
        expected_sm = np.array([nu['sm'] for nu in self.nu])

        mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc_2 if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc_2
        sigma_tc = np.sqrt(expected_eft * mean_tauc_sq) if hypothesis == 'eft' else np.sqrt(expected_sm * mean_tauc_sq)

        return mean_tc, sigma_tc


    def get_tc_nn(self, network_size, nn_rep, hypothesis):
        """
        Computes the mean and standard deviation of the extended log likelihood ratio test statistic tc using the
        nn (reconstructed) likelihood ratio.

        Parameters
        ----------
        network_size: list
            architecture of the network that was used for training
        nn_rep: int
            number of neural network replicas that were trained
        hypothesis: str
            sm or eft

        Returns
        -------
        tuple
            mean of tc, standard deviation of tc
            both have shape = (n eft points, nn_rep)
        """
        r_c = []
        for i, (cug, cuu) in enumerate(self.dict_int.keys()):
            ratio_list = []  # stores the likelihood ratio for each nn replica
            for rep in range(1, nn_rep + 1):
                pred_path = '/data/theorie/jthoeve/ML4EFT_v2/output/models/model_1/mc_run_{}'.format(rep)
                mean, std = np.loadtxt(pred_path + '/scaling.dat')
                data = self.data_sm if hypothesis is 'sm' else self.data_eft[i]
                ratio = analyse.get_likelihood_ratio_NN(pred_path + '/trained_nn.pt', network_size, data,
                                                        cug, cuu, mean, std)
                ratio_list.append(ratio)
            r_c.append(ratio_list)
        r_c = np.array(r_c)  # r_c.shape = (n_eft_points, nn_rep, n_events)
        tau_c = np.log(r_c)
        mean_tauc = np.mean(tau_c, axis=2)  # mean_tauc = (n_eft_points, nn_rep)

        # expected number of events
        expected_eft = np.array([nu['eft'] for nu in self.nu])  # expected_eft.shape = (n_eft_points, )
        expected_sm = np.array([nu['sm'] for nu in self.nu])

        # to make broadcasting possible we add a new axis
        expected_eft = np.expand_dims(expected_eft, axis=1)  # expected_eft.shape = (n_eft_points, 1)
        expected_sm = np.expand_dims(expected_sm, axis=1)

        mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc
        sigma_tc = np.sqrt(expected_eft * np.mean(tau_c ** 2, axis=2)) if hypothesis == 'eft' else np.sqrt(
            expected_sm * np.mean(tau_c ** 2, axis=2))
        return mean_tc, sigma_tc  # mean_tc.shape = (n_eft_points, nn_rep)

    def find_pdf(self):
        """
        Computes the mean and standard deviation of the extended likelihood ratio distribution in both the sm and the eft.
        It then gives the corresponding z-score for each of the eft points in the interpolation dictionary. The results are
        written to the output directory specified in the paths dictionary.

        Depending on whether nn is set to true or not, results are either computed analytically or using the neural network.
        """

        # Compute the expected number of events
        self.nu = [self.expected_nevents(np.array(c)) for c in self.dict_int.keys()]

        # TODO: useful feature to include?
        # generate samples with mg5 if not yet available and store them at path.
        # path = lhe.generate_samples(c, self.output_path)

        # TODO: path_sm is hard coded - change this.
        path_sm = '/data/theorie/jthoeve/ML4EFT/quad_clas/sm_events.lhe'

        # load the lhe file and construct the dataset of mtt
        n = int(1e5)  # parent dataset
        s = int(1e4)  # size of subset

        self.data_eft = [lhe.load_events(path_eft, n, s) for path_eft in self.dict_int.values()]
        self.data_sm = lhe.load_events(path_sm, n, s)

        # compute the mean and std. dev. of the pdf(tc) under either the sm or the eft
        if self.nn:  # mean_tc_eft.shape = (n_eft_points, nn_rep)
            network_size = [1, 30, 30, 30, 30, 30, 1]
            self.nn_rep = 40
            self.mean_tc_eft, self.sigma_tc_eft = self.get_tc_nn(network_size, self.nn_rep, hypothesis='eft')
            self.mean_tc_sm, self.sigma_tc_sm = self.get_tc_nn(network_size, self.nn_rep, hypothesis='sm')
        else:  # mean_tc_eft.shape = (n_eft_points, )
            self.mean_tc_eft, self.sigma_tc_eft = self.get_tc_truth_full_diff(hypothesis='eft')
            self.mean_tc_sm, self.sigma_tc_sm = self.get_tc_truth_full_diff(hypothesis='sm')

        # given the mean and std. dev. the z-score can be computed
        # for nn: self.z_score.shape = (n_eft_points, nn_rep)
        # for truth: self.z_score.shape = (n_eft_points, )
        self.z_score = (self.mean_tc_sm - self.mean_tc_eft) / self.sigma_tc_eft

        #  write the mean and stand. dev. taken over the nn_rep to a file
        loc = os.path.join(self.path_output, "mc_run_{}".format(self.mc_run))
        if not os.path.exists(loc):
            os.makedirs(loc)

        if self.nn:
            for rep in range(self.nn_rep):
                loc_rep = os.path.join(loc, 'rep_{}'.format(rep))
                if not os.path.exists(loc_rep):
                    os.makedirs(loc_rep)
                with open(os.path.join(loc_rep, "z_scores.dat"), "a") as f:
                    for i, (cug, cuu) in enumerate(self.dict_int.keys()):
                        line = "{}\t{}\t{}\n".format(cug, cuu, self.z_score[i, rep])
                        f.write(line)
        else:
            with open(os.path.join(loc, "z_scores.dat"), "a") as f:
                for i, (cug, cuu) in enumerate(self.dict_int.keys()):
                    line = "{}\t{}\t{}\n".format(cug, cuu, self.z_score[i])
                    f.write(line)


def plot_tc_accuracy(binned_analyses, c=np.array([0.5, 0]), n=10000):
    """
    This function shows a comparison between the asymptotic distribution and the exact sampling based approach.
    When multiple StatAnalysis instances are passed as an array to binned_analysis, the comparison is made for each of them.

    Parameters
    ----------
    binned_analysis: array_like
        Array that contains StatAnalysis instances
    c: array_like, optional
        EFT point at which to construct the distribution of the test statistic tc
    n: int, optional, default=10000
        Number of samples that make up the histogram

    Returns
    -------
    object
        figure object
    """
    nplots = len(binned_analyses)
    ncols = 2 if nplots > 1 else 1
    nrows = math.ceil(nplots / ncols)
    fig = plt.figure(figsize=(ncols * 10, nrows * 6))
    for i, bin in enumerate(binned_analyses):
        ax = fig.add_subplot(nrows, ncols, i + 1)
        plot = bin.plot_tc_binned(c, n_tc=n, ax=ax)
        plot.set_title(r'$\rm{Binning}\;%d$' % i)
    fig.tight_layout()
    return fig


# TODO: finish function below.
# function to plot the expected number of events as a function of c
def plot_nu_i(binned, path_save):
    fig = plt.figure(figsize=(10, 6))
    nu_i_eft = []
    cuu = np.linspace(-10, 10, 100)
    for c in cuu:
        nu_i = binned.expected_entries(np.array([0, c]))
        nu_i_eft.append(nu_i['eft'][-1])
    nu_i_eft = np.array(nu_i_eft)
    plt.plot(cuu, nu_i_eft)
    fig.savefig(path_save)
