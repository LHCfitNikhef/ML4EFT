import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))

# You don't need GridSpec if you are only creating one subplot
grid = plt.GridSpec(nrows=1,ncols=1,hspace=0.5, wspace=0.1)

ax = fig.add_subplot(grid[0,0])
plt.subplots_adjust(right=0.75)
df = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/thesis_pim/data/pt_background_vs_signal/event/tt_sm/events_0.pkl.gz',compression="infer")
cols_of_interest = ["pt_l_lead_reldiff", "pt_b_lead_reldiff"]
bound_cols = ["pt_l_lead_reldiff", "pt_b_lead_reldiff"]


bins=np.linspace(-0.4, 0.4, 120)
# Find the 5th and 95th percentiles for each column
bounds = {}
for col in bound_cols:
    lower_bound = df[col].quantile(0.16)
    upper_bound = df[col].quantile(0.84)
    bounds[col] = (lower_bound, upper_bound)

colors = ['C0','C1']
bound_labels = [r'$68 \% \; p_T^l \; \mathrm{bound}$',
                r'$68 \% \; p_T^b \; \mathrm{bound}$']
for i, col in enumerate(bound_cols):
    lower, upper = bounds[col]
    ax.axvline(lower, color=colors[i], linestyle='--', linewidth=0.7)
    ax.axvline(upper, color=colors[i], linestyle='--', linewidth=0.7, label=bound_labels[i])

col_names = [r'$p_T^l \; \mathrm{(leading)}$',
             r'$p_T^b \; \mathrm{(leading)}$']
for i, col in enumerate(cols_of_interest):
    hist, bins = np.histogram(df[col], bins=bins)
    ax.step(bins[:-1], hist,alpha=0.7, linewidth=0.7,linestyle='-',label=col_names[i])

    # df[col].plot.hist(ax=ax, bins=100, alpha=0.5, range=(-1, 1), linestyle='-', histtype='step', label=col_names[i])
ax.set_ylim(0,None)
ax.set_ylabel("Number of events")
ax.legend(bbox_to_anchor=(1.38, 1),
          loc='upper right')
ax.set_title(r'$\mathrm{Fractional \; change \; in} \; p_T \; \mathrm{from \; particle \; to \; hadron \; level}$')
plt.savefig('/data/theorie/pherbsch/ML4EFT/subproj/output/plots/pt_comparison.png')
