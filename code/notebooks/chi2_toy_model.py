import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon

exp_rv = expon()
norm_rv = norm(loc=3, scale=0.1)


def pdf(x, mass):
    norm_rv = norm(loc=mass, scale=0.1)
    prob = (exp_rv.pdf(x) + 0.1 * norm_rv.pdf(x)) / 1.1
    return prob


def pdf_binned(bins, mass):
    cdf_exp = exp_rv.cdf(bins)
    weights_exp = cdf_exp[1:] - cdf_exp[:-1]

    norm_rv = norm(loc=mass, scale=0.1)
    cdf_norm = norm_rv.cdf(bins)
    weights_norm = cdf_norm[1:] - cdf_norm[:-1]
    weights_total = (weights_exp + 0.1 * weights_norm) / 1.1
    return weights_total


def chi2_function(data, theory):
    return np.sum((data-theory) ** 2 / data)



mass_truth = 3
mass_range = np.arange(mass_truth-1, mass_truth+3, 0.001)
fig, ax = plt.subplots()
x = np.linspace(expon.ppf(0.01), expon.ppf(0.99), 100)
y = pdf(x, mass_truth)
ax.plot(x, y, 'k-', lw=1)
plt.xlabel('$\sqrt{s}$')
plt.ylabel('Cross section [a.u.]')


plt.show()

# rejections sampling
pseudo_data_cont = []
for i in range (10000):
    delta_x = np.max(x) - np.min(x)
    delta_y = np.max(y) - np.min(y)
    u1 = delta_x * np.random.random()
    u2 = delta_y * np.random.random()
    if u2 < pdf(u1, mass_truth):
        pseudo_data_cont.append(u1)
pseudo_data_cont = np.array(pseudo_data_cont)

# binned chi2 analysis
nrows = 3
ncols = 2
fig = plt.figure(figsize=(ncols * 8, nrows * 6))
for i, n_bins in enumerate([2, 5, 10, 20, 30]):
    #n_bins = 10
    ax = plt.subplot(3, 2, i + 1)
    bins = np.linspace(np.min(x), np.max(x), n_bins + 1)
    #bins = np.array([0.1, 0.5, 3.5, 4.0])

    nu_tot = len(pseudo_data_cont)

    #weights = pdf_binned(bins, 1, b_truth)
    #nu_i = nu_tot * weights
    pseudo_data, _ = np.histogram(pseudo_data_cont, bins=bins)#np.random.poisson(nu_i, len(nu_i))

    chi2_array = []

    for m in mass_range:
        weights = pdf_binned(bins, m)
        nu_i = nu_tot * weights
        chi2_array.append(chi2_function(pseudo_data, nu_i))
    chi2_array = np.array(chi2_array)

    b_min_idx = np.argmin(chi2_array)
    b_min = mass_range[b_min_idx]

    chi2_min = np.min(chi2_array)
    chi2_low_up_idx = np.argwhere(chi2_array < chi2_min + 4)
    b_low = mass_range[chi2_low_up_idx[0]]
    b_up = mass_range[chi2_low_up_idx[-1]]

    #fig, ax = plt.subplots()
    plt.plot(mass_range, chi2_array, color='C0')
    ax.axhline(chi2_min + 4, linestyle='dashed', color='C1')
    ax.axvline(mass_truth, 0, 1, linestyle='dashed', color='k')
    ax.text(0.9, 0.9,r'$c\;=\;%.2f ^{+%.2f}_{-%.2f}$'%(b_min, b_up-b_min, b_min-b_low),
            transform=ax.transAxes,
            horizontalalignment='right',
            verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))
    plt.ylabel(r'$\chi^2 \times n_{dat}$')
    plt.xlabel('$m_X$')
    plt.xlim(mass_range[chi2_low_up_idx[0]]-0.2, mass_range[chi2_low_up_idx[-1]]+0.2)
    plt.ylim(chi2_min-1, chi2_min + 10)
    plt.title(r'$\chi^2_{\rm{binned}}\;(%d\;\rm{bins})$'%n_bins)
    plt.grid()
    # ax.step(bins[:-1], pseudo_data, where='post')

ax = plt.subplot(3, 2, 6)
# plr analysis
likelihood_scan = np.array([np.sum(np.log(pdf(pseudo_data_cont, mass))) for mass in mass_range])
mass_hat = mass_range[np.argmax(likelihood_scan)]

def q(x, mass, mass_hat):
    q_b = -2 * np.sum(np.log(pdf(x, mass))) + 2 * np.sum(np.log(pdf(x, mass_hat)))
    return q_b

q_c_list = np.array([q(pseudo_data_cont, mass, mass_hat) for mass in mass_range])
#fig, ax = plt.subplots()
plt.plot(mass_range, q_c_list)
q_min = np.min(q_c_list)
c_min_idx = np.argmin(q_c_list)
c_min = mass_range[c_min_idx]

q_low_up_idx = np.argwhere(q_c_list < q_min + 4)
c_low = mass_range[q_low_up_idx[0]]
c_up = mass_range[q_low_up_idx[-1]]
ax.axhline(q_min + 4, linestyle='dashed', color='C1')
ax.axvline(mass_truth, 0, 1, linestyle='dashed', color='k')
ax.text(0.9, 0.9,r'$c\;=\;%.2f ^{+%.2f}_{-%.2f}$'%(c_min, c_up-c_min, c_min-c_low),
        transform=ax.transAxes,
        horizontalalignment='right',
        verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))
#ax.axvline(b_hat, 0, 1, linestyle='dashed', color='k')
plt.ylabel('$q_m$')
plt.xlabel('$m_X$')
plt.title('Unbinned analysis')
plt.grid()

plt.xlim(mass_range[q_low_up_idx[0]]-0.2, mass_range[q_low_up_idx[-1]]+0.2)
plt.ylim(q_min-1, q_min + 10)
plt.show()
fig.savefig('/Users/jaco/Documents/ML4EFT/code/notebooks/chi_toy_model_plots/chi2_binned_unbinned.pdf')

