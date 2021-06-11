import numpy as np
import os
import quad_clas.bounds as bounds

root_path = '/data/theorie/jthoeve/ML4EFT/'
output_path = os.path.join(root_path, 'output')
plots_path = os.path.join(output_path, 'plots')
paths = {'root': root_path, 'output': output_path, 'plots': plots_path}

# binned analysis

binning_0 = np.append(np.linspace(1000, 2000, 8), 4000).astype(int)
binning_1 = np.append(np.linspace(1000, 2000, 4), 4000).astype(int)
binning_2 = np.append(np.linspace(1000, 2000, 1), 4000).astype(int)

binnings = [binning_0, binning_1, binning_2]

# create instance of StatAnalysis and store them in a list
binned_analyses = []
for i, binning in enumerate(binnings):
    paths['output'] = os.path.join(output_path, 'binning_{}'.format(i))
    binned_analyses.append(bounds.StatAnalysis(paths, bins=binning, fit=False, luminosity=6))

# TODO: always start with cuu first
limits = np.array([[-1.2, 1.2], [-0.15, 0.2]])

binned_analyses[0].binned_analysis(limits=limits)

#binned_analyses[0].p_values_asi

# asymptotic versus exact analysis
fig = bounds.plot_tc_accuracy(binned_analyses, c=np.array([0, 1.0]), n=10000)
fig.savefig(os.path.join(plots_path, 'tc_comp.pdf'))




