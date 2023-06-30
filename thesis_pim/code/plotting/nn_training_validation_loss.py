# This code automizes the plotting of the validation loss vs training loss from all the neural networks


import wget
import tarfile
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import sys

import ml4eft.core.classifier as classifier
import ml4eft.analyse.analyse as analyse
import ml4eft.plotting.features as features

rc('text', usetex=False)
rc('font', **{'family': 'DejaVu Sans', 'size': 22})

typp = ["hard", "event"]

coeff=["cQd8", "cQd8_ctGRe", "cQj18_cQu8", "cQj38", "cQj38_ctj8", "cQu8_ctj8", "ctd8_ctj8", "ctj8", "cQd8_cQd8", "cQd8_ctj8", "cQj18_ctd8", "cQj38_cQj38", "cQj38_ctu8", "cQu8_ctu8", "ctGRe", "ctj8_ctj8", "cQd8_cQj18", "cQj18", "cQj18_ctGRe", "cQj38_cQu8", "cQu8", "ctd8", "ctGRe_ctGRe", "ctj8_ctu8", "cQd8_cQj38", "cQj18_cQj18", "cQj18_ctj8", "cQj38_ctd8", "ctd8_ctd8", "ctGRe_ctj8", "ctu8", "cQd8_ctd8", "cQj18_cQj38", "cQj18_ctu8", "cQj38_ctGRe", "cQu8_ctGRe", "ctd8_ctGRe", "ctGRe_ctu8", "ctu8_ctu8", "cQu8_cQu8"]


# for typ in typp:
for c_name in coeff:
    path_to_models_root = "/data/theorie/pherbsch/ML4EFT/subproj/output/models/FSR_ISR_MPI/quad_ptll_etal12/" +str(typ) +  "/2023/05/25"
    order = 'quad' # or quad when quadratic models have been trained

    models_paths_dict = analyse.Analyse.build_path_dict(root=path_to_models_root,
                            order=order,
                            prefix='model')

    analyser = analyse.Analyse(models_paths_dict, order, all=True)


    fig, _ = analyser.plot_loss_overview(c_name, order, xlim=100)

    path_to_save = "/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/validation_loss_tests/quad_2feat" +str (typ) + "_" + str(c_name) + ".png"
    fig.savefig(path_to_save)

