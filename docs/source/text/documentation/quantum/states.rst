.. include:: /styles.rst

.. _`sec:docs_states`:

******
States
******

In Qhronology, quantum states are both represented and constructed natively in the *computational* basis (also known as the *standard* or :math:`z`-basis). This is achieved primarily through the use of the :py:class:`~qhronology.quantum.states.QuantumState` class,

.. code:: python

   from qhronology.quantum.states import QuantumState

which itself relies chiefly on functionality provided by the matrix-generating :py:func:`~qhronology.mechanics.matrices.quantum_state` function:

.. code:: python

   from qhronology.mechanics.matrices import quantum_state

Characterization of quantum states is facilitated by two properties: ``form`` distinguishes between states which are ``"vector"`` or ``"matrix"``, while ``kind`` distinguishes those which are ``"pure"`` or ``"mixed"``. Of the four combinations (pairs) of these properties, all are valid except for the pairing of ``"vector"`` and ``"mixed"``. Therefore, to expedite and simplify state instantiation, the following subclasses of the base class :py:class:`~qhronology.quantum.states.QuantumState` are provided:

.. code:: python

   from qhronology.quantum.states import VectorState, MatrixState, PureState, MixedState

These classes are *specialized* (or *restrictive*) subclasses, meaning that they do not extend the base class in any way, and instead merely constrain its functionality in order to enforce the desired behaviour. They therefore allow for quantum state objects to be initialized in ways that are more concise than the general :py:class:`~qhronology.quantum.states.QuantumState` class.

Main class
==========

.. autoclass:: qhronology.quantum.states.QuantumState
   :show-inheritance:

   .. rubric:: :styleheader6:`Examples`

   >>> qubit_vector = QuantumState(
   ...     spec=[("a", [0]), ("b", [1])],
   ...     form="vector",
   ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
   ...     conditions=[("a*conjugate(a) + b*conjugate(b)", "1")],
   ...     norm=1,
   ...     label="ψ",
   ... )
   >>> qubit_vector.output()
   Matrix([
   [a],
   [b]])
   >>> qubit_vector.print()
   |ψ⟩ = a|0⟩ + b|1⟩
   >>> qubit_vector.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_vector-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_vector-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> qutrit_vector = QuantumState(
   ...     spec=[("a", [0]), ("b", [1]), ("c", [2])],
   ...     form="vector",
   ...     dim=3,
   ...     symbols={
   ...         "a": {"complex": True},
   ...         "b": {"complex": True},
   ...         "c": {"complex": True},
   ...     },
   ...     conditions=[("a*conjugate(a) + b*conjugate(b) + c*conjugate(c)", "1")],
   ...     norm=1,
   ...     label="φ",
   ... )
   >>> qutrit_vector.output()
   Matrix([
   [a],
   [b],
   [c]])
   >>> qutrit_vector.print()
   |φ⟩ = a|0⟩ + b|1⟩ + c|2⟩
   >>> qutrit_vector.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qutrit_vector-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qutrit_vector-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> qubit_pure = QuantumState(
   ...     spec=[("α", [0]), ("β", [1])],
   ...     form="matrix",
   ...     kind="pure",
   ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
   ...     conditions=[("α*conjugate(α) + β*conjugate(β)", 1)],
   ...     norm=1,
   ...     label="ξ",
   ... )
   >>> qubit_pure.output()
   Matrix([
   [α*conjugate(α), α*conjugate(β)],
   [β*conjugate(α), β*conjugate(β)]])
   >>> qubit_pure.print()
   |ξ⟩⟨ξ| = α*conjugate(α)|0⟩⟨0| + α*conjugate(β)|0⟩⟨1| + β*conjugate(α)|1⟩⟨0| + β*conjugate(β)|1⟩⟨1|
   >>> qubit_pure.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_pure-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_pure-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> qubit_mixed = QuantumState(
   ...     spec=[("p", [0]), ("1 - p", [1])],
   ...     form="matrix",
   ...     kind="mixed",
   ...     symbols={"p": {"real": True}},
   ...     norm=1,
   ...     label="τ",
   ... )
   >>> qubit_mixed.output()
   Matrix([
   [p,     0],
   [0, 1 - p]])
   >>> qubit_mixed.print()
   τ = p|0⟩⟨0| + (1 - p)|1⟩⟨1|
   >>> qubit_mixed.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_mixed-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_mixed-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> custom_vector = QuantumState(spec=[["μ"], ["ν"]], kind="mixed", label="η")
   >>> custom_vector.output()
   Matrix([
   [μ*conjugate(μ), μ*conjugate(ν)],
   [ν*conjugate(μ), ν*conjugate(ν)]])
   >>> custom_vector.print()
   η = μ*conjugate(μ)|0⟩⟨0| + μ*conjugate(ν)|0⟩⟨1| + ν*conjugate(μ)|1⟩⟨0| + ν*conjugate(ν)|1⟩⟨1|
   >>> custom_vector.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_vector-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_vector-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> custom_matrix = QuantumState(spec=[["w", "x"], ["y", "z"]], kind="mixed", label="ω")
   >>> custom_matrix.output()
   Matrix([
   [w, x],
   [y, z]])
   >>> custom_matrix.print()
   ω = w|0⟩⟨0| + x|0⟩⟨1| + y|1⟩⟨0| + z|1⟩⟨1|
   >>> custom_matrix.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_matrix-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_matrix-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> bell_state = QuantumState(spec=[(1, [0, 0]), (1, [1, 1])], form="vector", norm=1, label="Φ")
   >>> bell_state.output()
   Matrix([
   [sqrt(2)/2],
   [        0],
   [        0],
   [sqrt(2)/2]])
   >>> bell_state.print()
   |Φ⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩
   >>> bell_state.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_bipartite_bell-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_bipartite_bell-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}

   >>> tripartite_zero = QuantumState(spec=[(1, [0, 0, 0])], form="vector", label="0,0,0")
   >>> tripartite_zero.output()
   Matrix([
   [1],
   [0],
   [0],
   [0],
   [0],
   [0],
   [0],
   [0]])
   >>> tripartite_zero.print()
   |0,0,0⟩ = |0,0,0⟩
   >>> tripartite_zero.diagram()

   ..

      .. raw:: latex
         
         \vspace{1em}
         \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_tripartite_zero-dark.png
            :scale: 40 %
            :align: left
            :class: only-dark

      .. only:: html or latex

         .. image:: /figures/output/text_examples_docstrings_state_tripartite_zero-light.png
            :scale: 40 %
            :align: left
            :class: only-light

      .. raw:: latex
         
         \end{mdframed}
         \vspace{1em}
   
   .. raw:: latex

      \hrulefillthick

.. _`sec:docs_states_properties`:

Constructor argument properties
-------------------------------

.. autoproperty:: qhronology.quantum.states.QuantumState.spec

.. raw:: latex

   \hrulefillthick
   
.. autoproperty:: qhronology.quantum.states.QuantumState.form

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.kind

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.dim

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.symbols

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.conditions

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.norm

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.conjugate

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.label

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.notation

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.family

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.debug

.. raw:: latex

   \hrulefillthick

Read-only properties
--------------------

.. autoproperty:: qhronology.quantum.states.QuantumState.systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.num_systems

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.is_vector

.. raw:: latex

   \hrulefillthick

.. autoproperty:: qhronology.quantum.states.QuantumState.matrix


.. raw:: latex

   \hrulefillthick

.. _`sec:docs_states_methods`:

Methods
-------

.. automethod:: qhronology.quantum.states.QuantumState.output

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.diagram

   .. rubric:: :styleheader6:`Examples`

   For usage examples, please see those of the :py:class:`~qhronology.quantum.states.QuantumState` class itself.

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_states_operations`:

Operations
----------

All of these methods (except for :py:meth:`~qhronology.quantum.states.QuantumState.reset`) are inherited from :py:class:`~qhronology.mechanics.operations.OperationsMixin`.

.. automethod:: qhronology.quantum.states.QuantumState.reset

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.densify

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.dagger

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.simplify

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.apply

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.rewrite

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.normalize

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.coefficient

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.partial_trace

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.measure

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.postselect

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_states_quantities`:

Quantities
----------

All of these methods are inherited from :py:class:`~qhronology.mechanics.quantities.QuantitiesMixin`.

.. automethod:: qhronology.quantum.states.QuantumState.trace

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.purity

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.distance

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.fidelity

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.entropy

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.mutual

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_states_subclasses`:

Subclasses
==========

.. autoclass:: qhronology.quantum.states.VectorState

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.states.MatrixState

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.states.PureState

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.states.MixedState