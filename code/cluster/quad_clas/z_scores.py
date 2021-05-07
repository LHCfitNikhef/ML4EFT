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

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

z_scores_05 = []
z_scores_075 = []
z_scores_087 = []
z_scores_10 = []
cuu = np.array([0.5, 0.75, 0.87, 1.0])

def normal(z):
    return 1/(np.sqrt(2*np.pi))*np.exp(-z**2/2)
#
# with open("z_scores/truth/z_scores_truth.dat", "r") as f:
#     reader = csv.reader(f, delimiter='\t')
#     z_scores = []
#     for line in reader:
#         z_scores.append(float(line[-1]))
#     z_scores = np.array(z_scores)
#     sigma_p = normal(np.median(z_scores)) * np.std(z_scores)
#     #print(np.median(z_scores))
#     print("Truth: ", 1-norm.cdf(np.median(z_scores)), sigma_p)
#     p_value = 1 -norm.cdf(z_scores)
#     mean_p_value = np.mean(p_value)
#     std_p_value = np.std(p_value)
#     #print(mean_p_value, std_p_value)
#     #std_nn_rep = np.array(std_nn_rep)
#     #z_score = np.mean(z_nn_rep)


cuu = [0.5, 0.75, 0.87, 1.0]

######## BINNED ########

with open("z_scores/binned/z_scores_bin_1.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    p_value_binned_1 = []
    p_value_binned_1_unc =[]

    for line in reader:
        z_scores.append([float(line[1]), float(line[0])])
    z_scores = np.array(z_scores)
    #z_scores = z_scores[z_scores[:, 0].argsort()]
    for c in cuu:
        z_scores_c = z_scores[z_scores[:, 0] == c]
        z_med = np.median(z_scores_c)
        z_med_unc = np.std(z_scores_c)/np.sqrt(len(z_scores_c))
        p_value_binned_1.append(1 - norm.cdf(z_med))
        p_value_binned_1_unc.append(normal(z_med)*z_med_unc)

with open("z_scores/binned/z_scores_bin_2.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_scores = []
    p_value_binned_2 = []
    p_value_binned_2_unc =[]

    for line in reader:
        z_scores.append([float(line[1]), float(line[0])])
    z_scores = np.array(z_scores)
    #z_scores = z_scores[z_scores[:, 0].argsort()]
    for c in cuu:
        z_scores_c = z_scores[z_scores[:, 0] == c]
        z_med = np.median(z_scores_c)
        z_med_unc = np.std(z_scores_c)/np.sqrt(len(z_scores_c))
        p_value_binned_2.append(1 - norm.cdf(z_med))
        p_value_binned_2_unc.append(normal(z_med)*z_med_unc)




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

#
#
# ######## NN ###########
#
# p_values_mean_nn = []
# p_values_std_nn = []
#
# with open("z_scores/nn/z_scores_05.dat", "r") as f:
#     reader = csv.reader(f, delimiter='\t')
#     z_nn_rep = []
#     std_nn_rep = []
#     for line in reader:
#         z_nn_rep.append(float(line[0]))
#         std_nn_rep.append(float(line[1]))
#     z_nn_rep = np.array(z_nn_rep)
#     #std_nn_rep = np.array(std_nn_rep)
#     #z_score = np.mean(z_nn_rep)
#     #sigma_z = np.std(z_nn_rep)
#     #sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))
#
#     p_value = 1 - norm.cdf(z_nn_rep)
#     p_value_mean = np.mean(p_value)
#     p_value_sigma = np.std(p_value)
#     #p_value_sigma = normal(z_score)*sigma_z
#     p_values_mean_nn.append(p_value_mean)
#     p_values_std_nn.append(p_value_sigma)
#
# with open("z_scores/nn/z_scores_075.dat", "r") as f:
#     reader = csv.reader(f, delimiter='\t')
#     z_nn_rep = []
#     std_nn_rep = []
#     for line in reader:
#         z_nn_rep.append(float(line[0]))
#         std_nn_rep.append(float(line[1]))
#     z_nn_rep = np.array(z_nn_rep)
#     # std_nn_rep = np.array(std_nn_rep)
#     # z_score = np.mean(z_nn_rep)
#     # sigma_z = np.std(z_nn_rep)
#     # sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))
#
#     p_value = 1 - norm.cdf(z_nn_rep)
#     p_value_mean = np.mean(p_value)
#     p_value_sigma = np.std(p_value)
#     # p_value_sigma = normal(z_score)*sigma_z
#     p_values_mean_nn.append(p_value_mean)
#     p_values_std_nn.append(p_value_sigma)
#
# with open("z_scores/nn/z_scores_087.dat", "r") as f:
#     reader = csv.reader(f, delimiter='\t')
#     z_nn_rep = []
#     std_nn_rep = []
#     for line in reader:
#         z_nn_rep.append(float(line[0]))
#         std_nn_rep.append(float(line[1]))
#     z_nn_rep = np.array(z_nn_rep)
#     # std_nn_rep = np.array(std_nn_rep)
#     # z_score = np.mean(z_nn_rep)
#     # sigma_z = np.std(z_nn_rep)
#     # sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))
#
#     p_value = 1 - norm.cdf(z_nn_rep)
#     p_value_mean = np.mean(p_value)
#     p_value_sigma = np.std(p_value)
#     # p_value_sigma = normal(z_score)*sigma_z
#     p_values_mean_nn.append(p_value_mean)
#     p_values_std_nn.append(p_value_sigma)
#
# with open("z_scores/nn/z_scores_10.dat", "r") as f:
#     reader = csv.reader(f, delimiter='\t')
#     z_nn_rep = []
#     std_nn_rep = []
#     for line in reader:
#         z_nn_rep.append(float(line[0]))
#         std_nn_rep.append(float(line[1]))
#     z_nn_rep = np.array(z_nn_rep)
#     # std_nn_rep = np.array(std_nn_rep)
#     # z_score = np.mean(z_nn_rep)
#     # sigma_z = np.std(z_nn_rep)
#     # sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))
#
#     p_value = 1 - norm.cdf(z_nn_rep)
#     p_value_mean = np.mean(p_value)
#     p_value_sigma = np.std(p_value)
#     # p_value_sigma = normal(z_score)*sigma_z
#     p_values_mean_nn.append(p_value_mean)
#     p_values_std_nn.append(p_value_sigma)
#
# p_values_mean_nn = np.array(p_values_mean_nn)
# p_values_std_nn = np.array(p_values_std_nn)
#
# #### BINNED ####
# with open("z_scores/binned/bin_3/p_value.dat", "r") as f:
#     reader = csv.reader(f, delimiter='\t')
#     p_value_binned = []
#     for line in reader:
#         p_value_binned.append(float(line[0]))
#     p_value_binned = np.array(p_value_binned)
#
#
#
plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
# ax.plot(cuu,z_scores_mean,color='darkblue',label='$t_{g}^{train}$', lw=3)


ax.errorbar(cuu, p_value_binned_1, yerr=p_value_binned_1_unc, fmt='.', capsize=3,
            color='C0', label=r'$\rm{p-value\;(bin\;1)}$')

ax.errorbar(cuu, p_value_binned_2, yerr=p_value_binned_2_unc, fmt='.', capsize=3,
            color='C1', label=r'$\rm{p-value\;(bin\;2)}$')

# ax.errorbar(cuu, p_values_mean_nn, yerr=p_values_std_nn, fmt='.', capsize=3,
#             color='C1', label=r'$\rm{p-value}\;(NN\;recon)$')
#
# ax.scatter(cuu, p_value_binned, c='C2', label=r'$\rm{p-value\;(binned)}$')


# fit a quadratic polynomial
def quad_pol(x, a, b, c):
    return a * x ** 2 + b * x + c

def decay_exp(x, a, b, c):
    return a * np.exp(-b * x) + c


popt_bin_1, _ = curve_fit(quad_pol, cuu, p_value_binned_1, sigma=p_value_binned_1_unc)
popt_bin_2, _ = curve_fit(quad_pol, cuu, p_value_binned_2, sigma=p_value_binned_2_unc)
# popt_nn, _ = curve_fit(quad_pol, cuu, p_values_mean_nn, sigma=p_values_std_nn)
# popt_binned, _ = curve_fit(decay_exp, cuu, p_value_binned, maxfev=5000)

x = np.linspace(np.min(cuu), np.max(cuu), 400)
plt.hlines(0.05, np.min(cuu), np.max(cuu), color='black', linestyle='dashed')
ax.plot(x, quad_pol(x, *popt_bin_1), color='C0', linestyle='dotted', label=r'$\rm{Poly\;2\;fit\;(bin\;1)}$')
ax.plot(x, quad_pol(x, *popt_bin_2), color='C1', linestyle='dotted', label=r'$\rm{Poly\;2\;fit\;(bin\;2)}$')
# ax.plot(x, quad_pol(x, *popt_nn), color='C1', linestyle='dotted', label=r'$\rm{Poly\;2\;fit\;(NN\;recon)}$')
# ax.plot(x, decay_exp(x, *popt_binned), color='C2', linestyle='dotted', label=r'$\rm{exp\;fit\;(binned)}$')



#'fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt)



idx_bin_1 = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_bin_1) - 0.05))).flatten()


idx_bin_2 = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_bin_2) - 0.05))).flatten()
print(idx_bin_2)
# idx_nn = np.argwhere(np.diff(np.sign(quad_pol(x, *popt_nn) - 0.05))).flatten()
# idx_binned = np.argwhere(np.diff(np.sign(decay_exp(x, *popt_binned) - 0.05))).flatten()
plt.plot(x[idx_bin_1], quad_pol(x[idx_bin_1], *popt_bin_1), 'kx')
plt.plot(x[idx_bin_2], quad_pol(x[idx_bin_2], *popt_bin_2), 'kx')
# plt.plot(x[idx_nn], quad_pol(x[idx_nn], *popt_nn), 'kx')
# plt.plot(x[idx_binned], decay_exp(x[idx_binned], *popt_binned), 'kx')

ax.axvline(x[idx_bin_1], 0, 0.3, color='black', linestyle='dashed')
ax.axvline(x[idx_bin_1], 0, 0.3, color='black', linestyle='dashed')
#ax.axvline(x[idx_nn], 0, 0.3, color='black', linestyle='dashed')
#ax.axvline(x[idx_binned], 0, 0.3, color='black', linestyle='dashed')
#ax.text(0.1,0.9,r'$c_{2\sigma,\;\rm{bin\;1}} = %.3f$'%x[idx_bin_1],fontsize=20,transform=ax.transAxes)
#ax.text(0.1,0.82,r'$c_{2\sigma,\;\rm{bin\;2}} = %.3f$'%x[idx_bin_2],fontsize=20,transform=ax.transAxes)
#ax.text(0.2,0.74,r'$c_{2\sigma,\;\rm{binned}} = %.3f$'%x[idx_binned],fontsize=20,transform=ax.transAxes)

# Plot settings
ax.set_ylabel(r'$\rm{p-value}$', fontsize=20)
ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
ax.set_xlim((0.48, 1.02))
ax.legend(loc='best', fontsize=15, frameon=False)
ax.tick_params(which='both', direction='in', labelsize=20)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', length=5)
ax.set_title(r'$\rm{Interpolation\;of\;p-value}$', fontsize=20)
plt.tight_layout()
#plt.show()
plt.savefig('p_value_int_bin_fix.pdf')



