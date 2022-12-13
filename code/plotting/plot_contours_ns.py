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
path_to_truth = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/truth/mtt_y/posterior.json'
path_to_binned = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/binned/fb/posterior.json'



fig, ax = plt.subplots(figsize=(10, 10))

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
labels = [r'$1\;\rm{bin}$', r'$6\;\rm{bins}$', r'$16\;\rm{bins}$']
handles = []

def sample_loader(path):
    with open(path) as json_data:
        samples = json.load(json_data)
    df = pd.DataFrame(samples)
    return df


df_nn = sample_loader(path_to_nn)


df_truth = sample_loader(path_to_truth)


df_binned = sample_loader(path_to_binned)

handles=[]

g = sns.JointGrid(height=6)

sns.scatterplot(x=df_nn["ctgre"], y=df_nn["cut"], s=10, alpha=.5, ax=g.ax_joint)
sns.scatterplot(x=df_truth["ctgre"], y=df_truth["cut"], s=10, alpha=.5, ax=g.ax_joint)
sns.kdeplot(x=df_nn["ctgre"], y=df_nn["cut"], levels=[0.05], bw_adjust=1.2, ax=g.ax_joint)
sns.kdeplot(x=df_truth["ctgre"], y=df_truth["cut"], levels=[0.05], bw_adjust=1.2, ax=g.ax_joint)

sns.scatterplot(x=df_binned["ctgre"], y=df_binned["cut"], s=10, alpha=.5, ax=g.ax_joint)
sns.kdeplot(x=df_binned["ctgre"], y=df_binned["cut"], levels=[0.05], bw_adjust=1.2, ax=g.ax_joint)

handles.append(mpatches.Patch(ec='C0', fc=None, fill=False, label=r"$\mathrm{NN}$"))
handles.append(mpatches.Patch(ec='C1', fc=None, fill=False, label=r"$\mathrm{Truth}$"))
handles.append(mpatches.Patch(ec='C2', fc=None, fill=False, label=r"$\mathrm{Binned}$"))

sns.histplot(x=df_nn["ctgre"], ax=g.ax_marg_x, alpha=.3, kde=True, fill=True, color='C0')
sns.histplot(y=df_nn["cut"], ax=g.ax_marg_y, alpha=.3, kde=True, fill=True, color='C0')
sns.histplot(x=df_truth["ctgre"], ax=g.ax_marg_x, alpha=.3, kde=True, fill=True, color='C1')
sns.histplot(y=df_truth["cut"], ax=g.ax_marg_y, alpha=.3, kde=True, fill=True, color='C1')

g.set_axis_labels(r'$\mathrm{Re}\:C_{tG}$', r'$C_{tu}^{(1)}$')
g.ax_joint.legend(handles=handles, frameon=False)

g.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/23_06/tt_limits_binned_lin.pdf')

