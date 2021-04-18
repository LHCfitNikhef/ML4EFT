#!/bin/bash

# This script copies madgraph (to make parallel runs possible), generates processes and events.

events=50

copy_madgraph(){
 cp -r ../MG5_aMC_v3_0_0/ ../mg5_copies/copy_$i
}

generate_processes(){
	cp generate_processes.py ../mg5_copies/copy_$i/bin/
	cd ../mg5_copies/copy_$i/bin/
	python generate_processes.py $i
	cd ../../../mg5_scripts	
}

generate_events(){
	cp generate_events.py ../mg5_copies/copy_$i/bin/
	cd ../mg5_copies/copy_$i/bin/
	python generate_events.py $i $events
	cd ../../
}

for i in {0..18}
do
  copy_madgraph $i &
done

wait
echo "Copied MadGraph!"

for i in {0..18}
do
	generate_processes $i & # Put a function in the background
done

wait
echo "Generated processes!"

for i in {0..18}
do
	generate_events $i $events &  # Put a function in the background
done

wait
echo "Generated events!"