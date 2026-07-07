.. include:: /styles.rst

.. _`sec:docs_operations`:

Operations
==========

This module provides functions and a mixin for performing quantum operations.

.. raw:: latex

   \begin{code}

.. code:: python

   from qhronology.mechanics.operations import densify, columnify, dagger, round, simplify, rewrite, apply, normalize, coefficient, partial_trace, measure, postselect
   from qhronology.mechanics.operations import OperationsMixin

.. raw:: latex

   \end{code}

Functions
---------

.. .. automodule:: qhronology.mechanics.operations
..    :members: densify, columnify, dagger, round, simplify, apply, rewrite, normalize, coefficient, partial_trace, measure, postselect
..    :member-order: bysource

.. autofunction:: qhronology.mechanics.operations.densify

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> vector = sp.Matrix([["a"], ["b"]])
      >>> densify(vector)
      Matrix([
      [a*conjugate(a), a*conjugate(b)],
      [b*conjugate(a), b*conjugate(b)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.columnify

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> vector = sp.Matrix([["a", "b"]])
      >>> columnify(vector)
      Matrix([
      [a],
      [b]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.dagger

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], ["b"]])
      >>> dagger(matrix)
      Matrix([[conjugate(a), conjugate(b)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
      >>> dagger(matrix)
      Matrix([
      [conjugate(a), conjugate(c)],
      [conjugate(b), conjugate(d)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.round

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([[sp.I, 1/sp.sqrt(2)], [sp.exp(sp.Rational(1,2)), sp.pi]])
      >>> round(matrix)
      Matrix([
      [0, 1],
      [2, 3]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = np.eye(2) + sp.I*np.fliplr(np.eye(2))
      >>> round(matrix)
      array([[1, 0],
             [0, 1]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick


.. autofunction:: qhronology.mechanics.operations.simplify

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
      >>> simplify(matrix)
      Matrix([
      [a, b],
      [c, d]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix(["2*cos(pi*x/2)**2"])
      >>> simplify(matrix, comprehensive=False)
      Matrix([[2*cos(pi*x/2)**2]])
      >>> simplify(matrix, comprehensive=True)
      Matrix([[cos(pi*x) + 1]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.rewrite

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["cos(x)"], ["sin(x)"]])
      >>> rewrite(matrix, function=sp.exp)
      Matrix([
      [   exp(I*x)/2 + exp(-I*x)/2],
      [-I*(exp(I*x) - exp(-I*x))/2]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.apply

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([
      ...     ["""(x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)
      ...         /(x**2 - 1)"""],
      ... ])
      >>> apply(matrix, function=sp.cancel)
      Matrix([[(y**2 - 2*y*z + z**2)/(x - 1)]])
      >>> apply(matrix, function=sp.collect, arguments={"syms": "x"})
      Matrix([[(x*(y**2 - 2*y*z + z**2) + y**2 - 2*y*z + z**2)/(x**2 - 1)]])
      >>> apply(matrix, function=sp.collect, arguments={"syms": "y"})
      Matrix([[(x*z**2 + y**2*(x + 1) + y*(-2*x*z - 2*z) + z**2)/(x**2 - 1)]])
      >>> apply(matrix, function=sp.collect, arguments={"syms": "z"})
      Matrix([[(x*y**2 + y**2 + z**2*(x + 1) + z*(-2*x*y - 2*y))/(x**2 - 1)]])
      >>> apply(matrix, function=sp.expand)
      Matrix([[x*y**2/(x**2 - 1) - 2*x*y*z/(x**2 - 1) + x*z**2/(x**2 - 1) + y**2/(x**2 - 1) - 2*y*z/(x**2 - 1) + z**2/(x**2 - 1)]])
      >>> apply(matrix, function=sp.factor)
      Matrix([[(y - z)**2/(x - 1)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.normalize

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], ["b"]])
      >>> normalize(matrix, norm=1)
      Matrix([
      [a/sqrt(a*conjugate(a) + b*conjugate(b))],
      [b/sqrt(a*conjugate(a) + b*conjugate(b))]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
      >>> normalize(matrix, norm="n")
      Matrix([
      [a*n/(a + d), b*n/(a + d)],
      [c*n/(a + d), d*n/(a + d)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.coefficient

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([[1], [1]])
      >>> coefficient(matrix, scalar=1 / sp.sqrt(2))
      Matrix([
      [sqrt(2)/2],
      [sqrt(2)/2]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], ["b"]])
      >>> coefficient(matrix, scalar="exp(I*x)")
      Matrix([
      [a*exp(I*x)],
      [b*exp(I*x)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.partial_trace

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], ["b"], ["c"], ["d"]])
      >>> partial_trace(matrix, targets=[0], dim=2)
      Matrix([
      [a*conjugate(a) + c*conjugate(c), a*conjugate(b) + c*conjugate(d)],
      [b*conjugate(a) + d*conjugate(c), b*conjugate(b) + d*conjugate(d)]])
      >>> partial_trace(matrix, targets=[1], dim=2)
      Matrix([
      [a*conjugate(a) + b*conjugate(b), a*conjugate(c) + b*conjugate(d)],
      [c*conjugate(a) + d*conjugate(b), c*conjugate(c) + d*conjugate(d)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \newpage

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([
      ...     ["a", 0, 0, 0],
      ...     [0, "b", 0, 0],
      ...     [0, 0, "c", 0],
      ...     [0, 0, 0, "d"],
      ... ])
      >>> partial_trace(matrix, targets=[0], discard=True, dim=2)
      Matrix([
      [a + c,     0],
      [    0, b + d]])
      >>> partial_trace(matrix, targets=[1], discard=True, dim=2)
      Matrix([
      [a + b,     0],
      [    0, c + d]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. autofunction:: qhronology.mechanics.operations.measure

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], ["b"]])
      >>> plus = sp.Matrix([[1 / sp.sqrt(2)], [1 / sp.sqrt(2)]])
      >>> minus = sp.Matrix([[1 / sp.sqrt(2)], [-1 / sp.sqrt(2)]])
      >>> measure(
      ...     matrix,
      ...     operators=[plus, minus],
      ...     targets=[0],
      ...     observable=False,
      ...     statistics=True,
      ... )
      [a*conjugate(a)/2 + a*conjugate(b)/2 + b*conjugate(a)/2 + b*conjugate(b)/2,
       a*conjugate(a)/2 - a*conjugate(b)/2 - b*conjugate(a)/2 + b*conjugate(b)/2]
      >>> measure(
      ...     matrix,
      ...     operators=[plus, minus],
      ...     targets=[0],
      ...     observable=False,
      ...     statistics=False,
      ... )
      Matrix([
      [a*conjugate(a)/2 + b*conjugate(b)/2, a*conjugate(b)/2 + b*conjugate(a)/2],
      [a*conjugate(b)/2 + b*conjugate(a)/2, a*conjugate(a)/2 + b*conjugate(b)/2]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], ["b"]])
      >>> I = sp.Matrix([[1, 0], [0, 1]])
      >>> X = sp.Matrix([[0, 1], [1, 0]])
      >>> Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
      >>> Z = sp.Matrix([[1, 0], [0, -1]])
      >>> measure(
      ...     matrix,
      ...     operators=[I, X, Y, Z],
      ...     targets=[0],
      ...     observable=True,
      ...     statistics=True,
      ... )
      [a*conjugate(a) + b*conjugate(b),
       a*conjugate(b) + b*conjugate(a),
       I*(a*conjugate(b) - b*conjugate(a)),
       a*conjugate(a) - b*conjugate(b)]
      >>> measure(
      ...     matrix,
      ...     operators=[I, X, Y, Z],
      ...     targets=[0],
      ...     observable=True,
      ...     statistics=False,
      ... )
      Matrix([
      [2*a*conjugate(a), 2*a*conjugate(b)],
      [2*b*conjugate(a), 2*b*conjugate(b)]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

.. raw:: latex

   \enlargethispage{\baselineskip}

.. autofunction:: qhronology.mechanics.operations.postselect

   .. raw:: latex

      \begin{adjustwidth}{0.00cm}{0cm}

   .. rubric:: :styleheader6:`Examples`

   .. raw:: latex

      \begin{code}

   .. code:: python

      >>> matrix = sp.Matrix([["a"], [0], [0], ["b"]])
      >>> zero = sp.Matrix([[1], [0]])
      >>> one = sp.Matrix([[0], [1]])
      >>> postselect(matrix, postselections=[(zero, [0])], dim=2)
      Matrix([
      [a],
      [0]])
      >>> postselect(matrix, postselections=[(one, [0])], dim=2)
      Matrix([
      [0],
      [b]])

   .. raw:: latex

      \end{code}

   .. raw:: latex

      \end{adjustwidth}

.. raw:: latex

   \hrulefillthick

Mixin
-----

.. autoclass:: qhronology.mechanics.operations.OperationsMixin