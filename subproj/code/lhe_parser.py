import os
import subprocess
import pandas as pd

def convert_csv_to_pkl_gz(csv_path, pkl_gz_path):
    df = pd.read_csv(csv_path)
    df.to_pickle(pkl_gz_path, compression='gzip')
    os.remove(csv_path)

input_file = './parse_lists/parse_directories.txt'
base_directory = '/data/theorie/jthoeve/ML4EFT_events/'
output_directory = '../output/'
cpp_executable = './shower_code/./clean_shower_big_data_groom'

# Read directory names from the input file
with open(input_file, 'r') as f:
    dir_names = [line.strip() for line in f.readlines()]

# Iterate over the directory names
for dir_name in dir_names:
    # Iterate over the job subdirectories
    # job_number = 0
    job_dirs = os.listdir(os.path.join(base_directory, dir_name))
    for job_dir in job_dirs:
        # if job_number > 3:
        #     break
        # job_number += 1
        if not job_dir.startswith('job'):
            continue

        lhe_file_path = os.path.join(base_directory, dir_name, job_dir, 'Events', 'run_01', 'unweighted_events.lhe')

        hard_dest_dir = os.path.join(output_directory, 'hard', dir_name + '/')
        event_dest_dir = os.path.join(output_directory, 'event', dir_name + '/')
        os.makedirs(hard_dest_dir, exist_ok=True)
        os.makedirs(event_dest_dir, exist_ok=True)
        output = subprocess.check_output([cpp_executable, lhe_file_path, hard_dest_dir, event_dest_dir])


        # Convert the .csv files to .pkl.gz files and delete the .csv files
        for file_name in os.listdir(hard_dest_dir):
            if file_name.endswith('.csv'):
                csv_path = os.path.join(hard_dest_dir, file_name)
                pkl_gz_path = os.path.join(hard_dest_dir, file_name.replace('.csv', '.pkl.gz'))
                convert_csv_to_pkl_gz(csv_path, pkl_gz_path)
        
        for file_name in os.listdir(event_dest_dir):
            if file_name.endswith('.csv'):
                csv_path = os.path.join(event_dest_dir, file_name)
                pkl_gz_path = os.path.join(event_dest_dir, file_name.replace('.csv', '.pkl.gz'))
                convert_csv_to_pkl_gz(csv_path, pkl_gz_path)
