import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import ellipse_plotter_new as ellipse

import quad_clas.analyse.analyse as analyse

path_bin_1 = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_tt/binned_mtt_05_inf/posterior.json'
path_bin_2 = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_tt/binned_mtt_05_10_inf/posterior.json'

df_bin_1 = analyse.Analyse.posterior_loader(path_bin_1)
df_bin_2 = analyse.Analyse.posterior_loader(path_bin_2)

labels = [r'$\mathrm{Re}\:C_{tG}$', r'$C_{tu}^{(1)}$']

fig, ax = plt.subplots(figsize=(10, 10))

plotter = ellipse.EllipsePlotter()
ax, hndls = plotter.plot(ax, [df_bin_1, df_bin_2], coeff1="ctGRe", coeff2="ctu1", ax_labels=labels, samples=[True, True])

ax.legend(labels=[r"$p_T^Z\in[75, \infty)\:\mathrm{GeV}$", r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}$"], handles=hndls, loc='upper right', frameon=False, fontsize=25)

plt.tight_layout()
fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/22_07/test.pdf')

