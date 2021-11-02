import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon

exp_rv = expon()
norm_rv = norm(loc=3, scale=1)


def pdf(x, a, b):
    prob = (a * exp_rv.pdf(x) + b * norm_rv.pdf(x)) / (a + b)
    return prob


def pdf_binned(bins, a, b):
    cdf_exp = exp_rv.cdf(bins)
    weights_exp = cdf_exp[1:] - cdf_exp[:-1]
    cdf_norm = norm_rv.cdf(bins)
    weights_norm = cdf_norm[1:] - cdf_norm[:-1]
    weights_total = (a * weights_exp + b * weights_norm) / (a + b)
    return weights_total


def chi2_function(data, theory):
    return np.sum((data-theory) ** 2 / data)



b_truth = 0.5
b_values = np.arange(b_truth-0.4, b_truth+0.4, 0.001)
fig, ax = plt.subplots()
x = np.linspace(expon.ppf(0.01), expon.ppf(0.99), 100)
y = pdf(x, 1, b_truth)
ax.plot(x, y, 'k-', lw=1)


plt.show()

# rejections sampling
pseudo_data_cont = []
for i in range (10000):
    delta_x = np.max(x) - np.min(x)
    delta_y = np.max(y) - np.min(y)
    u1 = delta_x * np.random.random()
    u2 = delta_y * np.random.random()
    if u2 < pdf(u1, 1, b_truth):
        pseudo_data_cont.append(u1)
pseudo_data_cont = np.array(pseudo_data_cont)

# binned chi2 analysis
for n_bins in [1, 5, 10, 20, 50]:
    #n_bins = 10
    bins = np.linspace(np.min(x), np.max(x), n_bins + 1)
    #bins = np.array([0.1, 0.5, 3.5, 4.0])

    nu_tot = len(pseudo_data_cont)

    weights = pdf_binned(bins, 1, b_truth)
    nu_i = nu_tot * weights
    pseudo_data, _ = np.histogram(pseudo_data_cont, bins=bins)#np.random.poisson(nu_i, len(nu_i))

    chi2_array = []

    for b in b_values:
        weights = pdf_binned(bins, a=1, b=b)
        nu_i = nu_tot * weights
        chi2_array.append(chi2_function(pseudo_data, nu_i))
    chi2_array = np.array(chi2_array)

    b_min_idx = np.argmin(chi2_array)
    b_min = b_values[b_min_idx]

    chi2_min = np.min(chi2_array)
    chi2_low_up_idx = np.argwhere(chi2_array < chi2_min + 4)
    b_low = b_values[chi2_low_up_idx[0]]
    b_up = b_values[chi2_low_up_idx[-1]]

    fig, ax = plt.subplots()
    plt.plot(b_values, chi2_array, color='C0')
    ax.axhline(chi2_min + 4, linestyle='dashed', color='C1')
    ax.axvline(b_truth, 0, 1, linestyle='dashed', color='k')
    ax.text(0.9, 0.9,r'$c\;=\;%.2f ^{+%.2f}_{-%.2f}$'%(b_min, b_up-b_min, b_min-b_low),
            transform=ax.transAxes,
            horizontalalignment='right',
            verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))
    plt.ylabel(r'$\chi^2 \times n_{dat}$')
    plt.xlabel('c')
    plt.xlim(b_values[chi2_low_up_idx[0]]-0.2, b_values[chi2_low_up_idx[-1]]+0.2)
    plt.ylim(chi2_min-1, chi2_min + 10)
    plt.title(r'$\chi^2_{\rm{binned}}\;(%d\;\rm{bins})$'%n_bins)
    plt.grid()
    # ax.step(bins[:-1], pseudo_data, where='post')
    plt.show()

# plr analysis
likelihood_scan = np.array([np.sum(np.log(pdf(pseudo_data_cont, 1, b))) for b in b_values])
b_hat = b_values[np.argmax(likelihood_scan)]

def q(x, b, b_hat):
    q_b = -2 * np.sum(np.log(pdf(x, 1, b))) + 2 * np.sum(np.log(pdf(x, 1, b_hat)))
    return q_b

q_c_list = np.array([q(pseudo_data_cont, b, b_hat) for b in b_values])
fig, ax = plt.subplots()
plt.plot(b_values, q_c_list)
q_min = np.min(q_c_list)
c_min_idx = np.argmin(q_c_list)
c_min = b_values[c_min_idx]

q_low_up_idx = np.argwhere(q_c_list < q_min + 4)
c_low = b_values[q_low_up_idx[0]]
c_up = b_values[q_low_up_idx[-1]]
ax.axhline(q_min + 4, linestyle='dashed', color='C1')
ax.axvline(b_truth, 0, 1, linestyle='dashed', color='k')
ax.text(0.9, 0.9,r'$c\;=\;%.2f ^{+%.2f}_{-%.2f}$'%(c_min, c_up-c_min, c_min-c_low),
        transform=ax.transAxes,
        horizontalalignment='right',
        verticalalignment='top',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))
#ax.axvline(b_hat, 0, 1, linestyle='dashed', color='k')
plt.ylabel('$q_c$')
plt.xlabel('c')
plt.title('Unbinned analysis')
plt.grid()

plt.xlim(b_values[q_low_up_idx[0]]-0.2, b_values[q_low_up_idx[-1]]+0.2)
plt.ylim(q_min-1, q_min + 10)

plt.show()