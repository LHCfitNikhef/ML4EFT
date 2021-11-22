#!/bin/bash

################################################
# Script to convert lhe files to npy extension #
################################################

EVENT_DIR=/data/theorie/jthoeve/event_generation/lin_cHW/Events
SAVE_LOCATION=/data/theorie/jthoeve/event_generation/events_high_stats/lin/cHW
MCREPS=30

for ((i=0; i < $MCREPS; i++)); do
  EVENT_FILE=$EVENT_DIR/run_01_$i
  #gunzip $EVENT_FILE/unweighted_events.lhe.gz
  python /data/theorie/jthoeve/ML4EFT_higgs/code/src/quad_clas/preproc/compute_events.py $EVENT_FILE/unweighted_events.lhe $SAVE_LOCATION $i
done


#declare -a arr=("sm" "lin" "quad" "both")
#
#function create_dir() {
#
#  for i in "${arr[@]}"; do
#    #mkdir -p $SAVE_LOCATION/$i
#    for ((i=1; i <= $MCREPS; i++)); do
#      EVENT_DIR=$EVENT_DIR_ROOT/$b[]
#      gunzip run_0$i/unweighted_events.lhe.gz
#      #python /Users/jaco/Documents/ML4EFT/code/src/quad_clas/preproc/compute_events.py $EVENT_DIR/run_0$i/unweighted_events.lhe $SAVE_LOCATION $i
#    done
#  done
#}

