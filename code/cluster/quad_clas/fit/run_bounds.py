import os, sys
from ..core import bounds as bounds


root_path = '/data/theorie/jthoeve/ML4EFT/'
output_path = os.path.join(root_path, 'output')
plots_path = os.path.join(output_path, 'plots')
paths = {'root': root_path, 'output': output_path, 'plots': plots_path}

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


def run_truth_analysis(mc_run, fit, luminosity):
    paths['output'] = os.path.join(output_path, 'truth')
    truth = bounds.StatAnalysis(paths, dict_int=dict_int, nn=False, mc_run=mc_run, fit=fit, luminosity=luminosity)
    return truth


def run_nn_analysis(mc_run, fit, luminosity):
    paths['output'] = os.path.join(output_path, 'nn')
    nn = bounds.StatAnalysis(paths, dict_int=dict_int, nn=True, mc_run=mc_run, fit=fit, luminosity=luminosity)
    return nn


if __name__ == '__main__':

    mc_run = sys.argv[1]

    #################
    # truth analysis
    #################
    truth_analysis = run_truth_analysis(mc_run, fit=True, luminosity=6)

    #################
    # nn analysis
    #################
    #nn_analysis = run_nn_analysis(mc_run, fit=True, luminosity=6)
