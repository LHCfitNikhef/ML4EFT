import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
import EFTxSec as ExS 
import MC_generator as MCgenToy
import tauc as tau
import sys


def gaus(x, mean, sigma):
 	return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mean)**2/(2*sigma**2))

#Generate data in the SM and the EFT at a chosen Wilson coefficient
n_samples = 10**4
#NP = 0: SM data, NP = 1: linear EFT, NP = 2: quadratic EFT
data_sm = tau.load_data(0, n_samples, NP = 0)#load SM data
data_eft = tau.load_data(9.95*10**-5, 10**4, NP = 1)#load

coeffs = np.array([9.95*10**-5])#-np.linspace(1.79*10**-3, 1.87*10**-3,9)
npar = len(coeffs)
gs = int(np.sqrt(npar))+1
ncols, nrows = 1,1##3,3#gs, gs
plt.figure(figsize=(nrows*4, ncols*3))
cnt=1
for i in range(npar):
	ax = plt.subplot(ncols, nrows, cnt)
	plt.xlabel(r'$t_c$')
	ax.set_title(r'$pdf(t_{c}|H)$')

	mu_tc_0, sigma_tc_0 = tau.find_pdf_tc(coeffs[i], 0, data_eft)
	mu_tc_1, sigma_tc_1 = tau.find_pdf_tc(coeffs[i], 1, data_sm)

	z_score = (mu_tc_1-mu_tc_0)/sigma_tc_0

	tc_hor = np.linspace(mu_tc_0-3*sigma_tc_0, mu_tc_1+3*sigma_tc_1, 1000)
	gaus_eft = gaus(tc_hor, mu_tc_0, sigma_tc_0)
	plt.plot(tc_hor, gaus_eft, label = r'$H_0(c)$')
	
	plt.fill_between(tc_hor, gaus_eft, where = tc_hor > mu_tc_1, color='#539ecd')
	plt.plot(tc_hor, gaus(tc_hor, mu_tc_1, sigma_tc_1), label = r'$H_1$')

	textstr = '\n'.join((
    r'$c_{tG} = %.2E$'% Decimal(coeffs[i]),
    r'$\mathrm{z}=%.2f$' %z_score))
	props = dict(boxstyle='square', facecolor='white', alpha=0.5)
	ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=8, verticalalignment='top', bbox=props)

	plt.legend()

	cnt+=1

plt.show()

