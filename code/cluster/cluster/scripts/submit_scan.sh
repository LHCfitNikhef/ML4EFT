#!/bin/bash

# script to submit jobs to the smefit queue

pbs_file=/data/theorie/jthoeve/ML4EFT/cluster/scripts/scan.pbs
for mc_run in `seq 1 1`; do
    qsub -q smefit -W group_list=smefit -l nodes=1:ppn=2 -v ARG=$mc_run $pbs_file
done
