Higgs production in association with a Z boson
==============================================

We present here plots and animations related to Section 4.4 and 5.3 of :cite:`ML4EFT_temp_id`.

We consider Higgs production in association with a Z boson in the 
:math:`Z h \rightarrow \ell^{+} \ell^{-} \bar{b} b` final state,
at the LHC 14 TeV.

Models
------
Trained models for :math:`p p \rightarrow Z h \rightarrow \ell^{+} \ell^{-} \bar{b} b`
are presented in Table 1.
The models are trained on either a single feature, :math:`p_{T}^{Z}` (calculated as
the :math:`p_{T}` of the final-state leptons),
or the full set of 7 kinematic features.  More details about the kinematic features
used in the neural network training can be found in the :ref:`next<kinematics_zh>` section.


.. list-table:: Trained models for Higgs production in association with a Z boson
   :widths: 25 25
   :header-rows: 1

   * - Features
     - Models
   * - :math:`p_T^{Z}`
     - `models <https://www.dropbox.com/s/ka7xlrke9wl9w5u/zh_particle_pt_z.tar.gz?dl=0>`_
   * - all (7)
     - `models <https://www.dropbox.com/s/f8ouvyz117c07ao/zh_particle_7_feat.tar.gz?dl=0>`_

Results
----------------------
Plots and animations are available at the following links:

.. toctree::
   :maxdepth: 6

   zh_analysis1
   zh_analysis2
   zh_analysis3
   zh_analysis4
