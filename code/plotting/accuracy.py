import quad_clas.analyse.analyse as analyse
#%%
# script that plots the ratio NN/truth coefficient functions

# individual replica
fig = analyse.coeff_comp_rep(path_to_model='/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_0',
                             network_size=[2, 30, 30, 30, 30, 30, 1],
                             c1=10,
                             c2=0,
                             quad=False,
                             cross=False)


# median and pull
fig_median, fig_pull = analyse.coeff_comp(mc_reps=30,
                                          path_to_model='/Users/jaco/Documents/ML4EFT/models/lin/cHq3/mc_run_{mc_run}',
                                          network_size=[2, 30, 30, 30, 30, 30, 1],
                                          c1=0,
                                          c2=10,
                                          lin=True,
                                          quad=False,
                                          cross=False,
                                          path_sm_data=None)

#fig.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/talk_juan/chw_perf.pdf')
fig_median.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/talk_juan/chq3_perf_median.pdf')
fig_pull.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/talk_juan/chq3_perf_pull.pdf')
#%%
path_to_models = {'lin': ['/Users/jaco/Documents/ML4EFT/models/test/model_chw_lin_log_lag/mc_run_{mc_run}',
                         '/Users/jaco/Documents/ML4EFT/models/test/model_chw_lin_log_lag/mc_run_{mc_run}']}

fig_accuracy_1d = analyse.accuracy_1d(c=[2,0],
                                      path_to_models=path_to_models,
                                      network_size=[2, 30, 30, 30, 30, 30, 1],
                                      mc_reps=1,
                                      epoch=-1,
                                      lin=True,
                                      quad=False)
fig_accuracy_1d.savefig('/Users/jaco/Documents/ML4EFT/output/accuracy/zh/1d/performance_log.pdf')
