import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
#import arviz as az
import pymultinest
import json
import os
import matplotlib.patches as mpatches
from sklearn.decomposition import PCA

from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 15})
rc('text', usetex=True)

# load posterior samples
path_to_nn = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/nn/mzh_y/posterior.json'
path_to_truth = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/truth/mzh_y/posterior.json'

fig, ax = plt.subplots(figsize=(10, 10))

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
labels = [r'$1\;\rm{bin}$', r'$6\;\rm{bins}$', r'$16\;\rm{bins}$']
handles = []

def sample_loader(path):
    with open(path) as json_data:
        samples = json.load(json_data)
    df = pd.DataFrame(samples)
    return df

# dfs = []
# for i in range(27):
#     df = sample_loader('/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/nn/ns/mzh_y_ptz/r_{}/posterior.json'.format(i))
#     sns.kdeplot(x=df["chw"], y=df["chq3"], levels=[0.05], bw_adjust=1.2, ax=ax, color='C0', linewidths=0.1)
#     dfs.append(df)
# post_samples_all = pd.concat(dfs, ignore_index=True, axis=0)

# pca = PCA(n_components=2)
# samples_pca = pca.fit(post_samples_all)
#
# def pca_limits(pca, df):
#     samples_pca = pca.transform(df)
#     low = np.percentile(samples_pca, 2.5, axis=0)
#     high = np.percentile(samples_pca, 97.5, axis=0)
#     return low, high
#
# low = np.array([pca_limits(pca, df)[0] for df in dfs])
# high = np.array([pca_limits(pca, df)[1] for df in dfs])
#
# low_envelope = np.percentile(low, 16, axis=0)
# high_envelope = np.percentile(high, 84, axis=0)
#
# envelope_high_coord_pca = np.diag(high_envelope)
# envelope_low_coord_pca = np.diag(low_envelope)
#
# envelope_high_coord = pca.inverse_transform(envelope_high_coord_pca)
# envelope_low_coord = pca.inverse_transform(envelope_low_coord_pca)
#
# # samples_1 = pca.transform(dfs[0])
# pc = pca.components_.T

# g = sns.JointGrid()
# sns.scatterplot(x=samples_1[:,0], y=samples_1[:,1], s=10, alpha=.5, ax=g.ax_joint)
# #sns.kdeplot(x=samples_pca[:,0], y=samples_pca[:,0], levels=[0.05], bw_adjust=1.2, ax=g.ax_joint, color='red')
# g.ax_joint.axvline(np.percentile(samples_1[:,0], 84))
# g.ax_joint.axvline(np.percentile(samples_1[:,0], 16))
# g.ax_joint.axhline(np.percentile(samples_1[:,1], 84))
# g.ax_joint.axhline(np.percentile(samples_1[:,1], 16))
# sns.histplot(x=samples_1[:,0], ax=g.ax_marg_x, alpha=.5, kde=False)
# sns.histplot(y=samples_1[:,1], ax=g.ax_marg_y, alpha=.5, kde=False)

#g.savefig('/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/05_04/samples_rep_test_pca_marg.pdf')
#import pdb; pdb.set_trace()

with open(path_to_nn) as json_data_nn:
    df_nn = sample_loader(path_to_nn)

with open(path_to_truth) as json_data_truth:
    df_truth = sample_loader(path_to_truth)

df_truth['mode'] = "truth"
df_nn['mode'] = "nn"

df = pd.concat([df_truth, df_nn], ignore_index=True)




#sns.scatterplot(x=df_nn["chw"], y=df_nn["chq3"], s=10, alpha=.5, ax=ax)

# truth

#fig, ax = plt.subplots(figsize=(10,10))

# g = sns.JointGrid(data=df, x="ctgre", y="cut", hue="mode", size=12)
# g.plot_joint(sns.kdeplot, s=10, alpha=.5, levels=[0.05])
# g.plot_joint(sns.scatterplot, s=10, alpha=.5)
#
# ax = plt.gca()
# ax.legend(["test1", "test2"])
#
# g.plot_marginals(sns.histplot, kde=True, alpha=.3)
# g.set_axis_labels(r'$\mathrm{Re}\:C_{tG}$', r'$C_{tu}^{(1)}$')


handles=[]
g = sns.JointGrid(height=6)

sns.scatterplot(x=df_nn["ctgre"], y=df_nn["cut"], s=10, alpha=.5, ax=g.ax_joint)
sns.scatterplot(x=df_truth["ctgre"], y=df_truth["cut"], s=10, alpha=.5, ax=g.ax_joint)
sns.kdeplot(x=df_nn["ctgre"], y=df_nn["cut"], levels=[0.05], bw_adjust=1.2, ax=g.ax_joint)
sns.kdeplot(x=df_truth["ctgre"], y=df_truth["cut"], levels=[0.05], bw_adjust=1.2, ax=g.ax_joint)

handles.append(mpatches.Patch(ec='C0', fc=None, fill=False, label=r"$\mathrm{NN}$"))
handles.append(mpatches.Patch(ec='C1', fc=None, fill=False, label=r"$\mathrm{Truth}$"))

sns.histplot(x=df_nn["ctgre"], ax=g.ax_marg_x, alpha=.3, kde=True, fill=True, color='C0')
sns.histplot(y=df_nn["cut"], ax=g.ax_marg_y, alpha=.3, kde=True, fill=True, color='C0')
sns.histplot(x=df_truth["ctgre"], ax=g.ax_marg_x, alpha=.3, kde=True, fill=True, color='C1')
sns.histplot(y=df_truth["cut"], ax=g.ax_marg_y, alpha=.3, kde=True, fill=True, color='C1')

# sns.histplot(y=df_nn["cut"], ax=g.ax_marg_x, alpha=.5, kde=True, fill=False)
# sns.histplot(y=samples_1[:,1], ax=g.ax_marg_y, alpha=.5, kde=False)

g.set_axis_labels(r'$\mathrm{Re}\:C_{tG}$', r'$C_{tu}^{(1)}$')
g.ax_joint.legend(handles=handles, frameon=False)

# ax = sns.jointplot(data=df, x="ctgre", y="cut", hue="mode", alpha=.5)
# ax.set_axis_labels(r'$\mathrm{Re}\:C_{tG}$', r'$C_{tu}^{(1)}$')
# ax.plot_joint(sns.kdeplot, zorder=0, levels=6, s=10, alpha=.5)
#
# ax.set_title("test")
#
# texts = g.ax_joint.legend_.texts
# for t, label in zip(texts, "AB"):
#     t.set_text(label)

# plt.xlim((-2, 2))
# plt.ylim((-3.5, 3))

#plt.legend(labels=["test 1", "test2"], loc="upper left", frameon=False, fontsize=10)

g.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/23_06/tt_limits_both.pdf')
#g_truth.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/23_06/tt_limits_truth.pdf')
