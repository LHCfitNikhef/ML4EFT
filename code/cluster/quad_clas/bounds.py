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

def generate_samples(c, i):
    cugre = c[0]
    cuu = c[1]
    subprocess.call(['chmod', '+x', '/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh'])
    subprocess.call(["/data/theorie/jthoeve/ML4EFT/quad_clas/generate_samples.sh", '{}'.format(cugre), '{}'.format(cuu),
                     '{}'.format(i + 1)])


def get_events(c):
    """
    Load the MC events
    :param c:
    :param hypothesis:
    :return:
    """

    path_dict = {}
    for i in range(len(eft_points)):
        ctg, cuu = eft_points[i]
        path_to_data_eft = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_{process}/bin/process_{process}/Events/run_{mc_run}/unweighted_events.lhe'.format(
            process=i, mc_run=str(0) + str(1))
        path_dict[(ctg, cuu)] = path_to_data_eft

    n_dat = 1000

    if np.all((c == 0)):
        path_dict = {(0,
                      0): '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_18/bin/process_18/Events/run_01/unweighted_events.lhe'}

    events = EventDataset(tuple(c), 1, path_dict=path_dict, n_dat=n_dat)
    return events.event_data


def get_tc(expected_eft, expected_sm, data, c, hypothesis):
    cug, cuu = c
    data = np.array(data)
    mtt = data[:, 0] * 10 ** -3
    dsigma_dmtt_eft = np.array([ExS.dsigma_dmtt(mtt_i, cug, cuu) for mtt_i in mtt])
    dsigma_dmtt_sm = np.array([ExS.dsigma_dmtt(mtt_i, 0, 0) for mtt_i in mtt])

    r_c = dsigma_dmtt_eft / dsigma_dmtt_sm
    tau_c = np.log(r_c)
    mean_tauc = np.mean(tau_c)
    mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc if hypothesis == 'sm' else expected_eft - expected_sm - expected_eft * mean_tauc
    sigma_tc = np.sqrt(expected_eft * np.mean(tau_c ** 2)) if hypothesis == 'eft' else np.sqrt(
        expected_sm * np.mean(tau_c ** 2))
    return mean_tc, sigma_tc


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

    def __init__(self, c, nn):
        self.mean_tc_eft = None
        self.sigma_tc_eft = None
        self.mean_tc_sm = None
        self.sigma_tc_sm = None
        self.z_score = None
        if nn:
            self.find_pdf_nn(c)
        else:
            self.find_pdf(c)

    def find_pdf(self, c):
        expected_eft = exp_nevents.expected_nevents(c)
        expected_sm = exp_nevents.expected_nevents(np.zeros(len(c)))
        # TODO: the expected number of events only translates the two gaussians by the same amount, so as far as determining CL bounds these terms can be dropped

        # generate_samples(c, i)

        data_eft = get_events(c)
        data_sm = get_events(np.zeros(len(c)))

        self.mean_tc_eft, self.sigma_tc_eft = get_tc(expected_eft, expected_sm, data_eft, c, hypothesis='eft')
        self.mean_tc_sm, self.sigma_tc_sm = get_tc(expected_eft, expected_sm, data_sm, c, hypothesis='sm')
        self.z_score = (self.mean_tc_sm - self.mean_tc_eft) / self.sigma_tc_eft
        print("EFT: ", "Mean = {}, Std = {}".format(self.mean_tc_eft, self.sigma_tc_eft))
        print("SM: ", "Mean = {}, Std = {}".format(self.mean_tc_sm, self.sigma_tc_sm))
        print("z-score = {}".format(self.z_score))

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


def gauss(x, mean, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mean) ** 2 / (2 * sigma ** 2))


if __name__ == '__main__':

    datasets = []
    for param in eft_points:
        eft_params = np.array([param[0], param[1]])
        datasets.append(StatAnalysis(eft_params, nn=False))

    datasets_nn = []
    for param in eft_points:
        eft_params = np.array([param[0], param[1]])
        datasets_nn.append(StatAnalysis(eft_params, nn=True))

    z_score = [dataset.z_score for dataset in datasets]
    mean_sm = [dataset.mean_tc_sm for dataset in datasets]
    mean_eft = [dataset.mean_tc_eft for dataset in datasets]
    std_sm = [dataset.sigma_tc_sm for dataset in datasets]
    std_eft = [dataset.sigma_tc_eft for dataset in datasets]

    z_score_nn = [dataset.z_score for dataset in datasets_nn]
    mean_sm_nn = np.array([dataset.mean_tc_sm for dataset in datasets_nn])
    mean_eft_nn = np.array([dataset.mean_tc_eft for dataset in datasets_nn])
    std_sm_nn = np.array([dataset.sigma_tc_sm for dataset in datasets_nn])
    std_eft_nn = np.array([dataset.sigma_tc_eft for dataset in datasets_nn])

    fig = plt.figure(figsize=(1 * 10, 1 * 8))
    for i in range(1, len(z_score) + 1):
        plt.subplot(1, 1, i)
        x = np.linspace(mean_eft[i - 1] - 3 * std_eft[i - 1], mean_sm[i - 1] + 3 * std_sm[i - 1], 100)
        tc_eft = gauss(x, mean_eft[i - 1], std_eft[i - 1])
        tc_sm = gauss(x, mean_sm[i - 1], std_sm[i - 1])

        # x_nn = np.linspace(mean_eft_nn[i - 1] - 3 * std_eft_nn[i - 1], mean_sm_nn[i - 1] + 3 * std_sm_nn[i - 1], 100)
        # tc_eft_nn = gauss(x, mean_eft_nn[i-1], std_eft[i-1])

        tc_sm_nn = np.array([gauss(x, mean_sm_nn[i - 1, j], std_sm_nn[i - 1, j]) for j in range(mean_sm_nn.shape[1])])
        tc_sm_nn_median = np.median(tc_sm_nn, axis=0)
        tc_sm_nn_std = np.std(tc_sm_nn, axis=0)

        tc_eft_nn = np.array(
            [gauss(x, mean_eft_nn[i - 1, j], std_eft_nn[i - 1, j]) for j in range(mean_eft_nn.shape[1])])
        tc_eft_nn_median = np.median(tc_eft_nn, axis=0)
        tc_eft_nn_std = np.std(tc_eft_nn, axis=0)

        # print(np.std(tc_eft_nn, axis=1).shape, x_nn.shape)

        plt.fill_between(x, tc_sm_nn_median + tc_sm_nn_std, tc_sm_nn_median - tc_sm_nn_std, color='red', alpha=.5)
        plt.fill_between(x, tc_eft_nn_median + tc_eft_nn_std, tc_eft_nn_median - tc_eft_nn_std, color='green', alpha=.5)

        #print(x.shape, tc_sm_nn_median.shape, tc_sm_nn_std.shape)

        plt.plot(x, tc_sm, label='sm')
        plt.plot(x, tc_eft, label='eft')
        plt.fill_between(x, tc_eft, 0, where=x >= mean_sm[i - 1], color='b', alpha=.5)
        plt.title(r'\rm{z = }' + r'{0:.2f} '.format(z_score[i-1]) + r'\rm ctg = {} '.format(eft_points[i-1][0]) + r'\rm cuu = {} '.format(eft_points[i-1][1]))
        plt.legend()
        plt.xlabel(r'$t_c$')

    plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/test8.pdf')

    # plt.plot(cugre, z_score)
    # plt.show()
    # print(z_score)
    # generate_samples(eft_params)
