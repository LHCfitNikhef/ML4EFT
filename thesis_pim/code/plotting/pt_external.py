import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# external pt 
fig, ax = plt.subplots()
dfex = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/thesis_pim/data/pt_comparison/event/tt_sm/events_0.pkl.gz',compression="infer")
# dfex_fsr = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/consistency_checks/external_pt/FSR/event/tt_sm/events_0.pkl.gz',compression="infer")
df2 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/output/Final/FSR_ISR_MPI/event/tt_sm/events_0.pkl.gz',compression="infer")
cols_of_interest2 = ["pt_l_leading", "pt_l_trailing", "pt_b_leading", "pt_b_trailing"]
col_names = [r'$p_T^l \; \mathrm{(leading)}$',
             r'$p_T^l \; \mathrm{(trailing)}$',
             r'$p_T^b \; \mathrm{(leading)}$',
             r'$p_T^b \; \mathrm{(trailing)}$']
max_value = df2[cols_of_interest2].max().max()
# dfex_fsr["external_pt"].plot.hist(ax=ax, bins=100, alpha=0.5, range=(0, max_value), logy=True, histtype='step', label="FSR background")
dfex["external_pt"].plot.hist(ax=ax, bins=100, alpha=0.5, range=(0, max_value), logy=True, histtype='step', label=r"$p_T \; \mathrm{background}$")
for i, col in enumerate(cols_of_interest2):
    df2[col].plot.hist(ax=ax, bins=100, alpha=0.5, range=(0, max_value), logy=True, histtype='step', label=col_names[i])
plt.title(r'$\mathrm{Background \; vs \; Signal} \; p_T$')
plt.xlabel(r'$p_T \; \mathrm{GeV}$')
plt.ylabel('Number of events')
plt.legend()
plt.savefig('/data/theorie/pherbsch/ML4EFT/subproj/output/plots/background_pt.png')





