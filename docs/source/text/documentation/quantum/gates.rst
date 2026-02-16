.. include:: /styles.rst

.. _`sec:docs_gates`:

*****
Gates
*****

Quantum logic gates provide the building blocks for describing quantum operations, which are usually either (unitary) interactions between two or more (sub)systems, or (linear) transformations of any number of systems. In Qhronology, they are represented by instances of the :py:class:`~qhronology.quantum.gates.QuantumGate` base class,

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.gates import QuantumGate

.. raw:: latex

   \end{code}

and its derivatives (subclasses),

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.gates import Pauli, GellMann, Rotation, Phase, Diagonal, Swap, Summation, Not, Hadamard, Fourier, Measurement

.. raw:: latex

   \end{code}

These objects describe a distinct vertical "slice" in the quantum circuit picturalism, and so include information about the locations of both control and anticontrol nodes, in addition to the presence of any empty wires. They also possess other metadata associated with the gate such as parameter values, symbolic assumptions, and algebraic conditions.

Facilities to combine gates together are also provided by the package and take two forms: "interleaved" compositions via the :py:class:`~qhronology.quantum.gates.GateInterleave` class, and "stacked" compositions via the :py:class:`~qhronology.quantum.gates.GateStack` class:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.gates import GateInterleave, GateStack

.. raw:: latex

   \end{code}

Both of these classes concern the creation of more complex spatial ("vertical") gate structures. Temporal ("horizontal") compositions (i.e., gates wired in serial) as single object instances on the other hand are not supported, as this can be achieved simply by combining the individual components sequentially in a circuit.

Main class
==========

.. autoclass:: qhronology.quantum.gates.QuantumGate
   :show-inheritance:

   .. raw:: latex

      \newpage

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> U = QuantumGate(spec=unitary, label="U")
      >>> U.output()
      Matrix([
      [U[0, 0], U[0, 1]],
      [U[1, 0], U[1, 1]]])
      >>> U.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_u.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 3, 3).as_mutable()
      >>> U3 = QuantumGate(spec=unitary, dim=3, label="U")
      >>> U3.output()
      Matrix([
      [U[0, 0], U[0, 1], U[0, 2]],
      [U[1, 0], U[1, 1], U[1, 2]],
      [U[2, 0], U[2, 1], U[2, 2]]])
      >>> U3.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_u3.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_u3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> UI = QuantumGate(
      ...     spec=unitary,
      ...     targets=[0],
      ...     num_systems=2,
      ...     label="U",
      ... )
      >>> UI.output()
      Matrix([
      [U[0, 0],       0, U[0, 1],       0],
      [      0, U[0, 0],       0, U[0, 1]],
      [U[1, 0],       0, U[1, 1],       0],
      [      0, U[1, 0],       0, U[1, 1]]])
      >>> UI.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_ui.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_ui-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_ui-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> IU = QuantumGate(
      ...     spec=unitary,
      ...     targets=[1],
      ...     num_systems=2,
      ...     label="U",
      ... )
      >>> IU.output()
      Matrix([
      [U[0, 0], U[0, 1],       0,       0],
      [U[1, 0], U[1, 1],       0,       0],
      [      0,       0, U[0, 0], U[0, 1]],
      [      0,       0, U[1, 0], U[1, 1]]])
      >>> IU.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_iu.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_iu-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_iu-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 4, 4).as_mutable()
      >>> UU = QuantumGate(
      ...     spec=unitary,
      ...     targets=[0, 1],
      ...     num_systems=2,
      ...     label="U",
      ... )
      >>> UU.output()
      Matrix([
      [U[0, 0], U[0, 1], U[0, 2], U[0, 3]],
      [U[1, 0], U[1, 1], U[1, 2], U[1, 3]],
      [U[2, 0], U[2, 1], U[2, 2], U[2, 3]],
      [U[3, 0], U[3, 1], U[3, 2], U[3, 3]]])
      >>> UU.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_uu.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_uu-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_uu-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> CU = QuantumGate(
      ...     spec=unitary,
      ...     targets=[1],
      ...     controls=[0],
      ...     label="U",
      ... )
      >>> CU.output()
      Matrix([
      [1, 0,       0,       0],
      [0, 1,       0,       0],
      [0, 0, U[0, 0], U[0, 1]],
      [0, 0, U[1, 0], U[1, 1]]])
      >>> CU.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_cu.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_cu-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_cu-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> UC = QuantumGate(
      ...     spec=unitary,
      ...     targets=[0],
      ...     controls=[1],
      ...     label="U",
      ... )
      >>> UC.output()
      Matrix([
      [1,       0, 0,       0],
      [0, U[0, 0], 0, U[0, 1]],
      [0,       0, 1,       0],
      [0, U[1, 0], 0, U[1, 1]]])
      >>> UC.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_uc.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_uc-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_uc-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{-\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> AU = QuantumGate(
      ...     spec=unitary,
      ...     targets=[1],
      ...     anticontrols=[0],
      ...     label="U",
      ... )
      >>> AU.output()
      Matrix([
      [U[0, 0], U[0, 1], 0, 0],
      [U[1, 0], U[1, 1], 0, 0],
      [      0,       0, 1, 0],
      [      0,       0, 0, 1]])
      >>> AU.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_au.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_au-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_au-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> CCU = QuantumGate(
      ...     spec=unitary,
      ...     targets=[2],
      ...     controls=[0, 1],
      ...     label="U",
      ... )
      >>> CCU.output()
      Matrix([
      [1, 0, 0, 0, 0, 0,       0,       0],
      [0, 1, 0, 0, 0, 0,       0,       0],
      [0, 0, 1, 0, 0, 0,       0,       0],
      [0, 0, 0, 1, 0, 0,       0,       0],
      [0, 0, 0, 0, 1, 0,       0,       0],
      [0, 0, 0, 0, 0, 1,       0,       0],
      [0, 0, 0, 0, 0, 0, U[0, 0], U[0, 1]],
      [0, 0, 0, 0, 0, 0, U[1, 0], U[1, 1]]])
      >>> CCU.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_ccu.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_ccu-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_ccu-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> AUC = QuantumGate(
      ...     spec=unitary,
      ...     targets=[1],
      ...     controls=[2],
      ...     anticontrols=[0],
      ...     label="U",
      ... )
      >>> AUC.output()
      Matrix([
      [1,       0, 0,       0, 0, 0, 0, 0],
      [0, U[0, 0], 0, U[0, 1], 0, 0, 0, 0],
      [0,       0, 1,       0, 0, 0, 0, 0],
      [0, U[1, 0], 0, U[1, 1], 0, 0, 0, 0],
      [0,       0, 0,       0, 1, 0, 0, 0],
      [0,       0, 0,       0, 0, 1, 0, 0],
      [0,       0, 0,       0, 0, 0, 1, 0],
      [0,       0, 0,       0, 0, 0, 0, 1]])
      >>> AUC.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_custom_auc.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_auc-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_custom_auc-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_gates_properties`:

Constructor argument properties
-------------------------------

.. autoproperty:: qhronology.quantum.gates.QuantumGate.spec

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.targets

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.controls

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.anticontrols

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.num_systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.dim

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.symbols

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.conditions

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.conjugate

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.exponent

.. raw:: latex

   \newpage

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.coefficient

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.label

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.notation

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.family

.. raw:: latex

   \hrulefillthick

Read-only properties
--------------------

.. autoproperty:: qhronology.quantum.gates.QuantumGate.systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.gates.QuantumGate.matrix

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_gates_methods`:

Methods
-------

.. raw:: latex

   \enlargethispage{-2\baselineskip}

.. automethod:: qhronology.quantum.gates.QuantumGate.output

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.gates.QuantumGate.print

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
      >>> U = QuantumGate(
      ...     spec=unitary,
      ...     dim=2,
      ...     label="U",
      ... )
      >>> U.output()
      Matrix([
      [U[0, 0], U[0, 1]],
      [U[1, 0], U[1, 1]]])
      >>> U.print()
      U = U[0, 0]|0⟩⟨0| + U[0, 1]|0⟩⟨1| + U[1, 0]|1⟩⟨0| + U[1, 1]|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> unitary = sp.MatrixSymbol("U", 4, 4).as_mutable()
      >>> UU = QuantumGate(
      ...     spec=unitary,
      ...     targets=[0, 1],
      ...     dim=2,
      ...     label="UU",
      ... )
      >>> UU.output()
      Matrix([
      [U[0, 0], U[0, 1], U[0, 2], U[0, 3]],
      [U[1, 0], U[1, 1], U[1, 2], U[1, 3]],
      [U[2, 0], U[2, 1], U[2, 2], U[2, 3]],
      [U[3, 0], U[3, 1], U[3, 2], U[3, 3]]])
      >>> UU.print()
      UU = U[0, 0]|0,0⟩⟨0,0| + U[0, 1]|0,0⟩⟨0,1| + U[0, 2]|0,0⟩⟨1,0| + U[0, 3]|0,0⟩⟨1,1| + U[1, 0]|0,1⟩⟨0,0| + U[1, 1]|0,1⟩⟨0,1| + U[1, 2]|0,1⟩⟨1,0| + U[1, 3]|0,1⟩⟨1,1| + U[2, 0]|1,0⟩⟨0,0| + U[2, 1]|1,0⟩⟨0,1| + U[2, 2]|1,0⟩⟨1,0| + U[2, 3]|1,0⟩⟨1,1| + U[3, 0]|1,1⟩⟨0,0| + U[3, 1]|1,1⟩⟨0,1| + U[3, 2]|1,1⟩⟨1,0| + U[3, 3]|1,1⟩⟨1,1|
      >>> UU.print(product=True)
      UU = U[0, 0]|0⟩⟨0|⊗|0⟩⟨0| + U[0, 1]|0⟩⟨0|⊗|0⟩⟨1| + U[0, 2]|0⟩⟨1|⊗|0⟩⟨0| + U[0, 3]|0⟩⟨1|⊗|0⟩⟨1| + U[1, 0]|0⟩⟨0|⊗|1⟩⟨0| + U[1, 1]|0⟩⟨0|⊗|1⟩⟨1| + U[1, 2]|0⟩⟨1|⊗|1⟩⟨0| + U[1, 3]|0⟩⟨1|⊗|1⟩⟨1| + U[2, 0]|1⟩⟨0|⊗|0⟩⟨0| + U[2, 1]|1⟩⟨0|⊗|0⟩⟨1| + U[2, 2]|1⟩⟨1|⊗|0⟩⟨0| + U[2, 3]|1⟩⟨1|⊗|0⟩⟨1| + U[3, 0]|1⟩⟨0|⊗|1⟩⟨0| + U[3, 1]|1⟩⟨0|⊗|1⟩⟨1| + U[3, 2]|1⟩⟨1|⊗|1⟩⟨0| + U[3, 3]|1⟩⟨1|⊗|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.gates.QuantumGate.diagram

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   For usage examples, please see those of the :py:class:`~qhronology.quantum.gates.QuantumGate` class and its subclasses (:numref:`sec:docs_gates_subclasses` :ref:`sec:docs_gates_subclasses`).

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \newpage

.. _`sec:docs_gates_subclasses`:

Subclasses
==========

Most of the canonical gates used in standard quantum computing theory are implemented in Qhronology as an assortment of subclasses of the :py:class:`~qhronology.quantum.gates.QuantumGate` class. It is important to be aware of how, even though they share many of the same arguments and properties, the usage of these classes can differ greatly. This is especially true among a few distinct categorizations of gates, namely *dimensionality* and *compositionality*, which are summarized below:

.. raw:: latex

   \renewcommand{\arraystretch}{1}
   \renewcommand\cellgape{\Gape[2pt]}
   \renewcommand\cellset{\renewcommand\arraystretch{1}
   \setlength\extrarowheight{2pt}}
   \begin{center}
   \vspace{0.5cm}
   \begin{NiceTabular}{*{4}{c}}[corners,hvlines]
   & & \Block[c, fill=lightblue]{1-2}{\textbf{\textsf{Compositionality}}} \\
   & & \textit{\textsf{Unipartite}} & \textit{\textsf{Multipartite}} \\
   \Block[c, fill=lightblue]{2-1}{\textbf{\textsf{Dimensionality}}} & \textit{\textsf{Fixed}} &  \Block[l, respect-arraystretch]{}{\py{Pauli} \\ \py{GellMann} \\ \py{Rotation} \\ \py{Not}} & {\small \textsf{(none)}} \\
   & \textit{\textsf{Variable}} & \Block[l, respect-arraystretch]{}{\py{Phase} \\ \py{Diagonal} \\ \py{Hadamard} \\ \py{Summation}} & \Block[l, respect-arraystretch]{}{\py{Swap} \\ \py{Fourier} \\ \py{Measurement}} \\
   \end{NiceTabular}
   \captionof{table}{Classification of Qhronology's \py{QuantumGate} subclasses. Note that the \py{Swap} class can only describe bipartite gates, and so is not multipartite for any general number of systems. Also note that gates of the \py{Measurement} class can act on systems of any dimension but do not themselves possess a dimensionality.}\label{tbl:gate_classes}
   \end{center}

.. raw:: latex

   \renewcommand{\arraystretch}{1.25}

.. raw:: latex

   \vspace*{\baselineskip}

.. list-table:: Classifications and aliases of Qhronology's :py:class:`~qhronology.quantum.gates.QuantumGate` subclasses.
   :widths: 9 7 11 13
   :header-rows: 1
   :stub-columns: 1

   * - **Subclass**
     - **Alias**
     - **Dimensionality**
     - **Compositionality**
   * - :py:class:`~qhronology.quantum.gates.Pauli`
     - :python:`PAULI`
     - fixed (qubits)
     - unipartite
   * - :py:class:`~qhronology.quantum.gates.GellMann`
     - :python:`GM`
     - fixed (qutrits)
     - unipartite
   * - :py:class:`~qhronology.quantum.gates.Rotation`
     - :python:`ROT`
     - fixed (qubits)
     - unipartite
   * - :py:class:`~qhronology.quantum.gates.Phase`
     - :python:`PHS`
     - variable (qudits)
     - unipartite
   * - :py:class:`~qhronology.quantum.gates.Diagonal`
     - :python:`DIAG`
     - variable (qudits)
     - unipartite
   * - :py:class:`~qhronology.quantum.gates.Swap`
     - :python:`SWAP`
     - variable (qudits)
     - bipartite
   * - :py:class:`~qhronology.quantum.gates.Summation`
     - :python:`SUM`
     - variable (qudits)
     - unipartite
   * - :py:class:`~qhronology.quantum.gates.Not`
     - :python:`NOT`
     - fixed (qubits)
     - unipartite
   * - :py:class:`~qhronology.quantum.gates.Hadamard`
     - :python:`HAD`
     - variable (qudits)
     - unipartite, multipartite
   * - :py:class:`~qhronology.quantum.gates.Fourier`
     - :python:`QDFT`
     - variable (qudits)
     - unipartite, multipartite
   * - :py:class:`~qhronology.quantum.gates.Measurement`
     - :python:`METER`
     - variable (qudits)
     - multipartite

For the classes of fixed dimensionality, their constructors do not take :python:`dim` as an argument, nor can the associated property be set. For the classes describing unipartite gates, more than one system can still be targeted, in which case the gate's elementary matrix will simply be duplicated onto each system.

Please note that the documentation of these subclasses includes only properties and methods that are either new or modified from the base class :py:class:`~qhronology.quantum.gates.QuantumGate`.

.. note::

   In all of these subclasses, the :python:`spec` property should not be set.

.. autoclass:: qhronology.quantum.gates.Pauli
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> X = Pauli(index=1)
      >>> X.output()
      Matrix([
      [0, 1],
      [1, 0]])
      >>> X.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_pauli_x.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_x-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_x-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> Y = Pauli(index=2)
      >>> Y.output()
      Matrix([
      [0, -I],
      [I,  0]])
      >>> Y.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_pauli_y.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_y-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_y-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> Z = Pauli(index=3)
      >>> Z.output()
      Matrix([
      [1,  0],
      [0, -1]])
      >>> Z.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_pauli_z.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_z-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_z-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> I = Pauli(index=0)
      >>> I.output()
      Matrix([
      [1, 0],
      [0, 1]])
      >>> I.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_pauli_i.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_i-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_i-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> ZZ = Pauli(index=3, targets=[0, 1], label="Z⊗Z")
      >>> ZZ.output()
      Matrix([
      [1,  0,  0, 0],
      [0, -1,  0, 0],
      [0,  0, -1, 0],
      [0,  0,  0, 1]])
      >>> ZZ.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_pauli_zz.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_zz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_zz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> CZ = Pauli(index=3, targets=[1], controls=[0])
      >>> CZ.output()
      Matrix([
      [1, 0, 0,  0],
      [0, 1, 0,  0],
      [0, 0, 1,  0],
      [0, 0, 0, -1]])
      >>> CZ.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_pauli_cz.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_cz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_cz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{-\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> R_xx = Pauli(
      ...     index=1,
      ...     targets=[0, 1],
      ...     exponent="θ/pi",
      ...     coefficient="exp(-I*θ/2)",
      ...     label="R_xx(θ)",
      ... )
      >>> R_xx.output(simplify=True)
      Matrix([
      [   cos(θ/2),           0,           0, -I*sin(θ/2)],
      [          0,    cos(θ/2), -I*sin(θ/2),           0],
      [          0, -I*sin(θ/2),    cos(θ/2),           0],
      [-I*sin(θ/2),           0,           0,    cos(θ/2)]])
      >>> R_xx.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_pauli_rxx.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_rxx-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_pauli_rxx-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Pauli.index
      :no-index:

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.GellMann
   :show-inheritance:

   .. raw:: latex

      \vspace*{-\baselineskip}

   .. raw:: latex

      \enlargethispage{2\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> L = GellMann(index=8)
      >>> L.output()
      Matrix([
      [sqrt(3)/3,         0,            0],
      [        0, sqrt(3)/3,            0],
      [        0,         0, -2*sqrt(3)/3]])
      >>> L.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_gellmann_l.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_gellmann_l-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_gellmann_l-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> I = GellMann(index=0)
      >>> I.output()
      Matrix([
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]])
      >>> I.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_gellmann_i.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_gellmann_i-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_gellmann_i-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.GellMann.index
      :no-index:

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Rotation
   :show-inheritance:

   .. raw:: latex

      \vspace*{-0.85\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> R_x = Rotation(axis=1, angle="θ", label="R_x")
      >>> R_x.output()
      Matrix([
      [   cos(θ/2), -I*sin(θ/2)],
      [-I*sin(θ/2),    cos(θ/2)]])
      >>> R_x.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_rotation_x.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_x-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_x-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \vspace*{-0.25\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> R_y = Rotation(axis=2, angle="φ", label="R_y")
      >>> R_y.output()
      Matrix([
      [cos(φ/2), -sin(φ/2)],
      [sin(φ/2),  cos(φ/2)]])
      >>> R_y.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_rotation_y.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_y-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_y-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \vspace*{-0.25\baselineskip}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> R_z = Rotation(axis=3, angle="t", label="R_z")
      >>> R_z.output()
      Matrix([
      [exp(-I*t/2),          0],
      [          0, exp(I*t/2)]])
      >>> R_z.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_rotation_z.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_z-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_rotation_z-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Rotation.axis
      :no-index:

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Rotation.angle
      :no-index:

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Phase
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> P = Phase()
      >>> P.output()
      Matrix([
      [1,  0],
      [0, -1]])
      >>> P.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_phase_p.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> S = Phase(exponent=sp.Rational(1, 2), label="S")
      >>> S.output()
      Matrix([
      [1, 0],
      [0, I]])
      >>> S.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_phase_s.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_s-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_s-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> T = Phase(exponent=sp.Rational(1, 4), label="T")
      >>> T.output()
      Matrix([
      [1,           0],
      [0, exp(I*pi/4)]])
      >>> T.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_phase_t.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_t-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_t-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> P3 = Phase(dim=3)
      >>> P3.output()
      Matrix([
      [1,             0,              0],
      [0, exp(2*I*pi/3),              0],
      [0,             0, exp(-2*I*pi/3)]])
      >>> P3.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_phase_p3.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_p3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> W = Phase(phase="w", dim=3, label="W")
      >>> W.output()
      Matrix([
      [1, 0,    0],
      [0, w,    0],
      [0, 0, w**2]])
      >>> W.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_phase_w.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_w-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_phase_w-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Phase.phase
      :no-index:

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{-2\baselineskip}

.. autoclass:: qhronology.quantum.gates.Diagonal
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> D = Diagonal(entries={0: "u", 1: "v"})
      >>> D.output()
      Matrix([
      [u, 0],
      [0, v]])
      >>> D.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_diagonal_d.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_d-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_d-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> D3 = Diagonal(
      ...     entries={0: "a", 1: "b", 2: "c"},
      ...     dim=3,
      ... )
      >>> D3.output()
      Matrix([
      [a, 0, 0],
      [0, b, 0],
      [0, 0, c]])
      >>> D3.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_diagonal_d3.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_d3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_d3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> P = Diagonal(
      ...     entries={1: "p"},
      ...     exponentiation=True,
      ...     symbols={"p": {"real": True}},
      ...     label="P",
      ... )
      >>> P.output()
      Matrix([
      [1,        0],
      [0, exp(I*p)]])
      >>> P.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_diagonal_p.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_p-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_diagonal_p-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Diagonal.entries
      :no-index:

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Diagonal.exponentiation
      :no-index:

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Swap
   :show-inheritance:

   .. raw:: latex

      \vspace*{-0.35\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> S = Swap(targets=[0, 1])
      >>> S.output()
      Matrix([
      [1, 0, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 1]])
      >>> S.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_swap_s.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> S3 = Swap(targets=[0, 1], dim=3)
      >>> S3.output()
      Matrix([
      [1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1]])
      >>> S3.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_swap_s3.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_s3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> SIS = Swap(targets=[0, 2])
      >>> SIS.output()
      Matrix([
      [1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0],
      [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1]])
      >>> SIS.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_swap_sis.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_sis-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_sis-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> CSWAP = Swap(targets=[1, 2], controls=[0])
      >>> CSWAP.output()
      Matrix([
      [1, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1]])
      >>> CSWAP.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_swap_cswap.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_cswap-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_cswap-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> SCS = Swap(targets=[0, 2], controls=[1])
      >>> SCS.output()
      Matrix([
      [1, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1]])
      >>> SCS.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_swap_scs.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_scs-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_scs-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> RSWAP = Swap(
      ...     targets=[0, 1],
      ...     exponent=sp.Rational(1, 2),
      ...     label="√SWAP",
      ...     family="GATE",
      ... )
      >>> RSWAP.output()
      Matrix([
      [1,         0,         0, 0],
      [0, 1/2 + I/2, 1/2 - I/2, 0],
      [0, 1/2 - I/2, 1/2 + I/2, 0],
      [0,         0,         0, 1]])
      >>> RSWAP.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_swap_rswap.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_rswap-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_rswap-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> PSWAP = Swap(
      ...     targets=[0, 1],
      ...     exponent="p",
      ...     symbols={"p": {"real": True}},
      ...     label="SWAP^p",
      ...     family="GATE",
      ... )
      >>> PSWAP.output()
      Matrix([
      [1,                   0,                   0, 0],
      [0, exp(I*pi*p)/2 + 1/2, 1/2 - exp(I*pi*p)/2, 0],
      [0, 1/2 - exp(I*pi*p)/2, exp(I*pi*p)/2 + 1/2, 0],
      [0,                   0,                   0, 1]])
      >>> PSWAP.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_swap_pswap.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_pswap-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_swap_pswap-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{\baselineskip}

.. autoclass:: qhronology.quantum.gates.Summation
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> SUM = Summation(shift=1)
      >>> SUM.output()
      Matrix([
      [0, 1],
      [1, 0]])
      >>> SUM.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 0.02cm]{text_examples_docstrings_gate_summation_sum.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> SUM3 = Summation(shift=1, dim=3)
      >>> SUM3.output()
      Matrix([
      [0, 0, 1],
      [1, 0, 0],
      [0, 1, 0]])
      >>> SUM3.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 0.02cm]{text_examples_docstrings_gate_summation_sum3.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_summation_sum3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Summation.shift
      :no-index:

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Not
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> N = Not()
      >>> N.output()
      Matrix([
      [0, 1],
      [1, 0]])
      >>> N.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_not_n.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_n-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_n-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. .. raw:: latex

   ..    \begin{code}

   .. .. code:: python

   ..    >>> NN = Not(targets=[0, 1])
   ..    >>> NN.output()
   ..    Matrix([
   ..    [0, 0, 0, 1],
   ..    [0, 0, 1, 0],
   ..    [0, 1, 0, 0],
   ..    [1, 0, 0, 0]])
   ..    >>> NN.diagram()

   .. .. raw:: latex
      
   ..    \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_not_nn.pdf}
   ..    \vspace{-1\baselineskip}

   .. ..

   ..    .. only:: html

   ..       .. image:: /figures/output/text_examples_docstrings_gate_not_nn-dark.png
   ..          :scale: 40 %
   ..          :align: left
   ..          :class: only-dark

   ..    .. only:: html

   ..       .. image:: /figures/output/text_examples_docstrings_gate_not_nn-light.png
   ..          :scale: 40 %
   ..          :align: left
   ..          :class: only-light

   .. .. raw:: latex

   ..    \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> CNOT = Not(targets=[1], controls=[0])
      >>> CNOT.output()
      Matrix([
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 1],
      [0, 0, 1, 0]])
      >>> CNOT.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_not_cnot.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_cnot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_cnot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{-\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> ANOT = Not(targets=[1], anticontrols=[0])
      >>> ANOT.output()
      Matrix([
      [0, 1, 0, 0],
      [1, 0, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]])
      >>> ANOT.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_not_anot.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_anot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_anot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> CCNOT = Not(targets=[2], controls=[0, 1])
      >>> CCNOT.output()
      Matrix([
      [1, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 0]])
      >>> CCNOT.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_not_ccnot.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_ccnot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_ccnot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> RNOT = Not(
      ...     exponent=sp.Rational(1, 2),
      ...     label="√NOT",
      ...     family="GATE",
      ... )
      >>> RNOT.output()
      Matrix([
      [1/2 + I/2, 1/2 - I/2],
      [1/2 - I/2, 1/2 + I/2]])
      >>> RNOT.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_not_rnot.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_rnot-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_not_rnot-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Hadamard
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> H = Hadamard()
      >>> H.output()
      Matrix([
      [sqrt(2)/2,  sqrt(2)/2],
      [sqrt(2)/2, -sqrt(2)/2]])
      >>> H.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_hadamard_h.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{-3\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> HH = Hadamard(targets=[0, 1], label="H⊗H")
      >>> HH.output()
      Matrix([
      [1/2,  1/2,  1/2,  1/2],
      [1/2, -1/2,  1/2, -1/2],
      [1/2,  1/2, -1/2, -1/2],
      [1/2, -1/2, -1/2,  1/2]])
      >>> HH.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_hadamard_hh.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_hh-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_hh-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> H3 = Hadamard(dim=3)
      >>> H3.output()
      Matrix([
      [sqrt(3)/3,                sqrt(3)/3,                sqrt(3)/3],
      [sqrt(3)/3, sqrt(3)*exp(-2*I*pi/3)/3,  sqrt(3)*exp(2*I*pi/3)/3],
      [sqrt(3)/3,  sqrt(3)*exp(2*I*pi/3)/3, sqrt(3)*exp(-2*I*pi/3)/3]])
      >>> H3.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_hadamard_h3.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_hadamard_h3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Fourier
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> F = Fourier()
      >>> F.output()
      Matrix([
      [sqrt(2)/2,  sqrt(2)/2],
      [sqrt(2)/2, -sqrt(2)/2]])
      >>> F.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_fourier_f.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> F3 = Fourier(dim=3)
      >>> F3.output()
      Matrix([
      [sqrt(3)/3,                sqrt(3)/3,                sqrt(3)/3],
      [sqrt(3)/3, sqrt(3)*exp(-2*I*pi/3)/3,  sqrt(3)*exp(2*I*pi/3)/3],
      [sqrt(3)/3,  sqrt(3)*exp(2*I*pi/3)/3, sqrt(3)*exp(-2*I*pi/3)/3]])
      >>> F3.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_fourier_f3.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f3-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_f3-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> FF = Fourier(targets=[0, 1])
      >>> FF.output()
      Matrix([
      [1/2,  1/2,  1/2,  1/2],
      [1/2, -1/2,  1/2, -1/2],
      [1/2,  I/2, -1/2, -I/2],
      [1/2, -I/2, -1/2,  I/2]])
      >>> FF.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_fourier_ff.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_ff-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_fourier_ff-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Fourier.composite
      :no-index:

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Fourier.reverse
      :no-index:

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.gates.Measurement
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> from qhronology.mechanics.matrices import ket
      >>> basis_vectors = [ket(i) for i in [0, 1]]
      >>> M_basis = Measurement(operators=basis_vectors, observable=False)
      >>> M_basis.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_measurement_basis.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_basis-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_basis-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> pauli_matrices = [Pauli(index=i) for i in [1, 2, 3]]
      >>> M_pauli = Measurement(
      ...     operators=pauli_matrices,
      ...     observable=True,
      ...     targets=[0],
      ...     num_systems=2,
      ... )
      >>> M_pauli.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_measurement_pauli.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pauli-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pauli-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> from qhronology.mechanics.matrices import ket
      >>> plus = (ket(0) + ket(1)) / sp.sqrt(2)
      >>> minus = (ket(0) - ket(1)) / sp.sqrt(2)
      >>> M_pm = Measurement(
      ...     operators=[plus, minus],
      ...     observable=False,
      ...     targets=[1],
      ...     num_systems=2,
      ... )
      >>> M_pm.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_measurement_pm.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pm-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_measurement_pm-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Measurement.operators
      :no-index:

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.Measurement.observable
      :no-index:

.. raw:: latex

   \hrulefillthick

Combinations
============

.. autoclass:: qhronology.quantum.gates.GateInterleave
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> HI = Hadamard(targets=[0], num_systems=2)
      >>> IH = Hadamard(targets=[1], num_systems=2)
      >>> HH = GateInterleave(HI, IH, merge=True)
      >>> HH.output()
      Matrix([
      [1/2,  1/2,  1/2,  1/2],
      [1/2, -1/2,  1/2, -1/2],
      [1/2,  1/2, -1/2, -1/2],
      [1/2, -1/2, -1/2,  1/2]])
      >>> HH.diagram(sep=(1, 2))

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_composition_hh.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_hh-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_hh-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \newpage

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> XII = Pauli(index=1, targets=[0], num_systems=3)
      >>> IYI = Pauli(index=2, targets=[1], num_systems=3)
      >>> IIZ = Pauli(index=3, targets=[2], num_systems=3)
      >>> XYZ = GateInterleave(XII, IYI, IIZ)
      >>> XYZ.output()
      Matrix([
      [0,  0,  0, 0, 0,  0, -I, 0],
      [0,  0,  0, 0, 0,  0,  0, I],
      [0,  0,  0, 0, I,  0,  0, 0],
      [0,  0,  0, 0, 0, -I,  0, 0],
      [0,  0, -I, 0, 0,  0,  0, 0],
      [0,  0,  0, I, 0,  0,  0, 0],
      [I,  0,  0, 0, 0,  0,  0, 0],
      [0, -I,  0, 0, 0,  0,  0, 0]])
      >>> XYZ.diagram(sep=(1, 2))

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_composition_xyz.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_xyz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_xyz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> CNII = Not(targets=[1], controls=[0], num_systems=4)
      >>> IINC = Not(targets=[2], controls=[3], num_systems=4)
      >>> CNNC = GateInterleave(CNII, IINC)
      >>> CNNC.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_composition_cncn.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_cncn-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_composition_cncn-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.GateInterleave.gates
      :no-index:

   .. raw:: latex

      \hrulefillthick

   .. autoproperty:: qhronology.quantum.gates.GateInterleave.merge
      :no-index:

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \newpage

.. autoclass:: qhronology.quantum.gates.GateStack
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> X = Pauli(index=1)
      >>> Y = Pauli(index=2)
      >>> Z = Pauli(index=3)
      >>> XYZ = GateStack(X, Y, Z)
      >>> XYZ.output()
      Matrix([
      [0,  0,  0, 0, 0,  0, -I, 0],
      [0,  0,  0, 0, 0,  0,  0, I],
      [0,  0,  0, 0, I,  0,  0, 0],
      [0,  0,  0, 0, 0, -I,  0, 0],
      [0,  0, -I, 0, 0,  0,  0, 0],
      [0,  0,  0, I, 0,  0,  0, 0],
      [I,  0,  0, 0, 0,  0,  0, 0],
      [0, -I,  0, 0, 0,  0,  0, 0]])
      >>> XYZ.diagram(sep=(1, 2))

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_stack_xyz.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_xyz-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_xyz-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> gates = [
      ...     Not(
      ...         targets=[(i + 1) % 2],
      ...         controls=[i % 2],
      ...     ) for i in range(0, 4)
      ... ]
      >>> CNOTs = GateStack(*gates)
      >>> CNOTS.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_stack_cnots.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_cnots-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_cnots-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> gates = [GellMann(index=i) for i in range(1, 9)]
      >>> L = GateStack(*gates)
      >>> L.diagram(sep=(1, 1))

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_gate_stack_gellmann.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_gellmann-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_gate_stack_gellmann-light.png
            :scale: 40 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}