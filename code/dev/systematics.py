
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import chi2, norm, ncx2, poisson
#%%

def sample_dist(ntot, n_exp, c, n_bins):
    sigma = 3 + c  # eft
    mu = 0

    sigma_alt = 3  # sm
    mu_alt = mu

    bins = np.linspace(norm.ppf(1e-3, mu, 1), norm.ppf(1 - 1e-3, mu, 1), n_bins - 1)
    cdf = norm.cdf(bins, mu, sigma)

    diff = cdf[1:] - cdf[:-1]
    weights = np.insert(diff, 0, cdf[0])
    weights = np.append(weights, 1 - cdf[-1])
    nu_i = ntot * weights

    q_list = []
    for i in range(n_exp):
        n_i = np.random.poisson(nu_i, len(nu_i))
        if 0 in n_i:
            continue
        q = 2 * np.sum(n_i * np.log(n_i / nu_i) + nu_i - n_i)
        q_list.append(q)

    cdf_alt = norm.cdf(bins, mu_alt, sigma_alt)
    diff_alt = cdf_alt[1:] - cdf_alt[:-1]
    weights_alt = np.insert(diff_alt, 0, cdf_alt[0])
    weights_alt = np.append(weights_alt, 1 - cdf_alt[-1])
    nu_i_alt = ntot * weights_alt

    q_list_alt = []
    for i in range(n_exp):
        n_i_alt = np.random.poisson(nu_i_alt, len(nu_i_alt))
        if 0 in n_i_alt:
            continue
        q = 2 * np.sum(n_i_alt * np.log(n_i_alt / nu_i) + nu_i - n_i_alt)
        q_list_alt.append(q)

    t_asimov = 2 * np.sum(nu_i_alt * np.log(nu_i_alt / nu_i) + nu_i - nu_i_alt)

    return q_list, q_list_alt, t_asimov

#%%
# scanning
def scan_p(c_values, bins, mu_alt, sigma_alt, n_bins):
    ntot = 10000

    cdf_alt = norm.cdf(bins, mu_alt, sigma_alt)
    weights_alt = cdf_alt[1:] - cdf_alt[:-1]
    nu_i_alt = ntot * weights_alt

    exp_p_list = []
    for c in c_values:
        sigma = sigma_alt + c  # eft
        mu = mu_alt

        cdf = norm.cdf(bins, mu, sigma)
        weights = cdf[1:] - cdf[:-1]
        nu_i = ntot * weights

        t_asimov = 2 * np.sum(nu_i_alt * np.log(nu_i_alt / nu_i) + nu_i - nu_i_alt)

        rv_nc = ncx2(df=n_bins, nc=t_asimov)
        rv_chi2 = chi2(df=n_bins)
        med_q = rv_nc.ppf(0.5)  # median q under alt
        exp_p = rv_chi2.sf(med_q)  # expected p value under null

        exp_p_list.append(exp_p)

    return np.array(exp_p_list)

#%%
def plot_dist(df, nc, q, q_alt, c):
    font = {'size': 13,
            'weight': 'normal',
            'family': 'DejaVu Sans'}

    matplotlib.rc('font', **font)

    fig, ax = plt.subplots(figsize=(10, 6))

    rv_chi2 = chi2(df=df)
    rv_nc = ncx2(df=df, nc=nc)

    med_q = rv_nc.ppf(0.5)  # median q under alt
    exp_p = rv_chi2.sf(med_q)  # expected p value under null

    x = np.linspace(rv_chi2.ppf(1e-4), rv_nc.ppf(1 - 1e-3), 400)
    ax.plot(x, rv_chi2.pdf(x), color='C0', lw=2, label=r'$\chi^2(%d, %d)$' % (df, 0))
    ax.plot(x, rv_nc.pdf(x), color='C1', lw=2, label=r'$\chi^2(%d, %.2f)$' % (df, nc))

    ax.hist(q, bins=70, density=True, alpha=0.3)
    ax.hist(q_alt, bins=70, density=True, alpha=0.3)

    ax.axvline(med_q, 0, 1, linestyle='dashed', color='red')
    ax.fill_between(x, rv_chi2.pdf(x), 0, where=x > med_q, color='red')

    ax.text(0.75, 0.7, "Median p = {:.3f}".format(exp_p), transform=ax.transAxes)
    ax.text(0.75, 0.65, "c = {:.3f}".format(c), transform=ax.transAxes)

    plt.xlim(0, np.max(x))
    #plt.ylim(0, 0.5)
    plt.xlabel(r'$q(c)$')
    plt.title("Asymptotic sampling distributions - {:d} bins".format(df))
    plt.legend()

    return fig
#%%

def bin_dependence(n_bins, cmin, cmax):
    mu_alt = 0
    sigma_alt = 3

    bins = np.linspace(norm.ppf(1e-3, mu_alt, 1), norm.ppf(1 - 1e-3, mu_alt, 1), n_bins - 1)

    c_values = np.linspace(cmin, cmax, 1200)
    p_values = scan_p(c_values, bins, mu_alt, sigma_alt, n_bins)

    # find p = 0.05
    idx1 = np.argwhere(p_values >= 0.05)[0]
    idx2 = np.argwhere(p_values >= 0.05)[-1]
    c_min = c_values[idx1][0]
    c_max = c_values[idx2][0]

    # plot scan
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(c_values, p_values)
    ax.axvline(c_max)
    ax.axhline(0.05, color='red')
    plt.xlim(np.min(c_values), np.max(c_values))
    plt.show()

    # find sampling dist
    q_list, q_list_alt, t_asimov = sample_dist(ntot=1000, n_exp=100000, c=c_max, n_bins=n_bins)

    # plot distributions
    fig1 = plot_dist(df=n_bins, nc=t_asimov, q=q_list, q_alt=q_list_alt, c=c_max)
    return fig1
    #fig1.savefig("plots/dist_{}.pdf".format(n_bins))
#%%
fig = bin_dependence(3, cmin= -0.5, cmax=0.5)
plt.show()
#%%
fig = bin_dependence(20, cmin= -0.5, cmax=0.5)
plt.show()