#!/bin/bash

# script to submit jobs to the smefit queue
# Note: user has to change the number of mc_runs. Currently set to 1.

pbs_file=/data/theorie/jthoeve/ML4EFT/quad_clas/cluster/bounds.pbs
for mc_run in `seq 1 100`; do
    qsub -q smefit -W group_list=smefit -l nodes=1:ppn=2 -v ARG=$mc_run $pbs_file
done
