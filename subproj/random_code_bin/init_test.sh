#!/bin/bash

cluster_message_output_dir="../code/cluster_message_output/"
coefficient_file="../code/parse_lists/parse_sm.txt"

while IFS= read -r coefficient || [ -n "$coefficient" ]; do
    ./coef.sh "$coefficient"
done < "$coefficient_file"