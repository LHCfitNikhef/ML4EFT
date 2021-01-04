import EFTxSec as ExS 
import MC_generator as MCgenToy
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import integrate
import pylhe
import time
import lhapdf


#Parameters 
luminosity = 6*10**6#in pb^-1
ECM = 14000
s = ECM**2
pb_convert = 3.894E8
eff = 1
mt = 172
mtt_min = 2*mt#apply cuts
mtt_max = ECM


#Setup
xSec_SM = MCgenToy.MC_genEvents(10**5, 0, NP = 0, mtt_min = mtt_min, mtt_max = mtt_max, gen_events = False)[0]
xSec_EFT = MCgenToy.MC_genEvents(10**5, 1, NP = 1, mtt_min = mtt_min, mtt_max = mtt_max, gen_events = False)[0]



def N_mean(cSMEFT):#Only works up to linear order in the EFT cross section
	xSec = xSec_SM + cSMEFT*(xSec_EFT-xSec_SM)
	return xSec*luminosity*eff


def load_data(cSMEFT, n_samples, order = None, NP = None):
	""" Returns samples of the invariant mass mtt and the rapidity y under hypothesis H.
	Format of output: 
		1st column: mtt
		2nd column: y
	One can indicate the region of phase space to use for generating pseudo data.
	"""
	
	mtt, y = MCgenToy.MC_genEvents(n_samples, cSMEFT, order, NP, mtt_min = mtt_min, mtt_max = mtt_max)
	data = np.transpose([mtt, y])
	return data

def draw_hist(data, bins):
	for i in range(len(data)):
		hist, bins = np.histogram(data[i], bins = bins, density= False)
		plt.step(bins, np.append(hist, hist[-1]), where ='post', label = i)
	plt.legend()
	plt.show()


def find_pdf_tc(c, H, data):
	""" Return the mean and standard deviation of the pdf of tc under hypothesis H with Wilson coefficient c.
	Input: the Wilson coeffcient c, hypothesis H (SM or EFT), pseudo data (first column the invariant mass mtt, second column the rapidity y)

	"""
	
	#The expected number of events in the EFT and the SM
	N_H0 = N_mean(c)
	N_H1 = N_mean(0)

	

	mtt = data[:,0]
	y = data[:,1]
	
	dsigma_dmtt_dy_EFT = ExS.dsigma_dmtt_dy(mtt, y, c, NP = 1)
	dsigma_dmtt_dy_SM = ExS.dsigma_dmtt_dy(mtt, y, 0,  NP = 0)

	r_c = dsigma_dmtt_dy_EFT/dsigma_dmtt_dy_SM
	tau_c = np.log(r_c)
	mu_tauc = np.mean(tau_c)
	
	if H == 0:
		sigma_tauc = 1/(np.sqrt(N_H0))*np.sqrt(np.mean(tau_c**2))
		sigma_tc = N_H0*sigma_tauc
		mu_tc = N_H0-N_H1-N_H0*mu_tauc
	else:#H=1
		sigma_tauc = 1/(np.sqrt(N_H1))*np.sqrt(np.mean(tau_c**2))
		sigma_tc = N_H1*sigma_tauc
		mu_tc = N_H0-N_H1-N_H1*mu_tauc

	return mu_tc, sigma_tc

def find_pdf_tc_MC(c, H, data):

	#the expected number of events under H0 (EFT) and H1 (SM)
	N_H0 = N_mean(c)
	N_H1 = N_mean(0)


	nMCsamples = data.shape[0]


	print("test", N_H1, nMCsamples)

	#print("expected counts:", N_H1)
	t_c = []

	N_datasets = 10**5#Number of datasets for which we compute t_c

	print("Computing the test statistic tc for %f datasets"%(N_datasets))
	cnt = 0
	while cnt < N_datasets:
		
		sys.stdout.write("progress: %d%%   \r" % (float(cnt)*100./(N_datasets)) )
		
		#The size of the dataset is drawn from a Poisson distribution with mean N(X|H_1)
		n_cal = np.random.poisson(lam=N_H1, size=1)[0]
		#choose n_cal samples from the dataset of size nMCsamples
		random_indices = np.random.choice(nMCsamples, size = n_cal, replace = False)
		dataset = data[random_indices,:]

		#The invariant mass and rapidity data points
		mtt = dataset[:,0]
		y = dataset[:,1]

		#Construct tau_c
		dsigma_dmtt_dy_EFT = ExS.dsigma_dmtt_dy(mtt, y, c)
		dsigma_dmtt_dy_SM = ExS.dsigma_dmtt_dy(mtt, y, 0)
		tau_c = dsigma_dmtt_dy_EFT/dsigma_dmtt_dy_SM

		#Construct the test statistic t_c and store it
		tc = N_H0 - N_H1 - np.sum(np.log(tau_c))
		t_c.append(tc)

		cnt += 1
		
		sys.stdout.flush()
	t_c = np.array(t_c)
	return t_c


# calculate bin centers
#bin_centers = 0.5 * (bins[:-1] + bins[1:])

def nu_tot(cSMEFT):
	bins = np.array([344, 360, 430, 500, 580, 680, 800, 1000, 1200, 1500, 2500])
	xsec_bin = np.array([MCgenToy.MC_genEvents(10**4, cSMEFT, NP = 1, mtt_min = bins[i], mtt_max = bins[i+1], gen_events = False) for i in range(len(bins)-1)])[:,0]
	xsec_tot = np.sum(xsec_bin)
	nu_tot = luminosity*eff*xsec_tot
	nu_i = (xsec_bin/xsec_tot)*nu_tot
	return nu_tot, nu_i

def tc_binned(cSMEFT, H):
	nu_tot_0, nu_i_0 = nu_tot(0)
	nu_tot_1, nu_i_1 = nu_tot(1)
	nu_tot_c = nu_tot_0 + cSMEFT*(nu_tot_1- nu_tot_0) 
	nu_i_c = nu_i_0 + cSMEFT*(nu_i_1- nu_i_0)

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

	