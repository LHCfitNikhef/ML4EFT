import os
import pandas as pd
import numpy as np
import gzip
import pickle

# The top-level directory
top_dir = '/data/theorie/pherbsch/ML4EFT/subproj/output/big_data/event'

# Check each subdirectory
for root, sub_dirs, files in os.walk(top_dir):
    # Check each file in the subdirectory
    for file in files:
        # Only check .pkl.gz files
        if file.endswith('.pkl.gz'):
            # Get the full path to the file
            full_path = os.path.join(root, file)
            
            # Load the file into a DataFrame
            with gzip.open(full_path, 'rb') as f:
                df = pickle.load(f)
            
            # Check the properties of the DataFrame
            # if df.shape[1] != 18:
            #     print(f"DataFrame in {full_path} does not have 18 columns.")
            
            # if not (df.iloc[0] > 0.01).all() or not (df.iloc[0] < 1).all():
                # print(f"First row in DataFrame in {full_path} has values outside the range 0.01 to 1.")
            
            if df.isnull().values.any():
                print(f"DataFrame in {full_path} contains NaN values.")
