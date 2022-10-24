.. _kinematics_zh:

Kinematic features used as inputs to the neural network
============================================================

We display here the kinematic features used as inputs to the neural network,
calculated both in the SM and at representative points in the SMEFT parameter space.

First, we display the results including only linear contributions from the SMEFT Wilson coefficients:


.. image:: ../images/zh_lin_dist.png


Secondly, we include both linear and quadratic contributions:


.. image:: ../images/zh_quad_dist.png



The kinematic features are defined as follows:

.. list-table:: Definitions of the kinematic features displayed in the figures above.
   :widths: 25 50
   :header-rows: 1

   * - Label
     - Definition
   * - :math:`p_T^{Z}`
     - :math:`=p_T^{\ell \bar{\ell}}`, the :math:`p_{T}` of the dilepton system
   * - :math:`p_T^{b}`
     - :math:`p_{T}` of the b quark
   * - :math:`p_T^{b \bar{b}}`
     - :math:`p_{T}` of the :math:`b \bar{b}` system
   * - :math:`\Delta R(b_{1}, b_{2})`
     -  Angular separation between the two b quarks
   * - :math:`\Delta \phi(b, b \bar{b})`
     - Azimuthal angle between the :math:`b` quark and the :math:`b \bar{b}` system
   * - :math:`|\Delta \eta(Z, b \bar{b})|`
     - Absolute value of the pseudorapidity difference between the Z and the :math:`b \bar{b}` system
   * - :math:`m_{\ell \ell}`
     - Invariant mass of the dilepton system
   * - :math:`\Delta \phi(b,\ell)`
     - Azimuthal angle between the leading b quark and charged lepton
