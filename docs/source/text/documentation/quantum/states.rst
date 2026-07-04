.. include:: /styles.rst

.. _`sec:docs_states`:

******
States
******

In Qhronology, quantum states are described in the *computational* basis (also known as the *standard* basis or the :math:`z`-basis) and represented by instances of the :py:class:`~qhronology.quantum.states.QuantumState` class:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.states import QuantumState

.. raw:: latex

   \end{code}

When using this class, the characterization of a quantum state is facilitated primarily by four arguments (or properties):

#. :py:attr:`~qhronology.quantum.states.QuantumState.spec`: quantifies the values (i.e., amplitudes or probabilities) corresponding to specific components of the state's mathematical representation.

#. :py:attr:`~qhronology.quantum.states.QuantumState.form`: describes the state as being either a :python:`"vector"` or a :python:`"matrix"`. Defaults to :python:`"vector"`.

#. :py:attr:`~qhronology.quantum.states.QuantumState.kind`: describes the state as being either :python:`"pure"` or :python:`"mixed"`. Defaults to :python:`"pure"`.

#. :py:attr:`~qhronology.quantum.states.QuantumState.dim`: quantifies the state's dimensionality as an integer greater than or equal to :python:`2`. Defaults to :python:`2`.

Note that, of the four combinations (pairs) of the values which may be passed to :py:attr:`~qhronology.quantum.states.QuantumState.form` and :py:attr:`~qhronology.quantum.states.QuantumState.kind`, all are valid except for the pairing of :python:`"vector"` and :python:`"mixed"`.

To expedite and simplify state instantiation, the following subclasses of the base class :py:class:`~qhronology.quantum.states.QuantumState` are provided:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.quantum.states import VectorState, MatrixState, PureState, MixedState

.. raw:: latex

   \end{code}

These classes are *specialized* (or *restricting*) subclasses, meaning that they do not extend the base class in any way, and instead merely constrain its functionality in order to enforce the desired behaviour. They therefore allow for quantum state objects to be initialized in ways that are more concise than the general :py:class:`~qhronology.quantum.states.QuantumState` class. See :numref:`sec:docs_states_subclasses` :ref:`sec:docs_states_subclasses` for more information.

.. raw:: latex

   \newpage

Main class
==========

.. autoclass:: qhronology.quantum.states.QuantumState
   :show-inheritance:

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> qubit_vector = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
      ...     norm=1,
      ...     label="ψ",
      ... )
      >>> qubit_vector.output(simplify=True)
      Matrix([
      [a],
      [b]])
      >>> qubit_vector.print(simplify=True)
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> qubit_vector.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_unipartite_qubit_vector.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_vector-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_vector-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> qutrit_vector = QuantumState(
      ...     spec=[("a", [0]), ("b", [1]), ("c", [2])],
      ...     form="vector",
      ...     dim=3,
      ...     symbols={
      ...         "a": {"complex": True},
      ...         "b": {"complex": True},
      ...         "c": {"complex": True},
      ...     },
      ...     substitutions=[
      ...         ("a*conjugate(a) + b*conjugate(b) + c*conjugate(c)", 1),
      ...     ],
      ...     norm=1,
      ...     label="φ",
      ... )
      >>> qutrit_vector.output(simplify=True)
      Matrix([
      [a],
      [b],
      [c]])
      >>> qutrit_vector.print(simplify=True)
      |φ⟩ = a|0⟩ + b|1⟩ + c|2⟩
      >>> qutrit_vector.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_unipartite_qutrit_vector.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qutrit_vector-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qutrit_vector-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> qubit_pure = QuantumState(
      ...     spec=[("α", [0]), ("β", [1])],
      ...     form="matrix",
      ...     kind="pure",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("α*conjugate(α) + β*conjugate(β)", 1)],
      ...     norm=1,
      ...     label="ξ",
      ... )
      >>> qubit_pure.output(simplify=True)
      Matrix([
      [α*conjugate(α), α*conjugate(β)],
      [β*conjugate(α), β*conjugate(β)]])
      >>> qubit_pure.print(simplify=True)
      |ξ⟩⟨ξ| = α*conjugate(α)|0⟩⟨0| + α*conjugate(β)|0⟩⟨1| + β*conjugate(α)|1⟩⟨0| + β*conjugate(β)|1⟩⟨1|
      >>> qubit_pure.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_unipartite_qubit_pure.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_pure-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_pure-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> qubit_mixed = QuantumState(
      ...     spec=[("p", [0]), ("1 - p", [1])],
      ...     form="matrix",
      ...     kind="mixed",
      ...     symbols={"p": {"real": True, "nonnegative": True}},
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

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_unipartite_qubit_mixed.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_mixed-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_qubit_mixed-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{-\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> custom_vector = QuantumState(
      ...     spec=[["μ"], ["ν"]],
      ...     kind="mixed",
      ...     label="η",
      ... )
      >>> custom_vector.output()
      Matrix([
      [μ*conjugate(μ), μ*conjugate(ν)],
      [ν*conjugate(μ), ν*conjugate(ν)]])
      >>> custom_vector.print()
      η = μ*conjugate(μ)|0⟩⟨0| + μ*conjugate(ν)|0⟩⟨1| + ν*conjugate(μ)|1⟩⟨0| + ν*conjugate(ν)|1⟩⟨1|
      >>> custom_vector.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_unipartite_custom_vector.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_vector-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_vector-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> custom_matrix = QuantumState(
      ...     spec=[["w", "x"], ["y", "z"]],
      ...     kind="mixed",
      ...     label="ω"
      ... )
      >>> custom_matrix.output()
      Matrix([
      [w, x],
      [y, z]])
      >>> custom_matrix.print()
      ω = w|0⟩⟨0| + x|0⟩⟨1| + y|1⟩⟨0| + z|1⟩⟨1|
      >>> custom_matrix.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_unipartite_custom_matrix.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_matrix-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_unipartite_custom_matrix-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> bell_state = QuantumState(
      ...     spec=[(1, [0, 0]), (1, [1, 1])],
      ...     form="vector",
      ...     norm=1,
      ...     label="Φ",
      ... )
      >>> bell_state.output()
      Matrix([
      [sqrt(2)/2],
      [        0],
      [        0],
      [sqrt(2)/2]])
      >>> bell_state.print()
      |Φ⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩
      >>> bell_state.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_bipartite_bell.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_bipartite_bell-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_bipartite_bell-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex
      
      \enlargethispage{1\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> ghz_state = QuantumState(
      ...     spec=[(1, [0, 0, 0]), (1, [1, 1, 1])],
      ...     form="vector",
      ...     norm=1,
      ...     label="GHZ",
      ... )
      >>> ghz_state.output()
      Matrix([
      [sqrt(2)/2],
      [        0],
      [        0],
      [        0],
      [        0],
      [        0],
      [        0],
      [sqrt(2)/2]])
      >>> ghz_state.print()
      |GHZ⟩ = sqrt(2)/2|0,0,0⟩ + sqrt(2)/2|1,1,1⟩
      >>> ghz_state.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_tripartite_ghz.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_tripartite_ghz-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_tripartite_ghz-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}

   .. raw:: latex
      
      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> w_state = QuantumState(
      ...     spec=[(1, [0, 0, 1]), (1, [0, 1, 0]), (1, [1, 0, 0])],
      ...     form="vector",
      ...     norm=1,
      ...     label="W",
      ... )
      >>> w_state.output()
      Matrix([
      [        0],
      [sqrt(3)/3],
      [sqrt(3)/3],
      [        0],
      [sqrt(3)/3],
      [        0],
      [        0],
      [        0]])
      >>> w_state.print()
      |W⟩ = sqrt(3)/3|0,0,1⟩ + sqrt(3)/3|0,1,0⟩ + sqrt(3)/3|1,0,0⟩
      >>> w_state.diagram()

   .. raw:: latex
      
      \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 0.00cm]{text_examples_docstrings_state_tripartite_w.pdf}
      \vspace{-1\baselineskip}

   ..

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_tripartite_w-dark.png
            :scale: 36 %
            :align: left
            :class: only-dark

      .. only:: html

         .. image:: /figures/output/text_examples_docstrings_state_tripartite_w-light.png
            :scale: 36 %
            :align: left
            :class: only-light

   .. raw:: latex

      \end{code}
      
   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_states_properties`:

Constructor argument properties
-------------------------------

.. autoproperty:: qhronology.quantum.states.QuantumState.spec

   The object passed to :python:`spec` can be any of the following four types:

   - a SymPy matrix
   - a NumPy array
   - a list of lists (describing a matrix)
   - a list of 2-tuples

   The data type of the elements contained within the first three of these options can be any of the following: numerical (including all scalars from SymPy, NumPy, and the standard library), SymPy symbolic (including expressions), or string representations of such scalar types. However, the fourth option---the bespoke list-of-tuples format---is intended to be the primary way of characterizing quantum states. Its structure is reasonably straightforward: each 2-tuple contains an amplitude or probability (a scalar expression as a numerical, symbolic, or string value) followed by a list of non-negative integers corresponding to the levels of the number states of the desired basis vector. In the case of multiple such tuples in the given list, the resulting quantum state is the sum of all components formed from each individual tuple.

   For example, passing the list :python:`[("α", [0, 0]), ("β", [1, 1])]` to :python:`spec` in a :py:class:`~qhronology.quantum.states.QuantumState` construction yields a state which corresponds to one of the following forms (depending on the values passed to the other core arguments or properties):

   - :py:attr:`~qhronology.quantum.states.QuantumState.form` is :python:`"vector"`: :math:`\alpha\ket{0,0} + \beta\ket{1,1}`
   - :py:attr:`~qhronology.quantum.states.QuantumState.form` is :python:`"matrix"`:

     - :py:attr:`~qhronology.quantum.states.QuantumState.kind` is :python:`"pure"`: :math:`\abs{\alpha}^2\ket{0,0}\bra{0,0} + \alpha\beta^*\ket{0,0}\bra{1,1} + \alpha^*\beta\ket{1,1}\bra{0,0} + \abs{\beta}^2\ket{1,1}\bra{1,1}`
     - :py:attr:`~qhronology.quantum.states.QuantumState.kind` is :python:`"mixed"`: :math:`\alpha\ket{0,0}\bra{0,0} + \beta\ket{1,1}\bra{1,1}`

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

.. autoproperty:: qhronology.quantum.states.QuantumState.substitutions

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

.. automethod:: qhronology.quantum.states.QuantumState.print

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> vector_state = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> vector_state.output()
      Matrix([
      [a],
      [b]])
      >>> vector_state.print()
      |ψ⟩ = a|0⟩ + b|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> mixed_matrix_state = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="matrix",
      ...     kind="mixed",
      ...     label="ρ",
      ... )
      >>> mixed_matrix_state.output()
      Matrix([
      [a, 0],
      [0, b]])
      >>> mixed_matrix_state.print()
      ρ = a|0⟩⟨0| + b|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> pure_matrix_state = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="matrix",
      ...     kind="pure",
      ...     label="ψ",
      ... )
      >>> pure_matrix_state.output()
      Matrix([
      [a*conjugate(a), a*conjugate(b)],
      [b*conjugate(a), b*conjugate(b)]])
      >>> pure_matrix_state.print()
      |ψ⟩⟨ψ| = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> composite_vector_state = QuantumState(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> composite_vector_state.output()
      Matrix([
      [a],
      [0],
      [0],
      [b]])
      >>> composite_vector_state.print()
      |ψ⟩ = a|0,0⟩ + b|1,1⟩
      >>> composite_vector_state.print(delimiter="")
      |ψ⟩ = a|00⟩ + b|11⟩
      >>> composite_vector_state.print(product=True)
      |ψ⟩ = a|0⟩⊗|0⟩ + b|1⟩⊗|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> composite_mixed_matrix_state = QuantumState(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     form="matrix",
      ...     kind="mixed",
      ...     label="ρ",
      ... )
      >>> composite_mixed_matrix_state.output()
      Matrix([
      [a, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, b]])
      >>> composite_mixed_matrix_state.print()
      ρ = a|0,0⟩⟨0,0| + b|1,1⟩⟨1,1|
      >>> composite_mixed_matrix_state.print(delimiter="")
      ρ = a|00⟩⟨00| + b|11⟩⟨11|
      >>> composite_mixed_matrix_state.print(product=True)
      ρ = a|0⟩⟨0|⊗|0⟩⟨0| + b|1⟩⟨1|⊗|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> composite_pure_matrix_state = QuantumState(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     form="matrix",
      ...     kind="pure",
      ...     label="ψ",
      ... )
      >>> composite_pure_matrix_state.output()
      Matrix([
      [a*conjugate(a), 0, 0, a*conjugate(b)],
      [             0, 0, 0,              0],
      [             0, 0, 0,              0],
      [b*conjugate(a), 0, 0, b*conjugate(b)]])
      >>> composite_pure_matrix_state.print()
      |ψ⟩⟨ψ| = a*conjugate(a)|0,0⟩⟨0,0| + a*conjugate(b)|0,0⟩⟨1,1| + b*conjugate(a)|1,1⟩⟨0,0| + b*conjugate(b)|1,1⟩⟨1,1|
      >>> composite_pure_matrix_state.print(delimiter="")
      |ψ⟩⟨ψ| = a*conjugate(a)|00⟩⟨00| + a*conjugate(b)|00⟩⟨11| + b*conjugate(a)|11⟩⟨00| + b*conjugate(b)|11⟩⟨11|
      >>> composite_pure_matrix_state.print(product=True)
      |ψ⟩⟨ψ| = a*conjugate(a)|0⟩⟨0|⊗|0⟩⟨0| + a*conjugate(b)|0⟩⟨1|⊗|0⟩⟨1| + b*conjugate(a)|1⟩⟨0|⊗|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|⊗|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \newpage
   \null
   \vspace*{-2\baselineskip}

.. automethod:: qhronology.quantum.states.QuantumState.diagram

   .. raw:: latex

      \vspace*{-0.35\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   For usage examples, please see those of the :py:class:`~qhronology.quantum.states.QuantumState` class itself.

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \vspace*{-0.25\baselineskip}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \vspace*{-0.25\baselineskip}

.. raw:: latex

   \enlargethispage{\baselineskip}

.. _`sec:docs_states_operations`:

Operations
----------

All of these methods (except for :py:meth:`~qhronology.quantum.states.QuantumState.reset`) are inherited from :py:class:`~qhronology.mechanics.operations.OperationsMixin`.

.. automethod:: qhronology.quantum.states.QuantumState.reset

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.densify

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> psi.densify()
      >>> psi.print()
      |ψ⟩⟨ψ| = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.dagger

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> psi.dagger()
      >>> psi.print()
      ⟨ψ| = conjugate(a)⟨0| + conjugate(b)⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.simplify

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix(
      ...     [
      ...         ["(a**2 - 1)/(a - 1) - 1",
      ...          "log(cos(b) + I*sin(b))/I"],
      ...         ["acos((exp(I*c) + exp(-I*c))/2)",
      ...          "d**log(E*(sin(d)**2 + cos(d)**2))"],
      ...     ]
      ... )
      >>> rho = QuantumState(spec=matrix, form="matrix", label="ρ")
      >>> rho.print()
      ρ = (-1 + (a**2 - 1)/(a - 1))|0⟩⟨0| + -I*log(I*sin(b) + cos(b))|0⟩⟨1| + acos(exp(I*c)/2 + exp(-I*c)/2)|1⟩⟨0| + d**log(E*(sin(d)**2 + cos(d)**2))|1⟩⟨1|
      >>> rho.simplify()
      >>> rho.print()
      ρ = a|0⟩⟨0| + b|0⟩⟨1| + c|1⟩⟨0| + d|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.rewrite

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[("cos(θ)", [0]), ("sin(θ)", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = cos(θ)|0⟩ + sin(θ)|1⟩
      >>> psi.rewrite(sp.exp)
      >>> psi.print()
      |ψ⟩ = (exp(I*θ)/2 + exp(-I*θ)/2)|0⟩ + -I*(exp(I*θ) - exp(-I*θ))/2|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.apply

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[("a*b + b*c + c*a", [0]), ("x*y + y*z + z*x", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = (a*b + a*c + b*c)|0⟩ + (x*y + x*z + y*z)|1⟩
      >>> psi.apply(sp.collect, {"syms": ["a", "x"]})
      >>> psi.print()
      |ψ⟩ = (a*(b + c) + b*c)|0⟩ + (x*(y + z) + y*z)|1⟩
      >>> psi.apply(sp.expand)
      >>> psi.print()
      |ψ⟩ = (a*b + a*c + b*c)|0⟩ + (x*y + x*z + y*z)|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.normalize

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> psi.normalize()
      >>> psi.print()
      |ψ⟩ = a/sqrt(a*conjugate(a) + b*conjugate(b))|0⟩ + b/sqrt(a*conjugate(a) + b*conjugate(b))|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> identity = QuantumState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     symbols={"d": {"real": True}},
      ...     label="I",
      ... )
      >>> identity.print()
      I = |0⟩⟨0| + |1⟩⟨1|
      >>> identity.normalize("2/d")
      >>> identity.print()
      I = 1/d|0⟩⟨0| + 1/d|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.coefficient

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = |0⟩ + |1⟩
      >>> psi.coefficient(1 / sp.sqrt(2))
      >>> psi.print()
      |ψ⟩ = sqrt(2)/2|0⟩ + sqrt(2)/2|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> phi = QuantumState(
      ...     spec=[("cos(θ)", [0]), ("sin(θ)", [1])],
      ...     form="vector",
      ...     label="φ",
      ... )
      >>> phi.print()
      |φ⟩ = cos(θ)|0⟩ + sin(θ)|1⟩
      >>> phi.coefficient("exp(I*ξ)")
      >>> phi.print()
      |φ⟩ = exp(I*ξ)*cos(θ)|0⟩ + exp(I*ξ)*sin(θ)|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{\baselineskip}

.. automethod:: qhronology.quantum.states.QuantumState.partial_trace

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[
      ...         ("a*u", [0, 0]),
      ...         ("b*u", [1, 0]),
      ...         ("a*v", [0, 1]),
      ...         ("b*v", [1, 1]),
      ...     ],
      ...     form="vector",
      ...     substitutions=[
      ...         ("a*conjugate(a) + b*conjugate(b)", 1),
      ...         ("u*conjugate(u) + v*conjugate(v)", 1),
      ...     ],
      ...     label="Ψ",
      ... )
      >>> psi.print()
      |Ψ⟩ = a*u|0,0⟩ + a*v|0,1⟩ + b*u|1,0⟩ + b*v|1,1⟩
      >>> psi.partial_trace([1])
      >>> psi.simplify()
      >>> psi.notation = "ρ"
      >>> psi.print()
      ρ = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> bell = QuantumState(
      ...     spec=[(1, [0, 0]), (1, [1, 1])],
      ...     form="vector",
      ...     norm=1,
      ...     label="Φ",
      ... )
      >>> bell.print()
      |Φ⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩
      >>> bell.partial_trace([0])
      >>> bell.notation = "ρ"
      >>> bell.print()
      ρ = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.measure

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> from qhronology.quantum.gates import Pauli
      >>> psi = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> I = Pauli(index=0)
      >>> X = Pauli(index=1)
      >>> Y = Pauli(index=2)
      >>> Z = Pauli(index=3)
      >>> psi.measure(
      ...     operators=[I, X, Y, Z],
      ...     observable=True,
      ...     statistics=True,
      ... )
      [a*conjugate(a) + b*conjugate(b),
       a*conjugate(b) + b*conjugate(a),
       I*(a*conjugate(b) - b*conjugate(a)),
       a*conjugate(a) - b*conjugate(b)]
      >>> psi.measure(
      ...     operators=[I, X, Y, Z],
      ...     observable=True,
      ...     statistics=False,
      ... )
      >>> psi.simplify()
      >>> psi.coefficient(sp.Rational(1, 2))
      >>> psi.label += "′"
      >>> psi.print()
      |ψ′⟩⟨ψ′| = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> from qhronology.mechanics.matrices import ket
      >>> psi = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     label="ψ",
      ... )
      >>> psi.print()
      |ψ⟩ = a|0⟩ + b|1⟩
      >>> psi.measure(
      ...     operators=[ket(0), ket(1)],
      ...     observable=False,
      ...     statistics=True,
      ... )
      [a*conjugate(a), b*conjugate(b)]
      >>> psi.measure(
      ...     operators=[ket(0), ket(1)],
      ...     observable=False,
      ...     statistics=False,
      ... )
      >>> psi.notation = "ρ′"
      >>> psi.print()
      ρ′ = a*conjugate(a)|0⟩⟨0| + b*conjugate(b)|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.postselect

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> psi = QuantumState(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     form="vector",
      ...     label="Ψ",
      ... )
      >>> phi = QuantumState(
      ...     spec=[("c", [0]), ("d", [1])],
      ...     form="vector",
      ...     label="φ",
      ... )
      >>> psi.print()
      |Ψ⟩ = a|0,0⟩ + b|1,1⟩
      >>> phi.print()
      |φ⟩ = c|0⟩ + d|1⟩
      >>> psi.postselect([(phi, [0])])
      >>> psi.label += "′"
      >>> psi.print()
      |Ψ′⟩ = a*conjugate(c)|0⟩ + b*conjugate(d)|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> from qhronology.mechanics.matrices import ket
      >>> psi = QuantumState(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     form="vector",
      ...     label="Ψ",
      ... )
      >>> psi.print()
      |Ψ⟩ = a|0,0⟩ + b|1,1⟩
      >>> psi.label += "′"
      >>> psi.postselect([(ket(0), [0])])
      >>> psi.print()
      |Ψ′⟩ = a|0⟩
      >>> psi.reset()
      >>> psi.postselect([(ket(1), [0])])
      >>> psi.print()
      |Ψ′⟩ = b|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. _`sec:docs_states_quantities`:

Quantities
----------

All of these methods are inherited from :py:class:`~qhronology.mechanics.quantities.QuantitiesMixin`.

.. automethod:: qhronology.quantum.states.QuantumState.trace

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
      ...     norm=1,
      ... )
      >>> state.trace()
      1

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state = QuantumState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     kind="mixed",
      ...     symbols={"d": {"real": True}},
      ...     norm="1/d",
      ... )
      >>> state.trace()
      1/d

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.purity

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
      ...     norm=1,
      ... )
      >>> state.purity()
      1

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state = QuantumState(
      ...     spec=[("p", [0]), ("1 - p", [1])],
      ...     kind="mixed",
      ...     norm=1,
      ... )
      >>> state.purity()
      p**2 + (1 - p)**2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.distance

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_A = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
      ...     norm=1,
      ... )
      >>> state_B = QuantumState(
      ...     spec=[("c", [0]), ("d", [1])],
      ...     form="vector",
      ...     symbols={"c": {"complex": True}, "d": {"complex": True}},
      ...     substitutions=[("c*conjugate(c) + d*conjugate(d)", 1)],
      ...     norm=1,
      ... )
      >>> state_A.distance(state_A)
      0
      >>> state_B.distance(state_B)
      0
      >>> state_A.distance(state_B)
      sqrt((a*conjugate(b) - c*conjugate(d))*(b*conjugate(a) - d*conjugate(c)) + (b*conjugate(b) - d*conjugate(d))**2)/2 + sqrt((a*conjugate(a) - c*conjugate(c))**2 + (a*conjugate(b) - c*conjugate(d))*(b*conjugate(a) - d*conjugate(c)))/2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_A = QuantumState(
      ...     spec=[("p", [0]), ("1 - p", [1])],
      ...     kind="mixed",
      ...     symbols={"p": {"positive": True}},
      ...     norm=1,
      ... )
      >>> state_B = QuantumState(
      ...     spec=[("q", [0]), ("1 - q", [1])],
      ...     kind="mixed",
      ...     symbols={"q": {"positive": True}},
      ...     norm=1,
      ... )
      >>> state_A.distance(state_B)
      Abs(p - q)

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> plus_state = QuantumState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     form="vector",
      ...     norm=1,
      ... )
      >>> minus_state = QuantumState(
      ...     spec=[(1, [0]), (-1, [1])],
      ...     form="vector",
      ...     norm=1,
      ... )
      >>> plus_state.distance(minus_state)
      1

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.fidelity

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_A = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
      ...     norm=1,
      ... )
      >>> state_B = QuantumState(
      ...     spec=[("c", [0]), ("d", [1])],
      ...     form="vector",
      ...     symbols={"c": {"complex": True}, "d": {"complex": True}},
      ...     substitutions=[("c*conjugate(c) + d*conjugate(d)", 1)],
      ...     norm=1,
      ... )
      >>> state_A.fidelity(state_A)
      1
      >>> state_B.fidelity(state_B)
      1
      >>> state_A.fidelity(state_B)
      (a*conjugate(c) + b*conjugate(d))*(c*conjugate(a) + d*conjugate(b))

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \newpage

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_A = QuantumState(
      ...     spec=[("p", [0]), ("1 - p", [1])],
      ...     kind="mixed",
      ...     symbols={"p": {"positive": True}},
      ...     norm=1,
      ... )
      >>> state_B = QuantumState(
      ...     spec=[("q", [0]), ("1 - q", [1])],
      ...     kind="mixed",
      ...     symbols={"q": {"positive": True}},
      ...     norm=1,
      ... )
      >>> state_A.fidelity(state_B)
      (sqrt(p)*sqrt(q) + sqrt((1 - p)*(1 - q)))**2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> plus_state = QuantumState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     form="vector",
      ...     norm=1,
      ... )
      >>> minus_state = QuantumState(
      ...     spec=[(1, [0]), (-1, [1])],
      ...     form="vector",
      ...     norm=1,
      ... )
      >>> plus_state.fidelity(minus_state)
      0

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. automethod:: qhronology.quantum.states.QuantumState.entropy

   .. raw:: latex

      \enlargethispage{-\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_A = QuantumState(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
      ...     norm=1,
      ... )
      >>> state_B = QuantumState(
      ...     spec=[("c", [0]), ("d", [1])],
      ...     form="vector",
      ...     symbols={"c": {"complex": True}, "d": {"complex": True}},
      ...     substitutions=[("c*conjugate(c) + d*conjugate(d)", 1)],
      ...     norm=1,
      ... )
      >>> state_A.entropy()
      0
      >>> state_B.entropy()
      0
      >>> state_A.entropy(state_B)
      0

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_A = QuantumState(
      ...     spec=[("p", [0]), ("1 - p", [1])],
      ...     kind="mixed",
      ...     symbols={"p": {"positive": True}},
      ...     norm=1,
      ... )
      >>> state_B = QuantumState(
      ...     spec=[("q", [0]), ("1 - q", [1])],
      ...     kind="mixed",
      ...     symbols={"q": {"positive": True}},
      ...     norm=1,
      ... )
      >>> state_A.entropy()
      (-p*log(p) + (p - 1)*log(1 - p))/log(2)
      >>> state_B.entropy()
      (-q*log(q) + (q - 1)*log(1 - q))/log(2)
      >>> state_A.entropy(state_B, base="d")
      (-(p - 1)*(log(1 - p) - log(1 - q)) + log((p/q)**p))/log(d)

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \vspace*{-0.25\baselineskip}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{\baselineskip}

.. automethod:: qhronology.quantum.states.QuantumState.mutual

   .. raw:: latex

      \vspace*{-0.35\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_AB = QuantumState(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     form="vector",
      ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
      ...     substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
      ...     norm=1,
      ... )
      >>> state_AB.mutual([0], [1])
      2*(-a*log(a*conjugate(a))*conjugate(a) - b*log(b*conjugate(b))*conjugate(b))/log(2)

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_AB = QuantumState(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     kind="mixed",
      ...     symbols={"a": {"positive": True}, "b": {"positive": True}},
      ...     substitutions=[("a + b", 1)],
      ...     norm=1,
      ... )
      >>> state_AB.mutual([0], [1], base="d")
      -log(a**a*b**b)/log(d)

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> state_ABC = QuantumState(
      ...     spec=[("a", [1, 0, 0]), ("b", [0, 1, 0]), ("c", [0, 0, 1])],
      ...     kind="mixed",
      ...     symbols={
      ...         "a": {"positive": True},
      ...         "b": {"positive": True},
      ...         "c": {"positive": True},
      ...     },
      ...     substitutions=[("a + b + c", 1)],
      ...     norm=1,
      ... )
      >>> state_ABC.mutual([0], [1])
      -log((a**a*b**b*c**c)**(1/log(2)))

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \vspace*{-0.35\baselineskip}

.. _`sec:docs_states_subclasses`:

Subclasses
==========

.. raw:: latex

   \enlargethispage{\baselineskip}

.. autoclass:: qhronology.quantum.states.VectorState

   .. raw:: latex

      \vspace*{-0.35\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> vector = VectorState(spec=[(1, [0]), (1, [1])], norm=1)
      >>> vector.print()
      |ψ⟩ = sqrt(2)/2|0⟩ + sqrt(2)/2|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.states.MatrixState

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_pure = MatrixState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     kind="pure",
      ...     norm=1,
      ... )
      >>> matrix_pure.print()
      |ψ⟩⟨ψ| = 1/2|0⟩⟨0| + 1/2|0⟩⟨1| + 1/2|1⟩⟨0| + 1/2|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_mixed = MatrixState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     kind="mixed",
      ...     norm=1,
      ... )
      >>> matrix_mixed.print()
      ρ = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.states.PureState

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> pure_vector = PureState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     form="vector",
      ...     norm=1,
      ... )
      >>> pure_vector.print()
      |ψ⟩ = sqrt(2)/2|0⟩ + sqrt(2)/2|1⟩

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> pure_matrix = PureState(
      ...     spec=[(1, [0]), (1, [1])],
      ...     form="matrix",
      ...     norm=1,
      ... )
      >>> pure_matrix.print()
      |ψ⟩⟨ψ| = 1/2|0⟩⟨0| + 1/2|0⟩⟨1| + 1/2|1⟩⟨0| + 1/2|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autoclass:: qhronology.quantum.states.MixedState

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> mixed = MixedState(spec=[(1, [0]), (1, [1])], norm=1)
      >>> mixed.print()
      ρ = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}