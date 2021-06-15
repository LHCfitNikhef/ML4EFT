import numpy as np
import sys
import quad_clas.analyse.analyse as ana
import quad_clas.fit.run_bounds as run

root_path = '/data/theorie/jthoeve/ML4EFT/'

if __name__ == "__main__":

    scan = False
    analyse = True

    if scan:
        mc_run = sys.argv[1]

        # interpolation dictionary for nn and truth analysis
        # dict_int = {(0, -0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_1.lhe',
        #                 (0, -0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_2.lhe',
        #                 (0, -0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_3.lhe',
        #                 (0, -0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_4.lhe',
        #                 (0, 0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_5.lhe',
        #                 (0, 0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_6.lhe',
        #                 (0, 0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_7.lhe',
        #                 (0, 0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_8.lhe',
        #                 (-0.15, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_9.lhe',
        #                 (-0.12, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_10.lhe',
        #                 (-0.09, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_11.lhe',
        #                 (-0.06, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_12.lhe',
        #                 (0.06, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_13.lhe',
        #                 (0.09, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_14.lhe',
        #                 (0.12, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_15.lhe',
        #                 (0.15, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_16.lhe',
        #                 (-0.07, -0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_17.lhe',
        #                 (-0.06, -0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_18.lhe',
        #                 (-0.05, -0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_19.lhe',
        #                 (-0.04, -0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_20.lhe',
        #                 (0.04, 0.4): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_21.lhe',
        #                 (0.05, 0.5): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_22.lhe',
        #                 (0.06, 0.6): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_23.lhe',
        #                 (0.07, 0.7): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_24.lhe'
        #                 }
        dict_int = {(0.06, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_13.lhe',
                    (0.09, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_14.lhe',
                    (0.12, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_15.lhe',
                    (0.15, 0): '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/eft_16.lhe'
                    }

        run.ScanBounds(root_path, dict_int, mc_run, luminosity=6, truth=True, nn=False, fit=False)

    if analyse:
        #define the binnings
        binning_0 = np.append(np.linspace(340, 1000, 8), 4000).astype(int)
        binning_1 = np.append(np.linspace(340, 1000, 4), 4000).astype(int)
        binning_2 = np.append(np.linspace(340, 1000, 1), 4000).astype(int)

        binnings_list = [binning_0, binning_1, binning_2]

        extent = np.array([[-1.2, 1.2], [-0.3, 0.3]])
        analysis = ana.Analyse(root_path, nn=True, truth=True, fit=False, extent=extent)