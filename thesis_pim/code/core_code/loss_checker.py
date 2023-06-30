# This is a somewhat elaborate code to check if the neural network training went right. What the code does is parse through the 
# training/validation loss of the models to see if there are models that don't converge to roughly the same loss as the other
# models. Then this model is likely faulty. What the code does is compare the value of the for the final model with 4 other 
# final models and see if it is very different. Then it prompts the user to delete this model. This makes it so you don't have
# to check the validation/training loss manually to get rid of faulty models.

import os
import re
from shutil import rmtree
import numpy as np
import sys
from shutil import rmtree


# Function to get the unit of the decimal place following the first non-zero digit
def get_unit(num):
    str_num = str(num)
    non_zero_indices = [i for i, digit in enumerate(str_num) if digit != '0' and digit != '.']
    if len(non_zero_indices) >= 1:
        # calculate the unit for the decimal place following the first non-zero digit
        unit = 3 * 10 ** -(non_zero_indices[0] + 1 - str_num.index('.'))
        return unit
    return None

# Function to compare each loss with the others in its block
def compare_within_block(block, mc_run_dirs):
    block = list(block)  # Ensure block is a list, not a numpy array
    for i, loss in enumerate(block):
        unit = get_unit(loss)
        if unit is not None:
            other_losses = block[:i] + block[i+1:]  # Concatenate the slices into a new list
            deviations = [abs(other_loss - loss) >= unit for other_loss in other_losses]
            if deviations.count(True) > 2:  # Check if this loss deviates from more than 2 other losses in the block
                print(f'Loss for {mc_run_dirs[i]} is different from most others in its block.')
                print(f'This run: {loss}. Other runs in block: {other_losses}')
                delete = input('Do you want to delete this run? (y/n): ')
                if delete.lower() == 'y':
                    rmtree(mc_run_dirs[i])
                    return True  # A directory has been deleted
    return False  # No directory has been deleted




# Get the list of models directories
if len(sys.argv) < 2:
    raise ValueError('The "feature_num" argument must be provided.')
base_directory = '/data/theorie/pherbsch/ML4EFT/subproj/output/models/FSR_ISR_MPI/repeat_model_train/quad_18feat/event/2023/05/26'
model_directories = [os.path.join(base_directory, d) for d in os.listdir(base_directory) if 'model' in d]
feature_num = sys.argv[1]

for model_dir in model_directories:
    training_losses = []
    validation_losses = []
    mc_run_dirs = [os.path.join(model_dir, d) for d in os.listdir(model_dir) if 'mc_run' in d]
    
    # Extract losses from log files
    for mc_run_dir in mc_run_dirs:
        logs_directory = os.path.join(mc_run_dir, 'logs')
        log_files = [f for f in os.listdir(logs_directory) if f.endswith('.log')]
        
        if not log_files:
            print(f"No .log files in directory: {logs_directory}")
            delete = input('Do you want to delete this run? (y/n): ')
            if delete.lower() == 'y':
                rmtree(mc_run_dir, ignore_errors=True)
            continue  # Skip this mc_run_dir

        log_file_path = os.path.join(logs_directory, log_files[0])
        
        with open(log_file_path, 'r') as log_file:
            lines = log_file.readlines()
            num_lines = len(lines)
            
            if feature_num == '18':
                if num_lines < 204:
                    print(f"Warning: {log_file_path} does not have 201 lines. Only {num_lines} lines found.")
                    delete = input('Do you want to delete this run? (y/n): ')
                    if delete.lower() == 'y':
                        rmtree(mc_run_dir)
                        continue
                    else:
                        continue
                last_loss_line = lines[-204] 
                training_loss = float(last_loss_line.split('Training loss ')[1].split(',')[0])
                validation_loss = float(last_loss_line.split('Validation loss ')[1].split(',')[0])
                
                training_losses.append(training_loss)
                validation_losses.append(validation_loss)

            elif feature_num == '2':
                if num_lines < 104:
                    print(f"Warning: {log_file_path} does not have 101 lines. Only {num_lines} lines found.")
                    delete = input('Do you want to delete this run? (y/n): ')
                    if delete.lower() == 'y':
                        rmtree(mc_run_dir)
                        continue
                    else:
                        continue
                last_loss_line = lines[-104]
                training_loss = float(last_loss_line.split('Training loss ')[1].split(',')[0])
                validation_loss = float(last_loss_line.split('Validation loss ')[1].split(',')[0])
                
                training_losses.append(training_loss)
                validation_losses.append(validation_loss)


    # Divide losses into blocks of 5
    training_loss_blocks = np.array_split(training_losses, len(training_losses) // 5)
    validation_loss_blocks = np.array_split(validation_losses, len(validation_losses) // 5)
    mc_run_dir_blocks = np.array_split(mc_run_dirs, len(mc_run_dirs) // 5)

    # Check differences within each block
    for i, training_loss_block in enumerate(training_loss_blocks):
        deleted = compare_within_block(training_loss_block, mc_run_dir_blocks[i])
        if deleted:
            continue  # Skip checking the validation losses if a directory has been deleted

        compare_within_block(validation_loss_blocks[i], mc_run_dir_blocks[i])


