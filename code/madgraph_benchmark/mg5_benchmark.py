#%%
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

from quad_clas.core.truth import vh_prod, tt_prod
import quad_clas.preproc.constants as constants

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 16})
rc('text', usetex=True)


mt = constants.mt
bin_width = 10 * 10 ** -3

title = r'$\rm{t\bar{t}}\;\rm{production}\;\rm{benchmark,}\;\rm{LO+}\mathcal{O}\left(\Lambda^{-4}\right)$'#title = r'$t\bar{t}\;\rm{production}\;\rm{benchmark,}\;\rm{sm}$'

event_path = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/lin/ctgre/events_0.pkl.gz"
event_path_lin_new = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/lin/ctgre/events_1.pkl.gz"

event_path_lin_old = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l/lin/ctgre/events_9.pkl.gz'
df_new = pd.read_pickle(event_path_lin_new)
df_old = pd.read_pickle(event_path_lin_old)
df = pd.read_pickle(event_path)

#import pdb; pdb.set_trace()


def plot_benchmark(ax1, ax2, df, c, order, text=None):

    # data_madgraph = df_old['m_tt'].iloc[1:].values
    #
    # bin_min = 2 * mt
    #
    # hist_mg_old, bins_mg = np.histogram(data_madgraph, bins=np.arange(bin_min, np.max(data_madgraph), bin_width),
    #                                 density=True)
    # hist_mg_old *= df_old['m_tt'].iloc[0]

    data_madgraph = df['m_tt'].iloc[1:].values


    bin_min = 2 * mt

    hist_mg_new, bins_mg_new = np.histogram(data_madgraph, bins=np.arange(0.5, np.max(data_madgraph), bin_width),
                                        density=True)
    hist_mg_new *= df['m_tt'].iloc[0]


    #x = np.arange(2 * mt + bin_width / 2, 1.5, bin_width)
    x = np.arange(0.5 + bin_width / 2, 2.0, bin_width)

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
    ax1.set_xlim((0.45, 2.0))
    ax1.set_yscale('log')

    ax1.set_ylabel(r'$d\sigma/dm_{t\bar{t}}\;\mathrm{[pb\:TeV^{-1}]}$')
    ax1.legend(frameon=False, loc='best')


    #ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))

    ax2.scatter(x, hist_mg_new[:len(x)]/cross_section, s=10)
    ax2.axhline(1, 0, 1, color='k', linestyle='dashed')

    ax2.set_ylabel(r'$\rm{num/ana}$')

    ax2.set_xlim((0.45, 2.0))
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

df_ctgre_lin = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/lin/ctgre/events_0.pkl.gz')
df_sm = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/sm/events_0.pkl.gz')
df_ctgre_quad = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/quad/ctgre/events_0.pkl.gz')
df_ctu1_quad = pd.read_pickle('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/quad/ctu1/events_0.pkl.gz')

plot_benchmark(ax_0, ax_0_sub, df_sm, None, None, text=r'$\rm{SM}$')
plot_benchmark(ax_1, ax_1_sub, df_ctgre_lin, np.array([-10, 0]), 'lin', r'$c_{tG}=-10\;(\rm{SM + lin})$')
plot_benchmark(ax_2, ax_2_sub, df_ctgre_quad, np.array([10, 0]), 'quad', r'$c_{tG}=10\;(\rm{SM + quad})$')
plot_benchmark(ax_3, ax_3_sub, df_ctu1_quad, np.array([0, 10]), 'quad', r'$c_{tu}^{(1)}=10\;(\rm{SM + quad})$')

#
# y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
# x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)



fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/21_07/tt_benchmark_parton.pdf')