#!/bin/bash

# script to remove all madgraph events automatically

for i in {0..18}
do
	cd /data/theorie/jthoeve/mg5_copies/copy_$i/bin/process_$i/Events
	rm -rf run_*
done