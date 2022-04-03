import pymultinest
import json
import sys
import numpy as np
import time
import os
import pandas as pd

import quad_clas.analyse.analyse as analyse
from quad_clas.core.truth import vh_prod
from quad_clas.preproc import constants
from quad_clas.core.th_predictions import TheoryPred

mz = constants.mz
mh = constants.mh


class Optimize:

    """
    Parameters
    ----------
        config : dict
            configuration dictionary
        observed_data: numpy.ndarray()
            Observed events (i.e. under the SM)
        theory_pred: TheoryPred
            instance of TheoryPred that contains the theory predictions
    """

    def __init__(self, config):

        self.config = config.copy()

        # store input card as reference
        with open(os.path.join(self.config['results_path'], 'input_card.json'), 'w') as json_data:
            json.dump(self.config, json_data)

        if "mode" in self.config.keys():
            self.mode = self.config["mode"]
        else:
            print(
                "No mode (mode) selected, please specify one in the input card. Aborting."
            )
            sys.exit()

        if "parameters" in self.config.keys():
            self.parameters = self.config["parameters"]
            self.n_params = len(self.parameters)
        else:
            print(
                "Parameters names (parameters) not set in the input card. Aborting."
            )
            sys.exit()

        if "nlive" in self.config.keys():
            self.live_points = self.config["nlive"]
        else:
            print(
                "Number of live points (nlive) not set in the input card. Using default: 500"
            )
            self.live_points = 500

        if "max_val" in self.config.keys():
            self.max_val = self.config["max_val"]
        if "min_val" in self.config.keys():
            self.min_val = self.config["min_val"]

        if "lumi" in self.config.keys():
            self.lumi = self.config["lumi"]
        else:
            print(
                "Luminosity (lumi) not set in the input card. Using default: 5e3 pb^-1"
            )

        if self.mode == 'binned':
            if "bins" in self.config.keys():
                self.bins = self.config["bins"]
            else:
                print(
                    "No binning (bins) specified. Please set in the in the input card. Aborting."
                )
                sys.exit()
            if "kinematic" in self.config.keys():
                self.kinematic = self.config["kinematic"]
            else:
                print(
                    "No bin variable (kinematic) specified. Please set in the in the input card. Aborting."
                )
                sys.exit()
        else:  # unbinned case
            self.bins = None,
            self.kinematic = None

        event_path = self.config['theory_pred_path']
        theory_pred = TheoryPred(coeff=self.parameters,
                                 event_path=event_path,
                                 nreps=30,
                                 bins=self.bins,
                                 kinematic=self.kinematic)

        # load dataset (pseudo data)
        sm_data_path = self.config['observed_data_path']
        sm_data = pd.read_pickle(sm_data_path).iloc[1:, :]

        # construct observed dataset

        theory_pred_total = theory_pred.df.sum(axis=1)
        xsec_sm = theory_pred_total['sm']
        nu_tot_sm = xsec_sm * config['lumi']
        n_tot_sm = np.random.poisson(nu_tot_sm, 1)

        self.observed_data = sm_data.sample(int(n_tot_sm), random_state=1)

        # observed counts
        if self.mode == "unbinned":
            self.dsigma_dx_sm, self.dsigma_dx_eft = theory_pred.compute_diff_coefficients(self.observed_data)
        elif self.mode == "binned":
            self.n_i, _ = np.histogram(self.observed_data[self.kinematic].values, self.bins)

        # theory predictions
        self.theory_pred = theory_pred.df

    def my_prior(self, cube):
        """
        Construct prior volume

        Parameters
        ----------
        cube: numpy.ndarray, shape=(M,)
            unit hypercube of dim M

        Returns
        -------
        cube: numpy.ndarray
            hypercube prior
        """
        for i in range(self.n_params):
            cube[i] = cube[i] * (self.max_val - self.min_val) + self.min_val

        return cube

    def log_like_truth(self, cube):

        theory_pred_total = self.theory_pred.sum(axis=1)

        sigma = theory_pred_total['sm'] + cube[0] * theory_pred_total['chw'] + cube[1] * theory_pred_total['chq3']

        dsigma_dx = self.dsigma_dx_sm + self.dsigma_dx_eft['lin'].T @ cube

        nu = sigma * self.lumi

        log_likelihood = -nu + np.sum(np.log(dsigma_dx))

        return log_likelihood

    def log_like_binned(self, cube):
        
        sigma_i = self.theory_pred.loc['sm'] + self.theory_pred.iloc[1:, :].T @ cube
        nu_i = sigma_i * self.lumi
        log_l_i = self.n_i * np.log(nu_i) - nu_i

        #log_l_i[np.isnan(log_l_i)] = 0
        return log_l_i.sum()


    def run_sampling(self):
        """Run the minimisation with Nested Sampling"""

        # Prefix for results
        prefix = self.config["results_path"] + "/truth-"

        t1 = time.perf_counter()

        if self.mode == "unbinned":
            log_likelihood = self.log_like_truth
        elif self.mode == "binned":
            log_likelihood = self.log_like_binned

        result = pymultinest.solve(LogLikelihood=log_likelihood,
                                   Prior=self.my_prior,
                                   n_dims=self.n_params,
                                   outputfiles_basename=prefix,
                                   verbose=True,
                                   n_live_points=self.live_points,
                                   const_efficiency_mode=False,
                                   resume=False,
                                   importance_nested_sampling=True
                                   )

        t2 = time.perf_counter()

        print("Time = ", (t2 - t1) / 60.0)

        # export the posterior samples to json
        self.save(result)

        # remove ns raw output
        self.clean()

    def clean(self):
        """ Remove raw NS output if you want to keep raw output, don't call this method"""

        filelist = [
            f for f in os.listdir(self.config["results_path"]) if f.startswith("truth-")
        ]
        for f in filelist:
            if f in os.listdir(self.config["results_path"]):
                os.remove(os.path.join(self.config["results_path"], f))

    def save(self, result):
        """
        Save NS replicas to json inside a dictionary:
        {coeff: [replicas values]}
        Parameters
        ----------
            result : dict
                result dictionary
        """

        vals = {}
        for i, (c, samples) in enumerate(zip(self.parameters, result['samples'].T)):
            vals[c] = samples.tolist()
        with open(f"{self.config['results_path']}/posterior.json", "w") as f:
            json.dump(vals, f)






