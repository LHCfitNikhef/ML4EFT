import wget
import tarfile
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

import ml4eft.core.classifier as classifier
import ml4eft.analyse.analyse as analyse
import ml4eft.plotting.features as features

feature_dict = {'pt_l1': r'$p_T^{\ell}\;[\mathrm{GeV}]$',
            'pt_l2': r'$p_T^{\bar{\ell}}\;[\mathrm{GeV}]$',
            'pt_l_leading': r'$p_T^{\ell}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            'pt_l_trailing': r'$p_T^{\ell}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            'eta_l1': r'$\eta_\ell$',
            'eta_l2': r'$\eta_{\bar{\ell}}$',
            'eta_l_leading': r'$\eta_\ell\;(\mathrm{leading})$',
            'eta_l_trailing': r'$\eta_\ell\;(\mathrm{trailing})$',
            'pt_ll': r'$p_T^{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            'm_ll': r'$m_{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
            'DeltaPhi_ll': r'$\Delta\phi(\ell, \bar{\ell})$',
            'DeltaEta_ll': r'$\Delta\eta(\ell, \bar{\ell})$',
            'pt_b_leading': r'$p_T^{b}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
            'pt_b_trailing': r'$p_T^{b}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
            'eta_b_leading': r'$\eta_{b}\;(\mathrm{leading})$',
            'eta_b_trailing': r'$\eta_{b}\;(\mathrm{trailing})$',
            'pt_bb': r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$',
            'm_bb': r'$m_{b\bar{b}}\;[\mathrm{GeV}]$'
         }

legend_labels = [r'event_FSR',r'event_FSR_MPI_ISR']


coeff = ["sm", "ctd8", "cQj18", "cQu8", "ctj8", "ctGRe"]
typp = ["event"]
for typ in typp:

    for coef in coeff:
        # df_hard = pd.read_pickle('/data/theorie/jthoeve/ML4EFT/training_data/ml4eft10/tt_llvlvlbb/tt_' + str(coef) + '/events_0.pkl.gz', compression='infer')
        df_hard = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/output/big_data_good_phi/event/tt_' + str(coef) + '/events_0.pkl.gz', compression='infer')

        df = {}  # create an empty dictionary to store dataframes
        for i in range(23):
            df[i] = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/output/big_data_MPI_ISR/' + str(typ) + '/tt_' + str(coef) + '/events_' + str(i) + '.pkl.gz', compression='infer')

        events_shower = []
        for i in range(23):
            events_shower.append(df[i])


        fig = features.plot_features(df_hard, events_shower, feature_dict, legend_labels)
        plt.savefig('/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/distr_checks/' 'FSR_MPI_ISR_' + str(typ) + '_' + str(coef) + '.png')
    



# df_hard = pd.read_pickle('/data/theorie/jthoeve/ML4EFT/training_data/ml4eft10/tt_llvlvlbb/tt_cQj18/events_0.pkl.gz', compression='infer')

# df = {}  # create an empty dictionary to store dataframes
# for i in range(23):
#     df[i] = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/output/big_data_good_phi/hard/tt_cQj18/events_' + str(i) + '.pkl.gz', compression='infer')
# # for i in range(0,23):
# #     df + str(i) = pd.read_pickle('/data/theorie/jthoeve/ML4EFT/training_data/ml4eft10/tt_llvlvlbb/tt_sm/events_' + str(i) + '.pkl.gz', compression='infer')
# # df2 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/output/big_data_good_phi/hard/tt_cQd8/events_0.pkl.gz', compression='infer')
# # df3 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/output/big_data/hard/tt_sm/events_2.pkl.gz', compression='infer')
# # df4 = pd.read_pickle('/data/theorie/pherbsch/ML4EFT/subproj/output/big_data/hard/tt_sm/events_3.pkl.gz', compression='infer')

# # df_hard = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/consistency_checks/external_pt/reference/hard/tt_sm/events_0.csv')
# # df1 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/consistency_checks/external_pt/reference/event/tt_sm/events_0.csv')
# # df2 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/test/event/tt_sm/events_0.csv')
# # df3 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/output/test/tt_smrec_soft0.2.csv')
# # df4 = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/output/test/tt_ctd8_ctd8soft_rec0.2.csv')


# # coeff = ["a"]
# events_shower = []
# for i in range(23):
#     events_shower.append(df[i])
#     # events_shower.append(df2)
#     # events_shower.append(df3)
#     # events_shower.append(df4)


# feature_dict = {'pt_l1': r'$p_T^{\ell}\;[\mathrm{GeV}]$',
#             'pt_l2': r'$p_T^{\bar{\ell}}\;[\mathrm{GeV}]$',
#             'pt_l_leading': r'$p_T^{\ell}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
#             'pt_l_trailing': r'$p_T^{\ell}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
#             'eta_l1': r'$\eta_\ell$',
#             'eta_l2': r'$\eta_{\bar{\ell}}$',
#             'eta_l_leading': r'$\eta_\ell\;(\mathrm{leading})$',
#             'eta_l_trailing': r'$\eta_\ell\;(\mathrm{trailing})$',
#             'pt_ll': r'$p_T^{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
#             'm_ll': r'$m_{\ell\bar{\ell}}\;[\mathrm{GeV}]$',
#             'DeltaPhi_ll': r'$\Delta\phi(\ell, \bar{\ell})$',
#             'DeltaEta_ll': r'$\Delta\eta(\ell, \bar{\ell})$',
#             'pt_b_leading': r'$p_T^{b}\;(\mathrm{leading})\;[\mathrm{GeV}]$',
#             'pt_b_trailing': r'$p_T^{b}\;(\mathrm{trailing})\;[\mathrm{GeV}]$',
#             'eta_b_leading': r'$\eta_{b}\;(\mathrm{leading})$',
#             'eta_b_trailing': r'$\eta_{b}\;(\mathrm{trailing})$',
#             'pt_bb': r'$p_T^{b\bar{b}}\;[\mathrm{GeV}]$',
#             'm_bb': r'$m_{b\bar{b}}\;[\mathrm{GeV}]$'
#          }

# legend_labels = [r'hard_jaco_sm',r'h_pim_sm1']

# fig = features.plot_features(df_hard, events_shower, feature_dict, legend_labels)
# plt.savefig('/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/distr_check.png')

