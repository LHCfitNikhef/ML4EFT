import numpy as np
import sys
import quad_clas.analyse.analyse as ana
import quad_clas.fit.run_bounds as run
import quad_clas.core.quad_classifier_cluster as train
import quad_clas.core.analyse as plot
import quad_clas.preproc.lhe_to_npy as lhe_to_npy

import matplotlib
matplotlib.use('Agg')
root_path = '/data/theorie/jthoeve/ML4EFT_v2/'
#root_path = '/Users/jaco/Documents/ML4EFT/code'

if __name__ == "__main__":

    lhe_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/sm_events.lhe'
    save_path = '/Users/jaco/Documents/ML4EFT/code/output/plots/xsec_dist/vegas_check.pdf'
    # # plot_mg5_ana_mtt(30*10**-3, 2.5, 1, 0, lhe_path, save_path)
    plot.plot_xsec_ana(10 * 10 ** -3, 2.5, 0, 0, lhe_path, save_path)
    sys.exit()
    # plot.plot_mg5_ana_mtt(30 * 10 ** -3, 2.5, 0, 0, lhe_path, save_path)

    #lhe_to_npy.lhe_to_npy(n_processes=18)
    #sys.exit()

    #network_size = [1, 30, 30, 30, 30, 30, 1]

    #plot_pull_heatmap(network_size, [1.50, 1.80, 2.10, 2.40, 3.00, 3.50])
    #plot.plot_predictions_1d(network_size)
    #mc_run = sys.argv[1]
    #train.start(json_path='/data/theorie/jthoeve/ML4EFT_v2/cluster/launch_scripts/run_card_cluster.json', mc_run=str(mc_run))




    #
    #
    # #print(plt.get_backend())
    scan = False
    analyse = True

    if scan:
        mc_run = sys.argv[1]

        # interpolation dictionary for nn and truth analysis
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

        run.ScanBounds(root_path, dict_int, mc_run, luminosity=6, truth=False, nn=True, fit=False)

    if analyse:
        #define the binnings
        binning_0 = np.append(np.linspace(340, 2000, 20), 4000).astype(int)
        binning_1 = np.append(np.linspace(340, 2000, 10), 4000).astype(int)
        binning_2 = np.append(np.linspace(340, 2000, 5), 4000).astype(int)
        binning_3 = np.append(np.linspace(340, 2000, 2), 4000).astype(int)
        binning_4 = np.append(np.linspace(340, 2000, 1), 4000).astype(int)

        binnings_list = [binning_0, binning_1, binning_2, binning_3, binning_4]

        extent = np.array([[-1.2, 1.2], [-0.3, 0.3]])
        analysis = ana.Analyse(root_path, nn=True, truth=True, fit=False, extent=extent, luminosity=6)