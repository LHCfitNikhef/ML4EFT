#/bin/sh

HOMEDIR=/data/theorie/jthoeve
PY=/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python
#MGbase=$PWD/MG5_aMC_v3_3_1
Base=$HOMEDIR/MGjobs
mkdir -p $Base

for (( i=1; i<=2; i++ ));
do

jobBase="$Base/$1/job$i"
# $1 is given as input by the usr: the output name dir
#cardBase=$jobBase/MG5_aMC_v3_3_1/$1/Cards

mkdir -p $jobBase
cp -r $Base/$1/$1/. $jobBase

cd $jobBase

# create the launch script
echo "#/bin/sh" >> MGscript.sh
echo "echo 'seed: $i'" >> MGscript.sh
echo "$PY $jobBase/bin/madevent $jobBase/cmd" >> MGscript.sh

# create the run file
echo "launch" >> cmd
echo "0" >> cmd
echo "set chdd 10" >> cmd
echo "set nevents 1000" >> cmd
echo "set ebeam1 7000" >> cmd
echo "set ebeam2 7000" >> cmd
echo "set use_syst False" >> cmd
echo "set iseed $i"

#sed -i "33s/.*/      $i       = iseed   ! rnd seed (0=assigned automatically=default))/" $jobBase/MG5_aMC_v3_3_1/bin/test_run0/Cards/run_card.dat

chmod +x MGscript.sh
qsub -q smefit -W group_list=smefit MGscript.sh

done
