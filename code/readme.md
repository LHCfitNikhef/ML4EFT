[![CodeFactor](https://www.codefactor.io/repository/github/lhcfitnikhef/smeft/badge?s=e885406e89637e9e815c3a63dc207b99f4984a60)](https://www.codefactor.io/repository/github/lhcfitnikhef/smeft)

# Introduction

ML4EFT is a python package that studies machine learning (ML) applications for effective field
theories (EFTs). You can click [here](http://htmlpreview.github.io/?https://github.com/LHCfitNikhef/ML4EFT/blob/main/code/sphinx/_build/html/index.html) to browse the documentation.

## Organisation

In this directory you will find the following subdirectories:

* **UFO_model**: contains Universal FeynRules Output files


* **cluster** : contains scripts for submitting the code to a cluster


* **madgraph_cards**: contains MG5 runcards


* **notebooks**: contains mathematica notebooks and/or scripts


* **output**: contains all output, such as plots


* **quad_clas**: contains the quadratic classifier python package


* **sphinx**: contains the code's documentation


Furthermore, inside ```quad_clas``` you will find 

* **analyse**: contains code to analyse the z-scores that originate from
    scanning over EFT coefficient space. Results are presented for
    the neural network (nn), truth and binned analyses.
  

* **core**: the neural network training and the computation of the bounds is contained in here.


* **fit**: contains modules to start a fit

## Run instructions

The file ```main.py```  shows an example how to use the code. We distinguish between the following two
use cases:

1. Finding the expected exclusion limits at specific points in EFT coefficient space. 
2. Interpolating the results found from 1 to the entire EFT space. 

Note that 1 has to be done before 2. For step 1, one will have to switch ```scan``` inside the file 
```main.py``` to ```True```. Then for step 2, one should set ```scan``` to ```False``` and 
```analyse``` to ```True```. The binned analysis can be run from here as well.






