import sys, subprocess

# Get the number of runs from the command-line argument
process_number = int(sys.argv[1])

text = """
import model SMEFTsim_U35_MwScheme_UFO
generate g g > t t~ NP=1 /a z h h1 w+ w- w1+ w1- z1 t1
add process u u~ > t t~ NP=1 /a z h h1 w+ w- w1+ w1- z1 t1
add process d d~ > t t~ NP=1 /a z h h1 w+ w- w1+ w1- z1 t1
add process c c~ > t t~ NP=1 /a z h h1 w+ w- w1+ w1- z1 t1
add process s s~ > t t~ NP=1 /a z h h1 w+ w- w1+ w1- z1 t1
add process b b~ > t t~ NP=1 /a z h h1 w+ w- w1+ w1- z1 t1

output process_{}
"""

subprocess.call('export PATH=$PATH:/data/theorie/jthoeve/MG5_aMC_v3_0_0/HEPTools/lhapdf6/bin', shell=True)

# 18 eft + 1 sm = 19
eft_points = [[-2.0, 0], [-1.0, 0], [-0.5, 0], [0.5, 0], [1.0, 0], [2.0, 0], [0, -2.0], [0, -1.0], [0, -0.5],[0, 0.5], [0, 1.0], [0, 2.0], [-2.0, -2.0], [-1.0, -1.0], [-0.5, -0.5], [0.5, 0.5], [1.0, 1.0],[2.0, 2.0], [0.0, 0.0]]
eft_param = eft_points[process_number]

# write a process generating card
with open ('run_script_{}.txt'.format(process_number), 'w') as rs:
	rs.write(text.format(process_number))
  	
subprocess.call(['./mg5_aMC', 'run_script_{}.txt'.format(process_number)])
	
print 'INFO: Events folder generated.'

# copy run/param cards to each event folder

cugre, cuu = eft_param
# open parameter card
with open('./cards/param_card.dat', 'r') as file:
	data = file.readlines()
# update EFT parameters
data[54] = "      15 {} # cugre\n".format(cugre)
data[77] = "      38 {} # cuu\n".format(cuu)
# update parameter card
with open('./cards/param_card_copy.dat', 'w') as file:
	file.writelines(data)

run_card_path = './cards/run_card.dat'
param_card_path = './cards/param_card_copy.dat'
dest = './process_{}/Cards/'.format(process_number)
dest_param = dest + 'param_card.dat'
subprocess.call(['cp', run_card_path, dest])
subprocess.call(['cp', param_card_path, dest])
subprocess.call(['mv', '-f', param_card_path, dest_param])

print 'INFO: run/param cards copied.'
