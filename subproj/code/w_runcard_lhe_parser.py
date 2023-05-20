import os
import subprocess
import pandas as pd
import json
import shutil
import re
import sys

runcard_loc = "/data/theorie/pherbsch/ML4EFT/subproj/code/runcards/shower/shower_settings.json"
with open(runcard_loc, "r") as json_runcard:
    settings = json.load(json_runcard)

# reading the settings for the lhe_parser from the runcard
base_directory = settings["base_directory"]
output_directory = settings["output_directory"]
cpp_executable = settings["cpp_executable"]
num_jobs_max = settings["num_jobs_max"]
num_events_per_job = settings["num_events_per_job"]
coefficient = sys.argv[1]
zcut_beta = sys.argv[2].replace(';', ',') 
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
    job_num_search = re.search(r'job(\d+)', job_dir) 
    if job_num_search:
        job_number = int(job_num_search.group(1))
    else:
        continue

    if job_number > (num_jobs_max):
        break

    if not job_dir.startswith('job'):
        continue

    events_dir_path = os.path.join(base_directory, dir_name, job_dir, 'Events')
    if not os.listdir(events_dir_path): # If 'Events' folder is empty, skip the job
        continue

    run_dir_path = os.path.join(events_dir_path, 'run_01')
    lhe_file_path = os.path.join(run_dir_path, 'unweighted_events.lhe')
    
    if not os.path.exists(lhe_file_path): # If 'lhe' file is not found, check for 'lhe.gz'
        lhe_file_path = lhe_file_path + ".gz"
        if os.path.exists(lhe_file_path): # If 'lhe.gz' is found, this file is probably a bad run, so check for 'run_02'
            run_dir_path = os.path.join(events_dir_path, 'run_02')
            lhe_file_path = os.path.join(run_dir_path, 'unweighted_events.lhe')
            if not os.path.exists(lhe_file_path): # If 'run_02' doesn't exist or doesn't have the 'lhe' file, skip the job
                continue
    hard_dest_dir = os.path.join(output_directory, 'hard', dir_name + '/')
    event_dest_dir = os.path.join(output_directory, 'event', dir_name + '/')
    os.makedirs(hard_dest_dir, exist_ok=True)
    os.makedirs(event_dest_dir, exist_ok=True)

    #copy the runcard into the output directory
    if job_number == 1:
        print("Copying runcards to output directory")
        shutil.copy(runcard_loc, os.path.join(hard_dest_dir, "shower_settings.json"))
        shutil.copy(runcard_loc, os.path.join(event_dest_dir, "shower_settings.json"))

    output = subprocess.run([cpp_executable, lhe_file_path, hard_dest_dir, event_dest_dir, str(num_events_per_job), str(zcut_beta)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    log_dest_file = "/data/theorie/pherbsch/ML4EFT/subproj/random_data_bin/event_num_test/baseline_good/log.txt"
    with open(log_dest_file, 'w') as log_file: 
        log_file.write(output.stdout.decode('utf-8'))

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
