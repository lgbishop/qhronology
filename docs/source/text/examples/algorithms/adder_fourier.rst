.. _`eg:adder_fourier`:

Fourier transform adder
=======================

Description
-----------

The version of a quantum adder presented here sums two multi-qubit integers essentially by computing the summation in Fourier space :cite:p:`draper_addition_2000, ruiz-perez_quantum_2017, sahin_quantum_2020, pavlidis_quantum_2021, seidel_efficient_2022, atchade-adelomou_efficient_2023, wang_comprehensive_2025`. This is achieved by first performing a quantum (discrete) Fourier transform on one of the encoded integers, following with a controlled-phase gate (serving the same function as an ordinary full adder in ordinary non-Fourier Hilbert space), and concluding with an inverse Fourier transform on the same integer.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_fourier-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a QFT-based adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_fourier-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a QFT-based adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_fourier-light.png
   :name: fig:circuit_algorithm_adder_fourier
   :scale: 36 %
   :alt: A quantum circuit diagram of a QFT-based adder.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum circuit diagram of a QFT-based adder.

An example of this algorithm for :math:`3`-qubit integers appears in :numref:`fig:circuit_algorithm_adder_fourier_three`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_fourier_three-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a QFT-based adder for :math:`3`-qubit states.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_fourier_three-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a QFT-based adder for :math:`3`-qubit states.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_fourier_three-light.png
   :name: fig:circuit_algorithm_adder_fourier_three
   :scale: 36 %
   :alt: A quantum circuit diagram of a QFT-based adder for :math:`3`-qubit states.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A QFT-based adder for :math:`3`-qubit states.

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/adder_fourier.py
   :name: code:adder_fourier
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> adder.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_fourier-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_adder_fourier-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> augend_state.print()
   |x⟩ = |0,1⟩

.. code:: python

   >>> addend_state.print()
   |y⟩ = |0,1⟩

.. code:: python

   >>> sum_state.print()
   s = |1,0⟩⟨1,0|

Results
^^^^^^^

.. code:: python

   >>> print(computation)
   Computation: 1 + 1 = 2

.. code:: python

   >>> print(duration)
   Duration: 0.326 seconds

As both the number of qubits and the circuit depth (number of gates) of the quantum Fourier adder are significantly smaller than any of the other quantum adder algorithms, we appropriately find that its operation is computationally much faster.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage