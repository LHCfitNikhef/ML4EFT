#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/eels_kk/bin/python'

function submit_job () {

  REP=$1

  # create bash file to submit
  COMMAND=$PWD'/launch_rep_'$REP'.sh'

  # write launch command
  LAUNCH=$PY' '$PWD'/training_init.py '$REP

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/training_init.py'

  # submission
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=1 -l pvmem=8000mb -l walltime=08:00:00 $COMMAND
  rm $COMMAND

}

# SETUP
MCREPS=30

for ((rep=0; rep < $MCREPS; rep++)); do
  submit_job $rep
done