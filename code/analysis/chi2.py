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
bins = np.array([500, 2500])#np.array([344, 360, 430, 500, 580, 680, 800, 1000, 1200, 1500, 2500])
# calculate bin centers
bin_centers = 0.5 * (bins[:-1] + bins[1:])


def kappa_values(bins):
	sigma_SM = np.array([MCgenToy.MC_genEvents(10**4, 1, order = "SM", mtt_min = bins[i], mtt_max = bins[i+1], gen_events = False) for i in range(len(bins)-1)])[:,0]
	kappa_NHO = np.array([MCgenToy.MC_genEvents(10**4, 1, order = "NHO", mtt_min = bins[i], mtt_max = bins[i+1], gen_events = False) for i in range(len(bins)-1)])[:,0]
	kappa_HO = np.array([MCgenToy.MC_genEvents(10**4, 1, order = "HO", mtt_min = bins[i], mtt_max = bins[i+1], gen_events = False) for i in range(len(bins)-1)])[:,0]
	return sigma_SM, kappa_NHO, kappa_HO

def cross_section(cSMEFT, sigma_SM, kappa_NHO, kappa_HO):
	sigma = sigma_SM + kappa_NHO*cSMEFT+kappa_HO*cSMEFT**2
	return sigma

def n_events(sigma):
	n_events = lum*sigma*eff
	return n_events

#Find the SM cross section and the kappa coefficients in every bin
sigma_SM, kappa_NHO, kappa_HO = kappa_values(bins)
#print("Total cross section in the SM: ", sigma_SM)
nu_i_0 = n_events(sigma_SM)
n_i = np.random.poisson(nu_i_0, len(nu_i_0))

def chi2(pseudo_data, unc_stat, cSMEFT):
	sigma_BSM = cross_section(cSMEFT, sigma_SM, kappa_NHO, kappa_HO)
	theory = n_events(sigma_BSM)
	ndat = len(theory)
	chi2 = (1/(ndat-1))*np.sum(((pseudo_data - theory)/unc_stat)**2)
	return chi2

def tc_binned(cSMEFT, H):
	#expected number of events in the SM
	nu_i_0 = n_events(sigma_SM)
	nu_tot_0 = np.sum(nu_i_0)
	#expected number of events in the EFT
	sigma_c =cross_section(cSMEFT, sigma_SM, kappa_NHO, 0)
	nu_i_c = n_events(sigma_c)
	nu_tot_c = np.sum(nu_i_c)

	#Construct samples of the binned test statistic tc
	n_samples = 10**6
	tc_list = []
	for i in range(n_samples):
		if H == 0:#EFT
			n_i = np.random.poisson(nu_i_c, len(nu_i_c))
		else:
			n_i = np.random.poisson(nu_i_0, len(nu_i_0))
		tc = nu_tot_c - nu_tot_0 - np.sum(n_i*np.log(nu_i_c/nu_i_0))
		tc_list.append(tc)
	tc = np.array(tc_list)
	return tc

#Plot the binned distribution
cSMEFT = 9.95*10**-5	
tc_binned_sm = tc_binned(cSMEFT, 1)
tc_binned_eft = tc_binned(cSMEFT, 0)
tc_med = np.median(tc_binned_sm)
nbins = 80
hist_tc_sm, bins_tc_sm = np.histogram(tc_binned_sm, bins=nbins, density=True)
hist_tc_eft, bins_tc_eft = np.histogram(tc_binned_eft, bins=nbins, density=True)
binwidth = bins_tc_eft[1]- bins_tc_eft[0]
tc_med_idx = np.digitize(tc_med, bins_tc_eft)
p_tc_med = binwidth * np.sum(hist_tc_eft[tc_med_idx:])


fig, ax = plt.subplots()
ax.step(bins_tc_eft[:-1], hist_tc_eft, where ='post', label = r'$H_0(c)$')
ax.step(bins_tc_sm[:-1], hist_tc_sm, where ='post', label = r'$H_1$')


plt.title(r'$\mathrm{pdf}(t_c|H)$')

textstr = '\n'.join((
    r'p = %.3f'%p_tc_med,
    r'$c_{tG} = %.2E$'% Decimal(cSMEFT)))

	
	# plt.text(0.1, 0.8, r'$c_{tG} = %.2E$'% Decimal(coeffs[i]), horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)
	# plt.text(0.1, 0.7)
props = dict(boxstyle='square', facecolor='white', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=8, verticalalignment='top', bbox=props)

plt.legend()
plt.show()





# def nu_tot(cSMEFT):
# 	xsec_bin = np.array([MCgenToy.MC_genEvents(10**4, cSMEFT, mtt_min = bins[i], mtt_max = bins[i+1], gen_events = False) for i in range(len(bins)-1)])[:,0]
# 	xsec_tot = np.sum(xsec_bin)
# 	nu_tot = lum*eff*xsec_tot
# 	nu_i = (xsec_bin/xsec_tot)*nu_tot
# 	return nu_tot, nu_i

# nu_tot_0, nu_i_0 = nu_tot(0)
# nu_tot_1, nu_i_1 = nu_tot(1)
# n_i = np.random.poisson(nu_i_0, len(nu_i_0))


# def chi2(cSMEFT):
# 	nu_i_c = nu_i_0 + cSMEFT*(nu_i_1- nu_i_0)
# 	chi2 = (1/(len(nu_i_c)-1))*np.sum(((n_i - nu_i_c)**2)/nu_i_0)
# 	return chi2


# c_tG = np.linspace(-10**-3, 10**-3, 100)
# c_tG_y = np.array([chi2(n_i, np.sqrt(nu_i_0), c_i) for c_i in c_tG])
# plt.ylim(c_tG_y.min() - 2, c_tG_y.min()+5.841)
# idx = np.argwhere(np.diff(np.sign(c_tG_y.min()+3.841 - c_tG_y))).flatten()
# plt.plot(c_tG, c_tG_y)
# plt.xlabel("ctG")
# plt.ylabel(r'$\chi^2$')
# plt.scatter(c_tG[np.argmin(c_tG_y)], c_tG_y.min(), marker = 'o', c = 'green')
# plt.hlines(c_tG_y.min()+3.841, c_tG[idx[0]], c_tG[idx[1]], colors = 'orange', linestyles = 'dashed', linewidth=2, label = r'$95\%\: \mathrm{CL\:range}$')
# plt.vlines(0, c_tG_y.min() - 2, c_tG_y.min()+5.841, colors = 'purple', linestyles = 'dashed', label = 'SM')
# plt.vlines(c_tG[idx[0]], c_tG_y.min() - 2, c_tG_y.min()+5.841, colors = 'orange', linestyles = 'dashed')
# plt.vlines(c_tG[idx[1]], c_tG_y.min() - 2, c_tG_y.min()+5.841, colors = 'orange', linestyles = 'dashed')
# plt.xlim(1.4*c_tG[idx[0]], 1.4*c_tG[idx[1]])
# plt.legend()
# plt.title(r'$\chi^2$' + " profile for SM pseudodata")
# plt.show()

# plt.errorbar(bin_centers, n_i, yerr=np.sqrt(n_i), fmt='r.')
# plt.step(bins[:-1], n_i, where ='post')
# plt.show()



