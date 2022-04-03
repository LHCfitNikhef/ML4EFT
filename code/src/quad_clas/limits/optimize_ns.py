import pymultinest
import json
import sys
import numpy as np
import time
import os

import quad_clas.analyse.analyse as analyse
from quad_clas.core.truth import vh_prod
from quad_clas.preproc import constants

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

    def __init__(self, config, observed_data, theory_pred):

        self.config = config.copy()

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

        self.observed_data = observed_data

        # likelihood building blocks
        self.dsigma_dx_sm, self.dsigma_dx_eft = theory_pred.compute_diff_coefficients(self.observed_data)
        self.theory_pred_total = theory_pred.df.sum(axis=1)


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

    def my_log_like(self, cube):

        sigma = self.theory_pred_total['sm'] + cube[0] * self.theory_pred_total['chw'] + cube[1] * self.theory_pred_total['chq3']

        dsigma_dx = self.dsigma_dx_sm + self.dsigma_dx_eft['lin'].T @ cube

        #dsigma_dx = self.dsigma_dx_sm + cube[0] * (self.dsigma_dx_c1 - self.dsigma_dx_sm) / 10 + cube[1] * (self.dsigma_dx_c2 - self.dsigma_dx_sm) / 10

        nu = sigma * self.lumi

        log_likelihood = -nu + np.sum(np.log(dsigma_dx))

        return log_likelihood

    def run_sampling(self):
        """Run the minimisation with Nested Sampling"""

        # Prefix for results
        prefix = self.config["results_path"] + "/truth-"

        t1 = time.perf_counter()

        result = pymultinest.solve(LogLikelihood=self.my_log_like,
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






