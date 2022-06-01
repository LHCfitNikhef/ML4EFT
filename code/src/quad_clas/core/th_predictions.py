import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os
from quad_clas.core.truth import vh_prod, tt_prod

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

    def __init__(self, coeff, event_path, HOcorrections, bins=None, kinematic=None):

        self.coeff = coeff
        if bins is None:
            #self.bins = [0, 4]
            self.bins = [0, 4000]
        else:
            self.bins = bins

        self.kinematic = kinematic

        self.event_path = event_path
        self.df = None
        self.HOcorrections = HOcorrections


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
        return 10
        # filename = os.path.join(self.event_path, 'lin', wc, 'param_card.dat')
        # match_number = re.compile('[-+]?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?')
        #
        # with open(filename, 'r') as f:
        #     data = f.readlines()
        #     f.close()
        #
        # for line in data:
        #     if wc + ' \n' in line or wc + '\n' in line:
        #         final_list = [float(x) for x in re.findall(match_number, line)]
        #         param = float(final_list[-1])
        #         break
        #
        # return param


    def predictions(self):
        nbins = np.size(self.bins) - 1

        predictions = dict()

        # SM predictions
        SMpredictions = []

        base_dir_sm = os.path.join(self.event_path, 'sm')
        for df_path_rep in os.listdir(base_dir_sm):
            if not df_path_rep.startswith('events'):
                continue

            df = pd.read_pickle(os.path.join(base_dir_sm, df_path_rep))

            if self.kinematic is None:
                self.kinematic = df.columns.values[0]

            sigma = df.iloc[0, 0]
            events = df.iloc[1:, :]
            n_events = len(events)
            n, _ = np.histogram(events[self.kinematic], bins=self.bins)
            SMpredictions.append(n * sigma / n_events)

        predictions['sm'] = np.average(SMpredictions, axis=0)

        # linear predictions

        for coeff in self.coeff:
            base_dir = os.path.join(self.event_path, 'lin', coeff)

            EFTpredictions = []
            for df_path_rep in os.listdir(base_dir):
                if not df_path_rep.startswith('events'):
                    continue

                df = pd.read_pickle(os.path.join(base_dir, df_path_rep))

                sigma = df.iloc[0,0]
                events = df.iloc[1:, :]

                wc = self.read_param_value(coeff)

                n_events = len(events)

                n, _ = np.histogram(events[self.kinematic], bins=self.bins)

                sigma_EFT = n * sigma / n_events

                sigma_lin = (1. / wc) * (sigma_EFT - predictions['sm'])

                EFTpredictions.append(sigma_lin)

            predictions[coeff] = np.average(EFTpredictions, axis=0)

        #predictions['cuu'] = 0

        # quadratic predictions
        if self.HOcorrections:
            for coeff in self.coeff:
                base_dir = os.path.join(self.event_path, 'quad', coeff)

                EFTpredictions = []
                for df_path_rep in os.listdir(base_dir):
                    if not df_path_rep.startswith('events'):
                        continue

                    df = pd.read_pickle(os.path.join(base_dir, df_path_rep))

                    sigma = df.iloc[0,0]
                    events = df.iloc[1:, :]

                    wc = self.read_param_value(coeff)

                    n_events = len(events)

                    n, _ = np.histogram(events[self.kinematic], bins=self.bins)

                    sigma_EFT = n * sigma / n_events

                    sigma_quad = (1. / wc ** 2) * (sigma_EFT - predictions['sm'] - wc * predictions[coeff])

                    EFTpredictions.append(sigma_quad)

                predictions[coeff + '*' + coeff] = np.average(EFTpredictions, axis=0)


        bin_index = ['Bin ' + str(s + 1) for s in np.arange(nbins)]
        self.df = pd.DataFrame(predictions, index=bin_index).T



    def compute_diff_coefficients(self, observed_data, process):

        dsigma_dx_sm, dsigma_dx_eft = None, None

        if process == 'ZH':

            dsigma_dx_sm = np.array(
                [vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], 0, 0, lin=True, quad=False) for index, row in
                 observed_data.iterrows()])

            # dsigma_dx_sm = np.array(
            #     [vh_prod.dsigma_dmvh(row['m_zh'], 0, 0, lin=True, quad=False) for index, row
            #      in
            #      observed_data.iterrows()])

            dsigma_dx_c1 = np.array(
                [vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], 10, 0, lin=True, quad=False) for index, row in
                 observed_data.iterrows()])

            dsigma_dx_c1_lin_coef = (dsigma_dx_c1 - dsigma_dx_sm) / 10

            # dsigma_dx_c1 = np.array(
            #     [vh_prod.dsigma_dmvh(row['m_zh'], 10, 0, lin=True, quad=False) for index, row
            #      in
            #      observed_data.iterrows()])

            dsigma_dx_c2 = np.array(
                [vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], 0, 10, lin=True, quad=False) for index, row in
                 observed_data.iterrows()])

            # dsigma_dx_c2 = np.array(
            #     [vh_prod.dsigma_dmvh(row['m_zh'], 0, 10, lin=True, quad=False) for index, row
            #      in
            #      observed_data.iterrows()])

            dsigma_dx_c2_lin_coef = (dsigma_dx_c2 - dsigma_dx_sm) / 10

            dsigma_dx_eft = {'lin': np.stack((dsigma_dx_c1_lin_coef, dsigma_dx_c2_lin_coef))}


        elif process == 'tt':

            dsigma_dx_sm = np.array(
                [tt_prod.dsigma_dmtt(row['m_tt'], 0, 0, lin=True, quad=False) for index, row
                 in
                 observed_data.iterrows()])

            dsigma_dx_c1 = np.array(
                [tt_prod.dsigma_dmtt(row['m_tt'], -10, 0, lin=True, quad=False) for index, row
                 in
                 observed_data.iterrows()])

            dsigma_dx_c1_lin_coef = (dsigma_dx_c1 - dsigma_dx_sm) / -10

            dsigma_dx_c2 = np.array(
                [tt_prod.dsigma_dmtt(row['m_tt'], 0, 10, lin=True, quad=False) for index, row
                 in
                 observed_data.iterrows()])

            dsigma_dx_c2_lin_coef = (dsigma_dx_c2 - dsigma_dx_sm) / 10

            dsigma_dx_c1_quad = np.array(
                [tt_prod.dsigma_dmtt(row['m_tt'], 10, 0, lin=False, quad=True) for index, row
                 in
                 observed_data.iterrows()])

            dsigma_dx_c1_quad_coef = (dsigma_dx_c1_quad - dsigma_dx_sm - 10 * dsigma_dx_c1_lin_coef) / 100

            dsigma_dx_c2_quad = np.array(
                [tt_prod.dsigma_dmtt(row['m_tt'], 0, 10, lin=False, quad=True) for index, row
                 in
                 observed_data.iterrows()])

            dsigma_dx_c2_quad_coef = (dsigma_dx_c2_quad - dsigma_dx_sm - 10 * dsigma_dx_c2_lin_coef) / 100

            dsigma_dx_eft = {'lin': np.stack((dsigma_dx_c1_lin_coef, dsigma_dx_c2_lin_coef)),
                             'quad': np.stack((dsigma_dx_c1_quad_coef, dsigma_dx_c2_quad_coef))}

        return dsigma_dx_sm, dsigma_dx_eft

