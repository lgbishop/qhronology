.. include:: /styles.rst

.. _`sec:docs_architecture_classes`:

Classes and their relationships
===============================

Qhronology presents an innovative approach to describing both simulations of quantum mechanics and the various associated mathematical constructs and processes which collectively form the foundation of contemporary quantum physics. While this is not novel in the world of quantum libraries and toolkits, Qhronology is unique in how it places great emphasis on modularity in its descriptions of quantum states, gates, and circuits. Perhaps the best way by which this aspect can be appreciated is to gain a deeper understanding of the package's interface, specifically that manifested by its user-facing classes.

:numref:`fig:diagram_classes` contains a simplified UML class diagram, depicting the majority of the package's class objects and the relationships (including inheritance and composition) between them. As shown in this diagram, the :python:`QuantumObject` class is central to Qhronology's functionality. Being an *abstract* base class (and so is not meant to be instantiated itself), :python:`QuantumObject` constitutes the common substructure upon which all primitive quantum-mechanical objects are built. Specifically, this consists of the two main classes:

- :python:`QuantumState`: for creating quantum states. Instances have *mutable* internal states.
- :python:`QuantumGate`: for creating quantum gates. Instances have *immutable* internal states.

These are implemented as *extending* subclasses, where each adds to and modifies the functionality of the :python:`QuantumObject` base class primarily through class properties and methods.Instances of these derived classes provide exhaustive descriptions of their corresponding quantum constructs: in addition to containing a precise mathematical specification (including metadata regarding symbols and their associated constraints), they can be inspected, visualized, and, in the case of quantum states, transformed (mutated) via quantum operations. Here, :python:`QuantumObject` provides the core matrix, symbolic, and visualization machinery (in addition to all other internal implementation details) required by Qhronology's programmatic description of fundamental quantum objects. Thus, as both states and gates are simply just specific types of such objects, then using the :python:`QuantumObject` class as a shared foundation is a natural arrangement---one which greatly simplifies the project's source code by directly reducing redundancy.

.. raw:: latex
   
   \newpage
   \null
   \vspace*{-1.25\baselineskip}
   \enlargethispage{\baselineskip}

.. only:: html

   .. figure:: /figures/output/diagram_classes-dark.png
      :scale: 34 %
      :alt: A simple diagram depicting the (inheritance) relationships between the package's classes.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/diagram_classes-light.png
      :scale: 34 %
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

   A simplified UML (Unified Modeling Language) class diagram depicting the relationships between Qhronology's core classes.

.. raw:: latex
   
   \newpage

.. _`sec:docs_architecture_composition`:

Circuit composition
-------------------

Having gained an appreciation for Qhronology's implementation of quantum states and gates, we now turn our attention to that of quantum circuits. In standard quantum theory, a circuit can be thought of as being essentially an assembly of states and gates that corresponds to a mathematical description of some specific quantum-mechanical process. This ontology is reflected in Qhronology's circuit construction---facilitated by the :python:`QuantumCircuit` class---whereby circuit instances are created by passing :python:`QuantumState` and :python:`QuantumGate` objects to the appropriate arguments in the class constructor (or, alternatively, to the appropriate properties post-instantiation). In a pragmatic (albeit reductive) sense, :python:`QuantumCircuit` objects are merely containers for their various elementary components (while also possessing other necessary functionality). Of all the class's abilities, the most defining is the computation of the output state (of the circuit assembled from its state and gate components), which may be returned as either a SymPy matrix or a :python:`QuantumState` instance.

Building upon :python:`QuantumCircuit`, Qhronology's :python:`QuantumCTC` class provides the core scaffolding by which quantum circuits that possess CTCs are described. As far as the programmatic specification of such circuits is concerned, the main practical difference between them and their CTC-free counterparts is that the quantum systems of the former are not exclusively chronology-respecting---those which comprise the CTC subsystem are, by definition, chronology-violating. Qhronology recognizes this sentiment, and accordingly :python:`QuantumCTC` extends the :python:`QuantumCircuit` class only by the addition of the :python:`systems_respecting` and :python:`systems_violating` constructor arguments (along with homonymous class properties).

Instances of the :python:`QuantumCTC` class, constructed in much the same way as :python:`QuantumCircuit` instances (e.g., the passing of states and gates to the class constructor's relevant arguments), provide descriptions of specific interactions (defined by the given gates) between the CR and CV subsystems (with input state given on the former). By itself however, the :python:`QuantumCTC` class is unable to compute the output states on these subsystems, as this can only be accomplished within the context of a particular quantum prescription. Such models can be implemented simply as subclasses of :python:`QuantumCTC`, wherein the appropriate machinery is granted to the class methods which require it. Indeed, Qhronology provides the two foremost prescriptions, D-CTCs and P-CTCs, as the :python:`QuantumDCTC` and :python:`QuantumPCTC` classes, respectively. It is these subclasses which provide the capabilities for calculating the specific predictions of their associated quantum prescription of antichronological time travel.

.. _`sec:docs_architecture_design`:

Modularity and design patterns
------------------------------

Qhronology provides a flexible domain-specific framework for theoretical quantum mechanics, with the usage pattern of its circuit creation in particular being a highly modular procedure. As part of this, the program places great emphasis on the ability to define quantum primitives outside of the context of any circuit description. In other words, Qhronology treats individual states and gates as complete, fundamental, and independent objects.

The standard pattern of Qhronology's circuit instantiation (see :numref:`sec:docs_circuits` :ref:`sec:docs_circuits`) consists primarily of the passing of pre-existing state (:python:`QuantumState`) and gate (:python:`QuantumGate`) instances to the circuit (:python:`QuantumCircuit`) constructor's arguments. With an assembled circuit, one can then extract its total (composite) input and output states as :python:`QuantumState` instances, as well as the entire gate sequence as a single amalgamated :python:`QuantumGate` instance. These extracted objects are no different from any other user-created states or gates in Qhronology, and so can be inspected, modified, and incorporated into other circuits. Qhronology's claim to extensive modularity stems primarily from its ability to both assemble and extract elementary objects, which themselves can be subsequently used in a variety of contexts.

Although the typical procedure of creating circuits within the framework does not precisely resemble any single design pattern, it does possess some traits from what is canonically known as the *composite pattern*---a software-engineering design pattern :cite:p:`gamma_design_1994` characterized by the aggregation of elementary objects into a single, more complex object. Qhronology's particular structure however diverges from this pattern in one important way: while the :python:`QuantumCircuit` class facilitates the composition of fundamental objects (states and gates) into a more complex container (from which both all kinds of fundamental objects can be obtained), it itself cannot be further composed into other objects, nor does it share the same interface as its constituent objects. Nonetheless, the program's process of creating circuits (almost) completely from pre-defined primitives at instantiation is a distinctly novel approach, one that is in stark contrast with the *builder pattern*---quantum circuits constructed via a succession of methods called on an initially empty quantum circuit class instance---used in other Python-based quantum projects, including IBM's *Qiskit* :cite:p:`ibm_qiskit_2017, javadi-abhari_quantum_2024`, Google's *Cirq* :cite:p:`google_cirq_2018`, Xanadu's *PennyLane* :cite:p:`xanadu_pennylane_2018, bergholm_pennylane_2022`, and the community-run *QuTiP* :cite:p:`the_qutip_community_qutip_2012, lambert_qutip_2026`.

.. raw:: latex
   
   \newpage
   \null
   \vspace*{-2.15\baselineskip}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
