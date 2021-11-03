# same pseudo-dataset in all binnings

import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.xsec.vh_prod as vh_prod

events_sm = np.load('/Users/jaco/Documents/ML4EFT/data/events/sm/events_0.npy')
pseudo_data_full = events_sm[1:, 0]
luminosity = 60000

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
bins = np.array([mz+mh, 4])
a = vh_prod.findCoeff(bins)
nu_tot = vh_prod.nu_i(a, 0, 0, luminosity, quad=True)
n_tot = np.random.poisson(nu_tot, 1)
pseudo_data = np.random.choice(pseudo_data_full, int(nu_tot), replace=False)

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125



def chi2_function(data, theory):
    return np.sum((data-theory) ** 2 / data)



cHW_values = np.linspace(-0.3, 0.3, 200)
cHq3_values = np.linspace(-1, 1.2, 200)
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

    n_i, _ = np.histogram(pseudo_data, bins)
    #nu_i_sm = vh_prod.nu_i(a, 0, 0, luminosity, quad=True)

    #pseudo_data_binned = np.random.poisson(nu_i_sm, len(nu_i_sm))
    chi2_values = []
    for cHW in cHW_values:
        for cHq3 in cHq3_values:
            nu_i = vh_prod.nu_i(a, cHW, cHq3, luminosity, quad=True)
            chi2_values.append(chi2_function(n_i, nu_i))
    chi2_values = np.array(chi2_values)
    chi2_values = np.reshape(chi2_values, (len(cHW_values), len(cHq3_values)))

    xx, yy = np.meshgrid(cHW_values, cHq3_values, indexing='ij')
    plt.contourf(yy, xx, chi2_values, np.array([np.min(chi2_values), np.min(chi2_values) + 2.3]), colors='C0',
                 origin='lower', alpha=0.5)
    plt.contourf(yy, xx, chi2_values, np.array([np.min(chi2_values) + 2.3, np.min(chi2_values) + 5.99]), colors='C2',
                 origin='lower', alpha=0.5)
    plt.contour(yy, xx, chi2_values, np.array([np.min(chi2_values) + 2.3]), colors='k',
                origin='lower')

    contour = plt.contour(yy, xx, chi2_values, np.array([np.min(chi2_values) + 5.99]), colors='k',
                          origin='lower')

    plt.xlabel('cHq3')
    plt.ylabel('cHW')

    min_idx_0 = np.argmin(chi2_values) // chi2_values.shape[1]  # axis 0
    min_idx_1 = np.argmin(chi2_values) % chi2_values.shape[1]  # axis 1
    plt.scatter(cHq3_values[min_idx_1], cHW_values[min_idx_0], marker='x', label=r'$\chi^2_{\rm{min}}$', color='k')
    plt.scatter(0, 0, marker='o', label='SM', color='k')
    plt.legend()

    contour_line = contour.allsegs[0][0]
    cHq3_min, cHW_min = np.min(contour_line, axis=0)
    cHq3_max, cHW_max = np.max(contour_line, axis=0)
    delta_cHq3 = cHq3_max - cHq3_min
    delta_cHW = cHW_max - cHW_min
    x_min = cHq3_min - 0.1 * delta_cHq3
    x_max = cHq3_max + 0.1 * delta_cHq3

    plt.xlim(max(x_min, np.min(cHq3_values)), min(x_max, np.max(cHq3_values)))
    plt.ylim(max(cHW_min - 0.1 * delta_cHW, np.min(cHW_values)), min(cHW_max + 0.1 * delta_cHW, np.max(cHW_values)))

    plt.title(r'$\chi^2_{\rm{binned}}\;(%d\;\rm{bins})$' % n_bins)


plt.show()