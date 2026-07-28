.. _`eg:iswap`:

iSWAP (imaginary-SWAP)
======================

Description
-----------

An iSWAP (imaginary-SWAP) gate is a simply a SWAP gate in which any pair of states that are exchanged are also multiplied by a phase factor of :math:`\e^{\eye\pi/2} = \eye` (the imaginary unit). It can be constructed from :math:`\op{S}` (:math:`\op{Z}^{1/2}`) gates, :math:`\Hadamard` (Hadamard) gates, and CNOT gates, as depicted in :numref:`fig:circuit_algorithm_iswap`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_iswap-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the construction of the iSWAP gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_iswap-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the construction of the iSWAP gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_iswap-light.png
   :name: fig:circuit_algorithm_iswap
   :scale: 34 %
   :alt: A quantum circuit diagram of the construction of the iSWAP gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   One possible construction of the iSWAP gate.

.. raw:: latex

   \vspace*{-\baselineskip}

Implementation
--------------

.. raw:: latex

   \enlargethispage{-2\baselineskip}

.. raw:: latex

   \begin{codetitled}{iSWAP (imaginary-SWAP)}{}

.. literalinclude:: /text/examples/algorithms/iswap.py
   :name: code:iswap
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> iswap.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_iswap.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_iswap-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_iswap-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

Gate
^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(repr(iswap.gate(simplify=True)))
   Matrix([
   [1, 0, 0, 0],
   [0, 0, I, 0],
   [0, I, 0, 0],
   [0, 0, 0, 1]])

.. raw:: latex

   \end{code}

States
^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> input_state.print()
   |ψ,φ⟩ = a*c|0,0⟩ + a*d|0,1⟩ + b*c|1,0⟩ + b*d|1,1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> output_state.print()
   |(ψ,φ)′⟩ = a*c|0,0⟩ + I*b*c|0,1⟩ + I*a*d|1,0⟩ + b*d|1,1⟩

.. raw:: latex

   \end{code}

.. raw:: latex
   
   \newpage