import numpy as np
import os, sys
import matplotlib.pyplot as plt
import pandas as pd
import csv
from scipy.ndimage.filters import gaussian_filter
import quad_clas.bounds as bounds

root_path = '/data/theorie/jthoeve/ML4EFT/'
output_path = os.path.join(root_path, 'output')
plots_path = os.path.join(output_path, 'plots')
paths = {'root': root_path, 'output': output_path, 'plots': plots_path}


def run_binned_analysis(binnings, extent, fit, luminosity):
    """

    Parameters
    ----------
    binnings: list
        collection of binnings for which to run the analysis
    extent: array_like, shape (n, 2)
        The range of the eft parameters to scan
    fit: bool
        This should be set to true for every new binning
    luminosity: float
        luminosity of the experiment in pb^-1

    Returns
    -------
    list
        a list of binned analyses objects
    """

    binned_analyses = []

    for i, binning in enumerate(binnings):
        # output directory is different for each bin
        paths['output'] = os.path.join(output_path, 'binning_{}'.format(i))

        # create an analysis instance and perform the analysis
        analysis = bounds.StatAnalysis(paths, bins=binning, fit=fit, luminosity=luminosity)
        analysis.binned_analysis(extent=extent)

        # append results
        binned_analyses.append(analysis)

    return binned_analyses


def stdom(x):
    return np.std(x) / np.sqrt(len(x))


def wavg(group):
    z = group['z-score']
    sigma_z = group['uncertainty']
    z_wavg = ((z / sigma_z ** 2).sum()) / ((1 / sigma_z ** 2).sum())
    z_wavg_unc = 1 / ((1 / sigma_z ** 2).sum())
    return pd.Series({'z-score': z_wavg, 'uncertainty': z_wavg_unc})


def load_z_scores(path, mc_runs):
    """ Load the z-scores for all the mc runs

    Parameters
    ----------
    path: root path to z-scores file
    mc_runs: number of monte carlo runs to load

    Returns
    -------
    Pandas dataframe
    """
    z_scores = []
    for i in range(1, mc_runs + 1):
        loc = os.path.join(path, "mc_run_{}/z_scores.dat".format(i))
        with open(loc, "r") as f:
            reader = csv.reader(f, delimiter='\t')
            for line in reader:
                z_scores.append([float(value) for value in line])

    if 'nn' in path:
        z_scores = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score', 'uncertainty'])
        z_scores_grouped = z_scores.groupby(['cug', 'cuu'])
        z_scores_grouped = z_scores_grouped.apply(wavg)
        z_scores_grouped = z_scores_grouped.reset_index()
    else:
        z_scores = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score'])
        z_scores_grouped = z_scores.groupby(['cug', 'cuu']).agg({'z-score': ['mean', stdom]})
        z_scores_grouped.columns = ['z-score', 'uncertainty']
        z_scores_grouped = z_scores_grouped.reset_index()
    return z_scores_grouped


def combine_analyses(binned_analyses=None, truth_analysis=None, nn_analysis=None):

    fig, ax = plt.subplots(figsize=(10, 6))

    labels = []
    contours = []
    if binned_analyses is not None:
        sigma = 0.8
        for i, binnings in enumerate(binned_analyses):
            data_smoothed = gaussian_filter(binnings.z_scores_asi, sigma)
            contour = ax.contour(binnings.cuu_plane, binnings.cug_plane, data_smoothed, levels=np.array([1.64]))
            h0, _ = contour.legend_elements()
            contours.append(h0[0])
            labels.append(r'$\rm{Binning\;%d}$' % i)

    if truth_analysis is not None:
        path = os.path.join(output_path, 'truth')
        z_scores_truth = load_z_scores(path, 100)

    if nn_analysis is not None:
        path = os.path.join(output_path, 'nn')
        z_scores_nn = load_z_scores(path, 100)



        a = np.array([7.20387174, 129.1453496, -6.57299899])
        b = np.array([9.12224061, 47.0915748, 0.0468278945])

        def ellipse(x, y, a, b, c):
            return a * x ** 2 + b * y ** 2 + c * x * y

        # cntr_nn = ax.contour(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane,
        #                      ellipse(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane, *a), levels=[1.64],
        #                      colors='C0')
        # cntr_truth = ax.contour(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane,
        #                         ellipse(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane, *b), levels=[1.64],
        #                         colors='C1')

    ax.legend(contours, labels, fontsize=15, frameon=False, loc='best')
    ax.set_ylim(-0.2, 0.2)
    ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
    ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
    ax.set_title(r'$\rm{Expected\;exclusion\;limits}$', fontsize=20)


if __name__ == '__main__':

    mc_run = sys.argv[1]

    #################
    # binned analysis
    #################

    # define the binnings
    binning_0 = np.append(np.linspace(1000, 2000, 8), 4000).astype(int)
    binning_1 = np.append(np.linspace(1000, 2000, 4), 4000).astype(int)
    binning_2 = np.append(np.linspace(1000, 2000, 1), 4000).astype(int)

    binnings_list = [binning_0, binning_1, binning_2]

    # run a binned analysis on each of the binnings
    extent = np.array([[-1.2, 1.2], [-0.15, 0.2]])
    binned_analyses = run_binned_analysis(binnings_list, extent, fit=False, luminosity=6)

    # plot accuracy of Asimov method
    fig = bounds.plot_tc_accuracy(binned_analyses, c=np.array([1.0, 0]), n=10000)
    fig.savefig(os.path.join(plots_path, 'tc_comp.pdf'))


    ################
    # combined analysis
    ################
    combine_analyses(binned_analyses, truth_analysis, nn_analysis)










