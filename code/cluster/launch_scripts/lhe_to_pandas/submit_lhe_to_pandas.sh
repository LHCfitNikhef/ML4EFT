#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/eels_kk/bin/python'

function submit_job () {

  EVENT_DIR=$1
  PROCESS=$2
  SAVE_LOCATION=$3
  REP=$4

  # create bash file to submit
  COMMAND=$PWD'/lhe_to_pandas_'"${EVENT_DIR##*/}"'.sh'

  # write launch command

  LAUNCH=$PY' '$PWD'/lhe_to_pandas_tt.py '$EVENT_DIR' '$PROCESS' '$SAVE_LOCATION' '$REP

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/lhe_to_pandas.py'

  $COMMAND

  # submission
  #qsub -q smefit -W group_list=smefit -l nodes=1:ppn=1 -l pvmem=8000mb -l walltime=08:00:00 $COMMAND
  #rm $COMMAND

}

while getopts ":r:f:s:p:h" opt; do
  case ${opt} in
    r) echo "You chose 'r'=$OPTARG";NREP="$OPTARG";;
    f) echo "You chose 'f'=$OPTARG";ROOT="$OPTARG";;
    s) echo "You chose 's'=$OPTARG";SAVE_LOCATION="$OPTARG";;
    p) echo "You chose 'p'=$OPTARG";PROCESS="$OPTARG";;
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

#mkdir -p $SAVE_LOCATION



#for dir in $ROOT/*/     # list directories in the form "/tmp/dirname/"
#do
#    dir=${dir%*/} # remove the trailing "/"
#    #echo $dir $PROCESS $SAVE_LOCATION $NREP
#    submit_job $dir $PROCESS $SAVE_LOCATION $NREP
#done

submit_job $ROOT $PROCESS $SAVE_LOCATION $NREP

#submit_job "/data/theorie/jthoeve/ML4EFT_events/zh_sm" $PROCESS $SAVE_LOCATION $NREP

#root = sys.argv[1]
#process = sys.argv[2]
#save_root = sys.argv[3]
#n_rep = sys.argv[4]

#for ((i=0; i < $MCREPS; i++)); do
#  EVENT_FILE=$EVENT_DIR/job$(($i + 1))/Events/run_01
#  #gunzip $EVENT_FILE/unweighted_events.lhe.gz
#  submit_job $EVENT_FILE $SAVE_LOCATION $i
#done