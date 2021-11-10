import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon

exp_rv = expon()
norm_rv = norm(loc=2, scale=0.1)

def pdf(x, mass, a, b, c):
    norm_rv = norm(loc=mass, scale=0.2)
    prob = (a * exp_rv.pdf(x) + b * norm_rv.pdf(x) + c*np.exp(-0.9 * x))
    return prob

mass_truth = 3
mass_range = np.arange(mass_truth-1, mass_truth+3, 0.001)
fig, ax = plt.subplots()
x = np.linspace(expon.ppf(0.01), 4, 100)
y_np = pdf(x, mass_truth, 0, 0.2, 1)
y_sm = pdf(x, mass_truth, 1, 0, 0)
ax.plot(x, y_np, 'red', lw=2, linestyle='dashed')
ax.plot(x, y_sm, 'C0', lw=2)
ax.axvspan(2, np.max(x), alpha=0.3, color='green')
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
plt.xlabel('$\sqrt{s}$')
plt.ylabel(r'$d\sigma/dM$')
plt.xlim(0, 4)
plt.yscale('log')
#plt.show()
plt.savefig('/Users/jaco/Documents/ML4EFT/code/output/schematic.pdf')
