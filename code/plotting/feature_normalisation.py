import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.preprocessing import StandardScaler, RobustScaler


rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

# load data

# zh llbb
# df = pd.read_pickle("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/zh_llbb/sm/events_0.pkl.gz").iloc[1:,:]
# df['log_pt_z'] = np.log(df['pt_z'])
# df['log_pt_b'] = np.log(df['pt_b'])

# tt

df = pd.read_pickle("/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/zh_llbb_final/zh_sm/events_0.pkl.gz").iloc[1:,:]

# initialise sklearn scalers
stdsc = StandardScaler()
robsc = RobustScaler(quantile_range=(5, 95))

# transform features
features_scaled_std = stdsc.fit_transform(df.values)
features_scaled_rob = robsc.fit_transform(df.values)

# convert transformed features to dataframe
df_scaled_std = pd.DataFrame(features_scaled_std, columns=df.columns.values)
df_scaled_rob = pd.DataFrame(features_scaled_rob, columns=df.columns.values)


bins = np.concatenate([np.array([-2]), np.linspace(-1, 1, 20), np.array([2])])

# plot settings

# zh llbb

df = df.drop(labels=['pt_bbar'], axis=1)

x_labels = [r'$p_T^Z$',
            r'$p_T^b$',
            r'$m_{b\bar{b}}$',
            r'$\Delta R(b_1, b_2)$',
            r'$\Delta\phi(b, bb)$',
            r'$|\Delta \eta(Z, bb)|$',
            r'$m_{ll}$',
            r'$\Delta\phi(b, l)$']
# tt

# x_labels = [r'$p_T^t$',
#             r'$m_{t\bar{t}}$',
#             r'$y_{t\bar{t}}$'
#             ]


kwargs = dict(histtype='stepfilled', alpha=0.3, density=False, bins=bins, ec="k")


n_rows = 2
n_cols = int(np.ceil(df.shape[1] / n_rows))
fig = plt.figure(figsize=(n_cols * 4, n_rows * 4))


for i, feature in enumerate(df):
    ax = plt.subplot(n_rows, n_cols, i + 1)
    ax.hist(df_scaled_std[feature].values, **kwargs, label=r'$\rm{Standardised}$')
    ax.hist(df_scaled_rob[feature].values, **kwargs, label=r'$\rm{Robust\;scaler}$')

    ax.set_yticklabels([])
    ax.set_xlim(-1.2, 1.2)
    plt.xlabel(x_labels[i])
    if i == 0:
        plt.legend(prop={"size": 15}, loc='lower left', frameon=True)

    ax.axvline(1, color='red', linestyle='solid')
    ax.axvline(-1, color='red', linestyle='solid')

plt.tight_layout()
fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/19_07/features_zhllbb.pdf')


########

from matplotlib.ticker import NullFormatter

kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, ec="k", bins=50)

fig = plt.figure(figsize=(8, 4))
ax = plt.subplot(1, 2, 1)
ax.set_yticklabels([])
ax.hist(df['pt_z'].values, **kwargs)
plt.xlabel(r'$p_T^Z\;[\mathrm{GeV}]$')
plt.ylabel(r'$d\sigma/dp_T^Z\;[\mathrm{pb}\:\mathrm{GeV}^{-1}]$')
# ax.text(0.9, 0.9,r'$\rm{Unscaled}$',
#      horizontalalignment='right',
#      verticalalignment='center',
#      transform = ax.transAxes, size=6)
#plt.legend(prop={"size": 15}, loc='upper right', frameon=True)
plt.yscale('log')
ax.yaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.axes.yaxis.set_ticklabels([])
ax = plt.subplot(1, 2, 2)
kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, ec="k", bins=bins)
ax.hist(df_scaled_rob['pt_z'].values, **kwargs)
plt.xlabel(r'$p_T^Z\;\rm{(rescaled)}$')
plt.ylabel(r'$d\sigma/dp_T^Z$')
# ax.text(0.9, 0.9,r'$\rm{Rescaled}$',
#      horizontalalignment='right',
#      verticalalignment='center',
#      transform = ax.transAxes, size=6)
ax.set_xlim(-1.2, 1.2)

ax.axvline(1, color='red', linestyle='dotted')
ax.axvline(-1, color='red', linestyle='dotted')
plt.yscale('log')
ax.yaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.axes.yaxis.set_ticklabels([])
#plt.legend(prop={"size": 15}, loc='upper right', frameon=True)
plt.tight_layout()
fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/19_07/features_zhllbb_transformed.pdf')
