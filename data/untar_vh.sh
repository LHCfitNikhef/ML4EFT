#!/bin/bash

# this script unpacks the .lhe.gz event files.

EVENT_DIR=/Users/jaco/Documents/ML4EFT/code/MG5_aMC_v2.7.3/MG5_aMC_v2_7_3/bin/quad_cHq3_cHW/Events/
SAVE_LOCATION=/Users/jaco/Documents/ML4EFT/data/events/quad/cHq3

cd $EVENT_DIR

for i in {0..9}
do
  gunzip run_01_$i/unweighted_events.lhe.gz
  python /Users/jaco/Documents/ML4EFT/code/src/quad_clas/preproc/compute_events.py $EVENT_DIR/run_01_$i/unweighted_events.lhe $SAVE_LOCATION $i
done

