#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'

function submit_job () {

  RUN_CARD=$1
  REP=$2
  COEFF=$3

  # create bash file to submit
  COMMAND=$PWD'/launch_rep_'$COEFF'_'$REP'.sh'

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/theorie/jthoeve/miniconda3/lib;'$PY' '$PWD'/training_init.py '$RUN_CARD' '$REP' '$COEFF

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/training_init.py'

  # submission
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=1 -l pvmem=4000mb $COMMAND
  rm $COMMAND

}

# SETUP

MCREPS=25

# tt -> llvlvlbb

RUN_CARD="example_train_run_card.json"

coeff=( "ctGRe" "ctj8" "ctGRe_ctGRe" "ctGRe_ctj8" "ctj8_ctj8")

for c in "${coeff[@]}"
do
  for ((rep=0; rep < $MCREPS; rep++)); do
    submit_job $RUN_CARD $rep $c
  done
done
