#%%
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

from quad_clas.core.truth import vh_prod, tt_prod
import quad_clas.preproc.constants as constants

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 14})
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


def plot_benchmark(df_new, df_old, c1, c2, order):

    # data_madgraph = df_old['m_tt'].iloc[1:].values
    #
    # bin_min = 2 * mt
    #
    # hist_mg_old, bins_mg = np.histogram(data_madgraph, bins=np.arange(bin_min, np.max(data_madgraph), bin_width),
    #                                 density=True)
    # hist_mg_old *= df_old['m_tt'].iloc[0]

    data_madgraph = df_new['m_tt'].iloc[1:].values


    bin_min = 2 * mt

    hist_mg_new, bins_mg_new = np.histogram(data_madgraph, bins=np.arange(0.5, np.max(data_madgraph), bin_width),
                                        density=True)
    hist_mg_new *= df_new['m_tt'].iloc[0]


    #x = np.arange(2 * mt + bin_width / 2, 1.5, bin_width)
    x = np.arange(0.5 + bin_width / 2, 2.0, bin_width)

    #cross_section = np.array([tt_prod.dsigma_dmtt(mtt, np.array([c1, c2]), order) for mtt in x])

    #cross_section_sm = np.array([tt_prod.dsigma_dmtt(mtt, np.array([0, 0]), order) for mtt in x])
    #cross_section_lin = np.array([tt_prod.dsigma_dmtt(mtt, np.array([-10, 0]), 'lin') for mtt in x])
    #cross_section = cross_section_lin
    cross_section = np.array([tt_prod.dsigma_dmtt(mtt, np.array([-10, 0]), 'lin') for mtt in x])
    #cross_section = cross_section_quad - cross_section_lin + cross_section_sm

    fig = plt.figure(figsize=(8, 5))
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])

    ax1.step(bins_mg_new[:-1], hist_mg_new, c='C0', where='post', label=r'$\rm{mg5 new}$')
    #ax1.step(bins_mg[:-1], hist_mg_old, c='C1', where='post', label=r'$\rm{mg5 old}$')

    ax1.plot(x, cross_section, '-', c='C1', label=r'$\rm{FormCalc}$')

    y_min = np.min(cross_section)
    y_max = np.max(cross_section)
    ax1.set_ylim((0.8*y_min, 1.5*y_max))

    #ax1.set_xlim((0.2, 1.5))
    ax1.set_xlim((0.45, 2.0))
    plt.yscale('log')

    plt.ylabel(r'$d\sigma/dm_{t\bar{t}}\;\mathrm{[pb\:TeV^{-1}]}$')
    plt.legend(frameon=False, loc='best')


    ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))

    #ax2.scatter(x, hist_mg[:len(x)]/cross_section, s=10)
    ax2.axhline(1, 0, 1, color='k', linestyle='dashed')

    plt.ylabel(r'$\rm{num/ana}$')

    plt.xlim((0.45, 2.0))
    plt.xlabel(r'$m_{t\bar{t}}\;\mathrm{[TeV]}$')
    return fig


fig = plot_benchmark(df, df, 0, 0, order='lin')

fig.savefig("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/lin/ctgre/tt_benchmark_lin_sm_ctgre.pdf")