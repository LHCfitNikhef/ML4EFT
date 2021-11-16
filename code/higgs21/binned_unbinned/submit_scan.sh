#!/bin/bash

# script to submit jobs to the smefit queue
# Note: user has to change the number of mc_runs. Currently set to 1.

pbs_file=/data/theorie/jthoeve/ML4EFT_higgs/code/binned_unbinned/chi2_scan.pbs
#pbs_file_2=/data/theorie/jthoeve/ML4EFT/quad_clas/quad_clas_2.pbs

qsub -q smefit -W group_list=smefit $pbs_file
