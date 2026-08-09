.. Note: This file doubles as both the project repository's README and the first chapter source file in the associated PDF documentation.

.. include:: /styles.rst

.. raw:: html

   <style>
   .bd-main .bd-content {
       justify-content: center;
   }
   </style>

.. only:: html

   .. image:: /art/output/logo-main-50fps-3sec-animated-60compressed.webp
      :width: 720px
      :alt: Qhronology logo
      :align: center
      :class: dark-light

.. raw:: html

   <div style="display: none; visibility: hidden;">

.. _`part:overview`:

********
Overview
********

.. raw:: html

   </div>

.. only:: html

   .. rubric:: :styleheader0:`Overview`

.. .. raw:: latex

..    \vspace*{-0.25cm}

.. only:: latex

   .. image:: /art/output/logo-main-50fps-3sec.png
      :width: 720px
      :alt: Qhronology logo
      :align: center

.. .. raw:: latex

..    \vspace*{0.25cm}

Perhaps the most fascinating aspect of the current research on closed timelike curves (CTCs) is that there is more than one way to treat them with quantum mechanics to a sufficient degree of plausibility. While none of the established quantum models (sometimes called *prescriptions*) has been accepted by scientific consensus as the authoritative description of how the Universe may potentially conduct antichronological time travel, all of them can be used to predict evolutions of the time-travelling quantum systems associated with CTCs. Though these predictions often disagree in stark ways, their differences can also be subtle, which may likewise be true for any number of the prescriptions' other aspects, including their mathematical characteristics (such as [non-]linearity and [non-]unitarity in state evolution) and physical consequences (such as the abilities to distinguish non-orthogonal states, clone arbitrary states, signal superluminally, and increase the computational speed and efficiency of both classical and quantum computers). A major part of the research into the various prescriptions therefore is how, despite being formulated with radically distinct (and usually fundamentally incompatible) postulates, they all provide self-consistent, paradox-free evolutions of quantum systems near CTCs (including resolutions to temporal paradoxes), with the associated quantum states themselves always being physically valid, at least in the sense of standard quantum mechanics.

.. raw:: latex

   \enlargethispage{\baselineskip}

In the absence of physical CTCs on which to perform experiments, one of the more effective ways to investigate the various quantum models of time travel is to compare their theoretical predictions for the states of the quantum systems both internal (*chronology-violating*, or CV) and external (*chronology-respecting*, or CR) to a CTC in the context of specific inter-system interactions. Doing so however can prove to be both tedious and error-prone, especially in cases where the interactions are complex. For example, *Deutsch's model* (giving *Deutschian* CTCs, or D-CTCs) necessitates the solving of a fixed-point condition for which there is often a parametrized spectrum of (non-unique) CV solutions (and, accordingly, a corresponding spectrum of CR solutions). Similarly, the theory of *postselected teleportation* (giving *postselected* CTCs, or P-CTCs) requires one to non-unitarily evolve input states and subsequently renormalize the results. Needless to say, the procedures for computing the predictions of these prescriptions are highly involved, and so must be performed with great care.

.. raw:: latex

   \newpage
   \null
   \vspace*{-2.35\baselineskip}

Born out of the desire for a way to programmatically compute the states of the CR and CV systems according to the foremost quantum prescriptions of antichronological time travel, :inlinelatex:`\hspace{-0.35em}\emph{` `Qhronology <https://qhronology.org>`_ :inlinelatex:`}\hspace{-0.5em}` :cite:p:`bishop_qhronology-software_2025` was created as a unified computational environment for defining, simulating, and analyzing quantum information processes that incorporate CTCs. Notably, the package can be used to calculate quantum resolutions to any given temporal paradox, thereby enabling users to explore foundational questions regarding the quantum mechanics of time travel. By providing a unique approach to describing general quantum objects (such as states and gates), Qhronology can also operate as a complete quantum circuit simulator, of which a prominent component is its engine for the visualization of quantum circuit diagrams. Its main features include:

- Calculation of the states of the CR and CV quantum systems according to quantum-mechanical prescriptions of closed timelike curves

  - Deutsch's model (D-CTCs)
  - Postselected teleportation (P-CTCs)

- Simulation of general quantum information processing and computation

  - Symbolic calculations involving any number of variables and parameters
  - Numerical (classical) replication of quantum experiments

- Visualization of quantum circuit diagrams

  - Text-based semigraphical diagrams constructed from fixed-width typefaces

The primary purpose of Qhronology is to facilitate the study of quantum models of antichronological time travel and quantum algorithms of quantum computing in both educational and research capacities. As part of this, the project aims to make the expression of quantum states, gates, circuits, and models of CTCs near-limitlessly possible within a framework that is syntactically simple yet computationally powerful. Qhronology therefore provides a sufficiently complete and self-contained set of tools with the intention that needing to use external packages and libraries to perform transformations on its quantum constructs should not (usually) be necessary. Its underlying mathematical system accomplishes this using the standard :math:`\Dimension`-dimensional matrix mechanics of discrete-variable quantum theory in a general :math:`\Complexes^\Dimension`-representation.

Qhronology is written entirely in the `Python <https://www.python.org>`_ programming language. Being high-level, dynamically type-checked, and interpreted (at least within the context of its CPython reference implementation), Python is well-suited for building an accessible framework that emphasizes interactivity and scriptability. Additionally, like any popular language, it has both an extensive standard library and a plethora of powerful community packages available to it. Qhronology is built around features from two such packages: the eminent `SymPy <https://sympy.org>`_ and `NumPy <https://numpy.org>`_ projects. In particular, the package greatly leverages the symbolic and linear algebra capabilities of the former, and so aims to have a deep compatibility with SymPy and its matrix objects. It is therefore hoped that users who possess experience with these projects find Qhronology's interface to be intuitive.

.. note::

   Qhronology, in its current form, is considered to be highly experimental. Its output may not always be correct, and some features may not work as intended. Additionally, please note that all components of the package, including its functions, methods, classes, modules, and subpackages, may be subject to change in future versions.

.. raw:: latex

   \vspace*{-0.35\baselineskip}

Features
========

Quantum computing simulations
-----------------------------

.. .. raw:: latex

..    \begin{tabular}{M{0.5\textwidth}  C{0.5\textwidth}}

Designed to provide a powerful set of features with a simple and intuitive syntax, Qhronology facilitates the simulation of quantum computation, information processing, and algebraic calculations.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.65em}

.. only:: html

   .. image:: /figures/output/circuit_algorithm_teleportation-dark.png
      :scale: 34 %
      :align: center
      :class: only-dark

   .. image:: /figures/output/circuit_algorithm_teleportation-light.png
      :scale: 34 %
      :align: center
      :class: only-light

.. only:: latex

   .. image:: /figures/output/circuit_algorithm_teleportation.pdf
      :scale: 115 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \vspace*{0.15em}

Quantum resolutions to antichronological time-travel paradoxes
--------------------------------------------------------------

.. .. raw:: latex

..    \begin{tabular}{M{0.55\textwidth}  C{0.45\textwidth}}

The fundamental indeterminism of quantum mechanics can be leveraged to provide resolutions to quantum formulations of classic time-travel paradoxes (such as the infamous *grandfather paradox*). A select few prescriptions by which this may be achieved, including Deutsch's model (D-CTCs) and the postselected teleportation prescription (P-CTCs), are implemented both as bare functions and class methods.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.65em}

.. only:: html

   .. image:: /figures/output/circuit_ctc-dark.png
      :scale: 34 %
      :align: center
      :class: only-dark

   .. image:: /figures/output/circuit_ctc-light.png
      :scale: 34 %
      :align: center
      :class: only-light

.. only:: latex

   .. image:: /figures/output/circuit_ctc.pdf
      :scale: 115 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \vspace*{0.15em}

Quantum circuit visualization
-----------------------------

.. .. raw:: latex

..    \begin{tabular}{M{0.55\textwidth}  C{0.45\textwidth}}

Quantum circuit diagrams provide a powerful picturalism through which a quantum process can be visualized as a network of quantum logic gates connected by wires. Qhronology provides this functionality for any such processes constructed using its built-in classes.

.. Alternative methods of visualization, such as that provided by the LaTeX *Quantikz* package, are under consideration for future development.

.. .. literalinclude:: /figures/text/text_examples_algorithms_generation_w.txt
..    :class: semigraphical

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.75em}

.. only:: html

   .. image:: /figures/output/text_examples_algorithms_generation_w-dark.png
      :scale: 40 %
      :align: center
      :class: only-dark

   .. image:: /figures/output/text_examples_algorithms_generation_w-light.png
      :scale: 40 %
      :align: center
      :class: only-light

.. only:: latex

   .. image:: /figures/output/text_examples_algorithms_generation_w.pdf
      :scale: 145 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \vspace*{0.25em}

.. raw:: latex

   \enlargethispage{0.75\baselineskip}

.. raw:: latex

   \newpage
   \null
   \vspace*{-2.35\baselineskip}

Numerous examples
-----------------

.. raw:: latex

   \vspace*{-0.25em}

.. .. raw:: latex

..    \begin{tabular}{M{0.65\textwidth}  C{0.35\textwidth}}

Bundled with the project is a collection of complete examples that showcase its capabilities and syntax. This includes both implementations of canonical quantum algorithms and exotic circuits that use quantum mechanics to resolve paradoxical scenarios of antichronological time travel.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{-0.75em}

.. only:: html

   .. image:: /figures/output/circuit_ctc_grandfather-dark.png
      :scale: 34 %
      :align: center
      :class: only-dark

   .. image:: /figures/output/circuit_ctc_grandfather-light.png
      :scale: 34 %
      :align: center
      :class: only-light

.. only:: latex

   .. image:: /figures/output/circuit_ctc_grandfather.pdf
      :scale: 115 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \vspace*{-1.00em}

Extensive documentation
-----------------------

.. raw:: latex

   \vspace*{-0.25em}

.. .. raw:: latex

..    \begin{tabular}{M{0.55\textwidth}  C{0.45\textwidth}}

All of the objects in each of the various submodules have been rigorously detailed in their respective sections within the documentation. This includes multiple examples of usage for each, aiding the user's understanding of every available feature.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{-0.15em}

.. only:: html

   .. image:: /figures/output/diagram_bloch_sphere-dark.png
      :scale: 34 %
      :align: center
      :class: only-dark

   .. image:: /figures/output/diagram_bloch_sphere-light.png
      :scale: 34 %
      :align: center
      :class: only-light

.. only:: latex

   .. image:: /figures/output/diagram_bloch_sphere.pdf
      :scale: 100 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \vspace*{-1.15em}

Foundational theory
-------------------

.. raw:: latex

   \vspace*{-0.25em}

.. .. raw:: latex

..    \begin{tabular}{M{0.35\textwidth}  C{0.65\textwidth}}

All of the underlying mathematics upon which Qhronology is built is presented as a series of pedagogical reference articles within the documentation. This includes sections on the mathematical foundations of quantum mechanics (Hilbert spaces, linear operators, composite systems, etc.), quantum theory on both discrete and continuous Hilbert spaces, a brief overview of the quantum circuitry picturalism, and physical theories of time travel (both classical and quantum).

.. The aim of this theory is to serve as a comprehensive and complete reference for basic quantum mechanics and physical theories of time travel, thereby enabling the keen user to embark upon further research into these fascinating areas of study.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{-0.65em}

.. only:: html

   .. image:: /figures/output/diagram_spacetime_minkowski-dark.png
      :scale: 34 %
      :align: center
      :class: only-dark

   .. image:: /figures/output/diagram_spacetime_minkowski-light.png
      :scale: 34 %
      :align: center
      :class: only-light

.. only:: latex

   .. image:: /figures/output/diagram_spacetime_minkowski.pdf
      :scale: 100 %
      :align: center
      :class: light-dark hidden

.. raw:: latex

   \enlargethispage{3\baselineskip}

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \newpage
   \null
   \vspace*{-2.75\baselineskip}

Package installation and structure
==================================

.. raw:: latex

   \vspace*{-0.5\baselineskip}

Local installation of Qhronology from `PyPI <https://pypi.org/project/qhronology>`_ can be accomplished using a Python package manager, such as `pip <https://pip.pypa.io>`_, via your operating system's command line, e.g.,

.. raw:: latex

   \begin{code}

.. code:: sh

   $ pip install qhronology

.. raw:: latex

   \end{code}

You may also be able to use an alternative package manager of your choice.

After installation, Qhronology can be imported in Python in the standard way. One suggestion is as follows:

.. raw:: latex

   \begin{code}

.. code:: python

   import qhronology as qy

.. raw:: latex

   \end{code}

The package has the following directory structure:

.. raw:: latex

   \begin{code}

.. code:: text

   qhronology
   ├──quantum
   │  ├──circuits.py
   │  ├──gates.py
   │  ├──prescriptions.py
   │  └──states.py
   ├──mechanics
   │  ├──matrices.py
   │  ├──operations.py
   │  └──quantities.py
   └──utilities (intended for internal use only)
      ├──classification.py
      ├──diagrams.py
      ├──helpers.py
      ├──objects.py
      └──symbolics.py

.. raw:: latex

   \end{code}

.. raw:: latex

   \vspace*{-0.25\baselineskip}

Requirements
------------

.. raw:: latex

   \vspace*{-0.25\baselineskip}

Within the package and documentation, SymPy and NumPy are imported in their conventional manners:

.. raw:: latex

   \begin{code}

.. code:: python

   import sympy as sp
   import numpy as np

.. raw:: latex

   \end{code}

Qhronology is compatible with the following versions (from `requirements.txt <https://github.com/lgbishop/qhronology/blob/latest/requirements.txt>`_):

.. raw:: latex

   \begin{code}

.. literalinclude:: ./../../requirements.txt

.. raw:: latex

   \end{code}

These are the earliest versions with which the current release has been tested, but older versions may also be compatible. It also requires

.. raw:: latex

   \begin{code}

.. code:: python

   python>=3.11

.. raw:: latex

   \end{code}

Examples
========

:ref:`Generation of a Bell state <eg:generation_bell>`
------------------------------------------------------

Generation of the :math:`\ket{\Bell^+}` Bell state from primitive :math:`\ket{0}` states:

.. raw:: latex

   \begin{codetitled}{Generation of a Bell state}{}

.. literalinclude:: /text/examples/algorithms/generation_bell.py
   :language: python

.. raw:: latex

   \tcblowerspaced

.. code:: python

   >>> generator.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.05cm -0.05cm 0 -0.08cm]{text_examples_algorithms_generation_bell.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_bell-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_bell-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. code:: python

   >>> phi_plus.print()
   |Φ+⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩

.. raw:: latex

   \end{codetitled}

:ref:`Quantum teleportation <eg:teleportation>`
-----------------------------------------------

.. raw:: latex

   \enlargethispage{\baselineskip}

Quantum teleportation of an arbitrary qubit :math:`\ket{\psi} = a\ket{0} + b\ket{1}`:

.. raw:: latex

   \begin{codetitled}{Quantum teleportation}{}

.. literalinclude:: /text/examples/algorithms/teleportation.py
   :language: python
   :end-at: teleported_state.print()

.. raw:: latex

   \tcblowerspaced

.. code:: python

   >>> teleporter.diagram(force_separation=True)

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.02cm 0 -0.10cm]{text_examples_algorithms_teleportation.pdf}
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

.. code:: python

   >>> teleporting_state.print()
   |ψ⟩ = a|0⟩ + b|1⟩

.. code:: python

   >>> teleported_state.print()
   ρ = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

.. raw:: latex

   \end{codetitled}

:ref:`Unproven-theorem paradox <eg:unproven>`
---------------------------------------------

.. raw:: latex

   \enlargethispage{\baselineskip}

Computing resolutions to the unproven-theorem paradox according to various prescriptions of quantum time travel (D-CTCs and P-CTCs):

.. raw:: latex

   \begin{codetitled}{Unproven-theorem paradox}{}

.. literalinclude:: /text/examples/ctcs/unproven.py
   :language: python

.. raw:: latex

   \tcblowerspaced

.. code:: python

   >>> unproven.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.05cm 0 -0.12cm]{text_examples_ctcs_unproven.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_unproven-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_unproven-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. code:: python

   >>> unproven_DCTC_CR.print()
   ρ_D = g|0,0⟩⟨0,0| + (1 - g)|1,1⟩⟨1,1|

.. code:: python

   >>> unproven_DCTC_CV.print()
   τ_D = g|0⟩⟨0| + (1 - g)|1⟩⟨1|

.. code:: python

   >>> unproven_PCTC_CR.print()
   |ψ_P⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩

.. code:: python

   >>> unproven_PCTC_CV.print()
   τ_P = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{codetitled}

.. raw:: latex

   \newpage

Documentation
=============

The latest version of the documentation for the package is available at:

- The official website: https://qhronology.org
- The official PDF document: `Qhronology.pdf <https://github.com/lgbishop/qhronology/blob/latest/docs/_build/latex/Qhronology.pdf>`_

Both of these are built using `Sphinx <https://www.sphinx-doc.org>`_ (`repository <https://github.com/sphinx-doc/sphinx>`_), with their shared source files residing within the ``docs`` directory at the root of the project's repository. This includes all project text and artwork. Please see `shell-sphinx.nix <https://github.com/lgbishop/qhronology/blob/latest/docs/shell-sphinx.nix>`_ within that directory for a list of dependencies required to build both documentation targets. Note that a full LaTeX system installation from 2024 or later is required to build the project's PDF documentation, figures, and artwork (including the logo). Also note that the documentation's rendered circuit diagrams (generated from the package itself) are created using a custom LaTeX template (`render-text.tex <https://github.com/lgbishop/qhronology/blob/latest/docs/source/figures/render-text.tex>`_) and associated shell script :inlinelatex:`\linebreak` (`render-text.sh <https://github.com/lgbishop/qhronology/blob/latest/docs/source/figures/render-text.sh>`_).

.. raw:: latex

   \vspace*{\baselineskip}

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. include:: ./../../LICENSE

.. raw:: latex

   \vspace*{\baselineskip}

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. include:: ./../../CONTRIBUTING

Citation
========

- The package itself:

.. raw:: latex

   \begin{code}

.. code:: bibtex

   @software{bishop_qhronology-software_2025,
     title = {Qhronology: {{A Python}} package for studying quantum models of closed timelike curves and simulating general quantum information processing \& computation},
     author = {Bishop, Lachlan G.},
     year = 2025,
     month = jun,
     url = {https://github.com/lgbishop/qhronology},
     addendum = {Source code: \url{https://github.com/lgbishop/qhronology}}
   }

.. raw:: latex

   \end{code}

- The project's documentation:

.. raw:: latex

   \begin{code}

.. code:: bibtex

   @misc{bishop_qhronology-documentation_2025,
     title = {Qhronology: {{Documentation}}, {{Examples}}, and {{Theory}}},
     author = {Bishop, Lachlan G.},
     year = 2025,
     month = jun,
     url = {https://github.com/lgbishop/qhronology/blob/latest/docs/_build/latex/Qhronology.pdf},
     addendum = {Available online: \url{https://qhronology.org}}
   }

.. raw:: latex

   \end{code}

- The project's technical paper:

.. raw:: latex

   \begin{code}

.. code:: bibtex

   @misc{bishop_qhronology_2026,
     title = {Qhronology: {{A Python}} package for studying quantum models of closed timelike curves},
     author = {Bishop, Lachlan G.},
     year = 2026,
     month = jan,
     number = {arXiv:2601.17459},
     primaryclass = {quant-ph},
     publisher = {arXiv},
     doi = {10.48550/arXiv.2601.17459},
     url = {https://arxiv.org/abs/2601.17459}
   }

.. raw:: latex

   \end{code}

.. raw:: latex

   \newpage

Possible future work
====================

- Package:

  - Write proper (formal) unit tests.
  - Permit more intuitive usage (i.e., summation and multiplication) of quantum objects via operator overloading.
  - Tighter integration with SymPy's :python:`pprint()` functionality for enhanced state and gate printing.
  - Implement T-CTCs (the *transition-probabilities* quantum model of time travel).
  - Add the ability for circuit visualizations to target *Quantikz* LaTeX output.

    - Automatically rasterize using available (local) LaTeX installation.

  - Add the ability to label a circuit's output systems.
  - Implement the permutation (PERM) gate.
  - Add the ability for circuits to be optimized (to reduced gate depth).
  - Add the ability for circuits and/or gates to be decomposed (using a specified gate set).
  - Add the ability to use custom styles in the circuit diagram visualization.
  - Make the labelling/notation functionality more robust and extensible.
  - Investigate the addition of an ability to compile simple Qhronology programs to OpenQASM.

- Documentation:

  - More examples!

- Theory:

  - Expand section on the Cauchy problem near CTCs.
  - Add a section on the general theory of relativity and the associated geometric theories of CTCs.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames