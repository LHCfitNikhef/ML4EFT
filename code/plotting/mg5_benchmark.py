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

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
mt = constants.mt
bin_width = 10 * 10 ** -3

#title = r'$\rm{t\bar{t}}\;\rm{production}\;\rm{benchmark,}\;\rm{LO+}\mathcal{O}\left(\Lambda^{0}\right)$'
title = r'$t\bar{t}\;\rm{production}\;\rm{benchmark,}\;\rm{SM}$'
event_path = "/data/theorie/jthoeve/training_data/tt/sm/events_0.pkl.gz"

df = pd.read_pickle(event_path)


def plot_benchmark(df, cHW, cHq3, title, lin=False, quad=False):

    data_madgraph = df['m_tt'].iloc[1:].values
    bin_min = 2 * mt
    hist_mg, bins_mg = np.histogram(data_madgraph, bins=np.arange(bin_min, np.max(data_madgraph), bin_width),
                                    density=True)
    hist_mg *= df['m_tt'].iloc[0]

    x = np.arange(2 * mt + bin_width / 2, 1.5, bin_width)
    cross_section_sm = np.array([tt_prod.dsigma_dmtt(mtt, 0, 0) for mtt in x])


    fig = plt.figure(figsize=(8, 5))
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])

    ax1.step(bins_mg[:-1], hist_mg, c='C0', where='post', label=r'$\rm{mg5}$')

    ax1.plot(x, cross_section_sm, '-', c='C1', label=r'$\rm{FormCalc}$')

    #ax1.text(0.05, 0.2, r'$\rm{cHq3=%d}$' % cHq3, transform=ax1.transAxes)

    y_min = np.min(cross_section_sm)
    y_max = np.max(cross_section_sm)
    ax1.set_ylim((0.8*y_min, 1.2*y_max))
    ax1.set_xlim((0.3, 1.5))
    plt.yscale('log')
    plt.title(title)
    plt.ylabel(r'$d\sigma/dm_{t\bar{t}}\;\mathrm{[pb\:TeV^{-1}]}$')
    plt.legend(frameon=False, loc='best')

    ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))

    ax2.scatter(x, cross_section_sm / hist_mg[:len(x)], s=10)
    ax2.axhline(1, 0, 1, color='k', linestyle='dashed')

    plt.ylabel(r'$\rm{num/ana}$')

    plt.xlim((0.3, 1.5))
    plt.xlabel(r'$m_{t\bar{t}}\;\mathrm{[TeV]}$')
    return fig


fig = plot_benchmark(df, 0, 0, title, lin=False, quad=True)
fig.savefig("/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/09_04/tt_benchmark.pdf")