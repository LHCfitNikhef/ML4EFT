#!/bin/bash

# this script unpacks the .lhe.gz event files.

for i in {0..18}
do
	cd /data/theorie/jthoeve/ML4EFT/mg5_copies/copy_$i/bin/process_$i/Events
  #find ./* -maxdepth 0 -type d | wc -l
  for d in */
	do
    	cd $PWD/$d
    	gunzip unweighted_events.lhe.gz
    	cd ../
	done
done
