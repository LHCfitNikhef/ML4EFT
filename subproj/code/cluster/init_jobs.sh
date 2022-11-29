#!/bin/bash
qsub -q smefit job_list.sh

#-l walltime=10:00:00 -l nodes=1:ppn=4 -l pvmem=6gb 