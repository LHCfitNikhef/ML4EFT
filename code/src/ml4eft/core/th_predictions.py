import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os
import ml4eft.analyse.analyse as analyse
from ml4eft.core.truth import vh_prod, tt_prod
from collections import defaultdict

class TheoryPred:
    """
    The theory prediction class that provides the theory predictions in the SMEFT

    Parameters
    ----------
    coeff: dict
        Dictionary of EFT parameter names and values corresponding to the event data
    bins: array-like
        Array with bin edges
    event_path: str
        path to event files
    nreps: int, optional
        Number of replicas to use, 50 by default. The SMEFT predictions are averages over the replicas.
    """

    def __init__(self, path_to_theory_pred, kinematic=None, bins=None):

        self.path_to_theory_pred = path_to_theory_pred
        self.bins = bins
        self.kinematic = kinematic
        self.c_names = []
        self.th_dict = defaultdict(dict)

        self.build_theory_pred_df()
        self.c_names_unique = self.get_c_names_unique()

    def build_theory_pred_df(self):
        """
        Construct a theory prediction dictionary
        """

        for order, dict_fo in self.path_to_theory_pred.items():

            if order == 'sm':
                xsec_sm = self.compute_th_pred(path_to_events=dict_fo)
                self.th_dict[order] = xsec_sm
            else:
                for c_name, path_to_events in dict_fo.items():
                    xsec_eft = self.compute_th_pred(path_to_events)

                    # read EFT value at which the events have been generated
                    with open(os.path.join(path_to_events, 'info.txt')) as f:
                        c_value = np.array([int(c) for c in f.read().split()])

                    if order == 'lin':
                        self.th_dict[order][c_name] = (xsec_eft - self.th_dict['sm']) / c_value[0]
                    elif order == 'quad':
                        if 0 in c_value:
                            c_value = np.sum(c_value) ** 2
                        else:
                            c_value = np.prod(c_value)
                        self.th_dict[order][c_name] = (xsec_eft - self.th_dict['sm']) / c_value

                    if c_name not in self.c_names:
                        self.c_names.append(c_name)

    def get_c_names_unique(self):

        c_names = []
        if len(self.c_names) > 0:
            for c_name in self.c_names:
                if '_' in c_name:
                    c_names.extend(c_name.split('_', 1))
                else:
                    c_names.append(c_name)
        c_names = np.array(c_names)
        return np.unique(c_names)


    def compute_th_pred(self, path_to_events):

        # path to events
        events_paths = analyse.Analyse.get_event_paths(path_to_events)

        # store the xsec per bin for all the replicas
        xsec_col = []
        for path in events_paths:
            events, tot_xsec = analyse.Analyse.load_events(event_path=path)

            if self.bins is None:
                xsec_i = tot_xsec
            else:
                n_tot = len(events)
                n_i, _ = np.histogram(events[self.kinematic], self.bins)
                xsec_i = (n_i / n_tot) * tot_xsec

            xsec_col.append(xsec_i)
        xsec_col = np.array(xsec_col)

        return np.mean(xsec_col, axis=0)

    def compute_diff_coefficients(self, optimizer):

        events = optimizer.observed_data
        features = optimizer.th_features
        n_features = len(features)

        if optimizer.process == 'ZH':

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


        elif optimizer.process == 'tt':

            if n_features == 1:
                dsigma_dx = tt_prod.dsigma_dmtt
            if n_features == 2:
                dsigma_dx = tt_prod.dsigma_dmtt_dy
            if n_features == 3:
                dsigma_dx = tt_prod.dsigma_dmtt_dy_dpt

            dsigma_dx_sm = np.array([dsigma_dx(*row[features]) for _, row in events.iterrows()])

            dsigma_dx_c1 = np.array([dsigma_dx(*row[features], [-10, 0], "lin") for _, row
                                     in events.iterrows()])

            # dsigma_dx_c2 = np.array(
            #     [dsigma_dx(*row[features], [0, 10], "lin") for _, row in events.iterrows()])

            dsigma_dx_c1_quad = np.array(
                [dsigma_dx(*row[features], [-10, 0], "quad") for _, row in events.iterrows()])

            dsigma_dx_c2_quad = np.array(
                [dsigma_dx(*row[features], [0, 10], "quad") for _, row in events.iterrows()])

            dsigma_dx_c1_lin_coef = (dsigma_dx_c1 - dsigma_dx_sm) / (-10)

            #dsigma_dx_c2_lin_coef = (dsigma_dx_c2 - dsigma_dx_sm) / 10

            dsigma_dx_c1_quad_coef = (dsigma_dx_c1_quad - dsigma_dx_sm) / 100

            dsigma_dx_c2_quad_coef = (dsigma_dx_c2_quad - dsigma_dx_sm) / 100

            dsigma_dx = {'sm': dsigma_dx_sm,
                         'lin': {'ctGRe': dsigma_dx_c1_lin_coef},
                         'quad': {'ctGRe_ctGRe': dsigma_dx_c1_quad_coef, 'ctu1_ctu1': dsigma_dx_c2_quad_coef}}

        return dsigma_dx

