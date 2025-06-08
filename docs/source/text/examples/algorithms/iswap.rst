.. _`eg:iswap`:

iSWAP (imaginary-SWAP)
======================

Description
-----------

An iSWAP (imaginary-SWAP) gate is a simply a SWAP gate in which any pair of states that are exchanged are also multiplied by a phase factor of :math:`\e^{\tfrac{\eye\pi}{2}} = \eye` (the imaginary unit). It can be constructed from :math:`\op{S}` (:math:`\op{Z}^{\tfrac{1}{2}}`) gates, :math:`\Hadamard` (Hadamard) gates, and CNOT gates, as depicted in :numref:`fig:circuit_algorithm_iswap`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_iswap-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the construction of the iSWAP gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_iswap-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the construction of the iSWAP gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_iswap-light.png
   :name: fig:circuit_algorithm_iswap
   :scale: 36 %
   :alt: A quantum circuit diagram of the construction of the iSWAP gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   One possible construction of the iSWAP gate.

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/iswap.py
   :name: code:iswap
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> iswap.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_iswap-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_iswap-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

Gate
^^^^

.. code:: python

   >>> print(repr(iswap.gate()))
   Matrix([
   [1, 0, 0, 0],
   [0, 0, I, 0],
   [0, I, 0, 0],
   [0, 0, 0, 1]])

States
^^^^^^

.. code:: python

   >>> input_state.print()
   |ψ,φ⟩ = a*c|0,0⟩ + a*d|0,1⟩ + b*c|1,0⟩ + b*d|1,1⟩

.. code:: python

   >>> output_state.print()
   |(ψ,φ)'⟩ = a*c|0,0⟩ + I*b*c|0,1⟩ + I*a*d|1,0⟩ + b*d|1,1⟩

.. raw:: latex
   
   \newpage
