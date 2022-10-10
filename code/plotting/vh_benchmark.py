#%%
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

sys.path.append('/Users/jaco/Documents/ML4EFT/code')
from ml4eft.core.truth import vh_prod

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 14})
rc('text', usetex=True)

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
bin_width = 10 * 10 ** -3

title = r'$\rm{VH}\;\rm{production}\;\rm{benchmark,}\;\rm{LO+}\mathcal{O}\left(\Lambda^{-4}\right)$'
event_path = "/Users/jaco/Documents/ML4EFT/data/events_high_stats/quad_only/cHq3/events_0.npy"



def plot_benchmark(event_path, cHW, cHq3, title, lin=False, quad=False):
    data_madgraph = np.load(event_path)
    bin_min = mh + mz
    hist_mg, bins_mg = np.histogram(data_madgraph[1:, 0], bins=np.arange(bin_min, np.max(data_madgraph), bin_width),
                                    density=True)
    hist_mg *= data_madgraph[0, 0]

    x = np.arange(mz + mh + bin_width / 2, 1.0, bin_width)
    cross_section_vh_quad = np.array([vh_prod.dsigma_dmvh(mvh, cHW=cHW, cHq3=cHq3, lin=False, quad=True) for mvh in x])
    cross_section_vh_lin = np.array([vh_prod.dsigma_dmvh(mvh, cHW=cHW, cHq3=cHq3, lin=True, quad=False) for mvh in x])

    cross_section_vh_quad_only = cross_section_vh_quad - cross_section_vh_lin
    cross_section_vh_sm = np.array([vh_prod.dsigma_dmvh(mvh, cHW=0, cHq3=0, lin=lin, quad=quad) for mvh in x])
    cross_section_vh = cross_section_vh_quad_only + cross_section_vh_sm
    #cross_section_vh_quad_cHq3 = [vh_prod.dsigma_dmvh(mvh, cHW=0, cHq3=cHq3, lin=False, quad=True) for mvh in x]
    #cross_section_vh_quad_cHW = [vh_prod.dsigma_dmvh(mvh, cHW=cHW, cHq3=0, lin=False, quad=True) for mvh in x]
    fig = plt.figure(figsize=(8, 5))
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[])

    ax1.step(bins_mg[:-1], hist_mg, c='C0', where='post', label=r'$\rm{mg5}$')
    #ax1.plot(x, cross_section_vh_quad, '-', c='C1', label=r'$\rm{FormCalc}$')
    ax1.plot(x, cross_section_vh, '-', c='C1', label=r'$\rm{FormCalc}\;\rm{quad\;+sm\;only}$')
    #ax1.plot(x, cross_section_vh_sm, '-', c='C2', label=r'$\rm{FormCalc}\;\rm{sm}$')
    #ax1.plot(x, np.array(cross_section_vh_quad_cHq3) + np.array(cross_section_vh_quad_cHW), '-', c='C2', label=r'$\rm{FormCalc}\;\rm{quad}$' )

    #ax1.text(0.05, 0.1,r'$\rm{cHW=%d}$'%cHW, transform=ax1.transAxes)
    ax1.text(0.05, 0.2, r'$\rm{cHq3=%d}$' % cHq3, transform=ax1.transAxes)

    y_min = np.min(cross_section_vh)
    y_max = np.max(cross_section_vh)
    ax1.set_ylim((0.8*y_min, 1.2*y_max))
    ax1.set_xlim((0.2, 1))
    plt.yscale('log')
    plt.title(title)
    plt.ylabel(r'$d\sigma/dm_{HZ}\;\mathrm{[pb\:TeV^{-1}]}$')
    plt.legend(frameon=False, loc='best')

    ax2 = fig.add_axes([0.15, 0.14, 0.75, 0.18], ylim=(0.9, 1.1))
    ax2.scatter(x, cross_section_vh / hist_mg[:len(x)], s=10)
    ax2.hlines(1, 0.1, 1, colors='k', linestyles='dashed')

    plt.ylabel(r'$\rm{num/ana}$')

    plt.xlim((0.2, 1))
    plt.xlabel(r'$m_{HZ}\;\mathrm{[TeV]}$')
    return fig


fig = plot_benchmark(event_path, 0, 10, title, lin=False, quad=True)
fig.savefig("/Users/jaco/Documents/ML4EFT/plots/02_12/vh_benchmark.pdf")