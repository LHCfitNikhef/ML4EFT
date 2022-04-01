import numpy as np
from . import sampler
from multiprocessing import Pool
from itertools import repeat
from ..core.th_predictions import TheoryPred
import pandas as pd

luminosity = 5e3
seed = 0
mypriors = np.array([[-10,10],[-10,10]])
nlive = 100 #live points used by multinest
nprocs=1 #processers for parallelisation

# load theory predictions
theory_pred = TheoryPred(coeff = ['cHW', 'cHq3'],
                         bins = [0, 4000],
                         kinematic = 'pt_z',
                         event_path='/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz',
                         nreps=30)

# load observed dataset (pseudo data)
sm_data_path = '/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz/sm/events_0.pkl.gz'
events_sm = pd.read_pickle(sm_data_path).iloc[1:, :]

#Nested sampling, using each NN mc_rep in parallel
nestedSampler= sampler.Sampler(luminosity, seed, mypriors, process)
pool = Pool(processes=nprocs)
pool.starmap(nestedSampler.multinest, repeat(nlive))