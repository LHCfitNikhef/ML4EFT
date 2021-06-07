import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from matplotlib import rc
from scipy.stats import norm
import csv
import sys

#
# rc('font', **{'family': 'serif', 'serif': ['Times']})
# rc('text', usetex=True)

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

z_scores_05 = []
z_scores_075 = []
z_scores_087 = []
z_scores_10 = []
cuu = np.array([0.5, 0.75, 0.87, 1.0])

with open("z_scores/truth/z_scores.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    for line in reader:
        z_scores.append(list(map(float, line)))
    z_scores = np.array(z_scores)

p_value_0_05 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0.5, z_scores[:, 0] == 0)][:, -1])
p_value_0_075 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0.75, z_scores[:, 0] == 0)][:, -1])
p_value_0_087 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0.87, z_scores[:, 0] == 0)][:, -1])
p_value_0_10 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 1.0, z_scores[:, 0] == 0)][:, -1])

p_value_0_m05 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == -0.5, z_scores[:, 0] == 0)][:, -1])
p_value_0_m075 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == -0.75, z_scores[:, 0] == 0)][:, -1])
p_value_0_m10 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == -1.0, z_scores[:, 0] == 0)][:, -1])

p_value_m10_0 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0, z_scores[:, 0] == -1.0)][:, -1])
p_value_10_0 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0, z_scores[:, 0] == 1.0)][:, -1])
p_value_02_0 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0, z_scores[:, 0] == 0.2)][:, -1])
p_value_05_0 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0, z_scores[:, 0] == 0.5)][:, -1])
p_value_m02_0 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0, z_scores[:, 0] == -0.2)][:, -1])
p_value_m04_0 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0, z_scores[:, 0] == -0.4)][:, -1])

p_value_10_05 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0.5, z_scores[:, 0] == 1.0)][:, -1])
p_value_m10_m05 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == -0.5, z_scores[:, 0] == -1.0)][:, -1])
p_value_02_05 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0.5, z_scores[:, 0] == 0.2)][:, -1])
p_value_01_025 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0.25, z_scores[:, 0] == 0.1)][:, -1])
p_value_03_075 = 1 - norm.cdf(z_scores[np.logical_and(z_scores[:, 1] == 0.75, z_scores[:, 0] == 0.3)][:, -1])

p_values_mean_cuu = np.array([np.mean(p_value_0_05), np.mean(p_value_0_075), np.mean(p_value_0_087), np.mean(p_value_0_10)])
p_values_mean_cuu_neg = np.array([np.mean(p_value_0_m05), np.mean(p_value_0_m075), np.mean(p_value_0_m10)])
p_values_mean_cugre_neg = np.array([np.mean(p_value_m10_0), np.mean(p_value_m04_0), np.mean(p_value_m02_0)])
p_values_mean_cugre = np.array([np.mean(p_value_10_0), np.mean(p_value_02_0), np.mean(p_value_05_0)])
p_values_mean_diag = np.array([np.mean(p_value_10_05), np.mean(p_value_02_05), np.mean(p_value_01_025), np.mean(p_value_03_075)])

p_values_std_cuu = np.array([np.std(p_value_0_05), np.std(p_value_0_075), np.std(p_value_0_087), np.std(p_value_0_10)])
p_values_std_cuu_neg = np.array([np.std(p_value_0_m05), np.std(p_value_0_m075), np.std(p_value_0_m10)])
p_values_std_cugre_neg = np.array([np.std(p_value_m10_0), np.std(p_value_m04_0), np.std(p_value_m02_0)])
p_values_std_cugre = np.array([np.std(p_value_10_0), np.std(p_value_02_0), np.std(p_value_05_0)])
p_values_std_diag = np.array([np.std(p_value_10_05), np.std(p_value_02_05), np.std(p_value_01_025), np.std(p_value_03_075)])


cuu = np.array([[0, 0.5], [0, 0.75], [0, 0.87], [0, 1.0]])
cuu_neg = np.array([[0, -0.5], [0, -0.75], [0, -1.0]])
cugre = np.array([[1.0, 0], [0.2, 0], [0.5, 0]])
cugre_neg = np.array([[-1.0, 0], [-0.4, 0], [-0.2, 0]])
c_diag = np.array([[1.0, 0.5], [0.2, 0.5], [0.1, 0.25], [0.3, 0.75]])


plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
# ax.plot(cuu,z_scores_mean,color='darkblue',label='$t_{g}^{train}$', lw=3)


# ax.errorbar(cuu, p_values_mean, yerr=p_values_std, fmt='.', capsize=3,
#             color='C0', label=r'$\rm{p-value\;(truth)}$')
#
# ax.errorbar(cuu, p_values_mean_nn, yerr=p_values_std_nn, fmt='.', capsize=3,
#             color='C1', label=r'$\rm{p-value}\;(NN\;recon)$')
#
# ax.scatter(cuu, p_value_binned, c='C2', label=r'$\rm{p-value\;(binned)}$')


# fit a quadratic polynomial
def quad_pol(x, a, b, c):
    return a * x ** 2 + b * x + c

def decay_exp(x, a, b, c):
    return a * np.exp(-b * x) + c


popt_cuu, _ = curve_fit(quad_pol, cuu[:,0], p_values_mean_cuu, sigma=p_values_std_cuu)
popt_cugre, _ = curve_fit(quad_pol, cugre[:,1], p_values_mean_cugre, sigma=p_values_std_cugre)
popt_cuu_neg, _ = curve_fit(quad_pol, cuu_neg[:,0], p_values_mean_cuu_neg, sigma=p_values_std_cuu_neg)
popt_cugre_neg, _ = curve_fit(quad_pol, cugre_neg[:,1], p_values_mean_cugre_neg, sigma=p_values_std_cugre_neg)
#popt_c_diag, _ = curve_fit(quad_pol, c_diag, p_values_mean_diag, sigma=p_values_std_diag)

x_cuu = np.linspace(np.min(cuu), np.max(cuu), 400)
x_cugre = np.linspace(np.min(cugre), np.max(cugre), 400)
x_cuu_neg = np.linspace(np.min(cuu_neg), np.max(cuu_neg), 400)
x_cugre_neg = np.linspace(np.min(cugre_neg), np.max(cugre_neg), 400)

idx_cuu = np.argwhere(np.diff(np.sign(quad_pol(x_cuu, *popt_cuu) - 0.05))).flatten()
idx_cugre = np.argwhere(np.diff(np.sign(quad_pol(x_cugre, *popt_cugre) - 0.05))).flatten()
idx_cuu_neg = np.argwhere(np.diff(np.sign(quad_pol(x_cuu_neg, *popt_cuu_neg) - 0.05))).flatten()
idx_cugre_neg = np.argwhere(np.diff(np.sign(quad_pol(x_cugre_neg, *popt_cugre_neg) - 0.05))).flatten()

print(idx_cuu_neg, x_cuu_neg[idx_cuu_neg], x_cuu[idx_cuu])


#
# idx_cuu = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_cuu) - 0.05))).flatten()
# idx_nn = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_nn) - 0.05))).flatten()
# idx_binned = np.argwhere(np.diff(np.sign(decay_exp(x, *popt_binned) - 0.05))).flatten()
# plt.plot(x[idx], quad_pol(x[idx], *popt), 'kx')
# plt.plot(x[idx_nn], quad_pol(x[idx_nn], *popt_nn), 'kx')
# plt.plot(x[idx_binned], decay_exp(x[idx_binned], *popt_binned), 'kx')
#
# ax.axvline(x[idx], 0, 0.3, color='black', linestyle='dashed')
# ax.axvline(x[idx_nn], 0, 0.3, color='black', linestyle='dashed')
# #ax.axvline(x[idx_binned], 0, 0.3, color='black', linestyle='dashed')
# ax.text(0.1,0.9,r'$c_{2\sigma,\;\rm{truth}} = %.3f$'%x[idx],fontsize=20,transform=ax.transAxes)
# ax.text(0.1,0.82,r'$c_{2\sigma,\;\rm{NN}} = %.3f$'%x[idx_nn],fontsize=20,transform=ax.transAxes)
# #ax.text(0.2,0.74,r'$c_{2\sigma,\;\rm{binned}} = %.3f$'%x[idx_binned],fontsize=20,transform=ax.transAxes)
#
# # Plot settings
# ax.set_ylabel(r'$\rm{p-value}$', fontsize=20)
# ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
# ax.set_xlim((0.48, 1.02))
# ax.legend(loc='best', fontsize=15, frameon=False)
# ax.tick_params(which='both', direction='in', labelsize=20)
# ax.tick_params(which='major', length=10)
# ax.tick_params(which='minor', length=5)
# ax.set_title(r'$\rm{Interpolation\;of\;p-value}$', fontsize=20)
# plt.tight_layout()
# plt.savefig('p_value_int_bin3.pdf')
#
#
#
