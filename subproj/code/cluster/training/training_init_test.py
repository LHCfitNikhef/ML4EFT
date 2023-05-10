import sys
import ml4eft.core.classifier as classifier

path_to_json = sys.argv[1]
nn_rep = sys.argv[2]
coeff = sys.argv[3]

# model directory
output_path = '/data/theorie/pherbsch/ML4EFT/subproj/code/cluster/test/models'

# launch fit
fitter = classifier.Fitter(path_to_json, int(nn_rep), coeff, output_path)