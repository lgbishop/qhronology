# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
Functions and a mixin for performing quantum operations.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

from typing import Any, Callable

import numpy as np
import sympy as sp
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import (
    mat,
    arr,
    num,
    sym,
    Forms,
    matrix_form,
)
from qhronology.utilities.helpers import (
    flatten_list,
    count_systems,
    extract_matrix,
    extract_symbols,
    symbolize_expression,
    symbolize_tuples,
    extract_conditions,
    recursively_simplify,
    to_density,
    to_column,
)


def densify(vector: mat | QuantumObject) -> mat:
    """Convert :python:`vector` to its corresponding matrix form via the outer product.
    If :python:`vector` is a square matrix, it is unmodified.

    Arguments
    ---------
    vector : mat
        The input vector.

    Returns
    -------
    mat
        The outer product of :python:`vector` with itself.
    """
    vector = extract_matrix(vector)
    return to_density(vector)


def columnify(vector: mat | QuantumObject) -> mat:
    """Convert :python:`vector` to its corresponding column vector form via transposition.
    If :python:`vector` is a square matrix, it is unmodified.

    Arguments
    ---------
    vector : mat
        The input vector.

    Returns
    -------
    mat
        The column form of :python:`vector`.
    """
    vector = extract_matrix(vector)
    return to_column(vector)


def dagger(matrix: mat | QuantumObject) -> mat:
    """Perform conjugate transposition on :python:`matrix`.

    Arguments
    ---------
    matrix : mat
        The input matrix.

    Returns
    -------
    mat
        The conjugate transpose of :python:`matrix`.
    """
    matrix = extract_matrix(matrix)
    return sp.Matrix(Dagger(matrix))


def simplify(matrix: mat | QuantumObject, comprehensive: bool | None = None) -> mat:
    """Simplify :python:`matrix` using a powerful (albeit slow) algorithm.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be simplified.
    comprehensive : bool
        Whether the simplifying algorithm should use a relatively efficient subset of
        simplifying operations (:python:`False`),
        or alternatively use a larger, more powerful (but slower) set (:python:`True`).
        Defaults to :python:`False`.

    Returns
    -------
    mat
        The simplified version of :python:`matrix`.

    Note
    ----
    If :python:`comprehensive` is :python:`True`, the simplification algorithm will likely take *far*
    longer to execute than if :python:`comprehensive` were :python:`False`.
    """
    conditions = extract_conditions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_matrix(matrix)

    matrix = symbolize_expression(matrix, symbols)
    conditions = symbolize_tuples(conditions, symbols)

    matrix = recursively_simplify(matrix, conditions, comprehensive=comprehensive)

    return matrix


def apply(
    matrix: mat | QuantumObject,
    function: Callable,
    arguments: dict[str, Any] | None = None,
) -> mat:
    """Apply a Python function (:python:`function`) to :python:`matrix`.

    Useful when used with SymPy's symbolic-manipulation functions, such as:

    - :python:`apart()`
    - :python:`cancel()`
    - :python:`collect()`
    - :python:`expand()`
    - :python:`factor()`
    - :python:`simplify()`

    More can be found at:

    - `SymPy documentation: Simplification <https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html>`_
    - `SymPy documentation: Simplify <https://docs.sympy.org/latest/modules/simplify/simplify.html>`_

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be transformed.
    function : Callable
        A Python function.
        Its first non-keyword argument must be able to take a mathematical expression or
        a matrix/array of such types.
    arguments : dict[str, str]
        A dictionary of keyword arguments (both keys and values as strings) to pass to
        the :python:`function` call.
        Defaults to :python:`{}`.

    Returns
    -------
    mat
        The transformed version of :python:`matrix`.
    """
    arguments = {} if arguments is None else arguments
    symbols = extract_symbols(matrix)
    matrix = extract_matrix(matrix)

    matrix = symbolize_expression(matrix, symbols)

    try:
        for index, entry in enumerate(matrix):
            matrix[index] = function(entry, **arguments)
    except:
        try:
            matrix = function(matrix, **arguments)
        except:
            raise ValueError(
                f"Unable to apply the specified function (:python:`{function.__name__}()`) to the matrix."
            )

    return matrix


def rewrite(matrix: mat | QuantumObject, function: Callable) -> mat:
    """Rewrite the elements of :python:`matrix` using the given mathematical function (:python:`function`).

    Useful when used with SymPy's mathematical functions, such as:

    - :python:`exp()`
    - :python:`log()`
    - :python:`sin()`
    - :python:`cos()`

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be transformed.
    function : Callable
        A SymPy mathematical function.

    Returns
    -------
    mat
        The transformed version of :python:`matrix`.
    """
    symbols = extract_symbols(matrix)
    matrix = extract_matrix(matrix)

    matrix = symbolize_expression(matrix, symbols)

    try:
        for index, entry in enumerate(matrix):
            entry = entry.rewrite(function)
            matrix[index] = entry
    except:
        raise ValueError(
            f"""The specified function (:python:`{function.__name__}()`) cannot be used to rewrite
            the matrix."""
        )

    return matrix


def normalize(matrix: mat | QuantumObject, norm: num | sym | str | None = None) -> mat:
    """Normalize :python:`matrix` to the value specified (:python:`norm`).

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be normalized.
    norm : num | sym | str
        The value to which the matrix is normalized.
        Defaults to :python:`1`.

    Returns
    -------
    mat
        The normalized version of :python:`matrix`.
    """
    norm = 1 if norm is None else norm

    is_vector = False
    try:
        is_vector = matrix.is_vector
    except:
        if matrix_form(matrix) == Forms.VECTOR.value:
            is_vector = True

    conditions = extract_conditions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_matrix(matrix)

    matrix = symbolize_expression(matrix, symbols)
    conditions = symbolize_tuples(conditions, symbols)

    trace = sp.trace(densify(matrix))

    norm = symbolize_expression(norm, symbols)
    trace = symbolize_expression(trace, symbols)
    norm = recursively_simplify(norm, conditions)
    trace = recursively_simplify(trace, conditions)

    factor = norm / trace
    factor = recursively_simplify(factor, conditions)

    if is_vector is True:
        factor = sp.sqrt(factor)
    factor = recursively_simplify(factor, conditions)
    matrix = factor * matrix

    return matrix


def coefficient(
    matrix: mat | QuantumObject, scalar: num | sym | str | None = None
) -> mat:
    """Multiply :python:`matrix` by a scalar value (:python:`scalar`).

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be scaled.
    scalar : num | sym | str
        The value by which the state is multiplied.
        Defaults to :python:`1`.

    Returns
    -------
    mat
        The scaled version of :python:`matrix`.
    """
    scalar = 1 if scalar is None else scalar

    conditions = extract_conditions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_matrix(matrix)

    matrix = symbolize_expression(matrix, symbols)
    conditions = symbolize_tuples(conditions, symbols)

    scalar = symbolize_expression(scalar, symbols)

    matrix = scalar * matrix

    return matrix


def partial_trace(
    matrix: mat | QuantumObject,
    targets: int | list[int] | None = None,
    discard: bool | None = None,
    dim: int | None = None,
    optimize: bool | None = None,
) -> num | sym | mat:
    """Compute and return the partial trace of a matrix.

    Arguments
    ---------
    matrix : mat
        The matrix on which to perform the partial trace operation.
    targets : int | list[int]
        The numerical index/indices of the subsystem(s) to be partially traced over.
        Defaults to :python:`[]`.
    discard : bool
        Whether the systems corresponding to the indices given in :python:`targets` are to be
        discarded (:python:`True`) or kept (:python:`False`).
        Defaults to :python:`True`.
    dim : int
        The dimensionality of the matrix.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    optimize : bool
        Whether to optimize the implementation's algorithm.
        Can greatly increase the computational efficiency at the cost of a larger memory footprint
        during computation.
        Defaults to :python:`True`.

    Returns
    -------
    mat
        The reduced matrix.
    """
    targets = [] if targets is None else targets
    discard = True if discard is None else discard
    dim = 2 if dim is None else dim
    optimize = True if optimize is None else optimize

    matrix = extract_matrix(matrix)
    targets = flatten_list(list([targets]))
    if len(targets) == 0 and discard is True:
        return matrix
    matrix = densify(matrix)
    # Convert integer dim into the required list form
    if isinstance(dim, int):
        dim = [dim] * count_systems(matrix, dim)

    dim = np.asarray(dim)
    num_systems = dim.size
    systems = [k for k in range(0, num_systems)]

    matrix = np.asarray(matrix)
    if discard is True:
        keep = [k for k in systems if not k in targets]
    else:
        keep = [k for k in targets]
    num_keep = np.prod(dim[keep]) - 1

    i = [k for k in range(num_systems)]
    j = [num_systems + k if k in keep else k for k in range(num_systems)]
    operator_reduced = matrix.reshape(np.tile(dim, 2))
    operator_reduced = np.einsum(operator_reduced, i + j, optimize=optimize)

    if isinstance(operator_reduced, num):
        return operator_reduced
    else:
        return sp.Matrix(operator_reduced.reshape(num_keep + 1, num_keep + 1))


def measure(
    matrix: mat | QuantumObject,
    operators: list[mat | arr | QuantumObject],
    targets: int | list[int],
    observable: bool | None = None,
    statistics: bool | None = None,
    dim: int | None = None,
) -> mat | list[num | sym]:
    """Perform a quantum measurement on one or more systems (indicated in :python:`targets`)
    of :python:`matrix`.

    This function has two main modes of operation:

    - When :python:`statistics` is :python:`True`,
      the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in :python:`targets`)
      is measured and the set of resulting statistics is returned.
      This takes the form of an ordered list of values :math:`\\{p_i\\}_i` associated with each
      given operator, where:

      - :math:`p_i = \\trace[\\Kraus_i^\\dagger \\Kraus_i \\op{\\rho}]` (measurement probabilities)
        when :python:`observable` is :python:`False`
        (:python:`operators` is a list of Kraus operators or projectors :math:`\\Kraus_i`)
      - :math:`p_i = \\trace[\\Observable_i \\op{\\rho}]` (expectation values)
        when :python:`observable` is :python:`True`
        (:python:`operators` is a list of observables :math:`\\Observable_i`)

    - When :python:`statistics` is :python:`False`,
      the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in :python:`targets`)
      is measured and mutated it according to its predicted post-measurement form
      (i.e., the sum of all possible measurement outcomes).
      This yields the transformed states:

      - When :python:`observable` is :python:`False`:

      .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger.

      - When :python:`observable` is :python:`True`:

      .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}] \\Observable_i.

    In the case where :python:`operators` contains only a single item (:math:`\\Kraus`) and the
    current state (:math:`\\ket{\\psi}`) is a vector form, the transformation of the state
    is in accordance with the rule

    .. math::

       \\ket{\\psi^\\prime} = \\frac{\\Kraus \\ket{\\psi}}
           {\\sqrt{\\bra{\\psi} \\Kraus^\\dagger \\Kraus \\ket{\\psi}}}

    when :python:`observable` is :python:`False`. In all other mutation cases, the post-measurement state
    is a matrix, even if the pre-measurement state was a vector.

    The items in the list :python:`operators` can also be vectors (e.g., :math:`\\ket{\\xi_i}`),
    in which case each is converted into its corresponding operator matrix representation
    (e.g., :math:`\\ket{\\xi_i}\\bra{\\xi_i}`) prior to any measurements.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be measured.
    operators: list[mat | arr | QuantumObject]
        The operator(s) with which to perform the measurement.
        These would typically be a (complete) set of Kraus operators forming a POVM,
        a (complete) set of (orthogonal) projectors forming a PVM,
        or a set of observables constituting a complete basis for the relevant state space.
    targets : int | list[int]
        The numerical indices of the subsystem(s) to be measured.
        They must be consecutive, and their number must match the number of systems spanned
        by all given operators.
        Indexing begins at :python:`0`.
        All other systems are discarded (traced over) in the course of performing the measurement.
    observable: bool
        Whether to treat the items in :python:`operators` as observables instead of Kraus operators
        or projectors.
        Defaults to :python:`False`.
    statistics: bool
        Whether to return a list of probabilities (:python:`True`) or transform :python:`matrix` into a
        post-measurement probabilistic sum of all outcomes (:python:`False`).
        Defaults to :python:`False`.
    dim : int
        The dimensionality of :python:`matrix` and the item(s) of :python:`operators`.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    mat
        The post-measurement :python:`matrix`.
        Returned only if :python:`statistics` is :python:`False`.
    num | sym | list[num | sym]
        A list of probabilities corresponding to each operator given in :python:`operators`.
        Returned only if :python:`statistics` is :python:`True`.

    Note
    ----
    This method does not check for validity of supplied POVMs or the completeness of sets of
    observables, nor does it renormalize the post-measurement state.
    """
    observable = False if observable is None else observable
    statistics = False if statistics is None else statistics
    dim = 2 if dim is None else dim
    is_vector = False
    try:
        is_vector = matrix.is_vector
    except:
        if matrix_form(matrix) == Forms.VECTOR.value:
            is_vector = True

    conditions = extract_conditions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_matrix(matrix)

    matrix = symbolize_expression(matrix, symbols)
    conditions = symbolize_tuples(conditions, symbols)

    operators_initial = operators
    operators = flatten_list([operators])
    targets = flatten_list([targets])

    matrix = partial_trace(matrix=matrix, targets=targets, discard=False, dim=dim)
    operator_matrices = []
    for operator in operators:
        operator_matrices.append(extract_matrix(operator))
    if statistics is False:
        matrix_post_measurement = sp.zeros(dim ** len(targets))
        if observable is False:
            if len(operator_matrices) == 1 and is_vector is True:
                matrix_post_measurement = operator_matrices[0] * matrix
                normalization = 1 / sp.sqrt(sp.trace(densify(matrix_post_measurement)))
                normalization = symbolize_expression(normalization, symbols)
                normalization = recursively_simplify(normalization, conditions)
                matrix_post_measurement = normalization * matrix_post_measurement
            else:
                for operator in operator_matrices:
                    matrix_post_measurement += (
                        densify(operator) * densify(matrix) * Dagger(densify(operator))
                    )
        else:
            for operator in operator_matrices:
                probability = sp.trace(densify(operator) * densify(matrix))
                probability = symbolize_expression(probability, symbols)
                probability = recursively_simplify(probability, conditions)
                matrix_post_measurement += probability * densify(operator)
        return matrix_post_measurement
    else:
        if observable is False:
            probabilities = [
                sp.trace(
                    densify(operator) * densify(matrix) * Dagger(densify(operator))
                )
                for operator in operator_matrices
            ]
        else:
            probabilities = [
                sp.trace(densify(operator) * densify(matrix))
                for operator in operator_matrices
            ]
            for n, probability in enumerate(probabilities):
                probability = symbolize_expression(probability, symbols)
                probability = recursively_simplify(probability, conditions)
                probabilities[n] = probability
        if isinstance(operators_initial, list) is False:
            probabilities = probabilities[0]
        return probabilities


def postselect(
    matrix: mat | QuantumObject,
    postselections: list[tuple[mat | arr | QuantumObject, int]],
    dim: int | None = None,
) -> mat | list[num | sym]:
    """Perform postselection on :python:`matrix` against the operator(s) specified in :python:`postselections`.

    The postselections can be given in either vector or matrix form. For the former,
    the transformation of the vector :math:`\\ket{\\Psi}` follows the standard rule

    .. math:: \\ket{\\Psi^\\prime} = \\braket{\\phi}{\\Psi}

    where :math:`\\ket{\\phi}` is the postselection vector.
    In the case of a matrix form :math:`\\op{\\omega}`, the notion of postselection of a
    matrix :math:`\\op{\\rho}` naturally generalizes to

    .. math:: \\op{\\rho}^\\prime = \\trace_{\\{i\\}}[\\op{\\omega} \\op{\\rho}]

    where :math:`\\{i\\}` is the set of indices corresponding to the subsystem(s) upon which
    the postselection is performed.

    If multiple postselections are supplied, :python:`matrix` will be successively postselected in
    the order in which they are given. If a vector :python:`matrix` is postselected against a matrix form,
    it will automatically be transformed into its matrix form via the outer product as necessary.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be measured.
    postselections: list[tuple[mat | arr | QuantumObject, int]]
        A list of 2-tuples of vectors or matrix operators paired with the first (smallest) index
        of their postselection target systems.
    dim : int
        The dimensionality of :python:`matrix` and the item(s) of :python:`postselections`.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    mat
        The postselected form of :python:`matrix`.
    """
    dim = 2 if dim is None else dim

    matrix = extract_matrix(matrix)
    num_systems = count_systems(matrix, dim)
    systems = [k for k in range(num_systems)]

    is_vector = False
    try:
        is_vector = matrix.is_vector
    except:
        if matrix_form(matrix) == Forms.VECTOR.value:
            is_vector = True

    are_vector = [False for n in postselections]
    for n, twotuple in enumerate(postselections):
        try:
            are_vector[n] = twotuple[0].is_vector
        except:
            if matrix_form(twotuple[0]) == Forms.VECTOR.value:
                are_vector[n] = True
    postselection_is_vector = not any(boolean != True for boolean in are_vector)

    matrices = []
    targets = []
    for twotuple in postselections:
        operator = extract_matrix(twotuple[0])
        if matrix_form(operator) == Forms.VECTOR.value:
            operator = columnify(operator)
        matrices.append(operator)
        num_systems = count_systems(operator, dim)
        targets.append(
            [i + min(flatten_list([twotuple[1]])) for i in range(0, num_systems)]
        )

    operators = []
    identity = sp.eye(dim)
    for system in systems:
        if system not in flatten_list(targets):
            operators.append(identity)
        else:
            min_targets = [min(group) for group in targets]
            if system in min_targets:
                operators.append(matrices[min_targets.index(system)])

    if is_vector is True and postselection_is_vector is True:
        operators_combined = TensorProduct(*operators)
        matrix = Dagger(operators_combined) * matrix
    else:
        for i, operator in enumerate(operators):
            operators[i] = densify(operator)
        operators_combined = TensorProduct(*operators)
        matrix = densify(operators_combined) * densify(matrix)
        matrix = partial_trace(matrix=matrix, targets=flatten_list(targets), dim=dim)
    return matrix


class OperationsMixin:
    """A mixin for endowing classes with the ability to have their :python:`matrix` property mutated
    by various quantum operations.

    Note
    ----
    The :py:class:`~qhronology.mechanics.operations.OperationsMixin` mixin is used exclusively by
    the :py:class:`~qhronology.quantum.states.QuantumState` class---please see the corresponding
    section (:ref:`sec:docs_states_operations`) for documentation on its methods.
    """

    def densify(self):
        """Convert the state to its equivalent (density) matrix representation.

        States that are already in density matrix form are unmodified.
        """
        self.matrix = densify(self)

    def dagger(self):
        """Perform conjugate transposition on the state."""
        self.matrix = dagger(self)

    def simplify(self, comprehensive: bool | None = None):
        """Apply a forced simplification to the state using the values of its :python:`symbols` and
        :python:`conditions` properties.

        Useful if intermediate simplification is required during a sequence of mutating operations
        in order to process the state into a more desirable form.

        Arguments
        ---------
        comprehensive : bool
            Whether the simplifying algorithm should use a relatively efficient subset of
            simplifying operations (:python:`False`),
            or alternatively use a larger, more powerful (but slower) set (:python:`True`).
            Defaults to :python:`False`.

        Note
        ----
        If :python:`comprehensive` is :python:`True`, the simplification algorithm will likely take *far*
        longer to execute than if :python:`comprehensive` were :python:`False`.
        """
        self.matrix = simplify(self, comprehensive=comprehensive)

    def apply(self, function: Callable, arguments: dict[str, Any] | None = None):
        """Apply a Python function (:python:`function`) to the state.

        Useful when used with SymPy's symbolic-manipulation functions, such as:

        - :python:`simplify()`
        - :python:`expand()`
        - :python:`factor()`
        - :python:`collect()`
        - :python:`cancel()`
        - :python:`apart()`

        More can be found at:

        - `SymPy documentation: Simplification <https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html>`_
        - `SymPy documentation: Simplify <https://docs.sympy.org/latest/modules/simplify/simplify.html>`_

        Arguments
        ---------
        function : Callable
            A Python function.
            Its first non-keyword argument must be able to take a mathematical expression or
            a matrix/array of such types.
        arguments : dict[str, str]
            A dictionary of keyword arguments (with the keywords as strings) to pass
            to the :python:`function` call.
            Defaults to :python:`{}`.
        """
        self.matrix = apply(self, function=function, arguments=arguments)

    def rewrite(self, function: Callable):
        """Rewrite the elements of the state using the given mathematical function (:python:`function`).

        Useful when used with SymPy's mathematical functions, such as:

        - :python:`exp()`
        - :python:`log()`
        - :python:`sin()`
        - :python:`cos()`

        Arguments
        ---------
        function : Callable
            A SymPy mathematical function.
        """
        self.matrix = rewrite(self, function=function)

    def normalize(self, norm: num | sym | str | None = None):
        """Perform a forced (re)normalization on the state to the value specified (:python:`norm`).

        Useful when applied to a quantum state both before and after mutating operations,
        prior to any simplification (such as renormalization) performed on its processed output
        (obtained via the :python:`state()` method).

        Arguments
        ---------
        norm : num | sym | str
            The value to which the state is normalized.
            Defaults to :python:`1`.
        """
        norm = 1 if norm is None else norm
        self.matrix = normalize(self, norm=norm)

    def coefficient(self, scalar: num | sym | str | None = None):
        """Multiply the state by a scalar value (:python:`scalar`).

        Can be useful to manually (re)normalize states, or introduce a phase factor.

        Arguments
        ---------
        scalar : num | sym | str
            The value by which the state is multiplied.
            Defaults to :python:`1`.
        """
        scalar = 1 if scalar is None else scalar
        self.matrix = coefficient(self, scalar=scalar)

    def partial_trace(
        self,
        targets: int | list[int] | None = None,
        discard: bool | None = None,
        optimize: bool | None = None,
    ):
        """Perform a partial trace operation on the state.

        Arguments
        ---------
        targets : int | list[int]
            The numerical index/indices of the subsystem(s) to be partially traced over.
            Indexing begins at :python:`0`.
            Defaults to :python:`[]`.
        discard : bool
            Whether the systems corresponding to the indices given in :python:`targets` are to be
            discarded (:python:`True`) or kept (:python:`False`).
            Defaults to :python:`True`.
        optimize : bool
            Whether to optimize the partial trace implementation's algorithm.
            Can greatly increase the computational efficiency at the cost of a larger memory
            footprint during computation.
            Defaults to :python:`True`.
        """
        self.matrix = partial_trace(
            matrix=self,
            targets=targets,
            discard=discard,
            dim=self.dim,
            optimize=optimize,
        )

    def measure(
        self,
        operators: list[mat | arr | QuantumObject],
        targets: int | list[int] | None = None,
        observable: bool | None = None,
        statistics: bool | None = None,
    ) -> None | list[num | sym]:
        """Perform a quantum measurement on one or more systems (indicated in :python:`targets`)
        of the state.

        This method has two main modes of operation:

        - When :python:`statistics` is :python:`True`,
          the (reduced) state (:math:`\\op{\\rho}`)
          (residing on the systems indicated in :python:`targets`)
          is measured and the set of resulting statistics is returned.
          This takes the form of an ordered list of values :math:`\\{p_i\\}_i` associated with
          each given operator, where:

          - :math:`p_i = \\trace[\\Kraus_i^\\dagger \\Kraus_i \\op{\\rho}]`
            (measurement probabilities) when :python:`observable` is :python:`False`
            (:python:`operators` is a list of Kraus operators or projectors :math:`\\Kraus_i`)
          - :math:`p_i = \\trace[\\Observable_i \\op{\\rho}]`
            (expectation values) when :python:`observable` is :python:`True`
            (:python:`operators` is a list of observables :math:`\\Observable_i`)

        - When :python:`statistics` is :python:`False`,
          the (reduced) state (:math:`\\op{\\rho}`)
          (residing on the systems indicated in :python:`targets`)
          is measured and mutated it according to its predicted post-measurement form
          (i.e., the sum of all possible measurement outcomes).
          This yields the transformed states:

          - When :python:`observable` is :python:`False`:

          .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger.

          - When :python:`observable` is :python:`True`:

          .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}]\\Observable_i.

        In the case where :python:`operators` contains only a single item (:math:`\\Kraus`) and
        the current state (:math:`\\ket{\\psi}`) is a vector form,
        the transformation of the state is in accordance with the rule

        .. math::

           \\ket{\\psi^\\prime} = \\frac{\\Kraus \\ket{\\psi}}
               {\\sqrt{\\bra{\\psi} \\Kraus^\\dagger \\Kraus \\ket{\\psi}}}

        when :python:`observable` is :python:`False`. In all other mutation cases, the post-measurement state
        is a matrix, even if the pre-measurement state was a vector.

        The items in the list :python:`operators` can also be vectors (e.g., :math:`\\ket{\\xi_i}`),
        in which case each is converted into its corresponding operator matrix representation
        (e.g., :math:`\\ket{\\xi_i}\\bra{\\xi_i}`) prior to any measurements.

        Arguments
        ---------
        operators: list[mat | arr | QuantumObject]
            The operator(s) with which to perform the measurement.
            These would typically be a (complete) set of Kraus operators forming a POVM,
            a (complete) set of (orthogonal) projectors forming a PVM,
            or a set of observables constituting a complete basis for the relevant state space.
        targets : int | list[int]
            The numerical indices of the subsystem(s) to be measured.
            They must be consecutive, and their number must match the number of systems spanned
            by all given operators.
            Indexing begins at :python:`0`.
            All other systems are discarded (traced over) in the course of performing the measurement.
            Defaults to the value of :python:`self.systems`.
        observable: bool
            Whether to treat the items in :python:`operators` as observables instead of Kraus operators
            or projectors.
            Defaults to :python:`False`.
        statistics: bool
            Whether to return a list of probabilities (:python:`True`) or mutate the state into a
            post-measurement probabilistic sum of all outcomes (:python:`False`).
            Defaults to :python:`False`.

        Returns
        -------
        None
            Returned only if :python:`statistics` is :python:`False`.
        num | sym | list[num | sym]
            A list of probabilities corresponding to each operator given in :python:`operators`.
            Returned only if :python:`statistics` is :python:`True`.

        Note
        ----
        This method does not check for validity of supplied POVMs or the completeness of
        sets of observables, nor does it renormalize the post-measurement state.
        """
        targets = self.systems if targets is None else targets
        observable = False if observable is None else observable
        statistics = False if statistics is None else statistics
        if statistics is False:
            self.matrix = measure(
                self,
                operators=operators,
                targets=targets,
                observable=observable,
                statistics=False,
                dim=self.dim,
            )
        else:
            return measure(
                self,
                operators=operators,
                targets=targets,
                observable=observable,
                statistics=True,
                dim=self.dim,
            )

    def postselect(self, postselections: list[tuple[mat | arr | QuantumObject, int]]):
        """Perform postselection on the state against the operators(s)
        specified in :python:`postselections`.

        The postselections can be given in either vector or matrix form.
        For the former, the transformation of the vector state :math:`\\ket{\\Psi}` follows
        the standard rule

        .. math:: \\ket{\\Psi^\\prime} = \\braket{\\phi}{\\Psi}

        where :math:`\\ket{\\phi}` is the postselection vector.
        In the case of a matrix form :math:`\\op{\\omega}`, the notion of postselection of
        a density matrix state :math:`\\op{\\rho}` naturally generalizes to

        .. math:: \\op{\\rho}^\\prime = \\trace_{\\{i\\}}[\\op{\\omega} \\op{\\rho}]

        where :math:`\\{i\\}` is the set of indices corresponding to the subsystem(s) upon which
        the postselection is performed.

        If multiple postselections are supplied, the state will be successively postselected in the
        order in which they are specified. If a vector state is postselected against a matrix form,
        it will automatically be transformed into its matrix form as necessary.

        Arguments
        ---------
        postselections: list[tuple[mat | arr | QuantumObject, int]]
            A list of 2-tuples of vectors or matrix operators paired with the first (smallest) index
            of their postselection target systems.

        Note
        ----
        Any classes given in :python:`postselections` that are derived from the
        :py:class:`~qhronology.utilities.objects.QuantumObject` base class
        (such as :py:class:`~qhronology.quantum.states.QuantumState`
        and :py:class:`~qhronology.quantum.gates.QuantumGate`)
        will have their :python:`symbols` and :python:`conditions` properties merged into the current
        :py:class:`~qhronology.quantum.states.QuantumState` instance.
        """
        # Add the postselection(s) symbols and conditions to the current instance.
        for twotuple in postselections:
            self.conditions += extract_conditions(twotuple[0])
            symbols = extract_symbols(twotuple[0])
            for symbol in symbols.keys():
                if symbol in self.symbols.keys():
                    self.symbols[symbol] |= symbols[symbol]
                else:
                    self.symbols |= {symbol: symbols[symbol]}

        self.matrix = postselect(self, postselections=postselections, dim=self.dim)
