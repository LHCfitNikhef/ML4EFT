import bounds_2 as bnds
import expected_events as exp_nevents
import numpy as np
import matplotlib.pyplot as plt

# n = 100000
# event_data_1 = bnds.load_data('/data/theorie/jthoeve/ML4EFT/quad_clas/eft_06_v3.lhe', n=n, s=n)
# event_data_2 = bnds.load_data('/data/theorie/jthoeve/ML4EFT/quad_clas/eft_06_v2.lhe', n=n, s=n)
# bins = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 4000])
# #bins = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 4000])
# #bins = np.array([300, 400, 500, 600, 4000])
# n_i_1, _ = np.histogram(event_data_1, bins=bins)
# n_i_2, _ = np.histogram(event_data_2, bins=bins)
#
# print(n_i_1/n)
# print(n_i_2/n)
# print(n_i_1/n_i_2)
#
# # path_output = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_1'
# # n_exp = exp.expected_events_binned(np.array([0, 0.6]), bins, path_output).astype(int)
# #
# # print(n_exp)

n = 10000 # number of events to be loaded
luminosity = 6
nu_i_list = []
for i in range(1, 51):

    if i < 10:
        path_eft = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_8/bin/process_8/Events/run_0{}/unweighted_events.lhe'.format(i)
    else:
        path_eft = '/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_8/bin/process_8/Events/run_{}/unweighted_events.lhe'.format(i)

    event_data = bnds.load_data(path_eft, n, s=n)
    xsec, _ = exp_nevents.load_datapoint(path_eft)
    nu = luminosity * xsec

    bins = np.array([300, 400, 500, 600, 4000])
    n_i, _ = np.histogram(event_data, bins=bins)

    nu_i = (n_i / n) * nu
    nu_i_list.append(nu_i)

nu_i_list = np.array(nu_i_list)

# plt.figure(figsize=(10, 6))
#
# ax = plt.subplot(111)
# ax.hist(nu_i_list[:,0])
# plt.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/nu_i_dist.pdf')

c = np.array([0, -0.50])
path_output='/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_2_v3'
nu_i_fit = exp_nevents.expected_events_binned(c, bins, path_output).astype(int)


nrows = 2
ncols = 2
fig = plt.figure(figsize=(ncols * 10, nrows * 6))
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(0, nrows*ncols):
    ax = fig.add_subplot(nrows, ncols, i+1)
    ax.hist(nu_i_list[:, i], density=True, color='C0')
    nu_i_mean = np.mean(nu_i_list[:,i])
    nu_i_unc = np.std(nu_i_list[:,i])
    print(nu_i_list[:,i].size)
    nu_i_mean_unc = nu_i_unc/np.sqrt(nu_i_list[:,i].size)
    ax.axvline(nu_i_fit[i], 0, 1, color='C1', linestyle='dashed', label=r'$\rm{true}$')
    ax.axvline(nu_i_mean, 0, 1, color='C2', linestyle='dashed', label=r'$\rm{estimated}$')
    nu_i_fit_unc = np.sqrt(nu_i_fit[i])
    res_i = (nu_i_mean - nu_i_fit[i])/nu_i_mean_unc

    # ax.text(0.10,0.82,r'$\sigma_{\nu_i} = %.2f$'%nu_i_fit_unc,fontsize=20,transform=ax.transAxes)
    ax.text(0.05, 0.9, r'$\bar{\nu_i} = %.2f$' % nu_i_mean, fontsize=20, transform=ax.transAxes)
    ax.text(0.05, 0.82, r'$\nu_i = %.2f$' % nu_i_fit[i], fontsize=20, transform=ax.transAxes)
    ax.text(0.05, 0.74, r'$\hat{\sigma}_{\nu_i} = %.2f$' % nu_i_unc, fontsize=20, transform=ax.transAxes)
    ax.text(0.05, 0.66, r'$\rm{r_i} = %.2f$' % res_i, fontsize=20, transform=ax.transAxes)
    ax.set_xlabel(r'$\rm{\nu_i}$')
    ax.set_title(r'$\rm{bin\;}$' + r'${}$'.format(i+1))
    plt.legend()
    fig.tight_layout()
fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/nu_i_dist.pdf')
