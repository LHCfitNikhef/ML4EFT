#!/bin/bash

PY='/data/theorie/pherbsch/miniconda3/envs/madgraph/bin/python'
# RUN_CARD_PATH=""


function submit_job () {

  RUN_CARD=$1
  REP=$2
  COEFF=$3
  PY_INIT=$4

  # create bash file to submit
  COMMAND=$PWD'/launch_rep_'$COEFF'_'$REP'_'$(date +%Y%m%d_%H%M%S)'.sh'

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/theorie/pherbsch/miniconda3/lib;'$PY' '$PWD'/'$PY_INIT' '$RUN_CARD' '$REP' '$COEFF

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/training_init.py'

  # submission
  # qsub -q short -l walltime=04:00:00 -l nodes=1:ppn=1 -l pvmem=4000mb $COMMAND
  # qsub -q generic -l walltime=04:00:00 -l nodes=1:ppn=1 -l pvmem=4000mb $COMMAND
  qsub -q smefit -W group_list=smefit -l walltime=04:00:00 -l nodes=1:ppn=1 -l pvmem=4gb $COMMAND
  rm $COMMAND

}

# SETUP
MCREPS=25
RUN_CARD="/data/theorie/pherbsch/ML4EFT/thesis_pim/code/cluster/training/runcards/lin_2feat_event.json"
PY_INIT="training_init.py"
# coeff=("cQj38_cQj38" "ctj8_ctj8" "cQj18_cQj38") #quad 18 feat event
#change output path of py_init file
#check if the runcard is correct

# Specify which coefficients you want to train neural networks on:
coeff=("cQd8" "cQd8_ctGRe" "cQj18_cQu8" "cQj38" "cQj38_ctj8" "cQu8_ctj8" "ctd8_ctj8" "ctj8" "cQd8_cQd8" "cQd8_ctj8" "cQj18_ctd8" "cQj38_cQj38" "cQj38_ctu8" "cQu8_ctu8" "ctGRe" "ctj8_ctj8" "cQd8_cQj18" "cQj18" "cQj18_ctGRe" "cQj38_cQu8" "cQu8" "ctd8" "ctGRe_ctGRe" "ctj8_ctu8" "cQd8_cQj38" "cQj18_cQj18" "cQj18_ctj8" "cQj38_ctd8" "ctd8_ctd8" "ctGRe_ctj8" "ctu8" "cQd8_ctd8" "cQj18_cQj38" "cQj18_ctu8" "cQj38_ctGRe" "cQu8_ctGRe" "ctd8_ctGRe" "ctGRe_ctu8" "ctu8_ctu8")
# coeff=("cQu8_cQu8")
# coeff=("cQj18" "ctd8" "ctGRe" "ctj8" "cQu8")
# coeff=("cQu8_ctu8" "cQj18_ctGRe") # quad 2 feat event
# coeff=("cQj18_ctGRe") #quad 2 feat hard



for c in "${coeff[@]}"
do
  for ((rep=0; rep < $MCREPS; rep++)); do
    submit_job "$RUN_CARD" $rep $c $PY_INIT
  done
done