from quad_clas.core.nn_analyse import likelihood_ratio_nn, likelihood_ratio_truth
import quad_clas.core.quad_classifier_cluster as quad_classifier_cluster
import torch
import matplotlib.pyplot as plt
import numpy as np

network_size = [2, 30, 30, 30, 30, 30, 1]

path_sm_data = '/data/theorie/jthoeve/event_generation/events_high_stats/sm/events_0.npy'
path_dict_sm = {0: path_sm_data}
data_sm = quad_classifier_cluster.EventDataset(c=0,
                                               n_features=2,
                                               path_dict=path_dict_sm,
                                               n_dat=1000,
                                               hypothesis=1)

sm_events = data_sm.events.numpy()

#path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/17_11/model_final_lin_cHW/']}
path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/17_11/model_final_lin_cHW/',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/17_11/model_final_lin_cHq3_v7/']}

r_nn = []

n_models = 30
for mc_run in range(n_models):
    r_nn_rep = likelihood_ratio_nn(torch.Tensor(sm_events), [0, 2], path_to_models, network_size, mc_run=mc_run, lin=True)
    r_nn_rep = r_nn_rep.numpy().flatten()
    r_nn.append(r_nn_rep)
tau_nn = np.log(r_nn)

r_truth = likelihood_ratio_truth(sm_events, [0, 2], lin=True)
tau_truth = np.log(r_truth)

# overview plot for all replicas
nrows = 6
ncols = 5
fig = plt.figure(figsize=(ncols * 4, nrows * 4))

x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)
for i in range(ncols * nrows):
    plt.subplot(nrows, ncols, i+1)
    plt.scatter(tau_truth, tau_nn[i, :], s=5, color='k')
    plt.plot(x, x, linestyle='dashed', color='grey')
    plt.xlim((np.min(x), np.max(x)))
    plt.ylim((np.min(x), np.max(x)))

plt.tight_layout()
plt.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/18_11/point_by_point_cHq3_2_all_v2.pdf')

# median
fig, ax = plt.subplots(figsize=(8, 8))
x = np.linspace(np.min(tau_truth) - 0.1, np.max(tau_truth) + 0.1, 100)
plt.scatter(tau_truth, np.median(tau_nn, axis=0), s=5, color='k')
plt.plot(x, x, linestyle='dashed', color='grey')
plt.xlabel(r'$\tau(x, c)^{\rm{truth}}$')
plt.ylabel(r'$\tau(x, c)^{\rm{NN}}$')
plt.xlim((np.min(x), np.max(x)))
plt.ylim((np.min(x), np.max(x)))
plt.tight_layout()
plt.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/18_11/point_by_point_cHq3_2_median_v2.pdf')



