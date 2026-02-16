.. include:: /styles.rst

.. _`sec:docs_architecture_structure`:

Package structure
=================

The directory structure of the package appears below.

.. raw:: latex

   \begin{codetitled}{Package structure of Qhronology}{code:structure}

.. literalinclude:: ./../../../structure.txt
   :language: text
   :caption: Package structure of Qhronology
   :name: code:structure

.. raw:: latex

   \end{codetitled}

It consists of three subpackages:

- :python:`quantum`: most of the package's underlying mathematical framework and its user-facing classes.
- :python:`mechanics`: core logic for creating fundamental quantum objects, performing operations on them, and computing various quantum-mechanical scalar quantities.
- :python:`utilities`: a collection of modules containing various functionality intended for internal-use only, including the visualization engine, the core :python:`QuantumObject` class, and assorted helper functions.

In this documentation, we focus solely on the :python:`quantum` and :python:`mechanics` subpackages, with the former containing all of the classes intended to be user-facing. These are summarized in the following subsections.

.. raw:: latex

   \newpage
   \null
   \vspace*{-2.15\baselineskip}

:python:`quantum` subpackage
----------------------------

.. raw:: latex
   
   \enlargethispage{2\baselineskip}

The :python:`quantum` subpackage contains most of Qhronology's underlying mathematical framework and its user-facing classes.

.. list-table:: Overview of Qhronology's :python:`quantum` subpackage.
   :widths: 16 30 14
   :header-rows: 1

   * - **Module**
     - **Contents**
     - **Objects**
   * - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | :python:`states.py`
     - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | Classes for the creation of quantum states.
     - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | **Main class:**
       | :py:class:`~qhronology.quantum.states.QuantumState`
       | **Subclasses:**
       | :py:class:`~qhronology.quantum.states.VectorState`
       | :py:class:`~qhronology.quantum.states.MatrixState`
       | :py:class:`~qhronology.quantum.states.PureState`
       | :py:class:`~qhronology.quantum.states.MixedState`
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`gates.py`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | Classes for the creation of quantum gates.
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | **Main class:**
       | :py:class:`~qhronology.quantum.gates.QuantumGate`
       | **Subclasses:**
       | :py:class:`~qhronology.quantum.gates.Pauli`
       | :py:class:`~qhronology.quantum.gates.GellMann`
       | :py:class:`~qhronology.quantum.gates.Rotation`
       | :py:class:`~qhronology.quantum.gates.Phase`
       | :py:class:`~qhronology.quantum.gates.Diagonal`
       | :py:class:`~qhronology.quantum.gates.Swap`
       | :py:class:`~qhronology.quantum.gates.Summation`
       | :py:class:`~qhronology.quantum.gates.Not`
       | :py:class:`~qhronology.quantum.gates.Hadamard`
       | :py:class:`~qhronology.quantum.gates.Fourier`
       | :py:class:`~qhronology.quantum.gates.Measurement`
       | **Combinations:**
       | :py:class:`~qhronology.quantum.gates.GateInterleave`
       | :py:class:`~qhronology.quantum.gates.GateStack`
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`circuits.py`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | A class for the creation of quantum circuits.
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | **Class:**
       | :py:class:`~qhronology.quantum.circuits.QuantumCircuit`
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`prescriptions.py`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | A class for the creation of quantum circuits containing closed timelike curves.
       | Classes and functions implementing quantum prescriptions of time travel.
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | **Main class:**
       | :py:class:`~qhronology.quantum.prescriptions.QuantumCTC`
       | **Subclasses:**
       | :py:class:`~qhronology.quantum.prescriptions.DCTC`
       | :py:class:`~qhronology.quantum.prescriptions.PCTC`

.. raw:: latex
   
   \newpage
   \null
   \vspace*{-2.15\baselineskip}

:python:`mechanics` subpackage
------------------------------

.. raw:: latex
   
   \enlargethispage{2\baselineskip}

The :python:`mechanics` subpackage contains Qhronology's core logic for creating fundamental quantum objects, performing operations on them, and computing scalar quantities.

.. raw:: latex
   
   \vspace*{-0.65\baselineskip}

.. list-table:: Overview of Qhronology's :python:`mechanics` subpackage.
   :widths: 14 28 18
   :header-rows: 1

   * - **Module**
     - **Contents**
     - **Objects**
   * - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | :python:`matrices.py`
     - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | Core functions for creating quantum vectors and matrices.
     - | :inlinelatex:`\vspace*{-2.00\baselineskip}`
       | **Functions:**
       | :py:func:`~qhronology.mechanics.matrices.vector_basis`
       | :py:func:`~qhronology.mechanics.matrices.ket`
       | :py:func:`~qhronology.mechanics.matrices.bra`
       | :py:func:`~qhronology.mechanics.matrices.quantum_state`
       | :py:func:`~qhronology.mechanics.matrices.encode`
       | :py:func:`~qhronology.mechanics.matrices.decode_slow`
       | :py:func:`~qhronology.mechanics.matrices.decode`
       | :py:func:`~qhronology.mechanics.matrices.decode_fast`
       | :py:func:`~qhronology.mechanics.matrices.decode_multiple`
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`quantities.py`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | Functions for computing quantum quantities from matrices.
       | A mixin for endowing compatible classes with the ability to calculate these quantities.
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | **Functions:**
       | :py:func:`~qhronology.mechanics.quantities.trace`
       | :py:func:`~qhronology.mechanics.quantities.purity`
       | :py:func:`~qhronology.mechanics.quantities.distance`
       | :py:func:`~qhronology.mechanics.quantities.fidelity`
       | :py:func:`~qhronology.mechanics.quantities.entropy`
       | :py:func:`~qhronology.mechanics.quantities.mutual`
       | **Mixin:**
       | :py:class:`~qhronology.mechanics.quantities.QuantitiesMixin`
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`
   * - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | :python:`operations.py`
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | Functions for performing quantum operations on matrices.
       | A mixin for endowing compatible classes with the ability to perform these operations.
     - | :inlinelatex:`\vspace*{-1.75\baselineskip}`
       | **Functions:**
       | :py:func:`~qhronology.mechanics.operations.densify`
       | :py:func:`~qhronology.mechanics.operations.columnify`
       | :py:func:`~qhronology.mechanics.operations.dagger`
       | :py:func:`~qhronology.mechanics.operations.simplify`
       | :py:func:`~qhronology.mechanics.operations.rewrite`
       | :py:func:`~qhronology.mechanics.operations.apply`
       | :py:func:`~qhronology.mechanics.operations.normalize`
       | :py:func:`~qhronology.mechanics.operations.coefficient`
       | :py:func:`~qhronology.mechanics.operations.partial_trace`
       | :py:func:`~qhronology.mechanics.operations.measure`
       | :py:func:`~qhronology.mechanics.operations.postselect`
       | **Mixin:**
       | :py:class:`~qhronology.mechanics.operations.OperationsMixin`
       | :inlinelatex:`\vspace*{-1.85\baselineskip}`

.. raw:: latex

   \newpage
