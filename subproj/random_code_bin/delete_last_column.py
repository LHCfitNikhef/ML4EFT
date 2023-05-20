import os
import pandas as pd
import gzip
import pickle

# Path to the 'event' directory
dir_path = '/data/theorie/pherbsch/ML4EFT/subproj/output/big_data/event'

# Traverse through each subdirectory in 'event'
for root, dirs, files in os.walk(dir_path):
    for file in files:
        # Only consider .pkl.gz files
        if file.endswith('.pkl.gz'):
            file_path = os.path.join(root, file)
            # Load the dataframe from the pkl.gz file
            with gzip.open(file_path, 'rb') as f:
                df = pickle.load(f)
            
            # Check if the last column is 'Unnamed: 19' and all values are NaN
            if df.columns[-1] == 'Unnamed: 19' and df.iloc[:, -1].isna().all():
                print(f"Haven't removed the column from this file {file_path}")
                # # Drop the last column
                # df = df.iloc[:, :-1]
                
                # # Save the modified dataframe back to the pkl.gz file
                # with gzip.open(file_path, 'wb') as f:
                #     pickle.dump(df, f)
