import wget
import tarfile
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

df_hard = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/test/ex_from_bjet_test/event/tt_sm/events_0.csv')

#I want to make a histogram of the column in df_hard called external_pt with a logarithmic y scale and an x axis from 0 till 2000 with 100 bins

#I want to only save the external_pt column in a new dataframe
df_hard_external_pt = df_hard['external_pt']
#I want to save this dataframe as a csv file
df_hard_external_pt.to_csv('/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/test/external_pt.csv', index=False)
print(df_hard['external_pt'][0:200])
df_hard['external_pt'].hist(bins=100)
plt.yscale('log')
plt.xlim(0,2000)
plt.xlabel('external_pt')
plt.ylabel('number of events')
plt.title('Histogram of external_pt')

plt.savefig('/data/theorie/pherbsch/ML4EFT/subproj/random_plot_bin/external_pt.png')
