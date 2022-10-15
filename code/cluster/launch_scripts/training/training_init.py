import sys
import ml4eft.core.classifier as classifier

# training settings

# tt
#path_to_json = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/tt/run_card_tt_quad.json'

# zh
#path_to_json = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/zh/run_card_zh_mzh_y.json'

# zh llbb
#path_to_json = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/zh_llbb/run_card_zh_llbb_chw.json'

path_to_json = sys.argv[1]
nn_rep = sys.argv[2]

# model directory
output_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt'

# launch fit
fitter = classifier.Fitter(path_to_json, int(nn_rep), output_path)