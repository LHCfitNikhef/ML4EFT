This is a guide on how to use the code in the folder thesis_pim to shower particle level data, train neural networks and make posteriors, as well as how to make the plots shown in the thesis.
The locations of files has been changed to clean up the directories. As a result, some hardcoded specified paths have depreciated. To run most of the codes, you first have to specify the right new paths.
The following names can cause confusion and it is important to mention.
I often refer to Particle level as Hard
I often refer to hadron level as Event 

# Shower Particle level data
The data used as a starting point is that of Jaco ter Hoeve, this data is generated at particle level and saved in .lhe files. For more details, consult https://doi.org/10.1007/JHEP03(2023)033 also on arxiv: 2211.02058

The packages required to run the shower code are 
pythia8 -for showering the data
fastjet3.4 -for jet reconstruction
fastjet_contrib -for jet grooming using softdrop

The code used to call the shower.cc files is located in /code/cluster/shower. There is a python files called shower.py that calls the cc code and a submit_shower.sh the submits this code to a computing cluster.

shower.cc:
The make file currently in the /code/shower_code has the paths to the libraries necessary to run the shower code. Currently these paths are for pim's directory structure, so they have to be adjusted accordingly.

# Training neural networks
Using the data showered and saved somewhere we can train neural networks with the code in /code/cluster/training
A handy code called min_events.pt checks which datafile has the least number of events, to give in the runcard for event number. (min events is checked because going above this gives an error)
You also have to copy the info.txt files containing the values of the wilson coeff that the data was generated on to the newly showered data folder. For this you can use the /code/cluster/core_code copy_info.py code.
The training of neural networks can again be submitted to a computing cluster.

# Posteriors
Finally the neural networks along with the showered data can be used to generate posteriors for the coefficients. Here the submit_ns.sh calls the the optimize_runner code. 
The posteriors for the thesis are stored in /posteriors

# Plotting
To plot the posteriors the code in /code/cluster/plotting/posterior_plot first contains a list of commented settings for making the 12 results posterior plots in the thesis, to remake a plot just uncomment that code. The code below will submit it to a computing cluster and make the posterior. 

The other plotting code is for making the plots in the thesis with self explanatory names.

The features2vs2.py code is a adjusted version of jaco's features.py code that plots the feature distribtutions. It's adjusted to also plot ratio's of distributions for 2 sets of 2 datasets.

The plots for the thesis are stored in /plots

# Data
The data to make the plots in the thesis is stored in /data
The most important folder is hadron_level_data that stores all the hadron level showered datasets. 
The four other data folders are for the other plots in the thesis and finally there is a folder for the models

# conda environment
The settings for the conda environment used to run all codes is stored in /code/conda_enviroment.yml
To make this environment for yourself you just have to write in your terminal: (madgraph is the enviroment name)

conda env create -f conda_environment.yml

conda activate madgraph



