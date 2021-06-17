# Author: Jaco ter Hoeve
# This file should be copied to /bin inside each madgraph copy in order to generate events.
# Input:
#	process_number: labels the process, e.g. cuu = 1 and cugre = 5
#	number of runs: number of mc toy experiments to generate

import sys, subprocess

# Get the number of runs from the command-line argument
process_number = int(sys.argv[1]) 
number_of_runs = int(sys.argv[2]) # should be 50

#subprocess.call('export PATH=$PATH:/data/theorie/jthoeve/MG5_aMC_v3_0_0/HEPTools/lhapdf6/bin', shell=True)

for i in range(0, number_of_runs):
	path_events = './process_{}/bin/generate_events'.format(process_number)
	subprocess.call([path_events, '-f', '--cluster'])	
print('INFO: Events generated.')
