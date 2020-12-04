import EFTxSec_vers_03 as ExS 
import MC_generator_hadronic_own as MCgenToy
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import integrate
import pylhe
import time
import lhapdf


luminosity = 6*10**6#in pb^-1
ECM = 14000
s = ECM**2
eff = 10**-5#selection efficiency
pb_convert = 3.894E8
cSMEFT = 1
xSec_SM = 2.643116#101.347543074 #MadGraph result  in pb
xSec_EFT = 3.25015#125.640073926


#diff x-sec in mtt and y as a function of the ctG
def dsigma_dmtt_dy(mtt, y, cSMEFT):
	x1 = mtt/np.sqrt(s)*np.exp(y)
	x2 = mtt/np.sqrt(s)*np.exp(-y)
	dsigma_dmtt_dy = 2*mtt/s*ExS.v_weight(mtt, 91.188, x1, x2, cSMEFT)/(x1*x2)
	return pb_convert*dsigma_dmtt_dy

#print("Computing the inclusive cross sections in the SM and EFT at c = %2f.:" %(cSMEFT))

#xSec_SM, w_max_SM = MCgenToy.MC_xSec(Nsamples = 10**4, cSMEFT = 0)
#xSec_EFT, w_max_EFT = MCgenToy.MC_xSec(Nsamples = 10**4, cSMEFT = 1)

def N_mean(cSMEFT):#Only works up to linear order in the EFT cross section
	xSec = xSec_SM + cSMEFT*(xSec_EFT-xSec_SM)
	return xSec*luminosity*eff

#Generate samples with cSMEFT and save to hard disk for later use
def load_data(data_exist = False, cSMEFT = cSMEFT, use_MG = True, w_max = 0):
	if data_exist == False:
		smp_mtt, smp_y = MCgenToy.MC_genEvents(Nsamples = 10**4, w_max = w_max_EFT, cSMEFT = cSMEFT)
		np.savetxt('data.dat', np.transpose([smp_mtt,smp_y]))
	data = []
	if use_MG == False:
		with open('data.dat') as f:
			for line in f.readlines():
				row = [float(x) for x in line.split()] 
				data.append(row)
		data = np.array(data)   
		return data
	if use_MG == True:
		cnt = 0
		N_MC_samples = 10**5
		for e in pylhe.readLHE('lhe_events/gg_tt_SM_1500_10E5.lhe'):
			sys.stdout.write("progress: %d%%   \r" % (float(cnt)*100./(N_MC_samples)) )
			sys.stdout.flush()
			mtt = ExS.invariant_mass(e.particles[-1],e.particles[-2])
			y = ExS.rapidity(e.particles[-1],e.particles[-2])
			data.append([mtt, y])
			cnt += 1
		data = np.array(data)
		return data
    	
#load the data, or generate it if it does not exist
print("Loading the dataset: ")
data = load_data(data_exist = True)
nMCsamples = data.shape[0]#number of Monte Carlo samples 
print("Successfully loaded the entire dataset with %f samples"%(nMCsamples))

#t_c_med = []
#for c in np.arange(0, 1, 0.1):


#the expected number of events under H0 (EFT) and H1 (SM)
N_H0 = N_mean(cSMEFT= cSMEFT)
N_H1 = N_mean(cSMEFT=0)

#print("expected counts:", N_H1)


t_c = []

#The invariant mass and rapidity data points
mtt = data[:10**3,0]
y = data[:10**3,1]



#start = time.time()
#Construct tau_c
dsigma_dmtt_dy_EFT = dsigma_dmtt_dy(mtt, y, cSMEFT = cSMEFT)
dsigma_dmtt_dy_SM = dsigma_dmtt_dy(mtt, y, cSMEFT = 0)

#end = time.time()
#print(end - start)

# for i in range(dataset.shape[0]):
# 	dsigma_dmtt_dy_EFT.append(dsigma_dmtt_dy(mtt[i], y[i], cSMEFT = cSMEFT))
# 	dsigma_dmtt_dy_SM.append(dsigma_dmtt_dy(mtt[i], y[i], cSMEFT = 0))
# dsigma_dmtt_dy_EFT = np.array(dsigma_dmtt_dy_EFT)
# dsigma_dmtt_dy_SM = np.array(dsigma_dmtt_dy_SM)
r_c = dsigma_dmtt_dy_EFT/dsigma_dmtt_dy_SM
tau_c = np.log(r_c)

#Construct the test statistic t_c and strore it
mu_tauc = np.mean(tau_c)
sigma_tauc = 1/(np.sqrt(N_H1))*np.sqrt(np.mean(tau_c**2))

mu_tc = N_H0-N_H1-N_H1*mu_tauc
sigma_tc = N_H1*sigma_tauc


#t_c_med.append(np.median(t_c))

#np.savetxt('tc_%.2f.dat'%c, t_c)
print("the mean is given by: ", mu_tc)
print("the std dev is given by: ", sigma_tc)

	# hist_tc, bins_tc = np.histogram(t_c, bins=30, density=True)

	# fig, ax = plt.subplots()
	# ax.step(bins_tc[:-1], hist_tc, where ='post')
	# plt.title(r'$\mathrm{pdf}(t_c|H_1)$ for c = 1')
	# plt.show()

#MCgenToy.generate_histo(t_c, 'tc')
# t_c_med = np.array(t_c_med)
# fig, ax = plt.subplots()
# ax.scatter(np.arange(0, 1, 0.1), t_c_med)
# plt.title("Median value")
# plt.show()


plot1DDist = False
plot2DDist = False

# if plot1DDist == True:
#  	ExS.plotData(binWidth = 5, mtt_max = 1000, cSMEFT = 1)

# if plot2DDist == True:
# 	coeffs=[0.001, 0.01, 0.1, 1, 10, 100]
# 	xSec = [MCgenToy.MC_xSec(Nsamples = 10**4, cSMEFT = c, EFT = True, SM = True) for c in coeffs]
# 	ExS.plot2Ddist(coeffs, xSec = xSec)
