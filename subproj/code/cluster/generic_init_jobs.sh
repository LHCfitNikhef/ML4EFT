#!/bin/bash

cluster_message_err_dir="./cluster_message_output/err/"
cluster_message_output_dir="./cluster_message_output/out/"

coefficient_file="../parse_lists/parse_sm.txt"
zcut_beta="0.8;1"

while IFS= read -r coefficient || [ -n "$coefficient" ]; do
    # ./job_list.sh "$coefficient"
    # cat ../runcards/shower/shower_settings.json
    qsub -q short -l walltime=00:15:00 -o "${cluster_message_output_dir}" -e "${cluster_message_err_dir}" -v "coefficient=$coefficient,zcut_beta=$zcut_beta" job_list.sh
done < "$coefficient_file"