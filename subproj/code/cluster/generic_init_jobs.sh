#!/bin/bash

cluster_message_err_dir="./cluster_message_output/err/"
cluster_message_output_dir="./cluster_message_output/out/"

coefficient_file="/data/theorie/pherbsch/ML4EFT/subproj/code/parse_lists/coefficient_parse_list.txt"
zcut_beta="0.2;0.5"

while IFS= read -r coefficient || [ -n "$coefficient" ]; do
    # ./job_list.sh "$coefficient" "$zcut_beta"
    # cat ../runcards/shower/shower_settings.json
    qsub -q short -l walltime=04:00:00 -o "${cluster_message_output_dir}" -e "${cluster_message_err_dir}" -v "coefficient=$coefficient,zcut_beta=$zcut_beta" job_list.sh
done < "$coefficient_file"