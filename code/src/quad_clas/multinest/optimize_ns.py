import pymultinest
import json
import sys
import numpy as np
import time
import os

class Optimize:

    """
    Parameters
    ----------
        config : dict
            configuration dictionary
    """

    def __init__(self, config):

        with open(config) as json_data:
            self.config = json.load(json_data)

        self.parameters = self.config["parameters"]
        if "n_params" in self.config.keys():
            self.n_params = self.config["n_params"]
        else:
            print(
                "Number of paramaters (n_params) not set in the input card. Aborting."
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

        # generate pseudo data
        np.random.seed(4)

        mu_true = 4
        self.sigma_true = 0.5
        n_dat = 40

        self.data_x = np.arange(n_dat)
        self.data_y = np.random.normal(mu_true, self.sigma_true, n_dat)

    def my_prior(self, cube):
        for i in range(self.n_params):
            cube[i] = cube[i] * (self.max_val - self.min_val) + self.min_val

        return cube

    def chi2(self, mu):
        return np.sum(((self.data_y - mu) / self.sigma_true) ** 2)

    def my_log_like(self, cube):
        return -0.5 * self.chi2(cube[0])

    def run_sampling(self):
        """Run the minimisation with Nested Sampling"""

        # Prefix for results
        prefix = self.config["results_path"] + "/truth-"

        t1 = time.time()

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

        t2 = time.time()

        print("Time = ", (t2 - t1) / 60.0)

        self.save(result)
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






