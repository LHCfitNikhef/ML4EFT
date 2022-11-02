# ML4EFT
ML4EFT is a general open-source framework for the integration of unbinned multivariate observables into global fits of particle physics data.
It makes use of machine learning regression and classification techniques to parameterise high-dimensional likelihood ratios,
and can be seamlessly integrated into
global analyses of, for example, the Standard Model Effective Field Theory and Parton Distribution Functions.

The ML4EFT framework is made available via the Python Package Index (pip) and can be installed directly 
by running 

``pip install ml4eft``

or alternatively the code can be downloaded from this public GitHub repository, and then installed by running

```shell
cd code
pip install -e .
```  

The framework is documented on a dedicated website
https://lhcfitnikhef.github.io/ML4EFT,
where, in addition, one can find a self-standing tutorial (which can also
be run in Google Colab) where the user is guided step by step in how
unbinned multivariate observables can be constructed given a choice of
EFT coefficients and of final-state kinematic features.