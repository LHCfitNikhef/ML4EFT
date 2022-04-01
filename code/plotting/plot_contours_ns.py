import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy
import arviz as az
import pymultinest
import json
import os

from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 13})
rc('text', usetex=True)

def combine_qc(c_x, c_y, path):
    q_c = np.zeros((len(c_y), len(c_x)))
    for row, cHWB in enumerate(c_y):
        values = np.load(os.path.join(path.format(row)),
                         allow_pickle=True).flatten()
        q_c[row, :] = values
    q_c = 2 * (- q_c + np.nanmax(q_c))
    return q_c

#c_x, c_y = np.load('/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/features_mzh_y_robust/truth_v2/scan_domain.npy') #chw, chq3
#path_to_row_truth = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/features_mzh_y_robust/truth_v2'
#yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis

# load posterior samples
path_to_samples = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/ns/posterior.json'
with open(path_to_samples) as json_data:
    samples_json = json.load(json_data)

fig, ax = plt.subplots(figsize=(10, 10))

df = pd.DataFrame(samples_json)

g = sns.JointGrid()
x, y = df['chw'], df['chq3']
sns.scatterplot(x=x, y=y, s=10, alpha=.5, ax=g.ax_joint)
sns.kdeplot(x=x, y=y, levels=[0.05], bw_adjust=1.2, color='red', ax=g.ax_joint)
sns.histplot(x=x, ax=g.ax_marg_x, alpha=.5, kde=True)
sns.histplot(y=y, ax=g.ax_marg_y, alpha=.5, kde=True)
g.set_axis_labels(r'$\rm{cHW}$', r'$\rm{cHq3}$')

#q_c_truth = combine_qc(c_x, c_y, path_to_row_truth)
# plt.contour(xx, yy, q_c_truth, np.array([5.99]), origin='lower', linestyles='dashed',
#                                      linewidths=0.5, extent=(c_x.min(), c_x.max(), c_y.min(), c_y.max()))


# g = sns.JointGrid(data=df, x="chw", y="chq3", height=10)
# g.plot_joint(sns.scatterplot, s=10, alpha=.5)
# g.plot_marginals(sns.histplot, kde=True)
# g.kdeplot(x=samples_json['chw'], y=samples_json['chq3'],  levels=[0.05], bw_adjust=1.2, color='red')

g.savefig('/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/01_04/samples.pdf')
