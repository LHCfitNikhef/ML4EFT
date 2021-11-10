import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.pyplot import cm

fig, ax = plt.subplots(figsize=(10,6))

cHq3_values = np.array([0.08, 0.06, 0.05, 0.04, 0.02, -0.04, -0.05, -0.06])
#cHW_values = [0.03, 0.02, 0.01, 0.005, -0.005, -0.01, -0.02, -0.03]

# diagonal
# cHq3_values = np.array([0.2, 0.27752, 0.3])
# cHW_values = np.array([-0.21*cHq3 for cHq3 in cHq3_values])
#cHq3_values = np.array([0.02, 0.03, 0.04, 0.05, 0.06])
#cHW_values = 0.2 * cHq3_values

colors = iter(cm.rainbow(np.linspace(0, 1, 7)))

def f(x, a, b):
    return a * x + b

def interpolate(path, color):
    z_scores = np.load(path)
    print(path)
    z_scores_mean = np.mean(z_scores, axis=1)
    z_scores_unc = np.std(z_scores, axis=1)

    ax.errorbar(cHq3_values[5:], z_scores_mean[5:], yerr=z_scores_unc[5:], fmt='.', capsize=3, color=color)
    popt, _ = curve_fit(f, cHq3_values[5:], z_scores_mean[5:], sigma=z_scores_unc[5:])
    x = np.linspace(0, 0.1, 100)
    ax.plot(x, f(x, *popt), linestyle='dotted', color=color)
    return ax

for mc_run in [4]:
    path = '/Users/jaco/Documents/ML4EFT/code/output/limits/cHq3/nn/z_scores_{}.npy'
    color = next(colors)
    interpolate(path.format(mc_run), color)



#z_scores_nn = np.load('/Users/jaco/Documents/ML4EFT/code/output/limits/z_scores_nn_cHq3.npy')

#z_scores_mean_nn = np.mean(z_scores_nn, axis=1)
#z_scores_unc_nn = np.std(z_scores_nn, axis=1)

# z_scores_truth = np.load('/Users/jaco/Documents/ML4EFT/code/output/limits/z_scores_truth_cHW.npy')
# z_scores_mean_truth = np.mean(z_scores_truth, axis=1)
# z_scores_unc_truth = np.std(z_scores_truth, axis=1)

#ax.errorbar(cHq3_values[5:], z_scores_mean_nn[5:], yerr=z_scores_unc_nn[5:], fmt='.', capsize=3,
#                    color='C0', label=r'$\rm{z-score\;(NN)}$')
# ax.errorbar(cHW_values ** 2 + cHq3_values ** 2, z_scores_mean_truth, yerr=z_scores_unc_truth, fmt='.', capsize=3,
#                     color='C1', label=r'$\rm{z-score\;(Truth)}$')



#popt_nn, _ = curve_fit(f, cHq3_values[5:], z_scores_mean_nn[5:],sigma=z_scores_unc_nn[5:])
#popt_truth, _ = curve_fit(f, cHW_values[4:], z_scores_mean_truth[4:],sigma=z_scores_unc_truth[4:])

# compute critical value of c
#c_crit_nn = (1.64 - popt_nn[1])/popt_nn[0]
#c_crit_truth = (1.64 - popt_truth[1])/popt_truth[0]
x = np.linspace(-0.07, 0, 100)
#ax.plot(x, f(x, *popt_nn), linestyle='dotted', color='C0')
#ax.plot(x, f(x, *popt_truth), linestyle='dotted', color='C1')
ax.axhline(1.64, 0, 1, linestyle='dashed', color='k')
#ax.scatter(c_crit_truth, 1.64, marker='x', color='k')
#ax.scatter(c_crit_nn, 1.64, marker='x', color='k')
#ax.axvline(c_crit_nn, 0, 1, linestyle='dashed', label='nn', color='k')
#ax.axvline(c_crit_truth, 0, 1, linestyle='dashed', label='truth', color='k')
plt.legend()
plt.show()
# ax.errorbar(cHq3_values[3:], z_scores_mean[3:], yerr=z_scores_unc[3:], fmt='.', capsize=3,
#                     color='C1', label=r'$\rm{z-score\;(Truth)}$')
#plt.show()

# popt_truth, _ = curve_fit(self.quad_pol, c, z_score_truth, sigma=z_score_truth_unc)
#
# plt.hlines(1.64, xmin, xmax, color='black', linestyle='dashed')
#         # ax.plot(x, quad_pol(x, *popt_truth), color='C0', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(true)}$')
#         ax.plot(x, self.quad_pol(x, *popt_truth), color='C0', linestyle='dotted')  # , label=r'$\rm{Exp\;fit\;(NN)}$')