import quad_clas.analyse.animate as animate
import numpy as np


animator = animate.Animate(architecture=[2, 30, 30, 30, 30, 30, 1],
                           c=np.array([2, 0]),
                           path_to_models='/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_{mc_run}',
                           mc_runs=30,
                           save_path='/Users/jaco/Documents/ML4EFT/plots/25_11/cHW_lin_v3.gif',
                           lin=True)
