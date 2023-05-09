#!/bin/bash

PY='/data/theorie/pherbsch/miniconda3/envs/madgraph/bin/python'

function submit_job () { 


    COEF=$1
    ZCUT_BETA=$2

    # create bash file to submit
    COMMAND=$PWD'/launch_'$coef'_'$ZCUT_BETA'.sh'

    #write launch command
    LAUNCH='export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/theorie/pherbsch/miniconda3/lib;'$PY' '$PWD'/shower.py '$COEF' '$ZCUT_BETA

    # echo "export OMP_STACKSIZE=16000" >> $COMMAND
    # echo "export OMP_NUM_THREADS=4" >> $COMMAND
    # echo "export KMP_BLOCKTIME=0" >> $COMMAND
    # echo "export KMP_AFFINITY=granularity=fine,verbose,compact,1,0" >> $COMMAND
    echo $LAUNCH >> $COMMAND
    chmod +x $COMMAND
    chmod +x $PWD'/shower.py'

    # submission
    ./launch_$coef'_'$ZCUT_BETA'.sh'
    # qsub -q short -l walltime=00:10:00 -l nodes=1:ppn=1 -l pvmem=4000mb $COMMAND

    # rm $COMMAND
}

# SETUP
#MCREPS is also in the runcard, so make sure to change both. At some point make this better
# MCREPS=3

coeff=("ctu8")
zcut_beta="0.2;0.5"

for c in "${coeff[@]}"
do
  submit_job $c "$zcut_beta"
done