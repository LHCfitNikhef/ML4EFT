#!/bin/bash

for i in {0..18}
do
	cd /data/theorie/jthoeve/ML4EFT/mg5_copies/copy_$i/bin/process_$i/Events
  find ./* -maxdepth 0 -type d | wc -l

#	for d in */
#	do
#		#echo $PWD
#    	cd $PWD/$d
#    	gunzip unweighted_events.lhe.gz
#    	cd ../

	#done
done
