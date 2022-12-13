#!/bin/bash

# script to submit jobs to the smefit queue

pbs_file=/data/theorie/jthoeve/ML4EFT_higgs/code/launch_scripts/nn_accuracy/nn_accuracy_1d.pbs
for mc_run in `seq 1 1`; do
    qsub -q smefit -W group_list=smefit -v ARG=$mc_run $pbs_file
done
