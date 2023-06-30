#!/bin/bash

#specify the type of shower
coeff_list="parse_sm.txt"
ppn=16
walltime="1:00:00"
zcut_beta="0.2;0.5"

template_python_file="/data/theorie/pherbsch/ML4EFT/thesis_pim/code/cluster/shower/python_template/shower_template.py"

PY='/data/theorie/pherbsch/miniconda3/envs/madgraph/bin/python'
mem=$((ppn*8))
cluster_message_err_dir="./cluster_message_output/err/"
cluster_message_output_dir="./cluster_message_output/out/"
coefficient_file_path="/data/theorie/pherbsch/ML4EFT/thesis_pim/code/cluster/shower/coefficients_lists/$coeff_list"



while IFS= read -r coefficient || [ -n "$coefficient" ]; do

    job_script="$PWD/job_${type}_${coefficient}_${zbname}.sh"
    python_file="$PWD/python_script_${type}_${coefficient}_${zbname}.py"
    
    cp $template_python_file $python_file

    # Generate the job script
    cat > $job_script <<- EOM
#!/bin/bash
#PBS -N ${type}_${coefficient}_job
#PBS -o $cluster_message_output_dir
#PBS -e $cluster_message_err_dir
#PBS -l nodes=1:ppn=${ppn}
#PBS -l vmem=${mem}gb
#PBS -l walltime=$walltime
#PBS -W group_list=smefit
#PBS -q smefit 

export OMP_STACKSIZE=16000
export OMP_NUM_THREADS=4
export KMP_BLOCKTIME=0
export KMP_AFFINITY=granularity=fine,verbose,compact,1,0

$PY $python_file $coefficient "$zcut_beta"
EOM

    chmod +x $job_script
    chmod +x $python_file
    # Submit the job script
    qsub $job_script
done < "$coefficient_file_path"

