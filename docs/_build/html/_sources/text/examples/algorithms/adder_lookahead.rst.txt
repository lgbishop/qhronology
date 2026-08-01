.. _`eg:adder_lookahead`:

Carry-lookahead adder
=====================

Description
-----------

A quantum *carry-lookahead* adder, proposed by Vedral et al. :cite:p:`vedral_quantum_1996`, is another style of multi-qubit adder and appears in :numref:`fig:circuit_algorithm_adder_lookahead`. It consists of two phases: in the first, the carry qubits are computed, while in the second, the sums (taking into account the value of the carry qubits) are computed (in addition to the carry qubits being reverted back to their original values). Note that in this implementation, the order of the qubits in the encoding is reversed, such that the least-significant qubits are at the top while the most-significant qubits are at the bottom.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_lookahead-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a quantum carry-lookahead adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_lookahead-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a quantum carry-lookahead adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_lookahead-light.png
   :name: fig:circuit_algorithm_adder_lookahead
   :scale: 34 %
   :alt: A quantum circuit diagram of a quantum carry-lookahead adder.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A two-qubit quantum carry-lookahead adder.

.. raw:: latex

   \vspace*{-\baselineskip}

The values of the summation qubits can be determined to be

.. math::

   s_i =
       \begin{cases}
           x_0 \oplus y_0 \oplus c_0, & \text{if } i = 0; \\
           x_i \oplus y_i \oplus c^\prime_i, & \text{if } i > 0. \\
       \end{cases}

This version of an adder resets all output carry qubits to their original input values. The intermediary carry values however are

.. math::

   c^\prime_i =
       \begin{cases}
           c_1 \oplus x_0 y_0 \oplus c_0 (x_0 \oplus y_0), & \text{if } i = 1; \\
           c_i \oplus x_{i - 1} y_{i - 1} \oplus c^\prime_{i - 1} (x_{i - 1} \oplus y_{i - 1}), & \text{if } i > 1. \\
       \end{cases}

The last qubit is simply an overflow qubit and has the value

.. math:: c^\prime_\Dimension = c_\Dimension \oplus x_{\Dimension - 1} y_{\Dimension - 1} \oplus c^\prime_{\Dimension - 1} (x_{\Dimension - 1} \oplus y_{\Dimension - 1}).

It is non-zero when the sum of the most-significant qubits (plus carry) "wraps around" (due to the modular arithmetic), and so represents the case where the total resulting sum is too big to be encoded with just :math:`\Dimension` qubits, a situation known as *integer overflow*. If the value of this qubit is not required, then the circuit can be simplified by removing the last CARRY, the lone CNOT, and the qubit itself.

Implementation
--------------

In this implementation, the dimensionality of the input state can be decreased by removing the overflow qubit (via :python:`overflow_qubit = False`), thereby reducing the execution time of the algorithm.

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. raw:: latex

   \begin{codetitled}{Carry-lookahead adder}{}

.. literalinclude:: /text/examples/algorithms/adder_lookahead.py
   :name: code:adder_lookahead
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

Diagram
^^^^^^^

When :python:`overflow_qubit = True`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> adder.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_adder_lookahead.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

.. raw:: latex

   \enlargethispage{\baselineskip}

When :python:`overflow_qubit = False`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> adder.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_adder_lookahead_false.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead_false-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_lookahead_false-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

States
^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> augend_state.print()
   |x⟩ = |1,0⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> addend_state.print()
   |y⟩ = |1,0⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> sum_state.print()
   |s⟩ = |0,1⟩

.. raw:: latex

   \end{code}

Results
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(f"Computation: {computation}")
   Computation: 1 + 1 = 2

.. raw:: latex

   \end{code}

When :python:`overflow_qubit = True`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(f"Duration: {duration} seconds")
   Duration: 0.057 seconds

.. raw:: latex

   \end{code}

When :python:`overflow_qubit = False`:

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(f"Duration: {duration} seconds")
   Duration: 0.028 seconds

.. raw:: latex

   \end{code}

This version of a multi-qubit full adder is evidently much faster than the :numref:`eg:adder_ripple` :ref:`eg:adder_ripple` for the equivalent number of qubits, which highlights the efficiency advantage of using fewer qubits to achieve the same computation.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage