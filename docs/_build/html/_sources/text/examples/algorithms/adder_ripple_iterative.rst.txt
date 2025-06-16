.. _`eg:adder_ripple_iterative`:

Ripple-carry adder (iterative)
==============================

Description
-----------

This example builds upon the four-qubit ripple-carry adder in :ref:`eg:adder_ripple`. The implementation here simplifies the algorithm by instead applying copies of the circuit successively to a tetrapartite input state, which is a composition of the augend, addend, carry, and zero states. As a result, the sequence of trace operations (necessary to isolate the output sum and carry states) mixes the pure (vector) input composition, thereby destroying linearity of the evolution in the input states. This means that only mixed states for each qubit in the output sum state can be recovered, and so we can only sum single integers, not *superpositions* of integers. However, keeping the Hilbert space to a smaller total dimensionality at any one time makes the computations *much* faster, and so we can work with significantly larger integers.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_adder_ripple_iterative-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of one iteration of a multi-qubit quantum ripple-carry adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_adder_ripple_iterative-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of one iteration of a multi-qubit quantum ripple-carry adder.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_adder_ripple_iterative-light.png
   :name: fig:circuit_algorithm_adder_ripple_iterative
   :scale: 36 %
   :alt: A quantum circuit diagram of one iteration of a multi-qubit quantum ripple-carry adder.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   One iteration of a multi-qubit quantum ripple-carry adder.

Implementation
--------------

In this example, each qubit in the uppermost set on the diagram corresponds to the leftmost (most-significant) qubit in their respective encoded state, while each qubit in the lowermost set similarly corresponds to the rightmost (least-significant) qubit.

.. literalinclude:: /text/examples/algorithms/adder_ripple_iterative.py
   :name: code:adder_ripple_iterative
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

      .. image:: /figures/output/text_examples_algorithms_adder_ripple_iterative-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_adder_ripple_iterative-light.png
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
   |x⟩ = |0,0,0,1,1,1,1,1⟩

.. code:: python

   >>> addend_state.print()
   |y⟩ = |1,1,0,1,1,0,0,1⟩

.. code:: python

   >>> sum_state.print()
   |s⟩ = |1,1,1,1,1,0,0,0⟩

Results
^^^^^^^

.. code:: python

   >>> print(computation)
   Computation: 31 + 217 = 248

.. code:: python

   >>> print(duration)
   Duration: 3.621 seconds

Much faster and for much larger numbers than the linear implementation in :ref:`eg:adder_ripple`.

.. raw:: latex
   
   \newpage