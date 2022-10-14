Neural network training
============================================================


Here we present animations displaying the training of the neural network
on parton-level :math:`pp \rightarrow t\bar{t}` pseudo-data.  Details of the neural
network architecture and settings are presented in Section 3.3 of :cite:`ML4EFT_temp_id` .


Training of the decision boundary function
-------------------------------------------


The **ML4EFT** framework benefits from the polynomial structure of the EFT cross-sections.
A separate neural network is used to parametrise the dependence of the likelihood ratio on
each of the linear and quadratic contributions
from each Wilson coefficient.
As a result, the number of training 
scales quadratically with the number of EFT coefficients.


First, we display the training of the decision boundary function :math:`g(x,c)`, switching on 
only the linear contribution from :math:`c_{tg}`.  We see that over the course of 
the training, the 50 replicas converge and
good agreement with the analytical calculation is found.

.. image:: ../images/anim_1d.gif

Secondly, we repeat this training, including the quadratic contributon from :math:`c_{tg}`.
Again, by the end of the training, good agreement between the neural network and analytical calculation
is found.

.. image:: ../images/anim_1d.gif


Comparison of the NN with the truth, two-dimensional plots
-------------------------------------------------------------
Update one of these to be a pull plot:

.. image:: ../images/anim_2d.gif
   :width: 48 %
.. image:: ../images/anim_2d.gif
   :width: 48 %

