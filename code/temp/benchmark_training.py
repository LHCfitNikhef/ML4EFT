import torch
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

from ML4EFT_own.code.src.ml4eft.core import classifier as classifier
from ML4EFT_own.code.src.ml4eft.analyse import analyse

import sys

rc('text', usetex=False)

fig, ax = plt.subplots(figsize=(10, 6))

n_reps = 1

x = np.linspace(1.45, 3, 100).reshape(-1, 1)
#x = np.linspace(0.1, 5, 100).reshape(-1, 1)
df = pd.DataFrame(x, columns=['m_tt'])

r1_truth = analyse.Analyse.likelihood_ratio_truth(df, {'ctGRe': -2, 'ctu8': 0}, df.columns.values, process='tt',
												  order='lin')
NN1_truth = (r1_truth - 1) / (-2)

r2_truth = analyse.Analyse.likelihood_ratio_truth(df, {'ctGRe': 0, 'ctu8': 10}, df.columns.values, process='tt',
												  order='lin')
NN2_truth = (r2_truth - 1) / 10
# #
r11_truth = analyse.Analyse.likelihood_ratio_truth(df, {'ctGRe': 10, 'ctu8': 0}, df.columns.values, process='tt',
												   order='quad')
NN11_truth = (r11_truth - 1) / 100

r22_truth = analyse.Analyse.likelihood_ratio_truth(df, {'ctGRe': 0, 'ctu8': 10}, df.columns.values, process='tt',
												   order='quad')
NN22_truth = (r22_truth - 1) / 100

g_preds_NN1 = []
g_preds_NN2 = []
g_preds_NN11 = []
g_preds_NN22 = []


for rep in range(n_reps):

	print(rep)

	# MODIFY PATHS HERE
	#network_path = './ttparton_reweighting/mc_run_{}/trained_nn.pt'.format(rep)
	#path_to_scaler = './ttparton_reweighting/mc_run_{}/scaler.gz'.format(rep)
	#network_path = '/data/theorie/wgautier/wgautier/followup/models/2023/11/27/model_ctGRe/mc_run_1/trained_nn.pt'
	#path_to_scaler = '/data/theorie/wgautier/wgautier/followup/models/2023/11/27/model_ctGRe/mc_run_1/scaler.gz'

	# reweighted
	network_path = '/data/theorie/wgautier/wgautier/followup/models/2023/11/27/model_ctGRe/mc_run_1/trained_nn.pt'
	path_to_scaler = '/data/theorie/wgautier/wgautier/followup/models/2023/11/27/model_ctGRe/mc_run_1/scaler.gz'

	# pre-reweighting
	network_path_ = '/data/theorie/wgautier/wgautier/followup/models/no_weights/2023/11/29/model_ctGRe/mc_run_1/trained_nn.pt'
	path_to_scaler_ = '/data/theorie/wgautier/wgautier/followup/models/no_weights/2023/11/29/model_ctGRe/mc_run_1/scaler.gz'

	#network_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_mtt/2022/10/16/model_ctGRe/mc_run_10/trained_nn.pt'
	#path_to_scaler = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_mtt/2022/10/16/model_ctGRe/mc_run_10/scaler.gz'


	#loaded_model = classifier.Classifier([1, 25, 25, 25, 1],  4)
	loaded_model = classifier.Classifier([1, 100, 100, 100, 1], 2)
	loaded_model.load_state_dict(torch.load(network_path))

	scaler = joblib.load(path_to_scaler)
	features_scaled = scaler.transform(df[['m_tt']])

	loaded_model_ = classifier.Classifier([1, 100, 100, 100, 1], 2)
	loaded_model_.load_state_dict(torch.load(network_path_))

	scaler_ = joblib.load(path_to_scaler_)
	features_scaled_ = scaler_.transform(df[['m_tt']])
	with torch.no_grad():
		#NN1 = loaded_model.NN1(torch.tensor(features_scaled).float()).numpy().flatten()
		#NN11 = loaded_model.NN11(torch.tensor(features_scaled).float()).numpy().flatten()
		#NN2 = loaded_model.NN2(torch.tensor(features_scaled).float()).numpy().flatten()
		#NN22 = loaded_model.NN22(torch.tensor(features_scaled).float()).numpy().flatten()
		NN1 = loaded_model.forward(torch.tensor(features_scaled).float()).numpy().flatten()
		NN11 = loaded_model.forward(torch.tensor(features_scaled).float()).numpy().flatten()
		NN2 = loaded_model_.forward(torch.tensor(features_scaled_).float()).numpy().flatten()
		NN22 = loaded_model_.forward(torch.tensor(features_scaled_).float()).numpy().flatten()


	g_preds_NN1.append(NN1)
	g_preds_NN2.append(NN2)
	g_preds_NN11.append(NN11)
	g_preds_NN22.append(NN22)


	ax.plot(x, NN1, color='C0', linestyle='solid')
	ax.plot(x, NN11, color='C1', linestyle='solid', label='reweighted')
	ax.plot(x, NN2, color='C2', linestyle='solid')
	ax.plot(x, NN22, color='C3', linestyle='solid', label='no weights')


ax.fill_between(x.flatten(), np.percentile(g_preds_NN1, 16, axis=0), np.percentile(g_preds_NN1, 84, axis=0),
			   color='C0', alpha=0.4)
ax.fill_between(x.flatten(), np.percentile(g_preds_NN11, 16, axis=0), np.percentile(g_preds_NN11, 84, axis=0),
			   color='C1', alpha=0.4)
ax.fill_between(x.flatten(), np.percentile(g_preds_NN2, 16, axis=0), np.percentile(g_preds_NN2, 84, axis=0),
				color='C2', alpha=0.4)
ax.fill_between(x.flatten(), np.percentile(g_preds_NN22, 16, axis=0), np.percentile(g_preds_NN22, 84, axis=0),
				color='C3', alpha=0.4)

"""
plt.xlabel(r'$m_{t\bar{t}}\:[\rm{TeV}]$')
plt.tight_layout()

ax.plot(x, NN1_truth, label=r'$\mathrm{Truth}\;(c_{tG})$', linestyle='dotted', color='C0')
ax.plot(x, NN11_truth, label=r'$\mathrm{Truth}\;(c_{tG}\cdot c_{tG})$', linestyle='dotted', color='C1')
ax.plot(x, NN2_truth, label=r'$\mathrm{Truth}\;(c_{tu}^8)$', linestyle='dotted', color='C2')
ax.plot(x, NN22_truth, label=r'$\mathrm{Truth}\;(c_{tu}^8\cdot c_{tu}^8)$', linestyle='dotted', color='C3')
"""
plt.xlabel('Invariant Mass of t bar [TeV]')
#plt.tight_layout()

ax.plot(x, NN1_truth, label='Truth (ctG)', linestyle='dotted', color='C0')
#ax.plot(x, NN11_truth, label='Truth (ctG * ctG)', linestyle='dotted', color='C1')
#ax.plot(x, NN2_truth, label='Truth (ctu^8)', linestyle='dotted', color='C2')
#ax.plot(x, NN22_truth, label='Truth (ctu^8 * ctu^8)', linestyle='dotted', color='C3')
plt.legend(frameon=False)

fig.savefig('./ttparton_reweighting_benchmark.png')
