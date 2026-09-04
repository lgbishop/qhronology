.. _`eg:teleportation`:

Quantum teleportation
=====================

Description
-----------

Quantum teleportation :cite:p:`bennett_teleporting_1993` is a notable technique of quantum theory in which the transfer of quantum information between two parties (that may be spatially separated) is achieved. Importantly, this does not involve the movement of physical entities, but concerns rather the relocation of the (quantum) statistics of a physical system (manifesting as a quantum state) to another. This is often facilitated by a pair of entangled particles, the statistical correlations of which provide the actual mechanism of teleportation.

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

Protocol
--------

The canonical protocol of quantum teleportation involves three qubits divided across two parties, which are often referred to as :math:`A` and :math:`B` and contain two qubits and one qubit, respectively. These are initialized in the state

.. math:: \ket{\Psi_0} = \ket{\psi}^{\indices{A_0}} \otimes \ket{0}^{\indices{A_1}} \otimes \ket{0}^{\indices{B}}

where :math:`\ket{\psi}` is the state to be teleported. In our treatment here, we will, without loss of generality, write this state in the explicit form,

.. math:: \ket{\psi} \equiv a \ket{0} + b \ket{1}, \quad a,b \in \Complexes,

which is assumed to be normalized, e.g., :math:`\braket{\psi}{\psi} = \abs{a}^2 + \abs{b}^2 = 1`.

We first apply to this a Hadamard gate followed by a controlled-NOT, which entangles the last two qubits (:math:`A_1` and :math:`B`), forming a Bell state (:math:`\bigl|\Phi^+\bigr\rangle`) on these systems,

.. math::

   \begin{aligned}
       \ket{\Psi_1} &= \Control^{\indices{A_1}}\NOT^{\indices{B}} \cdot \Hadamard^{\indices{A_1}} \ket{\Psi_0} \\
       &= \ket{\psi} \otimes \bigl|\Phi^+\bigr\rangle.
   \end{aligned}

This creates a quantum channel between the two parties, across which quantum information of the two entangled qubits is coupled (or shared).

It is at this point where a degree of physical (spatial) separation is manifested between the two parties. The "teleportation" phenomenon is then realized when the complete state of the first qubit :math:`\ket{\psi}` is reconstructed (thereby destroying the original qubit) on the last system. This is achieved via the transmission of (classical) information about the state through a classical communication channel between parties :math:`A` and :math:`B`. To accomplish this, the first two qubits are transformed by a controlled-NOT gate and a Hadamard gate, yielding the superposition

.. math::

   \begin{aligned}
       \ket{\Psi_2} &= \Hadamard^{\indices{A_0}} \cdot \Control^{\indices{A_1}}\NOT^{\indices{A_1}} \ket{\Psi_1} \\
       &= a \ket{+} \otimes \bigl|\Phi^+\bigr\rangle + b \ket{-} \otimes \bigl|\Psi^+\bigr\rangle.
   \end{aligned}

These qubits (party :math:`A`) are then measured in the computational basis, and the outcomes of these measurements are used to determine the operations to be performed on :math:`B`. For any input state :math:`\ket{\psi}`, the probabilities are found to be uniform, i.e.,

.. math::

   \begin{aligned}
       p_0^{\indices{A_0}} &= p_1^{\indices{A_0}} = \frac{1}{2}, \\
       p_0^{\indices{A_1}} &= p_1^{\indices{A_1}} = \frac{1}{2},
   \end{aligned}

and so all four of the possible outcomes (each of the form :math:`\ket{u} \otimes \ket{v}`) are equiprobabilistic. Depending on the outcome, the :math:`B` qubit is then transformed in a particular way:

- If :math:`u = 1`, then a Pauli-:math:`Z` gate (phase flip) is performed.
- If :math:`v = 1`, then a Pauli-:math:`X` gate (bit flip) is performed.

This corresponds to two bits of information transmitted over a classical communication channel from party :math:`A` to :math:`B`. :numref:`table:teleportation` summarizes this procedure.

.. list-table:: Measurements in the quantum teleportation protocol.
   :name: table:teleportation
   :widths: 8 8 6
   :header-rows: 1

   * - **Outcome**
     - **Probability**
     - **Transformation**
   * - :math:`\ket{0} \otimes \ket{0}`
     - :math:`p_{00} = p_{0} p_{0} = \frac{1}{4}`
     - :math:`\Identity`
   * - :math:`\ket{1} \otimes \ket{0}`
     - :math:`p_{10} = p_{1} p_{0} = \frac{1}{4}`
     - :math:`\PauliZ`
   * - :math:`\ket{0} \otimes \ket{1}`
     - :math:`p_{01} = p_{0} p_{1} = \frac{1}{4}`
     - :math:`\PauliX`
   * - :math:`\ket{1} \otimes \ket{1}`
     - :math:`p_{11} = p_{1} p_{1} = \frac{1}{4}`
     - :math:`\PauliZ \PauliX`

.. raw:: latex

   \newpage

As this measurement-dependent transformation procedure concerns the exchange of purely classical information, it is depicted in the quantum circuit diagram as a pair of Pauli-:math:`X` annd Pauli-:math:`Z` gates with *classical* controls, with each classical wire connected to their respective measurement. After performing the pair of measurements and their associated transformations, the initial state on :math:`A_1` is perfectly reconstructed on :math:`B`, which is interpreted as :math:`\ket{\psi}` having "teleported" between two physically separated systems.

Implementation
--------------

.. raw:: latex

   \enlargethispage{-\baselineskip}

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
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_teleportation-light.png
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

   \enlargethispage{\baselineskip}

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