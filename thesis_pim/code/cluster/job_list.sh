#!/bin/sh
export OMP_STACKSIZE=16000
export OMP_NUM_THREADS=4
export KMP_BLOCKTIME=0
export KMP_AFFINITY=granularity=fine,verbose,compact,1,0

coefficient="$1"
zcut_beta="$2"
# coefficient="$coefficient"
# zcut_beta="$zcut_beta"

# echo "Executing command: python /data/theorie/pherbsch/ML4EFT/subproj/code/w_runcard_lhe_parser.py $coefficient $zcut_beta"
python /data/theorie/pherbsch/ML4EFT/subproj/code/w_runcard_lhe_parser.py $coefficient $zcut_beta
