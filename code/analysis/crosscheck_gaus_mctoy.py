import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

import EFTxSec as ExS 
import MC_generator as MCgenToy
import tauc as tau

def gaus(x, mean, sigma):
 	return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mean)**2/(2*sigma**2))

#Generate data in the SM and the EFT at a chosen Wilson coefficient
data_sm = tau.load_data(0, 10**4)#load SM data

t_c = tau.find_pdf_tc_MC(1, 1, data_sm)
hist_tc, bins_tc = np.histogram(t_c, bins=30, density=True)
#fig, ax = plt.subplots()
plt.step(bins_tc[:-1], hist_tc, where ='post')
#plt.title(r'$\mathrm{pdf}(t_c|H_1)$ for c = 1')

mu_tc, sigma_tc = tau.find_pdf_tc(1,1,data_sm)
tc_hor = np.linspace(mu_tc-3*sigma_tc, mu_tc+3*sigma_tc, 1000)
gaus_eft = gaus(tc_hor, mu_tc, sigma_tc)
plt.plot(tc_hor, gaus_eft)

plt.show()