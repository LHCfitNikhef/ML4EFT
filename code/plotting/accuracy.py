import quad_clas.analyse.analyse as analyse
#%%
# script that plots the ratio NN/truth coefficient functions

# individual replica
# fig = analyse.coeff_comp_rep(path_to_model='/Users/jaco/Documents/ML4EFT/models/lin/cHW/mc_run_0',
#                              network_size=[2, 30, 30, 30, 30, 30, 1],
#                              c1=10,
#                              c2=0,
#                              quad=False,
#                              cross=False)
#
#
# median and pull
path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_standard_scaler/model_chw_lin_no_batch',
                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_standard_scaler/model_chw_lin_no_batch']}

fig_median, fig_pull = analyse.coeff_comp(
    path_to_models=path_to_models,
    network_size=[2, 30, 30, 30, 30, 30, 1],
    c1=10,
    c2=0,
    n_kin=2,
    lin=True,
    quad=False,
    cross=False,
    path_sm_data=None)

#fig.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/talk_juan/chw_perf.pdf')
fig_median.savefig('/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/05_04/chw_perf_median_stand_no_batch.pdf')
fig_pull.savefig('/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/05_04/chw_perf_pull_stand_no_batch.pdf')
#%%
# from matplotlib import rc
# rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
# rc('text', usetex=True)
# path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/mc_run_{mc_run}',
#                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/mc_run_{mc_run}']}
#
# fig_accuracy_1d = analyse.accuracy_1d(c=[2,0],
#                                       path_to_models=path_to_models,
#                                       network_size=[2, 30, 30, 30, 30, 30, 1],
#                                       mc_reps=30,
#                                       epoch=-1,
#                                       lin=True,
#                                       quad=False)
# fig_accuracy_1d.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/2022/28_03/performance_log_v2.pdf')
