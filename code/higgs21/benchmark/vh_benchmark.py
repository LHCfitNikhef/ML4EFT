import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

sys.path.append('/Users/jaco/Documents/ML4EFT/code')
from quad_clas.core.xsec import vh_prod

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 14})
rc('text', usetex=True)

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
bin_width = 10 * 10 ** -3


title = r'$\rm{VH}\;\rm{production}\;\rm{benchmark,}\;\rm{SM}$'
event_path = "/Users/jaco/Documents/ML4EFT/data/events/vh_benchmark/events.npy"

def plot_benchmark(event_path, cHW, cHq3, title):
    data_madgraph = np.load(event_path)
    bin_min = mh + mz
    hist_mg, bins_mg = np.histogram(data_madgraph[1:, 0], bins=np.arange(bin_min, np.max(data_madgraph), bin_width),
                                    density=True)
    hist_mg *= data_madgraph[0, 0]

    x = np.arange(mz + mh + bin_width / 2, 1.0, bin_width)
    cross_section_vh = [vh_prod.dsigma_dmvh(mvh, cHW=cHW, cHq3=cHq3, lin=True, quad=False) for mvh in x]

    fig = plt.figure(figsize=(8, 5))
    ax1 = fig.add_axes([0.15, 0.35, 0.75, 0.55], xticklabels=[], xlim=(0.1, 1))

    ax1.step(bins_mg[:-1], hist_mg, c='C0', where='post', label=r'$\rm{mg5}$')
    ax1.plot(x, cross_section_vh, '-', c='C1', label=r'$\rm{FormCalc}$')
    ax1.set_ylim((10 ** -2, 10))
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


fig = plot_benchmark(event_path, 10, 0, title)
fig.savefig("/Users/jaco/Documents/ML4EFT/code/higgs21/plots/vh_linear_cHW.pdf")