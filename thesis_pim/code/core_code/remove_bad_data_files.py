# this code parses the particle and hadron level pkl.gz files to see if there are empty files and prompts for deletion

import os
import gzip
import pandas as pd
import shutil

# The base directory
base_dir = "/data/theorie/pherbsch/ML4EFT/subproj/output/Final/FSR_ISR_MPI"

# The directories to search
search_dirs = ["event", "hard"]

for search_dir in search_dirs:
    # Full path to the search directory
    full_search_dir = os.path.join(base_dir, search_dir)

    # Iterate over each subdirectory
    for subdir in os.listdir(full_search_dir):
        # Full path to the subdirectory
        full_subdir = os.path.join(full_search_dir, subdir)

        # Iterate over each file in the subdirectory
        for file_name in os.listdir(full_subdir):
            # Full path to the file
            full_file_path = os.path.join(full_subdir, file_name)

            # Check if the file is a .pkl.gz file
            if full_file_path.endswith(".pkl.gz"):
                # Open the file
                with gzip.open(full_file_path, 'rb') as f:
                    # Load the dataframe
                    df = pd.read_pickle(f)

                    # Check the number of rows in the dataframe
                    if df.shape[0] < 100000 and search_dir == "hard":
                        # Prompt the user for confirmation
                        response = input(f"The dataframe in file {full_file_path} has {df.shape[0]} rows, which is less than 100000. "
                                         "Do you want to delete this file and its corresponding file in the 'event' directory? (y/n) ")

                        if response.lower() == "y":
                            # Delete the file in the 'hard' directory
                            os.remove(full_file_path)

                            # Construct the path to the corresponding file in the 'event' directory
                            event_file_path = full_file_path.replace("hard", "event")

                            # Check if the file exists in the 'event' directory
                            if os.path.exists(event_file_path):
                                # Delete the file in the 'event' directory
                                os.remove(event_file_path)
                                print(f"Deleted files {full_file_path} and {event_file_path}")
                            else:
                                print(f"Corresponding event file {event_file_path} does not exist.")
