#!/bin/sh
# export OMP_STACKSIZE=16000
# export OMP_NUM_THREADS=4
# export KMP_BLOCKTIME=0
# export KMP_AFFINITY=granularity=fine,verbose,compact,1,0

#maybe the problem on the cluster is with my conda env, let's activate it explicitly
# source /data/theorie/pherbsch/miniconda3/condabin/conda.sh
# conda activate madgraph


# coefficient="$1"
# zcut_beta="$2"
coefficient="$coefficient"
zcut_beta="$zcut_beta"

# echo "Job list arguments:"
# echo "Coefficient: $coefficient"
# echo "Zcut_beta: $zcut_beta"

# cd /data/theorie/pherbsch/ML4EFT/subproj/code/

# Update the runcard with the coefficient given by the init file. 
# sed searches for the sequence of the coefficient and replaces it with the new coefficient

# sed -i "s/\"coefficient\": \".*\"/\"coefficient\": \"$coefficient\"/" ./runcards/shower/shower_settings.json

# echo "Executing command: python /data/theorie/pherbsch/ML4EFT/subproj/code/w_runcard_lhe_parser.py $coefficient $zcut_beta"
python /data/theorie/pherbsch/ML4EFT/subproj/code/w_runcard_lhe_parser.py $coefficient $zcut_beta


# cat ./runcards/shower/shower_settings.json
# # Print conda environment information only once
# if [ ! -f ../random_data_bin/test/error/conda_list.txt ]; then
#     conda list > ../random_data_bin/test/error/conda_list.txt
# fi