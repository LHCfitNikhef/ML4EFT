import pymultinest
import json
import sys
import numpy as np
import time
import os
import pandas as pd
from pathlib import Path
import shutil
import copy

import quad_clas.analyse.analyse as analyse
import quad_clas.core.th_predictions as theory_pred
from quad_clas.core.truth import vh_prod
from quad_clas.preproc import constants

from quad_clas.core.th_predictions import TheoryPred

mz = constants.mz
mh = constants.mh

# fix randomness
np.random.seed(0)


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

    def __init__(self, config, coeff=None, rep=None):

        self.config = config.copy()
        self.rep = rep
        self.coeff = coeff
        self.param_names = {}

        if self.rep is not None:
            self.config["results_path"] = os.path.join(self.config["results_path"], "r_{}".format(self.rep))

        if "order" in self.config.keys():
            self.order = self.config["order"]
        if "prior" in self.config.keys():
            self.prior_range = self.config["prior"]

        if "process" in self.config.keys():
            self.process = self.config["process"]
        if "mode" in self.config.keys():
            self.mode = self.config["mode"]
        else:
            print(
                "No mode (mode) selected, please specify one in the input card. Aborting."
            )
            sys.exit()

        if "path_to_theory_pred" in self.config.keys():
            self.path_to_theory_pred = self.config["path_to_theory_pred"]
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
                self.nn_analyser = analyse.Analyse(self.path_to_models)
            else:
                print(
                    "No path tot model (path_to_models) specified. Please set in the in the input card. Aborting."
                )
                sys.exit()

            self.bins = None
            self.kinematic = None
        elif self.mode == "truth":
            self.bins = None
            self.kinematic = None
            self.th_features = self.config['th_features']

        self.th_pred = theory_pred.TheoryPred(self.path_to_theory_pred,
                                              kinematic=self.kinematic,
                                              bins=self.bins)

        if self.coeff is None:
            self.glob = True
            self.coeff = self.th_pred.th_dict['lin'].keys() # coefficients to include in the fit
        else:
            self.glob = False

        self.suffix = ''
        if self.glob is False:
            self.suffix += '_'
            for c in self.coeff:
                self.suffix += c + '_'
            self.suffix = self.suffix[:-1]
        self.output_path = os.path.join(self.config["results_path"], self.mode, self.suffix[1:])

        Path(self.output_path).mkdir(parents=True, exist_ok=True)

        # store input card as reference
        with open(os.path.join(self.output_path, 'input_card.json'), 'w') as json_data:
            json.dump(self.config, json_data)

        # nr of dof
        self.n_params = len(self.coeff)

        # load dataset (pseudo data)
        sm_data_path = self.config['observed_data_path']
        sm_data, _ = analyse.Analyse.load_events(sm_data_path)

        # construct observed dataset
        xsec_sm_tot = np.sum(self.th_pred.th_dict['sm'])  # sum over bins
        nu_tot_sm = xsec_sm_tot * config['lumi']
        n_tot_sm = np.random.poisson(nu_tot_sm, 1)

        self.observed_data = sm_data.sample(int(n_tot_sm), random_state=1)

        if self.mode == "nn":
            # evaluated nn models on pseudo dataset
            self.nn_analyser.evaluate_models(self.observed_data)

            models_evaluated = self.nn_analyser.models_evaluated_df['models']

            # taken median over models
            self.nn_analyser.models_evaluated_df['models'] = models_evaluated.apply(lambda row:
                                                                                    np.median(row, axis=0))

        if self.mode == "truth":
            self.dsigma_dx = self.th_pred.compute_diff_coefficients(self)

        elif self.mode == "binned":
            self.n_i, _ = np.histogram(self.observed_data[self.kinematic].values, self.bins)

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

        for i, c_name in enumerate(self.coeff):
            prior_min, prior_max = self.prior_range[c_name]
            cube[i] = cube[i] * (prior_max - prior_min) + prior_min

        return cube

    def cube_to_dict(self, cube):

        # convert cube to dict
        for i, c_name in enumerate(self.coeff):
            self.param_names[c_name] = cube[i]


    def log_like_nn(self, cube):

        self.cube_to_dict(cube)

        # compute inclusive xsec at cube
        sigma = 0

        for c_name in self.coeff:
            sigma += self.param_names[c_name] * self.th_pred.th_dict['lin'][c_name]
            sigma += self.param_names[c_name] ** 2 * self.th_pred.th_dict['quad'][c_name]

        sigma += self.th_pred.th_dict['sm']

        nu = sigma * self.lumi

        # median likelihood ratio
        ratio_med = self.nn_analyser.likelihood_ratio_nn(self.param_names)
        log_r_med = np.log(ratio_med)

        return -nu + np.sum(log_r_med)

    def log_like_truth(self, cube):

        #self.cube_to_dict(cube)
        for i, c_name in enumerate(self.th_pred.th_dict['lin'].keys()):
            self.param_names[c_name] = cube[i]

        # compute inclusive and differential xsec at cube
        sigma = self.th_pred.th_dict['sm']
        dsigma_dx = copy.deepcopy(self.dsigma_dx['sm'])

        for c_name, sigma_i in self.th_pred.th_dict['lin'].items():
            sigma += self.param_names[c_name] * sigma_i
            dsigma_dx += self.param_names[c_name] * self.dsigma_dx['lin'][c_name]

        for c_name, sigma_i in self.th_pred.th_dict['quad'].items():
            sigma += self.param_names[c_name] ** 2 * sigma_i
            dsigma_dx += self.param_names[c_name] ** 2 * self.dsigma_dx['quad'][c_name]

        nu = sigma * self.lumi
        log_like = -nu + np.sum(np.log(dsigma_dx / self.dsigma_dx['sm']))

        return log_like

    def log_like_binned(self, cube):

        self.cube_to_dict(cube)

        sigma = 0

        for c_name in self.coeff:
            sigma += self.param_names[c_name] * self.th_pred.th_dict['lin'][c_name]
            sigma += self.param_names[c_name] ** 2 * self.th_pred.th_dict['quad'][c_name]

        sigma += self.th_pred.th_dict['sm']

        nu_i = sigma * self.lumi
        log_like_i = self.n_i * np.log(nu_i) - nu_i
        return np.sum(log_like_i)

    def run_sampling(self):
        """Run the minimisation with Nested Sampling"""

        # Prefix for results
        prefix = os.path.join(self.output_path, "1k-")

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
                                   const_efficiency_mode=True,
                                   importance_nested_sampling=True,
                                   sampling_efficiency=0.01,
                                   evidence_tolerance=0.5
                                   )
        print("NS done!")
        t2 = time.perf_counter()

        print("Time = ", (t2 - t1) / 60.0)

        # export the posterior samples to json
        self.save(result)

        # remove ns raw output
        self.clean()

    def clean(self):
        """ Remove raw NS output if you want to keep raw output, don't call this method"""

        filelist = [
            f for f in os.listdir(self.output_path) if f.startswith("1k-")
        ]
        for f in filelist:
            if f in os.listdir(self.output_path):
                os.remove(os.path.join(self.output_path, f))

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
        for i, (c, samples) in enumerate(zip(self.param_names.keys(), result['samples'].T)):
            vals[c] = samples.tolist()

        with open(os.path.join(self.output_path, 'posterior' + self.suffix + '.json'), "w") as f:
            json.dump(vals, f)
