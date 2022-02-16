# Custom cuts in madgraph

* The file ``dummy_fct.f`` implements a cut on $\Delta R_{b\bar{b}}$ conditioned on $p_T^Z$. 
* The jet cone radius uses the pseudorapidity: $\Delta_R^2 = \Delta\phi^2 + \Delta\eta^2$
* ``kin_functions.f`` should go into the ``Source`` directory, not in ``Subprocesses``.

