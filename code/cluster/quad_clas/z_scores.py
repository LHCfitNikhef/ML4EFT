import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from matplotlib import rc
from scipy.stats import norm
import csv
#
# rc('font', **{'family': 'serif', 'serif': ['Times']})
# rc('text', usetex=True)

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)
#
# z_scores_05 = []
# z_scores_075 = []
# z_scores_087 = []
# z_scores_10 = []
# cuu = np.array([0.5, 0.75, 0.87, 1.0])
#
# with open("z_scores.dat", "r") as f:
#     for line in f:
#         z_score = float(line.strip())
#         z_scores_05.append(z_score)
#     z_scores_05 = np.array(z_scores_05)
#
# with open("z_scores_075.dat", "r") as f:
#     for line in f:
#         z_score = float(line.strip())
#         z_scores_075.append(z_score)
#     z_scores_075 = np.array(z_scores_075)
#
#
# with open("z_scores_1.dat", "r") as f:
#     for line in f:
#         z_score = float(line.strip())
#         z_scores_10.append(z_score)
#     z_scores_10 = np.array(z_scores_10)
#
# p_value_05 = 1 - norm.cdf(z_scores_05)
# p_value_075 = 1 - norm.cdf(z_scores_075)
# p_value_087 = 1 - norm.cdf(z_scores_087)
# p_value_10 = 1 - norm.cdf(z_scores_10)
#
# p_values_mean = np.array([np.mean(p_value_05), np.mean(p_value_075), np.mean(p_value_087), np.mean(p_value_10)])
# p_values_std = np.array([np.std(p_value_05), np.std(p_value_075), np.std(p_value_087), np.std(p_value_10)])
#
# plt.figure(figsize=(10, 6))
# ax = plt.subplot(111)
# # ax.plot(cuu,z_scores_mean,color='darkblue',label='$t_{g}^{train}$', lw=3)
#
#
# ax.errorbar(cuu, p_values_mean, yerr=p_values_std, fmt='.',
#             color='darkblue', label=r'$\rm{p-value}$')
#
#
# # fit a quadratic polynomial
# def quad_pol(x, a, b, c):
#     return a * x ** 2 + b * x + c
#
#
# popt, _ = curve_fit(quad_pol, cuu, p_values_mean, sigma=p_values_std)
# x = np.linspace(np.min(cuu), np.max(cuu), 400)
# plt.hlines(0.05, np.min(cuu), np.max(cuu), color='red', linestyle='dashed')
# ax.plot(x, quad_pol(x, *popt), 'g--', label=r'$\rm{Poly\;2\;fit}$')
#
# #'fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt)
#
#
#
# idx = np.argwhere(np.diff(np.sign(quad_pol(x, *popt) - 0.05))).flatten()
# plt.plot(x[idx], quad_pol(x[idx], *popt), 'ro')
# ax.axvline(x[idx], 0, 0.3, color='black', linestyle='dotted')
# ax.text(0.1,0.9,r'$c_{2\sigma} = %.2f$'%x[idx],fontsize=20,transform=ax.transAxes)
#
# # Plot settings
# ax.set_ylabel(r'$\rm{p-value}$', fontsize=20)
# ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
# ax.legend(loc='best', fontsize=20, frameon=False)
# ax.tick_params(which='both', direction='in', labelsize=20)
# ax.tick_params(which='major', length=10)
# ax.tick_params(which='minor', length=5)
# ax.set_title(r'$\rm{Interpolation\;of\;p-value}$', fontsize=20)
# plt.tight_layout()
# plt.savefig('p_value_int.pdf')


with open("z_scores/nn/z_scores_087.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    mean = []
    std = []
    for line in reader:
        mean.append(float(line[0]))
        std.append(float(line[1]))
    mean = np.array(mean)
    std = np.array(std)
    z_score = np.mean(mean)
    sigma_z = 1/len(mean)*np.sqrt(np.sum(std**2))
    print(1 - norm.cdf(z_score))
