#!/bin/bash

pbs_file=/data/theorie/jthoeve/ML4EFT/quad_clas/quad_clas.pbs
for mc_run in `seq 1 1`; do
    qsub -q smefit -W group_list=smefit -l nodes=1:ppn=8 -v ARG=$mc_run $pbs_file
done
