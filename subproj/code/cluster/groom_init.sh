#!/bin/bash

cluster_message_err_dir="/data/theorie/pherbsch/ML4EFT/subproj/code/cluster/cluster_message_output/err/"
cluster_message_output_dir="/data/theorie/pherbsch/ML4EFT/subproj/code/cluster/cluster_message_output/out/"

zcut_beta_list="/data/theorie/pherbsch/ML4EFT/subproj/code/parse_lists/zcut_beta_parse_list.txt"
coefficient="sm"

while IFS= read -r zcut_beta || [ -n "$zcut_beta" ]; do
    # /data/theorie/pherbsch/ML4EFT/subproj/code/cluster/./job_list.sh "$coefficient" "$zcut_beta"
    # cat ../runcards/shower/shower_settings.json
    qsub -q generic -l walltime=05:00:00 -o "${cluster_message_output_dir}" -e "${cluster_message_err_dir}" -v "coefficient=$coefficient,zcut_beta=$zcut_beta" job_list.sh
done < "$zcut_beta_list"