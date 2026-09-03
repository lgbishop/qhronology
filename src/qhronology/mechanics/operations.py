# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
Functions and a mixin for performing quantum operations.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations
from typing import Any, Callable

import numpy as np
import sympy as sp

from qhronology.utilities.classification import Forms, arr, expr, mat, matrix_form, num
from qhronology.utilities.helpers import (
    cast,
    conjugate_transpose,
    count_systems,
    dtype,
    extract_substitutions,
    extract_representation,
    extract_symbols,
    flatten_list,
    generate_identity,
    generate_zeros,
    matrix_multiplication,
    recursively_simplify,
    symbolize_substitutions,
    symbolize_expression,
    tensor_product,
    to_column,
    to_density,
    to_matrix,
    to_numerical,
)


def densify(vector: mat | arr | QuantumObject) -> mat | arr:
    """Convert :python:`vector` to its corresponding matrix form via the outer product.
    If :python:`vector` is a square matrix, it is unmodified.

    Arguments
    ---------
    vector : mat | arr
        The input vector.

    Returns
    -------
    mat | arr
        The outer product of :python:`vector` with itself.
    """
    vector = extract_representation(vector)
    return to_density(vector)


def columnify(vector: mat | arr | QuantumObject) -> mat | arr:
    """Convert :python:`vector` to its corresponding column vector form via transposition.
    If :python:`vector` is a square matrix, it is unmodified.

    Arguments
    ---------
    vector : mat | arr
        The input vector.

    Returns
    -------
    mat | arr
        The column form of :python:`vector`.
    """
    vector = extract_representation(vector)
    return to_column(vector)


def dagger(matrix: mat | arr | QuantumObject) -> mat | arr:
    """Perform conjugate transposition on :python:`matrix`.

    Arguments
    ---------
    matrix : mat | arr
        The input matrix.

    Returns
    -------
    mat | arr
        The conjugate transpose of :python:`matrix`.
    """
    matrix = extract_representation(matrix)
    return conjugate_transpose(matrix)


def round(matrix: mat | arr | QuantumObject) -> mat | arr:
    """Round the elements of :python:`matrix` to the nearest (real) integer.

    Arguments
    ---------
    matrix : mat | arr
        The input matrix.

    Returns
    -------
    mat | arr
        The rounded version of :python:`matrix`.
    """
    matrix = extract_representation(matrix)

    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

    matrix = np.rint(np.real(np.array(matrix, dtype=complex))).astype(int)
    if matrix_arr is False:
        matrix = to_matrix(matrix)

    return matrix


def simplify(
    matrix: mat | arr | QuantumObject, comprehensive: bool | None = None
) -> mat | arr:
    """Simplify :python:`matrix` using a powerful (albeit slow) algorithm.

    Arguments
    ---------
    matrix : mat | arr | QuantumObject
        The matrix to be simplified.
    comprehensive : bool
        Whether the simplifying algorithm should use a relatively efficient subset of simplifying operations (:python:`False`), or alternatively use a larger, more powerful (but slower) set (:python:`True`).
        Defaults to :python:`False`.

    Returns
    -------
    mat | arr
        The simplified version of :python:`matrix`.

    Note
    ----
    If :python:`comprehensive` is :python:`True`, the simplification algorithm will likely take *far* longer to execute than if :python:`comprehensive` were :python:`False`.
    """
    substitutions = extract_substitutions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_representation(matrix)

    matrix = symbolize_expression(matrix, symbols)
    substitutions = symbolize_substitutions(substitutions, symbols)

    matrix = recursively_simplify(matrix, substitutions, comprehensive=comprehensive)

    return matrix


def rewrite(matrix: mat | arr | QuantumObject, function: Callable) -> mat | arr:
    """Rewrite the elements of :python:`matrix` using the given mathematical function (:python:`function`).

    Useful when used with SymPy's mathematical functions, such as:

    - :python:`exp()`
    - :python:`log()`
    - :python:`sin()`
    - :python:`cos()`
    - :python:`sqrt()`

    Arguments
    ---------
    matrix : mat | arr | QuantumObject
        The matrix to be transformed.
    function : Callable
        A SymPy mathematical function.

    Returns
    -------
    mat | arr
        The transformed version of :python:`matrix`.
    """
    symbols = extract_symbols(matrix)
    matrix = extract_representation(matrix)

    matrix = symbolize_expression(matrix, symbols)

    if dtype(matrix) is object:
        matrix_num = True if issubclass(dtype(matrix), num) is True else False
        matrix_arr = True if isinstance(matrix, arr) is True else False
        matrix = to_matrix(matrix)
        try:
            for index, entry in np.ndenumerate(matrix):
                entry = entry.rewrite(function)
                matrix[index] = entry
        except:
            raise ValueError(
                f"""The specified function (`{function.__name__}()`) cannot be used to rewrite the matrix."""
            )
        matrix = cast(matrix, numerical=matrix_num, array=matrix_arr)

    return matrix


def apply(
    matrix: mat | arr | QuantumObject,
    function: Callable,
    arguments: dict[str, Any] | None = None,
) -> mat | arr:
    """Apply a Python function (:python:`function`) element-wise to :python:`matrix`.

    Useful when used with SymPy's symbolic-manipulation functions, such as:

    - :python:`apart()`
    - :python:`cancel()`
    - :python:`collect()`
    - :python:`expand()`
    - :python:`factor()`
    - :python:`simplify()`
    - :python:`separatevars()`
    - :python:`rewrite()` (though the :py:func:`~qhronology.mechanics.operations.rewrite` function should be used instead)

    More can be found at:

    - `SymPy documentation: Simplification <https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html>`_
    - `SymPy documentation: Simplify <https://docs.sympy.org/latest/modules/simplify/simplify.html>`_

    Arguments
    ---------
    matrix : mat | arr | QuantumObject
        The matrix to be transformed.
    function : Callable
        A Python function.
        Its first non-keyword argument must be able to take a mathematical expression or a matrix/array of such types.
    arguments : dict[str, str]
        A dictionary of keyword arguments (both keys and values as strings) to pass to the :python:`function` call.
        Defaults to :python:`{}`.

    Returns
    -------
    mat | arr
        The transformed version of :python:`matrix`.
    """
    arguments = {} if arguments is None else arguments
    symbols = extract_symbols(matrix)
    matrix = extract_representation(matrix)

    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

    matrix = symbolize_expression(matrix, symbols)

    matrix = to_matrix(matrix)
    try:
        for index, entry in np.ndenumerate(matrix):
            matrix[index] = function(entry, **arguments)
    except:
        try:
            for index, entry in np.ndenumerate(matrix):
                matrix[index] = function(
                    to_numerical(entry, numerical=True), **arguments
                )
        except:
            raise ValueError(
                f"""Unable to apply the specified function (`{function.__name__}()`) to the matrix."""
            )
    matrix = cast(matrix, numerical=matrix_num, array=matrix_arr)

    return matrix


def normalize(
    matrix: mat | arr | QuantumObject, norm: num | expr | str | None = None
) -> mat | arr:
    """Normalize :python:`matrix` to the value specified (:python:`norm`).

    Arguments
    ---------
    matrix : mat | arr | QuantumObject
        The matrix to be normalized.
    norm : num | expr | str
        The value to which the matrix is normalized.
        Defaults to :python:`1`.

    Returns
    -------
    mat | arr
        The normalized version of :python:`matrix`.
    """
    norm = 1 if norm is None else norm

    is_vector = False
    try:
        is_vector = matrix.is_vector
    except:
        if matrix_form(matrix) == Forms.VECTOR.value:
            is_vector = True

    substitutions = extract_substitutions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_representation(matrix)

    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

    matrix = symbolize_expression(matrix, symbols)
    substitutions = symbolize_substitutions(substitutions, symbols)

    trace = densify(matrix).trace()

    norm = symbolize_expression(norm, symbols)
    trace = symbolize_expression(trace, symbols)
    norm = recursively_simplify(norm, substitutions)
    trace = recursively_simplify(trace, substitutions)

    factor = norm / trace
    factor = recursively_simplify(factor, substitutions)

    if is_vector is True:
        factor = sp.sqrt(factor)
    factor = recursively_simplify(factor, substitutions)
    matrix = factor * matrix

    matrix = cast(matrix, numerical=matrix_num, array=matrix_arr)

    return matrix


def coefficient(
    matrix: mat | arr | QuantumObject, scalar: num | expr | str | None = None
) -> mat | arr:
    """Multiply :python:`matrix` by a scalar value (:python:`scalar`).

    Arguments
    ---------
    matrix : mat | arr | QuantumObject
        The matrix to be scaled.
    scalar : num | expr | str
        The value by which the state is multiplied.
        Defaults to :python:`1`.

    Returns
    -------
    mat | arr
        The scaled version of :python:`matrix`.
    """
    scalar = 1 if scalar is None else scalar

    substitutions = extract_substitutions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_representation(matrix)

    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

    matrix = symbolize_expression(matrix, symbols)
    substitutions = symbolize_substitutions(substitutions, symbols)

    scalar = symbolize_expression(scalar, symbols)

    matrix = scalar * matrix

    matrix = cast(matrix, numerical=matrix_num, array=matrix_arr)

    return matrix


def partial_trace(
    matrix: mat | arr | QuantumObject,
    targets: list[int] | None = None,
    discard: bool | None = None,
    dim: int | None = None,
    optimize: bool | None = None,
) -> num | expr | mat | arr:
    """Compute and return the partial trace of a matrix.

    Arguments
    ---------
    matrix : mat | arr
        The matrix on which to perform the partial trace operation.
    targets : list[int]
        The numerical indices of the subsystem(s) to be partially traced over.
        Defaults to :python:`[]`.
    discard : bool
        Whether the systems corresponding to the indices given in :python:`targets` are to be discarded (:python:`True`) or kept (:python:`False`).
        Defaults to :python:`True`.
    dim : int
        The dimensionality of the matrix.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    optimize : bool
        Whether to optimize the implementation's algorithm.
        Can greatly increase the computational efficiency at the cost of a larger memory footprint during computation.
        Defaults to :python:`True`.

    Returns
    -------
    num | expr | mat | arr
        The reduced matrix or scalar trace expression.
    """
    targets = [] if targets is None else targets
    discard = True if discard is None else discard
    dim = 2 if dim is None else dim
    optimize = True if optimize is None else optimize

    matrix = extract_representation(matrix)

    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

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
        return cast(
            operator_reduced.reshape(num_keep + 1, num_keep + 1),
            numerical=matrix_num,
            array=matrix_arr,
        )


def measure(
    matrix: mat | arr | QuantumObject,
    operators: list[mat | arr | QuantumObject],
    targets: list[int],
    observable: bool | None = None,
    statistics: bool | None = None,
    dim: int | None = None,
) -> mat | arr | list[num | expr]:
    """Perform a quantum measurement on one or more systems (indicated in :python:`targets`) of :python:`matrix`.

    This function has two main modes of operation:

    - When :python:`statistics` is :python:`True`, the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in :python:`targets`) is measured, and the set of resulting statistics is returned.
      This takes the form of an ordered list of values :math:`\\{p_i\\}_i` associated with each given operator, where:

      - :math:`p_i = \\trace[\\Kraus_i^\\dagger \\Kraus_i \\op{\\rho}]` (measurement probabilities)
        when :python:`observable` is :python:`False`
        :inlinelatex:`\\newline` (:python:`operators` is a list of Kraus operators or projectors :math:`\\Kraus_i`)
      - :math:`p_i = \\trace[\\Observable_i \\op{\\rho}]` (expectation values)
        when :python:`observable` is :python:`True`
        :inlinelatex:`\\newline` (:python:`operators` is a list of observables :math:`\\Observable_i`)

    - When :python:`statistics` is :python:`False`, the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in :python:`targets`) is measured and mutated according to its predicted post-measurement form (i.e., the sum of all possible measurement outcomes).
      This yields the transformed states:

      - When :python:`observable` is :python:`False`:

      .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger

      - When :python:`observable` is :python:`True`:

      .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}] \\Observable_i

    In the case where :python:`operators` contains only a single item (:math:`\\Kraus`) and the current state (:math:`\\ket{\\psi}`) is a vector form, the transformation of the state is in accordance with the rule

    .. math::

       \\ket{\\psi^\\prime} = \\frac{\\Kraus \\ket{\\psi}}
           {\\sqrt{\\bra{\\psi} \\Kraus^\\dagger \\Kraus \\ket{\\psi}}}

    when :python:`observable` is :python:`False`. In all other mutation cases, the post-measurement state is a matrix, even if the pre-measurement state was a vector.

    The items in the list :python:`operators` can also be vectors (e.g., :math:`\\ket{\\xi_i}`), in which case each is converted into its corresponding operator matrix representation (e.g., :math:`\\ket{\\xi_i}\\bra{\\xi_i}`) prior to any measurements.

    Arguments
    ---------
    matrix : mat | arr | QuantumObject
        The matrix to be measured.
    operators: list[mat | arr | QuantumObject]
        The operator(s) with which to perform the measurement.
        These would typically be a (complete) set of Kraus operators forming a POVM,
        a (complete) set of (orthogonal) projectors forming a PVM,
        or a set of observables constituting a complete basis for the relevant state space.
    targets : list[int]
        The numerical indices of the subsystem(s) to be measured.
        They must be contiguous, and their number must match the number of systems spanned by all given operators.
        Indexing begins at :python:`0`.
        All other systems are discarded (traced over) in the course of performing the measurement.
    observable: bool
        Whether to treat the items in :python:`operators` as observables instead of Kraus operators or projectors.
        Defaults to :python:`False`.
    statistics: bool
        Whether to return a list of probabilities (:python:`True`) or transform :python:`matrix` into a post-measurement probabilistic sum of all outcomes (:python:`False`).
        Defaults to :python:`False`.
    dim : int
        The dimensionality of :python:`matrix` and the item(s) of :python:`operators`.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    mat | arr
        The post-measurement :python:`matrix`.
        Returned if :python:`statistics` is :python:`False`.
    num | expr | list[num | expr]
        A list of probabilities corresponding to each operator given in :python:`operators`.
        Returned if :python:`statistics` is :python:`True`.

    Note
    ----
    This method does not verify the validity of supplied POVMs or the completeness of sets of observables, nor does it renormalize the post-measurement state.
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

    substitutions = extract_substitutions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_representation(matrix)

    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

    matrix = symbolize_expression(matrix, symbols)
    substitutions = symbolize_substitutions(substitutions, symbols)

    operators_initial = operators
    operators = flatten_list([operators])
    targets = flatten_list([targets])

    matrix = partial_trace(matrix=matrix, targets=targets, discard=False, dim=dim)
    operator_matrices = []
    for operator in operators:
        operator_matrices.append(
            cast(
                extract_representation(operator), numerical=matrix_num, array=matrix_arr
            )
        )
    if statistics is False:
        matrix_post_measurement = generate_zeros(
            dim ** len(targets), numerical=matrix_num, array=matrix_arr
        )
        if observable is False:
            if len(operator_matrices) == 1 and is_vector is True:
                matrix_post_measurement = matrix_multiplication(
                    operator_matrices[0], matrix
                )
                normalization = 1 / sp.sqrt(densify(matrix_post_measurement).trace())
                normalization = symbolize_expression(normalization, symbols)
                normalization = recursively_simplify(normalization, substitutions)
                matrix_post_measurement = normalization * matrix_post_measurement
            else:
                for operator in operator_matrices:
                    matrix_post_measurement = (
                        matrix_post_measurement
                        + matrix_multiplication(
                            densify(operator),
                            densify(matrix),
                            conjugate_transpose(densify(operator)),
                        )
                    )
        else:
            for operator in operator_matrices:
                probability = matrix_multiplication(
                    densify(operator), densify(matrix)
                ).trace()
                probability = symbolize_expression(probability, symbols)
                probability = recursively_simplify(probability, substitutions)
                matrix_post_measurement = (
                    matrix_post_measurement + probability * densify(operator)
                )
        return cast(matrix_post_measurement, numerical=matrix_num, array=matrix_arr)
    else:
        if observable is False:
            probabilities = [
                matrix_multiplication(
                    densify(operator),
                    densify(matrix),
                    conjugate_transpose(densify(operator)),
                ).trace()
                for operator in operator_matrices
            ]
        else:
            probabilities = [
                matrix_multiplication(densify(operator), densify(matrix)).trace()
                for operator in operator_matrices
            ]
            for n, probability in enumerate(probabilities):
                probability = symbolize_expression(probability, symbols)
                probability = recursively_simplify(probability, substitutions)
                probabilities[n] = probability
        if isinstance(operators_initial, list) is False:
            probabilities = probabilities[0]
        return probabilities


def postselect(
    matrix: mat | arr | QuantumObject,
    postselections: list[tuple[mat | arr | QuantumObject, list[int]]],
    dim: int | None = None,
) -> mat | arr | list[num | expr]:
    """Perform postselection on :python:`matrix` against the operator(s) specified in :python:`postselections`.

    The postselections can be given in either vector or matrix form.
    For the former, the transformation of the vector :math:`\\ket{\\Psi}` (residing in some composite Hilbert space :math:`\\SpaceHilbert`) follows the standard rule

    .. math:: \\ket{\\Psi^\\prime} = \\braket{\\phi}{\\Psi}

    where :math:`\\ket{\\phi} \\in \\tilde{\\SpaceHilbert}` is the postselection vector (which resides in a proper subsystem :math:`\\tilde{\\SpaceHilbert}` of :math:`\\SpaceHilbert`).
    In the case of a matrix form :math:`\\op{\\omega}` on :math:`\\tilde{\\SpaceHilbert}`, the notion of postselection of a density matrix :math:`\\op{\\rho}` on :math:`\\SpaceHilbert` naturally generalizes to

    .. math:: \\op{\\rho}^\\prime = \\trace_{\\tilde{\\SpaceHilbert}}[\\op{\\omega} \\op{\\rho}].

    If multiple postselections are supplied, :python:`matrix` will be successively postselected in the order in which they are given.
    If a vector :python:`matrix` is postselected against a matrix form, it will automatically be transformed into its matrix form via the outer product as necessary.

    Arguments
    ---------
    matrix : mat | arr | QuantumObject
        The matrix to be postselected.
    postselections: list[tuple[mat | arr | QuantumObject, list[int]]]
        A list of 2-tuples of vectors or matrix operators paired with the indices of their postselection target systems.
        The indices of each postselection must be contiguous.
    dim : int
        The dimensionality of :python:`matrix` and the item(s) of :python:`postselections`.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    mat | arr | list[num | expr]
        The postselected form of :python:`matrix`.
    """
    dim = 2 if dim is None else dim

    matrix = extract_representation(matrix)
    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

    num_systems = count_systems(matrix, dim)
    systems = [k for k in range(num_systems)]

    is_vector = False
    try:
        is_vector = matrix.is_vector
    except:
        if matrix_form(matrix) == Forms.VECTOR.value:
            is_vector = True

    are_vector = [False for n in postselections]
    for n, postselection in enumerate(postselections):
        try:
            are_vector[n] = postselection[0].is_vector
        except:
            if matrix_form(postselection[0]) == Forms.VECTOR.value:
                are_vector[n] = True
    postselection_is_vector = all(boolean is True for boolean in are_vector)

    matrices = []
    targets = []
    for postselection in postselections:
        operator = extract_representation(postselection[0])
        if matrix_form(operator) == Forms.VECTOR.value:
            operator = columnify(operator)
        operator = cast(operator, numerical=matrix_num, array=matrix_arr)
        matrices.append(operator)
        num_systems = count_systems(operator, dim)
        if len(postselection[1]) != num_systems:
            raise ValueError(
                """Mismatch between the postselection operator's calculated size and the number of its specified targets."""
            )
        targets.append(sorted(postselection[1]))

    operators = []
    identity = generate_identity(dim, numerical=matrix_num, array=matrix_arr)
    for system in systems:
        if system not in flatten_list(targets):
            operators.append(identity)
        else:
            min_targets = [min(group) for group in targets]
            if system in min_targets:
                operators.append(matrices[min_targets.index(system)])

    if is_vector is True and postselection_is_vector is True:
        operators_combined = tensor_product(*operators)
        matrix = matrix_multiplication(conjugate_transpose(operators_combined), matrix)
    else:
        for i, operator in enumerate(operators):
            operators[i] = densify(operator)
        operators_combined = tensor_product(*operators)
        matrix = matrix_multiplication(densify(operators_combined), densify(matrix))
        matrix = partial_trace(matrix=matrix, targets=flatten_list(targets), dim=dim)
    return cast(matrix, numerical=matrix_num, array=matrix_arr)


class OperationsMixin:
    """A mixin for endowing classes with the ability to have their :python:`matrix` property mutated by various quantum operations.

    Note
    ----
    The :py:class:`~qhronology.mechanics.operations.OperationsMixin` mixin is used exclusively by the :py:class:`~qhronology.quantum.states.QuantumState` class---please see :numref:`sec:docs_states_operations` :ref:`sec:docs_states_operations` for documentation on its methods.
    """

    def densify(self):
        """Convert the state to its equivalent (density) matrix representation.

        States that are already in density matrix form are unmodified.
        """
        self.current = densify(self)

    def dagger(self):
        """Perform conjugate transposition on the state."""
        self.current = dagger(self)

    def round(self):
        """Round the state's elements to the nearest (real) integer."""
        self.current = round(self)

    def simplify(self, comprehensive: bool | None = None):
        """Apply a forced simplification to the state using the values of its :python:`symbols` and :python:`substitutions` properties.

        Useful if intermediate simplification is required during a sequence of mutating operations in order to process the state into a more desirable form.

        Arguments
        ---------
        comprehensive : bool
            Whether the simplifying algorithm should use a relatively efficient subset of simplifying operations (:python:`False`), or alternatively use a larger, more powerful (but slower) set (:python:`True`).
            Defaults to :python:`False`.

        Note
        ----
        If :python:`comprehensive` is :python:`True`, the simplification algorithm will likely take *far* longer to execute than if :python:`comprehensive` were :python:`False`.
        """
        self.current = simplify(self, comprehensive=comprehensive)

    def rewrite(self, function: Callable):
        """Rewrite the elements of the state using the given mathematical function (:python:`function`).

        Useful when used with SymPy's mathematical functions, such as:

        - :python:`exp()`
        - :python:`log()`
        - :python:`sin()`
        - :python:`cos()`
        - :python:`sqrt()`

        Arguments
        ---------
        function : Callable
            A SymPy mathematical function.
        """
        self.current = rewrite(self, function=function)

    def apply(self, function: Callable, arguments: dict[str, Any] | None = None):
        """Apply a Python function (:python:`function`) to the state.

        Useful when used with SymPy's symbolic-manipulation functions, such as:

        - :python:`simplify()`
        - :python:`expand()`
        - :python:`factor()`
        - :python:`collect()`
        - :python:`cancel()`
        - :python:`apart()`
        - :python:`separatevars()`
        - :python:`rewrite()` (though the :py:meth:`~qhronology.quantum.states.QuantumState.rewrite` method should be used instead)

        More can be found at:

        - `SymPy documentation: Simplification <https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html>`_
        - `SymPy documentation: Simplify <https://docs.sympy.org/latest/modules/simplify/simplify.html>`_

        Arguments
        ---------
        function : Callable
            A Python function.
            Its first non-keyword argument must be able to take a mathematical expression or a matrix/array of such types.
        arguments : dict[str, str]
            A dictionary of keyword arguments (with the keywords as strings) to pass to the :python:`function` call.
            Defaults to :python:`{}`.
        """
        self.current = apply(self, function=function, arguments=arguments)

    def normalize(self, norm: num | expr | str | None = None):
        """Perform a forced (re)normalization on the state to the value specified (:python:`norm`).

        Useful when applied to a quantum state both before and after mutating operations, prior to any simplification (such as renormalization) performed on its processed output (obtained via the :python:`state()` method).

        Arguments
        ---------
        norm : num | expr | str
            The value to which the state is normalized.
            Defaults to :python:`1`.
        """
        norm = 1 if norm is None else norm
        self.current = normalize(self, norm=norm)

    def coefficient(self, scalar: num | expr | str | None = None):
        """Multiply the state by a scalar value (:python:`scalar`).

        Can be useful to manually (re)normalize states, or introduce a phase factor.

        Arguments
        ---------
        scalar : num | expr | str
            The value by which the state is multiplied.
            Defaults to :python:`1`.
        """
        scalar = 1 if scalar is None else scalar
        self.current = coefficient(self, scalar=scalar)

    def partial_trace(
        self,
        targets: list[int] | None = None,
        discard: bool | None = None,
        optimize: bool | None = None,
    ):
        """Perform a partial trace operation on the state.

        Arguments
        ---------
        targets : list[int]
            The numerical indices of the subsystem(s) to be partially traced over.
            Indexing begins at :python:`0`.
            Defaults to :python:`[]`.
        discard : bool
            Whether the systems corresponding to the indices given in :python:`targets` are to be discarded (:python:`True`) or kept (:python:`False`).
            Defaults to :python:`True`.
        optimize : bool
            Whether to optimize the partial trace implementation's algorithm.
            Can greatly increase the computational efficiency at the cost of a larger memory footprint during computation.
            Defaults to :python:`True`.
        """
        self.current = partial_trace(
            matrix=self,
            targets=targets,
            discard=discard,
            dim=self.dim,
            optimize=optimize,
        )

    def measure(
        self,
        operators: list[mat | arr | QuantumObject],
        targets: list[int] | None = None,
        observable: bool | None = None,
        statistics: bool | None = None,
    ) -> None | list[num | expr]:
        """Perform a quantum measurement on one or more systems (indicated in :python:`targets`) of the state.

        This method has two main modes of operation:

        - When :python:`statistics` is :python:`True`, the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in :python:`targets`) is measured, and the set of resulting statistics is returned.
          This takes the form of an ordered list of values :math:`\\{p_i\\}_i` associated with each given operator, where:

          - :math:`p_i = \\trace[\\Kraus_i^\\dagger \\Kraus_i \\op{\\rho}]` (measurement probabilities)
            when :python:`observable` is :python:`False`
            :inlinelatex:`\\newline` (:python:`operators` is a list of Kraus operators or projectors :math:`\\Kraus_i`)
          - :math:`p_i = \\trace[\\Observable_i \\op{\\rho}]` (expectation values)
            when :python:`observable` is :python:`True`
            :inlinelatex:`\\newline` (:python:`operators` is a list of observables :math:`\\Observable_i`)

        - When :python:`statistics` is :python:`False`, the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in :python:`targets`) is measured and mutated according to its predicted post-measurement form (i.e., the sum of all possible measurement outcomes).
          This yields the transformed states:

          - When :python:`observable` is :python:`False`:

          .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger

          - When :python:`observable` is :python:`True`:

          .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}]\\Observable_i

        In the case where :python:`operators` contains only a single item (:math:`\\Kraus`) and the current state (:math:`\\ket{\\psi}`) is a vector form, the transformation of the state is in accordance with the rule

        .. math::

           \\ket{\\psi^\\prime} = \\frac{\\Kraus \\ket{\\psi}}
               {\\sqrt{\\bra{\\psi} \\Kraus^\\dagger \\Kraus \\ket{\\psi}}}

        when :python:`observable` is :python:`False`. In all other mutation cases, the post-measurement state is a matrix, even if the pre-measurement state was a vector.

        The items in the list :python:`operators` can also be vectors (e.g., :math:`\\ket{\\xi_i}`), in which case each is converted into its corresponding operator matrix representation (e.g., :math:`\\ket{\\xi_i}\\bra{\\xi_i}`) prior to any measurements.

        Arguments
        ---------
        operators: list[mat | arr | QuantumObject]
            The operator(s) with which to perform the measurement.
            These would typically be a (complete) set of Kraus operators forming a POVM,
            a (complete) set of (orthogonal) projectors forming a PVM,
            or a set of observables constituting a complete basis for the relevant state space.
        targets : list[int]
            The numerical indices of the subsystem(s) to be measured.
            They must be contiguous, and their number must match the number of systems spanned by all given operators.
            Indexing begins at :python:`0`.
            All other systems are discarded (traced over) in the course of performing the measurement.
            Defaults to the value of :python:`self.systems`.
        observable: bool
            Whether to treat the items in :python:`operators` as observables instead of Kraus operators or projectors.
            Defaults to :python:`False`.
        statistics: bool
            Whether to return a list of probabilities (:python:`True`) or mutate the state into a post-measurement probabilistic sum of all outcomes (:python:`False`).
            Defaults to :python:`False`.

        Returns
        -------
        None
            Returned if :python:`statistics` is :python:`False`.
        num | expr | list[num | expr]
            A list of probabilities corresponding to each operator given in :python:`operators`.
            Returned if :python:`statistics` is :python:`True`.

        Note
        ----
        This method does not verify the validity of supplied POVMs or the completeness of sets of observables, nor does it renormalize the post-measurement state.
        """
        targets = self.systems if targets is None else targets
        observable = False if observable is None else observable
        statistics = False if statistics is None else statistics
        if statistics is False:
            self.current = measure(
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

    def postselect(self, postselections: list[tuple[mat | arr | QuantumObject, list[int]]]):
        """Perform postselection on the state against the operators(s) specified in :python:`postselections`.

        The postselections can be given in either vector or matrix form.
        For the former, the transformation of the vector :math:`\\ket{\\Psi}` (residing in some composite Hilbert space :math:`\\SpaceHilbert`) follows the standard rule

        .. math:: \\ket{\\Psi^\\prime} = \\braket{\\phi}{\\Psi}

        where :math:`\\ket{\\phi} \\in \\tilde{\\SpaceHilbert}` is the postselection vector (which resides in a proper subsystem :math:`\\tilde{\\SpaceHilbert}` of :math:`\\SpaceHilbert`).
        In the case of a matrix form :math:`\\op{\\omega}` on :math:`\\tilde{\\SpaceHilbert}`, the notion of postselection of a density matrix :math:`\\op{\\rho}` on :math:`\\SpaceHilbert` naturally generalizes to

        .. math:: \\op{\\rho}^\\prime = \\trace_{\\tilde{\\SpaceHilbert}}[\\op{\\omega} \\op{\\rho}].

        If multiple postselections are supplied, the state will be successively postselected in the order in which they are specified.
        If a vector state is postselected against a matrix form, it will automatically be transformed into its matrix form as necessary.

        Arguments
        ---------
        postselections: list[tuple[mat | arr | QuantumObject, list[int]]]
            A list of 2-tuples of vectors or matrix operators paired with the indices of their postselection target systems.
            The indices of each postselection must be contiguous.

        Note
        ----
        Any classes given in :python:`postselections` that are derived from the :py:class:`~qhronology.utilities.objects.QuantumObject` base class (such as :py:class:`~qhronology.quantum.states.QuantumState` and :py:class:`~qhronology.quantum.gates.QuantumGate`) will have their :python:`symbols` and :python:`substitutions` properties merged into the current :py:class:`~qhronology.quantum.states.QuantumState` instance.
        """
        # Add the postselection(s) symbols and substitutions to the current instance.
        for postselection in postselections:
            self.substitutions += extract_substitutions(postselection[0])
            symbols = extract_symbols(postselection[0])
            for symbol in symbols.keys():
                if symbol in self.symbols.keys():
                    self.symbols[symbol] |= symbols[symbol]
                else:
                    self.symbols |= {symbol: symbols[symbol]}

        self.current = postselect(self, postselections=postselections, dim=self.dim)
