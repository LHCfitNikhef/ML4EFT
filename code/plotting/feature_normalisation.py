import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.preprocessing import StandardScaler, RobustScaler

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

import os

plot_directory = '/Users/jaco/Documents/ML4EFT/plots/2022/24_02'

df = pd.read_pickle("/Users/jaco/Documents/ML4EFT/training_data/zh_llbb/sm/events_0.pkl.gz").iloc[1:,:]
df['log_pt_z'] = np.log(df['pt_z'])

kinematic = ['pt_z']

df_scaled = df.copy()


stdsc = StandardScaler()
quantile_scaler = RobustScaler(quantile_range=(5, 95))

df_scaled['pt_z_std'] = stdsc.fit_transform(df[kinematic].values.reshape(-1,1))
df_scaled['pt_z_log_std'] = stdsc.fit_transform(df['log_pt_z'].values.reshape(-1,1))
df_scaled['pt_z_robust'] = quantile_scaler.fit_transform(df['log_pt_z'].values.reshape(-1,1))


bins = np.concatenate([np.array([df_scaled['pt_z_std'].min()]), np.linspace(-1, 1, 20), np.array([df_scaled['pt_z_std'].max()])])

fig, ax = plt.subplots(figsize=(10,6))
kwargs = dict(histtype='stepfilled', alpha=0.3, density=False, bins=bins, ec="k")
plt.hist(df_scaled['pt_z_std'].values, **kwargs, label=r'$\rm{Standardized}$')
plt.hist(df_scaled['pt_z_log_std'].values, **kwargs, label=r'$\rm{Log\;transform}$' )
plt.hist(df_scaled['pt_z_robust'].values, **kwargs, label=r'$\rm{Robust\;scaler}$')



plt.xlabel(r'$p_T^Z\;\rm{(scaled)}$')
plt.ylabel(r'$\rm{a.u.}$')
ax.set_yticklabels([])
plt.legend(prop={"size": 15}, loc='upper left')
plt.xlim(-1.2, 1.2)
plt.axvline(1, color='red', linestyle='solid')
plt.axvline(-1, color='red', linestyle='solid')
plt.tight_layout()
fig.savefig('/Users/jaco/Documents/ML4EFT/output/plots_paper/methodology/feature_scaling.pdf')
