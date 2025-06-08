.. _`eg:cnot`:

CNOT (controlled-NOT)
=====================

Description
-----------

A CNOT (controlled-NOT) gate is a useful gate for performing a (qu)bit-wise sum of the state values of two quantum systems. For instance, given the states :math:`\ket{x}` and :math:`\ket{y}` in a :math:`\Dimension`-dimensional basis :math:`\{\ket{n}\}_{n=0}^{\Dimension - 1}`, a CNOT operation has the action

.. math:: \ket{x} \otimes \ket{y} \rightarrow \ket{x} \otimes \ket{x \oplus y}.

A circuit diagram of a CNOT gate appears in :numref:`fig:circuit_algorithm_cnot`.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_cnot-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a CNOT (controlled-NOT) gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_cnot-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a CNOT (controlled-NOT) gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_cnot-light.png
   :name: fig:circuit_algorithm_cnot
   :scale: 36 %
   :alt: A quantum circuit diagram of a CNOT (controlled-NOT) gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A CNOT (controlled-NOT) gate.

As the input states are both vectors, the application of the CNOT gate

.. math::

   \begin{aligned}
       \Unitary &= \Control^0 \NOT^1 \\
       &= \Identity \otimes \Identity + {\ket{1}\bra{1}} \otimes (\Pauli_{x} - \Identity),
   \end{aligned}

on the bipartite input :math:`\ket{x} \otimes \ket{y}` simply produces a vector state:

.. math::

   \begin{aligned}
       \MapGeneral_{\Unitary} \bigl[\ket{x} \otimes \ket{y}\bigr] &= \Control^0 \NOT^1 \ket{x} \otimes \ket{y} \\
       % &= \sum\limits_{a,b=0}^{1} {\ket{a}\braket{a}{x}} \otimes {\ket{b \oplus a}\braket{b}{y}}, \\
       &= \ket{x} \otimes \ket{x \oplus y}
   \end{aligned}

Observe how the value of the second system is now the sum of the inputs values (modulo the dimensionality), so if we simply discard (trace over) the first system, we obtain our desired result. A truth table for qubits appears in :numref:`table:cnot`.

.. list-table:: Truth table of the CNOT gate.
   :name: table:cnot
   :align: left
   :widths: 5 5 10
   :header-rows: 1

   * - :math:`x`
     - :math:`y`
     - :math:`x \oplus y`
   * - :math:`0`
     - :math:`0`
     - :math:`0`
   * - :math:`1`
     - :math:`0`
     - :math:`1`
   * - :math:`0`
     - :math:`1`
     - :math:`1`
   * - :math:`1`
     - :math:`1`
     - :math:`0`

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/cnot.py
   :name: code:cnot
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> circuit.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_cnot-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_cnot-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> first_state.print()
   |x⟩ = a|0⟩ + b|1⟩

.. code:: python

   >>> second_state.print()
   |y⟩ = c|0⟩ + d|1⟩

.. code:: python

   >>> output_state.print()
   |x, x ⊕ y⟩ = a*c|0,0⟩ + a*d|0,1⟩ + b*d|1,0⟩ + b*c|1,1⟩
.. raw:: latex
   
   \newpage