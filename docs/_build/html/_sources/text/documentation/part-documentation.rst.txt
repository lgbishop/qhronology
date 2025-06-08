.. .. raw:: latex

..    \part{Documentation}

.. include:: /styles.rst

.. only:: html

   .. raw:: html

      <style>
         .bd-sidebar-secondary {
            display: none;
            visibility: hidden;
         }
      </style>

.. only:: html

   .. raw:: html

      <style>
         h1 {
            margin-top: 1.5rem !important;
         }
      </style>

.. _`part:documentation`:

.. only:: html

   .. raw:: html

      <div style="display: none; visibility: hidden;">

   #############
   Documentation
   #############

   .. raw:: html
   
      </div>

   .. rubric:: :styleheader0:`Documentation`

In this part, detailed documentation of the Qhronology package is presented. This includes in-depth descriptions of the package's various submodules and their respective functions and classes (including all methods and properties). Numerous usage examples of many of the most important objects are also provided. Note however that only the components of the package which are intended to be used by the end user are included here. For the other, undocumented modules, please see the relevant parts of the package's source code.

.. raw:: latex
   
   \newpage

.. rubric:: :styleheader1:`Quantum`

The ``quantum`` subpackage contains most of Qhronology's underlying mathematical framework.

.. list-table:: Overview of Qhronology's ``quantum`` subpackage
   :widths: 15 25 20
   :header-rows: 1

   * - Module
     - Contents
     - Objects
   * - ``states.py``
     - Classes for the creation of quantum states.
     - | **Main class:**
       | :py:class:`~qhronology.quantum.states.QuantumState`
       | **Subclasses:**
       | :py:class:`~qhronology.quantum.states.VectorState`
       | :py:class:`~qhronology.quantum.states.MatrixState`
       | :py:class:`~qhronology.quantum.states.PureState`
       | :py:class:`~qhronology.quantum.states.MixedState`
   * - ``gates.py``
     - Classes for the creation of quantum gates.
     - | **Main class:**
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
       | **Combining gates:**
       | :py:class:`~qhronology.quantum.gates.GateInterleave`
       | :py:class:`~qhronology.quantum.gates.GateStack`
   * - ``circuits.py``
     - A class for the creation of quantum circuits.
     - | **Class:**
       | :py:class:`~qhronology.quantum.circuits.QuantumCircuit`
   * - ``prescriptions.py``
     - A class for the creation of quantum circuits containing closed timelike curves. Classes and functions implementing quantum prescriptions of time travel.
     - | **Main class:**
       | :py:class:`~qhronology.quantum.prescriptions.QuantumCTC`
       | **Subclasses:**
       | :py:class:`~qhronology.quantum.prescriptions.DCTC`
       | :py:class:`~qhronology.quantum.prescriptions.PCTC`
       | **Functions:**
       | :py:func:`~qhronology.quantum.prescriptions.dctc_violating`
       | :py:func:`~qhronology.quantum.prescriptions.dctc_respecting`
       | :py:func:`~qhronology.quantum.prescriptions.pctc_violating`
       | :py:func:`~qhronology.quantum.prescriptions.pctc_respecting`

.. raw:: latex
   
   \newpage

.. rubric:: :styleheader1:`Mechanics`

The ``mechanics`` subpackage contains Qhronology's core logic for creating quantum vectors and matrices, performing operations on such constructs, and computing various significant scalar quantities.

.. list-table:: Overview of Qhronology's ``mechanics`` subpackage
   :widths: 15 25 20
   :header-rows: 1

   * - Module
     - Contents
     - Objects
   * - ``matrices.py``
     - Core functions for creating quantum vectors and matrices.
     - | **Functions:**
       | :py:func:`~qhronology.mechanics.matrices.vector_basis`
       | :py:func:`~qhronology.mechanics.matrices.ket`
       | :py:func:`~qhronology.mechanics.matrices.bra`
       | :py:func:`~qhronology.mechanics.matrices.quantum_state`
       | :py:func:`~qhronology.mechanics.matrices.encode`
       | :py:func:`~qhronology.mechanics.matrices.decode_slow`
       | :py:func:`~qhronology.mechanics.matrices.decode`
       | :py:func:`~qhronology.mechanics.matrices.decode_fast`
       | :py:func:`~qhronology.mechanics.matrices.decode_multiple`
   * - ``quantities.py``
     - Functions for computing quantum quantities from matrices. A mixin for endowing compatible classes with the ability to calculate these quantities.
     - | **Functions:**
       | :py:func:`~qhronology.mechanics.quantities.trace`
       | :py:func:`~qhronology.mechanics.quantities.purity`
       | :py:func:`~qhronology.mechanics.quantities.distance`
       | :py:func:`~qhronology.mechanics.quantities.fidelity`
       | :py:func:`~qhronology.mechanics.quantities.entropy`
       | :py:func:`~qhronology.mechanics.quantities.mutual`
       | **Mixin:**
       | :py:class:`~qhronology.mechanics.quantities.QuantitiesMixin`
   * - ``operations.py``
     - Functions for performing quantum operations on matrices. A mixin for endowing compatible classes with the ability to perform these operations.
     - | **Functions:**
       | :py:func:`~qhronology.mechanics.operations.densify`
       | :py:func:`~qhronology.mechanics.operations.columnify`
       | :py:func:`~qhronology.mechanics.operations.dagger`
       | :py:func:`~qhronology.mechanics.operations.simplify`
       | :py:func:`~qhronology.mechanics.operations.apply`
       | :py:func:`~qhronology.mechanics.operations.rewrite`
       | :py:func:`~qhronology.mechanics.operations.normalize`
       | :py:func:`~qhronology.mechanics.operations.coefficient`
       | :py:func:`~qhronology.mechanics.operations.partial_trace`
       | :py:func:`~qhronology.mechanics.operations.measure`
       | :py:func:`~qhronology.mechanics.operations.postselect`
       | **Mixin:**
       | :py:class:`~qhronology.mechanics.operations.OperationsMixin`

.. raw:: latex
   
   \newpage

.. rubric:: :styleheader1:`Structure`

For reference, a structure diagram detailing the relationships between Qhronology's classes in the standard UML (Unified Modelling Language) framework is depicted in :numref:`fig:diagram_classes`.

.. only:: html

   .. figure:: /figures/output/diagram_classes-dark.png
      :scale: 36 %
      :alt: A simple diagram depicting the (inheritance) relationships between the package's classes.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/diagram_classes-light.png
      :scale: 36 %
      :alt: A simple diagram depicting the (inheritance) relationships between the package's classes.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/diagram_classes-light.png
   :name: fig:diagram_classes
   :scale: 36 %
   :alt: A simple diagram depicting the (inheritance) relationships between the package's classes.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The (inheritance) relationships between the package's classes.

.. raw:: latex
   
   \newpage

.. rubric:: :styleheader1:`Types`

Qhronology's underlying functionality takes advantage of a few bespoke type aliases, which are detailed in the table below.

.. list-table:: Internal type aliases
   :widths: 5 20 40
   :header-rows: 1

   * - Type Alias
     - Description
     - Definition
   * - ``num``
     - Scalar numerical numbers
     - ``numbers.Number | numpy.generic | sympy.Basic``
   * - ``sym``
     - SymPy symbolic scalar expressions and symbols
     - ``sympy.matrices.expressions.matexpr.MatrixSymbol | sympy.matrices.expressions.matexpr.MatrixElement | sympy.core.symbol.Symbol``
   * - ``mat``
     - SymPy (mutable) dense matrices
     - ``sympy.matrices.dense.MutableDenseMatrix``
   * - ``arr``
     - NumPy arrays
     - ``numpy.ndarray``

.. raw:: html

   <div style="display: none; visibility: hidden;">

.. only:: html

   .. rubric:: :styleheader2:`Modules`

.. rst-class:: hide-caption

   .. toctree::
      :caption: Quantum
      :maxdepth: 1

      quantum/states.rst
      quantum/gates.rst
      quantum/circuits.rst
      quantum/prescriptions.rst

.. only:: html

   .. rubric:: :styleheader2:`Modules`

.. rst-class:: hide-caption

   .. toctree::
      :caption: Mechanics
      :maxdepth: 1

      mechanics/matrices.rst
      mechanics/quantities.rst
      mechanics/operations.rst

.. .. only:: html

..    .. rubric:: :styleheader2:`Modules`

.. .. rst-class:: hide-caption

..    .. toctree::
..       :caption: Utilities
..       :maxdepth: 1

..       utilities/objects.rst
..       utilities/symbolics.rst
..       utilities/classifications.rst
..       utilities/diagrams.rst
..       utilities/helpers.rst

.. raw:: html

   </div>