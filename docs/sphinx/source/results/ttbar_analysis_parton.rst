Inclusive top pair production at the parton level
=================================================

We present here the plots and animations related to Sections 4.2 and 5.1 of :cite:`ML4EFT_temp_id`.

We consider inclusive top quark pair production with stable tops, :math:`p p \rightarrow t \bar{t}`, at the LHC 14 TeV,
benchmarking the neural network parametrisation of the likelihood ratio against the analytical calculation.

We consider the effects
of two representative dimension-six SMEFT operators modifying inclusive top quark pair
production 
as defined in :cite:`Brivio:2020onw` in the topU3l flavour scheme:

.. math::
    \nonumber \mathcal{O}_{tu}^{(8)} &= (\bar{t}\gamma_\mu T^A t)(\bar{u}\gamma^\mu T^A u) \, ,\\
    \mathcal{O}_{tG} &= (\bar{Q}\sigma^{\mu\nu}T^a t) \tilde{H}G_{\mu\nu}^a \, .
    \label{eq:tt_part_operators}


Models and training reports
-----------------------------

Trained models of top-quark pair production with two features, the invariant mass :math:`m_{t\bar{t}}` and the rapidity :math:`y_{t\bar{t}}`,
are available `here <https://www.dropbox.com/s/hbq29u6vqadfscf/tt_parton_mtt_y.tar.gz?dl=0>`_. See Table 1 for the
training reports corresponding to each Wilson coefficient, at both :math:`\mathcal{O}(\Lambda^{-2})` and :math:`\mathcal{O}(\Lambda^{-4})` in the 
EFT expansion.

.. list-table:: Training reports per EFT ratio function for top-quark pair production at the parton level with :math:`c_{tG}` and :math:`c_{tu}^{(8)}`.
                Each ratio function is 
                trained on two features, the invariant mass :math:`m_{t\bar{t}}` and the rapidity :math:`y_{t\bar{t}}` of the top-quark pair.
   :widths: 25 25
   :header-rows: 1

   * - :math:`p p \rightarrow t \bar{t}`
     - Training report :math:`(m_{t\bar{t}}, y_{t\bar{t}})`
   * - ``ctu8``
     - `report <https://www.dropbox.com/s/wym4sfa5vyeynf2/report_2022_10_15_model_ctu8_lin.pdf?dl=0>`_
   * - ``ctu8_ctu8``
     - `report <https://www.dropbox.com/s/v91cj0r511x2mkw/report_2022_10_15_model_ctu8_quad.pdf?dl=0>`_
   * - ``ctGRe``
     - `report <https://www.dropbox.com/s/5qmp39gzun0z1g4/report_2022_10_15_model_ctGRe_lin.pdf?dl=0>`_
   * - ``ctGRe_ctGRe``
     - `report <https://www.dropbox.com/s/tgk8kd7z4s8zj7m/report_2022_10_15_model_ctGRe_quad.pdf?dl=0>`_

Trained models of top-quark pair production with a single feature, the invariant mass :math:`m_{t\bar{t}}`,
are available `here <https://www.dropbox.com/s/467rbwodz6lh21p/tt_parton_mtt.tar.gz?dl=0>`_. See Table 2 for the corresponding
training reports.


.. list-table:: Training reports per EFT ratio function for top-quark pair production at the parton level with :math:`c_{tG}` and :math:`c_{tu}^{(8)}`,
                trained on a single feature, the invariant mass :math:`m_{t\bar{t}}` of the top-quark pair.
   :widths: 25 25
   :header-rows: 1

   * - :math:`p p \rightarrow t \bar{t}`
     - Training report :math:`(m_{t\bar{t}})`
   * - ``ctu8``
     - `report <https://www.dropbox.com/s/9mlp14adofq66kr/report_2022_10_16_model_ctu8_lin_mtt.pdf?dl=0>`_
   * - ``ctu8_ctu8``
     - `report <https://www.dropbox.com/s/bub4gak4hzzyniw/report_2022_10_16_model_ctu8_quad_mtt.pdf?dl=0>`_
   * - ``ctGRe``
     - `report <https://www.dropbox.com/s/ns3cllru4h9ralp/report_2022_10_16_model_ctGRe_lin_mtt.pdf?dl=0>`_
   * - ``ctGRe_ctGRe``
     - `report <https://www.dropbox.com/s/bub4gak4hzzyniw/report_2022_10_16_model_ctu8_quad_mtt.pdf?dl=0>`_


Results
----------------------
Plots and animations are available at the following links:

.. toctree::
   :maxdepth: 5

   ttbar_analysis_parton1
   ttbar_analysis_parton2
   ttbar_analysis_parton3
