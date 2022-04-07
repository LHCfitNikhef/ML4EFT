import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import arviz as az
import pymultinest
import json
import os
import matplotlib.patches as mpatches

from matplotlib import rc

#rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 13})
#rc('text', usetex=True)

# grid scan
c_x, c_y = np.load('/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/truth/grid/mzh_y_ptz/scan_domain.npy') #chw chq3
yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis

def combine_qc(c_x, c_y, path):
    q_c = np.zeros((len(c_y), len(c_x)))
    for row, cHWB in enumerate(c_y):
        values = np.load(os.path.join(path.format(row)),
                         allow_pickle=True).flatten()
        q_c[row, :] = values
    q_c = 2 * (- q_c + np.nanmax(q_c))
    return q_c

q_c_truth_mzh_y_ptz = combine_qc(c_x, c_y, '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/truth/grid/mzh_y_ptz/q_c_truth_row_{}.npy')
q_c_truth_mzh_y = combine_qc(c_x, c_y, '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/truth/grid/mzh_y/q_c_truth_row_{}.npy')

# load posterior samples
#path_to_nn = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/nn/ns/mzh_y_ptz/posterior.json'
path_to_nn = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/nn/ns/mzh_y_ptz/r_0/posterior.json'
#path_to_binned = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/ns/binned/bin_{}/posterior.json'
#path_to_truth = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/ns/truth/posterior.json'
path_to_truth_mzh_y_ptz = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/truth/ns/mzh_y_ptz/posterior.json'
path_to_truth_mzh_y = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/truth/ns/mzh_y/posterior.json'

fig, ax = plt.subplots(figsize=(10, 10))

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
labels = [r'$1\;\rm{bin}$', r'$6\;\rm{bins}$', r'$16\;\rm{bins}$']
handles = []

with open(path_to_truth_mzh_y_ptz) as json_data:
    samples_json = json.load(json_data)
    df_truth_mzh_y_ptz = pd.DataFrame(samples_json)

with open(path_to_truth_mzh_y) as json_data:
    samples_json = json.load(json_data)
    df_truth_mzh_y = pd.DataFrame(samples_json)

def sample_loader(path):
    with open(path) as json_data:
        samples = json.load(json_data)
    df = pd.DataFrame(samples)
    return df

for i in range(27):
    df = sample_loader('/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/nn/ns/mzh_y_ptz/r_{}/posterior.json'.format(i))
    sns.kdeplot(x=df["chw"], y=df["chq3"], levels=[0.05], bw_adjust=1.2, ax=ax, color='C0')

# with open(path_to_nn) as json_data_nn:
#     samples_json_nn = json.load(json_data_nn)
#     df_nn = pd.DataFrame(samples_json_nn).sample(100)


#sns.scatterplot(x=df_nn["chw"], y=df_nn["chq3"], s=10, alpha=.5, ax=ax)

# truth

## grid
# ax.contour(xx, yy, q_c_truth_mzh_y_ptz, np.array([5.99]), origin='lower', linestyles='dashed',
#                             linewidths=2.0,
#                             colors='C0')
# handles.append(mpatches.Patch(ec='C0', fc=None, fill=False, label="Truth (3 feat, grid)", linestyle='dashed'))
#
# ax.contour(xx, yy, q_c_truth_mzh_y, np.array([5.99]), origin='lower', linestyles='dashed',
#                             linewidths=2.0,
#                             colors='C1')
#
# handles.append(mpatches.Patch(ec='C1', fc=None, fill=False, label="Truth (2 feat, grid)", linestyle='dashed'))
#
# ## ns
# sns.kdeplot(x=df_truth_mzh_y_ptz["chw"], y=df_truth_mzh_y_ptz["chq3"], levels=[0.05], bw_adjust=1.2, ax=ax, color='C2')
# handles.append(mpatches.Patch(ec='C2', fc=None, fill=False, label="Truth (3 feat, NS)"))
#
# sns.kdeplot(x=df_truth_mzh_y["chw"], y=df_truth_mzh_y["chq3"], levels=[0.05], bw_adjust=1.2, ax=ax, color='C3')
# handles.append(mpatches.Patch(ec='C3', fc=None, fill=False, label="Truth (2 feat, NS)"))
#
# # nn
# sns.kdeplot(x=df_nn["chw"], y=df_nn["chq3"], levels=[0.05], bw_adjust=1.2, ax=ax, color='C4')
# handles.append(mpatches.Patch(ec='C4', fc=None, fill=False, label="NN (3 feat, NS)"))

# for i in range(3):
#     with open(path_to_binned.format(i+1)) as json_data:
#         samples_json = json.load(json_data)
#     df_binned = pd.DataFrame(samples_json)
#     sns.kdeplot(x=df_binned["chw"], y=df_binned["chq3"], levels=[0.05], bw_adjust=1.2, ax=ax, color=colors[i])
#     handles.append(mpatches.Patch(ec=colors[i], fc=None, fill=False, label=labels[i]))

plt.legend(handles=handles)
plt.xlabel(r'$\rm{cHW}$')
plt.ylabel(r'$\rm{cHq3}$')
# plt.xlim((-0.6, 0.4))
# plt.ylim((-1.4, 2))

fig.savefig('/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/05_04/samples_rep_1_3_feat_vs_truth_grid.pdf')
