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

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

# cuu = [0.25, 0.5, 0.75, 0.87, 1.0, 1.2, 1.4, 1.6, 2.0]
cuu = [0.40, 0.45, 0.50, 0.55, 0.75, 0.87, 1.0, 1.2]
#cuu = [-0.40, -0.45, -0.50, -0.55, -0.60, -0.65, -0.70, -0.75, -0.80, -0.85, -0.90, -0.95, -1.00, -1.05, -1.10, -1.10, -1.15, -1.20, -1.25, -1.30, -1.35, -1.40]

#cuu = [0.6]

def normal(z):
    return 1/(np.sqrt(2*np.pi))*np.exp(-z**2/2)

##### TRUTH ########
with open("z_scores/truth/z_scores_final.dat", "r") as f:

    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    p_value_truth = []
    p_value_truth_unc = []

    for line in reader:
        z_scores.append([float(line[1]), float(line[2])])
    z_scores = np.array(z_scores)

    for c in cuu:
        z_scores_c = z_scores[z_scores[:, 0] == c][:, 1]
        p_values_c = 1 - norm.cdf(z_scores_c)
        p_value_c = np.mean(p_values_c)
        p_value_c_unc = np.std(p_values_c)/np.sqrt(len(p_values_c))
        p_value_truth.append(p_value_c)
        p_value_truth_unc.append(p_value_c_unc)
        # z_mean = np.mean(z_scores_c)
        # z_unc = np.std(z_scores_c)
        # p_value_truth.append(1 - norm.cdf(z_mean))
        # p_value_truth_unc.append(normal(z_mean)*z_unc)

# print("p-values truth: ", p_value_truth)
# print("p-values unc truth: ", p_value_truth_unc)
# sys.exit()

##### NN ########
with open("z_scores/nn/z_scores_final.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    p_value_nn = []
    p_value_nn_unc = []

    for line in reader:
        z_scores.append([float(line[1]), float(line[2])])
    z_scores = np.array(z_scores)

    for c in cuu:
        z_scores_c = z_scores[z_scores[:, 0] == c][:, 1]
        p_values_c = 1 - norm.cdf(z_scores_c)
        p_value_c = np.mean(p_values_c)
        p_value_c_unc = np.std(p_values_c) / np.sqrt(len(p_values_c))
        p_value_nn.append(p_value_c)
        p_value_nn_unc.append(p_value_c_unc)

# print("p-values nn: ", p_value_nn)
# print("p-values unc nn: ", p_value_nn_unc)
# sys.exit()


######## BINNED ########
with open("z_scores/binned/bin_1/z_scores_final.dat", "r") as f:

    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    p_value_bin_1 = []
    p_value_bin_1_unc = []

    for line in reader:
        z_scores.append([float(line[1]), float(line[2])])
    z_scores = np.array(z_scores)

    for c in cuu:
        z_scores_c = z_scores[z_scores[:, 0] == c][:, 1]


        p_values_c = 1 - norm.cdf(z_scores_c)
        p_value_c = np.mean(p_values_c)
        p_value_c_unc = np.std(p_values_c) / np.sqrt(len(p_values_c))
        p_value_bin_1.append(p_value_c)
        p_value_bin_1_unc.append(p_value_c_unc)

        # z_mean = np.mean(z_scores_c)
        # z_unc = np.std(z_scores_c)/np.sqrt(len(z_scores_c))
        # p_value_bin_1.append(1 - norm.cdf(z_mean))
        # p_value_bin_1_unc.append(normal(z_mean)*z_unc)



with open("z_scores/binned/bin_2/z_scores_final.dat", "r") as f:

    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    p_value_bin_2 = []
    p_value_bin_2_unc = []

    for line in reader:
        z_scores.append([float(line[1]), float(line[2])])
    z_scores = np.array(z_scores)


    for c in cuu:
        z_scores_c = z_scores[z_scores[:, 0] == c][:, 1]
        p_values_c = 1 - norm.cdf(z_scores_c)
        p_value_c = np.mean(p_values_c)
        p_value_c_unc = np.std(p_values_c) / np.sqrt(len(p_values_c))
        p_value_bin_2.append(p_value_c)
        p_value_bin_2_unc.append(p_value_c_unc)

# print(p_value_bin_2, p_value_bin_2_unc)
# sys.exit()

with open("z_scores/binned/bin_3/z_scores_final.dat", "r") as f:

    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    p_value_bin_3 = []
    p_value_bin_3_unc = []

    for line in reader:
        z_scores.append([float(line[1]), float(line[2])])
    z_scores = np.array(z_scores)

    for c in cuu:
        z_scores_c = z_scores[z_scores[:, 0] == c][:, 1]

        p_values_c = 1 - norm.cdf(z_scores_c)
        p_value_c = np.mean(p_values_c)
        p_value_c_unc = np.std(p_values_c) / np.sqrt(len(p_values_c))
        p_value_bin_3.append(p_value_c)
        p_value_bin_3_unc.append(p_value_c_unc)

    # sigma_p = normal(np.median(z_scores))*np.std(z_scores)
    # print("Binned: ", 1-norm.cdf(np.median(z_scores)), sigma_p)
    #print(1 - norm.cdf(np.median(z_scores)))
    # p_value = 1 - norm.cdf(z_scores)
    # mean_p_value = np.mean(p_value)
    # std_p_value = np.std(p_value)
    # print(mean_p_value, std_p_value)
#
# with open("z_scores_075.dat", "r") as f:
#     for line in f:
#         z_score = float(line.strip())
#         z_scores_075.append(z_score)
#     z_scores_075 = np.array(z_scores_075)
#
# with open("z_scores_087.dat", "r") as f:
#     for line in f:
#         z_score = float(line.strip())
#         z_scores_087.append(z_score)
#     z_scores_087 = np.array(z_scores_087)
#
#
# with open("z_scores_1.dat", "r") as f:
#     for line in f:
#         z_score = float(line.strip())
#         z_scores_10.append(z_score)
#     z_scores_10 = np.array(z_scores_10)
#
#
# p_value_05 = 1 - norm.cdf(z_scores_05)
# p_value_075 = 1 - norm.cdf(z_scores_075)
# p_value_087 = 1 - norm.cdf(z_scores_087)
# p_value_10 = 1 - norm.cdf(z_scores_10)
#
# p_values_mean = np.array([np.mean(p_value_05), np.mean(p_value_075), np.mean(p_value_087), np.mean(p_value_10)])
# p_values_std = np.array([np.std(p_value_05), np.std(p_value_075), np.std(p_value_087), np.std(p_value_10)])
#


plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
#ax.plot(cuu,z_scores_mean,color='darkblue',label='$t_{g}^{train}$', lw=3)

ax.errorbar(cuu, p_value_truth, yerr=p_value_truth_unc, fmt='.', capsize=3,
            color='C0', label=r'$\rm{p-value\;(true)}$')

ax.errorbar(cuu, p_value_nn, yerr=p_value_nn_unc, fmt='.', capsize=3,
            color='C1', label=r'$\rm{p-value\;(NN)}$')

# ax.errorbar(cuu, p_value_bin_1, yerr=p_value_bin_1_unc, fmt='.', capsize=3,
#              color='C2', label=r'$\rm{p-value\;(bin\;1)}$')
#
# ax.errorbar(cuu, p_value_bin_2, yerr=p_value_bin_2_unc, fmt='.', capsize=3,
#             color='C3', label=r'$\rm{p-value\;(bin\;2)}$')
#
# ax.errorbar(cuu, p_value_bin_3, yerr=p_value_bin_3_unc, fmt='.', capsize=3,
#             color='C4', label=r'$\rm{p-value\;(bin\;3)}$')


# fit a quadratic polynomial
def quad_pol(x, a, b, c):
    return a * x ** 2 + b * x + c

def decay_exp(x, a, b, c):
    return a * np.exp(-b * x)

popt_truth, _ = curve_fit(decay_exp, cuu[:6], p_value_truth[:6], sigma=p_value_truth_unc[:6])
popt_nn, _ = curve_fit(decay_exp, cuu[:6], p_value_nn[:6], sigma=p_value_nn_unc[:6])
popt_bin_1, _ = curve_fit(quad_pol, cuu, p_value_bin_1, sigma=p_value_bin_1_unc)
popt_bin_2, _ = curve_fit(quad_pol, cuu, p_value_bin_2, sigma=p_value_bin_2_unc)
popt_bin_3, _ = curve_fit(quad_pol, cuu, p_value_bin_3, sigma=p_value_bin_3_unc)


x = np.linspace(0.38, np.max(cuu), 400)
plt.hlines(0.05, 0.38, 0.60, color='black', linestyle='dashed')

ax.plot(x, decay_exp(x, *popt_truth), color='C0', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(true)}$')
ax.plot(x, decay_exp(x, *popt_nn), color='C1', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(NN)}$')
# ax.plot(x, quad_pol(x, *popt_bin_1), color='C2', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(bin\;1)}$')
# ax.plot(x, quad_pol(x, *popt_bin_2), color='C3', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(bin\;2)}$')
# ax.plot(x, quad_pol(x, *popt_bin_3), color='C4', linestyle='dotted')#, label=r'$\rm{Exp\;fit\;(bin\;3)}$')


idx_truth = np.argwhere(np.diff(np.sign(decay_exp(x, *popt_truth) - 0.05))).flatten()
idx_nn = np.argwhere(np.diff(np.sign(decay_exp(x, *popt_nn) - 0.05))).flatten()
#
# idx_bin_1 = np.argwhere(np.diff(np.sign(decay_exp(x, *popt_bin_1) - 0.05))).flatten()
# idx_bin_2 = np.argwhere(np.diff(np.sign(decay_exp(x, *popt_bin_2) - 0.05))).flatten()
# idx_bin_3 = np.argwhere(np.diff(np.sign(decay_exp(x, *popt_bin_3) - 0.05))).flatten()
#
# plt.plot(x[idx_bin_1], decay_exp(x[idx_bin_1], *popt_bin_1), 'kx')
# plt.plot(x[idx_bin_2], decay_exp(x[idx_bin_2], *popt_bin_2), 'kx')
# plt.plot(x[idx_bin_3], decay_exp(x[idx_bin_3], *popt_bin_3), 'kx')
plt.plot(x[idx_nn], decay_exp(x[idx_nn], *popt_nn), 'kx')
plt.plot(x[idx_truth], decay_exp(x[idx_truth], *popt_truth), 'kx')

# ax.axvline(x[idx_bin_1], 0, 0.3, color='black', linestyle='dashed')
# ax.axvline(x[idx_bin_1], 0, 0.3, color='black', linestyle='dashed')
#ax.axvline(x[idx_nn], 0, 0.3, color='black', linestyle='dashed')
#ax.axvline(x[idx_binned], 0, 0.3, color='black', linestyle='dashed')
# ax.text(0.15,0.9,r'$c_{2\sigma,\;\rm{bin\;1}} = %.3f$'%x[idx_bin_1],fontsize=20,transform=ax.transAxes)
# ax.text(0.15,0.82,r'$c_{2\sigma,\;\rm{bin\;2}} = %.3f$'%x[idx_bin_2],fontsize=20,transform=ax.transAxes)
# ax.text(0.15,0.74,r'$c_{2\sigma,\;\rm{bin\;3}} = %.3f$'%x[idx_bin_3],fontsize=20,transform=ax.transAxes)
ax.text(0.40,0.9,r'$c_{2\sigma,\;\rm{true}} = %.3f$'%x[idx_truth],fontsize=20,transform=ax.transAxes)
ax.text(0.40,0.82,r'$c_{2\sigma,\;\rm{NN}} = %.3f$'%x[idx_nn],fontsize=20,transform=ax.transAxes)

# Plot settings
ax.set_ylabel(r'$\rm{p-value}$', fontsize=20)
ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
#ax.set_xlim((0.38, 1.42))
ax.set_xlim((0.38, 0.60))
ax.set_ylim((0, 0.15))
ax.legend(loc='best', fontsize=15, frameon=False)
ax.tick_params(which='both', direction='in', labelsize=20)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', length=5)
ax.set_title(r'$\rm{Interpolation\;of\;p-value}$', fontsize=20)
plt.tight_layout()
plt.show()
#plt.savefig('p_value_scan_pcuu_nn_truth.pdf')



