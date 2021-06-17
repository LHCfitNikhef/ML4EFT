#!/bin/bash

# script to submit jobs to the smefit queue

pbs_file=/data/theorie/jthoeve/ML4EFT_v2/cluster/launch_scripts/scan.pbs
for mc_run in `seq 1 1`; do
    qsub -q smefit -W group_list=smefit -v ARG=$mc_run $pbs_file
done
