.. _`eg:toffoli`:

Toffoli decomposition
=====================

Description
-----------

An important research subfield of quantum computing involves the (de)construction of complex gates using sets of more primitive gates. This is termed *decomposition*, and mostly concerns the task of finding the (most) minimal *gate set* (i.e., most restricted) for any given gate. It is an interesting problem as primitive gates are in fact usually the only gates which can be directly implemented in many physical quantum computers. Consequently, finding compositions of such primitives that correctly reconstruct more complex gates is necessary in the pursuit of executing more advanced algorithms. Balancing the *depth* of the circuit (i.e., the longest path along its wires from input to output) with minimizing the size of the gate set also forms an avenue of research, as a circuit's depth generally correlates with its execution time (discounting any execution time differences between the various types of gates).

The Toffoli gate, also known as the CCNOT gate (see :numref:`eg:ccnot` :ref:`eg:ccnot`), is one such gate that can be decomposed into more primitive gates. As it is an *entangling* gate, the Toffoli's gate set must include more than just the single-qubit rotation gates (such as the :math:`\op{T}` gate), as all such gates describe *non-entangling* operations. Thus, one such set of gates consists of the Hadamard gate :math:`\Hadamard` and the CNOT gate, in addition to the :math:`\op{T}` gate (fourth root of :math:`\op{Z}`, i.e., :math:`\op{Z}^{1/4}`). Using this restricted set, one possible decomposition of the Toffoli gate appears in :numref:`fig:circuit_algorithm_toffoli`. Note that the conjugate transpose of any gate in the set, e.g., :math:`\op{T}^\dagger`, is considered to also be in the set.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_toffoli-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting a decomposition of the Toffoli gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_toffoli-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram depicting a decomposition of the Toffoli gate.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_toffoli-light.png
   :name: fig:circuit_algorithm_toffoli
   :scale: 34 %
   :alt: A quantum circuit diagram depicting a decomposition of the Toffoli gate.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A decomposition of the Toffoli gate.

.. raw:: latex

   \vspace*{-\baselineskip}

Implementation
--------------

.. raw:: latex

   \begin{codetitled}{Toffoli decomposition}{}

.. literalinclude:: /text/examples/algorithms/toffoli.py
   :name: code:toffoli
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

   >>> toffoli.diagram(force_separation=True, visible={"gates"})

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_toffoli.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_toffoli-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_toffoli-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

Gate
^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> toffoli.gate()
   Matrix([
   [1, 0, 0, 0, 0, 0, 0, 0],
   [0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0],
   [0, 0, 0, 0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 1],
   [0, 0, 0, 0, 0, 0, 1, 0]])

.. raw:: latex

   \end{code}

.. raw:: latex
   
   \newpage