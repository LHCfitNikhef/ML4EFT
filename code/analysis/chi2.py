#Compute the chi-squared profile

import EFTxSec as ExS 
import numpy as np 
import matplotlib.pyplot as plt
import sys
import MC_generator as MCgenToy
from scipy import integrate
from decimal import Decimal

lum = 6*10**6#in pb^-1
eff = 1#10**-5
bins = np.array([344, 360, 430, 500, 580, 680, 800, 1000, 1200, 1500, 2500])
# calculate bin centers
bin_centers = 0.5 * (bins[:-1] + bins[1:])

def nu_tot(cSMEFT):
	xsec_bin = np.array([MCgenToy.MC_genEvents(10**4, cSMEFT, mtt_min = bins[i], mtt_max = bins[i+1], gen_events = False) for i in range(len(bins)-1)])[:,0]
	xsec_tot = np.sum(xsec_bin)
	nu_tot = lum*eff*xsec_tot
	nu_i = (xsec_bin/xsec_tot)*nu_tot
	return nu_tot, nu_i

nu_tot_0, nu_i_0 = nu_tot(0)
nu_tot_1, nu_i_1 = nu_tot(1)
n_i = np.random.poisson(nu_i_0, len(nu_i_0))


def chi2(cSMEFT):
	nu_i_c = nu_i_0 + cSMEFT*(nu_i_1- nu_i_0)
	chi2 = (1/(len(nu_i_c)-1))*np.sum(((n_i - nu_i_c)**2)/nu_i_0)
	return chi2


c_tG = np.linspace(-10**-3, 10**-3, 100)
c_tG_y = np.array([chi2(c_i) for c_i in c_tG])
plt.ylim(c_tG_y.min() - 2, c_tG_y.min()+5.841)
idx = np.argwhere(np.diff(np.sign(c_tG_y.min()+3.841 - c_tG_y))).flatten()
plt.plot(c_tG, c_tG_y)
plt.xlabel("ctG")
plt.ylabel(r'$\chi^2$')
plt.scatter(c_tG[np.argmin(c_tG_y)], c_tG_y.min(), marker = 'o', c = 'green')
plt.hlines(c_tG_y.min()+3.841, c_tG[idx[0]], c_tG[idx[1]], colors = 'orange', linestyles = 'dashed', linewidth=2, label = r'$95\%\: \mathrm{CL\:range}$')
plt.vlines(0, c_tG_y.min() - 2, c_tG_y.min()+5.841, colors = 'purple', linestyles = 'dashed', label = 'SM')
plt.vlines(c_tG[idx[0]], c_tG_y.min() - 2, c_tG_y.min()+5.841, colors = 'orange', linestyles = 'dashed')
plt.vlines(c_tG[idx[1]], c_tG_y.min() - 2, c_tG_y.min()+5.841, colors = 'orange', linestyles = 'dashed')
plt.xlim(1.4*c_tG[idx[0]], 1.4*c_tG[idx[1]])
plt.legend()
plt.title(r'$\chi^2$' + " profile for SM pseudodata")
plt.show()

# plt.errorbar(bin_centers, n_i, yerr=np.sqrt(n_i), fmt='r.')
# plt.step(bins[:-1], n_i, where ='post')
# plt.show()



