import bounds_2 as bnds
import expected_events as exp
import numpy as np

n = 100000
event_data_1 = bnds.load_data('/data/theorie/jthoeve/ML4EFT/quad_clas/eft_06_v3.lhe', n=n, s=n)
event_data_2 = bnds.load_data('/data/theorie/jthoeve/ML4EFT/quad_clas/eft_06_v2.lhe', n=n, s=n)
bins = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 4000])
#bins = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 4000])
#bins = np.array([300, 400, 500, 600, 4000])
n_i_1, _ = np.histogram(event_data_1, bins=bins)
n_i_2, _ = np.histogram(event_data_2, bins=bins)

print(n_i_1/n)
print(n_i_2/n)
print(n_i_1/n_i_2)

# path_output = '/data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/binned/bin_1'
# n_exp = exp.expected_events_binned(np.array([0, 0.6]), bins, path_output).astype(int)
#
# print(n_exp)