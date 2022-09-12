#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'
MULTINEST='data/theorie/jthoeve/miniconda3/lib:$LD_LIBRARY_PATH'
MPI='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/mpiexec'

function submit_job () {

  NCORES=$1
  FIT_ID=$2
#  COEFF1=$3
#  COEFF2=$4

  # create bash file to submit
  COMMAND=$PWD'/launch_ns.sh'

  ARGS='-f '$FIT_ID
  #ARGS='-f '$FIT_ID' -c '$COEFF1' '$COEFF2

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH='$MULTINEST';'$MPI' -n '$NCORES' '$PY' '$PWD'/optimize_runner.py '$ARGS
  echo $LAUNCH >> $COMMAND

  chmod +x $COMMAND
  chmod +x $PWD'/optimize_runner.py'

  # submission
  qsub -q short7 -W group_list=theorie -l nodes=1:ppn=$NCORES -l pvmem=8000mb -l walltime=04:00:00 $COMMAND
  rm $COMMAND

}

# SETUP
NCORES='16'
FID_ID=$PWD'/run_cards/NS_run_card_tt_llvlvlbb.json'

# pair of operator fits

# zh
#set -- "cHu" "cHd" "cHj1" "cHj3" "cbHRe" "cHW" "cHWB"

# tt
#set -- "cQd8" "cQj18" "cQj38" "cQu8" "ctd8" "ctGRe" "ctj8" "ctu8"

#pair-wise fit
#for a; do
#    shift
#    for b; do
#      submit_job $NCORES $FID_ID $a $b
#    done
#done

# global fit

submit_job $NCORES $FID_ID



