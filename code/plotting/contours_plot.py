from quad_clas.plotting.plot_contours import plot_contours
import numpy as np
from quad_clas.core.th_predictions import TheoryPred

c_x, c_y = np.load('/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/cbh_chw/nn/scan_domain.npy') #chw, chq3
c_x_binned, c_y_binned = np.load('/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/cbh_chw/binned/binning_1/scan_domain.npy')


label_legend = r'$\rm{binned}$'
label_x = r'$\rm{cHW}$'
label_y = r'$\rm{cbH}$'

bins = np.array([0, 75, 150, 250, 400, 1000])
coeffs = ['chw', 'cbhre']
theory_pred = TheoryPred(coeffs, bins, 'pt_z', '/Users/jaco/Documents/ML4EFT/training_data/zh_llbb', nreps=50)
xsec_df = theory_pred.df.sum(axis=1)

#path_to_row_nn = []
#path_to_row_nn = []
path_to_row_nn = [['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/cbh_chw/nn/q_c_nn_median_row_{}.npy', r'$\rm{NN}$']]
#path_to_row_truth = [['/Users/jaco/Documents/ML4EFT/output/contours/zh/features_mzh_y_check/truth/q_c_truth_row_{}.npy', r'$\rm{Truth}$']]
path_to_row_truth = []
# path_to_row_binned = [['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/binned/binning_1/q_c_binned_row_{}.npy', r'$5\;\rm{bins}$'],
#                        ['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/binned/binning_2/q_c_binned_row_{}.npy', r'$1\;\rm{bin}$'],
#                       ['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/binned/binning_3/q_c_binned_row_{}.npy', r'$30\;\rm{bins}$']]

#path_to_row_binned = []
path_to_row_binned = [['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/cbh_chw/binned/binning_3/q_c_binned_row_{}.npy', r'$5\;\rm{bins}$'],
                    ['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/cbh_chw/binned/binning_2/q_c_binned_row_{}.npy', r'$1\;\rm{bin}$']]
#path_to_row_binned = [['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/chw_chdd/binned/binning_1/q_c_binned_row_{}.npy', r'$5\;\rm{bins}$'],
#                      ['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/chw_chdd/binned/binning_2/q_c_binned_row_{}.npy', r'$1\;\rm{bin}$']]

fig = plot_contours(c_x, c_y, c_x_binned, c_y_binned, path_to_row_truth, path_to_row_nn, path_to_row_binned, label_legend, label_x, label_y, xsec_df, coeffs)
fig.savefig('/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/cbh_chw/nn/contour_nn_v2.pdf')