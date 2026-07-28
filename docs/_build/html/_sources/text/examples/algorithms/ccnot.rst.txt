.. _`eg:ccnot`:

CCNOT (controlled-controlled-NOT)
=================================

Description
-----------

A CCNOT (controlled-controlled-NOT) gate, also known as a *Toffoli gate*, is a simple extension to a CNOT gate (see :numref:`eg:cnot` :ref:`eg:cnot`). It is useful as a method of multiplying the values of two qubits (e.g., :math:`\ket{x}` and :math:`\ket{y}`), and imprinting this result onto a third qubit (e.g., :math:`\ket{z}`), e.g.,

.. math:: \ket{x} \otimes \ket{y} \otimes \ket{z} \rightarrow \ket{x} \otimes \ket{y} \otimes \ket{z \oplus xy}.

:numref:`fig:circuit_algorithm_csum` visualizes this operation.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_ccnot-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a CCNOT (controlled-controlled-NOT) gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_ccnot-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a CCNOT (controlled-controlled-NOT) gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_ccnot-light.png
   :name: fig:circuit_algorithm_csum
   :scale: 34 %
   :alt: A quantum circuit diagram of a CCNOT (controlled-controlled-NOT) gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A CCNOT (controlled-controlled-NOT) gate.

.. raw:: latex

   \vspace*{-\baselineskip}

As the input states are both vectors, the action of the (linear) CCNOT gate, described by the unitary

.. math::

   \begin{aligned}
       \Unitary &= \Control^{\indices{0,1}} \NOT^{\indices{2}} \\
       &= \Identity \otimes \Identity \otimes \Identity + {\ket{1}\bra{1}} \otimes {\ket{1}\bra{1}} \otimes (\Pauli_{x} - \Identity),
   \end{aligned}

on the tripartite input :math:`\ket{x} \otimes \ket{y} \otimes \ket{z}` yields a vector state:

.. math::

   \begin{aligned}
       \MapGeneral_{\Unitary} \bigl[\ket{x} \otimes \ket{y} \oplus \ket{z}\bigr] &= \Control^{\indices{0,1}} \NOT^{\indices{2}} \ket{x} \otimes \ket{y} \oplus \ket{z} \\
       &= \ket{x} \otimes \ket{y} \otimes \ket{z \oplus x y}.
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

.. raw:: latex

   \begin{codetitled}{CCNOT (controlled-controlled-NOT)}{}

.. literalinclude:: /text/examples/algorithms/ccnot.py
   :name: code:ccnot
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

   >>> circuit.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_ccnot.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_ccnot-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_ccnot-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

.. raw:: latex

   \enlargethispage{\baselineskip}

States
^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> first_state.print()
   |x⟩ = a|0⟩ + b|1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> second_state.print()
   |y⟩ = c|0⟩ + d|1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> third_state.print()
   |z⟩ = u|0⟩ + v|1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> output_state.print()
   |x, y, z ⊕ xy⟩ = a*c*u|0,0,0⟩ + a*c*v|0,0,1⟩ + a*d*u|0,1,0⟩ + a*d*v|0,1,1⟩ + b*c*u|1,0,0⟩ + b*c*v|1,0,1⟩ + b*d*v|1,1,0⟩ + b*d*u|1,1,1⟩

.. raw:: latex

   \end{code}

.. raw:: latex
   
   \newpage