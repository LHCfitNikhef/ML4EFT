import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import NullFormatter
import json
import pandas as pd

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 22})
rc('text', usetex=True)

def sample_loader(path):
    with open(path) as json_data:
        samples = json.load(json_data)
    df = pd.DataFrame(samples)
    return df

df_nn_global = sample_loader('/data/theorie/jthoeve/ns_samples/tt_llvlvlbb/nn_ctu8_only/posterior.json')

n_cols = 1
n_rows = int(np.ceil(len(df_nn_global.columns) / n_cols))
fig = plt.figure(figsize=(n_cols * 5, n_rows * 5))

coeff_dict = {"cHu": r'$c_{\varphi u}$', "cHd": r'$c_{\varphi d}$', "cHj1": r'$c_{\varphi q}^{(1)}$', "cHj3": r'$c_{\varphi q}^{(3)}$',
              "cbHRe": r'$c_{b\varphi}$', "cHW": r'$c_{\varphi W}$', "cHWB": r'$c_{\varphi WB}$', "ctu8": r'$c_{tu}^{(8)}$'}

for i, c in enumerate(df_nn_global):
    ax = plt.subplot(n_rows, n_cols, i + 1)
    ax.hist(df_nn_global[c], bins=50)
    ax.set_xlabel(coeff_dict[c])
plt.tight_layout()
fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/28_09/ctu8_only_post.pdf')