import numpy as np
import pandas as pd
import sys, os

npy_dir = sys.argv[1]
n_reps = sys.argv[2]
output_dir = sys.argv[3]

for i in range(int(n_reps)):
    events = np.load(os.path.join(npy_dir, 'events_{}.npy'.format(i)))
    df = pd.DataFrame(events, columns=['m_zh', 'y', 'pt_z'])
    df.to_pickle(os.path.join(output_dir, 'events_{}.pkl.gz'.format(i)), compression='infer')




