[![CodeFactor](https://www.codefactor.io/repository/github/lhcfitnikhef/ml4eft/badge?s=4529ce75fe7f8468c4b83b95ee93648e8aba7e6a)](https://www.codefactor.io/repository/github/lhcfitnikhef/ml4eft)

# Introduction

ML4EFT is a python package that studies machine learning (ML) applications for effective field
theories (EFTs). 


## Organisation

In this directory you will find the following subdirectories:

* **UFO_model**: contains Universal FeynRules Output files


* **cluster** : contains scripts for submitting the code to a cluster


* **dev**: contains developmental code (can be ignored)


* **madgraph_cards**: contains MG5 runcards


* **notebooks**: contains mathematica notebooks and/or scripts


* **sphinx**: contains the code's documentation


* **src**: contains the ML4EFT python package


* **tutorial**: contains tutorials how to use the code


## Run instructions

The file ```main.py```  shows an example how to use the code. We distinguish between the following two
use cases:

1. Finding the expected exclusion limits at specific points in EFT coefficient space. 
2. Interpolating the results found from 1 to the entire EFT space. 

Note that 1 has to be done before 2. For step 1, one will have to switch ```scan``` inside the file 
```main.py``` to ```True```. Then for step 2, one should set ```scan``` to ```False``` and 
```analyse``` to ```True```. The binned analysis can be run from here as well.






