#/usr/bin/bash

mg5_path=/data/theorie/jthoeve/ML4EFT/mg5_copies
runcards_path=/data/theorie/jthoeve/ML4EFT_higgs/code/launch_scripts/mg5_runcards
runcards=(cmd_sm cmd_lin_cHq3 cmd_quad_cHq3)

for i in ${!runcards[@]}; do
  cmd=$runcards_path/${runcards[$i]}
  nohup python $mg5_path/copy_$i/bin/mg5_aMC $cmd &
done
