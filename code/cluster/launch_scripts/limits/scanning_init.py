import numpy as np
import ml4eft.analyse.confidence_intervals as conf_int
import sys, os
import pandas as pd

row = sys.argv[1]

# Network's architecture of the pretrained models
architecture = [1, 30, 30, 30, 30, 30, 1]

# atlas multivariate analysis in zh > llbb
path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_llbb/model_chw_lin/mc_run_{mc_run}',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_llbb/model_chwb_lin/mc_run_{mc_run}']}

# observed data
sm_data_path = '/data/theorie/jthoeve/training_data/zh_llbb/sm/events_0.pkl.gz'

events_sm = pd.read_pickle(sm_data_path).iloc[1:, :]#['pt_z']
luminosity = 5E6

# location where to save the plot
plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh_llbb/binned/binning_3'
if not os.path.exists(plot_save):
    os.makedirs(plot_save)

cHW_values = np.linspace(-1.0, 0.5, 200)
cHWB_values = np.linspace(-0.5, 1.0, 200)
if int(row) == 0:
    np.save(os.path.join(plot_save, 'scan_domain.npy'), np.array([cHW_values, cHWB_values]))
scan_domain = (cHW_values, [cHWB_values[int(row)]])

# number of bins to consider
# binning 1
#bins = np.array([0, 75, 150, 250, 400, 1000])

# binning 2
#bins = np.array([0, 4000])

# binning 3
bins = np.linspace(0, 4000, 30)

# number of trained neural network replicas
mc_reps = 50

#coeffs = ['chdd', 'chwb', 'cbhre', 'chw']
coeffs = ['chw', 'chwb']

limits = conf_int.Limits(luminosity=luminosity,
                         bins=bins,
                         kinematic='pt_z',
                         scan_domain=scan_domain,
                         coeffs=coeffs,
                         path_to_models=path_to_models,
                         event_path='/data/theorie/jthoeve/training_data/zh_llbb',
                         mc_reps=mc_reps,
                         data_sm=events_sm,
                         lin=True,
                         plot_path=plot_save,
                         architecture=architecture,
                         row=int(row),
                         save=True,
                         save_path=plot_save,
                         nn = False,
                         binned=True,
                         truth=False)