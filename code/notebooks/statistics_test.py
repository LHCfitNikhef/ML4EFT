#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, ncx2

data_normal = np.random.normal(6, 1, 100  00)

fig = plt.figure(figsize=(10,6))
# plt.hist(data_normal, bins=70)
# plt.show()

# plt.hist(data_normal ** 2, bins=70, density=True)
plt.hist(((data_normal - 1)/1) ** 2, bins=70, density=True)
#rv_chi2 = chi2(df=1)
nc = ((6-1)/1) ** 2
rv_nc2 = ncx2(df=1, nc=nc)
x = np.linspace(0, 60, 100)
plt.plot(x, rv_nc2.pdf(x), color='red', lw=2)
plt.show()

