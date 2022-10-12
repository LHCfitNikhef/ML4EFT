.. ML4EFT documentation master file, created by
   sphinx-quickstart on Tue Aug 16 09:50:44 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



ML4EFT
==================================

ML4EFT is a general open-source framework for the integration of unbinned observables into global fits of particle physics data.
It makes use of machine learning regression and classification techniques to parameterise high-dimensional likelihood ratios,
and can be seamlessly integrated into
global analyses of, for example, the Standard Model Effective Field Theory and Parton Distribution Functions.


.. figure:: images/summary.png
    :width: 100%
    :class: align-center
    :figwidth: 100%
    :figclass: align-center

    *Caption*

.. toctree::
   :maxdepth: 5
   :caption: Overview
   :hidden:

   overview/features.rst
   overview/quadratic_classifier.rst
   overview/mlspecs.rst


.. toctree::
   :maxdepth: 6
   :caption: Code
   :hidden:

   modules/installation.rst
   modules/tutorial.rst
   _autosummary/ml4eft.rst


.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:


.. toctree::
   :maxdepth: 4
   :caption: Results
   :hidden:

   results/overview.rst


Project Description
-------------------------
Optimizing theoretical interpretations of particle physics data demands identifying experimental observables with high sensitivity to the model parameters of interest.
Such measurements not only lead to more stringent constraints on the model parameters, but also provide quantitative upper bounds indicating the maximum amount of physical information that can be extracted from a given process.


With this motivation, we have developed a machine learning framework which enables the integration of unbinned observables into global fits of particle physics data: **ML4EFT**.
See the :ref:`Overview<overview>` section for more details of the ML4EFT framework, and the :ref:`Code<code>` section for the ML4EFT code documentation.


ML4EFT appears in the following paper:

- *Unbinned measurements for global SMEFT fits from machine learning*, Gomez Ambrosio, Raquel and ter Hoeve, Jaco, and Madigan, Maeve and Rojo, Juan and Sanz, Veronica :cite:p:...
 
Here, we provide a proof-of-concept of the ML4EFT framework by constructing unbinned observables from pseudo-data of particle-level :math:`t\bar{t}` and :math:`hZ` production at the LHC 14 TeV,
demonstrating the improved sensitivity that can be obtained relative to binned measurements. 
Results from this paper are presented in the :ref:`Results<results>` section, including animations not present in the paper.







Team Description
----------------------------------
- Raquel Gomez Ambrosio *Universita degli Studi di Milano-Bicocca and INFN*
- Jaco ter Hoeve, *VU Amsterdam and Nikhef Theory Group*
- Maeve Madigan *University of Cambridge*
- Juan Rojo, *VU Amsterdam and Nikhef Theory Group*
- Veronica Sanz *Universidad de Valencia-CSIC and University of Sussex*
  
Citation policy
----------------------------------
If you use the ML4EFT code in a scientific publication, please make sure to cite:

- *Unbinned measurements for global SMEFT fits from machine learning*, Gomez Ambrosio, Raquel and ter Hoeve, Jaco, and Madigan, Maeve and Rojo, Juan and Sanz, Veronica :cite:p:...

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
