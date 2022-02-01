#!/bin/bash

################################################
# Script to convert lhe files to npy extension #
################################################

EVENT_DIR=/data/theorie/jthoeve/event_generation/quad_only_cHq3/Events
SAVE_LOCATION=/data/theorie/jthoeve/event_generation/events_high_stats/quad_only/cHq3
MCREPS=1

for ((i=0; i < $MCREPS; i++)); do
  EVENT_FILE=$EVENT_DIR/run_01_$i
  gunzip $EVENT_FILE/unweighted_events.lhe.gz
  python /data/theorie/jthoeve/ML4EFT_higgs/code/src/quad_clas/preproc/compute_events.py $EVENT_FILE/unweighted_events.lhe $SAVE_LOCATION $i
done


