import pylhe
import numpy as np
import subprocess
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
import sys, os
from scipy.stats import norm

from quad_classifier_cluster import EventDataset
from scipy.stats import chi2
import xsec_cluster as ExS
import expected_events as exp_nevents
import analyse
import scipy
import torch

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

luminosity = 6

def generate_samples(c):
    cugre = c[0]
    cuu = c[1]
    subprocess.call(['chmod', '+x', '/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh'])
    subprocess.call(["/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh", '{}'.format(cugre), '{}'.format(cuu)])
    path = "/data/theorie/jthoeve/ML4EFT/mg5_copies/mg5_test/bin/process_0/Events/run_01/unweighted_events.lhe"
    return path


def get_events(c, path=None):

    if np.all((c == 0)):
        path_dict = {(0, 0): '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_18/bin/process_18/Events/run_01/unweighted_events.lhe'}
    else:
        path_dict = {(c[0], c[1]): path}

    events = EventDataset(tuple(c), n_features=1, path_dict=path_dict, n_dat=10000)
    return events.event_data


def invariant_mass(p1, p2): #TODO use invariant method in quad_classifier_cluster module
    """
    Computes the invariant mass of an event
    """
    return np.sqrt(
        sum((1 if mu == 'e' else -1) * (getattr(p1, mu) + getattr(p2, mu)) ** 2 for mu in ['e', 'px', 'py', 'pz']))


def load_data(path, n, s):
    """ Load a subset of size s from n events from the lhe file.

    Parameters
    ----------
    path: str
        Path to lhe file
    n: int
        total size of the dataset
    s:
        size of the subset
    Returns
    -------
    event_data: ndarray
        The loaded subset of events
    """

    skip = np.random.choice(n, n - s, replace=False)
    event_seq = pylhe.readLHE(path)

    event_data = []

    for i in range(n):
        e = next(event_seq)
        if i not in skip:
            mtt = invariant_mass(e.particles[-1], e.particles[-2])
            event_data.append(mtt)
    event_data = np.array(event_data)
    return event_data


def get_tc(expected_eft, expected_sm, data, c, hypothesis):
    cug, cuu = c
    dsigma_dmtt_eft = np.array([ExS.dsigma_dmtt(mtt_i, cug, cuu) for mtt_i in data])
    dsigma_dmtt_sm = np.array([ExS.dsigma_dmtt(mtt_i, 0, 0) for mtt_i in data])

    r_c = dsigma_dmtt_eft / dsigma_dmtt_sm
    tau_c = np.log(r_c)
    mean_tauc = np.mean(tau_c)
    mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc
    sigma_tc = np.sqrt(expected_eft * np.mean(tau_c ** 2)) if hypothesis == 'eft' else np.sqrt(
        expected_sm * np.mean(tau_c ** 2))
    return mean_tc, sigma_tc, mean_tauc


def get_tc_nn(expected_eft, expected_sm, data, c, hypothesis):
    cug, cuu = c

    network_size = [1, 30, 30, 30, 30, 30, 1]
    r_c = []
    nn_rep = 40
    for i in range(1, nn_rep + 1):
        pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(i)
        mean, std = np.loadtxt(pred_path + '/scaling.dat')
        r_c_i = analyse.get_likelihood_ratio_NN(pred_path + '/trained_nn.pt', network_size, data,
                                                cug, cuu, mean, std)
        r_c.append(r_c_i)
    r_c = np.array(r_c)  # r_c.shape = (nn_rep, n_events)
    tau_c = np.log(r_c)
    mean_tauc = np.mean(tau_c, axis=1)  # mean_tauc = (nn_rep, 1)
    mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc
    sigma_tc = np.sqrt(expected_eft * np.mean(tau_c ** 2, axis=1)) if hypothesis == 'eft' else np.sqrt(
        expected_sm * np.mean(tau_c ** 2, axis=1))
    return mean_tc, sigma_tc  # mean_tc[:, 0].shape = (nn_rep, )


def write_log(log):
    with open("/data/theorie/jthoeve/ML4EFT/quad_clas/bounds_log.txt", "a") as f:
        f.write(log + "\n")


class StatAnalysis:
    """
    Construct the pdf of the test statistic tc by using either the NN reconstructed likelihood ratio
    or the analytical likelihood ratio. In the former case, nn should be set to True.
    """

    def __init__(self, c, nn, path_eft_lhe, path_output, bins=None, fit=False):
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

        if bins is None:
            self.find_pdf(c, nn, path_eft_lhe, path_output)
        else:
            self.bins = bins
            self.path_output = path_output

            if fit is False:
                self.binned_fit()

            self.nu_i = None

            self.mean_tc_binned_mc = None
            self.mean_tc_asi = None

            self.std_tc_binned_mc = None
            self.std_tc_asi = None

            self.tc_data = None
            self.z_score_binned_mc = None

            self.cuu_list, self.cug_list, self.p_values_asi, self.z_scores_asi = self.binned_analysis()
            self.plot_binned_analysis()
            #self.plot_tc_binned(c)

    def binned_fit(self): # TODO: write this method
        pass

    def plot_binned_analysis(self):

        plt.figure(figsize=(8, 6))
        ax = plt.subplot(111)
        aspect = (self.cuu_list.max()-self.cuu_list.min())/(self.cug_list.max()-self.cug_list.min())
        X, Y = np.meshgrid(self.cuu_list, self.cug_list)
        ax.contour(X, Y, self.z_scores_asi, levels=np.array([1.64]))

        im = ax.imshow(self.z_scores_asi, interpolation='hanning', origin='lower', vmin=0, vmax=2, cmap='BuGn', extent=[self.cuu_list.min(), self.cuu_list.max(), self.cug_list.min(), self.cug_list.max()], aspect=aspect)


        # ax.plot(self.cuu_list, self.p_values_asi, label=r'$\rm{p-value}$', color='C0')
        ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
        ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
        #ax.set_xlim((self.cuu_list.min(), self.cuu_list.max()))
        #ax.set_ylim((self.cug_list.min(), self.cug_list.max()))
        plt.colorbar(im)
        ax.set_title(r'$\rm{z-score\;(asymptotic)}$', fontsize=20)
        # ax.legend(loc='best', fontsize=15, frameon=False)
        # plt.tight_layout()
        # plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/p_value_asym.pdf')
        #
        # plt.figure(figsize=(10, 6))
        # ax = plt.subplot(111)
        # ax.plot(self.cuu_list, self.z_scores_asi, label=r'$\rm{z-scores}$', color='C0')
        # ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
        # ax.set_title(r'$\rm{z-scores\;(asymptotic)}$', fontsize=20)
        # ax.legend(loc='best', fontsize=15, frameon=False)
        # plt.tight_layout()
        plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores_heatmap_bin_3.pdf')

    def binned_analysis(self, exact=False):
        p_values_asi = []
        z_scores_asi = []
        cuu_list = np.linspace(-5, 5, 200)
        cug_list = np.linspace(-0.15, 1, 200)

        for cug in cug_list:
            for cuu in cuu_list:
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

        p_values_asi = np.reshape(p_values_asi, (len(cug_list), len(cuu_list)))
        z_scores_asi = np.reshape(z_scores_asi, (len(cug_list), len(cuu_list)))

        # idx = np.argwhere(np.diff(np.sign(p_values_asi - 0.05))).flatten()
        # c_exc = ()

        return cuu_list, cug_list, p_values_asi, z_scores_asi#, c_exc


    def expected_entries(self, c):
        nu_i_eft = exp_nevents.expected_events_binned(c, self.bins, self.path_output).astype(int)
        nu_i_sm = exp_nevents.expected_events_binned(np.zeros(len(c)), self.bins, self.path_output).astype(int)
        nu_i = {'sm': nu_i_sm, 'eft': nu_i_eft}
        return nu_i

    def find_pdf_binned_mc(self, hypothesis):
        """ Construct a histogram of the distribution of the binned test statistic using mc sampling.

        Parameters
        ----------
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

        n_tc = 10000
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

        Parameters
        ----------
        nu_i: dictionary with expected number of entries in bin i under the SM and the EFT

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

    def find_bound_binned_mc(self):

        mean_tc_binned_sm, std_tc_binned_sm, tc_data_sm = self.find_pdf_binned_mc(hypothesis='sm')
        mean_tc_binned_eft, std_tc_binned_eft, tc_data_eft = self.find_pdf_binned_mc(hypothesis='eft')
        z_score_binned = (mean_tc_binned_sm - mean_tc_binned_eft) / std_tc_binned_eft

        mean = {'sm': mean_tc_binned_sm, 'eft': mean_tc_binned_eft}
        std = {'sm': std_tc_binned_sm, 'eft': std_tc_binned_eft}
        tc_data = {'sm': tc_data_sm, 'eft': tc_data_eft}

        # with open(os.path.join(path_output, "z_scores_cug_check_v2.dat"), "a") as f:
        #     #f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.z_score_binned) + "\t" + str(z_score_binned_unc) + "\n")
        #     f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(z_score_binned) + "\n")

        return mean, std, tc_data, z_score_binned

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

    def p_value_asimov(self):
        z_score = (self.mean_tc_asi['sm'] - self.mean_tc_asi['eft']) / self.std_tc_asi['eft']
        p_value = 1 - norm.cdf(z_score)
        return z_score, p_value

    def plot_tc_binned(self, c):

        self.nu_i = self.expected_entries(c)
        self.mean_tc_binned_mc, self.std_tc_binned_mc, self.tc_data, self.z_score_binned_mc = self.find_bound_binned_mc()
        self.mean_tc_asi, self.std_tc_asi = self.find_pdf_binned_asimov()

        x = np.linspace(self.mean_tc_asi['eft'] - 4*self.std_tc_asi['eft'], self.mean_tc_asi['sm'] + 4*self.std_tc_asi['sm'], 400)
        tc_asi_eft = gauss(x, self.mean_tc_asi['eft'], self.std_tc_asi['eft'])
        tc_asi_sm = gauss(x, self.mean_tc_asi['sm'], self.std_tc_asi['sm'])

        plt.figure(figsize=(10, 6))
        ax = plt.subplot(111)
        ax.hist(self.tc_data['eft'], bins=80, label=r'$\rm{EFT\;(MC)}$', density=True, color='C0', alpha=0.5)
        ax.hist(self.tc_data['sm'], bins=80, label=r'$\rm{SM\;(MC)}$', density=True, color='C1', alpha=0.5)
        ax.plot(x, tc_asi_eft, label=r'$\rm{Asimov\;(EFT)}$', color='C0')
        ax.plot(x, tc_asi_sm, label=r'$\rm{Asimov\;(SM)}$', color='C1')
        ax.set_xlabel(r'$t_c$', fontsize=20)
        ax.set_title(r'$\rm{Asymptotic\;distribution\;for\;binned\;analysis}$', fontsize=20)
        ax.legend(loc='best', fontsize=15, frameon=False)
        plt.tight_layout()


        z_score = (self.mean_tc_asi['sm']-self.mean_tc_asi['eft'])/self.std_tc_asi['eft']
        #ax.text(0.15, 0.9, r'$\rm{z-score} = %.3f$' % z_score, fontsize=20, transform=ax.transAxes)
        plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/tc_dist.pdf')

    def find_pdf(self, c, nn, path_eft, result_path):
        """
        Given the eft parameter(s) c, this function computes the mean and standard deviation of pdf(tc) under both
        the SM and the EFT. It uses the analytical likelihood ratio.
        :param c: nd_array that specifies the point in eft parameter space
        """

        # compute the expected number of events given the eft param c
        expected_eft = exp_nevents.expected_nevents(c)
        expected_sm = exp_nevents.expected_nevents(np.zeros(len(c)))

        # generate samples with mg5 if not yet available and store them at path.
        #path = generate_samples(c)

        path_sm = '/data/theorie/jthoeve/ML4EFT/quad_clas/sm_events.lhe'

        # load the lhe file and construct a data set
        #write_log("loading eft data")
        n = int(1e5) # total number of events
        s = int(1e4) # size of subset
        data_eft = load_data(path_eft, n, s)
        #write_log("eft data loaded")
        data_sm = load_data(path_sm, n, s)
        #write_log("sm data loaded")

        data_eft = data_eft * 10 ** -3
        data_sm = data_sm * 10 ** -3

        # compute the mean and std. dev. of the pdf(tc) under either the sm or the eft

        if nn:  # mean_tc_eft.shape = (nn_rep, )
            self.mean_tc_eft, self.sigma_tc_eft = get_tc_nn(expected_eft, expected_sm, data_eft, c,
                                                            hypothesis='eft')
            #write_log("mean and std of tc under eft computed")
            self.mean_tc_sm, self.sigma_tc_sm = get_tc_nn(expected_eft, expected_sm, data_sm, c,
                                                          hypothesis='sm')
            #write_log("mean and std of tc under sm computed")
        else:  # mean_tc_eft.shape = (1, )
            self.mean_tc_eft, self.sigma_tc_eft, self.mean_tauc_eft = get_tc(expected_eft, expected_sm, data_eft, c,
                                                                             hypothesis='eft')
            #write_log("mean and std of tc under eft computed")
            self.mean_tc_sm, self.sigma_tc_sm, self.mean_tauc_sm = get_tc(expected_eft, expected_sm, data_sm, c,
                                                                          hypothesis='sm')
            #write_log("mean and std of tc under sm computed")

        # given the mean and std. dev. the z-score can be computed
        self.z_score = (self.mean_tc_sm - self.mean_tc_eft) / self.sigma_tc_eft

        if nn:
            with open(os.path.join(result_path, "z_scores_pdiag.dat"), "a") as f:
                #  write the mean and stand. dev. taken over the nn_rep to a file
                f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(np.mean(self.z_score)) + "\t" + str(np.std(self.z_score)) + "\n")
            # with open(os.path.join(result_path, "tc_eft.dat"), "a") as f:
            #     #  write the mean and stand. dev. taken over the nn_rep to a file
            #     f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.mean_tc_eft) + "\t" + str(self.sigma_tc_eft) + "\n")
            # with open(os.path.join(result_path, "tc_sm.dat"), "a") as f:
            #     #  write the mean and stand. dev. taken over the nn_rep to a file
            #     f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.mean_tc_sm) + "\t" + str(self.sigma_tc_sm) + "\n")
        else:
            with open(os.path.join(result_path, "z_scores_pdiag.dat"), "a") as f:
                f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.z_score) + "\n")
            # with open(os.path.join(result_path, "tc_eft.dat"), "a") as f:
            #     #  write the mean and stand. dev. taken over the nn_rep to a file
            #     f.write(str(expected_eft) + "\t" + str(expected_sm) + "\t" + str(self.mean_tc_eft) + "\t" + str(self.mean_tauc_eft) + "\t" + str(self.sigma_tc_eft) + "\n")
            # with open(os.path.join(result_path, "tc_sm.dat"), "a") as f:
            #     #  write the mean and stand. dev. taken over the nn_rep to a file
            #     f.write(str(expected_eft) + "\t" + str(expected_sm) + "\t" + str(self.mean_tc_sm) + "\t" + str(self.mean_tauc_sm) + "\t" + str(self.sigma_tc_sm) + "\n")



def gauss(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))


if __name__ == '__main__':

    truth = False
    NN = False
    binned = True
    data_loaded = True


    #bins = np.arange(300, 4100, 100)

    eft_points_mcuu = [[0, -0.40], [0, -0.45], [0, -0.50], [0, -0.55], [0, -0.60], [0, -0.65], [0, -0.70],
                  [0, -0.75], [0, -0.80]]
        # , [-0.85, 0], [-0.90, 0], [-0.95, 0], [-1.00, 0], [-1.05, 0],
        #           [-1.10, 0], [-1.15, 0], [-1.20, 0], [-1.25, 0], [-1.30, 0], [-1.35, 0], [-1.40, 0]]

    eft_points_pcug = [[0.01, 0], [0.05, 0], [0.1, 0], [0.3, 0]]

    eft_points_ncug = [[-0.075, 0], [-0.10, 0], [-0.125, 0]]

    eft_point_pdiag = [[0.02, 0.1], [0.04, 0.2], [0.06, 0.3]]

    # choice of binning
    bin_1 = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 4000])
    bin_2 = np.array([300, 400, 500, 600, 4000])
    bin_3 = np.array([300, 4000])

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