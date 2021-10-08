#!/bin/bash

# this script unpacks the .lhe.gz event files.

EVENT_DIR=/data/theorie/jthoeve/ML4EFT/mg5_copies/copy_0/bin/vh_cHW_linear/Events
SAVE_LOCATION=/data/theorie/jthoeve/ML4EFT_higgs/events/linear_cHW

cd $EVENT_DIR

for i in {0..1}
do
  gunzip run_01_$i/unweighted_events.lhe.gz
  python compute_events.py $EVENT_DIR/run_01_$i/unweighted_events.lhe $SAVE_LOCATION
done

