"""Module to compute theory predictions in the SMEFT"""

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
    SMEFT theory calculator
    """

    def __init__(self, path_to_theory_pred, bins=None):
        """
        TheoryPred Constructor

        Parameters
        ----------
        path_to_theory_pred: dict
            Nested dictionary that contains the paths to the events in the SM and the EFT. It
            must be of the form {'sm': ``<path_to_sm_data>``, 'lin': {'c1': ``<path_to_c1_data>``, 'c2': ``<path_to_c2_data>`` },
            'quad': {'c1_c1': ``<path_to_c1_c1_data>``, 'c1_c2': ``<path_to_c1_c1_data>``, 'c2_c2': ``<path_to_c1_c1_data>``}}
        bins: dict, optional
            Dictionary that specifies the binning per kinematic (keys)

        Examples
        --------
        We consider :math:`pp \\rightarrow t\\bar{t} \\rightarrow \\ell^+\\ell^-\\nu_\\ell\\bar{\\nu}_\\ell b\\bar{b}` and compute
        SMEFT theory predictions for :math:`c_{tG}` and :math:`c_{tu}^{(8)}` in the bins :math:`m_{tt}\in[1450, 1500, 1600, 1700, 2000, \infty)` GeV

        Specify the binning (represent infinity by a large number) and initialise a TheoryPred object:

        >>> bins = [1450, 1500, 1600, 1700, 2000, 10000]
        >>> th_predictor = TheoryPred(path_to_theory_pred, kinematic="sqrts_hat", bins=bins)

        SMEFT predictions can now be computed by

        >>> th_predictor.build_theory_pred_df()
        >>> th_predictor.th_dict
        {'sm': array([0.00579859, 0.00844186, 0.00556653, 0.00799101, 0.00446887]), 'lin': {'ctGRe': array([-0.00176097, -0.00260213, -0.00173878, -0.00256058, -0.00140833]), 'ctu8': array([0.00039829, 0.0006311 , 0.00045633, 0.00075374, 0.0005058 ])},
        'quad': {'ctu8_ctu8': array([0.00033827, 0.0005906 , 0.00048487, 0.00100111, 0.00123616]), 'ctGRe_ctGRe': array([0.00090503, 0.00139715, 0.00099753, 0.00164754, 0.0013285 ]), 'ctGRe_ctu8': array([-6.63046602e-05, -1.10171981e-04, -8.56486609e-05, -1.57056872e-04,-1.38448708e-04])}}
        """

        self.path_to_theory_pred = path_to_theory_pred
        self.bins = bins
        self.c_names = []
        self.th_dict = defaultdict(dict)

        self.build_theory_pred_df()
        self.c_names_unique = self.get_c_names_unique()

    def build_theory_pred_df(self):
        """
        Builds a SMEFT theory prediction dictionary
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
        """
        Returns a unique list of EFT parameters in which each parameter only appears once

        Returns
        -------
        array_like
            ```(N, ) ndarray``` array of unique EFT parameters present in `path_to_theory_pred`
        """
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
        """
        Computes cross-section in the SMEFT for a given binning if specified in `bins`. Otherwise it returns an
        average of the total cross section averaged over the available replicas.

        Parameters
        ----------
        path_to_events: str
            Path to events, e.g. ``tt_llvlvlbb/tt_ctGRe``

        Returns
        -------
        array_like
            Cross section per bin averaged over the available replicas
        """
        # path to events
        events_paths = analyse.Analyse.get_event_paths(path_to_events)

        # store the xsec per bin for all the replicas
        xsec_collected = []
        for path in events_paths:
            events, tot_xsec = analyse.Analyse.load_events(event_path=path)

            if self.bins is None:
                xsec_i = tot_xsec
            else:
                n_tot = len(events)
                if len(self.bins) == 1:
                    kin, = self.bins.keys()
                    x = events[kin].values
                    n_i, _, = np.histogram(x, self.bins[kin])
                elif len(self.bins) == 2:
                    kin_1, kin_2 = self.bins.keys()
                    x = events[kin_1].values
                    y = events[kin_2].values
                    n_i, _, _ = np.histogram2d(x, y, bins=(self.bins[kin_1], self.bins[kin_2]))
                xsec_i = (n_i / n_tot) * tot_xsec

            xsec_collected.append(xsec_i)
        xsec_collected = np.array(xsec_collected)

        # average over the replicas
        return np.mean(xsec_collected, axis=0)

    def compute_diff_coefficients(self, optimizer):
        """
        Computes unbinned SMEFT theory predictions for the analytical models, i.e. :math:`t\\bar{t}` or :math:`ZH`

        Parameters
        ----------
        optimizer: :class:`ml4eft.limits.optimize_ns.Optimize`
            Optimizer object

        Returns
        -------
        dict
            unbinned SMEFT predictions
        """
        events = optimizer.observed_data
        features = optimizer.th_features
        n_features = len(features)

        if optimizer.process == 'ZH':

            dsigma_dx_sm = np.array(
                [vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], 0, 0, lin=True, quad=False) for index, row in
                 observed_data.iterrows()])

            dsigma_dx_c1 = np.array(
                [vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], 10, 0, lin=True, quad=False) for index, row in
                 observed_data.iterrows()])

            dsigma_dx_c1_lin_coef = (dsigma_dx_c1 - dsigma_dx_sm) / 10

            dsigma_dx_c2 = np.array(
                [vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], 0, 10, lin=True, quad=False) for index, row in
                 observed_data.iterrows()])

            dsigma_dx_c2_lin_coef = (dsigma_dx_c2 - dsigma_dx_sm) / 10

            dsigma_dx_eft = {'lin': np.stack((dsigma_dx_c1_lin_coef, dsigma_dx_c2_lin_coef))}


        elif optimizer.process == 'ttparton':
            if n_features == 1:
                dsigma_dx = tt_prod.dsigma_dmtt
            if n_features == 2:
                dsigma_dx = tt_prod.dsigma_dmtt_dy
            if n_features == 3:
                dsigma_dx = tt_prod.dsigma_dmtt_dy_dpt

            dsigma_dx_sm = np.array([dsigma_dx(*row[features]) for _, row in events.iterrows()])

            dsigma_dx_c1 = np.array([dsigma_dx(*row[features], [-10, 0], "lin") for _, row
                                     in events.iterrows()])

            dsigma_dx_c2 = np.array(
                [dsigma_dx(*row[features], [0, 10], "lin") for _, row in events.iterrows()])

            dsigma_dx_c1_quad = np.array(
                [dsigma_dx(*row[features], [-10, 0], "quad") for _, row in events.iterrows()])

            dsigma_dx_c2_quad = np.array(
                [dsigma_dx(*row[features], [0, 10], "quad") for _, row in events.iterrows()])

            dsigma_dx_c1_lin_coef = (dsigma_dx_c1 - dsigma_dx_sm) / (-10)

            dsigma_dx_c2_lin_coef = (dsigma_dx_c2 - dsigma_dx_sm) / 10

            dsigma_dx_c1_quad_coef = (dsigma_dx_c1_quad - dsigma_dx_sm) / 100

            dsigma_dx_c2_quad_coef = (dsigma_dx_c2_quad - dsigma_dx_sm) / 100

            dsigma_dx = {'sm': dsigma_dx_sm,
                         'lin': {'ctGRe': dsigma_dx_c1_lin_coef, 'ctu8': dsigma_dx_c2_lin_coef},
                         'quad': {'ctGRe_ctGRe': dsigma_dx_c1_quad_coef, 'ctu8_ctu8': dsigma_dx_c2_quad_coef}}

        return dsigma_dx
