#%%
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

from ml4eft.core.truth import vh_prod, tt_prod
import ml4eft.preproc.constants as constants

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 16})
rc('text', usetex=True)


mt = constants.mt
bin_width = 10 * 10 ** -3

title = r'$\rm{t\bar{t}}\;\rm{production}\;\rm{benchmark,}\;\rm{LO+}\mathcal{O}\left(\Lambda^{-4}\right)$'#title = r'$t\bar{t}\;\rm{production}\;\rm{benchmark,}\;\rm{sm}$'



# def plot_benchmark(ax1, ax2, df, c, order, min, max, text=None):
#
#     data_madgraph = df['m_tt'].iloc[1:].values
#
#     hist_mg_new, bins_mg_new = np.histogram(data_madgraph, bins=np.arange(np.min(data_madgraph), np.max(data_madgraph), bin_width),
#                                         density=True)
#     hist_mg_new *= df['m_tt'].iloc[0]
#
#     x = np.arange(np.min(data_madgraph) + bin_width / 2, np.max(data_madgraph), bin_width)
#
#     cross_section = np.array([tt_prod.dsigma_dmtt(mtt, c, order) for mtt in x])
#
#     ax1.step(bins_mg_new[:-1], hist_mg_new, c='C0', where='post', label=r'$\verb|MadGraph5_aMC@NLO|$')
#
#
#     ax1.plot(x, cross_section, '-', c='C1', label=r'$\rm{Analytical}\:(\verb|FormCalc|)$')
#     ax1.text(0.05, 0.1, text, horizontalalignment='left', verticalalignment='center', transform=ax1.transAxes)
#
#
#     y_min = np.min(cross_section[(x > min) & (x < max)])
#     y_max = np.max(cross_section[(x > min) & (x < max)])
#     ax1.set_ylim((0.8*y_min, 1.5*y_max))
#
#     #ax1.set_xlim((0.2, 1.5))
#     ax1.set_xlim((min - 0.05, max + 0.05))
#     ax1.set_yscale('log')
#
#     ax1.set_ylabel(r'$d\sigma/dm_{t\bar{t}}\;\mathrm{[pb\:TeV^{-1}]}$')
#     ax1.legend(frameon=False, loc='best')
#
#
#     #ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))
#
#
#     idx_max = np.argwhere(bins_mg_new > max).flatten()[0]
#
#     ax2.scatter(x[:idx_max], hist_mg_new[:idx_max]/cross_section[:idx_max], s=10)
#
#
#     ax2.axhline(1, 0, 1, color='k', linestyle='dashed')
#
#     ax2.set_ylabel(r'$\rm{num/ana}$')
#
#     ax2.set_xlim((min - 0.05, max + 0.05))
#     ax2.set_ylim((0.75, 1.25))
#     ax2.set_xlabel(r'$m_{t\bar{t}}\;\mathrm{[TeV]}$')
#     return ax1, ax2

def plot_benchmark(ax1, ax2, df, c, order, min, max, text=None):

    # data_madgraph = df_old['m_tt'].iloc[1:].values
    #
    # bin_min = 2 * mt
    #
    # hist_mg_old, bins_mg = np.histogram(data_madgraph, bins=np.arange(bin_min, np.max(data_madgraph), bin_width),
    #                                 density=True)
    # hist_mg_old *= df_old['m_tt'].iloc[0]

    data_madgraph = df['m_tt'].iloc[1:].values


    bin_min = 2 * mt

    hist_mg_new, bins_mg_new = np.histogram(data_madgraph, bins=np.arange(min, np.max(data_madgraph), bin_width),
                                        density=True)
    hist_mg_new *= df['m_tt'].iloc[0]


    #x = np.arange(2 * mt + bin_width / 2, 1.5, bin_width)
    x = np.arange(min + bin_width / 2, max, bin_width)

    #cross_section = np.array([tt_prod.dsigma_dmtt(mtt, np.array([c1, c2]), order) for mtt in x])

    #cross_section_sm = np.array([tt_prod.dsigma_dmtt(mtt, np.array([0, 0]), order) for mtt in x])
    #cross_section_lin = np.array([tt_prod.dsigma_dmtt(mtt, np.array([-10, 0]), 'lin') for mtt in x])
    #cross_section = cross_section_lin
    cross_section = np.array([tt_prod.dsigma_dmtt(mtt, c, order) for mtt in x])
    #cross_section = cross_section_quad - cross_section_lin + cross_section_sm

    #fig = plt.figure(figsize=(8, 5))
    #ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])

    ax1.step(bins_mg_new[:-1], hist_mg_new, c='C0', where='post', label=r'$\verb|MadGraph5_aMC@NLO|$')
    #ax1.step(bins_mg[:-1], hist_mg_old, c='C1', where='post', label=r'$\rm{mg5 old}$')

    ax1.plot(x, cross_section, '-', c='C1', label=r'$\rm{Analytical}\:(\verb|FormCalc|)$')
    ax1.text(0.05, 0.1, text, horizontalalignment='left', verticalalignment='center', transform=ax1.transAxes)


    y_min = np.min(cross_section)
    y_max = np.max(cross_section)
    ax1.set_ylim((0.8*y_min, 1.5*y_max))

    #ax1.set_xlim((0.2, 1.5))
    ax1.set_xlim((min-0.05, max))
    ax1.set_yscale('log')

    ax1.set_ylabel(r'$d\sigma/dm_{t\bar{t}}\;\mathrm{[pb\:TeV^{-1}]}$')
    ax1.legend(frameon=False, loc='best')


    #ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))

    ax2.scatter(x, hist_mg_new[:len(x)]/cross_section, s=10)
    ax2.axhline(1, 0, 1, color='k', linestyle='dashed')

    ax2.set_ylabel(r'$\rm{num/ana}$')

    ax2.set_xlim((min-0.05, max))
    ax2.set_ylim((0.75, 1.25))
    ax2.set_xlabel(r'$m_{t\bar{t}}\;\mathrm{[TeV]}$')
    return ax1, ax2



#fig = plot_benchmark(df, df, 0, 0, order='lin')

#fig.savefig("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/lin/ctgre/tt_benchmark_lin_sm_ctgre.pdf")

fig = plt.figure(figsize=(16, 10))
grid = plt.GridSpec(11, 2, wspace=0.2, hspace=0.4)

ax_0 = fig.add_subplot(grid[0:4, 0], xticklabels=[])
ax_0_sub = fig.add_subplot(grid[4, 0])

ax_1 = fig.add_subplot(grid[0: 4, 1], xticklabels=[])
ax_1_sub = fig.add_subplot(grid[4, 1])

ax_dummy = fig.add_subplot(grid[5,:])
ax_dummy.set_visible(False)

ax_2 = fig.add_subplot(grid[6:10, 0], xticklabels=[])
ax_2_sub = fig.add_subplot(grid[10, 0])

ax_3 = fig.add_subplot(grid[6:10, 1], xticklabels=[])
ax_3_sub = fig.add_subplot(grid[10, 1])

df_ctu8 = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu8/events_0.pkl.gz')
df_sm = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_sm/events_0.pkl.gz')
df_ctgre_ctgre = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctGRe_ctGRe_test/events_0.pkl.gz')
df_ctu8_ctu8 = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu8_ctu8_test2/events_1.pkl.gz')
df_ctu8_ctu8_145 = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu8_ctu8_test2/events_0.pkl.gz')

df_ctu1_ctu1 = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu1_ctu1_test4/events_0.pkl.gz')
df_ctu1_ctu1_sm = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu1_ctu1_test5/events_0.pkl.gz')
df_ctu1_ctu1_nocut = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu1_ctu1_test3/events_0.pkl.gz')
df_ctu1_ctu1_cut = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu1_ctu1_test3/events_1.pkl.gz')

df_ctu1_ctu1_old = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/tt_ctu1_ctu1/events_0.pkl.gz')
df_ctu1_ctu1_old_repro = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/mtt_145/tt_parton_ctu1_ctu1_test5/events_0.pkl.gz')


plot_benchmark(ax_0, ax_0_sub, df_ctu8_ctu8, np.array([0, 10]), 'quad', min=0.5, max=2.0, text=r'$c_{tu}^{(8)}=10\;(\rm{SM + quad})$')
plot_benchmark(ax_1, ax_1_sub, df_ctu8_ctu8_145, np.array([0, 10]), 'quad', min=1.45, max=3.0, text=r'$c_{tu}^{(8)}=10\;(\rm{SM + quad})$')

#plot_benchmark(ax_1, ax_1_sub, df_ctgre_ctgre, np.array([10, 0]), 'quad', 1.45, 3.0, r'$c_{tG}=10\;(\rm{quad})$')



# plot_benchmark(ax_1, ax_1_sub, df_sm, None, None, 1.45, 3.0, r'$(\rm{SM})$')
# plot_benchmark(ax_3, ax_3_sub, df_ctu1_ctu1_sm, np.array([0, 10]), 'quad', 1.45, 3.0, r'$c_{tu}^{(1)}=10\;(\rm{quad})$')
# plot_benchmark(ax_2, ax_2_sub, df_ctu1_ctu1, np.array([0, 10]), 'quad', 1.45, 3.0, r'$c_{tu}^{(1)}=10\;(\rm{quad})$')

#
# y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
# x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)



fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/10_10/tt_benchmark_parton_ctu8_ctu8_145.pdf')