#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'
MULTINEST='data/theorie/jthoeve/miniconda3/lib:$LD_LIBRARY_PATH'
MPI='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/mpiexec'

function submit_job () {

  NCORES=$1
  FIT_ID=$2
  COEFF1=$3
  COEFF2=$4

  # create bash file to submit
  COMMAND=$PWD'/launch_ns.sh'

  ARGS='-f '$FIT_ID' -c '$COEFF1' '$COEFF2

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH='$MULTINEST';'$MPI' -n '$NCORES' '$PY' '$PWD'/optimize_runner.py '$ARGS
  echo $LAUNCH >> $COMMAND

  chmod +x $COMMAND
  chmod +x $PWD'/optimize_runner.py'

  # submission
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=$NCORES -l pvmem=8000mb -l walltime=06:00:00 $COMMAND
  rm $COMMAND

}

# SETUP
NCORES='4'
FID_ID=$PWD'/run_cards/NS_run_card_zhllbb.json'

coeff=( "cHu" "cHd" "cHj1" "cHj3" "cbHRe" "cHW" "cHWB")

#coeff=( "cHu_cHu" "cHu_cbHRe" "cHu_cHW" "cHu_cHWB" "cHd_cHd" "cHd_cbHRe" "cHd_cHW" "cHd_cHWB" "cHj1_cHj1" "cHj1_cHj3" "cHj1_cbHRe"
#"cHj1_cHW" "cHj1_cHWB" "cHj3_cHj3" "cHj3_cbHRe" "cHj3_cHW" "cHj3_cHWB" "cHj3_cHWB" "cbHRe_cbHRe" "cbHRe_cHW" "cbHRe_cHWB"
#"cHW_cHW" "cHW_cHWB" "cHWB_cHWB")

set -- "cHu" "cHd" "cHj1" "cHj3" "cbHRe" "cHW" "cHWB"
for a; do
    shift
    for b; do
      submit_job $NCORES $FID_ID $a $b
    done
done

#for c in "${coeff[@]}"
#do
#  for ((rep=0; rep < $MCREPS; rep++)); do
#    submit_job $NCORES $FID_ID $COEFF1 $COEFF2
#  done
#done



