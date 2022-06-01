import pymultinest
import json
import sys
import numpy as np
import time
import os
import pandas as pd
from pathlib import Path
import shutil

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

    def __init__(self, config, rep=None):

        self.config = config.copy()
        self.rep = rep

        if self.rep is not None:
            self.config["results_path"] = os.path.join(self.config["results_path"], "r_{}".format(self.rep))
        Path(self.config["results_path"]).mkdir(parents=True, exist_ok=True)

        # store input card as reference
        with open(os.path.join(self.config['results_path'], 'input_card.json'), 'w') as json_data:
            json.dump(self.config, json_data)

        if "HOcorrections" in self.config.keys():
            self.HOcorrections = self.config["HOcorrections"]

        if "process" in self.config.keys():
            self.process = self.config["process"]
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
        elif self.mode == "nn":
            if "path_to_models" in self.config.keys():
                self.path_to_models = self.config["path_to_models"]
            else:
                print(
                    "No path tot model (path_to_models) specified. Please set in the in the input card. Aborting."
                )
                sys.exit()
            # if "architecture" in self.config.keys():
            #     self.architecture = self.config["architecture"]
            # else:
            #     print(
            #         "No architecture (architecture) specified. Please set in the in the input card. Aborting."
            #     )
            #     sys.exit()

            self.bins = None
            self.kinematic = None
        else:  # unbinned case
            self.bins = None
            self.kinematic = None
        
        event_path = self.config['theory_pred_path']
        theory_pred = TheoryPred(coeff=self.parameters.keys(),
                                 event_path=event_path,
                                 HOcorrections = self.HOcorrections,
                                 bins=self.bins,
                                 kinematic=self.kinematic)

        # load dataset (pseudo data)
        sm_data_path = self.config['observed_data_path']
        sm_data = pd.read_pickle(sm_data_path).iloc[1:, :]

        # construct observed dataset
        np.random.seed(0)
        theory_pred_total = theory_pred.df.sum(axis=1)
        xsec_sm = theory_pred_total['sm'] # TODO: take xsec from df directly?
        nu_tot_sm = xsec_sm * config['lumi']
        n_tot_sm = np.random.poisson(nu_tot_sm, 1)

        self.observed_data = sm_data.sample(int(n_tot_sm), random_state=1)

        #self.observed_data['log_m_zh'] = np.log(self.observed_data['m_zh'])

        # check
        #self.observed_data = self.observed_data[(self.observed_data['m_zh'] < 0.8) & (self.observed_data['m_zh'] > 0.5)]
        #self.observed_data = self.observed_data[self.observed_data['m_zh'] < 1.0]

        # observed counts
        if self.mode == "nn":

            [n_lin, model_idx], n_quad, n_cross = analyse.load_coefficients_nn(self.observed_data, self.parameters, self.path_to_models)
            rep_tot = np.array([n_lin[i].shape[0] for i in range(len(n_lin))])
            rep_ava = rep_tot.min() # max available replicas

            if self.rep is None:
                self.n_lin_chw = np.median(n_lin[0], axis=0)
                self.n_lin_chq3 = np.median(n_lin[1], axis=0)
            else:
                if self.rep >= rep_ava:
                    print(
                        "The specified replica number is not available, please enter a smaller number. Aborting."
                    )

                    try:
                        shutil.rmtree(self.config['results_path'])
                    except OSError as e:
                        print("Error: %s : %s" % (self.config['results_path'], e.strerror))

                    sys.exit()
                self.n_lin_chw = n_lin[0][self.rep, :]
                self.n_lin_chq3 = n_lin[1][self.rep, :]

        if self.mode == "truth":
            self.dsigma_dx_sm, self.dsigma_dx_eft = theory_pred.compute_diff_coefficients(self.observed_data, self.process)
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

    def log_like_nn(self, cube):

        theory_pred_total = self.theory_pred.sum(axis=1)

        sigma = theory_pred_total['sm'] + theory_pred_total[self.parameters] @ cube

        nu = sigma * self.lumi

        r_nn = 1 + cube[0] * self.n_lin_chw + cube[1] * self.n_lin_chq3

        log_r_nn = np.log(r_nn)
        log_likelihood = -nu + np.sum(log_r_nn)

        return log_likelihood

    def log_like_truth(self, cube):

        theory_pred_total = self.theory_pred.sum(axis=1)

        quad_idx = [i for i, (index, _) in enumerate(theory_pred_total.items()) if '*' in index]

        if self.HOcorrections:
            sigma = theory_pred_total['sm'] + theory_pred_total[self.parameters] @ cube + theory_pred_total.iloc[quad_idx] @ (cube ** 2)
            dsigma_dx = self.dsigma_dx_sm + self.dsigma_dx_eft['lin'].T @ cube + self.dsigma_dx_eft['quad'].T @ (
                        cube ** 2)
        else:
            sigma = theory_pred_total['sm'] + theory_pred_total[self.parameters] @ cube
            dsigma_dx = self.dsigma_dx_sm + self.dsigma_dx_eft['lin'].T @ cube

        nu = sigma * self.lumi

        log_likelihood = -nu + np.sum(np.log(dsigma_dx))

        return log_likelihood

    def log_like_binned(self, cube):

        quad_idx = [i for i, (index, _) in enumerate(self.theory_pred.iterrows()) if '*' in index]

        if self.HOcorrections:
            sigma_i = self.theory_pred.loc['sm'] + self.theory_pred.loc[self.parameters].T @ cube + self.theory_pred.iloc[quad_idx].T @ (cube ** 2)
        else:
            sigma_i = self.theory_pred.loc['sm'] + self.theory_pred.loc[self.parameters].T @ cube

        nu_i = sigma_i * self.lumi
        log_l_i = self.n_i * np.log(nu_i) - nu_i

        return log_l_i.sum()


    def run_sampling(self):
        """Run the minimisation with Nested Sampling"""

        # Prefix for results
        if self.rep is not None:

            prefix = os.path.join(self.config["results_path"], "1k-")
        else:
            prefix = os.path.join(self.config["results_path"], "1k-")

        t1 = time.perf_counter()

        if self.mode == "nn":
            log_likelihood = self.log_like_nn
        elif self.mode == "truth":
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
            f for f in os.listdir(self.config["results_path"]) if f.startswith("1k-")
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
        for i, (c, samples) in enumerate(zip(self.parameters.keys(), result['samples'].T)):
            vals[c] = samples.tolist()
        with open(os.path.join(self.config['results_path'], 'posterior.json'), "w") as f:
            json.dump(vals, f)






