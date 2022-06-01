import sys
import quad_clas.core.classifier as classifier

# training settings
#path_to_json = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/tt/run_card_tt_mtt_y_pt.json'
path_to_json = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/zh/run_card_zh_mzh_y.json'
nn_rep = sys.argv[1]

# model directory
output_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh'

# launch fit
fitter = classifier.Fitter(path_to_json, nn_rep, output_path)