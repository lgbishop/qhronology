.. _`eg:ccnot`:

CCNOT (controlled-controlled-NOT)
=================================

Description
-----------

A CCNOT (controlled-controlled-NOT) gate, also known as a *Toffoli gate*, is a simple extension to a CNOT gate (see :ref:`eg:cnot`). It is useful as a method of multiplying the values of two qubits (e.g., :math:`\ket{x}` and :math:`\ket{y}`), and imprinting this result onto a third qubit (e.g., :math:`\ket{z}`), e.g.,

.. math:: \ket{x} \otimes \ket{y} \otimes \ket{z} \rightarrow \ket{x} \otimes \ket{y} \otimes \ket{z \oplus xy}.

:numref:`fig:circuit_algorithm_csum` visualizes this operation.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_ccnot-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a CCNOT (controlled-controlled-NOT) gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_ccnot-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a CCNOT (controlled-controlled-NOT) gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_ccnot-light.png
   :name: fig:circuit_algorithm_csum
   :scale: 36 %
   :alt: A quantum circuit diagram of a CCNOT (controlled-controlled-NOT) gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A CCNOT (controlled-controlled-NOT) gate.

As the input states are both vectors, the action of the (linear) CCNOT gate, described by the unitary

.. math::

   \begin{aligned}
       \Unitary &= \Control^{0,1} \NOT^2 \\
       &= \Identity \otimes \Identity \otimes \Identity + {\ket{1}\bra{1}} \otimes {\ket{1}\bra{1}} \otimes (\Pauli_{x} - \Identity),
   \end{aligned}

on the tripartite input :math:`\ket{x} \otimes \ket{y} \otimes \ket{z}` yields a vector state:

.. math::

   \begin{aligned}
       \MapGeneral_{\Unitary} \bigl[\ket{x} \otimes \ket{y} \oplus \ket{z}\bigr] &= \Control^{0,1} \NOT^2 \ket{x} \otimes \ket{y} \oplus \ket{z} \\
       &= \ket{x} \otimes \ket{y} \otimes \ket{z \oplus x y}
   \end{aligned}

:numref:`table:ccnot` is a truth table for this operation in the context of qubits.

.. list-table:: Truth table of the CCNOT gate.
   :name: table:ccnot
   :align: left
   :widths: 5 5 5 10
   :header-rows: 1

   * - :math:`x`
     - :math:`y`
     - :math:`z`
     - :math:`z \oplus x y`
   * - :math:`0`
     - :math:`0`
     - :math:`0`
     - :math:`0`
   * - :math:`1`
     - :math:`0`
     - :math:`0`
     - :math:`0`
   * - :math:`0`
     - :math:`1`
     - :math:`0`
     - :math:`0`
   * - :math:`1`
     - :math:`1`
     - :math:`0`
     - :math:`1`
   * - :math:`0`
     - :math:`0`
     - :math:`1`
     - :math:`1`
   * - :math:`1`
     - :math:`0`
     - :math:`1`
     - :math:`1`
   * - :math:`0`
     - :math:`1`
     - :math:`1`
     - :math:`1`
   * - :math:`1`
     - :math:`1`
     - :math:`1`
     - :math:`0`

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/ccnot.py
   :name: code:ccnot
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

      .. image:: /figures/output/text_examples_algorithms_ccnot-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_ccnot-light.png
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

   >>> third_state.print()
   |z⟩ = u|0⟩ + v|1⟩

.. code:: python

   >>> output_state.print()
   |x, y, z ⊕ xy⟩ = a*c*u|0,0,0⟩ + a*c*v|0,0,1⟩ + a*d*u|0,1,0⟩ + a*d*v|0,1,1⟩ + b*c*u|1,0,0⟩ + b*c*v|1,0,1⟩ + b*d*v|1,1,0⟩ + b*d*u|1,1,1⟩

.. raw:: latex
   
   \newpage