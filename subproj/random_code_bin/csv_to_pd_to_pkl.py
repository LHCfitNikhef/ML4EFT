import os
import glob
import gzip
import numpy as np
import pandas as pd

# I want to loop over the files in the output directory "/data/theorie/pherbsch/ML4EFT/subproj/output/" and loop over the csv files to convert them to pickle files
# I want to save the pickle files in the directory "/data/theorie/pherbsch/ML4EFT/subproj/output/pkl_files/"


input_dir_event = '/data/theorie/pherbsch/ML4EFT/subproj/output/event/'
output_dir_event = '/data/theorie/pherbsch/ML4EFT/subproj/output/pkl_files/event/'
input_dir_hard = '/data/theorie/pherbsch/ML4EFT/subproj/output/hard/'
output_dir_hard = '/data/theorie/pherbsch/ML4EFT/subproj/output/pkl_files/hard/'

def process_csv_files(input_dir, output_dir):
    for csv_file in glob.glob(os.path.join(input_dir, '*.csv')):
        # Get the name of the CSV file without the ".csv" extension
        csv_name = os.path.splitext(os.path.basename(csv_file))[0]

        # Create a subdirectory with the name of the CSV file
        sub_dir = os.path.join(output_dir, csv_name)
        os.makedirs(sub_dir, exist_ok=True)

        # Construct the save path for the corresponding pickle file
        save_path = os.path.join(sub_dir, 'events_0.pkl.gz')

        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Save the DataFrame as a pickle file
        df.to_pickle(save_path, compression="gzip")

# Process the CSV files in the event and hard directories
process_csv_files(input_dir_event, output_dir_event)
process_csv_files(input_dir_hard, output_dir_hard)