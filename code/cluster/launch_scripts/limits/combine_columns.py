#%%
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

fig = plt.figure(figsize=(12, 10))

cHW_values, cHWB_values = np.load('/Users/jaco/Documents/ML4EFT/23_02/scan_domain.npy')

#path_to_columns = '/Users/jaco/Documents/ML4EFT/plots/2022/27_01/run_05'

def combine_qc(path):
    q_c = np.zeros((len(cHWB_values), len(cHW_values)))
    for row, cHWB in enumerate(cHWB_values):
        values = np.load(os.path.join(path.format(row)),
                         allow_pickle=True).flatten()
        q_c[row, :] = values
    q_c = 2 * (- q_c + np.nanmax(q_c))
    return q_c


yy, xx = np.meshgrid(cHWB_values, cHW_values, indexing='ij') # cHWB is y-axis
fig = plt.figure(figsize=(12, 10))

# path_truth_2 = '/Users/jaco/Documents/ML4EFT/plots/2022/27_01/meeting_28_01/truth_2/q_c_truth_row_{}.npy'
# q_c_truth_2 = combine_qc(path_truth_2)
#
# path_truth_3 = '/Users/jaco/Documents/ML4EFT/plots/2022/27_01/meeting_28_01/truth_3/q_c_truth_row_{}.npy'
# q_c_truth_3 = combine_qc(path_truth_3)

# path_nn_2 = '/Users/jaco/Documents/ML4EFT/plots/2022/27_01/meeting_28_01/nn_2/q_c_nn_median_row_{}.npy'
# q_c_nn_2 = combine_qc(path_nn_2)

# path_nn_3 = '/Users/jaco/Documents/ML4EFT/plots/2022/27_01/meeting_28_01/nn_3/q_c_nn_median_row_{}.npy'
# q_c_nn_3 = combine_qc(path_nn_3)

path_nn = '/Users/jaco/Documents/ML4EFT/23_02/q_c_nn_median_row_{}.npy'
q_c_nn = combine_qc(path_nn)



#contour_truth_2 = plt.contour(yy, xx, q_c_truth_2, np.array([5.99]),
#                              origin='lower', linestyles='dashed', linewidths=1.5, colors='C0')
# contour_nn_2 = plt.contour(yy, xx, q_c_nn_2, np.array([5.99]),
#                               origin='lower', linestyles='solid', linewidths=1.5, colors='C0')

# contour_truth_3 = plt.contour(yy, xx, q_c_truth_3, np.array([5.99]),
#                               origin='lower', linestyles='dashed', linewidths=1.5, colors='C1')

# contour_nn_3 = plt.contour(yy, xx, q_c_nn_3, np.array([5.99]),
#                               origin='lower', linestyles='solid', linewidths=1.5, colors='C1')

contour_nn = plt.contour(xx, yy, q_c_nn, np.array([5.99]), origin='lower', linestyles='dashed', linewidths=1.5, colors='C1')

labels = []
contours = []

# contour_handle, _ = contour_truth_2.legend_elements()
# contours.append(contour_handle[0])

# contour_handle, _ = contour_nn_2.legend_elements()
# contours.append(contour_handle[0])

# contour_handle, _ = contour_truth_3.legend_elements()
# contours.append(contour_handle[0])

contour_handle, _ = contour_nn.legend_elements()
contours.append(contour_handle[0])

# contour_handle, _ = contour_nn_3.legend_elements()
# contours.append(contour_handle[0])

#labels.append(r'$\rm{Truth\;2\;features}$')
# labels.append(r'$\rm{NN\;2\;features}$')
#labels.append(r'$\rm{Truth\;3\;features}$')
labels.append(r'$\rm{NN\;8\;features}$')

plt.title(r'$95\%\rm{\;CL\;intervals}$')
plt.xlabel(r'$\rm{cHW}$')
plt.ylabel(r'$\rm{cHWB}$')
plt.scatter(0, 0, marker='+', label='SM', color='k')
idx_q_c_min = np.argwhere(q_c_nn == 0)
plt.scatter(cHW_values[idx_q_c_min[0,1]], cHWB_values[idx_q_c_min[0,0]] , marker='x')

plt.legend(contours, labels, fontsize=15, frameon=False, loc='best')
plt.show()
#plt.savefig('/Users/jaco/Documents/ML4EFT/plots/2022/27_01/meeting_28_01/truth_2_vs_3.pdf')
