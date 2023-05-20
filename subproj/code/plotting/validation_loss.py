import wget
import tarfile
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

import ml4eft.core.classifier as classifier
import ml4eft.analyse.analyse as analyse
import ml4eft.plotting.features as features

rc('text', usetex=False)
rc('font', **{'family': 'DejaVu Sans', 'size': 22})

# typp = ["hard"]
# coeff = ["ctd8", "cQj18", "cQu8", "ctj8", "ctGRe"]

# for typ in typp:
#     for c_name in coeff:
#         path_to_models_root = "/data/theorie/pherbsch/ML4EFT/subproj/output/models/" +str(typ) +  "/2023/05/18"
#         order = 'lin' # or quad when quadratic models have been trained

#         models_paths_dict = analyse.Analyse.build_path_dict(root=path_to_models_root,
#                                 order=order,
#                                 prefix='model')

#         analyser = analyse.Analyse(models_paths_dict, order, all=True)


#         fig, _ = analyser.plot_loss_overview(c_name, order, xlim=150)

#         path_to_save = "/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/validation_loss_tests/" +str (typ) + "_" + str(c_name) + ".png"
#         fig.savefig(path_to_save)

# coeff = ["ctd8", "cQj18", "cQu8", "ctj8", "ctGRe"]
coeff = ["ctj8"]


for c_name in coeff:
    path_to_models_root = "/data/theorie/pherbsch/ML4EFT/subproj/output/models/event/2023/05/19"
    order = 'lin' # or quad when quadratic models have been trained

    models_paths_dict = analyse.Analyse.build_path_dict(root=path_to_models_root,
                            order=order,
                            prefix='model')

    analyser = analyse.Analyse(models_paths_dict, order, all=True)


    fig, _ = analyser.plot_loss_overview(c_name, order, xlim=150)

    path_to_save = "/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/validation_loss_tests/" "event" "_" + str(c_name) + ".png"
    fig.savefig(path_to_save)