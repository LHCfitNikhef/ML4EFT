import numpy as np
import quad_clas.analyse.analyse as ana

root_path = '/data/theorie/jthoeve/ML4EFT/'

# define the binnings
binning_0 = np.append(np.linspace(1000, 2000, 8), 4000).astype(int)
binning_1 = np.append(np.linspace(1000, 2000, 4), 4000).astype(int)
binning_2 = np.append(np.linspace(1000, 2000, 1), 4000).astype(int)

binnings_list = [binning_0, binning_1, binning_2]

extent = np.array([[-1.2, 1.2], [-1, 1]])
analysis = ana.Analyse(root_path, nn=False, truth=True, fit=False, extent=extent)