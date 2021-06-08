import bounds
import sys
import numpy as np
#from scipy.ndimage.filters import gaussian_filter

def run_bounds_binned():

    # define bin choices here
    binning_0 = np.append(np.linspace(340, 1000, 40), 4000).astype(int)
    binning_1 = np.append(np.linspace(340, 1000, 20), 4000).astype(int)
    binning_2 = np.append(np.linspace(340, 1000, 10), 4000).astype(int)
    binning_3 = np.append(np.linspace(340, 1000, 5), 4000).astype(int)
    binning_4 = np.append(np.linspace(340, 1000, 2), 4000).astype(int)
    binning_5 = np.append(np.linspace(340, 1000, 1), 4000).astype(int)

    # each bin choice gets associated its own directory
    path_output_bin_0 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_0'
    path_output_bin_1 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_1'
    path_output_bin_2 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_2'
    path_output_bin_3 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_3'
    path_output_bin_4 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_4'
    path_output_bin_5 = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned_test_v3/bin_5'

    # limits = np.array([[-1.2, 1.2], [-0.15, 0.2]])

    # construct a list of StatAnalysis instances, each having a different bin choice
    binned_analysis = []
    binning = [binning_0, binning_1, binning_2, binning_3, binning_4, binning_5]
    path_output = [path_output_bin_0, path_output_bin_1, path_output_bin_2, path_output_bin_3, path_output_bin_4,
                   path_output_bin_5]
    for i in range(len(binning)):
        binned_analysis.append(bounds.StatAnalysis(path_output=path_output[i], bins=binning[i], fit=False))

    # change the luminosity like this
    # StatAnalysis.luminosity = 6*10
    bounds.plot_tc_accuracy(binned_analysis, path_save='/data/theorie/jthoeve/ML4EFT/quad_clas/plots/tc_accuracy.pdf')


    # TODO: finish the below on 07/06

    # # bin_1.plot_binned_analysis(path_save='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores_heatmap_bin_3.pdf')
    #
    #
    #
    # sigma = 0.8  # this depends on how noisy your data is, play with it!
    #
    # data_bin0 = gaussian_filter(bin_0.z_scores_asi, sigma)
    # data_bin1 = gaussian_filter(bin_1.z_scores_asi, sigma)
    # data_bin2 = gaussian_filter(bin_2.z_scores_asi, sigma)
    # data_bin3 = gaussian_filter(bin_3.z_scores_asi, sigma)
    #
    # fig, ax = plt.subplots(figsize=(10, 6))
    # cntr0 = ax.contour(bin_1.cuu_plane, bin_0.cug_plane, data_bin0, levels=np.array([1.64]), colors='C3')
    # cntr1 = ax.contour(bin_1.cuu_plane, bin_1.cug_plane, data_bin1, levels=np.array([1.64]), colors='C0')
    # cntr2 = ax.contour(bin_2.cuu_plane, bin_2.cug_plane, data_bin2, levels=np.array([1.64]), colors='C1')
    # cntr3 = ax.contour(bin_3.cuu_plane, bin_3.cug_plane, bin_3.z_scores_asi, levels=np.array([1.64]), colors='C2')
    #
    # h0, _ = cntr0.legend_elements()
    # h1, _ = cntr1.legend_elements()
    # h2, _ = cntr2.legend_elements()
    # h3, _ = cntr3.legend_elements()
    # ax.legend([h0[0], h1[0], h2[0], h3[0]], [r'$\rm{Bin\;0}$', r'$\rm{Bin\;1}$', r'$\rm{Bin\;2}$', r'$\rm{Bin\;3}$'])
    # # ax.legend([h3[0]], [r'$\rm{Bin\;3}$'])
    # ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
    # ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
    # ax.set_title(r'$\rm{Expected\;exclusion\;limits}$', fontsize=20)
    #
    # plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/exclusion_limit_bin_all_v3.pdf')


if __name__ == '__main__':

    mc_run = sys.argv[1]

    # example input
    # dict_int = {(0, -0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_1.lhe',
    #             (0, -0.45): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_2.lhe',
    #             (0, -0.50): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_3.lhe',
    #             (0, -0.55): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_4.lhe',
    #             (0, -0.60): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/mcuu/eft_5.lhe'}

    dict_int = {(0.01, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pcug/eft_1.lhe',
                (0.05, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pcug/eft_2.lhe',
                (0.1, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pcug/eft_3.lhe',
                (0.3, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/pcug/eft_4.lhe'}


    path_output_nn = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/nn/cug'
    path_output_truth = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/truth/cug'

    # run bounds nn
    bounds.StatAnalysis(path_output=path_output_nn, dict_int=dict_int, nn=True, mc_run=mc_run)

    # run bounds truth
    bounds.StatAnalysis(path_output=path_output_truth, dict_int=dict_int, nn=False, mc_run=mc_run)

    # run bounds binned
    #run_bounds_binned()


