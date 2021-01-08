import EFTxSec as ExS 
import numpy as np
import matplotlib.pyplot as plt

mtt = 400
y = 2
c = 1




def n_alpha_ana(x):
	mtt, y = x[0], x[1]
	mu = 91.188
	x1 = mtt/np.sqrt(ExS.s)*np.exp(y)
	x2 = mtt/np.sqrt(ExS.s)*np.exp(-y)
	#kappa_LO_qq = ExS.LambdaSMEFT*ExS.sigma_part_qq_LO(mtt, 1)
	#kappa_LO_gg = ExS.LambdaSMEFT*ExS.sigma_part_gg_LO(mtt, 1)
	return (2*mtt / (ExS.LambdaSMEFT**2*ExS.dsigma_dmtt_dy(mtt, y, 0, NP = 0)*ExS.s))*ExS.LambdaSMEFT**2*ExS.weight(mtt, mu, x1, x2, 1, order = "NHO", NP = None)


# dsigma_dmtt_dy_EFT = ExS.dsigma_dmtt_dy(mtt, y, c, NP = 1)
# dsigma_dmtt_dy_SM = ExS.dsigma_dmtt_dy(mtt, y, 0,  NP = 0)

# r_c = dsigma_dmtt_dy_EFT/dsigma_dmtt_dy_SM
# tau_c = np.log(r_c)
# print("log likelihood ratio: ", tau_c)

print(n_alpha_ana([-0.7106325341398294, 0.05537046044063021]))