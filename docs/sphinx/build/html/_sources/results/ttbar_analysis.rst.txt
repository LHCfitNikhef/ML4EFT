Inclusive top pair production at the particle level
===================================================

We present here plots and animations related to Sections 4.3 and 5.2 of :cite:`ML4EFT_temp_id`.

We consider inclusive top quark pair production at the particle level i.e. including top quark
decays in the dilepton channel: :math:`p p \rightarrow t \bar{t}, t \bar{t} \rightarrow b \bar{b} \ell^{+} \ell^{-} \nu_{\ell} \bar{\nu}_{\ell}`, at the LHC 14 TeV.

Models
------
Trained models of top-quark pair production in the dileptonic decay channel are presented in Table 1.
The models are trained on either a single feature, :math:`p_{T}^{\ell \ell}`, 
a pair of features :math:`(p_{T}^{\ell \ell}, \eta_{\ell})` or
the full set of 18 kinematic features.  More details about the kinematic features
used in the neural network training can be found in the :ref:`next<kinematics>` section.


.. list-table:: Trained models for top-quark pair production at the particle level
   :widths: 25 25
   :header-rows: 1

   * - Features
     - Models
   * - :math:`p_T^{\ell\bar{\ell}}`
     - `models <https://www.dropbox.com/s/o48ajbsh4xwfpu4/tt_particle_pt_ll.tar.gz?dl=0>`_
   * - :math:`p_T^{\ell\bar{\ell}}, \eta_\ell`
     - `models <https://www.dropbox.com/s/dy7ni8t4g8x68u0/tt_particle_ptll_etal.tar.gz?dl=0>`_
   * - all (18)
     - `models <https://www.dropbox.com/s/54uchr1w7pkjrqf/tt_particle_18_feat.tar.gz?dl=0>`_

Results
-------
Plots and animations are available at the following links:

.. toctree::
   :maxdepth: 5

   ttbar_analysis_particle1
   ttbar_analysis_particle2
   ttbar_analysis_particle3
   ttbar_analysis_particle4   
   ttbar_analysis_particle5
   ttbar_analysis_particle6


 
