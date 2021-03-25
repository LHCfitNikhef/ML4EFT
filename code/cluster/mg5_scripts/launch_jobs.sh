#!/bin/bash

events=43 # should be 50

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


#for i in {18..18}
#do
#	generate_processes $i & # Put a function in the background
#done

#wait 
#echo "Generated processes!"

for i in {0..17}
do
	generate_events $i $events &  # Put a function in the background
done

wait 
echo "Generated events!"


# for i in {0..0}
# do
# 	cp generate_processes.py ./MG5_aMC_process_$i/bin/
# 	cd ./MG5_aMC_process_$i/bin/
# 	python generate_processes.py $i
# 	cd ../../
# done
