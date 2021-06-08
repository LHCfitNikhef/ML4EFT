import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from matplotlib import rc
import csv
import sys
import pandas as pd


#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

def stdom(x):
    return np.std(x) / np.sqrt(len(x))

def wavg(group):
    z = group['z-score']
    sigma_z = group['uncertainty']
    z_wavg = ((z / sigma_z ** 2).sum()) / ((1 / sigma_z ** 2).sum())
    z_wavg_unc = 1 / ((1 / sigma_z ** 2).sum())
    return pd.Series({'z-score': z_wavg, 'uncertainty': z_wavg_unc})

#nn

mc_runs = 100
z_scores = []
for i in range(1, mc_runs + 1):
    path = "z_scores/nn/cug/mc_run_{}/z_scores.dat".format(i)
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            z_scores.append([float(value) for value in line])

z_scores_nn = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score', 'uncertainty'])
z_scores_nn_grouped = z_scores_nn.groupby(['cug', 'cuu'])
z_scores_nn_grouped = z_scores_nn_grouped.apply(wavg)
z_scores_nn_grouped = z_scores_nn_grouped.reset_index()

#truth
z_scores_truth = []
for i in range(1, mc_runs + 1):
    path = "z_scores/truth/cug/mc_run_{}/z_scores.dat".format(i)
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            z_scores_truth.append([float(value) for value in line])

z_scores_truth = pd.DataFrame(z_scores_truth, columns=['cug', 'cuu', 'z-score'])
z_scores_truth_grouped = z_scores_nn.groupby(['cug', 'cuu']).agg({'z-score': ['mean', stdom]})
z_scores_truth_grouped.columns = ['z-score', 'uncertainty']
z_scores_truth_grouped = z_scores_truth_grouped.reset_index()


cuu = z_scores_nn_grouped.cuu.values
cug = z_scores_nn_grouped.cug.values
z_score_truth = z_scores_truth_grouped['z-score'].values
z_score_unc_truth = z_scores_truth_grouped['uncertainty'].values

z_score_nn = z_scores_nn_grouped['z-score'].values
z_score_unc_nn = z_scores_nn_grouped['uncertainty'].values

plt.figure(figsize=(10, 6))
ax = plt.subplot(111)

ax.errorbar(cug, z_score_truth, yerr=z_score_unc_truth, fmt='.', capsize=3,
             color='C0', label=r'$\rm{z-score\;(truth)}$')

ax.errorbar(cug, z_score_nn, yerr=z_score_unc_nn, fmt='.', capsize=3,
            color='C1', label=r'$\rm{z-score\;(NN)}$')


# fit a quadratic polynomial
def quad_pol(x, a, b, c):
    return a * x ** 2 + b * x + c


popt_truth, _ = curve_fit(quad_pol, cug, z_score_truth, sigma=z_score_unc_truth)
popt_nn, _ = curve_fit(quad_pol, cug, z_score_nn, sigma=z_score_unc_nn)

epsilon = 0.1*(np.max(cug) - np.min(cug))
xmin = np.min(cug) - epsilon
xmax = np.max(cug) + epsilon
x = np.linspace(xmin, xmax, 400)

plt.hlines(1.64, xmin, xmax, color='black', linestyle='dashed')
ax.plot(x, quad_pol(x, *popt_truth), color='C0', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(true)}$')
ax.plot(x, quad_pol(x, *popt_nn), color='C1', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(NN)}$')

idx_truth = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_truth) - 1.64))).flatten()
idx_nn = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_nn) - 1.64))).flatten()

plt.plot(x[idx_nn], quad_pol(x[idx_nn], *popt_nn), 'kx')
plt.plot(x[idx_truth], quad_pol(x[idx_truth], *popt_truth), 'kx')

# Plot settings
ax.set_ylabel(r'$\rm{z-score}$', fontsize=20)
ax.set_xlabel(r'$\rm{cug}$', fontsize=20)
ax.set_xlim((xmin, xmax))

epsilon = 0.1*(np.max(z_score_nn) - np.min(z_score_nn))
ymin = np.min([z_score_nn.min() - epsilon, z_score_nn.min() - epsilon])
ymax = np.max([z_score_nn.max() + epsilon, z_score_nn.max() + epsilon])

ax.set_ylim((ymin, ymax))
ax.legend(loc='best', fontsize=15, frameon=False)
ax.tick_params(which='both', direction='in', labelsize=20)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', length=5)
ax.set_title(r'$\rm{Interpolation\;of\;z-score}$', fontsize=20)
plt.tight_layout()
plt.show()
#plt.savefig('p_value_int_comp.pdf')



