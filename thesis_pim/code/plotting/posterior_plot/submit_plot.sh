#!/bin/bash

# plot1
# order="lin"

# data1="/data/theorie/pherbsch/l2f/nn_h2/posterior.json"
# data2="/data/theorie/pherbsch/l2f/nn_Ev2/posterior.json"
# data3='None'

# label1="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Hadron}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label3="label3"

# name=1$order"2feat_particle_vs_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # plot2
# order="lin"

# data1="/data/theorie/pherbsch/l18f/nn_h/posterior.json"
# data2="/data/theorie/pherbsch/l18f/nn_Ev/posterior.json"
# data3='None'

# label1="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(18\;\mathrm{features})"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Hadron}\; \mathrm{level} \;(18\;\mathrm{features})"
# label3="label3"

# name=2$order"18feat_particle_vs_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # plot3
# order="quad"

# data1="/data/theorie/pherbsch/q2f/nn_h/posterior.json"
# data2="/data/theorie/pherbsch/q2f/nn_Ev/posterior.json"
# data3='None'

# label1="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Hadron}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label3="label3"

# name=3$order"2feat_particle_vs_nn_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # # plot4
# order="quad"

# data1="/data/theorie/pherbsch/q18f/nn_h/posterior.json"
# data2="/data/theorie/pherbsch/q18f/nn_Ev/posterior.json"
# data3='None'

# label1="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle} \; \mathrm{level} \;(18\;\mathrm{features})"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Hadron} \; \mathrm{level} \; (18\;\mathrm{features})"
# label3="label3"

# name=4$order"18feat_nn_particle_vs_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# plot5
# order="lin"

# data1="/data/theorie/pherbsch/l2f/binned_Ev2/posterior.json"
# data2="/data/theorie/pherbsch/l2f/nn_Ev2/posterior.json"
# data3='None'

# label1="\mathrm{Binned} \; \mathrm{Hadron} \; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label3="label3"

# name=5$order"2feat_binned_vs_nn_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# plot6
# order="lin"

# data1="/data/theorie/pherbsch/l2f/nn_Ev2/posterior.json"
# data2="/data/theorie/pherbsch/l18f/nn_Ev/posterior.json"
# data3='None'

# label1="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(18\;\mathrm{features})"
# label3="label3"

# name=6$order"2feat_vs_18feat_nn_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # plot7
# order="quad"

# data1="/data/theorie/pherbsch/q2f/binned_Ev/posterior.json"
# data2="/data/theorie/pherbsch/q2f/nn_Ev/posterior.json"
# data3='None'

# label1="\mathrm{Binned} \; \mathrm{Hadron} \; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label3="label3"

# name=7$order"2feat_binned_vs_nn_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # plot8
# order="quad"

# data1="/data/theorie/pherbsch/q2f/nn_Ev/posterior.json"
# data2="/data/theorie/pherbsch/q18f/nn_Ev/posterior.json"
# data3='None'

# label1="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(18\;\mathrm{features})"
# label3="label3"

# name=8$order"2feat_vs_18feat_nn_hadron"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # plot9
# order="lin"

# data1="/data/theorie/pherbsch/jaco_posteriors/posterior_samples/tt_llvlvlbb/nn_glob_lin_pt_ll_eta_l/posterior.json"
# data2="/data/theorie/pherbsch/l2f/nn_h2/posterior.json"
# data3='None'

# label1="\mathrm{Validation} \; \mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label3="label3"

# name=9$order"2feat_ambrosio_particle_vs_my_particle"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # # plot10
# order="lin"

# data1="/data/theorie/pherbsch/jaco_posteriors/posterior_samples/tt_llvlvlbb/nn_glob_lin_all/posterior.json"
# data2="/data/theorie/pherbsch/l18f/nn_h/posterior.json"
# data3='None'

# label1="\mathrm{Validation} \; \mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level}\;(18\;\mathrm{features})"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(18\;\mathrm{features})"
# label3="label3"

# name=10$order"18feat_ambrosio_particle_vs_my_particle"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # plot11
# order="quad"

# data1="/data/theorie/pherbsch/jaco_posteriors/posterior_samples/tt_llvlvlbb/nn_glob_quad_pt_ll_eta_l/posterior.json"
# data2="/data/theorie/pherbsch/q2f/nn_h/posterior.json"
# data3='None'

# label1="\mathrm{Validation} \; \mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# label3="label3"

# name=11$order"2feat_ambrosio_vs_my_particle"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# # plot12
# order="quad"

# data1="/data/theorie/pherbsch/jaco_posteriors/posterior_samples/tt_llvlvlbb/nn_glob_quad_all/posterior.json"
# data2="/data/theorie/pherbsch/q18f/nn_h/posterior.json"
# data3='None'

# label1="\mathrm{Validation} \; \mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level}\;(18\;\mathrm{features})"
# label2="\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(18\;\mathrm{features})"
# label3="label3"

# name=12$order"18feat_ambrosio_vs_my_particle"

# loc="/data/theorie/pherbsch/ML4EFT/subproj/output/plots/posterior/"

# save_loc=$loc$name".png"

# store handy expressions
# particle level
# "\mathrm{Particle}\; \mathrm{level} \;\mathrm{binned}\;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# "\mathrm{Particle}\; \mathrm{level} \;\mathrm{binned}\;(18\;\mathrm{features})"
# "\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# "\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(18\;\mathrm{features})"

# "\mathrm{Binned} \; \mathrm{Hadron} \; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# "\mathrm{Binned} \; \mathrm{Hadron} \; \mathrm{level} \;(18\;\mathrm{features})"
# "\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(p_T^{\ell\bar{\ell}}, \eta_\ell)"
# "\mathrm{Unbinned} \; \mathrm{ML} \; \mathrm{Particle}\; \mathrm{level} \;(18\;\mathrm{features})"




template_python_file="/data/theorie/pherbsch/ML4EFT/subproj/code/plotting/posterior_plot/template_py_files/posterior_plot.py"
PY='/data/theorie/pherbsch/miniconda3/envs/madgraph/bin/python'
ellipse_plotter_new='/data/theorie/pherbsch/ML4EFT/subproj/code/plotting/'
ppn=2
walltime="00:20:00"
mem=$((ppn*8))
cluster_message_output_dir="/data/theorie/pherbsch/ML4EFT/subproj/code/plotting/posterior_plot/cluster_message_output"
color1='C1'
color2='C2'
color3='C3'



job_script="$PWD/job_${type}_${name}.sh"
python_file="$PWD/python_script_${type}_${name}.py"

cp $template_python_file $python_file

# run on the cluster
# Generate the job script
cat > $job_script <<- EOM
#!/bin/bash
#PBS -N ${type}_${name}_job
#PBS -o $cluster_message_output_dir
#PBS -e $cluster_message_output_dir
#PBS -l nodes=1:ppn=${ppn}
#PBS -l vmem=${mem}gb
#PBS -l walltime=$walltime
#PBS -W group_list=smefit
#PBS -q smefit 

export OMP_STACKSIZE=16000
export OMP_NUM_THREADS=4
export KMP_BLOCKTIME=0
export KMP_AFFINITY=granularity=fine,verbose,compact,1,0

export PYTHONPATH="$PYTHONPATH:$ellipse_plotter_new"
"$PY" "$python_file" "$order" "$data1" "$data2" "$data3" "$label1" "$label2" "$label3" "$color1" "$color2" "$color3" "$save_loc"
EOM

chmod +x $job_script
chmod +x $python_file
# Submit the job script
qsub $job_script

# end cluster run code


# #run in interactive terminal
# chmod +x $python_file

# export PYTHONPATH="$PYTHONPATH:$ellipse_plotter_new"
# "$PY" "$python_file" "$order" "$data1" "$data2" "$data3" "$label1" "$label2" "$label3" "$color1" "$color2" "$color3" "$save_loc"
