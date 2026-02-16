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

.. raw:: latex

   \vspace*{-0.25cm}

.. only:: latex

   .. image:: /art/output/logo-main-50fps-3sec.png
      :width: 720px
      :alt: Qhronology logo
      :align: center

*Qhronology* is a Python package for computing the states of the chronology-respecting (CR) and chronology-violating (CV) quantum systems according to the foremost quantum prescriptions of closed timelike curves (CTCs). By providing a unique approach to describing general quantum objects (such as states and gates), Qhronology can also operate as a complete quantum circuit simulator, of which a prominent component is its engine for the visualization of quantum circuit diagrams. Its main features include:

- calculation of the states of the CR and CV quantum systems according to quantum-mechanical prescriptions of closed timelike curves

  - Deutsch's model (D-CTCs)
  - postselected teleportation (P-CTCs)

- simulation of general quantum information processing and computation

  - numerical and symbolic calculations involving any number of variables and parameters
  - (classical) replication of quantum experiments

- visualization of quantum circuit diagrams

  - text-based semigraphical diagrams constructed using glyphs from monospace fonts

The primary purpose of Qhronology is to facilitate the study of quantum models of antichronological time travel and quantum algorithms of quantum computing in both educational and research capacities. As part of this, the project aims to make the expression of quantum states, gates, circuits, and models of CTCs near-limitlessly possible within a framework that is syntactically simple, informationally dense, mathematically powerful, extremely flexible, and easily extensible. Qhronology therefore provides a sufficiently complete and self-contained set of tools with the intention that using external packages and libraries to perform transformations on its quantum constructs should not be necessary (at least in most cases). Its underlying mathematical system accomplishes this using the standard :math:`\Dimension`-dimensional matrix mechanics of discrete-variable quantum theory in a general :math:`\Complexes^\Dimension`-representation.

Qhronology is written entirely in the `Python <https://www.python.org/>`_ programming language. Being high-level, dynamically type-checked, and interpreted (at least within the context of its CPython reference implementation), Python is well-suited for building an accessible framework that emphasizes interactivity and scriptability. Additionally, like any popular language, it has both an extensive standard library and a plethora of powerful community packages available to it. Qhronology is built around features from two such packages: the canonical `SymPy <https://sympy.org>`_ and `NumPy <https://numpy.org>`_ projects. In particular, the package greatly leverages the symbolic and linear algebra capabilities of the former, and so aims to have a deep compatibility with SymPy and its matrix objects. It is therefore hoped that users who possess experience with these projects find Qhronology's interface both familiar and intuitive.

.. note::

   Qhronology, in its current form, is considered to be highly experimental. Its output may not always be correct, and some features may not work as intended. Additionally, please note that all components of the package, including its functions, methods, classes, modules, and subpackages, may be subject to change in future versions.

.. raw:: latex

   \vspace*{-1.00em}

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

   \vspace*{0.5em}

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

   \vspace*{-0.15em}

Quantum resolutions to antichronological time-travel paradoxes
--------------------------------------------------------------

.. .. raw:: latex

..    \begin{tabular}{M{0.55\textwidth}  C{0.45\textwidth}}

The fundamental indeterminism of quantum mechanics can be leveraged to provide resolutions to quantum formulations of classic time-travel paradoxes (such as the infamous *grandfather paradox*). A select few prescriptions by which this may be achieved, including Deutsch's model (D-CTCs) and the postselected teleportation prescription (P-CTCs), are implemented both as bare functions and class methods.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.5em}

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

   \vspace*{-0.15em}

Quantum circuit visualization
-----------------------------

.. .. raw:: latex

..    \begin{tabular}{M{0.55\textwidth}  C{0.45\textwidth}}

Quantum circuit diagrams provide a powerful picturalism through which any quantum process can be visualized as a network of quantum logic gates connected by wires. Qhronology provides this functionality for any quantum process constructed using its built-in classes.

.. Alternative methods of visualization, such as that provided by the LaTeX *Quantikz* package, are under consideration for future development.

.. .. literalinclude:: /figures/text/text_examples_algorithms_generation_w.txt
..    :class: semigraphical

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.5em}

.. only:: html

   .. image:: /figures/output/text_examples_algorithms_generation_w-dark.png
      :scale: 44 %
      :align: center
      :class: only-dark

   .. image:: /figures/output/text_examples_algorithms_generation_w-light.png
      :scale: 44 %
      :align: center
      :class: only-light

.. only:: latex

   .. image:: /figures/output/text_examples_algorithms_generation_w.pdf
      :scale: 135 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \vspace*{-0.15em}

.. raw:: latex

   \enlargethispage{\baselineskip}

Numerous examples
-----------------

.. .. raw:: latex

..    \begin{tabular}{M{0.65\textwidth}  C{0.35\textwidth}}

Bundled with the project is a small collection of complete examples that showcase its capabilities and syntax. These are divided into two categories: :ref:`sec:examples_algorithms` and :ref:`sec:examples_ctc`. The former contains implementations of canonical algorithms in quantum computing, while the latter consists of exotic circuits that use quantum mechanics to resolve paradoxical scenarios of antichronological time travel.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.25em}

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

   \vspace*{-0.15em}

Extensive documentation
-----------------------

.. .. raw:: latex

..    \begin{tabular}{M{0.55\textwidth}  C{0.45\textwidth}}

All of the functions, classes, and methods in each of the various submodules have been rigorously detailed in their respective sections within the documentation. This includes multiple examples of usage for each, aiding the user's understanding of every available feature.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.65em}

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
      :scale: 120 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. .. raw:: latex

..    \vspace*{-0.15em}

Foundational theory
-------------------

.. .. raw:: latex

..    \begin{tabular}{M{0.35\textwidth}  C{0.65\textwidth}}

All of the underlying mathematics upon which Qhronology is built is presented as a series of pedagogical reference articles within the documentation. This includes sections on the mathematical foundations of quantum mechanics (Hilbert spaces, linear operators, composite systems, etc.), quantum theory on both discrete and continuous Hilbert spaces, a brief overview of the quantum circuitry picturalism, and physical theories of time travel (both classical and quantum).

The aim of this theory is to serve as a comprehensive and complete reference for basic quantum mechanics and physical theories of time travel, thereby enabling the keen user to embark upon further research into these fascinating areas of study.

.. .. raw:: latex

..    &

.. raw:: latex

   \vspace*{0.65em}

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
      :scale: 115 %
      :align: center
      :class: light-dark hidden

.. .. raw:: latex

..    \end{tabular}

.. raw:: latex

   \newpage

Package installation and structure
==================================

Local installation of Qhronology from `PyPI <https://pypi.org/project/qhronology/>`_ can be accomplished using :sh:`pip` (`website <https://pip.pypa.io/>`_, `repository <https://github.com/pypa/pip>`_) via your operating system's command line, e.g.,

.. raw:: latex

   \begin{code}

.. code:: sh

   $ pip install qhronology

.. raw:: latex

   \end{code}

You may also be able to use an alternative package manager of your choice.

After installation, the package can be imported in Python in the standard way. One suggestion is as follows:

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

Requirements
------------

Within the package and documentation, SymPy and NumPy are imported in their conventional manners:

.. raw:: latex

   \begin{code}

.. code:: python

   import sympy as sp
   import numpy as np

.. raw:: latex

   \end{code}

Qhronology is compatible with the following package versions (from `requirements.txt <https://github.com/lgbishop/qhronology/blob/latest/requirements.txt>`_):

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

.. .. raw:: latex

..    \newpage

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
   
   \includegraphics[scale=1.25, trim=-0.05cm -0.02cm 0 -0.10cm]{text_examples_algorithms_generation_bell.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_bell-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_generation_bell-light.png
         :scale: 40 %
         :align: left
         :class: only-light

.. code:: python

   >>> phi_plus.print()
   |Φ+⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩

.. raw:: latex

   \end{codetitled}

:ref:`Quantum teleportation <eg:teleportation>`
-----------------------------------------------

Quantum teleportation of an arbitrary qubit :math:`\ket{\psi} = a\ket{0} + b\ket{1}`:

.. raw:: latex

   \begin{codetitled}{Quantum teleportation}{}

.. literalinclude:: /text/examples/algorithms/teleportation.py
   :language: python

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
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_teleportation-light.png
         :scale: 40 %
         :align: left
         :class: only-light

.. code:: python

   >>> teleporting_state.print()
   |ψ⟩ = a|0⟩ + b|1⟩

.. code:: python

   >>> teleported_state.print()
   ρ = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

.. code:: python

   >>> teleporting_state.distance(teleported_state)
   0

.. code:: python

   >>> teleporting_state.fidelity(teleported_state)
   1

.. raw:: latex

   \end{codetitled}

.. raw:: latex

   \newpage

:ref:`Unproven-theorem paradox <eg:unproven>`
---------------------------------------------

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
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_unproven-light.png
         :scale: 40 %
         :align: left
         :class: only-light

.. code:: python

   >>> unproven_DCTC_respecting.print()
   ρ_D = g|0,0⟩⟨0,0| + (1 - g)|1,1⟩⟨1,1|

.. code:: python

   >>> unproven_DCTC_violating.print()
   τ_D = g|0⟩⟨0| + (1 - g)|1⟩⟨1|

.. code:: python

   >>> unproven_PCTC_respecting.print()
   |ψ_P⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩

.. code:: python

   >>> unproven_PCTC_violating.print()
   τ_P = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{codetitled}

.. .. raw:: latex

..    \newpage

Documentation
=============

The latest version of the documentation for the package is available at:

- The official website: https://qhronology.org
- The official PDF document: `Qhronology.pdf <https://github.com/lgbishop/qhronology/blob/latest/docs/_build/latex/Qhronology.pdf>`_

Both of these are built using `Sphinx <https://www.sphinx-doc.org>`_ (`repository <https://github.com/sphinx-doc/sphinx>`_), with their shared source files residing within the ``docs`` directory at the root of the project's repository. This includes all project text and artwork. Please see `shell-sphinx.nix <https://github.com/lgbishop/qhronology/blob/latest/docs/shell-sphinx.nix>`_ within that directory for a list of dependencies required to build both documentation targets. Note that a full LaTeX system installation from 2024 or later is required to build the project's PDF documentation, figures, and artwork (including the logo). Also note that the documentation's rendered circuit diagrams (generated from the package itself) were created using a custom LaTeX template (`render-text.tex <https://github.com/lgbishop/qhronology/blob/latest/docs/source/figures/render-text.tex>`_) and associated shell script (`render-text.sh <https://github.com/lgbishop/qhronology/blob/latest/docs/source/figures/render-text.sh>`_).

.. include:: ./../../LICENSE

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. include:: ./../../CONTRIBUTING

.. raw:: latex

   \newpage

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

- The project's `technical paper <https://arxiv.org/abs/2601.17459>`_:

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
     abstract = {Qhronology is a novel scientific-computing package for studying quantum models of closed timelike curves (CTCs) and simulating general quantum information processing and computation. Written in Python, the program provides a comprehensive framework for analyzing quantum theories of antichronological time travel, including functionality to calculate quantum resolutions to temporal paradoxes. It also operates as a complete quantum circuit simulator, enabling the examination of quantum algorithms and protocols in both numerical and symbolic capacities. In this paper, we formally introduce Qhronology, beginning with discussion on aspects of its design philosophy and architecture. An overview of its basic usage is then presented, along with a collection of examples demonstrating its various capabilities within a variety of distinct contexts. Lastly, the performance of the package's circuit simulation component is characterized by way of some simple empirical benchmarking.},
     url = {https://arxiv.org/abs/2601.17459}
   }

.. raw:: latex

   \end{code}

.. raw:: latex

   \newpage

Possible future work
====================

- Package:

  - Write proper (more formal) unit tests.
  - Permit more intuitive usage (i.e., summation and multiplication) of quantum objects via operator overloading.
  - Tighter integration with SymPy's :python:`pprint()` functionality for enhanced state and gate printing.
  - Implement T-CTCs (the *transition-probabilities* quantum model of time travel).
  - Add the ability for circuit visualizations to target *Quantikz* LaTeX output.

    - Automatically rasterize using available (local) LaTeX installation.

  - Add the ability to label a circuit's output systems.
  - Implement the permutation (PERM) gate.
  - Add the ability for circuits to be optimized (to reduced gate depth).
  - Add the ability for circuits and/or gates to be decomposed (using a specified gate set).

- Documentation:

  - More examples.
  - Website:

    - Fix citation numbering.

- Theory:

  - Expand section on the Cauchy problem near CTCs.
  - Add a section on the general theory of relativity and the associated geometric theories of CTCs.