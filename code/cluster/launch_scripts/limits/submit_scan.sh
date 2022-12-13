#!/bin/bash

# script to submit jobs to the smefit queue

pbs_file=/data/theorie/jthoeve/ML4EFT_higgs/code/launch_scripts/limits/scan.pbs
for row in `seq 0 49`; do
    qsub -q smefit -W group_list=smefit -v ARG=$row $pbs_file
done
