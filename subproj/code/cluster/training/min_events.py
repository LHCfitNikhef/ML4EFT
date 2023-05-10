import glob
import pandas as pd
import gzip
import pickle
import sys
import os

def get_dataframe_length(file_path):
    # Try to load the file into a pandas dataframe
    try:
        with gzip.open(file_path, 'rb') as f:
            df = pickle.load(f)

        # Get the number of rows
        length = len(df)
        return length
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

# Use glob to get all the .pkl.gz files in the directory
coeff = sys.argv[1]
file_paths = glob.glob("/data/theorie/pherbsch/ML4EFT/subproj/output/big_data/event/" + coeff + "/*.pkl.gz")

# Initialize minimum length to a very large number
min_length = float('inf')
processed_files = 0
# Iterate over each file
for file_path in file_paths[:25]:
    length = get_dataframe_length(file_path)
    # If length is None, there was an error processing the file
    if length is not None:
        processed_files += 1
        # If this file's number of rows is smaller than the current minimum, update the minimum
        if length < min_length:
            min_length = length

# Print the shortest column length and the number of files considered
sm_events_num = 63311

if (min_length -1 < sm_events_num):
    print(f"The shortest column length among all {processed_files} processed files out of {len(file_paths)} total files is: {min_length - 1}")
else:
    print(f"The shortest column length is from the sm which is: {sm_events_num} events")