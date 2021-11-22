import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.truth.vh_prod as vh_prod

events_sm = np.load('/Users/jaco/Documents/ML4EFT/data/events/sm/events_0.npy')
pseudo_data_full = events_sm[1:, 0]

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
luminosity = 30000
#bins = np.array([mz+mh, 4])
#bins = np.append(bins, 4.0)
#a = vh_prod.findCoeff(bins)
#nu_i_sm = vh_prod.nu_i(a, 0, 0, luminosity, quad=True)
#nu_tot = np.sum(nu_i_sm)

#n_tot = np.random.poisson(nu_tot, 1)
#pseudo_data = np.random.choice(pseudo_data_full, n_tot, replace=False)

def chi2_function(data, theory):
    return np.sum((data-theory) ** 2 / data)



cHW_values = np.linspace(-1, 1, 1000)

nrows = 3
ncols = 2
fig = plt.figure(figsize=(ncols * 8, nrows * 6))
for i, n_bins in enumerate([2, 5, 10, 15, 20]):
    ax = plt.subplot(nrows, ncols, i + 1)
    if n_bins == 1:
        bins = np.array([mz+mh, 4.0])
    else:
        bins = np.linspace(mz + mh, 1.5, n_bins)
        bins = np.append(bins, 4.0)
    a = vh_prod.findCoeff(bins)
    nu_i_sm = vh_prod.nu_i(a, 0, 0, luminosity, quad=True)
    #pseudo_data_binned, _ = np.histogram(pseudo_data, bins=bins)
    pseudo_data_binned = np.random.poisson(nu_i_sm, len(nu_i_sm)) # TODO: comparing apples and oranges: don't use a different dataset for per binning
    chi2_values = []
    for cHW in cHW_values:
        nu_i = vh_prod.nu_i(a, cHW, -4.76 * cHW, luminosity, quad=True)
        chi2_values.append(chi2_function(pseudo_data_binned, nu_i))
    chi2_values = np.array(chi2_values)

    #fig, ax = plt.subplots(figsize=(10,6))
    plt.plot(cHW_values, chi2_values)

    plt.ylabel(r'$\chi^2 \times n_{dat}$')
    plt.xlabel('$cHW$')

    chi2_min = np.min(chi2_values)
    chi2_low_up_idx = np.argwhere(chi2_values < chi2_min + 4)

    c_min_idx = np.argmin(chi2_values)
    c_min = cHW_values[c_min_idx]
    c_low = cHW_values[chi2_low_up_idx[0]]
    c_up = cHW_values[chi2_low_up_idx[-1]]

    ax.axhline(chi2_min + 4, linestyle='dashed', color='C1')
    ax.axvline(0, 0, 1, linestyle='dashed', color='k')

    ax.text(0.9, 0.9, r'$c\;=\;%.2f ^{+%.2f}_{-%.2f}$' % (c_min, c_up - c_min, c_min - c_low),
            transform=ax.transAxes,
            horizontalalignment='right',
            verticalalignment='top',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))

    plt.xlim(cHW_values[chi2_low_up_idx[0]]-0.2, cHW_values[chi2_low_up_idx[-1]]+0.2)
    plt.ylim(chi2_min-1, chi2_min + 10)
    plt.title(r'$\chi^2_{\rm{binned}}\;(%d\;\rm{bins})$'%n_bins)
    plt.grid()

plt.show()