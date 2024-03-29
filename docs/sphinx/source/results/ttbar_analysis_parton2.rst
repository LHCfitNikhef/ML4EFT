Neural network training
============================================================
Here we present plots and animations displaying the training of the neural network
on parton-level :math:`pp \rightarrow t\bar{t}` pseudo-data.  Details of the neural
network architecture and settings are presented in Section 3.3 of :cite:`ML4EFT_temp_id` .


Overview
-----------
First, we present an overview of the training of the neural network associated to the quadratic contribution of the 
chromomagnetic operator :math:`C_{tG}`, trained on two features, :math:`m_{t \bar{t}}` and :math:`y_{t \bar{t}}`.

From left to right and top to bottom we display:

- a point-by-point comparison of the log-likelihood ratio in the ML model and the corresponding analytical calculation; 
- the median of the ratio between the ML model and the analytical calculation and the associated pull in the :math:`(m_{t \bar{t}}, y_{t \bar{t}})` feature space;
- the evolution of the loss function split in training and validation sets for a representative replica as a function of the number of training epochs; 
- the resultant decision boundary :math:`g(x,c)` for :math:`c_{tG} = 2` including MC replica uncertainties, at the end of the training procedure.


.. image:: ../images/nn_perf_overview.png


Animation of the progression of the Truth/NN comparison with training
----------------------------------------------------------------------
The following animation shows the evolution of the median of the ratio between the ML model and the analytical calculation in the :math:`(m_{t \bar{t}}, y_{t \bar{t}})` feature space
with the neural network training.

.. image:: ../images/anim_2d.gif


Animation of the training of the decision boundary function
------------------------------------------------------------
The following animation shows the evolution of the per-replica decision boundary function :math:`g(x,c)`, this time trained on :math:`m_{t \bar{t}}` only.  
The uncertainty on :math:`g(x,c)` is obtained from the spread of replicas.
We compare this to the exact calculation of :math:`g(x,c)`, shown in red.
Excellent agreement between the neural network and exact calculation is found.


.. image:: ../images/anim_1d.gif



