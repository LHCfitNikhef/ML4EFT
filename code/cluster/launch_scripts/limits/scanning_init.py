import numpy as np
import quad_clas.analyse.confidence_intervals as conf_int

# Network's architecture of the pretrained models
architecture = [3, 30, 30, 30, 30, 30, 1]

path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHW_3_feat',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01/model_lin_cHq3_3_feat']}

sm_data_path = '/data/theorie/jthoeve/event_generation/events_high_stats/pT/sm/events_0.npy'

events_sm = np.load(sm_data_path)[1:, :]

luminosity = 5000

# domain of EFT parameters to scan for limit setting
cHW_values = np.linspace(-1, 1, 4)
cHq3_values = np.linspace(-3, 3, 4)
scan_domain = np.array([cHW_values, cHq3_values])

# number of bins to consider
bins = np.array([2])

# number of trained neural network replicas
mc_reps = 30

# location where to save the plot
plot_save = '/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/24_01/'

limits = conf_int.Limits(luminosity=luminosity,
                         bins=bins,
                         scan_domain=scan_domain,
                         path_to_models=path_to_models,
                         mc_reps=mc_reps,
                         data_sm=events_sm,
                         lin=True,
                         plot_path=plot_save,
                         architecture=architecture,
                         save=True,
                         save_path='/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/24_01')