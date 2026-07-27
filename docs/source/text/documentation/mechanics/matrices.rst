.. include:: /styles.rst

.. _`sec:docs_matrices`:

Matrices
========

This module provides core functions for constructing matrices in quantum mechanics:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.mechanics.matrices import vector_basis, ket, bra, quantum_object, encode, decode, decode_fast, decode_multiple

.. raw:: latex

   \end{code}

Functions
---------

.. .. automodule:: qhronology.mechanics.matrices
..    :members: vector_basis, ket, bra, quantum_object, encode, decode, decode, decode_fast, decode_multiple
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

.. raw:: latex

   \enlargethispage{-\baselineskip}

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

.. raw:: latex

   \enlargethispage{\baselineskip}

.. autofunction:: qhronology.mechanics.matrices.quantum_object

   .. raw:: latex

      \enlargethispage{\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_object(
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

      >>> quantum_object(
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

      >>> quantum_object(
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

      >>> quantum_object(
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

      >>> quantum_object(
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

      >>> quantum_object(
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
      >>> quantum_object(
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

      \begin{code}

   .. code:: python

      >>> quantum_object(
      ...     spec=[(1/sp.sqrt(2), [0]), (1/sp.sqrt(2), [1])],
      ...     form="vector",
      ...     kind="pure",
      ...     dim=2,
      ...     numerical=True,
      ...     array=True,
      ... )
      array([[0.70710678+0.j],
             [0.70710678+0.j]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> quantum_object(
      ...     spec=[
      ...         (sp.Rational(1, 3), [0]),
      ...         (sp.Rational(1, 3), [1]),
      ...         (sp.Rational(1, 3), [2]),
      ...     ],
      ...     form="matrix",
      ...     kind="mixed",
      ...     dim=3,
      ...     numerical=True,
      ...     array=True,
      ... )
      array([[0.33333333+0.j, 0.        +0.j, 0.        +0.j],
             [0.        +0.j, 0.33333333+0.j, 0.        +0.j],
             [0.        +0.j, 0.        +0.j, 0.33333333+0.j]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.matrices.encode

   .. raw:: latex

      \enlargethispage{2\baselineskip}

   .. raw:: latex

      \vspace*{-0.35\baselineskip}

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

      >>> encode(264, num_systems=3, dim=10, return_type=list)
      [2, 6, 4]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> encode(115, num_systems=8, return_type=tuple)
      (0, 1, 1, 1, 0, 0, 1, 1)

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> encode(115, num_systems=8, return_type=str, reverse=True)
      '11001110'

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{\baselineskip}

.. autofunction:: qhronology.mechanics.matrices.decode

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> decode(encode(64))
      64

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
      >>> decode(matrix)
      4

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> decode([1, 0, 1, 0, 1])
      21

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> decode('1110011')
      115

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{-\baselineskip}

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

.. raw:: latex

   \enlargethispage{\baselineskip}

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