.. _`eg:generation_ghz`:

Generation of a GHZ state
=========================

Description
-----------

The circuit in :numref:`fig:circuit_algorithm_generation_ghz` illustrates an algorithm for the generation of a GHZ state :eq:`eq:GHZ_state` from primitive :math:`\ket{0}` states.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_generation_ghz-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting the generation of a GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_generation_ghz-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting the generation of a GHZ state.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_generation_ghz-light.png
   :name: fig:circuit_algorithm_generation_ghz
   :scale: 36 %
   :alt: A quantum circuit diagram depicting the generation of a GHZ state.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Generation of a GHZ state.

The complete unitary transformation described by this circuit is the product

.. math:: \Unitary = \Control^1 \NOT^2 \cdot \Control^0 \NOT^1 \cdot \Hadamard^0.

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/generation_ghz.py
   :name: code:generation_ghz
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> generator.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_ghz-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_generation_ghz-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

State
^^^^^

.. code:: python

   >>> ghz_state.print()
   |GHZ⟩ = sqrt(2)/2|0,0,0⟩ + sqrt(2)/2|1,1,1⟩

.. raw:: latex
   
   \newpage