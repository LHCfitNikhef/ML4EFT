#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/eels_kk/bin/python'

function submit_job () {

  EVENT_FILE=$1
  SAVE_LOCATION=$2
  REP=$3

  # create bash file to submit
  COMMAND=$PWD'/lhe_to_pandas.sh'

  # write launch command
  LAUNCH=$PY' '$PWD'/lhe_to_pandas.py'' '$EVENT_FILE'/unweighted_events.lhe '$SAVE_LOCATION' '$REP

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/lhe_to_pandas.py'

  # submission
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=1 -l pvmem=8000mb -l walltime=08:00:00 $COMMAND
  rm $COMMAND

}

# CONVERSION SETUP

# number of lhe replicas
MCREPS=1

# location of lhe event file to convert
EVENT_DIR=/data/theorie/jthoeve/event_generation/lin_cHW/Events

# location where npy file must be stored
SAVE_LOCATION=/data/theorie/jthoeve/event_generation/events_high_stats/pT/lin/cHW

for ((i=0; i < $MCREPS; i++)); do
  EVENT_FILE=$EVENT_DIR/run_01_$i
  submit_job $EVENT_FILE $SAVE_LOCATION $i
done