# After deleting faulty models witht the loss_checker.py code, this code helps check if there are too few models left.

import os

# Base directory
base_directory = '/data/theorie/pherbsch/ML4EFT/subproj/output/models/FSR_ISR_MPI/lin_2feat/hard/2023/05/25'

# Get model directories
model_directories = [os.path.join(base_directory, d) for d in os.listdir(base_directory) if 'model' in d]

# Iterate over model directories
for model_dir in model_directories:
    # Get mc_run directories
    mc_run_dirs = [os.path.join(model_dir, d) for d in os.listdir(model_dir) if 'mc_run' in d]

    # Check if there are less than 23 mc_run directories
    if len(mc_run_dirs) < 23:
        print(f'Model directory "{model_dir}" contains {len(mc_run_dirs)} mc_run directories.')
    
