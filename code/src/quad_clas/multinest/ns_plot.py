import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import arviz as az
import pymultinest
import json

# load posterior samples
path_to_samples = '/data/theorie/jthoeve/multinest/demo/example/ns_run/truth/posterior.json'
with open(path_to_samples) as json_data:
    samples_json = json.load(json_data)

# load chi2 bounds
mu_low, mu_high = np.load('/data/theorie/jthoeve/multinest/demo/example/grid_scan/bounds.npy')

prefix = '/data/theorie/jthoeve/multinest/demo/example/ns_run/truth/truth-'

samples_unweighted= samples_json['cHq3']

mu_low_ns_unweighted = np.percentile(samples_unweighted, 16)
mu_high_ns_unweighted = np.percentile(samples_unweighted, 84)

# plotting setup
fig = plt.figure()
plt.hist(samples_unweighted, bins=200, histtype='stepfilled', alpha=0.3, ec='k', density=True)
plt.axvline(mu_low, 0, 1, color='C0', label='$\chi^2$')
plt.axvline(mu_high, 0, 1, color='C0')
plt.axvline(mu_low_ns_unweighted, 0, 1, linestyle='dotted', color='C2', label='NS')
plt.axvline(mu_high_ns_unweighted, 0, 1, linestyle='dotted', color='C2')
sns.kdeplot(x=samples_unweighted, color='red', bw_adjust=1.5, label='kde')

x_min = np.percentile(samples_unweighted, 1)
x_max = np.percentile(samples_unweighted, 99)

plt.xlabel(r'$\theta_0$')
plt.ylabel('')
plt.legend()
plt.xlim((x_min, x_max))
fig.savefig('/data/theorie/jthoeve/multinest/demo/example/sample_dist_3.pdf')