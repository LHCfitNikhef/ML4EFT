#!/bin/bash

PY='/data/theorie/pherbsch/miniconda3/envs/madgraph/bin/python'

# It's important to change the fit_id for the posteriors, otherwise we'll get no results, so this prompt is important
echo "Did you change the fit_id in the runcard? (yes/no):"
read user_input

# Make the input case-insensitive (convert to lowercase)
user_input=$(echo "$user_input" | tr '[:upper:]' '[:lower:]')

# Check the user's answer
if [ "$user_input" = "yes" ]; then
  # The user wants to continue

  echo "Continuing the script..."

  # The rest of your script goes here...

else
  # The user doesn't want to continue

  echo "Stopping the script."
  exit 0
fi

function submit_job () {

  NCORES=$1
  FIT_ID=$2
  COEFF1=$3
  COEFF2=$4
  COEFF3=$5
  COEFF4=$6
  COEFF5=$7

  TIMESTAMP=$(date +%Y%m%d_%H%M%S)
  OPTIMIZE_RUNNER=$PWD"/optimize_runner_$TIMESTAMP.py"

  # create Python file to submit
  cat > $OPTIMIZE_RUNNER <<- EOM
import argparse
import json
from ml4eft.limits.optimize_ns import Optimize

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--fit_cards",
        required=True,
        type=str,
        help="fit card"
    )

    parser.add_argument(
        "-c",
        "--coeff",
        required=False,
        type=str,
        nargs = "*",
        help="subset of operators to include"
    )

    args = parser.parse_args()

    with open(args.fit_cards) as json_data:
        config = json.load(json_data)

    runner = Optimize(config, coeff=args.coeff)
    runner.run_sampling()
EOM

  chmod +x $OPTIMIZE_RUNNER

  # create bash file to submit
  COMMAND=$PWD"/launch_ns_$TIMESTAMP.sh"

  # _$(date +%Y%m%d_%H%M%S)
  # for 5 linear coefficients
  ARGS="-f $FIT_ID -c $COEFF1 $COEFF2 $COEFF3 $COEFF4 $COEFF5"
  # ARGS="-f $FIT_ID"


  # for pairwise fits
  # ARGS='-f '$FIT_ID' -c '$COEFF1' '$COEFF2'

  # write launch command
  LAUNCH=$PY' '$OPTIMIZE_RUNNER' '$ARGS

  echo $LAUNCH >> $COMMAND

  chmod +x $COMMAND
  # chmod +x $PWD'/optimize_runner.py'

  # submission
  # cat $COMMAND
  # qsub -q short -l nodes=1:ppn=$NCORES -l walltime=01:00:00 $COMMAND
  qsub -q smefit -W group_list=smefit -l nodes=1:ppn=$NCORES -l vmem=160gb -l walltime=20:00:00 $COMMAND
  rm $COMMAND

  # removing the created python file
  # rm $OPTIMIZE_RUNNER
}


# SETUP
NCORES='16'
FID_ID=$PWD'/run_cards/lin_2feat_event_binned.json'

# # global fit
# submit_job $NCORES $FID_ID

#check runcard

# selection of operators
submit_job $NCORES $FID_ID "ctd8" "cQj18" "cQu8" "ctj8" "ctGRe"

#pair-wise fit

# tt
# set -- "cQd8" "cQj18" "cQj38" "cQu8" "ctd8" "ctGRe" "ctj8" "ctu8"

#for a; do
#    shift
#    for b; do
#      submit_job $NCORES $FID_ID $a $b
#    done
#done

