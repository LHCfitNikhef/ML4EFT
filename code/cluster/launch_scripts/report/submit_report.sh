#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'


COMMAND=$PWD'/launch_report.sh'

LAUNCH='export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/theorie/jthoeve/miniconda3/lib;'$PY' /data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/plotting/report.py'
echo $LAUNCH >> $COMMAND
chmod +x $COMMAND

qsub -q short7 -W group_list=theorie -l nodes=1:ppn=1 -l walltime=00:30:00 $COMMAND