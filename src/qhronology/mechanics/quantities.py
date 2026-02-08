# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
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
    of :python:`matrix` (:math:`\\op{\\rho}`).

    Arguments
    ---------
    matrix : mat | QuantumObject
        The input matrix.

    Returns
    -------
    num | sym
        The trace of the input :python:`matrix`.
    """
    symbols = extract_symbols(matrix)
    conditions = extract_conditions(matrix)
    conditions = symbolize_tuples(conditions, symbols)

    matrix = densify(extract_matrix(matrix))
    matrix = symbolize_expression(matrix, symbols)

    trace = sp.trace(matrix)
    trace = recursively_simplify(trace, conditions)
    return trace


def purity(state: mat | QuantumObject) -> num | sym:
    """Calculate the purity (:math:`\\Purity`) of :python:`state` (:math:`\\op{\\rho}`):

    .. math:: \\Purity(\\op{\\rho}) = \\trace[\\op{\\rho}^2].

    Arguments
    ---------
    state : mat | QuantumObject
        The matrix representation of the input state.

    Returns
    -------
    num | sym
        The purity of the input :python:`state`.
    """
    symbols = extract_symbols(state)
    conditions = extract_conditions(state)
    conditions = symbolize_tuples(conditions, symbols)

    matrix = densify(extract_matrix(state))
    matrix = symbolize_expression(matrix, symbols)

    purity = sp.trace(matrix**2)
    purity = recursively_simplify(purity, conditions)
    return purity


def distance(state_A: mat | QuantumObject, state_B: mat | QuantumObject) -> num | sym:
    """Calculate the trace distance (:math:`\\TraceDistance`) between two states
    :python:`state_A` (:math:`\\op{\\rho}`) and :python:`state_B` (:math:`\\op{\\tau}`):

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
        The trace distance between the inputs :python:`state_A` and :python:`state_B`.
    """
    symbols = extract_symbols(state_A, state_B)
    conditions = extract_conditions(state_A, state_B)
    conditions = symbolize_tuples(conditions, symbols)

    matrix_A = densify(extract_matrix(state_A))
    matrix_B = densify(extract_matrix(state_B))

    matrix_A = symbolize_expression(matrix_A, symbols)
    matrix_B = symbolize_expression(matrix_B, symbols)

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
    :python:`state_A` (:math:`\\op{\\rho}`) and :python:`state_B` (:math:`\\op{\\tau}`):

    .. math::

       \\Fidelity(\\op{\\rho}, \\op{\\tau})
           = \\left(\\trace{\\sqrt{\\sqrt{\\op{\\rho}}\\,\\op{\\tau}\\sqrt{\\op{\\rho}}}}\\right)^2.

    Arguments
    ---------
    state_A : mat | QuantumObject
        The matrix representation of the first input state.
    state_B : mat | QuantumObject
        The matrix representation of the second input state.

    Returns
    -------
    num | sym
        The fidelity between the inputs :python:`state_A` and :python:`state_B`.
    """
    symbols = extract_symbols(state_A, state_B)
    conditions = extract_conditions(state_A, state_B)
    conditions = symbolize_tuples(conditions, symbols)

    matrix_A = densify(extract_matrix(state_A))
    matrix_B = densify(extract_matrix(state_B))

    matrix_A = symbolize_expression(matrix_A, symbols)
    matrix_B = symbolize_expression(matrix_B, symbols)

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
    base: num | sym | str | None = None,
) -> num | sym:
    """Calculate the relative von Neumann entropy (:math:`\\Entropy`) between two states
    :python:`state_A` (:math:`\\op{\\rho}`) and :python:`state_B` (:math:`\\op{\\tau}`):

    .. math::

       \\Entropy(\\op{\\rho} \\Vert \\op{\\tau})
           = \\trace\\bigl[\\op{\\rho} (\\log_\\Base\\op{\\rho} - \\log_\\Base\\op{\\tau})\\bigr].

    If :python:`state_B` is not specified (i.e., :python:`None`), calculate the ordinary von Neumann entropy
    of :python:`state_A` (:math:`\\op{\\rho}`) instead:

    .. math:: \\Entropy(\\op{\\rho}) = \\trace[\\op{\\rho}\\log_\\Base\\op{\\rho}].

    Here, :math:`\\Base` represents :python:`base`, which is the dimensionality of the unit
    of information with which the entropy is measured.

    Arguments
    ---------
    state_A : mat | QuantumObject
        The matrix representation of the first input state.
    state_B : mat | QuantumObject
        The matrix representation of the second input state.
    base : num | sym | str
        The dimensionality of the unit of information with which the entropy is measured.
        Defaults to :python:`2`.

    Returns
    -------
    num | sym
        The von Neumann entropy of the input :python:`state_A` (if :python:`state_B` is :python:`None`) or
        the relative entropy between :python:`state_A` and :python:`state_B` (if :python:`state_B` is not :python:`None`).
    """
    symbols = extract_symbols(state_A)
    conditions = extract_conditions(state_A)
    conditions = symbolize_tuples(conditions, symbols)

    base = 2 if base is None else base
    base = symbolize_expression(base, symbols)

    matrix_A = densify(extract_matrix(state_A))
    matrix_A = symbolize_expression(matrix_A, symbols)
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
    base: num | sym | str | None = None,
) -> num | sym:
    """Calculate the mutual information (:math:`\\MutualInformation`) between two subsystems
    :python:`systems_A` (:math:`A`) and :python:`systems_B` (:math:`B`) of a composite quantum system
    represented by :python:`state` (:math:`\\rho^{A,B}`):

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
        Defaults to :python:`[0]`.
    systems_B : int | list[int]
        The indices of the second subsystem.
        Defaults to the complement of :python:`systems_A` with respect to the entire composition of
        subsystems of :python:`state`.
    dim : int
        The dimensionality of the composite quantum system (and its subsystems).
        Must be a non-negative integer.
        Defaults to :python:`2`.
    base : num | sym | str
        The dimensionality of the unit of information with which the mutual information is measured.
        Defaults to the value of :python:`dim`.

    Returns
    -------
    num | sym
        The mutual information between the subsystems :python:`systems_A` and :python:`systems_B` of
        the composite input :python:`state`.
    """
    systems_A = [0] if systems_A is None else systems_A
    dim = 2 if dim is None else dim

    symbols = extract_symbols(state)
    conditions = extract_conditions(state)
    conditions = symbolize_tuples(conditions, symbols)

    base = dim if base is None else base
    base = symbolize_expression(base, symbols)

    matrix_AB = densify(extract_matrix(state))
    matrix_AB = symbolize_expression(matrix_AB, symbols)
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

    mutual = (
        entropy(matrix_A, base=base)
        + entropy(matrix_B, base=base)
        - entropy(matrix_AB, base=base)
    )
    mutual = recursively_simplify(mutual, conditions)
    return mutual


class QuantitiesMixin:
    """A mixin for endowing classes with the ability to calculate various quantum quantities.

    Any inheriting class must possess a matrix representation that can be accessed by either
    an :python:`output()` method or a :python:`matrix` property.

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
        """
        return trace(matrix=self)

    def purity(self) -> num | sym:
        """Calculate the purity (:math:`\\Purity`) of the internal state (:math:`\\op{\\rho}`):

        .. math:: \\Purity(\\op{\\rho}) = \\trace[\\op{\\rho}^2].

        Returns
        -------
        num | sym
            The purity of the internal state.
        """
        return purity(state=self)

    def distance(self, state: mat | QuantumObject) -> num | sym:
        """Calculate the trace distance (:math:`\\TraceDistance`) between
        the internal state (:math:`\\op{\\rho}`) and the given :python:`state` (:math:`\\op{\\tau}`):

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
            The trace distance between the internal state and :python:`state`.
        """
        return distance(state_A=self, state_B=state)

    def fidelity(self, state: mat | QuantumObject) -> num | sym:
        """Calculate the fidelity (:math:`\\Fidelity`) between
        the internal state (:math:`\\op{\\rho}`) and the given :python:`state` (:math:`\\op{\\tau}`):

        .. math::

           \\Fidelity(\\op{\\rho}, \\op{\\tau})
               = \\left(\\trace{\\sqrt{\\sqrt{\\op{\\rho}}\\,\\op{\\tau}\\sqrt{\\op{\\rho}}}}\\right)^2.

        Arguments
        ---------
        state : mat | QuantumObject
            The given state.

        Returns
        -------
        num | sym
            The fidelity between the internal state and :python:`state`.
        """
        return fidelity(state_A=self, state_B=state)

    def entropy(
        self, state: mat | QuantumObject = None, base: num | sym | str | None = None
    ) -> num | sym:
        """Calculate the relative von Neumann entropy (:math:`\\Entropy`) between
        the internal state (:math:`\\op{\\rho}`) and the given :python:`state` (:math:`\\op{\\tau}`):

        .. math::

           \\Entropy(\\op{\\rho} \\Vert \\op{\\tau})
               = \\trace\\bigl[\\op{\\rho} (\\log_\\Base\\op{\\rho} - \\log_\\Base\\op{\\tau})\\bigr].

        If :python:`state` is not specified (i.e., :python:`None`), calculate the ordinary von Neumann entropy
        of the internal state (:math:`\\op{\\rho}`) instead:

        .. math:: \\Entropy(\\op{\\rho}) = \\trace[\\op{\\rho}\\log_\\Base\\op{\\rho}].

        Here, :math:`\\Base` represents :python:`base`, which is the dimensionality of the unit
        of information with which the entropy is measured.

        Arguments
        ---------
        state : mat | QuantumObject
            The given state.
        base : num | sym | str
            The dimensionality of the unit of information with which the entropy is measured.
            Defaults to :python:`2`.

        Returns
        -------
        num | sym
            The (relative) von Neumann entropy.
        """
        return entropy(state_A=self, state_B=state, base=base)

    def mutual(
        self,
        systems_A: int | list[int],
        systems_B: int | list[int] | None = None,
        base: num | sym | str | None = None,
    ) -> num | sym:
        """Calculate the mutual information (:math:`\\MutualInformation`) between two subsystems
        :python:`systems_A` (:math:`A`) and :python:`systems_B` (:math:`B`)
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
            Defaults to :python:`[0]`.
        systems_B : int | list[int]
            The indices of the second subsystem.
            Defaults to the complement of :python:`systems_A` with respect to the entire composition
            of the subsystems of :python:`state`.
        base : num | sym | str
            The dimensionality of the unit of information with which the mutual information is measured.
            Defaults to the value of :python:`self.dim`.

        Returns
        -------
        num | sym
            The mutual information between the subsystems :python:`systems_A` and :python:`systems_B`
            of the internal state.
        """
        return mutual(
            state=self,
            systems_A=systems_A,
            systems_B=systems_B,
            dim=self.dim,
            base=base,
        )
