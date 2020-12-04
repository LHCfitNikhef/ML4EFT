import EFTxSec_vers_02 as ExS 
import MC_generator_hadronic_own as MCgenToy
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import integrate
import pylhe

from scipy.optimize import curve_fit

# median_tc = []
# median_tc_unc = []
# fig, ax = plt.subplots()
# for c in np.arange(0.1, 1, 0.1):
# 	data = []
# 	with open('tc_%.2f.dat'%c) as f:
# 		for line in f.readlines():
# 			#row = [x for x in line]
# 			row = [float(x) for x in line.split()][0]
# 			data.append(row)
# 			#data.append(line)
# 	data = np.array(data)  

# 	#print(data)
# 	hist_tc, bins_tc = np.histogram(data, bins=40, density=True)
# 	median_tc.append(np.median(data))
# 	# var_median = 1/(4*len(data)*)
# 	ax.step(bins_tc[:-1], hist_tc, where ='post', label = 'c = %.1f'%c)

# plt.xlabel(r'$t_c$')
# plt.legend()
# plt.title(r'$pdf(t_c|H_1)$')
# plt.show()


# median_tc = np.array(median_tc)
# tc = np.arange(0.1, 1, 0.1)
# plt.scatter(tc, median_tc)

# # plt.show()


# def func(x, a, b, c):
# 	return a + b*x + c*x**2

# popt, pcov = curve_fit(func, tc, median_tc)
# plt.plot(tc, func(tc, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, d=%5.3f' % tuple(popt))
# plt.xlabel(r'$c$')
# plt.ylabel(r'$t_{med}(c)$')
# plt.legend()
# plt.title("Median of " + r'$t_c$' + " under the SM")
# plt.show()
# # sigma_median = 1/np.sqrt(4*)

data = []
fig, ax = plt.subplots()
with open('t1_H1.dat') as f:
	for line in f.readlines():
		#row = [x for x in line]
		row = [float(x) for x in line.split()][0]
		data.append(row)
		#data.append(line)
	data = np.array(data)  

	#print(data)
	hist_tc, bins_tc = np.histogram(data, bins=40, density=True)
	#median_tc.append(np.median(data))
	# var_median = 1/(4*len(data)*)
	ax.step(bins_tc[:-1], hist_tc, where ='post')

tc_hor = np.linspace(-7.5, 12.5, 100)
def gaus(x, sigma, mean):
	return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mean)**2/(2*sigma**2))
plt.plot(tc_hor, gaus(tc_hor, 2.60040293387464, 3.675358012666535))
plt.xlabel(r'$t_c$')
plt.legend()
plt.title(r'$pdf(t_{1}|H_1)$')
plt.show()



