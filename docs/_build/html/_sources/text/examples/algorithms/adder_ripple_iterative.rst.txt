.. _`eg:adder_ripple_iterative`:

Ripple-carry adder (iterative)
==============================

Description
-----------

This example builds upon the four-qubit ripple-carry adder in :ref:`eg:adder_ripple`. The implementation here simplifies the algorithm by instead applying copies of the circuit successively to a tetrapartite input state, which is a composition of the augend, addend, carry, and zero states. As a result, the sequence of trace operations (necessary to isolate the output sum and carry states) mixes the pure (vector) input composition, thereby destroying linearity of the evolution in the input states. This means that only mixed states for each qubit in the output sum state can be recovered, and so we can only sum single integers, not *superpositions* of integers. However, keeping the Hilbert space to a smaller total dimensionality at any one time makes the computations *much* faster, and so we can work with significantly larger integers.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_ripple_iterative-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of one iteration of a multi-qubit quantum ripple-carry adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_ripple_iterative-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of one iteration of a multi-qubit quantum ripple-carry adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_ripple_iterative-light.png
   :name: fig:circuit_algorithm_adder_ripple_iterative
   :scale: 34 %
   :alt: A quantum circuit diagram of one iteration of a multi-qubit quantum ripple-carry adder.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   One iteration of a multi-qubit quantum ripple-carry adder.

Implementation
--------------

In this example, each qubit in the uppermost set on the diagram corresponds to the leftmost (most-significant) qubit in their respective encoded state, while each qubit in the lowermost set similarly corresponds to the rightmost (least-significant) qubit.

.. raw:: latex

   \begin{codetitled}{Ripple-carry adder (iterative)}{}

.. literalinclude:: /text/examples/algorithms/adder_ripple_iterative.py
   :name: code:adder_ripple_iterative
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

   >>> adder.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 -0.10cm]{text_examples_algorithms_adder_ripple_iterative.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_ripple_iterative-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_adder_ripple_iterative-light.png
         :scale: 40 %
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
   |x⟩ = |0,0,0,1,1,1,1,1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> addend_state.print()
   |y⟩ = |1,1,0,1,1,0,0,1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> sum_state.print()
   |s⟩ = |1,1,1,1,1,0,0,0⟩

.. raw:: latex

   \end{code}

Results
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(computation)
   Computation: 31 + 217 = 248

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> print(duration)
   Duration: 3.264 seconds

.. raw:: latex

   \end{code}

Much faster and for much larger numbers than the linear implementation in :ref:`eg:adder_ripple`.

.. raw:: latex
   
   \newpage