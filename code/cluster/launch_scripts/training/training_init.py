import sys
import quad_clas.core.classifier as classifier

# training settings
path_to_json = '/data/theorie/jthoeve/ML4EFT_higgs/code/launch_scripts/run_cards/run_card_lin_pt.json'
nn_rep = sys.argv[1]

# model directory
output_path = '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/24_01'

# launch fit
fitter = classifier.Fitter(path_to_json, nn_rep, output_path)