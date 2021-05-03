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

z_scores_05 = []
z_scores_075 = []
z_scores_087 = []
z_scores_10 = []
cuu = np.array([0.5, 0.75, 0.87, 1.0])

with open("z_scores.dat", "r") as f:
    for line in f:
        z_score = float(line.strip())
        z_scores_05.append(z_score)
    z_scores_05 = np.array(z_scores_05)

with open("z_scores_075.dat", "r") as f:
    for line in f:
        z_score = float(line.strip())
        z_scores_075.append(z_score)
    z_scores_075 = np.array(z_scores_075)

with open("z_scores_087.dat", "r") as f:
    for line in f:
        z_score = float(line.strip())
        z_scores_087.append(z_score)
    z_scores_087 = np.array(z_scores_087)


with open("z_scores_1.dat", "r") as f:
    for line in f:
        z_score = float(line.strip())
        z_scores_10.append(z_score)
    z_scores_10 = np.array(z_scores_10)


p_value_05 = 1 - norm.cdf(z_scores_05)
p_value_075 = 1 - norm.cdf(z_scores_075)
p_value_087 = 1 - norm.cdf(z_scores_087)
p_value_10 = 1 - norm.cdf(z_scores_10)

p_values_mean = np.array([np.mean(p_value_05), np.mean(p_value_075), np.mean(p_value_087), np.mean(p_value_10)])
p_values_std = np.array([np.std(p_value_05), np.std(p_value_075), np.std(p_value_087), np.std(p_value_10)])

def normal(z):
    return 1/(np.sqrt(2*np.pi))*np.exp(-z**2/2)


######## NN ###########

p_values_mean_nn = []
p_values_std_nn = []

with open("z_scores/nn/z_scores_05.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_nn_rep = []
    std_nn_rep = []
    for line in reader:
        z_nn_rep.append(float(line[0]))
        std_nn_rep.append(float(line[1]))
    z_nn_rep = np.array(z_nn_rep)
    std_nn_rep = np.array(std_nn_rep)
    z_score = np.mean(z_nn_rep)
    sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))

    p_value = 1 - norm.cdf(z_score)
    p_value_sigma = normal(z_score)*sigma_z
    p_values_mean_nn.append(p_value)
    p_values_std_nn.append(p_value_sigma)

with open("z_scores/nn/z_scores_075.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_nn_rep = []
    std_nn_rep = []
    for line in reader:
        z_nn_rep.append(float(line[0]))
        std_nn_rep.append(float(line[1]))
    z_nn_rep = np.array(z_nn_rep)
    std_nn_rep = np.array(std_nn_rep)
    z_score = np.mean(z_nn_rep)
    sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))

    p_value = 1 - norm.cdf(z_score)
    p_value_sigma = normal(z_score)*sigma_z
    p_values_mean_nn.append(p_value)
    p_values_std_nn.append(p_value_sigma)

with open("z_scores/nn/z_scores_087.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_nn_rep = []
    std_nn_rep = []
    for line in reader:
        z_nn_rep.append(float(line[0]))
        std_nn_rep.append(float(line[1]))
    z_nn_rep = np.array(z_nn_rep)
    std_nn_rep = np.array(std_nn_rep)
    z_score = np.mean(z_nn_rep)
    sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))

    p_value = 1 - norm.cdf(z_score)
    p_value_sigma = normal(z_score)*sigma_z
    p_values_mean_nn.append(p_value)
    p_values_std_nn.append(p_value_sigma)

with open("z_scores/nn/z_scores_10.dat", "r") as f:
    reader = csv.reader(f, delimiter='\t')
    z_nn_rep = []
    std_nn_rep = []
    for line in reader:
        z_nn_rep.append(float(line[0]))
        std_nn_rep.append(float(line[1]))
    z_nn_rep = np.array(z_nn_rep)
    std_nn_rep = np.array(std_nn_rep)
    z_score = np.mean(z_nn_rep)
    sigma_z = 1/len(z_nn_rep)*np.sqrt(np.sum(std_nn_rep**2))

    p_value = 1 - norm.cdf(z_score)
    p_value_sigma = normal(z_score)*sigma_z
    p_values_mean_nn.append(p_value)
    p_values_std_nn.append(p_value_sigma)

p_values_mean_nn = np.array(p_values_mean_nn)
p_values_std_nn = np.array(p_values_std_nn)


plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
# ax.plot(cuu,z_scores_mean,color='darkblue',label='$t_{g}^{train}$', lw=3)


ax.errorbar(cuu, p_values_mean, yerr=p_values_std, fmt='.',
            color='C0', label=r'$\rm{p-value\;(truth)}$')

ax.errorbar(cuu, p_values_mean_nn, yerr=p_values_std_nn, fmt='.',
            color='C1', label=r'$\rm{p-value}\;(NN\;recon)$')


# fit a quadratic polynomial
def quad_pol(x, a, b, c):
    return a * x ** 2 + b * x + c


popt, _ = curve_fit(quad_pol, cuu, p_values_mean, sigma=p_values_std)
popt_nn, _ = curve_fit(quad_pol, cuu, p_values_mean_nn, sigma=p_values_std_nn)

x = np.linspace(np.min(cuu), np.max(cuu), 400)
plt.hlines(0.05, np.min(cuu), np.max(cuu), color='green', linestyle='dashed')
ax.plot(x, quad_pol(x, *popt), color='C0', linestyle='dashed', label=r'$\rm{Poly\;2\;fit}$')
ax.plot(x, quad_pol(x, *popt_nn), color='C1', linestyle='dashed', label=r'$\rm{Poly\;2\;fit}$')

#'fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt)



idx = np.argwhere(np.diff(np.sign(quad_pol(x, *popt) - 0.05))).flatten()
plt.plot(x[idx], quad_pol(x[idx], *popt), 'ro')
ax.axvline(x[idx], 0, 0.3, color='black', linestyle='dotted')
ax.text(0.1,0.9,r'$c_{2\sigma} = %.2f$'%x[idx],fontsize=20,transform=ax.transAxes)

# Plot settings
ax.set_ylabel(r'$\rm{p-value}$', fontsize=20)
ax.set_xlabel(r'$\rm{cuu}$', fontsize=20)
ax.legend(loc='best', fontsize=20, frameon=False)
ax.tick_params(which='both', direction='in', labelsize=20)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', length=5)
ax.set_title(r'$\rm{Interpolation\;of\;p-value}$', fontsize=20)
plt.tight_layout()
plt.savefig('p_value_int.pdf')



