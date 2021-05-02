import pylhe
import numpy as np
import subprocess
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
import sys

from quad_classifier_cluster import EventDataset
import xsec_cluster as ExS
import expected_events as exp_nevents
import analyse

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)


#eft_points = [[-10.0, 0], [-5.0, 0] , [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0]]#,
#eft_points = [[0, -2.0], [0, -1.0], [0, -0.5], [0, 0.5], [0, 1.0], [0, 2.0]]#, [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],[10.0, 2.0]]
#eft_points = [[-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0], [10.0, 2.0]]
eft_points = [[0, 0.5]]

def generate_samples(c):
    cugre = c[0]
    cuu = c[1]
    subprocess.call(['chmod', '+x', '/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh'])
    subprocess.call(["/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh", '{}'.format(cugre), '{}'.format(cuu)])
    path = "/data/theorie/jthoeve/ML4EFT/mg5_copies/mg5_test/bin/process_0/Events/run_01/unweighted_events.lhe"
    return path


def get_events(c, path=None):
    """
    Load the MC events with eft param c
    :param path:
    :param c:
    :param hypothesis:
    :return:
    """

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
    data = np.array(data)
    mtt = data[:, 0] * 10 ** -3

    network_size = [1, 30, 30, 30, 30, 30, 1]
    r_c = []
    mc_runs = 40
    for i in range(1, mc_runs + 1):
        pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(i)
        mean, std = np.loadtxt(pred_path + '/scaling.dat')
        r_c_i = [analyse.get_likelihood_ratio_NN(pred_path + '/trained_nn.pt', network_size, mtt_i, cug, cuu, mean, std)
                 for mtt_i in mtt]
        r_c.append(r_c_i)
    r_c = np.array(r_c)
    tau_c = np.log(r_c)
    mean_tauc = np.mean(tau_c, axis=1)
    mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc
    sigma_tc = np.sqrt(expected_eft * np.mean(tau_c ** 2, axis=1)) if hypothesis == 'eft' else np.sqrt(
        expected_sm * np.mean(tau_c ** 2, axis=1))
    return mean_tc[:, 0], sigma_tc[:, 0]


class StatAnalysis:
    """
    Construct the pdf of the test statistic tc by using either the NN reconstructed likelihood ratio
    or the analytical likelihood ratio. In the former case, nn should be set to True.
    """

    def __init__(self, c, nn):
        self.mean_tc_eft = None
        self.sigma_tc_eft = None
        self.mean_tc_sm = None
        self.sigma_tc_sm = None
        self.z_score = None
        self.mean_tauc_eft = None
        self.mean_tauc_sm = None
        if nn:
            self.find_pdf_nn(c)
        else:
            self.find_pdf(c)

    def find_pdf(self, c):
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

        # path to eft data (cug = 0, cuu = 0.5)
        path_eft = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_9/bin/process_9/Events/run_06/unweighted_events.lhe'
        # path to sm data
        path_sm = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_18/bin/process_18/Events/run_01/unweighted_events.lhe'

        # load the lhe file and construct a data set
        n = int(1e2) # total number of events
        s = int(1e1) # size of subset
        data_eft = load_data(path_eft, n, s)
        data_sm = load_data(path_sm, n, s)

        data_eft = data_eft * 10 ** -3
        data_sm = data_sm * 10 ** -3

        # compute the mean and std. dev. of the pdf(tc) under either the sm or the eft
        self.mean_tc_eft, self.sigma_tc_eft, self.mean_tauc_eft = get_tc(expected_eft, expected_sm, data_eft, c, hypothesis='eft')
        self.mean_tc_sm, self.sigma_tc_sm, self.mean_tauc_sm = get_tc(expected_eft, expected_sm, data_sm, c, hypothesis='sm')

        # given the mean and std. dev. the z-score can be computed
        self.z_score = (self.mean_tc_sm - self.mean_tc_eft) / self.sigma_tc_eft


        with open("z_score.dat", "a") as f:
            f.write(str(self.z_score) + "\n")

        # print the output
        #print("EFT: ", "Mean = {}, Std = {}".format(self.mean_tc_eft, self.sigma_tc_eft))
        #print("SM: ", "Mean = {}, Std = {}".format(self.mean_tc_sm, self.sigma_tc_sm))
        print("z-score = {}".format(self.z_score))
        print("mean tauc sm = {}".format(self.mean_tauc_sm))
        print("mean tauc eft = {}".format(self.mean_tauc_eft))


    def find_pdf_nn(self, c):
        expected_eft = exp_nevents.expected_nevents(c)
        expected_sm = exp_nevents.expected_nevents(np.zeros(len(c)))
        # TODO: the expected number of events only translates the two gaussians by the same amount, so as far as determining CL bounds these terms can be dropped

        # generate_samples(c, i)

        data_eft = get_events(c)
        data_sm = get_events(np.zeros(len(c)))

        self.mean_tc_eft, self.sigma_tc_eft = get_tc_nn(expected_eft, expected_sm, data_eft, c, hypothesis='eft')
        self.mean_tc_sm, self.sigma_tc_sm = get_tc_nn(expected_eft, expected_sm, data_sm, c, hypothesis='sm')
        self.z_score = (np.mean(self.mean_tc_sm) - np.mean(self.mean_tc_eft)) / np.mean(self.sigma_tc_eft)

        # print("EFT: ", "Mean = {}, Std = {}".format(self.mean_tc_eft, self.sigma_tc_eft))
        # print("SM: ", "Mean = {}, Std = {}".format(self.mean_tc_sm, self.sigma_tc_sm))
        print("z-score = {}".format(self.z_score))


def exp_vs_unexp_check():
    eft_param = np.array([0, 0.5])
    dataset = StatAnalysis(eft_param, nn=False)
    unexpanded = dataset.z_score


def gauss(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))


if __name__ == '__main__':
    #exp_vs_unexp_check()
    StatAnalysis(np.array([0, 0.5]), nn=False)

    # datasets = []
    # for param in eft_points:
    #     eft_params = np.array([param[0], param[1]])
    #     datasets.append(StatAnalysis(eft_params, nn=False))
    #
    # datasets_nn = []
    # for param in eft_points:
    #     eft_params = np.array([param[0], param[1]])
    #     datasets_nn.append(StatAnalysis(eft_params, nn=True))
    #
    # z_score = [dataset.z_score for dataset in datasets]
    # mean_sm = [dataset.mean_tc_sm for dataset in datasets]
    # mean_eft = [dataset.mean_tc_eft for dataset in datasets]
    # std_sm = [dataset.sigma_tc_sm for dataset in datasets]
    # std_eft = [dataset.sigma_tc_eft for dataset in datasets]
    #
    # z_score_nn = [dataset.z_score for dataset in datasets_nn]
    # mean_sm_nn = np.array([dataset.mean_tc_sm for dataset in datasets_nn])
    # mean_eft_nn = np.array([dataset.mean_tc_eft for dataset in datasets_nn])
    # std_sm_nn = np.array([dataset.sigma_tc_sm for dataset in datasets_nn])
    # std_eft_nn = np.array([dataset.sigma_tc_eft for dataset in datasets_nn])
    #
    # fig = plt.figure(figsize=(1 * 10, 1 * 8))
    # for i in range(1, len(z_score) + 1):
    #     plt.subplot(1, 1, i)
    #     x = np.linspace(mean_eft[i - 1] - 3 * std_eft[i - 1], mean_sm[i - 1] + 3 * std_sm[i - 1], 100)
    #     tc_eft = gauss(x, mean_eft[i - 1], std_eft[i - 1])
    #     tc_sm = gauss(x, mean_sm[i - 1], std_sm[i - 1])
    #
    #     # x_nn = np.linspace(mean_eft_nn[i - 1] - 3 * std_eft_nn[i - 1], mean_sm_nn[i - 1] + 3 * std_sm_nn[i - 1], 100)
    #     # tc_eft_nn = gauss(x, mean_eft_nn[i-1], std_eft[i-1])
    #
    #     tc_sm_nn = np.array([gauss(x, mean_sm_nn[i - 1, j], std_sm_nn[i - 1, j]) for j in range(mean_sm_nn.shape[1])])
    #     tc_sm_nn_median = np.median(tc_sm_nn, axis=0)
    #     tc_sm_nn_std = np.std(tc_sm_nn, axis=0)
    #
    #     tc_eft_nn = np.array(
    #         [gauss(x, mean_eft_nn[i - 1, j], std_eft_nn[i - 1, j]) for j in range(mean_eft_nn.shape[1])])
    #     tc_eft_nn_median = np.median(tc_eft_nn, axis=0)
    #     tc_eft_nn_std = np.std(tc_eft_nn, axis=0)
    #
    #     # print(np.std(tc_eft_nn, axis=1).shape, x_nn.shape)
    #
    #     plt.fill_between(x, tc_sm_nn_median + tc_sm_nn_std, tc_sm_nn_median - tc_sm_nn_std, color='red', alpha=.5)
    #     plt.fill_between(x, tc_eft_nn_median + tc_eft_nn_std, tc_eft_nn_median - tc_eft_nn_std, color='green', alpha=.5)
    #
    #     #print(x.shape, tc_sm_nn_median.shape, tc_sm_nn_std.shape)
    #
    #     plt.plot(x, tc_sm, label='sm')
    #     plt.plot(x, tc_eft, label='eft')
    #     plt.fill_between(x, tc_eft, 0, where=x >= mean_sm[i - 1], color='b', alpha=.5)
    #     plt.title(r'\rm{z = }' + r'{0:.2f} '.format(z_score[i-1]) + r'\rm ctg = {} '.format(eft_points[i-1][0]) + r'\rm cuu = {} '.format(eft_points[i-1][1]))
    #     plt.legend()
    #     plt.xlabel(r'$t_c$')
    #
    # plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/test8.pdf')
    #
    # # plt.plot(cugre, z_score)
    # # plt.show()
    # # print(z_score)
    # # generate_samples(eft_params)
