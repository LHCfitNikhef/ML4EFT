import EFTxSec as xsec
import numpy as np
import matplotlib.pyplot as plt

mt = 172
s = (13*10**3)**2
Ymax = np.log(np.sqrt(s)/(2*mt))
Ymin = -Ymax

vdsigma_dmtt_dy = np.vectorize(xsec.dsigma_dmtt_dy)


plt.figure()
x = np.arange(2*mt,3*mt, 0.1)
y = np.arange(Ymin, Ymax, 0.1)
X,Y = np.meshgrid(x, y)
Z = vdsigma_dmtt_dy(X, Y, 1, NP = 1)
im = plt.imshow(Z, cmap = plt.cm.Wistia, aspect = 23.7, extent=[2*mt, 3*mt, Ymin, Ymax], vmax = 10**-3, vmin = 0)
plt.colorbar(im)

plt.ylabel(r'Rapidity $Y = \log\sqrt{x_1/x_2}$')
plt.xlabel(r'$m_{tt}\;\mathrm{GeV}$')

#plt.title(r'$pdf(x|H_1(c=10^{%d}))$'%(-3+3))
plt.show()

#print(xsec.dsigma_dmtt_dy(400, 3.8, 1, NP = 1))