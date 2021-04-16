import pylhe
import numpy as np
from matplotlib import pyplot as plt

from quad_classifier_cluster import EventDataset
import xsec_cluster as ExS


def get_events(c):
    """
    Load the MC events
    :param c:
    :param hypothesis:
    :return:
    """
    n_dat = 10000
    if c == (0, 0):
        path_dict = {(0,
                         0): '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_18/bin/process_18/Events/run_01/unweighted_events.lhe'}
    else:
        path_dict = {c: '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_0/bin/process_0/Events/run_01/unweighted_events.lhe'}

    events = EventDataset(c, path_dict=path_dict, n_dat=n_dat)
    return events.event_data


def get_tc(expected_eft, expected_sm, data, c, hypothesis):
    cug, cuu = c
    data = np.array(data)
    mtt = data[:, 0]*10**-3
    dsigma_dmtt_eft = np.array([ExS.dsigma_dmtt(mtt_i, cug, cuu) for mtt_i in mtt])
    dsigma_dmtt_sm = np.array([ExS.dsigma_dmtt(mtt_i, 0, 0) for mtt_i in mtt])

    r_c = dsigma_dmtt_eft / dsigma_dmtt_sm
    tau_c = np.log(r_c)
    mean_tauc = np.mean(tau_c)
    mean_tc = expected_eft - expected_sm - expected_sm * mean_tauc if hypothesis=='sm' else expected_eft - expected_sm - expected_eft * mean_tauc
    sigma_tc = np.sqrt(expected_eft*np.mean(tau_c**2)) if hypothesis=='eft' else np.sqrt(expected_sm*np.mean(tau_c**2))
    return mean_tc, sigma_tc


def get_nevents(c):
    #TODO: find number of expected events under both hypotheses
    return 1


class StatAnalysis:

    def __init__(self, c):
        self.mean_tc_eft = None
        self.sigma_tc_eft = None
        self.mean_tc_sm = None
        self.sigma_tc_sm = None
        self.find_pdf(c)

    def find_pdf(self, c):
        expected_eft = get_nevents(c)
        expected_sm = get_nevents((0,0))
        # TODO: the expected number of events only translates the two gaussians by the same amount, so as far as determining CL bounds these terms can be dropped

        data_eft = get_events(c)
        data_sm = get_events((0, 0))

        self.mean_tc_eft, self.sigma_tc_eft = get_tc(expected_eft, expected_sm, data_eft, c, hypothesis='eft')
        self.mean_tc_sm, self.sigma_tc_sm = get_tc(expected_eft, expected_sm, data_sm, c, hypothesis='sm')
        print("EFT: ", "Mean = {}, Std = {}".format(self.mean_tc_eft, self.sigma_tc_eft))
        print("SM: ", "Mean = {}, Std = {}".format(self.mean_tc_sm, self.sigma_tc_sm))


if __name__ == '__main__':
    eft_params = (1, 1)
    bounds = StatAnalysis(eft_params)
