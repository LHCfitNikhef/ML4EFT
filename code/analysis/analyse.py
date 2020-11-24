import EFTxSec as ExS 
import MC_generator_hadronic_own as MCgenToy
import numpy as np
import matplotlib.pyplot as plt

#Generate and plot differential distribution in mtt

plot1DDist = False
plot2DDist = True	

coeffs=[0.001, 0.01, 0.1, 1, 10, 100]
xSec = [MCgenToy.MC_xSec(Nsamples = 10**4, cSMEFT = c, EFT = True, SM = True) for c in coeffs]

if plot1DDist == True:
	ExS.plotData(binWidth = 20, mtt_max = 400, cSMEFT = 1)

if plot2DDist == True:
	ExS.plot2Ddist(coeffs, xSec = xSec)