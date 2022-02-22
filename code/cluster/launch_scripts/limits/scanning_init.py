import numpy as np
import quad_clas.analyse.confidence_intervals as conf_int
import sys, os
import pandas as pd

row = sys.argv[1]

# Network's architecture of the pretrained models
architecture = [8, 30, 30, 30, 30, 30, 1]

# mvh, y, pt (no decays)
# path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHW_3_feat/mc_run_{mc_run}',
#                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHq3_3_feat/mc_run_{mc_run}']}
# sm_data_path = '/data/theorie/jthoeve/event_generation/events_high_stats/pT/sm/events_0.npy'
# plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/27_01/run_03/'


# atlas multivariate analysis in zh > llbb
path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/21_02/model_chw_lin/mc_run_{mc_run}',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/21_02/model_chwb_lin/mc_run_{mc_run}']}

sm_data_path = '/data/theorie/jthoeve/training_data/sm/events_0.pkl.gz'

events_sm = pd.read_pickle(sm_data_path).iloc[1:, :].drop('pt_b', axis=1)

luminosity = 5E6

# location where to save the plot
plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/21_02'

# domain of EFT parameters (pt, mvh, y) to scan for limit setting
# cHW_values = np.linspace(-0.5, 0.2, 50)
# cHq3_values = np.linspace(-1.0, 2.0, 50)
# if int(row) == 0:
#     np.save(os.path.join(plot_save, 'scan_domain.npy'), np.array([cHW_values, cHq3_values]))
# scan_domain = (cHW_values, [cHq3_values[int(row)]])

cHW_values = np.linspace(-0.5, 0.2, 50)
cHWB_values = np.linspace(-1.0, 2.0, 50)
if int(row) == 0:
    np.save(os.path.join(plot_save, 'scan_domain.npy'), np.array([cHW_values, cHWB_values]))
scan_domain = (cHW_values, [cHWB_values[int(row)]])

# number of bins to consider
bins = np.array([0, 75, 150, 250, 400, 1000])

# number of trained neural network replicas
mc_reps = 50

coeffs = ['chdd', 'chwb', 'cbhre', 'chw']

limits = conf_int.Limits(luminosity=luminosity,
                         bins=bins,
                         scan_domain=scan_domain,
                         coeffs=coeffs,
                         path_to_models=path_to_models,
                         event_path='/data/theorie/jthoeve/training_data',
                         mc_reps=mc_reps,
                         data_sm=events_sm,
                         lin=True,
                         plot_path=plot_save,
                         architecture=architecture,
                         row=int(row),
                         save=True,
                         save_path=plot_save,
                         nn = True,
                         binned=False,
                         truth=False)

#save_path='/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/27_01/run_03/',