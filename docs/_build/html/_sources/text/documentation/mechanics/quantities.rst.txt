.. include:: /styles.rst

.. _`sec:docs_quantities`:

Quantities
==========

This module provides functions and a mixin for calculating quantum quantities:

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.mechanics.quantities import trace, purity, distance, fidelity, entropy, mutual
   from qhronology.mechanics.quantities import QuantitiesMixin

.. raw:: latex

   \end{code}

Functions
---------

.. .. automodule:: qhronology.mechanics.quantities
..    :members: trace, purity, distance, fidelity, entropy, mutual
..    :member-order: bysource

.. autofunction:: qhronology.mechanics.quantities.trace

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
      >>> trace(matrix)
      a + d

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.MatrixSymbol("U", 3, 3).as_mutable()
      >>> trace(matrix)
      U[0, 0] + U[1, 1] + U[2, 2]

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.quantities.purity

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
      >>> purity(matrix)
      a**2 + 2*b*c + d**2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix(
      ...     [["a*conjugate(a)", "a*conjugate(b)"],
      ...      ["b*conjugate(a)", "b*conjugate(b)"]],
      ... )
      >>> purity(matrix)
      (a*conjugate(a) + b*conjugate(b))**2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{\baselineskip}

.. autofunction:: qhronology.mechanics.quantities.distance

   .. raw:: latex

      \vspace*{-0.35\baselineskip}

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_A = sp.Matrix([["p", 0], [0, "1 - p"]])
      >>> matrix_B = sp.Matrix([["q", 0], [0, "1 - q"]])
      >>> distance(matrix_A, matrix_B)
      sqrt((p - q)*(conjugate(p) - conjugate(q)))

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_A = sp.Matrix([["1/sqrt(2)"], ["1/sqrt(2)"]])
      >>> matrix_B = sp.Matrix([["1/sqrt(2)"], ["-1/sqrt(2)"]])
      >>> distance(matrix_A, matrix_B)
      1

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
      >>> distance(matrix, matrix)
      0

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.quantities.fidelity

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_A = sp.Matrix([["a"], ["b"]])
      >>> matrix_B = sp.Matrix([["c"], ["d"]])
      >>> fidelity(matrix_A, matrix_A)
      (a*conjugate(a) + b*conjugate(b))**2
      >>> fidelity(matrix_B, matrix_B)
      (c*conjugate(c) + d*conjugate(d))**2
      >>> fidelity(matrix_A, matrix_B)
      (a*conjugate(c) + b*conjugate(d))*(c*conjugate(a) + d*conjugate(b))

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_A = sp.Matrix([["p", 0], [0, "1 - p"]])
      >>> matrix_B = sp.Matrix([["q", 0], [0, "1 - q"]])
      >>> fidelity(matrix_A, matrix_B)
      (sqrt(p*q) + sqrt((1 - p)*(1 - q)))**2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_A = sp.Matrix([["1/sqrt(2)"], ["1/sqrt(2)"]])
      >>> matrix_B = sp.Matrix([["1/sqrt(2)"], ["-1/sqrt(2)"]])
      >>> fidelity(matrix_A, matrix_B)
      0

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.quantities.entropy

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], ["b"]])
      >>> entropy(matrix, base='d')
      -(a*conjugate(a) + b*conjugate(b))**2*log(a*conjugate(a) + b*conjugate(b))/(b*log(d)*conjugate(b))

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_A = sp.Matrix([["p", 0], [0, "1 - p"]])
      >>> matrix_B = sp.Matrix([["q", 0], [0, "1 - q"]])
      >>> entropy(matrix_A, base="d")
      (-p*log(p) + (p - 1)*log(1 - p))/log(d)
      >>> entropy(matrix_B, base="d")
      (-q*log(q) + (q - 1)*log(1 - q))/log(d)
      >>> entropy(matrix_A, matrix_B, base="d")
      (p*(log(p) - log(q)) - (p - 1)*(log(1 - p) - log(1 - q)))/log(d)

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix_A = sp.Matrix([["1/sqrt(2)"], ["1/sqrt(2)"]])
      >>> matrix_B = sp.eye(2) / 2
      >>> entropy(matrix_A)
      0
      >>> entropy(matrix_B)
      1
      >>> entropy(matrix_A, matrix_B)
      1
      >>> entropy(matrix_B, matrix_A)
      -1

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.quantities.mutual

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
      >>> mutual(matrix, [0], [1])
      2

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([1, 0, 0, 0, 0, 0, 0, 0, 1]) / sp.sqrt(2)
      >>> mutual(matrix, [0], [1], dim=3)
      2*log(2)/log(3)

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix(["a", 0, 0, "b"])
      >>> mutual(matrix, [0], [1], base="d")
      (-2*b*(a*log(a*conjugate(a))*conjugate(a) + b*log(b*conjugate(b))*conjugate(b))*conjugate(b) + (a*conjugate(a) + b*conjugate(b))**2*log(a*conjugate(a) + b*conjugate(b)))/(b*log(d)*conjugate(b))

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.eye(4) / 4
      >>> mutual(matrix, [0], [1])
      0

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

Mixin
-----

.. raw:: latex

   \enlargethispage{\baselineskip}

.. autoclass:: qhronology.mechanics.quantities.QuantitiesMixin