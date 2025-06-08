.. _`eg:toffoli`:

Toffoli decomposition
=====================

Description
-----------

An important research subfield of quantum computing involves the (de)construction of complex gates using sets of more primitive gates. This is termed *decomposition*, and mostly concerns the task of finding the (most) minimal *gate set* (i.e., most restricted) for any given gate. It is an interesting problem as primitive gates are in fact usually the only gates which can be directly implemented in many physical quantum computers. Consequently, finding compositions of such primitives that correctly reconstruct more complex gates is necessary in the pursuit of executing more advanced algorithms. Balancing the *depth* of the circuit (i.e., the longest path along its wires from input to output) with minimizing the size of the gate set also forms an avenue of research, as a circuit's depth generally correlates with its execution time (discounting any execution time differences between the various types of gates).

The Toffoli gate, also known as the CCNOT gate (see :ref:`Example: CCNOT <eg:ccnot>`), is one such gate that can be decomposed into more primitive gates. As it is an *entangling* gate, the Toffoli's gate set must include more than just the single-qubit rotation gates (such as the :math:`\op{T}` gate), as all such gates describe *non-entangling* operations. Thus, one such set of gates consists of the Hadamard gate :math:`\Hadamard` and the CNOT gate, in addition to the :math:`\op{T}` gate (fourth root of :math:`\op{Z}`, i.e., :math:`\op{Z}^{\tfrac{1}{4}}`). Using this restricted set, one possible decomposition of the Toffoli gate appears in :numref:`fig:circuit_algorithm_toffoli`. Note that the conjugate transpose of any gate in the set, e.g., :math:`\op{T}^\dagger`, is considered to also be in the set.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_toffoli-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting one possible decomposition of the Toffoli gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_toffoli-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram depicting one possible decomposition of the Toffoli gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_toffoli-light.png
   :name: fig:circuit_algorithm_toffoli
   :scale: 36 %
   :alt: A quantum circuit diagram depicting one possible decomposition of the Toffoli gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   One possible decomposition of the Toffoli gate.

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/toffoli.py
   :name: code:toffoli
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> circuit.diagram(force_separation = True)

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_toffoli-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_toffoli-light.png
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