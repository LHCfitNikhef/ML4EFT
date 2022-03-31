import numpy as np
import matplotlib.pyplot as plt
import pymultinest
import json

mu_true = 4
sigma_true = 0.5
n_dat = 40

data_x = np.arange(n_dat)
np.random.seed(0)
data_y = np.random.normal(mu_true, sigma_true, n_dat)

fig = plt.figure()
x = np.linspace(-1, n_dat, 100)
mu_ml = np.mean(data_y)

plt.errorbar(data_x, data_y, yerr=sigma_true, linestyle="none", marker="o")
plt.plot(x, mu_ml * np.ones(x.shape))
plt.ylim((mu_true - 2, mu_true + 2))

fig.savefig('/data/theorie/jthoeve/multinest/demo/example/data.png')

def chi2(data, mu):
    return np.sum(((data - mu) / sigma_true) ** 2)

mu_range = np.linspace(mu_true - 0.5, mu_true + 0.5, 5000)
chi2_profile = np.array([chi2(data_y, mu) for mu in mu_range])

fig = plt.figure()
plt.plot(mu_range, chi2_profile)
chi2_min = chi2(data_y, mu_ml)
plt.scatter(mu_ml, chi2_min, marker='x')
plt.axhline(chi2(data_y, mu_ml) + 1, 0, 1)

idx = np.argwhere(chi2_profile <= chi2_min + 1)
idx_low = idx[0]
idx_high = idx[-1]

mu_low = mu_range[idx_low]
mu_high = mu_range[idx_high]


np.save('/data/theorie/jthoeve/multinest/demo/example/grid_scan/bounds.npy', np.array([mu_low, mu_high]))

plt.ylim((chi2(data_y, mu_ml) - 1, chi2(data_y, mu_ml) + 2))
plt.xlim((mu_low - 0.1, mu_high + 0.1))

plt.axvline(mu_low, 0, 1, linestyle='dotted', color='k')
plt.axvline(mu_high, 0, 1, linestyle='dotted', color='k')

fig.savefig('/data/theorie/jthoeve/multinest/demo/example/chi2.png')


### nested sampling ###


outputfile = '/data/theorie/jthoeve/multinest/demo/example/ns_run/samples'

nparams = 1
nlivepoints=2000

def myprior(cube, ndim, nparam):
    cube[0] = 8 * cube[0]

def myloglike(cube, ndim, nparam):
    mu = cube[0]
    return -0.5 * chi2(data_y, mu)


result = pymultinest.run(LogLikelihood=myloglike, Prior=myprior,
                         n_dims=nparams, outputfiles_basename=outputfile, verbose=True, n_live_points=nlivepoints,
                         const_efficiency_mode=False, resume=False, importance_nested_sampling=True)
