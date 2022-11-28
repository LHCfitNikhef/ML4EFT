#!/bin/sh
export OMP_STACKSIZE=16000
export OMP_NUM_THREADS=4
export KMP_BLOCKTIME=0
export KMP_AFFINITY=granularity=fine,verbose,compact,1,0

python /data/theorie/pherbsch/ML4EFT/subproj/code/cluster/nn_ctu8_ctu8.py
python /data/theorie/pherbsch/ML4EFT/subproj/code/cluster/nn_ctu8.py