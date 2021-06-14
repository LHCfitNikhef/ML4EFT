import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from matplotlib import rc
import csv
import sys, os
import pandas as pd
from scipy.stats import norm


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


def load_z_scores(path, mc_runs):
    """ Load the z-scores for all the mc runs

    Parameters
    ----------
    path: root path to z-scores file
    mc_runs: number of monte carlo runs to load

    Returns
    -------
    Pandas dataframe
    """
    z_scores = []
    for i in range(1, mc_runs + 1):
        loc = os.path.join(path, "mc_run_{}/z_scores.dat".format(i))
        with open(loc, "r") as f:
            reader = csv.reader(f, delimiter='\t')
            for line in reader:
                z_scores.append([float(value) for value in line])

    if 'nn' in path:
        z_scores = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score', 'uncertainty'])
        z_scores_grouped = z_scores.groupby(['cug', 'cuu'])
        z_scores_grouped = z_scores_grouped.apply(wavg)
        z_scores_grouped = z_scores_grouped.reset_index()
    else:
        z_scores = pd.DataFrame(z_scores, columns=['cug', 'cuu', 'z-score'])
        z_scores_grouped = z_scores.groupby(['cug', 'cuu']).agg({'z-score': ['mean', stdom]})
        z_scores_grouped.columns = ['z-score', 'uncertainty']
        z_scores_grouped = z_scores_grouped.reset_index()
    return z_scores_grouped

# def pvalue(group):
#     z = group['z-score']
#     p = 1 - norm.cdf(z)
#     p_avg = np.mean(p)
#     p_unc = np.std(p) / np.sqrt(len(p))
#     return pd.Series({'p-value': p_avg, 'uncertainty': p_unc})


# z_scores_truth = load_z_scores('z_scores/truth/', 100)
# z_scores_truth_grouped = z_scores_truth.groupby(['cug', 'cuu'])
# z_scores_truth_grouped = z_scores_truth_grouped.apply(pvalue)
# z_scores_truth_grouped = z_scores_truth_grouped.reset_index()
# print(z_scores_truth_grouped)
# sys.exit()

z_scores_nn = load_z_scores('z_scores/nn/', 100)
z_scores_truth = load_z_scores('z_scores/truth/run_2', 100)


cuu = z_scores_nn.cuu.values
cug = z_scores_nn.cug.values

z_score_truth = z_scores_truth['z-score'].values
z_score_unc_truth = z_scores_truth['uncertainty'].values

z_score_nn = z_scores_nn['z-score'].values
z_score_unc_nn = z_scores_nn['uncertainty'].values

eft_points = np.array([cug, cuu]).T




def coefficient_matrix(eft_points):
    matrix = []
    for c in eft_points:
        cug = c[0]
        cuu = c[1]
        row = [cuu**2, cug**2, cug*cuu]
        matrix.append(row)
    return np.array(matrix)

coeff_mat = coefficient_matrix(eft_points)



# solve the linear equation xsec = coeff_matrix * a for a
a_nn, _, _, _ = np.linalg.lstsq(coeff_mat, z_score_nn, rcond=None)
a_truth, _, _, _ = np.linalg.lstsq(coeff_mat, z_score_truth, rcond=None)

print(a_nn)
print(a_truth)
sys.exit()


def ellipse(x, y, a, b, c):
    return a*x**2 + b*y**2 + c*x*y

x = np.linspace(-3, 3, 100)
y = np.linspace(-0.15, 0.4, 100)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(10, 6))
ax = plt.subplot(111)

cntr0 = ax.contour(X, Y, ellipse(X, Y, *a_nn), levels = [1.64], colors ='C0')
cntr1 = ax.contour(X, Y, ellipse(X, Y, *a_truth), levels = [1.64], colors ='C1')

h0, _ = cntr0.legend_elements()
h1, _ = cntr1.legend_elements()

ax.legend([h0[0], h1[0]], [r'$\rm{NN}$', r'$\rm{Truth}$'])
ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
ax.set_ylabel(r'$\rm{cug}$', fontsize=20)
ax.set_title(r'$\rm{Expected\;exclusion\;limits}$', fontsize=20)

plt.show()
#
# sys.exit()

z_scores_nn_pcuu = z_scores_nn[(z_scores_nn['cug'] == 0) & (z_scores_nn['cuu'] > 0)]
z_scores_nn_ncuu = z_scores_nn[(z_scores_nn['cug'] == 0) & (z_scores_nn['cuu'] < 0)]
z_scores_nn_pcug = z_scores_nn[(z_scores_nn['cuu'] == 0) & (z_scores_nn['cug'] > 0)]
z_scores_nn_ncug = z_scores_nn[(z_scores_nn['cuu'] == 0) & (z_scores_nn['cug'] < 0)]
z_scores_nn_pdiag = z_scores_nn[(z_scores_nn['cuu'] > 0) & (z_scores_nn['cug'] > 0)]
z_scores_nn_ndiag = z_scores_nn[(z_scores_nn['cuu'] < 0) & (z_scores_nn['cug'] < 0)]

z_scores_truth_pcuu = z_scores_truth[(z_scores_truth['cug'] == 0) & (z_scores_truth['cuu'] > 0)]
z_scores_truth_ncuu = z_scores_truth[(z_scores_truth['cug'] == 0) & (z_scores_truth['cuu'] < 0)]
z_scores_truth_pcug = z_scores_truth[(z_scores_truth['cuu'] == 0) & (z_scores_truth['cug'] > 0)]
z_scores_truth_ncug = z_scores_truth[(z_scores_truth['cuu'] == 0) & (z_scores_truth['cug'] < 0)]
z_scores_truth_pdiag = z_scores_truth[(z_scores_truth['cuu'] > 0) & (z_scores_truth['cug'] > 0)]
z_scores_truth_ndiag = z_scores_truth[(z_scores_truth['cuu'] < 0) & (z_scores_truth['cug'] < 0)]

# fit a quadratic polynomial
def quad_pol(x, a, b, c):
    return a * x ** 2 + b * x + c

def interpolation(z_scores_truth, z_scores_nn):
    plt.figure(figsize=(10, 6))
    ax = plt.subplot(111)
    z_scores_nn = z_scores_nn.reset_index(drop=True)
    z_scores_truth = z_scores_truth.reset_index(drop=True)
    c = z_scores_nn.cuu.values if z_scores_nn.cuu.values[0] != 0 else z_scores_nn.cug.values

    z_score_nn = z_scores_nn['z-score'].values
    z_score_nn_unc = z_scores_nn['uncertainty'].values

    z_score_truth = z_scores_truth['z-score'].values
    z_score_truth_unc = z_scores_truth['uncertainty'].values

    ax.errorbar(c, z_score_nn, yerr=z_score_nn_unc, fmt='.', capsize=3,
                color='C0', label=r'$\rm{z-score\;(NN)}$')

    ax.errorbar(c, z_score_truth, yerr=z_score_truth_unc, fmt='.', capsize=3,
                color='C1', label=r'$\rm{z-score\;(truth)}$')

    popt_nn, _ = curve_fit(quad_pol, c, z_score_nn, sigma=z_score_nn_unc)
    popt_truth, _ = curve_fit(quad_pol, c, z_score_truth, sigma=z_score_truth_unc)

    epsilon = 0.1 * (np.max(c) - np.min(c))
    xmin = np.min(c) - epsilon
    xmax = np.max(c) + epsilon
    x = np.linspace(xmin, xmax, 400)

    plt.hlines(1.64, xmin, xmax, color='black', linestyle='dashed')
    # ax.plot(x, quad_pol(x, *popt_truth), color='C0', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(true)}$')
    ax.plot(x, quad_pol(x, *popt_truth), color='C1', linestyle='dotted')  # , label=r'$\rm{Exp\;fit\;(NN)}$')
    ax.plot(x, quad_pol(x, *popt_nn), color='C0', linestyle='dotted')  # , label=r'$\rm{Exp\;fit\;(NN)}$')

    idx_truth = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_truth) - 1.64))).flatten()
    idx_nn = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_nn) - 1.64))).flatten()

    plt.plot(x[idx_truth], quad_pol(x[idx_truth], *popt_truth), 'kx')
    plt.plot(x[idx_nn], quad_pol(x[idx_nn], *popt_nn), 'kx')

    # Plot settings
    ax.set_ylabel(r'$\rm{z-score}$', fontsize=20)
    ax.set_xlabel(r'$\rm{c}$', fontsize=20)
    ax.set_xlim((xmin, xmax))

    epsilon = 0.1 * (np.max(z_score_truth) - np.min(z_score_truth))
    ymin = 0#np.min([z_score_truth.min() - epsilon, z_score_truth.min() - epsilon])
    ymax = 2#np.max([z_score_truth.max() + epsilon, z_score_truth.max() + epsilon])

    ax.set_ylim((ymin, ymax))
    ax.legend(loc='best', fontsize=15, frameon=False)
    ax.tick_params(which='both', direction='in', labelsize=20)
    ax.tick_params(which='major', length=10)
    ax.tick_params(which='minor', length=5)
    ax.set_title(r'$\rm{Interpolation\;of\;z-score}$', fontsize=20)
    plt.tight_layout()
    plt.show()

#interpolation(z_scores_truth_ncug, z_scores_nn_ncug)
# interpolation(z_scores_nn_pcuu)
# interpolation(z_scores_nn_ncug)
# interpolation(z_scores_nn_pcug)
#sys.exit()


# plt.figure(figsize=(10, 6))
# ax = plt.subplot(111)
#
# # ax.errorbar(cug, z_score_truth, yerr=z_score_unc_truth, fmt='.', capsize=3,
# #              color='C0', label=r'$\rm{z-score\;(truth)}$')
#
# cuu = z_scores_nn_pcuu['cuu']
# z_score_nn = z_scores_nn_pcuu['z-score'].values
# z_score_unc_nn = z_scores_nn_pcuu['uncertainty'].values
#
# ax.errorbar(cuu, z_score_nn, yerr=z_score_unc_nn, fmt='.', capsize=3,
#             color='C1', label=r'$\rm{z-score\;(NN)}$')
#
#
#
#
#
# #popt_truth, _ = curve_fit(quad_pol, cug, z_score_truth, sigma=z_score_unc_truth)
# popt_nn, _ = curve_fit(quad_pol, cuu, z_score_nn, sigma=z_score_unc_nn)
#
# epsilon = 0.1*(np.max(cuu) - np.min(cuu))
# xmin = np.min(cuu) - epsilon
# xmax = np.max(cuu) + epsilon
# x = np.linspace(xmin, xmax, 400)
#
# plt.hlines(1.64, xmin, xmax, color='black', linestyle='dashed')
# #ax.plot(x, quad_pol(x, *popt_truth), color='C0', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(true)}$')
# ax.plot(x, quad_pol(x, *popt_nn), color='C1', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(NN)}$')
#
# #idx_truth = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_truth) - 1.64))).flatten()
# idx_nn = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_nn) - 1.64))).flatten()
#
# plt.plot(x[idx_nn], quad_pol(x[idx_nn], *popt_nn), 'kx')
# #plt.plot(x[idx_truth], quad_pol(x[idx_truth], *popt_truth), 'kx')
#
# # Plot settings
# ax.set_ylabel(r'$\rm{z-score}$', fontsize=20)
# ax.set_xlabel(r'$\rm{cug}$', fontsize=20)
# ax.set_xlim((xmin, xmax))
#
# epsilon = 0.1*(np.max(z_score_nn) - np.min(z_score_nn))
# ymin = np.min([z_score_nn.min() - epsilon, z_score_nn.min() - epsilon])
# ymax = np.max([z_score_nn.max() + epsilon, z_score_nn.max() + epsilon])
#
# ax.set_ylim((ymin, ymax))
# ax.legend(loc='best', fontsize=15, frameon=False)
# ax.tick_params(which='both', direction='in', labelsize=20)
# ax.tick_params(which='major', length=10)
# ax.tick_params(which='minor', length=5)
# ax.set_title(r'$\rm{Interpolation\;of\;z-score}$', fontsize=20)
# plt.tight_layout()
# plt.show()
#plt.savefig('p_value_int_comp.pdf')



