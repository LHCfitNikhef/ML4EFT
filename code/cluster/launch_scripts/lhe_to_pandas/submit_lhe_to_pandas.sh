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

while getopts ":r:f:s:h" opt; do
  case ${opt} in
    r) echo "You chose 'r'=$OPTARG";MCREPS="$OPTARG";;
    f) echo "You chose 'f'=$OPTARG";EVENT_DIR="$OPTARG";;
    s) echo "You chose 's'=$OPTARG";SAVE_LOCATION="$OPTARG";;
    h)
      echo "Options:"
      echo "    -h      display this help message."
      echo "    -r      number of replicas to convert."
      echo "    -f      path to lhe file"
      echo "    -s      path to output directory"
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG"
      exit 1
      ;;
  esac
done
shift $((OPTIND -1))

mkdir -p $SAVE_LOCATION

for ((i=0; i < $MCREPS; i++)); do
  EVENT_FILE=$EVENT_DIR/job$(($i + 1))/Events/run_01
  gunzip $EVENT_FILE/unweighted_events.lhe.gz
  submit_job $EVENT_FILE $SAVE_LOCATION $i
done