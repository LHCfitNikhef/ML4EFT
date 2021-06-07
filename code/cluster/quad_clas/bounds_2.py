import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
import sys, os
from scipy.stats import norm
import math
from quad_classifier_cluster import EventDataset
import xsec_cluster as ExS
import expected_events as exp_nevents
import analyse
import lhelib.lhe as lhe

import scipy
import torch

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)


def write_log(log):
    with open("/data/theorie/jthoeve/ML4EFT/quad_clas/bounds_log.txt", "a") as f:
        f.write(log + "\n")


class StatAnalysis:
    """
    Construct the pdf of the test statistic tc by using either the NN reconstructed likelihood ratio
    or the analytical likelihood ratio. In the former case, nn should be set to True.
    """

    # points in EFT parameter space used to find the dependence of the cross section on the Wilson coefficients
    eft_points = [[-10.0, 0], [-5.0, 0], [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0], [0, -10.0], [0, -5.0], [0, -1.0],
                  [0, 1.0], [0, 5.0], [0, 10.0], [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],
                  [10.0, 2.0], [0.0, 0.0]]

    luminosity = 6  # Units: pb^-1

    def __init__(self, path_output, dict_int=None, nn=False, bins=None, truth=False, fit=False, limits=None):
        self.mean_tc_eft = None
        self.sigma_tc_eft = None
        self.mean_tc_sm = None
        self.sigma_tc_sm = None
        self.z_score = None
        self.mean_tauc_eft = None
        self.mean_tauc_sm = None

        self.mean_tc_binned_sm = None
        self.mean_tc_binned_eft = None
        self.std_tc_binned_sm = None
        self.std_tc_binned_eft = None
        self.z_score_binned = None
        self.p_value_binned = None

        self.path_output = path_output

        if bins is None:
            # load the total cross section for each of the eft points in eft_points, including uncertainty
            # This is needed to find how the expected number of events varies with the Wilson coefficient
            self.nn = nn
            self.truth = truth
            self.dict_int = dict_int
            self.data_eft = None
            self.data_sm = None
            self.nu = None
            self.xsec, self.xsec_sigma = self.xsec_unbinned()
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

            self.cuu_plane, self.cug_plane, self.p_values_asi, self.z_scores_asi = self.binned_analysis(limits=limits)
            #self.plot_binned_analysis()
            #self.plot_tc_binned(c)

    # binned methods

    def xsec_binned(self):
        """ Creates a numpy ndarray with the cross section in each bin for all the the eft points
        in the list self.eft_points and save it to disk.
        """

        # define an empty list dataset that is going to be filled with the cross section in each bin
        dataset = []

        for i, eft_point in enumerate(self.eft_points):

            #  path to lhe file
            path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{}/bin/process_{}/Events/run_01/unweighted_events.lhe'.format(i, i)
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

        os.makedirs(self.path_output)
        with open(os.path.join(self.path_output, "xsec_bin.npy"), 'wb') as f:
            np.save(f, dataset)

    def expected_events_binned(self, c):
        """
        Returns
        -------
        The number of expected events in each bin at the specified point in EFT parameter space
        """

        path_xsec_binned = os.path.join(self.path_output, "xsec_bin.npy")
        with open(path_xsec_binned, 'rb') as f:
            dataset = np.load(f)

        # build the matrix of coefficients
        coeff_mat = self.coefficient_matrix()

        # solve the linear equation xsec = coeff_matrix * a for a

        # TODO: rewrite the blow so that the fit does not have to be done each time the function is called
        a, _, _, _ = np.linalg.lstsq(coeff_mat, dataset, rcond=None)

        # find the x_sec per bin at the specified point in eft parameter space
        cugre, cuu = c[0], c[1]
        eft_point = np.array([1, cugre, cugre ** 2, cuu, cuu ** 2, cugre * cuu])
        x_sec = np.einsum('ij,i', a, eft_point)
        return x_sec * self.luminosity

    def coefficient_matrix(self):
        coeff_mat = []
        for cugre, cuu in self.eft_points:
            row = [1, cugre, cugre ** 2, cuu, cuu ** 2, cugre * cuu]
            coeff_mat.append(row)
        coeff_mat = np.array(coeff_mat)
        return coeff_mat

    def plot_binned_analysis(self, path_save):
        """ Method to produce a heatmap of the asymptotic z-scores in the 2D eft plane

        """
        plt.figure(figsize=(8, 6))
        ax = plt.subplot(111)
        aspect = (self.cuu_plane.max()-self.cuu_plane.min())/(self.cug_plane.max()-self.cug_plane.min())
        ax.contour(self.cuu_plane, self.cug_plane, self.z_scores_asi, levels=np.array([1.64]))

        # from imshow doc: The first two dimensions (M, N) define the rows and columns of the image. Without transposing cuu
        # would create the rows, whereas we want cuu on the horizontal axis.
        im = ax.imshow(self.z_scores_asi.T, interpolation='hanning', origin='lower', vmin=0, vmax=2, cmap='BuGn', extent=[self.cuu_plane.min(), self.cuu_plane.max(), self.cug_plane.min(), self.cug_plane.max()], aspect=aspect)

        ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
        ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
        plt.colorbar(im)
        ax.set_title(r'$\rm{z-score\;(asymptotic)}$', fontsize=20)
        plt.savefig(path_save)

    def binned_analysis(self, limits=None, exact=False):
        """ Method to compute the z-score and p-value in the 2D eft plane specified by cug and cuu

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
        p_values_asi = []
        z_scores_asi = []
        if limits is None:
            cuu_list = np.linspace(-5, 5, 20)
            cug_list = np.linspace(-0.15, 1, 10)
        else:
            cuu_min, cuu_max = limits[0, :]
            cug_min, cug_max = limits[1, :]
            cuu_list = np.linspace(cuu_min, cuu_max, 200)
            cug_list = np.linspace(cug_min, cug_max, 200)

        for cuu in cuu_list:
            for cug in cug_list:
                c = np.array([cug, cuu])
                self.nu_i = self.expected_entries(c)

                if exact:
                    self.mean_tc_binned_mc, self.std_tc_binned_mc, self.tc_data, self.z_score_binned_mc = self.find_bound_binned_mc()

                self.mean_tc_asi, self.std_tc_asi = self.find_pdf_binned_asimov()
                z_score_asi, p_value_asi = self.p_value_asimov()

                p_values_asi.append(p_value_asi)
                z_scores_asi.append(z_score_asi)

        p_values_asi = np.array(p_values_asi)
        z_scores_asi = np.array(z_scores_asi)

        p_values_asi = np.reshape(p_values_asi, (len(cuu_list), len(cug_list)))
        z_scores_asi = np.reshape(z_scores_asi, (len(cuu_list), len(cug_list)))
        cuu_plane, cug_plane = np.meshgrid(cuu_list, cug_list, indexing='ij')

        # idx = np.argwhere(np.diff(np.sign(p_values_asi - 0.05))).flatten()
        # c_exc = ()

        return cuu_plane, cug_plane, p_values_asi, z_scores_asi

    def expected_entries(self, c):
        nu_i_eft = self.expected_events_binned(c).astype(int)
        nu_i_sm = self.expected_events_binned(np.zeros(len(c))).astype(int)
        nu_i = {'sm': nu_i_sm, 'eft': nu_i_eft}
        return nu_i

    def find_pdf_binned_mc(self, hypothesis, n_tc):
        """ Construct a histogram of the distribution of the binned test statistic using mc sampling.

        Parameters
        ----------
        n_tc: int
            number of samples in the histogram of tc
        hypothesis: SM or EFT

        Returns
        -------
        mean, standard deviation, tc histogram
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
        """ Compute the mean and standard deviation of the asymptotic distribution of the binned test statistic.

        Returns
        -------
        Two dictionaries with the mean and standard deviation each having both keys sm and eft.
        """

        tc_mean_sm_asi = self.t_c_asimov('sm', self.nu_i['eft'], self.nu_i['sm'])
        tc_mean_eft_asi = self.t_c_asimov('eft', self.nu_i['eft'], self.nu_i['sm'])
        tc_std_sm_asi = np.sqrt(2 * self.t_c_asimov('sm', self.nu_i['eft'], self.nu_i['sm']))
        tc_std_eft_asi = np.sqrt(-2 * self.t_c_asimov('eft', self.nu_i['eft'], self.nu_i['sm']))

        mean_asi = {'sm': tc_mean_sm_asi, 'eft': tc_mean_eft_asi}
        std_asi = {'sm': tc_std_sm_asi, 'eft': tc_std_eft_asi}
        return mean_asi, std_asi

    def find_bound_binned_mc(self, n_tc):

        mean_tc_binned_sm, std_tc_binned_sm, tc_data_sm = self.find_pdf_binned_mc(hypothesis='sm', n_tc=n_tc)
        mean_tc_binned_eft, std_tc_binned_eft, tc_data_eft = self.find_pdf_binned_mc(hypothesis='eft', n_tc=n_tc)
        z_score_binned = (mean_tc_binned_sm - mean_tc_binned_eft) / std_tc_binned_eft

        mean = {'sm': mean_tc_binned_sm, 'eft': mean_tc_binned_eft}
        std = {'sm': std_tc_binned_sm, 'eft': std_tc_binned_eft}
        tc_data = {'sm': tc_data_sm, 'eft': tc_data_eft}

        # with open(os.path.join(path_output, "z_scores_cug_check_v2.dat"), "a") as f:
        #     #f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.z_score_binned) + "\t" + str(z_score_binned_unc) + "\n")
        #     f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(z_score_binned) + "\n")

        return mean, std, tc_data, z_score_binned

    def p_value_asimov(self):
        z_score = (self.mean_tc_asi['sm'] - self.mean_tc_asi['eft']) / self.std_tc_asi['eft']
        p_value = 1 - norm.cdf(z_score)
        return z_score, p_value

    def plot_tc_binned(self, c, n_tc=10000, ax=None):

        self.nu_i = self.expected_entries(c)
        self.mean_tc_binned_mc, self.std_tc_binned_mc, self.tc_data, self.z_score_binned_mc = self.find_bound_binned_mc(n_tc=n_tc)
        self.mean_tc_asi, self.std_tc_asi = self.find_pdf_binned_asimov()

        x = np.linspace(self.mean_tc_asi['eft'] - 4 * self.std_tc_asi['eft'],
                        self.mean_tc_asi['sm'] + 4 * self.std_tc_asi['sm'], 400)
        tc_asi_eft = self.gauss(x, self.mean_tc_asi['eft'], self.std_tc_asi['eft'])
        tc_asi_sm = self.gauss(x, self.mean_tc_asi['sm'], self.std_tc_asi['sm'])

        #plt.figure(figsize=(10, 6))
        #ax = plt.subplot(111)

        # create plots
        ax.hist(self.tc_data['eft'], bins=80, label=r'$\rm{Exact\;(EFT)}$', density=True, color='C0', alpha=0.5)
        ax.hist(self.tc_data['sm'], bins=80, label=r'$\rm{Exact\;(SM)}$', density=True, color='C1', alpha=0.5)
        ax.plot(x, tc_asi_eft, label=r'$\rm{Asymptotic\;(EFT)}$', color='C0')
        ax.plot(x, tc_asi_sm, label=r'$\rm{Asymptotic\;(SM)}$', color='C1')

        # plot settings
        ax.set_xlabel(r'$t_c$', fontsize=20)
        ax.set_title(r'$\rm{Asymptotic\;versus\;exact\;(binned\;analysis)}$', fontsize=20)
        ax.legend(loc='upper left', fontsize=15, frameon=False)
        plt.tight_layout()

        z_score = (self.mean_tc_asi['sm']-self.mean_tc_asi['eft'])/self.std_tc_asi['eft']
        ax.text(0.05, 0.19, r'$\rm{z-score} = %.2f$' % z_score, fontsize=20, transform=ax.transAxes)
        ax.text(0.05, 0.12, r'$\rm{cuu} = %.2f $' % c[1], fontsize=20, transform=ax.transAxes)
        ax.text(0.05, 0.05, r'$\rm{cug} = %.2f $' % c[0], fontsize=20, transform=ax.transAxes)
        return ax
        #plt.savefig(path_save)

    @staticmethod
    def gauss(x, mean, sigma):
        return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))

    @staticmethod
    def t_c_asimov(hypothesis, nu_i_eft, nu_i_sm):
        """ Compute the binned test statistic with the Asimov dataset under either the SM or the EFT.

        Parameters
        ----------
        hypothesis: the hypothesis under which t_c is to be computed
        nu_i_eft: expected number of entries in bin i under the EFT
        nu_i_sm: expected number of entries in bin i under the SM

        Returns
        -------
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
        data = []
        data_sigma = []

        for i, eft_point in enumerate(self.eft_points):
            #  path to lhe file
            path = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{}/bin/process_{}/Events/run_01/unweighted_events.lhe'.format(i, i)
            if 5 < i < 12:
                path = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/cuu/eft_{}.lhe'.format(i - 5)
            y, sigma_y = lhe.total_xs(path)
            data.append(y)
            data_sigma.append(sigma_y)
        data = np.array(data)
        data_sigma = np.array(data_sigma)
        return data, data_sigma

    def expected_nevents(self, c):
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

        nu = {'sm': xsec_sm*self.luminosity, 'eft': xsec_eft*self.luminosity}
        return nu

    def get_tc_truth(self, hypothesis):
        cug, cuu = dict_int.keys()

        dsigma_dmtt_eft = []
        for i, (cug, cuu) in enumerate(dict_int.keys()):
            dsigma_dmtt_eft.append([ExS.dsigma_dmtt(mtt, cug, cuu) for mtt in self.data_eft[i]])

        dsigma_dmtt_eft = np.array(dsigma_dmtt_eft)
        dsigma_dmtt_sm = np.array([ExS.dsigma_dmtt(mtt, cug, cuu) for mtt in self.data_sm])

        # likelihood ratio
        r_c = dsigma_dmtt_eft / dsigma_dmtt_sm

        # log-likelihood ratio
        tau_c = np.log(r_c)
        mean_tauc = np.mean(tau_c, axis=1).flatten()

        # expected number of events
        expected_eft = np.array([nu['eft'] for nu in self.nu])
        expected_sm = np.array([nu['sm'] for nu in self.nu])

        mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc
        sigma_tc = np.sqrt(expected_eft * np.mean(tau_c ** 2)) if hypothesis == 'eft' else np.sqrt(
            expected_sm * np.mean(tau_c ** 2))

        return mean_tc, sigma_tc

    def get_tc_nn(self, network_size, nn_rep, hypothesis):

        r_c = []
        for i, (cug, cuu) in enumerate(dict_int.keys()):
            ratio_list = []
            for rep in range(1, nn_rep + 1):
                pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(rep)
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
        Given the eft parameter(s) c, this function computes the mean and standard deviation of pdf(tc) under both
        the SM and the EFT. It uses the analytical likelihood ratio.
        :param c: nd_array that specifies the point in eft parameter space
        """

        # Compute the expected number of events
        self.nu = [self.expected_nevents(np.array(c)) for c in self.dict_int.keys()]

        # generate samples with mg5 if not yet available and store them at path.
        # path = lhe.generate_samples(c, self.output_path)

        path_sm = '/data/theorie/jthoeve/ML4EFT/quad_clas/sm_events.lhe'

        # load the lhe file and construct the dataset of mtt
        n = int(1e2) # parent dataset
        s = int(1e1) # size of subset
        self.data_eft = [lhe.load_events(path_eft, n, s) * 10 ** -3 for path_eft in self.dict_int.values()]
        self.data_sm = lhe.load_events(path_sm, n, s) * 10 ** -3

        # compute the mean and std. dev. of the pdf(tc) under either the sm or the eft
        if self.nn:  # mean_tc_eft.shape = (n_eft_points, nn_rep)
            network_size = [1, 30, 30, 30, 30, 30, 1]
            nn_rep = 40
            self.mean_tc_eft, self.sigma_tc_eft = self.get_tc_nn(network_size, nn_rep, hypothesis='eft')
            self.mean_tc_sm, self.sigma_tc_sm = self.get_tc_nn(network_size, nn_rep, hypothesis='sm')
        else:  # mean_tc_eft.shape = (n_eft_points, )
            self.mean_tc_eft, self.sigma_tc_eft = self.get_tc_truth(hypothesis='eft')
            self.mean_tc_sm, self.sigma_tc_sm = self.get_tc_truth(hypothesis='sm')

        # given the mean and std. dev. the z-score can be computed
        # for nn: self.z_score.shape = (n_eft_points, nn_rep)
        # for truth: self.z_score.shape = (n_eft_points, )
        self.z_score = (self.mean_tc_sm - self.mean_tc_eft) / self.sigma_tc_eft

        if self.nn:
            #  write the mean and stand. dev. taken over the nn_rep to a file
            with open(os.path.join(self.path_output, "z_scores_test.dat"), "a") as f:
                for i, (cug, cuu) in enumerate(dict_int.keys()):
                    line = "{}\t{}\t{}\t{}\n".format(cug, cuu, np.mean(self.z_score, axis=1)[i], np.std(self.z_score, axis=1)[i])
                    f.write(line)
        else:
            with open(os.path.join(self.path_output, "z_scores_test.dat"), "a") as f:
                for i, (cug, cuu) in enumerate(dict_int.keys()):
                    line = "{}\t{}\t{}\n".format(cug, cuu, self.z_score[i])
                    f.write(line)


def plot_tc_accuracy(binned_analysis):
    ncols = 2
    nrows = math.ceil(len(binned_analysis)/ncols)
    fig = plt.figure(figsize=(ncols * 10, nrows * 6))
    for i, bin in enumerate(binned_analysis):
        ax = fig.add_subplot(nrows, ncols, i + 1)
        plot = bin.plot_tc_binned(np.array([0, 0.5]), n_tc=100000, ax=ax)
        plot.set_title(r'$\rm{Bin}\;%d$'%i)
    fig.tight_layout()
    fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/tc_acc_v4.pdf')

def plot_nu_i(binned):
    fig = plt.figure(figsize=(10,6))
    nu_i_eft = []
    cuu = np.linspace(-10, 10, 100)
    for c in cuu:
        nu_i = binned.expected_entries(np.array([0, c]))
        nu_i_eft.append(nu_i['eft'][-1])
    nu_i_eft = np.array(nu_i_eft)
    plt.plot(cuu, nu_i_eft)
    fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/nu_i_acc.pdf')


if __name__ == '__main__':

    truth = False
    NN = False
    binned = False
    data_loaded = True

    # TODO: write a nice loop over the StatAnalysis instances here

    # input
    dict_int = {(0, -0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_1.lhe',
                (0, -0.45): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_2.lhe'}
    path_output = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn'
    binned = StatAnalysis(path_output=path_output, dict_int=dict_int, nn=True)

    sys.exit()


    binning_0 = np.append(np.linspace(340, 1000, 40), 4000).astype(int)
    binning_1 = np.append(np.linspace(340, 1000, 20), 4000).astype(int)
    binning_2 = np.append(np.linspace(340, 1000, 10), 4000).astype(int)
    binning_3 = np.append(np.linspace(340, 1000, 5), 4000).astype(int)
    binning_4 = np.append(np.linspace(340, 1000, 2), 4000).astype(int)
    binning_5 = np.append(np.linspace(340, 1000, 1), 4000).astype(int)


    path_output_bin_0 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_0'
    path_output_bin_1 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_1'
    path_output_bin_2 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_2'
    path_output_bin_3 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_3'
    path_output_bin_4 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_4'
    path_output_bin_5 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_5'

    # limits = np.array([[-1.2, 1.2], [-0.15, 0.2]])

    # construct a list of StatAnalysis instances, each having a different bin choice
    binned_analysis = []
    binning = [binning_0, binning_1, binning_2, binning_3, binning_4, binning_5]
    path_output = [path_output_bin_0, path_output_bin_1, path_output_bin_2, path_output_bin_3, path_output_bin_4, path_output_bin_5]
    for i in range(len(binning)):
        binned_analysis.append(StatAnalysis(path_output=path_output[i], bins=binning[i], fit=True))
    #StatAnalysis.luminosity = 6*10
    plot_tc_accuracy(binned_analysis)
    sys.exit()


    #bin_1.plot_binned_analysis(path_save='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores_heatmap_bin_3.pdf')

    from scipy.ndimage.filters import gaussian_filter

    sigma = 0.8  # this depends on how noisy your data is, play with it!

    data_bin0 = gaussian_filter(bin_0.z_scores_asi, sigma)
    data_bin1 = gaussian_filter(bin_1.z_scores_asi, sigma)
    data_bin2 = gaussian_filter(bin_2.z_scores_asi, sigma)
    data_bin3 = gaussian_filter(bin_3.z_scores_asi, sigma)


    fig, ax = plt.subplots(figsize=(10,6))
    cntr0 = ax.contour(bin_1.cuu_plane, bin_0.cug_plane, data_bin0, levels=np.array([1.64]), colors='C3')
    cntr1 = ax.contour(bin_1.cuu_plane, bin_1.cug_plane, data_bin1, levels=np.array([1.64]), colors='C0')
    cntr2 = ax.contour(bin_2.cuu_plane, bin_2.cug_plane, data_bin2, levels=np.array([1.64]), colors='C1')
    cntr3 = ax.contour(bin_3.cuu_plane, bin_3.cug_plane, bin_3.z_scores_asi, levels=np.array([1.64]), colors='C2')

    h0, _ = cntr0.legend_elements()
    h1, _ = cntr1.legend_elements()
    h2, _ = cntr2.legend_elements()
    h3, _ = cntr3.legend_elements()
    ax.legend([h0[0], h1[0], h2[0], h3[0]], [r'$\rm{Bin\;0}$', r'$\rm{Bin\;1}$', r'$\rm{Bin\;2}$', r'$\rm{Bin\;3}$'])
    #ax.legend([h3[0]], [r'$\rm{Bin\;3}$'])
    ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
    ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
    ax.set_title(r'$\rm{Expected\;exclusion\;limits}$', fontsize=20)

    plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/exclusion_limit_bin_all_v3.pdf')




    #bins = np.arange(300, 4100, 100)

    eft_points_mcuu = [[0, -0.40], [0, -0.45], [0, -0.50], [0, -0.55], [0, -0.60], [0, -0.65], [0, -0.70],
                  [0, -0.75], [0, -0.80]]
        # , [-0.85, 0], [-0.90, 0], [-0.95, 0], [-1.00, 0], [-1.05, 0],
        #           [-1.10, 0], [-1.15, 0], [-1.20, 0], [-1.25, 0], [-1.30, 0], [-1.35, 0], [-1.40, 0]]

    eft_points_pcug = [[0.01, 0], [0.05, 0], [0.1, 0], [0.3, 0]]

    eft_points_ncug = [[-0.075, 0], [-0.10, 0], [-0.125, 0]]

    eft_point_pdiag = [[0.02, 0.1], [0.04, 0.2], [0.06, 0.3]]

    # choice of binning



    # the below is only needed for a binned analysis
    # fit the cross section per bin as a function of c
    if not data_loaded:
        exp_nevents.xsec_binned(bin_3, '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3_v2')

    ####### TRUTH #########
    if truth is True:

        path_output_truth = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth'

        for i, c in enumerate(eft_point_pdiag):
            StatAnalysis(c, nn=False,
                         path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pdiag/eft_{}.lhe'.format(i+1),
                         path_output=path_output_truth,
                         bins=None)

        # StatAnalysis(np.array([0, 0.40]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_040_v2.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.45]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_045_v2.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.50]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05_v2.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.55]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_055_v2.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.75]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.87]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 1.0]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 1.2]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_12.lhe',
        #              path_output=path_output_truth,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 1.4]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_14.lhe',
        #              path_output=path_output_truth,
        #              bins=None)



    ####### NN #########
    if NN is True:

        path_output_nn = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn'
        for i, c in enumerate(eft_point_pdiag):
            StatAnalysis(c, nn=True,
                         path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pdiag/eft_{}.lhe'.format(i+1),
                         path_output=path_output_nn,
                         bins=None)

        # StatAnalysis(np.array([0, 0.40]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_040_v2.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.45]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_045_v2.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.50]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05_v2.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.55]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_055_v2.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.75]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 0.87]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 1.0]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 1.2]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_12.lhe',
        #              path_output=path_output_nn,
        #              bins=None)
        #
        # StatAnalysis(np.array([0, 1.4]), nn=True,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_14.lhe',
        #              path_output=path_output_nn,
        #              bins=None)

    ####### BINNED #########
    if binned is True:

        path_output_bin_1 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_1_v2'
        path_output_bin_2 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_2_v3'
        path_output_bin_3 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3_v2'

        #StatAnalysis(np.array([0, -0.75]), nn=False, path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_8.lhe', path_output=path_output_bin_1, bins=bin_1)

        #sys.exit()
        # for i, c in enumerate(eft_points_pcug):
        #     StatAnalysis(c, nn=False,
        #                  path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pcug/eft_{}.lhe'.format(i+1),
        #                  path_output=path_output_bin_1,
        #                  bins=bin_1)
        #
        # for i, c in enumerate(eft_points_pcug):
        #     StatAnalysis(c, nn=False,
        #                  path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pcug/eft_{}.lhe'.format(i+1),
        #                  path_output=path_output_bin_2,
        #                  bins=bin_2)
        #
        # for i, c in enumerate(eft_points_pcug):
        #     StatAnalysis(c, nn=False,
        #                  path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pcug/eft_{}.lhe'.format(i+1),
        #                  path_output=path_output_bin_3,
        #                  bins=bin_3)

        # bin 1

        # StatAnalysis(np.array([0, 0.40]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_040_v2.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 0.45]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_045_v2.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 0.50]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05_v2.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)

        # StatAnalysis(np.array([0, 0.55]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_055_v3.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)

        # StatAnalysis(np.array([0, 0.6]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_06_v6.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 0.75]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 0.87]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 1.0]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 1.2]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_12.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 1.4]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_14.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)


        # bin 2

        # StatAnalysis(np.array([0, 0.40]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_040_v2.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        # StatAnalysis(np.array([0, 0.45]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_045_v2.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        # StatAnalysis(np.array([0, 0.50]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05_v2.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        # StatAnalysis(np.array([0, -0.55]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_4.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        StatAnalysis(np.array([0, -0.55]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_4.lhe',
                     path_output=path_output_bin_3,
                     bins=bin_3)

        # StatAnalysis(np.array([0, -0.75]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_8.lhe',
        #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_2_v3',
        #              bins=bin_2)

        # StatAnalysis(np.array([0, -0.50]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_3.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, -0.55]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_4.lhe',
        #              path_output=path_output_bin_1,
        #              bins=bin_1)
        #
        # StatAnalysis(np.array([0, 0.87]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        # StatAnalysis(np.array([0, 1.0]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        # StatAnalysis(np.array([0, 1.2]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_12.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        # StatAnalysis(np.array([0, 1.4]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_14.lhe',
        #              path_output=path_output_bin_2,
        #              bins=bin_2)
        #
        # # bin 3
        #
        # StatAnalysis(np.array([0, 0.40]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_040_v2.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 0.45]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_045_v2.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 0.50]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05_v2.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 0.55]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_055_v2.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 0.75]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 0.87]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 1.0]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 1.2]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_12.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)
        #
        # StatAnalysis(np.array([0, 1.4]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_14.lhe',
        #              path_output=path_output_bin_3,
        #              bins=bin_3)