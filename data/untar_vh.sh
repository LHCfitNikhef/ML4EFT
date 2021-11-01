#!/bin/bash

# this script unpacks the .lhe.gz event files.

EVENT_DIR=/Users/jaco/Documents/ML4EFT/code/MG5_aMC_v2.7.3/MG5_aMC_v2_7_3/bin/p_value_scan_cHW_cHq3/Events
SAVE_LOCATION=/Users/jaco/Documents/ML4EFT/data/z_scores/cHW_cHq3

cd $EVENT_DIR

for i in {1..3}
do
  gunzip run_0$i/unweighted_events.lhe.gz
  python /Users/jaco/Documents/ML4EFT/code/src/quad_clas/preproc/compute_events.py $EVENT_DIR/run_0$i/unweighted_events.lhe $SAVE_LOCATION $i
done

