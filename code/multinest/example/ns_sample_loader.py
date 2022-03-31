import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import arviz as az

file = '/data/theorie/jthoeve/multinest/demo/example/ns_run/samples.txt'
file_unweighted = '/data/theorie/jthoeve/multinest/demo/example/ns_run/samplespost_equal_weights.dat'
mu_low, mu_high = np.load('/data/theorie/jthoeve/multinest/demo/example/grid_scan/bounds.npy')

samples = np.array([float(x.split()[-1]) for x in open(file).readlines()])
#weights = np.array([float(x.split()[0]) for x in open(file).readlines()])

samples_unweighted = np.array([float(x.split()[0]) for x in open(file_unweighted)])

# df = pd.DataFrame({'samples': samples, 'weights': weights})
#
# total_weight = df.weights.sum()
# p_low = 0.16 * total_weight
# p_high = 0.84 * total_weight
#
# sort_samp_idx = np.argsort(samples)
# weights_sorted = np.cumsum(weights[sort_samp_idx])
# idx_low = np.argwhere(weights_sorted > p_low).min()
# idx_high = np.argwhere(weights_sorted > p_high).min()
#
# mu_low_ns = samples[sort_samp_idx][idx_low]
# mu_high_ns = samples[sort_samp_idx][idx_high]

mu_low_ns_unweighted = np.percentile(samples_unweighted, 16)
mu_high_ns_unweighted = np.percentile(samples_unweighted, 84)


fig = plt.figure()
#plt.hist(samples, bins=300, weights=df.weights, histtype='stepfilled', alpha=0.3, ec='k', density=True)
plt.hist(samples_unweighted, bins=200, histtype='stepfilled', alpha=0.3, ec='k', density=True)
plt.axvline(mu_low, 0, 1, color='C0', label='$\chi^2$')
plt.axvline(mu_high, 0, 1, color='C0')
#plt.axvline(mu_low_ns, 0, 1, linestyle='dotted')
#plt.axvline(mu_high_ns, 0, 1, linestyle='dotted')
plt.axvline(mu_low_ns_unweighted, 0, 1, linestyle='dotted', color='C1', label='NS')
plt.axvline(mu_high_ns_unweighted, 0, 1, linestyle='dotted', color='C1')


#az.plot_kde(samples, quantiles=[0.16, 0.84])
sns.kdeplot(x=samples_unweighted, color='red', bw_adjust=1.5, label='kde')


#sns.rugplot(np.random.choice(samples, size=100, replace=False))
plt.xlabel(r'$\theta_0$')
plt.ylabel('')
plt.legend()
plt.xlim((3.8, 4.5))
fig.savefig('/data/theorie/jthoeve/multinest/demo/example/sample_dist.pdf')