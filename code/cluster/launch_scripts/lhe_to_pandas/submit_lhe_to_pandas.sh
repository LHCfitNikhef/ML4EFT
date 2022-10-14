#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/eels_kk/bin/python'

function submit_job () {

  EVENT_DIR=$1
  PROCESS=$2
  SAVE_LOCATION=$3

  # create bash file to submit
  COMMAND=$PWD'/lhe_to_pandas_'"${EVENT_DIR##*/}"'.sh'

  # write launch command

  LAUNCH=$PY' '$PWD'/lhe_to_pandas_tt_parton.py '$EVENT_DIR' '$PROCESS' '$SAVE_LOCATION

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/lhe_to_pandas_tt_parton.py'

  #$COMMAND

  # submission
  qsub -q short7 -W group_list=theorie -l nodes=1:ppn=1 -l pvmem=2000mb -l walltime=01:00:00 $COMMAND
  rm $COMMAND

}

while getopts ":f:s:p:h" opt; do
  case ${opt} in
    f) echo "You chose 'f'=$OPTARG";ROOT="$OPTARG";;
    s) echo "You chose 's'=$OPTARG";SAVE_LOCATION="$OPTARG";;
    p) echo "You chose 'p'=$OPTARG";PROCESS="$OPTARG";;
    h)
      echo "Options:"
      echo "    -h      display this help message."
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

#mkdir -p $SAVE_LOCATION

for dir in $ROOT/*/
do
    dir=${dir%*/} # remove the trailing "/"
    submit_job $dir $PROCESS $SAVE_LOCATION
done

#submit_job $ROOT $PROCESS $SAVE_LOCATION



