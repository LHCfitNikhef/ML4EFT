import sys, subprocess

# Get the number of runs from the command-line argument
process_number = int(sys.argv[1]) 
number_of_runs = int(sys.argv[2]) # should be 50

#subprocess.call('export PATH=$PATH:/data/theorie/jthoeve/MG5_aMC_v3_0_0/HEPTools/lhapdf6/bin', shell=True)

for i in range(0, number_of_runs):
	path_events = './process_{}/bin/generate_events'.format(process_number)
	#print(path_events)
	#subprocess.call("echo $PWD", shell=True)
	subprocess.call([path_events, '-f', '--cluster'])	
print 'INFO: Events generated.'
