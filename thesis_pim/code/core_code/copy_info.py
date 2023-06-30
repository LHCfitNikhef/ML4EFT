# This code directly copies the files containing the value of the wilson coefficients from the jaco's directories to the newly created directories

import os
import shutil

# Define your directory paths
base_dir = "/data/theorie/jthoeve/ML4EFT/training_data/ml4eft10/tt_llvlvlbb/"
dest_dir = "/data/theorie/pherbsch/ML4EFT/subproj/output/Final/FSR_ISR_MPI/hard/"

# Get list of subdirectories in both directories
subdirs1 = {d.name for d in os.scandir(base_dir) if d.is_dir()}
subdirs2 = {d.name for d in os.scandir(dest_dir) if d.is_dir()}

# Find common subdirectories
common_subdirs = subdirs1.intersection(subdirs2)

# Copy 'info.txt' from subdirectories in base_dir to dest_dir
for subdir in common_subdirs:
    file_src = os.path.join(base_dir, subdir, 'info.txt')
    file_dst = os.path.join(dest_dir, subdir, 'info.txt')
    
    if os.path.isfile(file_src):
        shutil.copy2(file_src, file_dst)
