.. _`eg:adder_full`:

Full adder
==========

Description
-----------

A *full* adder is simply an adder with *three* (non-zero) inputs, as opposed to the two of a half adder. With the first and second of these inputs being the ordinary pair of values to be summed (e.g., :math:`x` and :math:`y`), a full adder's third input is used to modify the addition operation. This enables the circuit to take into account the carry output value :math:`c` of a previous iteration, yielding the summation output

.. math:: s = x \oplus y \oplus c,

and the carry output

.. math:: c^\prime = xy \oplus yc \oplus xc.

Importantly, this means that full adders can be used in succession as a way to sum multi-qubit-encoded numbers. Like the half adder, the full adder (as it is presented here in :numref:`fig:circuit_algorithm_adder_full`) was first studied by Feynman :cite:p:`feynman_quantum_1986`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_full-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum adder with a carry qubit.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_full-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum adder with a carry qubit.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_full-light.png
   :name: fig:circuit_algorithm_adder_full
   :scale: 36 %
   :alt: A quantum circuit diagram of a quantum adder with a carry qubit.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum full adder.

A truth table for this circuit in the context of qubits appears in :numref:`table:adder_full`.

.. list-table:: Truth table for the full adder.
   :name: table:adder_full
   :align: left
   :widths: 6 6 10 10 10
   :header-rows: 1

   * - :math:`x` (augend)
     - :math:`y` (addend)
     - :math:`c` (carry input)
     - :math:`s` (sum)
     - :math:`c^\prime` (carry output)
   * - :math:`0`
     - :math:`0`
     - :math:`0`
     - :math:`0`
     - :math:`0`
   * - :math:`1`
     - :math:`0`
     - :math:`0`
     - :math:`1`
     - :math:`0`
   * - :math:`0`
     - :math:`1`
     - :math:`0`
     - :math:`1`
     - :math:`0`
   * - :math:`1`
     - :math:`1`
     - :math:`0`
     - :math:`0`
     - :math:`1`
   * - :math:`0`
     - :math:`0`
     - :math:`1`
     - :math:`1`
     - :math:`0`
   * - :math:`1`
     - :math:`0`
     - :math:`1`
     - :math:`0`
     - :math:`1`
   * - :math:`0`
     - :math:`1`
     - :math:`1`
     - :math:`0`
     - :math:`1`
   * - :math:`1`
     - :math:`1`
     - :math:`1`
     - :math:`1`
     - :math:`1`

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/adder_full.py
   :name: code:adder_full
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

      .. image:: /figures/output/text_examples_algorithms_adder_full-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_adder_full-light.png
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
   |x⟩ = a|0⟩ + b|1⟩

.. code:: python

   >>> addend_state.print()
   |y⟩ = |1⟩

.. code:: python

   >>> carry_input_state.print()
   |c⟩ = |1⟩

.. code:: python

   >>> sum_state.print()
   s = a*conjugate(a)|0⟩⟨0| + b*conjugate(b)|1⟩⟨1|

.. code:: python

   >>> carry_output_state.print()
   c' = |1⟩⟨1|

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage