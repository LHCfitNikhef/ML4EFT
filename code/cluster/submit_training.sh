#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'
LD_LIBRARY='/data/theorie/jthoeve/miniconda3/lib'

function submit_job () {

  RUN_CARD=$1
  REP=$2
  COEFF=$3

  # create bash file to submit
  COMMAND=$PWD'/launch_rep_'$COEFF'_'$REP'.sh'

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LD_LIBRARY;'$PY' '$PWD'/training_init.py '$RUN_CARD' '$REP' '$COEFF

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/training_init.py'

  # submission
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=1 -l pvmem=4000mb $COMMAND
  rm $COMMAND

}

# SETUP

MCREPS=25

# tt -> llvlvlbb

RUN_CARD="./run_card_tt_llvlvlbb_all.json"

coeff=( "cQd8" "cQj18" "cQj38" "cQu8" "ctd8" "ctGRe" "ctj8" "ctu8" "cQd8_cQd8" "cQd8_cQj18" "cQd8_cQj38" "cQd8_ctd8" "cQd8_ctGRe" "cQd8_ctj8" "cQj18_cQj18" "cQj18_cQj38" "cQj18_cQu8" "cQj18_ctd8"
"cQj18_ctGRe" "cQj18_ctj8" "cQj18_ctu8" "cQj38_cQj38" "cQj38_cQu8" "cQj38_ctd8" "cQj38_ctGRe" "cQj38_ctj8" "cQj38_ctu8" "cQu8_cQu8" "cQu8_ctGRe"
"cQu8_ctj8" "cQu8_ctu8" "ctd8_ctd8" "ctd8_ctGRe" "ctd8_ctj8" "ctGRe_ctGRe" "ctGRe_ctj8" "ctGRe_ctu8" "ctj8_ctj8" "ctj8_ctu8" "ctu8_ctu8")

for c in "${coeff[@]}"
do
  for ((rep=0; rep < $MCREPS; rep++)); do
    submit_job $RUN_CARD $rep $c
  done
done