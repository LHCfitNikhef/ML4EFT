#!/bin/bash

PY='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python'
MULTINEST='data/theorie/jthoeve/miniconda3/lib:$LD_LIBRARY_PATH'
MPI='/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/mpiexec'

function submit_job () {

  NCORES=$1
  FIT_ID=$2
  COEFF1=$3
  COEFF2=$4
  COEFF3=$5
  COEFF4=$6
  COEFF5=$7


  # create bash file to submit
  COMMAND=$PWD'/launch_ns.sh'

  # for 5 linear coefficients
  ARGS='-f '$FIT_ID ' -c '$COEFF1' '$COEFF2' '$COEFF3' '$COEFF4' '$COEFF5

  # for pairwise fits
  # ARGS='-f '$FIT_ID' -c '$COEFF1' '$COEFF2'

  # write launch command
  LAUNCH='export LD_LIBRARY_PATH='$MULTINEST';'$MPI' -n '$NCORES' '$PY' '$PWD'/optimize_runner.py '$ARGS
  echo $LAUNCH >> $COMMAND

  chmod +x $COMMAND
  chmod +x $PWD'/optimize_runner.py'

  # submission
  qsub -q short -l nodes=1:ppn=$NCORES -l walltime=01:00:00 $COMMAND
  # qsub -q smefit -W group_list=smefit -l nodes=1:ppn=$NCORES -l walltime=24:00:00 $COMMAND
  rm $COMMAND

}

# SETUP
NCORES='8'
FID_ID=$PWD'/data/theorie/pherbsch/ML4EFT/code/cluster/limits/run_cards/lin_posteriors.json'

# global fit
# submit_job $NCORES $FID_ID

# selection of operators
submit_job $NCORES $FID_ID ctd8 cQj18 cQu8 ctj8 ctGRe

#pair-wise fit

# tt
# set -- "cQd8" "cQj18" "cQj38" "cQu8" "ctd8" "ctGRe" "ctj8" "ctu8"

#for a; do
#    shift
#    for b; do
#      submit_job $NCORES $FID_ID $a $b
#    done
#done