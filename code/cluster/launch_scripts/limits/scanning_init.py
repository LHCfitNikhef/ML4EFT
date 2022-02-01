import numpy as np
import quad_clas.analyse.confidence_intervals as conf_int
import sys

row = sys.argv[1]

# Network's architecture of the pretrained models
architecture = [3, 30, 30, 30, 30, 30, 1]

path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHW_3_feat/mc_run_{mc_run}',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHq3_3_feat/mc_run_{mc_run}']}

sm_data_path = '/data/theorie/jthoeve/event_generation/events_high_stats/pT/sm/events_0.npy'

events_sm = np.load(sm_data_path)[1:, :]

luminosity = 5000

plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/27_01/run_03/'

# domain of EFT parameters to scan for limit setting
cHW_values = np.linspace(-0.5, 0.2, 50)
cHq3_values = np.linspace(-1.0, 2.0, 50)
if int(row) == 0:
    np.save(os.path.join(plot_save, 'scan_domain.npy'), np.array([cHW_values, cHq3_values]))
scan_domain = (cHW_values, [cHq3_values[int(row)]])

# number of bins to consider
bins = np.array([2])

# number of trained neural network replicas
mc_reps = 30

# location where to save the plot


limits = conf_int.Limits(luminosity=luminosity,
                         bins=bins,
                         scan_domain=scan_domain,
                         path_to_models=path_to_models,
                         mc_reps=mc_reps,
                         data_sm=events_sm,
                         lin=True,
                         plot_path=plot_save,
                         architecture=architecture,
                         row=int(row),
                         save=True,
                         save_path='/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/27_01/run_03/',
                         nn = False,
                         binned=False,
                         truth=True)