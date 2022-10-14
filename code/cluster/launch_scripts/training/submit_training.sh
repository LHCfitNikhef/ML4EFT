#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'

function submit_job () {

  RUN_CARD=$1
  REP=$2
  COEFF=$3

  # create bash file to submit
  COMMAND=$PWD'/launch_rep_'$COEFF'_'$REP'.sh'

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/theorie/jthoeve/miniconda3/lib;'$PY' '$PWD'/training_init.py '$RUN_CARD' '$REP

  echo $LAUNCH >> $COMMAND
  chmod +x $COMMAND
  chmod +x $PWD'/training_init.py'

  # submission
  qsub -q short7 -W group_list=theorie -l nodes=1:ppn=1 -l pvmem=4000mb $COMMAND
  rm $COMMAND

}

# SETUP

MCREPS=1

# zh -> llbb

#RUN_CARD_ROOT="/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/zh_llbb_pt_z/run_card_zh_llbb_"

#coeff=( "cHu" "cHd" "cHj1" "cHj3" "cbHRe" "cHW" "cHWB")

#coeff=( "cHu_cHu" "cHu_cbHRe" "cHu_cHW" "cHu_cHWB" "cHd_cHd" "cHd_cbHRe" "cHd_cHW" "cHd_cHWB" "cHj1_cHj1" "cHj1_cHj3" "cHj1_cbHRe"
#"cHj1_cHW" "cHj1_cHWB" "cHj3_cHj3" "cHj3_cbHRe" "cHj3_cHW" "cHj3_cHWB" "cHj3_cHWB" "cbHRe_cbHRe" "cbHRe_cHW" "cbHRe_cHWB"
#"cHW_cHW" "cHW_cHWB" "cHWB_cHWB")

# tt -> llvlvlbb

RUN_CARD_ROOT="/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/code/cluster/launch_scripts/run_cards/tt_llvlvlbb_pt_ll_eta_l/run_card_tt_llvlvlbb_"
coeff=( "cQd8")
#coeff=( "ctGRe")

#coeff=( "cQd8_cQd8" "cQd8_cQj18" "cQd8_cQj38" "cQd8_ctd8" "cQd8_ctGRe" "cQd8_ctj8" "cQj18_cQj18" "cQj18_cQj38" "cQj18_cQu8" "cQj18_ctd8"
#"cQj18_ctGRe" "cQj18_ctj8" "cQj18_ctu8" "cQj38_cQj38" "cQj38_cQu8" "cQj38_ctd8" "cQj38_ctGRe" "cQj38_ctj8" "cQj38_ctu8" "cQu8_cQu8" "cQu8_ctGRe"
#"cQu8_ctj8" "cQu8_ctu8" "ctd8_ctd8" "ctd8_ctGRe" "ctd8_ctj8" "ctGRe_ctGRe" "ctGRe_ctj8" "ctGRe_ctu8" "ctj8_ctj8" "ctj8_ctu8" "ctu8_ctu8")

for c in "${coeff[@]}"
do
  for ((rep=0; rep < $MCREPS; rep++)); do
    submit_job $RUN_CARD_ROOT$c".json" $rep $c
  done
done
