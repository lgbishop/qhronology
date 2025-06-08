.. _`eg:pswap`:

PSWAP (power-SWAP)
==================

Description
-----------

Exponentiation of the SWAP gate produces an interesting interaction (PSWAP) between its input systems: the degree to which their states' values are exchanged depends entirely on the power to which the SWAP gate is taken. This effect means that the PSWAP gate is useful for modelling interesting physical phenomena such as probabilistic scattering, where the power parameter of the gate is analogous to the interaction chance of two particles in a scattering experiment. For even powers, no SWAP occurs, while for odd powers, a SWAP does occur. Non-integer values of the power therefore smoothly interpolate between these two outcomes in the form of a (weighted) quantum superposition of them. :numref:`fig:circuit_algorithm_pswap` depicts a simple PSWAP interaction.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_pswap-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a PSWAP gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_pswap-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a PSWAP gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_pswap-light.png
   :name: fig:circuit_algorithm_pswap
   :scale: 36 %
   :alt: A quantum circuit diagram of a PSWAP gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A PSWAP gate (with power :math:`p`).

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/pswap.py
   :name: code:scattering
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> pswap.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_pswap-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_pswap-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

Gate
^^^^

.. code:: python

   >>> print(repr(pswap.gate()))
   Matrix([
   [1,                   0,                   0, 0],
   [0, exp(I*pi*p)/2 + 1/2, 1/2 - exp(I*pi*p)/2, 0],
   [0, 1/2 - exp(I*pi*p)/2, exp(I*pi*p)/2 + 1/2, 0],
   [0,                   0,                   0, 1]])

States
^^^^^^

.. code:: python

   >>> input_state.print()
   |ψ,φ⟩ = a*c|0,0⟩ + a*d|0,1⟩ + b*c|1,0⟩ + b*d|1,1⟩

.. code:: python

   >>> output_state.print()
   |(ψ,φ)'⟩ = a*c|0,0⟩ + (a*d*(exp(I*pi*p)/2 + 1/2) + b*c*(1/2 - exp(I*pi*p)/2))|0,1⟩ + (a*d*(1/2 - exp(I*pi*p)/2) + b*c*(exp(I*pi*p)/2 + 1/2))|1,0⟩ + b*d|1,1⟩

.. raw:: latex
   
   \newpage