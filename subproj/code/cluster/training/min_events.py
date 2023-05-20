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

def get_sm_events_num(sm_dir):
    sm_min_length = float('inf')
    for file in glob.glob(os.path.join(sm_dir, "*.pkl.gz"))[:25]:
        length = get_dataframe_length(file)
        if length is not None and length < sm_min_length:
            sm_min_length = length
    return sm_min_length

# Use glob to get all the .pkl.gz files in the directory
top_dir = '/data/theorie/pherbsch/ML4EFT/subproj/output/big_data_good_phi/event/tt_sm'
sm_dir = '/data/theorie/pherbsch/ML4EFT/subproj/output/big_data_good_phi/event/tt_sm'

# Get the number of SM events
sm_events_num = get_sm_events_num(sm_dir)

for root, sub_dirs, files in os.walk(top_dir):
    # Initialize minimum length to a very large number
    min_length = float('inf')
    processed_files = 0

    for file in files:
        if file.endswith('.pkl.gz'):
            full_path = os.path.join(root, file)
            length = get_dataframe_length(full_path)
            
            # If length is None, there was an error processing the file
            if length is not None:
                processed_files += 1
                # If this file's number of rows is smaller than the current minimum, update the minimum
                if length < min_length:
                    min_length = length
    #I want to print length and the name of the files in the directory we are considering if the length is smaller than the sm_events_num
    if (min_length - 1 < sm_events_num):
        print(f"The minimal column length of files in directory '{root}' compared with the sm is: {min_length - 1}")



# The code below is usefull to quickly check the minimal column length of a directory of a coefficient of interest
# # Initialize minimum length to a very large number
# min_length = float('inf')
# processed_files = 0
# # Iterate over each file
# for file_path in file_paths[:25]:
#     length = get_dataframe_length(file_path)
#     # If length is None, there was an error processing the file
#     if length is not None:
#         processed_files += 1
#         # If this file's number of rows is smaller than the current minimum, update the minimum
#         if length < min_length:
#             min_length = length

# # Print the shortest column length and the number of files considered
# sm_events_num = 63311

# if (min_length -1 < sm_events_num):
#     print(f"The shortest column length among all {processed_files} processed files out of {len(file_paths)} total files is: {min_length - 1}")
# else:
#     print(f"The shortest column length is from the sm which is: {sm_events_num} events")