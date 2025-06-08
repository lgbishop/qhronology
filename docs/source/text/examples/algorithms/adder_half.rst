.. _`eg:adder_half`:

Half adder
==========

Description
-----------

An *adder* is a circuit that sums the values of two quantum vector states in some basis. For instance, this could be the states :math:`\ket{x}` and :math:`\ket{y}` in a :math:`\Dimension`-dimensional number basis :math:`\{\ket{n}\}_{n=0}^{\Dimension - 1}`. As described in :ref:`Example: CNOT <eg:cnot>`, this can be accomplished with just a CNOT (controlled-NOT) gate, which produces the sum state :math:`\ket{x \oplus y}`.

We consider here perhaps the simplest form of a quantum adder: a *half* adder (see :numref:`fig:circuit_algorithm_adder_simple`). In addition to producing a *summation* output value

.. math:: s = x \oplus y,

a half adder also produces a *carry* output value

.. math:: c^\prime = xy,

which represents the *overflow* of the summation. This is simply the value by which the modular sum of the inputs :math:`x` and :math:`y` is larger than the modulus :math:`\Dimension`. The form of a half adder presented here was first described by Feynman :cite:p:`feynman_quantum_1986` in the context of quantum computing.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_half-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum half adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_half-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum half adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_half-light.png
   :name: fig:circuit_algorithm_adder_simple
   :scale: 36 %
   :alt: A quantum circuit diagram of a quantum half adder.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum half adder.

A truth table for this circuit in the context of qubits appears in :numref:`table:adder_half`.

.. list-table:: Truth table for a half adder.
   :name: table:adder_half
   :align: left
   :widths: 5 5 10 10
   :header-rows: 1

   * - :math:`x` (augend)
     - :math:`y` (addend)
     - :math:`s` (sum)
     - :math:`c^\prime` (carry)
   * - :math:`0`
     - :math:`0`
     - :math:`0`
     - :math:`0`
   * - :math:`1`
     - :math:`0`
     - :math:`1`
     - :math:`0`
   * - :math:`0`
     - :math:`1`
     - :math:`1`
     - :math:`0`
   * - :math:`1`
     - :math:`1`
     - :math:`0`
     - :math:`1`

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/adder_half.py
   :name: code:adder_half
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

      .. image:: /figures/output/text_examples_algorithms_adder_half-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_adder_half-light.png
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

   >>> sum_state.print()
   s = b*conjugate(b)|0⟩⟨0| + a*conjugate(a)|1⟩⟨1|

.. code:: python

   >>> carry_output_state.print()
   c' = a*conjugate(a)|0⟩⟨0| + b*conjugate(b)|1⟩⟨1|

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage