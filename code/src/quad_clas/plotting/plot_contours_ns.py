import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import arviz as az
import pymultinest
import json

# load posterior samples
path_to_samples = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/ns/posterior.json'
with open(path_to_samples) as json_data:
    samples_json = json.load(json_data)
