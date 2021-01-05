import EFTxSec as ExS 
import numpy as np
import matplotlib.pyplot as plt

mtt = 400
y = 2
c = 1

dsigma_dmtt_dy_EFT = ExS.dsigma_dmtt_dy(mtt, y, c, NP = 1)
dsigma_dmtt_dy_SM = ExS.dsigma_dmtt_dy(mtt, y, 0,  NP = 0)

r_c = dsigma_dmtt_dy_EFT/dsigma_dmtt_dy_SM
tau_c = np.log(r_c)
print("log likelihood ratio: ", tau_c)