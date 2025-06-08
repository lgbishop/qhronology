.. _`eg:adder_lookahead`:

Carry-lookahead adder
=====================

Description
-----------

A quantum *carry-lookahead* adder, proposed by Vedral et al. :cite:p:`vedral_quantum_1996`, is another style of multi-qubit adder and appears in :numref:`fig:circuit_algorithm_adder_lookahead`. It consists of two phases: in the first, the carry qubits are computed, while in the second, the sums (taking into account the value of the carry qubits) are computed (in addition to the carry qubits being reverted back to their original values). Note that in this implementation, the order of the qubits in the encoding is reversed, such that the least-significant qubits are at the top while the most-significant qubits are at the bottom.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_lookahead-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum carry-lookahead adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_lookahead-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum carry-lookahead adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_lookahead-light.png
   :name: fig:circuit_algorithm_adder_lookahead
   :scale: 36 %
   :alt: A quantum circuit diagram of a quantum carry-lookahead adder.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A :math:`2`-qubit quantum carry-lookahead adder.

The values of the summation qubits can be determined to be

.. math::

   s_i =
       \begin{cases}
           x_0 \oplus y_0 \oplus c_0 & i = 0; \\
           x_i \oplus y_i \oplus c^\prime_i & i > 0. \\
       \end{cases}

This version of an adder resets all output carry qubits to their original input values. The intermediary carry values however are

.. math::

   c^\prime_i =
       \begin{cases}
           c_1 \oplus x_0 y_0 \oplus c_0 (x_0 \oplus y_0) & i = 1; \\
           c_i \oplus x_{i - 1} y_{i - 1} \oplus c^\prime_{i - 1} (x_{i - 1} \oplus y_{i - 1}) & i > 1. \\
       \end{cases}

The last qubit is simply an overflow qubit and has the value

.. math:: c^\prime_\Dimension = c_\Dimension \oplus x_{\Dimension - 1} y_{\Dimension - 1} \oplus c^\prime_{\Dimension - 1} (x_{\Dimension - 1} \oplus y_{\Dimension - 1}).

It is non-zero when the sum of the most-significant qubits (plus carry) "wraps around" (due to the modular arithmetic), and so represents the case where the total resulting sum is too big to be encoded with just :math:`\Dimension` qubits, a situation known as *integer overflow*. If the value of this qubit is not required, then the circuit can be simplified by removing the last CARRY, the lone CNOT, and the qubit itself.

Implementation
--------------

In this implementation, the dimensionality of the input state can be decreased by removing the overflow qubit (via ``overflow_qubit = False``), thereby reducing the execution time of the algorithm.

.. literalinclude:: /text/examples/algorithms/adder_lookahead.py
   :name: code:adder_lookahead
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

When ``overflow_qubit = True``:

.. code:: python

   >>> adder.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

When ``overflow_qubit = False``:

.. code:: python

   >>> adder.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead_false-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead_false-light.png
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
   |x⟩ = |1,0⟩

.. code:: python

   >>> addend_state.print()
   |y⟩ = |1,0⟩

.. code:: python

   >>> sum_state.print()
   |s⟩ = |0,1⟩

Results
^^^^^^^

.. code:: python

   >>> print(computation)
   Computation: 1 + 1 = 2

When ``overflow_qubit = True``:

.. code:: python

   >>> print(duration)
   Duration: 5.815 seconds

When ``overflow_qubit = False``:

.. code:: python

   >>> print(duration)
   Duration: 1.469 seconds

This version of a multi-qubit full adder is evidently much faster than the :ref:`eg:adder_ripple` for the equivalent number of qubits, which highlights the efficiency advantage of using fewer qubits to achieve the same computation.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage