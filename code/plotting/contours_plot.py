from quad_clas.plotting.plot_contours import plot_contours
import numpy as np

coeffs = ['cHq3', 'cHW']

c_x, c_y = np.load('/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_1/scan_domain.npy') #chw, chq3

label_legend = r'$\rm{binned}$'
label_x = r'$\rm{cHW}$'
label_y = r'$\rm{cHq3}$'

path_to_row_truth='/Users/jaco/Documents/ML4EFT/output/contours/zh/truth/q_c_truth_row_{}.npy'
path_to_row_nn='/Users/jaco/Documents/ML4EFT/output/contours/zh/nn/q_c_nn_median_row_{}.npy'

xsec_df = None
fig = plot_contours(c_x, c_y, path_to_row_truth, path_to_row_nn, label_legend, label_x, label_y, xsec_df, binned=True, path_to_row_binned='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_1/q_c_binned_row_{}.npy',
                    path_to_row_binned_2='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_2/q_c_binned_row_{}.npy',
                    path_to_row_binned_3='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_3/q_c_binned_row_{}.npy',
                    path_to_row_binned_4='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_4/q_c_binned_row_{}.npy')

fig.savefig('/Users/jaco/Documents/ML4EFT/output/contours/zh/truth/truth_v4.pdf')