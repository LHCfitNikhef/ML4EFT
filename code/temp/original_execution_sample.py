"""
This file contains a legacy sample approach to implementing reweighting in the
ML4EFT framework.

"""
import json
import os
import time

import ml4eft.core.classifier as classifier
import ml4eft.analyse.analyse as analyse


##### SETTINGS #####
coeffs = [#'cHu',
			"ctGRe"]#_ctGRe"]
output_dir = "/data/theorie/wgautier/wgautier/followup/models/no_weights"
runcard = "/data/theorie/wgautier/wgautier/followup/runcards/train_test_tt.json"
options = {
	"update_runcard": False,
	"fit": True,
	"display_loss": False
}

##### update runcard with n datapoints #####
if options["update_runcard"]:
	with open(runcard) as json_runcard:
		json_runcard_loaded = json.load(json_runcard)

	# set number of data points (varies per dataset)
	with open(f"{json_runcard_loaded['event_data']}/../len_data.txt", "r") as file:
		len_data = int(file.read())

	# update runcard
	with open(runcard, 'w') as runcard_updated:
		json.dump(json_runcard_loaded, runcard_updated)
##########


##### initialise fitting #####
if options["fit"]:
	for coefficient in coeffs:
			fitter = classifier.Fitter(
				json_path = runcard,
				mc_run = 1,
				c_name = coefficient, 
				output_dir = output_dir,
				print_log=True
			)
##########


##### display loss of first  #####
# TODO: latex error, build own display func
if options["display_loss"]:
	# ONLY IF MODELS TRAINED TODAY
	path_to_models_root = os.path.join(output_dir, time.strftime("%Y/%m/%d"))
	
	order = 'lin' # or quad when quadratic models have been trained

	models_paths_dict = analyse.Analyse.build_path_dict(root=path_to_models_root,
							order=order,
							prefix='model')

	analyser = analyse.Analyse(models_paths_dict, order, all=True)
	fig, _ = analyser.plot_loss_overview(coeffs[0], 
										order, 
										xlim=5)