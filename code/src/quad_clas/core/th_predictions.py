import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os
from quad_clas.core.truth import vh_prod

class TheoryPred:
    """
    The theory prediction class that provides the theory predictions in the SMEFT

    Parameters
    ----------
    coeff: array-like
        Array of SMEFT coefficient names
    bins: array-like
        Array with bin edges
    event_path: str
        path to event files
    nreps: int, optional
        Number of replicas to use, 50 by default. The SMEFT predictions are averages over the replicas.
    """

    def __init__(self, coeff, event_path, nreps=50, bins=None, kinematic=None):

        self.coeff = coeff
        if bins is None:
            self.bins = [0, 4]
        else:
            self.bins = bins

        self.kinematic = kinematic

        self.event_path = event_path
        self.nreps = nreps
        self.df = None

        self.predictions()

    def read_param_value(self, wc):
        """
        Function to read parameter value from param card

        Parameters
        ----------
        wc: str
            EFT coefficient

        Returns
        -------
        param: float
            Value of the EFT coefficient in the param card
        """

        #TODO: regular expression does not select wilson coefficients that end with a number

        # filename = os.path.join(self.event_path, 'lin', wc, 'param_card.dat')
        # match_number = re.compile('[-+]?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?')

        # with open(filename, 'r') as f:
        #     data = f.readlines()
        #     f.close()
        #
        # for line in data:
        #     if wc + ' \n' in line or wc + '\n' in line:
        #         final_list = [float(x) for x in re.findall(match_number, line)]
        #         param = float(final_list[-1])
        #         break
        return 10
        #
        # with open(filename, 'r') as f:
        #     data = f.readlines()
        #     f.close()
        # for line, next_line in zip(data, data[1:] + [data[0]]):
        #     if 'Block smeft' in line:
        #         final_list = [float(x) for x in re.findall(match_number, next_line)]
        #         param = float(final_list[-1])
        #         break
        # return param

    def predictions(self):
        nbins = np.size(self.bins) - 1

        predictions = dict()

        # SM predictions
        SMpredictions = np.zeros((self.nreps, nbins))
        for mcrep in np.arange(self.nreps):
            df_path = os.path.join(self.event_path, 'sm/events_{}.pkl.gz'.format(mcrep))
            df = pd.read_pickle(df_path)

            if self.kinematic is None:
                self.kinematic = df.columns.values[0]

            sigma = df[self.kinematic][0]
            nevents = np.size(df[self.kinematic]) - 1
            n, bins, patches = plt.hist(x=df[self.kinematic][1:], bins=self.bins)
            SMpredictions[mcrep, :] = n * sigma / nevents

        predictions['sm'] = np.average(SMpredictions, axis=0)

        # SMEFT predictions
        for coeff in self.coeff:
            EFTpredictions = np.zeros((self.nreps, nbins))
            for mcrep in np.arange(self.nreps):
                # Read dataframe and WC value
                df_path = os.path.join(self.event_path, 'lin/{}/events_{}.pkl.gz'.format(coeff, str(mcrep)))
                df = pd.read_pickle(df_path)
                wc = self.read_param_value(coeff)

                # Get total cross section and number of generated events
                sigma = df[self.kinematic][0]
                nevents = np.size(df[self.kinematic]) - 1

                n, bins, patches = plt.hist(x=df[self.kinematic][1:], bins=bins)
                sigma_EFT = n * sigma / nevents

                sigma_1 = (1. / wc) * (sigma_EFT - predictions['sm'])
                EFTpredictions[mcrep, :] = sigma_1

            predictions[coeff] = np.average(EFTpredictions, axis=0)

        bin_index = ['Bin ' + str(s + 1) for s in np.arange(nbins)]
        self.df = pd.DataFrame(predictions, index=bin_index).T

    def compute_diff_coefficients(self, observed_data):

        # TODO: generalise to arbitary processes

        # diff xsec
        dsigma_dx_sm = np.array(
            [vh_prod.dsigma_dmvh_dy_dpt(row['y'], row['m_zh'], row['pt_z'], 0, 0, lin=True, quad=False) for index, row in
             observed_data.iterrows()])

        # TODO: generalise to arbirtrary wilson coefficients
        dsigma_dx_c1 = np.array(
            [vh_prod.dsigma_dmvh_dy_dpt(row['y'], row['m_zh'], row['pt_z'], 10, 0, lin=True, quad=False) for index, row in
             observed_data.iterrows()])

        dsigma_dx_c1 = (dsigma_dx_c1 - dsigma_dx_sm) / 10

        dsigma_dx_c2 = np.array(
            [vh_prod.dsigma_dmvh_dy_dpt(row['y'], row['m_zh'], row['pt_z'], 0, 10, lin=True, quad=False) for index, row in
             observed_data.iterrows()])

        dsigma_dx_c2 = (dsigma_dx_c2 - dsigma_dx_sm) / 10

        dsigma_dx_eft = {'lin': np.stack((dsigma_dx_c1, dsigma_dx_c2))}

        return dsigma_dx_sm, dsigma_dx_eft

