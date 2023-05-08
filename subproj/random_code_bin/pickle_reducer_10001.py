import pandas as pd
import numpy as np
import os

pickle_file = '/data/theorie/pherbsch/ML4EFT/subproj/code/cluster/downloads/training_data/tt_cQd8/events_0.pkl.gz'
# save_loc = '/data/theorie/pherbsch/ML4EFT/subproj/theory_data/tt_parton_shower_sm'
# df = pd.read_pickle(pickle_file,compression='infer')
df = pd.read_csv('/data/theorie/pherbsch/ML4EFT/subproj/output/h_tt_cQu8_cQu8.csv')

# # Store the first element of the column

# first_element = df.loc[0, 'pt_e']

# # Drop the first element from the column
# df = df.drop(0).reset_index(drop=True)


# # Generate a random subset of the remaining elements
# subset = df.sample(n = int(1e5))

# # Concatenate the stored variable back onto the front of the subset
# subset = pd.concat([pd.DataFrame([first_element], columns= subset.columns),subset], ignore_index=True)
# # df = pd.concat([pd.DataFrame([xsec], columns=df.columns), df], ignore_index=True)



# subset.to_pickle(os.path.join(save_loc, "events_0.pkl.gz"), compression="infer")
print(df)