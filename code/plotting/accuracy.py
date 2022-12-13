import ml4eft.analyse.analyse as analyse
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
# path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_standard_scaler/model_chw_lin_no_batch',
#                           '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_standard_scaler/model_chw_lin_no_batch']}

# path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/test_zh/model_chq3_lin_robust',
#                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/test_zh/model_chq3_lin_robust']}

path_to_models = {'lin': {
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/07/model_ctgre_lin_v9',
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/07/model_ctgre_lin_v9'}}

# fig_median, fig_pull = analyse.coeff_comp(
#     path_to_models=path_to_models,
#     network_size=[2, 100, 100, 100, 1],
#     c1=-10,
#     c2=0,
#     c_train={
#         "ctgre": -10,
#         "cuu_quad": 100.0
#     },
#     n_kin=2,
#     process='tt',
#     lin=True,
#     quad=False,
#     cross=False,
#     path_sm_data=None)
#
# #fig.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/talk_juan/chw_perf.pdf')
# fig_median.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/03_06/ctgre_lin_perf.pdf')
# fig_pull.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/03_06/ctgre_lin_perf_pull.pdf')

#%%
from matplotlib import rc
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)
# path_to_models = {'lin': ['/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/mc_run_{mc_run}',
#                          '/data/theorie/jthoeve/ML4EFT_higgs/models/2022/zh_mzh_y_robust_scaler/model_chw_lin/mc_run_{mc_run}']}

fig_accuracy_1d = analyse.accuracy_1d(c=[-5,0],
                                      path_to_models=path_to_models,
                                      c_train={"ctgre": -10,"cuu_quad": 100.0},
                                      epoch=-1,
                                      lin=True,
                                      quad=False)

fig_accuracy_1d.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/07_06/1d_f_v9.pdf')
