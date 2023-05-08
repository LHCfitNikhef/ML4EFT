#!/bin/bash

cluster_message_output_dir="./cluster_message_output/"
coefficient_file="../parse_lists/parse_sm.txt"

while IFS= read -r coefficient || [ -n "$coefficient" ]; do
    # ./job_list.sh "$coefficient"
    qsub -q smefit -W group_list = smefit -l walltime=10:00:00 -l nodes=1:ppn=4 -l pvmem=6gb -o "${cluster_message_output_dir}" -e "${cluster_message_output_dir}" -v "coefficient=$coefficient" job_list.sh
done < "$coefficient_file"