#%%
import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.xsec.vh_prod as vh_prod

bins = np.linspace(0.3, 1, 10)
n_dat = len(bins) - 1
cHW = 1
cHq3 = 0
lumi = 1e5

sigma_i_sm = vh_prod.sigma_bin(bins, 0, 0, lin=True, quad=False)
sigma_i_eft = vh_prod.sigma_bin(bins, cHW, cHq3, lin=True, quad=False)

nu_i_sm = lumi * sigma_i_sm
#nu_i_eft = lumi * sigma_i_eft
coeff = vh_prod.findCoeff(bins)
nu_i_eft = vh_prod.nu_i(coeff, cHW, cHq3, lumi, lin=True)

# pseudo data settings
delta_stat = 0.05
delta_lum = 0.02

r_i_stat = np.random.normal(size=n_dat)
r_sys = np.random.normal()
alpha_i = delta_stat * nu_i_eft
beta_i = nu_i_eft * delta_lum

# pseudo experiment
n_i_exp = nu_i_eft * (1 + r_i_stat * delta_stat + r_sys * delta_lum)

def r_i_sys_rec(cHW):
    sigma_i_eft = vh_prod.sigma_bin(bins, cHW, 0, lin=True, quad=False)
    nu_i_eft = lumi * sigma_i_eft
    r_i_sys_rec = np.sum(((n_i_exp - nu_i_eft) * beta_i) / alpha_i ** 2) / (1 + np.sum(beta_i ** 2 / alpha_i ** 2))
    return r_i_sys_rec

print("lambda recovered = ", r_i_sys_rec(1))
print("lambda true = ", r_sys)

def chi2(data, coeff, cHW, cHq3, r_sys, beta_i, alpha_i):
    theory = vh_prod.nu_i(coeff, cHW, cHq3, lumi, lin=True)
    chi2_value = np.sum((data-theory-r_sys * beta_i) ** 2 / alpha_i ** 2) + r_sys ** 2
    return chi2_value

chi2_values = []
cHW_range = np.linspace(cHW-0.2, cHW+0.2, 100)
r_i_sys_range = np.linspace(r_sys - 4, r_sys + 4, 100)
coeff = vh_prod.findCoeff(bins)
for cHW_i in cHW_range:
    for r_sys_i in r_i_sys_range:
        chi2_value = chi2(n_i_exp, coeff, cHW_i, 0, r_sys_i, beta_i, alpha_i)
        chi2_values.append(chi2_value)
chi2_values = np.array(chi2_values)
chi2_values = np.reshape(chi2_values, (cHW_range.shape[0], r_i_sys_range.shape[0]))
xx, yy = np.meshgrid(r_i_sys_range, cHW_range)
contours = plt.contour(xx, yy, chi2_values, np.array([np.min(chi2_values)+3.84]), colors='black')
img = plt.imshow(chi2_values, extent=[np.min(r_i_sys_range), np.max(r_i_sys_range), np.min(cHW_range), np.max(cHW_range)], origin='lower', cmap='RdGy', aspect='auto', vmin=0)
cbar = plt.colorbar(img, shrink=0.8, extend='max')

plt.scatter(r_sys, cHW, marker='x', color='black', label='Truth')
idx = np.where(chi2_values == np.min(chi2_values))
plt.scatter(r_i_sys_range[idx[1]], cHW_range[idx[0]], marker='o', color='black', label=r'$\chi^2_{\rm{min}}$')

r_i_sys_rec_array = np.array([r_i_sys_rec(cHW_i) for cHW_i in cHW_range])
plt.plot(r_i_sys_rec_array,cHW_range,  linestyle='dashed', color='black')
plt.legend()
#plt.vlines(r_i_sys_rec, np.min(cHW_range), np.max(cHW_range), linestyles='dashed', color='black')

plt.xlabel(r'$\lambda$')
plt.ylabel(r'$cHW$')
plt.show()

# plot theory predictions
fig, ax = plt.subplots(figsize=(10,6))
ax.step(bins[:-1], nu_i_sm, where='post', label='SM (Theory)')
ax.step(bins[:-1], nu_i_eft, where='post', label='EFT (Theory)')
ax.step(bins[:-1], n_i_exp, where='post', label='Data')

plt.xlabel(r'$m_{ZH}\;[\mathrm{TeV}]$')
plt.ylabel('events')
plt.yscale('log')
plt.legend()
plt.show()
