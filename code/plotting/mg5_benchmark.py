#%%
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

from ml4eft.core.truth import vh_prod, tt_prod
import ml4eft.preproc.constants as constants

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 16})
rc('text', usetex=True)


mt = constants.mt
bin_width = 15 * 10 ** -3

title = r'$\rm{t\bar{t}}\;\rm{production}\;\rm{benchmark,}\;\rm{LO+}\mathcal{O}\left(\Lambda^{-4}\right)$'#title = r'$t\bar{t}\;\rm{production}\;\rm{benchmark,}\;\rm{sm}$'


def plot_benchmark(ax1, ax2, df, c, order, min, max, text=None):

    data_madgraph = df['m_tt'].iloc[1:].values

    hist_mg_new, bins_mg_new = np.histogram(data_madgraph, bins=np.arange(min, np.max(data_madgraph), bin_width),
                                        density=True)
    hist_mg_new *= df['m_tt'].iloc[0]

    x = np.arange(min + bin_width / 2, max, bin_width)

    cross_section = np.array([tt_prod.dsigma_dmtt(mtt, c, order) for mtt in x])

    ax1.step(bins_mg_new[:-1], hist_mg_new, c='C0', where='post', label=r'$\verb|MadGraph5_aMC@NLO|$')

    ax1.plot(x, cross_section, '-', c='C1', label=r'$\rm{Analytical}\:(\verb|FormCalc|)$')
    ax1.text(0.05, 0.1, text, horizontalalignment='left', verticalalignment='center', transform=ax1.transAxes)

    y_min = np.min(cross_section)
    y_max = np.max(cross_section)
    ax1.set_ylim((0.8*y_min, 1.5*y_max))
    ax1.set_xlim((min-0.05, max))

    ax1.tick_params(
        axis='y',  # changes apply to the y-axis
        which='minor',
        labelleft=False  # both major and minor ticks are affected
    )
    ax1.set_yscale('log')

    ax1.legend(frameon=False, loc='best')

    ax2.scatter(x, hist_mg_new[:len(x)]/cross_section, s=10)
    ax2.axhline(1, 0, 1, color='k', linestyle='dashed')

    ax2.set_xlim((min-0.05, max))
    ax2.set_ylim((0.75, 1.25))

    return ax1, ax2

fig = plt.figure(figsize=(16, 10))
grid = plt.GridSpec(17, 2, wspace=0.08, hspace=0.5)

ax_0 = fig.add_subplot(grid[0:6, 0], xticklabels=[])
ax_0_sub = fig.add_subplot(grid[6:8, 0], xticklabels=[])

ax_1 = fig.add_subplot(grid[0: 6, 1], xticklabels=[])
ax_1_sub = fig.add_subplot(grid[6:8, 1], xticklabels=[], yticklabels=[])

ax_dummy = fig.add_subplot(grid[9,:])
ax_dummy.set_visible(False)

ax_2 = fig.add_subplot(grid[9:15, 0], xticklabels=[])
ax_2_sub = fig.add_subplot(grid[15:17, 0])

ax_3 = fig.add_subplot(grid[9:15, 1], xticklabels=[])
ax_3_sub = fig.add_subplot(grid[15:17, 1], yticklabels=[])

ax_0_sub.set(xlabel=None)
ax_1_sub.set(xlabel=None)
ax_2_sub.set(xlabel=r'$m_{t\bar{t}}\;\mathrm{[TeV]}$')
ax_3_sub.set(xlabel=r'$m_{t\bar{t}}\;\mathrm{[TeV]}$')
ax_0.set(ylabel=r'$d\sigma/dm_{t\bar{t}}\;\mathrm{[pb\:TeV^{-1}]}$')
ax_2.set(ylabel=r'$d\sigma/dm_{t\bar{t}}\;\mathrm{[pb\:TeV^{-1}]}$')
ax_0_sub.set(ylabel=r'$\rm{num/ana}$')
ax_2_sub.set(ylabel=r'$\rm{num/ana}$')

df_sm = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_sm/events_0.pkl.gz')
df_ctu8 = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu8/events_0.pkl.gz')
df_ctu8_ctu8 = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu8_ctu8/events_0.pkl.gz')
df_ctgre = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctGRe/events_0.pkl.gz')
df_ctgre_ctgre = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctGRe_ctGRe/events_0.pkl.gz')

plot_benchmark(ax_0, ax_0_sub, df_ctu8, np.array([0, 10]), 'lin', min=1.45, max=3.0, text=r'$c_{tu}^{(8)}=10\;(\rm{SM + lin})$')
plot_benchmark(ax_1, ax_1_sub, df_ctu8_ctu8, np.array([0, 10]), 'quad', min=1.45, max=3.0, text=r'$c_{tu}^{(8)}=10\;(\rm{SM + quad})$')
plot_benchmark(ax_2, ax_2_sub, df_ctgre, np.array([-10, 0]), 'lin', min=1.45, max=3.0, text=r'$c_{tG}=-10\;(\rm{SM + lin})$')
plot_benchmark(ax_3, ax_3_sub, df_ctgre_ctgre, np.array([-10, 0]), 'quad', min=1.45, max=3.0, text=r'$c_{tG}=10\;(\rm{SM + quad})$')

fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/14_10/tt_benchmark_parton.pdf')