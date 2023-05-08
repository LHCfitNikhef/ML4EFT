import os
import subprocess
import pandas as pd
import json
import shutil
import re
import sys


with open("/data/theorie/pherbsch/ML4EFT/subproj/code/runcards/shower/shower_settings.json", "r") as json_runcard:
    settings = json.load(json_runcard)

# reading the settings for the lhe_parser from the runcard
base_directory = settings["base_directory"]
output_directory = settings["output_directory"]
cpp_executable = settings["cpp_executable"]
num_jobs_max = settings["num_jobs_max"]
num_events_per_job = settings["num_events_per_job"]
coefficient = sys.argv[1]
zcut_beta = sys.argv[2].replace(';', ',') #This way of getting the zcut_beta info is important for passing the list of pairs onto the c++ code
print("zcut_beta: ", zcut_beta)
print("coefficient: ", coefficient)

def convert_csv_to_pkl_gz(csv_path, pkl_gz_path):
    df = pd.read_csv(csv_path)
    df.to_pickle(pkl_gz_path, compression='gzip')
    os.remove(csv_path)

dir_name = "tt_" + coefficient
# Iterate over the job subdirectories
job_number = 0
job_dirs = os.listdir(os.path.join(base_directory, dir_name))
for job_dir in job_dirs:
    #search for the job number in the job directory name
    job_num_search = re.search(r'job(\d+)', job_dir) 
    if job_num_search:
        job_number = int(job_num_search.group(1))
    else:
        continue
    #stop at a specified number of jobs
    if job_number > (num_jobs_max):
        break
    #check if the subdirectory of the coefficient in the ML4EFT events directory is a job directory
    if not job_dir.startswith('job'):
        continue

    # Get the path to the LHE file
    lhe_file_path = os.path.join(base_directory, dir_name, job_dir, 'Events', 'run_01', 'unweighted_events.lhe')

    # Create the path to the output directory and create the directory if it doesn't exist
    hard_dest_dir = os.path.join(output_directory, 'hard', dir_name + '/')
    event_dest_dir = os.path.join(output_directory, 'event', dir_name + '/')
    os.makedirs(hard_dest_dir, exist_ok=True)
    os.makedirs(event_dest_dir, exist_ok=True)

    #copy the runcard into the output directory
    if job_number == 1:
        print("Copying runcards to output directory")
        shutil.copy("/data/theorie/pherbsch/ML4EFT/subproj/code/runcards/shower/shower_settings_groom.json", os.path.join(hard_dest_dir, "shower_settings.json"))
        shutil.copy("/data/theorie/pherbsch/ML4EFT/subproj/code/runcards/shower/shower_settings_groom.json", os.path.join(event_dest_dir, "shower_settings.json"))

    # print("cpp_executable: ", cpp_executable)
    # print("lhe_file_path: ", lhe_file_path)
    # print("hard_dest_dir: ", hard_dest_dir)
    # print("event_dest_dir: ", event_dest_dir)
    # print("num_events_per_job: ", num_events_per_job)
    # print("zcut_beta: ", zcut_beta)
    output = subprocess.run([cpp_executable, lhe_file_path, hard_dest_dir, event_dest_dir, str(num_events_per_job), str(zcut_beta)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    if output.returncode != 0:
        error_dest_file = "/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/test/error/" + "error_" + dir_name + str(job_number) + '.txt'
        
        with open(error_dest_file, 'w') as error_file:
            error_file.write(output.stderr.decode('utf-8'))
    else:
        print("Command executed successfully")

    # Convert the .csv files to .pkl.gz files and delete the .csv files
    #for hard
    for file_name in os.listdir(hard_dest_dir):
        if file_name.endswith('.csv'):
            csv_path = os.path.join(hard_dest_dir, file_name)
            pkl_gz_path = os.path.join(hard_dest_dir, file_name.replace('.csv', '.pkl.gz'))
            convert_csv_to_pkl_gz(csv_path, pkl_gz_path)
    #for event
    for file_name in os.listdir(event_dest_dir):
        if file_name.endswith('.csv'):
            csv_path = os.path.join(event_dest_dir, file_name)
            pkl_gz_path = os.path.join(event_dest_dir, file_name.replace('.csv', '.pkl.gz'))
            convert_csv_to_pkl_gz(csv_path, pkl_gz_path)
