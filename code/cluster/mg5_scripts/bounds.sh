#!/bin/bash

# this script moves and unpacks the .lhe.gz event files for the bound analysis

for i in {1..6}
do
  if [[ $i -ge 10 ]]
  then
    mv /data/theorie/jthoeve/ML4EFT/mg5_copies/mg5_test/bin/process_0/Events/run_$i/unweighted_events.lhe.gz /data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/cuu/eft_$i.lhe.gz
	else
    mv /data/theorie/jthoeve/ML4EFT/mg5_copies/mg5_test/bin/process_0/Events/run_0$i/unweighted_events.lhe.gz /data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/cuu/eft_$i.lhe.gz
	fi

	gunzip /data/theorie/jthoeve/ML4EFT/quad_clas/z_scores/events/cuu/eft_$i.lhe.gz

done