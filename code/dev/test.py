# %%
from quad_clas.core.th_predictions import TheoryPred
from quad_clas.plotting.plot_contours import plot_contours, plot_contours_binned
import numpy as np

# %%

coeffs = ['chdd', 'chwb', 'cbhre', 'chw']
bins = np.array([0, 75, 150, 250, 400, 1000])

theory_pred = TheoryPred(coeffs, bins, '/Users/jaco/Documents/ML4EFT/training_data/zh_llbb', nreps=50)

xsec_df = theory_pred.df.sum(axis=1)

c_x, c_y = np.load('/Users/jaco/Documents/ML4EFT/23_02/scan_domain.npy')
path_to_row = '/Users/jaco/Documents/ML4EFT/23_02/q_c_nn_median_row_{}.npy'
label_legend = r'$\rm{NN\;8\;features}$'
label_x = r'$\rm{cHW}$'
label_y = r'$\rm{cHWB}$'

path_to_row = '/Users/jaco/Documents/ML4EFT/output/contours/nn/q_c_nn_median_row_{}.npy'
# fig = plot_contours(c_x, c_y, path_to_row, label_legend, label_x, label_y, xsec_df, binned=True, path_to_row_binned='/Users/jaco/Documents/ML4EFT/output/contours/binned/q_c_binned_row_{}.npy')

fig = plot_contours(c_x, c_y, path_to_row, label_legend, label_x, label_y, xsec_df)
fig.savefig('/Users/jaco/Documents/ML4EFT/code/dev/contour_nn_debug.pdf')

# %%
import os
import re

filename = '/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz/lin/cHq3/param_card.dat'
#match_number = re.compile('[-+]? *[0-9]+.?[0-9]*(?:[Ee] *[-+]? *[0-9]+)?')
match_number = re.compile('[-+]?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?')

with open(filename, 'r') as f:
    data = f.readlines()
    f.close()
# %%
pattern = re.compile(r'# cHq3\s+', re.IGNORECASE)
for i, line in enumerate(data):
    if len(pattern.findall(line)) > 0:
        print([x for x in pattern.findall(line)])
        matched_line = [x for x in match_number.findall(line)]
        break
param = float(matched_line[-1])
# final_list = [x for x in re.findall(pattern, line)]
#
# matches = pattern.finditer(line)
# for match in matches:
#     print(i, match)

#%%
coeffs = ['cHq3', 'cHW']
bins = np.array([0, 75, 150, 250, 400, 1000]) * 1E-3
theory_pred = TheoryPred(coeffs, bins, '/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz', nreps=30)


#%%
# zh (no decays, 2 features)

coeffs = ['cHq3', 'cHW']
bins = np.array([0, 75, 150, 250, 400, 1000])

# cHW_values = np.linspace(-1, 0.5, 100)
# cHq3_values = np.linspace(-2, 3, 100)

#theory_pred = TheoryPred(coeffs, bins, '/Users/jaco/Documents/ML4EFT/training_data/zh_llbb', nreps=50)

#xsec_df = theory_pred.df.sum(axis=1)

c_x, c_y = np.load('/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_1/scan_domain.npy') #chw, chq3
#path_to_row = '/Users/jaco/Documents/ML4EFT/23_02/q_c_nn_median_row_{}.npy'
label_legend = r'$\rm{binned}$'
label_x = r'$\rm{cHW}$'
label_y = r'$\rm{cHq3}$'
path_to_row_truth='/Users/jaco/Documents/ML4EFT/output/contours/zh/truth/q_c_truth_row_{}.npy'
path_to_row_nn='/Users/jaco/Documents/ML4EFT/output/contours/zh/nn/q_c_nn_median_row_{}.npy'


#path_to_row = '/Users/jaco/Documents/ML4EFT/output/contours/nn/q_c_nn_median_row_{}.npy'
xsec_df = None
fig = plot_contours(c_x, c_y, path_to_row_truth, path_to_row_nn, label_legend, label_x, label_y, xsec_df, binned=True, path_to_row_binned='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_1/q_c_binned_row_{}.npy',
                    path_to_row_binned_2='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_2/q_c_binned_row_{}.npy',
                    path_to_row_binned_3='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_3/q_c_binned_row_{}.npy',
                    path_to_row_binned_4='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_4/q_c_binned_row_{}.npy')
fig.savefig('/Users/jaco/Documents/ML4EFT/output/contours/zh/truth/truth_v4.pdf')

#%%
# zh (no decays, 3 features)

coeffs = ['cHq3', 'chw']
bins = np.array([0, 75, 150, 250, 400, 1000])

# cHW_values = np.linspace(-1, 0.5, 100)
# cHq3_values = np.linspace(-2, 3, 100)

#theory_pred = TheoryPred(coeffs, bins, '/Users/jaco/Documents/ML4EFT/training_data/zh_llbb', nreps=50)

#xsec_df = theory_pred.df.sum(axis=1)

c_x, c_y = np.load('/Users/jaco/Documents/ML4EFT/output/contours/zh/features_mzh_y_ptz/truth/scan_domain.npy') #chw, chq3
#path_to_row = '/Users/jaco/Documents/ML4EFT/23_02/q_c_nn_median_row_{}.npy'
label_legend = r'$\rm{binned}$'
label_x = r'$\rm{cHW}$'
label_y = r'$\rm{cHq3}$'
path_to_row_truth='/Users/jaco/Documents/ML4EFT/output/contours/zh/features_mzh_y_ptz/truth/q_c_truth_row_{}.npy'
path_to_row_truth_2='/Users/jaco/Documents/ML4EFT/output/contours/zh/features_mzh_y/truth/q_c_truth_row_{}.npy'
path_to_row_nn=None

theory_pred = TheoryPred(coeffs, bins, '/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz', nreps=30)
xsec_df = theory_pred.df.sum(axis=1)


#path_to_row = '/Users/jaco/Documents/ML4EFT/output/contours/nn/q_c_nn_median_row_{}.npy'

fig = plot_contours(c_x, c_y, path_to_row_truth, path_to_row_truth_2, path_to_row_nn, label_legend, label_x, label_y, xsec_df, binned=False, path_to_row_binned='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_1/q_c_binned_row_{}.npy',
                    path_to_row_binned_2='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_2/q_c_binned_row_{}.npy',
                    path_to_row_binned_3='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_3/q_c_binned_row_{}.npy',
                    path_to_row_binned_4='/Users/jaco/Documents/ML4EFT/output/contours/zh/binned/binning_4/q_c_binned_row_{}.npy')
fig.savefig('/Users/jaco/Documents/ML4EFT/output/contours/zh/features_mzh_y_ptz/truth/truth.pdf')
#%%

c_x, c_y = np.load('/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/nn/pt_only/scan_domain.npy') #chw, chq3

label_legend = r'$\rm{binned}$'
label_x = r'$\rm{cHW}$'
label_y = r'$\rm{cHWB}$'



bins = np.array([0, 75, 150, 250, 400, 1000])
coeffs = ['chw', 'chwb']
theory_pred = TheoryPred(coeffs, bins, 'pt_z', '/Users/jaco/Documents/ML4EFT/training_data/zh_llbb', nreps=50)
xsec_df = theory_pred.df.sum(axis=1)

path_to_row_nn = [['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/nn/pt_only/q_c_nn_median_row_{}.npy', r'$\rm{NN}$']]

path_to_row_truth = []

path_to_row_binned = [['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/binned/binning_1/q_c_binned_row_{}.npy', r'$5\;\rm{bins}$'],
                       ['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/binned/binning_2/q_c_binned_row_{}.npy', r'$1\;\rm{bin}$'],
                      ['/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/binned/binning_3/q_c_binned_row_{}.npy', r'$30\;\rm{bins}$']]

fig = plot_contours(c_x, c_y, path_to_row_truth, path_to_row_nn, path_to_row_binned, label_legend, label_x, label_y, xsec_df)
fig.savefig('/Users/jaco/Documents/ML4EFT/output/contours/zh_llbb/nn/pt_only/nn.pdf')
