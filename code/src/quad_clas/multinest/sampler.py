import torch
import numpy as np
import os
import json

import pymultinest as prun

import quad_clas.analyse.analyse as analyse
from quad_clas.core.truth import vh_prod
from quad_clas.preproc import constants

mz = constants.mz
mh = constants.mh

class Sampler:

    def __init__(self, seed, priors, luminosity, theory_pred, events):

        self.luminosity = luminosity
        self.prior = priors
        self.seed = seed
        self.nparams = 2

        np.random.seed(self.seed)

        self.theory_pred_total = theory_pred.df.sum(axis=1)

        # find expected number of events under the sm
        xsec_sm = theory_pred_total['sm']
        nu_tot_sm = xsec_sm * self.luminosity
        n_tot_sm = np.random.poisson(nu_tot_sm, 1)

        self.events = events.sample(int(n_tot_sm), random_state=1)

    def loglike(self, cube):
        '''
        Returns log(likelihood(C)). This is the object NS will aim to maximise.
        '''
        cvals = [cube[0], cube[1]]

        theory_pred_total = self.theory_pred.df.sum(axis=1)

        sigma = theory_pred_total['sm'] + cube[0] * theory_pred_total[self.coeffs[0]] + cube[1] * theory_pred_total[
            self.coeffs[1]]

        nu = sigma * self.luminosity

        dsigma_dx = np.array(
            [vh_prod.dsigma_dmvh_dy(row['y'], row['m_zh'], cube[0], cube[1], lin=self.lin, quad=self.quad) for index, row in
             self.events.iterrows()])

        log_likelihood = -nu + np.sum(np.log(dsigma_dx))

        return log_likelihood

    def multinest(self, mcrep=1, nlivepoints=100, nparams=2, verb=True, likefunc=loglike, parameters=['cHw', 'cHq3'], ):

        outputfile = 'samples_parrallel_' + str(mcrep)
        try:
            os.mkdir('samples_output_chains')
        except OSError:
            pass
        prefix = "samples_output_chains/" + str(outputfile)
        with open('%sparams.json' % prefix, 'w') as f:
            json.dump(parameters, f, indent=2)

        def myprior(cube, ndim, nparam):
            for i in range(nparam):
                cube[i] = cube[i] * (self.prior[i, 1] - self.prior[i, 0]) + self.prior[i, 0]

        def myloglike(cube):
            return self.loglike(cube)

        result = prun.run(LogLikelihood=myloglike, Prior=myprior, n_dims=nparams, outputfiles_basename=prefix,
                          verbose=verb, sampling_efficiency=0.8, n_live_points=nlivepoints, evidence_tolerance=1,
                          const_efficiency_mode=False, resume=False, importance_nested_sampling=True)
        return result