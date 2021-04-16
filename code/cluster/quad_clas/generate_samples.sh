#!/bin/bash

cugre="$1"
cuu="$2"
MY_FILE='/data/theorie/jthoeve/ML4EFT/mg5_copies/mg5_test/bin/run_commands'
> "$MY_FILE"
echo 'launch process_0' >> $MY_FILE
echo 'set nevents 1000' >> $MY_FILE
echo "set cugre $1"  >> "$MY_FILE"
echo "set cuu $2" >> "$MY_FILE"

#python /data/theorie/jthoeve/ML4EFT/mg5_copies/mg5_test/bin/mg5_aMC $MY_FILE
