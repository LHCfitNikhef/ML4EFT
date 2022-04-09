import numpy as np
import quad_clas.analyse.confidence_intervals as conf_int
import sys, os
import pandas as pd

row = sys.argv[1]

# Network's architecture of the pretrained models
architecture = [2, 30, 30, 30, 30, 30, 1]

# mvh, y, pt (no decays)
path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/zh_mzh_y_robust_scaler/model_chw_lin/mc_run_{mc_run}',
                         '/Users/jaco/Documents/ML4EFT/models/zh_mzh_y_robust_scaler/model_chq3_lin/mc_run_{mc_run}']}

sm_data_path = '/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz/sm/events_0.pkl.gz'

#drop pt_z
events_sm = pd.read_pickle(sm_data_path).iloc[1:, :]


luminosity = 5E3

# location where to save the plot
plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/nn/'

# domain of EFT parameters (pt, mvh, y) to scan for limit setting
cHW_values = np.linspace(-1, 0.5, 100)
cHq3_values = np.linspace(-2, 3, 100)
if int(row) == 0:
    np.save(os.path.join(plot_save, 'scan_domain.npy'), np.array([cHW_values, cHq3_values]))
scan_domain = (cHW_values, [cHq3_values[int(row)]])


# number of bins to consider
#bins = np.array([0, 4000])
#bins = np.array([0, 75, 150, 250, 400, 4000]) * 1E-3
#bins = np.array([0, 4000]) * 1E-3

# m_zh bins

# binning_1
#bins = np.array([0, 200, 300, 400, 600, 1000, 4000]) * 1E-3

# binning_2
#bins = np.array([0, 4000]) * 1E-3

# binning 3
#bins = np.array([0, 200, 300, 400, 4000]) * 1E-3

# binning 4
bins = np.array([0, 300, 4000]) * 1E-3

# number of trained neural network replicas
mc_reps = 30

coeffs = ['cHW', 'cHq3']

limits = conf_int.Limits(luminosity=luminosity,
                         bins=bins,
                         kinematic='pt_z',
                         scan_domain=scan_domain,
                         coeffs=coeffs,
                         path_to_models=path_to_models,
                         event_path='/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz',
                         mc_reps=mc_reps,
                         data_sm=events_sm,
                         lin=True,
                         plot_path=plot_save,
                         architecture=architecture,
                         row=int(row),
                         save=True,
                         save_path=plot_save,
                         nn = False,
                         binned=False,
                         truth=True)

#save_path='/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/27_01/run_03/',