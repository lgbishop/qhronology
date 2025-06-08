# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
Functions and a mixin for calculating quantum quantities.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

import sympy as sp
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import mat, num, sym
from qhronology.utilities.helpers import (
    count_systems,
    extract_matrix,
    extract_symbols,
    symbolize_expression,
    symbolize_tuples,
    extract_conditions,
    recursively_simplify,
    apply_function,
)

from qhronology.mechanics.operations import densify, partial_trace


def trace(matrix: mat | QuantumObject) -> num | sym:
    """Calculate the (complete) trace :math:`\\trace[\\op{\\rho}]`
    of ``matrix`` (:math:`\\op{\\rho}`).

    Arguments
    ---------
    matrix : mat | QuantumObject
        The input matrix.

    Returns
    -------
    num | sym
        The trace of the input ``matrix``.

    Examples
    --------
    >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
    >>> trace(matrix)
    a + d

    >>> matrix = sp.MatrixSymbol("U", 3, 3).as_mutable()
    >>> trace(matrix)
    U[0, 0] + U[1, 1] + U[2, 2]
    """
    conditions = extract_conditions(matrix)
    symbols = extract_symbols(matrix)
    matrix = densify(extract_matrix(matrix))

    matrix = symbolize_expression(matrix, symbols)
    conditions = symbolize_tuples(conditions, symbols)

    trace = sp.trace(matrix)

    trace = recursively_simplify(trace, conditions)
    return trace


def purity(state: mat | QuantumObject) -> num | sym:
    """Calculate the purity (:math:`\\Purity`) of ``state`` (:math:`\\op{\\rho}`):

    .. math:: \\Purity(\\op{\\rho}) = \\trace[\\op{\\rho}^2].

    Arguments
    ---------
    state : mat | QuantumObject
        The matrix representation of the input state.

    Returns
    -------
    num | sym
        The purity of the input ``state``.

    Examples
    --------
    >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
    >>> purity(matrix)
    a**2 + 2*b*c + d**2

    >>> matrix = sp.Matrix(
    ...     [["a*conjugate(a)", "a*conjugate(b)"], ["b*conjugate(a)", "b*conjugate(b)"]]
    ... )
    >>> purity(matrix)
    (a*conjugate(a) + b*conjugate(b))**2
    """
    conditions = extract_conditions(state)
    symbols = extract_symbols(state)
    matrix = densify(extract_matrix(state))

    matrix = symbolize_expression(matrix, symbols)

    conditions = symbolize_tuples(conditions, symbols)

    purity = sp.trace(matrix**2)

    purity = recursively_simplify(purity, conditions)
    return purity


def distance(state_A: mat | QuantumObject, state_B: mat | QuantumObject) -> num | sym:
    """Calculate the trace distance (:math:`\\TraceDistance`) between two states
    ``state_A`` (:math:`\\op{\\rho}`) and ``state_B`` (:math:`\\op{\\tau}`):

    .. math::

       \\TraceDistance(\\op{\\rho}, \\op{\\tau})
           = \\frac{1}{2}\\trace{\\abs{\\op{\\rho} - \\op{\\tau}}}.

    Arguments
    ---------
    state_A : mat | QuantumObject
        The matrix representation of the first input state.
    state_B : mat | QuantumObject
        The matrix representation of the second input state.

    Returns
    -------
    num | sym
        The trace distance between the inputs ``state_A`` and ``state_B``.

    Examples
    --------
    >>> matrix_A = sp.Matrix([["p", 0], [0, "1 - p"]])
    >>> matrix_B = sp.Matrix([["q", 0], [0, "1 - q"]])
    >>> distance(matrix_A, matrix_B)
    sqrt((p - q)*(conjugate(p) - conjugate(q)))

    >>> matrix_A = sp.Matrix([["1/sqrt(2)"], ["1/sqrt(2)"]])
    >>> matrix_B = sp.Matrix([["1/sqrt(2)"], ["-1/sqrt(2)"]])
    >>> distance(matrix_A, matrix_B)
    1

    >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
    >>> distance(matrix, matrix)
    0
    """
    conditions = extract_conditions(state_A, state_B)
    symbols = extract_symbols(state_A, state_B)
    matrix_A = densify(extract_matrix(state_A))
    matrix_B = densify(extract_matrix(state_B))

    matrix_A = symbolize_expression(matrix_A, symbols)
    matrix_B = symbolize_expression(matrix_B, symbols)

    conditions = symbolize_tuples(conditions, symbols)
    matrix_A = recursively_simplify(matrix_A, conditions)
    matrix_B = recursively_simplify(matrix_B, conditions)

    product = recursively_simplify(
        Dagger(matrix_A - matrix_B) * (matrix_A - matrix_B), conditions
    )
    root = recursively_simplify(sp.sqrt(product), conditions)
    trace = recursively_simplify(sp.trace(root) / 2, conditions)
    distance = trace

    distance = recursively_simplify(trace, conditions)
    return distance


def fidelity(state_A: mat | QuantumObject, state_B: mat | QuantumObject) -> num | sym:
    """Calculate the fidelity (:math:`\\Fidelity`) between two states
    ``state_A`` (:math:`\\op{\\rho}`) and ``state_B`` (:math:`\\op{\\tau}`):

    .. math::

       \\Fidelity(\\op{\\rho}, \\op{\\tau})
           = \\left(\\trace{\\sqrt{\\sqrt{\\op{\\rho}}\\op{\\tau}\\sqrt{\\op{\\rho}}}}\\right)^2.

    Arguments
    ---------
    state_A : mat | QuantumObject
        The matrix representation of the first input state.
    state_B : mat | QuantumObject
        The matrix representation of the second input state.

    Returns
    -------
    num | sym
        The fidelity between the inputs ``state_A`` and ``state_B``.

    Examples
    --------
    >>> matrix_A = sp.Matrix([["a"], ["b"]])
    >>> matrix_B = sp.Matrix([["c"], ["d"]])
    >>> fidelity(matrix_A, matrix_A)
    (a*conjugate(a) + b*conjugate(b))**2
    >>> fidelity(matrix_B, matrix_B)
    (c*conjugate(c) + d*conjugate(d))**2
    >>> fidelity(matrix_A, matrix_B)
    (a*conjugate(c) + b*conjugate(d))*(c*conjugate(a) + d*conjugate(b))

    >>> matrix_A = sp.Matrix([["p", 0], [0, "1 - p"]])
    >>> matrix_B = sp.Matrix([["q", 0], [0, "1 - q"]])
    >>> fidelity(matrix_A, matrix_B)
    (sqrt(p*q) + sqrt((1 - p)*(1 - q)))**2

    >>> matrix_A = sp.Matrix([["1/sqrt(2)"], ["1/sqrt(2)"]])
    >>> matrix_B = sp.Matrix([["1/sqrt(2)"], ["-1/sqrt(2)"]])
    >>> fidelity(matrix_A, matrix_B)
    0
    """
    conditions = extract_conditions(state_A, state_B)
    symbols = extract_symbols(state_A, state_B)
    matrix_A = densify(extract_matrix(state_A))
    matrix_B = densify(extract_matrix(state_B))

    matrix_A = symbolize_expression(matrix_A, symbols)
    matrix_B = symbolize_expression(matrix_B, symbols)

    conditions = symbolize_tuples(conditions, symbols)

    matrix_A = recursively_simplify(matrix_A, conditions)
    matrix_B = recursively_simplify(matrix_B, conditions)

    product = recursively_simplify(matrix_A * matrix_B, conditions)
    root = recursively_simplify(sp.sqrt(product), conditions)
    trace = recursively_simplify(sp.trace(root), conditions)
    square = recursively_simplify(trace**2, conditions)
    fidelity = square

    fidelity = recursively_simplify(fidelity, conditions)
    return fidelity


def entropy(
    state_A: mat | QuantumObject,
    state_B: mat | QuantumObject | None = None,
    base: num | None = None,
) -> num | sym:
    """Calculate the relative von Neumann entropy (:math:`\\Entropy`) between two states
    ``state_A`` (:math:`\\op{\\rho}`) and ``state_B`` (:math:`\\op{\\tau}`):

    .. math::

       \\Entropy(\\op{\\rho} \\Vert \\op{\\tau})
           = \\trace\\bigl[\\op{\\rho} (\\log_\\Base\\op{\\rho} - \\log_\\Base\\op{\\tau})\\bigr].

    If ``state_B`` is not specified (i.e., ``None``), calculate the ordinary von Neumann entropy
    of ``state_A`` (:math:`\\op{\\rho}`) instead:

    .. math:: \\Entropy(\\op{\\rho}) = \\trace[\\op{\\rho}\\log_\\Base\\op{\\rho}].

    Here, :math:`\\Base` represents ``base``, which is the dimensionality of the unit
    of information with which the entropy is measured.

    Arguments
    ---------
    state_A : mat | QuantumObject
        The matrix representation of the first input state.
    state_B : mat | QuantumObject
        The matrix representation of the second input state.
    base : num
        The dimensionality of the unit of information with which the entropy is measured.
        Defaults to ``2``.

    Returns
    -------
    num | sym
        The von Neumann entropy of the input ``state_A`` (if ``state_B`` is ``None``) or
        the relative entropy between ``state_A`` and ``state_B`` (if ``state_B`` is not ``None``).

    Examples
    --------
    >>> matrix = sp.Matrix([["a"], ["b"]])
    >>> entropy(matrix, base='d')
    -(a*conjugate(a) + b*conjugate(b))**2*log(a*conjugate(a) + b*conjugate(b))/(b*log(d)*conjugate(b))

    >>> matrix_A = sp.Matrix([["p", 0], [0, "1 - p"]])
    >>> matrix_B = sp.Matrix([["q", 0], [0, "1 - q"]])
    >>> entropy(matrix_A, base="d")
    (-p*log(p) + (p - 1)*log(1 - p))/log(d)
    >>> entropy(matrix_B, base="d")
    (-q*log(q) + (q - 1)*log(1 - q))/log(d)
    >>> entropy(matrix_A, matrix_B, base="d")
    (p*(log(p) - log(q)) - (p - 1)*(log(1 - p) - log(1 - q)))/log(d)

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
    """
    conditions = extract_conditions(state_A)
    symbols = extract_symbols(state_A)
    matrix_A = densify(extract_matrix(state_A))

    base = 2 if base is None else base
    base = symbolize_expression(base, symbols)

    matrix_A = symbolize_expression(matrix_A, symbols)

    conditions = symbolize_tuples(conditions, symbols)
    matrix_A = recursively_simplify(matrix_A, conditions)

    if state_B is not None:
        symbols |= extract_symbols(state_B)
        conditions += symbolize_tuples(extract_conditions(state_B), symbols)
        matrix_B = densify(extract_matrix(state_B))

        matrix_B = symbolize_expression(matrix_B, symbols)

        matrix_A = recursively_simplify(matrix_A, conditions)
        matrix_B = recursively_simplify(matrix_B, conditions)

        # Relative entropy
        entropy = sp.trace(
            matrix_A
            * (
                apply_function(matrix_A, sp.log, arguments=[base])
                - apply_function(matrix_B, sp.log, arguments=[base])
            )
        )
    else:
        # von Neumann entropy.
        entropy = -sp.trace(
            matrix_A * apply_function(matrix_A, sp.log, arguments=[base])
        )

    entropy = recursively_simplify(entropy, conditions)
    return entropy


def mutual(
    state: mat | QuantumObject,
    systems_A: int | list[int] | None = None,
    systems_B: int | list[int] | None = None,
    dim: int | None = None,
) -> num | sym:
    """Calculate the mutual information (:math:`\\MutualInformation`) between two subsystems
    ``systems_A`` (:math:`A`) and ``systems_B`` (:math:`B`) of a composite quantum system
    represented by ``state`` (:math:`\\rho^{A,B}`):

    .. math::

       \\MutualInformation(A : B)
           = \\Entropy(\\op{\\rho}^A) + \\Entropy(\\op{\\rho}^B) - \\Entropy(\\op{\\rho}^{A,B})

    where :math:`\\Entropy(\\op{\\rho})` is the von Neumann entropy of a state :math:`\\op{\\rho}`.

    Arguments
    ---------
    state : mat | QuantumObject
        The matrix representation of the composite input state.
    systems_A : int | list[int]
        The indices of the first subsystem.
        Defaults to ``[0]``.
    systems_B : int | list[int]
        The indices of the second subsystem.
        Defaults to the complement of ``systems_A`` with respect to the entire composition of
        subsystems of ``state``.
    dim : int
        The dimensionality of the composite quantum system (and its subsystems).
        Must be a non-negative integer.
        Defaults to ``2``.

    Returns
    -------
    num | sym
        The mutual information between the subsystems ``systems_A`` and ``systems_B`` of
        the composite input ``state``.

    Examples
    --------
    >>> matrix = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    >>> mutual(matrix, [0], [1])
    2

    >>> matrix = sp.eye(4) / 4
    >>> mutual(matrix, [0], [1])
    0

    """
    systems_A = [0] if systems_A is None else systems_A
    dim = 2 if dim is None else dim

    conditions = extract_conditions(state)
    symbols = extract_symbols(state)
    matrix_AB = densify(extract_matrix(state))

    matrix_AB = symbolize_expression(matrix_AB, symbols)

    conditions = symbolize_tuples(conditions, symbols)
    matrix_AB = recursively_simplify(matrix_AB, conditions)

    num_systems = count_systems(matrix_AB, dim)
    systems_AB = [k for k in range(0, num_systems)]
    matrix_A = partial_trace(
        matrix=matrix_AB, targets=systems_A, discard=True, dim=dim, optimize=True
    )
    systems_B = (
        list(set(systems_AB) ^ set(systems_A)) if systems_B is None else systems_B
    )
    matrix_B = partial_trace(
        matrix=matrix_AB, targets=systems_B, discard=True, dim=dim, optimize=True
    )

    mutual = entropy(matrix_A) + entropy(matrix_B) - entropy(matrix_AB)

    mutual = recursively_simplify(mutual, conditions)
    return mutual


class QuantitiesMixin:
    """A mixin for endowing classes with the ability to calculate various quantum quantities.

    Any inheriting class must possess a matrix representation that can be accessed by either
    an ``output()`` method or a ``matrix`` property.

    Note
    ----
    The :py:class:`~qhronology.mechanics.quantities.QuantitiesMixin` mixin is used exclusively by
    the :py:class:`~qhronology.quantum.states.QuantumState` class---please see the corresponding
    section (:ref:`sec:docs_states_quantities`) for documentation on its methods.
    """

    def trace(self) -> num | sym:
        """Calculate the (complete) trace :math:`\\trace[\\op{\\rho}]`
        of the internal state (:math:`\\op{\\rho}`).

        Returns
        -------
        num | sym
            The trace of the internal state.

        Examples
        --------
        >>> state = QuantumState(
        ...     spec=[("a", [0]), ("b", [1])],
        ...     form="vector",
        ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
        ...     conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
        ...     norm=1,
        ... )
        >>> state.trace()
        1

        >>> state = QuantumState(
        ...     spec=[(1, [0]), (1, [1])],
        ...     kind="mixed",
        ...     symbols={"d": {"real": True}},
        ...     norm="1/d",
        ... )
        >>> state.trace()
        1/d

        """

        return trace(matrix=self)

    def purity(self) -> num | sym:
        """Calculate the purity (:math:`\\Purity`) of the internal state (:math:`\\op{\\rho}`):

        .. math:: \\Purity(\\op{\\rho}) = \\trace[\\op{\\rho}^2].

        Returns
        -------
        num | sym
            The purity of the internal state.

        Examples
        --------
        >>> state = QuantumState(
        ...     spec=[("a", [0]), ("b", [1])],
        ...     form="vector",
        ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
        ...     conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
        ...     norm=1,
        ... )
        >>> state.purity()
        1

        >>> state = QuantumState(spec=[("p", [0]), ("1 - p", [1])], kind="mixed", norm=1)
        >>> state.purity()
        p**2 + (1 - p)**2
        """
        return purity(state=self)

    def distance(self, state: mat | QuantumObject) -> num | sym:
        """Calculate the trace distance (:math:`\\TraceDistance`) between
        the internal state (:math:`\\op{\\rho}`) and the given ``state`` (:math:`\\op{\\tau}`):

        .. math::

           \\TraceDistance(\\op{\\rho}, \\op{\\tau})
               = \\frac{1}{2}\\trace{\\abs{\\op{\\rho} - \\op{\\tau}}}.

        Arguments
        ---------
        state : mat | QuantumObject
            The given state.

        Returns
        -------
        num | sym
            The trace distance between the internal state and ``state``.

        Examples
        --------
        >>> state_A = QuantumState(
        ...     spec=[("a", [0]), ("b", [1])],
        ...     form="vector",
        ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
        ...     conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
        ...     norm=1,
        ... )
        >>> state_B = QuantumState(
        ...     spec=[("c", [0]), ("d", [1])],
        ...     form="vector",
        ...     symbols={"c": {"complex": True}, "d": {"complex": True}},
        ...     conditions=[("c*conjugate(c) + d*conjugate(d)", 1)],
        ...     norm=1,
        ... )
        >>> state_A.distance(state_A)
        0
        >>> state_B.distance(state_B)
        0
        >>> state_A.distance(state_B)
        sqrt((a*conjugate(b) - c*conjugate(d))*(b*conjugate(a) - d*conjugate(c)) + (b*conjugate(b) - d*conjugate(d))**2)/2 + sqrt((a*conjugate(a) - c*conjugate(c))**2 + (a*conjugate(b) - c*conjugate(d))*(b*conjugate(a) - d*conjugate(c)))/2

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

        >>> plus_state = QuantumState(spec=[(1, [0]), (1, [1])], form="vector", norm=1)
        >>> minus_state = QuantumState(spec=[(1, [0]), (-1, [1])], form="vector", norm=1)
        >>> plus_state.distance(minus_state)
        1
        """
        return distance(state_A=self, state_B=state)

    def fidelity(self, state: mat | QuantumObject) -> num | sym:
        """Calculate the fidelity (:math:`\\Fidelity`) between
        the internal state (:math:`\\op{\\rho}`) and the given ``state`` (:math:`\\op{\\tau}`):

        .. math::

           \\Fidelity(\\op{\\rho}, \\op{\\tau})
               = \\left(\\trace{\\sqrt{\\sqrt{\\op{\\rho}}\\op{\\tau}\\sqrt{\\op{\\rho}}}}\\right)^2.

        Arguments
        ---------
        state : mat | QuantumObject
            The given state.

        Returns
        -------
        num | sym
            The fidelity between the internal state and ``state``.

        Examples
        --------
        >>> state_A = QuantumState(
        ...     spec=[("a", [0]), ("b", [1])],
        ...     form="vector",
        ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
        ...     conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
        ...     norm=1,
        ... )
        >>> state_B = QuantumState(
        ...     spec=[("c", [0]), ("d", [1])],
        ...     form="vector",
        ...     symbols={"c": {"complex": True}, "d": {"complex": True}},
        ...     conditions=[("c*conjugate(c) + d*conjugate(d)", 1)],
        ...     norm=1,
        ... )
        >>> state_A.fidelity(state_A)
        1
        >>> state_B.fidelity(state_B)
        1
        >>> state_A.fidelity(state_B)
        (a*conjugate(c) + b*conjugate(d))*(c*conjugate(a) + d*conjugate(b))

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

        >>> plus_state = QuantumState(spec=[(1, [0]), (1, [1])], form="vector", norm=1)
        >>> minus_state = QuantumState(spec=[(1, [0]), (-1, [1])], form="vector", norm=1)
        >>> plus_state.fidelity(minus_state)
        0
        """
        return fidelity(state_A=self, state_B=state)

    def entropy(
        self, state: mat | QuantumObject = None, base: num | None = None
    ) -> num | sym:
        """Calculate the relative von Neumann entropy (:math:`\\Entropy`) between
        the internal state (:math:`\\op{\\rho}`) and the given ``state`` (:math:`\\op{\\tau}`):

        .. math::

           \\Entropy(\\op{\\rho} \\Vert \\op{\\tau})
               = \\trace\\bigl[\\op{\\rho} (\\log_\\Base\\op{\\rho} - \\log_\\Base\\op{\\tau})\\bigr].

        If ``state`` is not specified (i.e., ``None``), calculate the ordinary von Neumann entropy
        of the internal state (:math:`\\op{\\rho}`) instead:

        .. math:: \\Entropy(\\op{\\rho}) = \\trace[\\op{\\rho}\\log_\\Base\\op{\\rho}].

        Here, :math:`\\Base` represents ``base``, which is the dimensionality of the unit
        of information with which the entropy is measured.

        Arguments
        ---------
        state : mat | QuantumObject
            The given state.
        base : num
            The dimensionality of the unit of information with which the entropy is measured.
            Defaults to ``2``.

        Returns
        -------
        num | sym
            The (relative) von Neumann entropy.

        Examples
        --------
        >>> state_A = QuantumState(
        ...     spec=[("a", [0]), ("b", [1])],
        ...     form="vector",
        ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
        ...     conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
        ...     norm=1,
        ... )
        >>> state_B = QuantumState(
        ...     spec=[("c", [0]), ("d", [1])],
        ...     form="vector",
        ...     symbols={"c": {"complex": True}, "d": {"complex": True}},
        ...     conditions=[("c*conjugate(c) + d*conjugate(d)", 1)],
        ...     norm=1,
        ... )
        >>> state_A.entropy()
        0
        >>> state_B.entropy()
        0
        >>> state_A.entropy(state_B)
        0

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
        >>> state_A.entropy(state_B)
        (-(p - 1)*(log(1 - p) - log(1 - q)) + log((p/q)**p))/log(2)
        """
        return entropy(state_A=self, state_B=state, base=base)

    def mutual(
        self, systems_A: int | list[int], systems_B: int | list[int] | None = None
    ) -> num | sym:
        """Calculate the mutual information (:math:`\\MutualInformation`) between two subsystems
        ``systems_A`` (:math:`A`) and ``systems_B`` (:math:`B`)
        of the internal state (:math:`\\rho^{A,B}`):

        .. math::

           \\MutualInformation(A : B)
               = \\Entropy(\\op{\\rho}^A) + \\Entropy(\\op{\\rho}^B) - \\Entropy(\\op{\\rho}^{A,B})

        where :math:`\\Entropy(\\op{\\rho})` is the von Neumann entropy of
        a state :math:`\\op{\\rho}`.

        Arguments
        ---------
        systems_A : int | list[int]
            The indices of the first subsystem.
            Defaults to ``[0]``.
        systems_B : int | list[int]
            The indices of the second subsystem.
            Defaults to the complement of ``systems_A`` with respect to the entire composition
            of subsystems of ``state``.
        dim : int
            The dimensionality of the composite quantum system (and its subsystems).
            Must be a non-negative integer.
            Defaults to ``2``.

        Returns
        -------
        num | sym
            The mutual information between the subsystems ``systems_A`` and ``systems_B``
            of the internal state.

        Examples
        --------
        >>> state_AB = QuantumState(
        ...     spec=[("a", [0, 0]), ("b", [1, 1])],
        ...     form="vector",
        ...     symbols={"a": {"complex": True}, "b": {"complex": True}},
        ...     conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
        ...     norm=1,
        ... )
        >>> state_AB.mutual([0], [1])
        2*(-a*log(a*conjugate(a))*conjugate(a) - b*log(b*conjugate(b))*conjugate(b))/log(2)

        >>> state_AB = QuantumState(
        ...     spec=[("a", [0, 0]), ("b", [1, 1])],
        ...     kind="mixed",
        ...     symbols={"a": {"positive": True}, "b": {"positive": True}},
        ...     conditions=[("a + b", 1)],
        ...     norm=1,
        ... )
        >>> state_AB.mutual([0], [1])
        (-a*log(a) - b*log(b))/log(2)
        """
        return mutual(
            state=self, systems_A=systems_A, systems_B=systems_B, dim=self.dim
        )
