import sys
import ml4eft.core.classifier as classifier

# training settings

path_to_json = sys.argv[1]
nn_rep = sys.argv[2]
coeff = sys.argv[3]

# model directory
output_path = './models/tt_llvlvlbb'

# launch fit
fitter = classifier.Fitter(path_to_json, int(nn_rep), coeff, output_path)