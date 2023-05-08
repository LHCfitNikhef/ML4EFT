#!/bin/bash

cluster_message_err_dir="./cluster_message_output/err/"
cluster_message_output_dir="./cluster_message_output/out/"

coefficient_file="../parse_lists/coefficient_parse_list.txt"
zcut_beta="0.2;0.5"

while IFS= read -r coefficient || [ -n "$coefficient" ]; do
    # ./job_list.sh "$coefficient"
    # cat ../runcards/shower/shower_settings.json
    qsub -q generic -l walltime=06:00:00 -o "${cluster_message_output_dir}" -e "${cluster_message_err_dir}" -v "coefficient=$coefficient,zcut_beta=$zcut_beta" job_list.sh
done < "$coefficient_file"