#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'
MULTINEST='data/theorie/jthoeve/miniconda3/lib:$LD_LIBRARY_PATH'
MPI='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/mpiexec'

function submit_job () {

  NCORES=$1
  FIT_ID=$2
  # create bash file to submit
  COMMAND=$PWD'/launch_ns.sh'

  ARGS='-f '$FIT_ID

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH='$MULTINEST';'$MPI' -n '$NCORES' '$PY' '$PWD'/optimize_runner.py '$ARGS
  echo $LAUNCH >> $COMMAND

  chmod +x $COMMAND
  chmod +x $PWD'/optimize_runner.py'

  # submission
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=$NCORES -l pvmem=16000mb -l walltime=00:30:00 $COMMAND
  rm $COMMAND

}

# SETUP
NCORES='24'
FID_ID=$PWD'/run_cards/NS_run_card.json'
submit_job $NCORES $FID_ID
