import numpy as np
import matplotlib.pyplot as plt

import EFTxSec as ExS 
import MC_generator as MCgenToy
import tauc as tau
from decimal import Decimal

cSMEFT = -0.94*10**-4
tc_binned_sm = tau.tc_binned(cSMEFT, 1)
tc_binned_eft = tau.tc_binned(cSMEFT, 0)
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

