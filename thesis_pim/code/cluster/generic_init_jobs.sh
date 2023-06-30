#!/bin/bash

cluster_message_err_dir="./cluster_message_output/err/"
cluster_message_output_dir="./cluster_message_output/out/"

coefficient_file="/data/theorie/pherbsch/ML4EFT/subproj/code/parse_lists/parse_sm.txt"
zcut_beta="0.2;0.5"
# 
while IFS= read -r coefficient || [ -n "$coefficient" ]; do
    ./job_list.sh "$coefficient" "$zcut_beta"
    # cat ../runcards/shower/shower_settings.json
    # qsub -q smefit -W group_list=smefit -l nodes=1:ppn=8 -l vmem=64gb -l walltime=40:00:00 -o "${cluster_message_output_dir}" -e "${cluster_message_err_dir}" -v "coefficient=$coefficient,zcut_beta=$zcut_beta" job_list.sh
done < "$coefficient_file"