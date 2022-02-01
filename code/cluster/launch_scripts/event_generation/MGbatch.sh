#/bin/sh

PY=/data/theorie/jthoeve/miniconda3/envs/ml4eft/bin/python
MGbase=$HOME/mg5_parallel/MG5_aMC_v3_3_1
Base=$HOME/MGjobs
mkdir $Base

for (( i=1; i<=2; i++ ));
do

jobBase=$Base/job$i
cardBase=$jobBase/MG5_aMC_v3_3_1/bin/test_run0/Cards

mkdir $jobBase
cp -r $MGbase $jobBase

cd $jobBase

echo "#/bin/sh" >> MGscript.sh
echo "echo 'seed: $i'" >> MGscript.sh
echo "printenv" >> MGscript.sh
echo "$PY $jobBase/MG5_aMC_v3_3_1/bin/test_run0/bin/generate_events 0 run$i" >> MGscript.sh

sed -i "33s/.*/      $i       = iseed   ! rnd seed (0=assigned automatically=default))/" $jobBase/MG5_aMC_v3_3_1/bin/test_run0/Cards/run_card.dat

chmod +x MGscript.sh
qsub -q smefit -W group_list=smefit MGscript.sh

done
