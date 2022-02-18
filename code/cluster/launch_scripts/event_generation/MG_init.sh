#/bin/sh

HOMEDIR=/data/theorie/jthoeve
PY=/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python
MGbase=$PWD/MG5_aMC_v3_3_1
CUSTOMCUT=/data/theorie/jthoeve/ML4EFT_higgs/code/launch_scripts/event_generation/custom_cuts/dummy_fct.f
CUSTOMKIN=/data/theorie/jthoeve/ML4EFT_higgs/code/launch_scripts/event_generation/custom_cuts/kin_functions.f

echo "Creating output directory..."
mkdir -p "$HOMEDIR/MGjobs/$1"
cd "$HOMEDIR/MGjobs/$1"
$PY "$MGbase/bin/mg5_aMC" "$HOMEDIR/mg5_parallel/mg5_runcards/$1"

# copy custom cut to even directory
cp $CUSTOMCUT $HOMEDIR/MGjobs/$1/$1/SubProcesses/dummy_fct.f
cp $CUSTOMKIN $HOMEDIR/MGjobs/$1/$1/Source/kin_functions.f
echo "Output directory created!"