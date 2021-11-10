import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon
from matplotlib.pyplot import cm

exp_rv = expon()
norm_rv = norm(loc=3, scale=0.1)


def pdf(x, mass, width):
    norm_rv = norm(loc=mass, scale=width)
    prob = (exp_rv.pdf(x) + 0.1 * norm_rv.pdf(x)) / 1.1
    return prob


def pdf_binned(bins, mass, width):
    cdf_exp = exp_rv.cdf(bins)
    weights_exp = cdf_exp[1:] - cdf_exp[:-1]

    norm_rv = norm(loc=mass, scale=width)
    cdf_norm = norm_rv.cdf(bins)
    weights_norm = cdf_norm[1:] - cdf_norm[:-1]
    weights_total = (weights_exp + 0.1 * weights_norm) / 1.1
    return weights_total


def chi2_function(data, theory):
    return np.sum((data-theory) ** 2 / data)



mass_truth = 3
width_truth = 0.2
mass_range = np.linspace(mass_truth-0.5, mass_truth+0.5, 200)
width_range = np.linspace(0.03, width_truth + 0.2, 200)
fig, ax = plt.subplots()
x = np.linspace(expon.ppf(0.01), expon.ppf(0.99), 100)
y = pdf(x, mass_truth, width_truth)
ax.plot(x, y, 'k-', lw=1)
plt.xlabel('$\sqrt{s}$')
plt.ylabel('Cross section [a.u.]')


plt.show()

# rejections sampling
pseudo_data_cont = []
for i in range (10000):
    delta_x = np.max(x) - np.min(x)
    delta_y = np.max(y) - np.min(y)
    u1 = delta_x * np.random.random()
    u2 = delta_y * np.random.random()
    if u2 < pdf(u1, mass_truth, width_truth):
        pseudo_data_cont.append(u1)
pseudo_data_cont = np.array(pseudo_data_cont)

# binned chi2 analysis
nrows = 1
ncols = 1
fig = plt.figure(figsize=(ncols * 8, nrows * 6))
contours = []
labels = []
x_min = []
x_max = []
y_min = []
y_max = []

xx, yy = np.meshgrid(mass_range, width_range, indexing='ij')
bins = np.array([2, 5, 8, 15, 30])
color = iter(cm.Set1(np.linspace(0, 1, len(bins))))
for i, n_bins in enumerate(bins):
    #n_bins = 10
    #ax = plt.subplot(3, 2, i + 1)
    bins = np.linspace(np.min(x), np.max(x), n_bins + 1)
    #bins = np.array([0.1, 0.5, 3.5, 4.0])

    nu_tot = len(pseudo_data_cont)

    #weights = pdf_binned(bins, 1, b_truth)
    #nu_i = nu_tot * weights
    pseudo_data, _ = np.histogram(pseudo_data_cont, bins=bins)#np.random.poisson(nu_i, len(nu_i))

    chi2_array = []

    for m in mass_range:
        for w in width_range:
            weights = pdf_binned(bins, m, w)
            nu_i = nu_tot * weights
            chi2_array.append(chi2_function(pseudo_data, nu_i))
    chi2_array = np.array(chi2_array)
    chi2_array = np.reshape(chi2_array, (len(mass_range), len(width_range)))


    #plt.contourf(yy, xx, chi2_array, np.array([np.min(chi2_array), np.min(chi2_array) + 2.3]), colors='C0',
    #             origin='lower', alpha=0.5)
    #plt.contourf(yy, xx, chi2_array, np.array([np.min(chi2_array) + 2.3, np.min(chi2_array) + 5.99]), colors='C2', origin='lower', alpha=0.5)
    #plt.contour(yy, xx, chi2_array, np.array([np.min(chi2_array) + 2.3]), colors='k',
    #            origin='lower')
    c = next(color)
    contour = plt.contour(yy, xx, chi2_array, np.array([np.min(chi2_array) + 5.99]), colors=[c],
                 origin='lower', linestyles='dashed', linewidths=1.0)
    contour_handle, _ = contour.legend_elements()
    contours.append(contour_handle[0])
    labels.append(r'$\rm{%d\;bins}$' % n_bins)



    #min_idx_0 = np.argmin(chi2_array) // chi2_array.shape[1] # axis 0
    #min_idx_1 = np.argmin(chi2_array) % chi2_array.shape[1] # axis 1
    #plt.scatter(width_range[min_idx_1], mass_range[min_idx_0], marker='x', label=r'$\chi^2_{\rm{min}}$', color='k')
    #plt.scatter(width_truth, mass_truth, marker='o', label='Truth', color='k')
    #plt.legend()


    contour_line = contour.allsegs[0][0]
    width_min, mass_min = np.min(contour_line, axis=0)
    width_max, mass_max = np.max(contour_line, axis=0)
    delta_width = width_max - width_min
    delta_mass = mass_max - mass_min


    x_min.append(max(width_min - 0.1 * delta_width, np.min(width_range)))
    x_max.append(min(width_max + 0.1 * delta_width, np.max(width_range)))

    y_min.append(max(mass_min - 0.1 * delta_mass, np.min(mass_range)))
    y_max.append(min(mass_max + 0.1 * delta_mass, np.max(mass_range)))

plt.title(r'$95\%\rm{\;CL\;intervals}$')
#     # ax.step(bins[:-1], pseudo_data, where='post')
# plt.show()

# plr analysis
#fig = plt.figure()
likelihood_scan = []
for m in mass_range:
    for w in width_range:
        likelihood = np.sum(np.log(pdf(pseudo_data_cont, m, w)))
        likelihood_scan.append(likelihood)

likelihood_scan = np.array(likelihood_scan)
likelihood_scan = np.reshape(likelihood_scan, (len(mass_range), len(width_range)))

q_c_array = 2 * (- likelihood_scan + np.max(likelihood_scan))

# mass_idx_hat = np.argmax(likelihood_scan) // likelihood_scan.shape[1] # axis 0
# width_idx_hat = np.argmax(likelihood_scan) % likelihood_scan.shape[1]
# mass_hat = mass_range[mass_idx_hat]
# width_hat = width_range[width_idx_hat]


xx, yy = np.meshgrid(mass_range, width_range, indexing='ij')
#plt.contourf(yy, xx, q_c_array, np.array([np.min(q_c_array), np.min(q_c_array) + 2.3]), colors='C0',
#             origin='lower', alpha=0.5)
#plt.contourf(yy, xx, q_c_array, np.array([np.min(q_c_array) + 2.3, np.min(q_c_array) + 5.99]), colors='C2', origin='lower', alpha=0.5)
#plt.contour(yy, xx, q_c_array, np.array([np.min(q_c_array) + 2.3]), colors='k',
#            origin='lower')

contour = plt.contour(yy, xx, q_c_array, np.array([np.min(q_c_array) + 5.99]), colors='k',
             origin='lower', linestyles='dashed')

contour_handle, _ = contour.legend_elements()
contours.append(contour_handle[0])
labels.append('Unbinned')

plt.xlabel('width')
plt.ylabel('mass')
plt.title(r'$95\%\rm{\;CL\;intervals}$')



#min_idx_0 = np.argmin(q_c_array) // q_c_array.shape[1] # axis 0
#min_idx_1 = np.argmin(q_c_array) % q_c_array.shape[1] # axis 1
#plt.scatter(width_range[min_idx_1], mass_range[min_idx_0], marker='x', label=r'$\chi^2_{\rm{min}}$', color='k')
plt.scatter(width_truth, mass_truth, marker='o', label='Truth', color='k')
plt.legend()


plt.xlim(min(x_min), max(x_max))
plt.ylim(min(y_min), max(y_max))
plt.legend(contours, labels, fontsize=15, frameon=False, loc='best')

#plt.title('Unbinned analysis')

plt.show()
#fig.savefig('/Users/jaco/Documents/ML4EFT/code/notebooks/chi_toy_model_plots/chi2_binned_unbinned_2d_v5.pdf')

