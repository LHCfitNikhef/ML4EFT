#/bin/sh

HOMEDIR=/data/theorie/jthoeve
PY=/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python
MGbase=$PWD/MG5_aMC_v3_3_1

echo "Creating output directory..."
mkdir -p "$HOMEDIR/MGjobs/$1"
cd "$HOMEDIR/MGjobs/$1"
$PY "$MGbase/bin/mg5_aMC" "$HOMEDIR/mg5_parallel/mg5_runcards/$1"
echo "Output directory created!"