import pylhe
import numpy as np
import subprocess
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
import sys, os
from scipy.stats import norm

from quad_classifier_cluster import EventDataset
import xsec_cluster as ExS
import expected_events as exp_nevents
import analyse
import torch

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)


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

    def __init__(self, c, nn, path_eft_lhe, path_output, bins=None):
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
            self.find_bound_binned(c, path_eft_lhe, path_output, bins)

    def find_pdf_binned(self, c, path_eft, path_output, bins, hypothesis):

        path_sm = '/data/theorie/jthoeve/ML4EFT/quad_clas/sm_events.lhe'

        # expected number of events that fall into each bin at the specified eft coefficient c
        n_exp_eft = exp_nevents.expected_events_binned(c, bins, path_output).astype(int)
        n_exp_sm = exp_nevents.expected_events_binned(np.zeros(len(c)), bins, path_output).astype(int)

        # total number of expected events is found by taking the sum over the binned expected countings
        expected_eft = np.sum(n_exp_eft)
        expected_sm = np.sum(n_exp_sm)

        n = 100000 # number of events to be loaded
        event_data_tot = load_data(path_eft, n, s=n) if hypothesis == 'eft' else load_data(path_sm, n, s=n)

        n_tc = 1000
        tc_data = []
        for i in range(n_tc):
            # total number of expected events
            n_exp_tot = expected_eft if hypothesis == 'eft' else expected_sm

            # the size of the dataset is drawn from a Poisson dist with mean n_exp_tot
            size_dataset = np.random.poisson(n_exp_tot, 1)

            # draw size_dataset events at random
            event_data = np.random.choice(event_data_tot, size=size_dataset, replace=False)

            # find how many events fall into each bin
            n_i, _ = np.histogram(event_data, bins=bins)

            tc = expected_eft - expected_sm - np.sum(n_i*np.log(n_exp_eft/n_exp_sm))
            tc_data.append(tc)
        tc_data = np.array(tc_data)

        # find mean and variance of tc dist
        mean_tc_binned = np.mean(tc_data)
        std_tc_binned = np.std(tc_data)
        return mean_tc_binned, std_tc_binned

    def find_bound_binned(self, c, path_eft_lhe, path_output, bins):

        self.mean_tc_binned_sm, self.std_tc_binned_sm = self.find_pdf_binned(c, path_eft_lhe, path_output, bins, hypothesis='sm')
        self.mean_tc_binned_eft, self.std_tc_binned_eft = self.find_pdf_binned(c, path_eft_lhe, path_output, bins, hypothesis='eft')
        self.z_score_binned = (self.mean_tc_binned_sm - self.mean_tc_binned_eft) / self.std_tc_binned_eft
        print(self.z_score_binned, self.mean_tc_binned_sm, self.mean_tc_binned_eft, self.std_tc_binned_eft)

        with open(os.path.join(path_output, "z_scores.dat"), "a") as f:
            f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.z_score_binned) + "\n")

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
        write_log("loading eft data")
        n = int(1e5) # total number of events
        s = int(1e4) # size of subset
        data_eft = load_data(path_eft, n, s)
        write_log("eft data loaded")
        data_sm = load_data(path_sm, n, s)
        write_log("sm data loaded")

        data_eft = data_eft * 10 ** -3
        data_sm = data_sm * 10 ** -3

        # compute the mean and std. dev. of the pdf(tc) under either the sm or the eft

        if nn:  # mean_tc_eft.shape = (nn_rep, )
            self.mean_tc_eft, self.sigma_tc_eft = get_tc_nn(expected_eft, expected_sm, data_eft, c,
                                                            hypothesis='eft')
            write_log("mean and std of tc under eft computed")
            self.mean_tc_sm, self.sigma_tc_sm = get_tc_nn(expected_eft, expected_sm, data_sm, c,
                                                          hypothesis='sm')
            write_log("mean and std of tc under sm computed")
        else:  # mean_tc_eft.shape = (1, )
            self.mean_tc_eft, self.sigma_tc_eft, self.mean_tauc_eft = get_tc(expected_eft, expected_sm, data_eft, c,
                                                                             hypothesis='eft')
            write_log("mean and std of tc under eft computed")
            self.mean_tc_sm, self.sigma_tc_sm, self.mean_tauc_sm = get_tc(expected_eft, expected_sm, data_sm, c,
                                                                          hypothesis='sm')
            write_log("mean and std of tc under sm computed")

        # given the mean and std. dev. the z-score can be computed
        self.z_score = (self.mean_tc_sm - self.mean_tc_eft) / self.sigma_tc_eft

        if nn:
            # with open(os.path.join(result_path, "z_scores.dat"), "a") as f:
            #     #  write the mean and stand. dev. taken over the nn_rep to a file
            #     f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(np.mean(self.z_score)) + "\t" + str(np.std(self.z_score)) + "\n")
            with open(os.path.join(result_path, "tc_eft.dat"), "a") as f:
                #  write the mean and stand. dev. taken over the nn_rep to a file
                f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.mean_tc_eft) + "\t" + str(self.sigma_tc_eft) + "\n")
            with open(os.path.join(result_path, "tc_sm.dat"), "a") as f:
                #  write the mean and stand. dev. taken over the nn_rep to a file
                f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.mean_tc_sm) + "\t" + str(self.sigma_tc_sm) + "\n")
        else:
            # with open(os.path.join(result_path, "z_scores.dat"), "a") as f:
            #     f.write(str(c[0]) + "\t" + str(c[1]) + "\t" + str(self.z_score) + "\n")
            with open(os.path.join(result_path, "tc_eft.dat"), "a") as f:
                #  write the mean and stand. dev. taken over the nn_rep to a file
                f.write(str(expected_eft) + "\t" + str(expected_sm) + "\t" + str(self.mean_tc_eft) + "\t" + str(self.mean_tauc_eft) + "\t" + str(self.sigma_tc_eft) + "\n")
            with open(os.path.join(result_path, "tc_sm.dat"), "a") as f:
                #  write the mean and stand. dev. taken over the nn_rep to a file
                f.write(str(expected_eft) + "\t" + str(expected_sm) + "\t" + str(self.mean_tc_sm) + "\t" + str(self.mean_tauc_sm) + "\t" + str(self.sigma_tc_sm) + "\n")


def gauss(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))


if __name__ == '__main__':

    truth = True
    NN = False
    binned = False
    data_loaded = True


    #bins = np.arange(300, 4100, 100)

    # choice of binning
    bin_1 = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 4000])
    bin_2 = np.array([300, 400, 500, 600, 4000])
    bin_3 = np.array([300, 4000])
    # bin_5 = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 4000])
    # bin_6 = np.append(np.arange(300, 1810, 10), 4000)

    bins = bin_3


    # the below is only needed for a binned analysis
    # fit the cross section per bin as a function of c
    if not data_loaded:
        exp_nevents.xsec_binned(bins, '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3')

    ####### TRUTH #########
    if truth is True:
        # StatAnalysis(np.array([0, 0.25]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_025.lhe',
        #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth',
        #              bins=None)
        StatAnalysis(np.array([0, 0.50]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth',
                     bins=None)
        # StatAnalysis(np.array([0, 0.75]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
        #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth',
        #              bins=None)
        # StatAnalysis(np.array([0, 0.87]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
        #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth',
        #              bins=None)
        # StatAnalysis(np.array([0, 1.0]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
        #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth',
        #              bins=None)
        # StatAnalysis(np.array([0, 2.0]), nn=False,
        #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_20.lhe',
        #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth',
        #              bins=None)

    ####### NN #########
    if NN is True:
        StatAnalysis(np.array([0, 0.25]), nn=True,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_025.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn',
                     bins=None)
        StatAnalysis(np.array([0, 0.50]), nn=True,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn',
                     bins=None)
        StatAnalysis(np.array([0, 0.75]), nn=True,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn',
                     bins=None)
        StatAnalysis(np.array([0, 0.87]), nn=True,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn',
                     bins=None)
        StatAnalysis(np.array([0, 1.0]), nn=True,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn',
                     bins=None)
        StatAnalysis(np.array([0, 2.0]), nn=True,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_20.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn',
                     bins=None)

    ####### BINNED #########
    if binned is True:
        StatAnalysis(np.array([0, 0.25]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_025.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3',
                     bins=bins)
        StatAnalysis(np.array([0, 0.50]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3',
                     bins=bins)
        StatAnalysis(np.array([0, 0.75]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3',
                     bins=bins)
        StatAnalysis(np.array([0, 0.87]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3',
                     bins=bins)
        StatAnalysis(np.array([0, 1.0]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3',
                     bins=bins)
        StatAnalysis(np.array([0, 2.0]), nn=False,
                     path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_20.lhe',
                     path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_3',
                     bins=bins)


    # StatAnalysis(np.array([0, 0.50]), nn=False,
    #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_05.lhe',
    #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_6',
    #              bins=bin_6)
    #
    # StatAnalysis(np.array([0, 0.75]), nn=False,
    #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_075.lhe',
    #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_6',
    #              bins=bin_6)
    #
    # StatAnalysis(np.array([0, 0.87]), nn=False,
    #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_087.lhe',
    #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_6',
    #              bins=bin_6)
    #
    # StatAnalysis(np.array([0, 1.0]), nn=False,
    #              path_eft_lhe='/data/theorie/jthoeve/ML4EFT/quad_clas/eft_10.lhe',
    #              path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_6',
    #              bins=bin_6)

