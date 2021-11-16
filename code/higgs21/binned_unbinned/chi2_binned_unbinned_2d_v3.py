# same pseudo-dataset in all binnings
#%%
import numpy as np
import matplotlib.pyplot as plt
import quad_clas.core.xsec.vh_prod as vh_prod
from matplotlib.pyplot import cm

# load data under the sm hypothesis
events_sm = np.load('/data/theorie/jthoeve/event_generation/events/sm/events_0.npy')[1:, :]
luminosity = 2000

mz = 91.188 * 10 ** -3  # z boson mass [TeV]
mh = 0.125
bins = np.array([mz+mh, 4])
a = vh_prod.findCoeff(bins)
nu_tot = vh_prod.nu_i(a, 0, 0, luminosity, quad=True)
n_tot = np.random.poisson(nu_tot, 1)

# draw a subset of events with size following a Poisson distribution with mean nu_tot
events_idx = np.random.choice(np.arange(0, len(events_sm)), int(nu_tot), replace=False)

events_mvh = events_sm[events_idx, 0]
events_mvh_y = events_sm[events_idx, :]
#%%

def chi2_function(data, theory, error):
    return np.sum(((data-theory) / error) ** 2)

cHW_values = np.linspace(-1.5, 1.5, 50)
cHq3_values = np.linspace(-5, 7, 50)

nrows = 1
ncols = 1
fig = plt.figure(figsize=(ncols * 8, nrows * 6))

bins = np.array([2, 5, 8, 15, 20])
x_min = []
x_max = []
y_min = []
y_max = []

color = iter(cm.Set1(np.linspace(0, 1, len(bins))))
labels = []
contours = []
xx, yy = np.meshgrid(cHW_values, cHq3_values, indexing='ij')
for i, n_bins in enumerate(bins):

    if n_bins == 1:
        bins = np.array([mz+mh, 4.0])
    else:
        bins = np.linspace(mz + mh, 1.5, n_bins)
        bins = np.append(bins, 4.0)
    kappa = vh_prod.findCoeff(bins)

    n_i, _ = np.histogram(events_mvh, bins)

    log_likelihood = []
    for cHW in cHW_values:
        for cHq3 in cHq3_values:
            nu_i = vh_prod.nu_i(kappa, cHW, cHq3, luminosity, quad=True)
            log_l_i = n_i * np.log(nu_i) - nu_i

            log_l_i[np.isnan(log_l_i)] = 0
            log_likelihood.append(np.sum(log_l_i))

    log_likelihood = np.array(log_likelihood)
    log_likelihood = np.reshape(log_likelihood, (len(cHW_values), len(cHq3_values)))

    #xx, yy = np.meshgrid(cHW_values, cHq3_values, indexing='ij')

    c = next(color)
    contour = plt.contour(yy, xx, log_likelihood, np.array([np.max(log_likelihood) - 5.99]),
                          origin='lower', linestyles='dashed', linewidths=1.0, colors=[c])
    contour_handle, _ = contour.legend_elements()
    contours.append(contour_handle[0])
    labels.append(r'$\rm{%d\;bins}$' % n_bins)

    min_idx_0 = np.argmax(log_likelihood) // log_likelihood.shape[1]  # axis 0
    min_idx_1 = np.argmax(log_likelihood) % log_likelihood.shape[1]  # axis 1

    plt.scatter(cHq3_values[min_idx_1], cHW_values[min_idx_0], marker='x', label=r'$\chi^2_{\rm{min}}$', color=[c])

    contour_line = contour.allsegs[0][0]
    cHq3_min, cHW_min = np.min(contour_line, axis=0)
    cHq3_max, cHW_max = np.max(contour_line, axis=0)

    delta_cHq3 = cHq3_max - cHq3_min
    delta_cHW = cHW_max - cHW_min

    x_min.append(max(cHq3_min - 0.1 * delta_cHq3, np.min(cHq3_values)))
    x_max.append(min(cHq3_max + 0.1 * delta_cHq3, np.max(cHq3_values)))

    y_min.append(max(cHW_min - 0.1 * delta_cHW, np.min(cHW_values)))
    y_max.append(min(cHW_max + 0.1 * delta_cHW, np.max(cHW_values)))


likelihood_scan = []
a = vh_prod.findCoeff(np.array([mz + mh, 4]))

for cHW in cHW_values:
    print(cHW)
    for cHq3 in cHq3_values:
        nu = vh_prod.nu_i(a, cHW, cHq3, luminosity, quad=True)
        dsigma_dx = np.array([vh_prod.dsigma_dmvh_dy(y, mvh, cHW, cHq3, lin=False, quad=True) for (mvh, y) in events_mvh_y])
        #likelihood = -nu + events_mvh_y.shape[0] * np.sum(np.log(dsigma_dx))
        likelihood = -nu + np.sum(np.log(dsigma_dx))
        if np.isnan(np.array(likelihood)):
            import pdb
            pdb.set_trace()
        likelihood_scan.append(likelihood)

likelihood_scan = np.array(likelihood_scan)
likelihood_scan = np.reshape(likelihood_scan, (len(cHW_values), len(cHq3_values)))

#
# xx_coarse, yy_coarse = np.meshgrid(cHW_values, cHq3_values, indexing='ij')
# eft_points = np.array([xx_coarse.flatten(), yy_coarse.flatten()]).T
# a = [[1, c1, c2, c1 ** 2, c2 ** 2, c1 * c2] for (c1, c2) in eft_points]
# coeff, _, _, _ = np.linalg.lstsq(a, likelihood_scan.flatten())
#
# def likelihood_int(coeff, c1, c2):
#     a = np.array([np.ones(c1.shape), c1, c2, c1 ** 2, c2 ** 2, c1 * c2])
#     return np.einsum('ijk,i', a, coeff)
#
# cHW_values_int = np.linspace(-2, 2, 200)
# cHq3_values_int = np.linspace(-3, 3, 200)
# xx, yy = np.meshgrid(cHW_values_int, cHq3_values_int, indexing='ij')
#
#
# likelihood_scan_int = likelihood_int(coeff, xx, yy)

q_c_array = 2 * (- likelihood_scan + np.max(likelihood_scan))
#
# plt.contourf(yy, xx, q_c_array, np.array([np.min(q_c_array), np.min(q_c_array) + 2.3]), colors='C0',
#              origin='lower', alpha=0.5)
# plt.contourf(yy, xx, q_c_array, np.array([np.min(q_c_array) + 2.3, np.min(q_c_array) + 5.99]), colors='C2', origin='lower', alpha=0.5)
# plt.contour(yy, xx, q_c_array, np.array([np.min(q_c_array) + 2.3]), colors='k',
#             origin='lower')
# plt.contour(yy, xx, q_c_array, np.array([np.min(q_c_array) + 2.3]), colors='k',
#             origin='lower')



contour = plt.contour(yy, xx, q_c_array, np.array([5.99]),
                          origin='lower', linestyles='dashed', linewidths=1.0, colors='k')
contour_handle, _ = contour.legend_elements()
contours.append(contour_handle[0])
labels.append(r'$\rm{Unbinned}$')
# contour = plt.contour(yy_coarse, xx_coarse, likelihood_scan, 5, colors='red',
#              origin='lower', linestyles='dotted')
plt.title(r'$95\%\rm{\;CL\;intervals}$')
plt.xlabel('cHq3')
plt.ylabel('cHW')
plt.scatter(0, 0, marker='+', label='SM', color='k')
# plt.xlim(min(x_min), max(x_max))
# plt.ylim(min(y_min), max(y_max))
plt.legend(contours, labels, fontsize=15, frameon=False, loc='best')


#
# min_idx_0 = np.argmin(q_c_array) // q_c_array.shape[1] # axis 0
# min_idx_1 = np.argmin(q_c_array) % q_c_array.shape[1] # axis 1
# plt.scatter(cHq3_values_int[min_idx_1], cHW_values_int[min_idx_0], marker='x', label=r'$\chi^2_{\rm{min}}$', color='k')
# plt.scatter(0, 0, marker='o', label='SM', color='k')
# plt.legend()


fig.savefig('/data/theorie/jthoeve/ML4EFT_higgs/code/binned_unbinned/binned_unbinned_v4.pdf')