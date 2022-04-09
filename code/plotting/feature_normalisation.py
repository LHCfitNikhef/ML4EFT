import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.preprocessing import StandardScaler, RobustScaler


rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

# load data
df = pd.read_pickle("/Users/jaco/Documents/ML4EFT/training_data/zh_llbb/sm/events_0.pkl.gz").iloc[1:,:]
df['log_pt_z'] = np.log(df['pt_z'])
df['log_pt_b'] = np.log(df['pt_b'])


# initialise sklearn scalers
stdsc = StandardScaler()
robsc = RobustScaler(quantile_range=(5, 95))

# transform features
features_scaled_std = stdsc.fit_transform(df.values)
features_scaled_rob = robsc.fit_transform(df.values)

# convert transformed features to dataframe
df_scaled_std = pd.DataFrame(features_scaled_std, columns=df.columns.values)
#df_scaled_rob = pd.DataFrame(features_scaled_rob, columns=df.columns.values)

bins = np.concatenate([np.array([-2]), np.linspace(-1, 1, 20), np.array([2])])
df = df.drop(labels=['pt_z', 'pt_b', 'pt_bbar'], axis=1)
# plot settings

x_labels = [r'$m_{b\bar{b}}$',
            r'$\Delta R(b_1, b_2)$',
            r'$\Delta\phi(b, bb)$',
            r'$|\Delta \eta(Z, bb)|$',
            r'$m_{ll}$',
            r'$\Delta\phi(b, l)$',
            r'$\log p_T^Z$',
            r'$\log p_T^b$'
           ]


kwargs = dict(histtype='stepfilled', alpha=0.3, density=False, bins=bins, ec="k")

n_cols = 2
n_rows = int(np.ceil(df.shape[1] / n_cols))
fig = plt.figure(figsize=(n_cols * 5, n_rows * 4))

df_scaled_rob = pd.read_pickle('/Users/jaco/Documents/ML4EFT/models/test/model_cbhre_lin_lag/mc_run_1/df_sm_scaled.pkl')

for i, feature in enumerate(df):
    ax = plt.subplot(n_rows, n_cols, i + 1)
    ax.hist(df_scaled_std[feature].values, **kwargs, label=r'$\rm{Standardized}$')
    ax.hist(df_scaled_rob[feature].values, **kwargs, label=r'$\rm{Robust\;scaler}$')
    ax.set_yticklabels([])
    ax.set_xlim(-1.2, 1.2)
    plt.xlabel(x_labels[i])
    plt.legend(prop={"size": 15}, loc='upper left')
    ax.axvline(1, color='red', linestyle='solid')
    ax.axvline(-1, color='red', linestyle='solid')

plt.tight_layout()
plt.show()
#fig.savefig('/Users/jaco/Documents/ML4EFT/output/plots_paper/methodology/feature_scaling_log.pdf')


#%%
# load existing scaler
import joblib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
scaler_path = '/Users/jaco/Documents/ML4EFT/models/test/model_chw_lin_log_lag/mc_run_0/scaler.gz'
scaler = joblib.load(scaler_path)
df = pd.read_pickle('/Users/jaco/Documents/ML4EFT/training_data/zh/features_mzh_y_ptz/sm/events_0.pkl.gz')
y = np.zeros(100000)
log_m_zh = np.log(df['m_zh'].iloc[1:])
x_unscaled = np.stack((log_m_zh, y), axis=-1)
x_scaled = scaler.transform(x_unscaled)

plt.hist(x_scaled[:,0])
plt.show()