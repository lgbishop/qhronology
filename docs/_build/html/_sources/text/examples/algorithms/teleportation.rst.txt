.. _`eg:teleportation`:

Quantum teleportation
=====================

Description
-----------

Quantum teleportation :cite:p:`bennett_teleporting_1993` is a significant technique of quantum theory in which the transfer of quantum information between two parties (that may be spatially separated) is achieved. Importantly, this does not involve the movement of physical entities, but concerns rather the relocation of the (quantum) statistics of a physical system (manifesting as a quantum state) to another. This is often facilitated by a pair of entangled particles, the statistical correlations of which provide the actual mechanism of teleportation.

Note that in the process of teleporting the state, the original is destroyed, and so the no-cloning theorem remains unviolated. Additionally, because classical information needs to be sent between the two parties, the teleportation cannot occur faster than the speed of light, meaning that the laws of (special) relativity are satisfied. This example (:numref:`fig:circuit_algorithm_teleportation`) implements the canonical version of the algorithm.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_teleportation-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a quantum teleportation protocol.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_teleportation-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a quantum teleportation protocol.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_teleportation-light.png
   :name: fig:circuit_algorithm_teleportation
   :scale: 34 %
   :alt: A quantum circuit diagram of a quantum teleportation protocol.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum teleportation protocol.

.. raw:: latex

   \vspace*{-\baselineskip}

Implementation
--------------

.. raw:: latex

   \begin{codetitled}{Quantum teleportation}{}

.. literalinclude:: /text/examples/algorithms/teleportation.py
   :name: code:teleportation
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

   >>> teleporter.diagram(force_separation=True)

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_teleportation.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_teleportation-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_teleportation-light.png
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

   >>> teleporting_state.print()
   |ψ⟩ = a|0⟩ + b|1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> teleported_state.print()
   ρ = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

.. raw:: latex

   \end{code}

Results
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> teleporting_state.distance(teleported_state)
   0

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> teleporting_state.fidelity(teleported_state)
   1

.. raw:: latex

   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage