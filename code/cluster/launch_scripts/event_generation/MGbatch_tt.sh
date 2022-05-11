#/bin/sh

HOMEDIR=/data/theorie/jthoeve
PY=/data/theorie/jthoeve/miniconda3/envs/mg5/bin/python
#MGbase=$PWD/MG5_aMC_v3_3_2
Base=$HOMEDIR/MGjobs
mkdir -p $Base

#chdd=(0 10)

for (( i=1; i<=50; i++ ));
do

# $1 is given as input by the usr: the output name dir
jobBase="$Base/$1/job$i"

mkdir -p $jobBase
cp -r $Base/$1/$1/. $jobBase

cd $jobBase

# create the launch script
echo "#/bin/sh" >> MGscript.sh
#echo "echo 'seed: $i'" >> MGscript.sh
echo "$PY $jobBase/bin/madevent $jobBase/cmd" >> MGscript.sh

# create the run file
echo "launch" >> cmd
echo "0" >> cmd
echo "set pdlabel lhapdf" >> cmd
echo "set lhaid 315000" >> cmd
#echo "set ${op[]} ${chdd[i-1]}" >> cmd
echo "set cugre -2" >> cmd
echo "set nevents 100k" >> cmd
echo "set ebeam1 7000" >> cmd
echo "set ebeam2 7000" >> cmd
echo "set use_syst False" >> cmd
echo "set iseed $((1 + $RANDOM % 200))" >> cmd
echo "set fixed_ren_scale True" >> cmd
echo "set fixed_fac_scale True" >> cmd
#echo "set cut_decays True" >> cmd
#echo "set scale 125" >> cmd
#echo "set dsqrt_q2fact1 125" >> cmd
#echo "set dsqrt_q2fact2 125" >> cmd

# cuts
#echo "set pt_min_pdg {5: 45}" >> cmd
#echo "set mxx_min_pdg {5: 115}" >> cmd
#echo "set ptllmin 75" >> cmd
##echo "set pt_max_pdg {23: 150}" >> cmd
#echo "set mmll 81" >> cmd
#echo "set mmllmax 101" >> cmd
#echo "set mmjj 115" >> cmd
#echo "set mmjjmax 135" >> cmd
#echo "set ptl1min 27" >> cmd
#echo "set ptl2min 7" >> cmd
#echo "set hard_process True" >> cmd


# add executable rights
chmod +x MGscript.sh

# submit to queue
qsub -q short7 -W group_list=theorie -l nodes=1:ppn=4 MGscript.sh

done
