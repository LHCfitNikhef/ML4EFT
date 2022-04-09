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

# grid scan

c_x, c_y = np.load('/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/features_mzh_y_robust/truth_v2/scan_domain.npy') #chw, chq3
yy, xx = np.meshgrid(c_y, c_x, indexing='ij')  # c_y is y-axis

def combine_qc(c_x, c_y, path):
    q_c = np.zeros((len(c_y), len(c_x)))
    for row, cHWB in enumerate(c_y):
        values = np.load(os.path.join(path.format(row)),
                         allow_pickle=True).flatten()
        q_c[row, :] = values
    q_c = 2 * (- q_c + np.nanmax(q_c))
    return q_c

q_c_truth = combine_qc(c_x, c_y, '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/features_mzh_y_robust/truth_v2/q_c_truth_row_{}.npy')

            # plot 95% CL interval

# load posterior samples
path_to_posterior = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/ns/binned/bin_{}/posterior.json'
path_to_truth = '/data/theorie/jthoeve/ML4EFT_higgs/output/contours/zh/ns/truth/posterior.json'

fig = plt.figure(figsize=(10, 10))
g = sns.JointGrid()
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
labels = ['1 bin', '6 bins']
handles = []
import matplotlib.patches as  mpatches
#for i in range(2):
    #with open(path_to_posterior.format(i+1)) as json_data:
with open(path_to_truth) as json_data:
    samples_json = json.load(json_data)

df = pd.DataFrame(samples_json)

#sns.scatterplot(x=df["chw"], y=df["chq3"], s=10, alpha=.5, ax=g.ax_joint)
sns.kdeplot(x=df["chw"], y=df["chq3"], levels=[0.05], bw_adjust=1.2, ax=g.ax_joint, color='red')
handles.append(mpatches.Patch(ec='red', fc=None, fill=False, label="Truth (NS)"))
#sns.histplot(x=df["chw"], ax=g.ax_marg_x, alpha=.5, kde=True)
#sns.histplot(y=df["chq3"], ax=g.ax_marg_y, alpha=.5, kde=True)

#g.ax_joint.scatter(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
contour_truth = g.ax_joint.contour(xx, yy, q_c_truth, np.array([5.99]), origin='lower', linestyles='dashed',
                            linewidths=2.0,
                            colors='green')
handles.append(mpatches.Patch(ec='green', fc=None, fill=False, label="Truth (grid)"))

#g.set_axis_labels(r'$\rm{cHW}$', r'$\rm{cHq3}$')

#handles = [mpatches.Patch(ec=plt.cm.Reds(100), fc=None, fill=False, label="Bin 1")]
plt.legend(handles=handles)
plt.xlabel(r'$\rm{cHW}$')
plt.ylabel(r'$\rm{cHq3}$')
plt.xlim((-0.6, 0.4))
plt.ylim((-2.1, 2.1))

g.savefig('/data/theorie/jthoeve/ML4EFT_higgs/output/plots/2022/01_04/samples_truth_test.pdf')
