.. include:: /styles.rst

.. _`sec:docs_matrices`:

Matrices
========

This module provides core functions for constructing matrices in quantum mechanics:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.mechanics.matrices import vector_basis, ket, bra, quantum_state, encode, decode_slow, decode, decode_fast, decode_multiple

.. raw:: latex

   \end{code}

Functions
---------

.. .. automodule:: qhronology.mechanics.matrices
..    :members: vector_basis, ket, bra, quantum_state, encode, decode_slow, decode, decode_fast, decode_multiple
..    :member-order: bysource

.. autofunction:: qhronology.mechanics.matrices.vector_basis

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> vector_basis(2)
      [Matrix([
       [1],
       [0]]),
       Matrix([
       [0],
       [1]])]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> vector_basis(3)
      [Matrix([
       [1],
       [0],
       [0]]),
       Matrix([
       [0],
       [1],
       [0]]),
       Matrix([
       [0],
       [0],
       [1]])]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.ket

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> ket(0)
      Matrix([
      [1],
      [0]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> ket(1)
      Matrix([
      [0],
      [1]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> ket([2, 1], dim=3)
      Matrix([
      [0],
      [0],
      [0],
      [0],
      [0],
      [0],
      [0],
      [1],
      [0]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.bra

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> bra(0)
      Matrix([[1, 0]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> bra(1)
      Matrix([[0, 1]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> bra([0, 2], dim=3)
      Matrix([[0, 0, 1, 0, 0, 0, 0, 0, 0]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.quantum_state

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_state(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="vector",
      ...     kind="pure",
      ...     dim=2,
      ... )
      Matrix([
      [a],
      [b]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_state(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="matrix",
      ...     kind="pure",
      ...     dim=2,
      ... )
      Matrix([
      [a*conjugate(a), a*conjugate(b)],
      [b*conjugate(a), b*conjugate(b)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_state(
      ...     spec=[("a", [0]), ("b", [1])],
      ...     form="matrix",
      ...     kind="mixed",
      ...     dim=2,
      ... )
      Matrix([
      [a, 0],
      [0, b]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_state(
      ...     spec=[("a", [0]), ("b", [1]), ("c", [2])],
      ...     form="vector",
      ...     kind="pure",
      ...     dim=3,
      ... )
      Matrix([
      [a],
      [b],
      [c]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_state(
      ...     spec=[("a", [0, 0]), ("b", [1, 1])],
      ...     form="vector",
      ...     kind="pure",
      ...     dim=2,
      ... )
      Matrix([
      [a],
      [0],
      [0],
      [b]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_state(
      ...     spec=[["a", "b"], ["c", "d"]],
      ...     form="matrix",
      ...     kind="mixed",
      ...     dim=2,
      ... )
      Matrix([
      [a, b],
      [c, d]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
      >>> quantum_state(
      ...     spec=matrix,
      ...     form="matrix",
      ...     kind="mixed",
      ...     dim=2,
      ... )
      Matrix([
      [a, b],
      [c, d]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.encode

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> encode(3, num_systems=2)
      Matrix([
      [0],
      [0],
      [0],
      [1]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> encode(7, num_systems=2, dim=3)
      Matrix([
      [0],
      [0],
      [0],
      [0],
      [0],
      [0],
      [0],
      [1],
      [0]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> encode(264, num_systems=3, dim=10, output_list=True)
      [2, 6, 4]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> encode(115, num_systems=8, output_list=True)
      [0, 1, 1, 1, 0, 0, 1, 1]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> encode(115, num_systems=8, output_list=True, reverse=True)
      [1, 1, 0, 0, 1, 1, 1, 0]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.decode_slow

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> decode_slow(encode(64))
      64

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
      >>> decode_slow(matrix)
      4

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.decode

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.decode_fast

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> decode_fast(encode(2048))
      2048

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([0, 0, 1, 0, 0, 0, 0])
      >>> decode_fast(matrix, dim=3)
      2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.decode_multiple

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> a, b = sp.symbols("a, b")
      >>> matrix = a * encode(0) + b * encode(1)
      >>> decode_multiple(matrix)
      [(0, a*conjugate(a)), (1, b*conjugate(b))]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix(["x", 0, 0, "y"])
      >>> decode_multiple(matrix)
      [(0, x*conjugate(x)), (3, y*conjugate(y))]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}