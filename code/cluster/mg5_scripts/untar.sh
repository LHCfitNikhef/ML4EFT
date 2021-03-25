#!/bin/bash

for i in {0..0}
do
	cd /data/theorie/jthoeve/mg5_copies/copy_$i/bin/process_$i/Events
	for d in */ 
	do
		#echo $PWD
    	cd $PWD/$d
    	gunzip unweighted_events.lhe.gz
    	cd ../
    	
	done
done
