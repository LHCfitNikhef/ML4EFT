#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/eels_kk/bin/python'

function submit_job () {

  RUN_CARD=$1
  REP=$2
  COEFF=$3

  # create bash file to submit
  COMMAND=$PWD'/launch_rep_'$COEFF'_'$REP'.sh'

  # write launch command
  LAUNCH=$PY' '$PWD'/training_init.py '$RUN_CARD' '$REP

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/training_init.py'

  # submission
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=1 -l pvmem=8000mb -l walltime=08:00:00 $COMMAND
  rm $COMMAND

}

# SETUP
RUN_CARD_ROOT="/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/zh_llbb_pt_z/run_card_zh_llbb_"
MCREPS=50

coeff=( "cHu" "cHd" "cHj1" "cHj3" "cbHRe" "cHW" "cHWB")

#coeff=( "cHu_cHu" "cHu_cbHRe" "cHu_cHW" "cHu_cHWB" "cHd_cHd" "cHd_cbHRe" "cHd_cHW" "cHd_cHWB" "cHj1_cHj1" "cHj1_cHj3" "cHj1_cbHRe"
#"cHj1_cHW" "cHj1_cHWB" "cHj3_cHj3" "cHj3_cbHRe" "cHj3_cHW" "cHj3_cHWB" "cHj3_cHWB" "cbHRe_cbHRe" "cbHRe_cHW" "cbHRe_cHWB"
#"cHW_cHW" "cHW_cHWB" "cHWB_cHWB")

for c in "${coeff[@]}"
do
  for ((rep=0; rep < $MCREPS; rep++)); do
    submit_job $RUN_CARD_ROOT$c".json" $rep $c
  done
done
