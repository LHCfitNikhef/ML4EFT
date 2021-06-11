import bounds
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter

def run_bounds_binned():

    # define bin choices here
    #binning_0 = np.append(np.linspace(340, 1500, 50), 4000).astype(int)
    #binning_1 = np.append(np.linspace(340, 1500, 20), 4000).astype(int)
    #binning_2 = np.append(np.linspace(340, 1000, 10), 4000).astype(int)
    binning_3 = np.append(np.linspace(1000, 2000, 8), 4000).astype(int)
    binning_4 = np.append(np.linspace(1000, 2000, 4), 4000).astype(int)
    binning_5 = np.append(np.linspace(1000, 2000, 1), 4000).astype(int)

    # each bin choice gets associated its own directory
    #path_output_bin_0 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v5/bin_0'
    #path_output_bin_1 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v5/bin_1'
    #path_output_bin_2 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v5/bin_2'
    path_output_bin_3 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v7/bin_3'
    path_output_bin_4 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v7/bin_4'
    path_output_bin_5 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v7/bin_5'

    # limits = np.array([[-1.2, 1.2], [-0.15, 0.2]])

    # construct a list of StatAnalysis instances, each having a different bin choice
    binned_analysis = []
    #binning = [binning_0, binning_1, binning_2, binning_3, binning_4, binning_5]
    binning = [binning_3, binning_4, binning_5]
    path_output = [path_output_bin_3, path_output_bin_4,
                   path_output_bin_5]
    for i in range(len(binning)):
        binned_analysis.append(bounds.StatAnalysis(path_output=path_output[i], bins=binning[i], fit=False))
        #binned_analysis.append(bounds.StatAnalysis(path_output=path_output[i], bins=binning[i], fit=False))

    # change the luminosity like this
    # StatAnalysis.luminosity = 6*10
    bounds.plot_tc_accuracy(binned_analysis, path_save='/data/theorie/jthoeve/ML4EFT/quad_clas/plots/tc_accuracy_v8.pdf')
    sys.exit()


    # TODO: finish the below on 07/06

    # # bin_1.plot_binned_analysis(path_save='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores_heatmap_bin_3.pdf')
    #
    #
    #
    sigma = 0.8  # this depends on how noisy your data is, play with it!
    #
    #
    data_bin0 = gaussian_filter(binned_analysis[0].z_scores_asi, sigma)
    data_bin1 = gaussian_filter(binned_analysis[1].z_scores_asi, sigma)
    data_bin2 = gaussian_filter(binned_analysis[2].z_scores_asi, sigma)

    #
    fig, ax = plt.subplots(figsize=(10, 6))
    cntr0 = ax.contour(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane, data_bin0, levels=np.array([1.64]), colors='C2')
    cntr1 = ax.contour(binned_analysis[1].cuu_plane, binned_analysis[1].cug_plane, data_bin1, levels=np.array([1.64]), colors='C3')
    cntr2 = ax.contour(binned_analysis[2].cuu_plane, binned_analysis[2].cug_plane, data_bin2, levels=np.array([1.64]), colors='C4')

    #
    a = np.array([7.20387174, 129.1453496, -6.57299899])
    b = np.array([9.12224061, 47.0915748, 0.0468278945])


    def ellipse(x, y, a, b, c):
        return a * x ** 2 + b * y ** 2 + c * x * y

    cntr_nn = ax.contour(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane, ellipse(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane, *a), levels=[1.64], colors='C0')
    cntr_truth = ax.contour(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane,
                         ellipse(binned_analysis[0].cuu_plane, binned_analysis[0].cug_plane, *b), levels=[1.64],
                         colors='C1')
    h0, _ = cntr_nn.legend_elements()
    h1, _ = cntr_truth.legend_elements()
    h2, _ = cntr0.legend_elements()
    h3, _ = cntr1.legend_elements()
    h4, _ = cntr2.legend_elements()

    ax.legend([h0[0], h1[0], h2[0], h3[0], h4[0]], [r'$\rm{NN}$', r'$\rm{Truth}$', r'$\rm{Binning\;0}$', r'$\rm{Binning\;1}$', r'$\rm{Binning\;2}$'], fontsize=15, frameon=False, loc='best')
    # ax.legend([h3[0]], [r'$\rm{Bin\;3}$'])
    ax.set_ylim(-0.2, 0.2)
    ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
    ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
    ax.set_title(r'$\rm{Expected\;exclusion\;limits}$', fontsize=20)

    plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/nn_bins.pdf')


if __name__ == '__main__':

    mc_run = sys.argv[1]

    dict_int = {(0, -0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_1.lhe',
                (0, -0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_2.lhe',
                (0, -0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_3.lhe',
                (0, -0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_4.lhe',
                (0, 0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_5.lhe',
                (0, 0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_6.lhe',
                (0, 0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_7.lhe',
                (0, 0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_8.lhe',
                (-0.15, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_9.lhe',
                (-0.12, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_10.lhe',
                (-0.09, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_11.lhe',
                (-0.06, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_12.lhe',
                (0.06, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_13.lhe',
                (0.09, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_14.lhe',
                (0.12, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_15.lhe',
                (0.15, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_16.lhe',
                (-0.07, -0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_17.lhe',
                (-0.06, -0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_18.lhe',
                (-0.05, -0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_19.lhe',
                (-0.04, -0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_20.lhe',
                (0.04, 0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_21.lhe',
                (0.05, 0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_22.lhe',
                (0.06, 0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_23.lhe',
                (0.07, 0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_24.lhe'
                }


    path_output_nn = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn/'
    path_output_truth = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth/run_2'

    # run bounds nn
    #nn = bounds.StatAnalysis(path_output=path_output_nn, dict_int=dict_int, nn=True, mc_run=mc_run, fit=False)

    # run bounds truth
    #truth = bounds.StatAnalysis(path_output=path_output_truth, dict_int=dict_int, nn=False, mc_run=mc_run)

    # run bounds binned
    run_bounds_binned()


