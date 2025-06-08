# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
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
    """Convert ``vector`` to its corresponding matrix form via the outer product.
    If ``vector`` is a square matrix, it is unmodified.

    Arguments
    ---------
    vector : mat
        The input vector.

    Returns
    -------
    mat
        The outer product of ``vector`` with itself.

    Examples
    --------
    >>> vector = sp.Matrix([["a"], ["b"]])
    >>> densify(vector)
    Matrix([
    [a*conjugate(a), a*conjugate(b)],
    [b*conjugate(a), b*conjugate(b)]])
    """
    vector = extract_matrix(vector)
    return to_density(vector)


def columnify(vector: mat | QuantumObject) -> mat:
    """Convert ``vector`` to its corresponding column vector form via transposition.
    If ``vector`` is a square matrix, it is unmodified.

    Arguments
    ---------
    vector : mat
        The input vector.

    Returns
    -------
    mat
        The column form of ``vector``.

    Examples
    --------
    >>> vector = sp.Matrix([["a", "b"]])
    >>> columnify(vector)
    Matrix([
    [a],
    [b]])
    """
    vector = extract_matrix(vector)
    return to_column(vector)


def dagger(matrix: mat | QuantumObject) -> mat:
    """Perform conjugate transposition on ``matrix``.

    Arguments
    ---------
    matrix : mat
        The input matrix.

    Returns
    -------
    mat
        The conjugate transpose of ``matrix``.

    Examples
    --------
    >>> matrix = sp.Matrix([["a"], ["b"]])
    >>> dagger(matrix)
    Matrix([[conjugate(a), conjugate(b)]])

    >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
    >>> dagger(matrix)
    Matrix([
    [conjugate(a), conjugate(c)],
    [conjugate(b), conjugate(d)]])

    """
    matrix = extract_matrix(matrix)
    return sp.Matrix(Dagger(matrix))


def simplify(matrix: mat | QuantumObject) -> mat:
    """Simplify ``matrix`` using a powerful (albeit slow) algorithm.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be simplified.

    Returns
    -------
    mat
        The simplified version of ``matrix``.

    Examples
    --------
    >>> matrix = sp.Matrix(
    ...     [
    ...         ["(a**2 - 1)/(a - 1) - 1", "log(cos(b) + I*sin(b))/I"],
    ...         ["acos((exp(I*c) + exp(-I*c))/2)", "d**log(E*(sin(d)**2 + cos(d)**2))"],
    ...     ]
    ... )
    >>> simplify(matrix)
    Matrix([
    [a, b],
    [c, d]])
    """
    conditions = extract_conditions(matrix)
    symbols = extract_symbols(matrix)
    matrix = extract_matrix(matrix)

    matrix = symbolize_expression(matrix, symbols)
    conditions = symbolize_tuples(conditions, symbols)

    matrix = recursively_simplify(matrix, conditions)

    return matrix


def apply(
    matrix: mat | QuantumObject,
    function: Callable,
    arguments: dict[str, Any] | None = None,
) -> mat:
    """Apply a Python function (``function``) to ``matrix``.

    Useful when used with SymPy's symbolic-manipulation functions, such as:

    - ``apart()``
    - ``cancel()``
    - ``collect()``
    - ``expand()``
    - ``factor()``
    - ``simplify()``

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
        the ``function`` call.
        Defaults to ``{}``.

    Returns
    -------
    mat
        The transformed version of ``matrix``.

    Examples
    --------
    >>> matrix = sp.Matrix([["(x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)"]])
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
                f"Unable to apply the specified function (``{function.__name__}()``) to the matrix."
            )

    return matrix


def rewrite(matrix: mat | QuantumObject, function: Callable) -> mat:
    """Rewrite the elements of ``matrix`` using the given mathematical function (``function``).

    Useful when used with SymPy's mathematical functions, such as:

    - ``exp()``
    - ``log()``
    - ``sin()``
    - ``cos()``

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be transformed.
    function : Callable
        A SymPy mathematical function.

    Returns
    -------
    mat
        The transformed version of ``matrix``.

    Examples
    --------
    >>> matrix = sp.Matrix([["cos(x)"], ["sin(x)"]])
    >>> rewrite(matrix, function=sp.exp)
    Matrix([
    [   exp(I*x)/2 + exp(-I*x)/2],
    [-I*(exp(I*x) - exp(-I*x))/2]])
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
            f"The specified function (``{function.__name__}()``) cannot be used to rewrite \
            the matrix."
        )

    return matrix


def normalize(matrix: mat | QuantumObject, norm: num | sym | str | None = None) -> mat:
    """Normalize ``matrix`` to the value specified (``norm``).

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be normalized.
    norm : num | sym | str
        The value to which the matrix is normalized.
        Defaults to ``1``.

    Returns
    -------
    mat
        The normalized version of ``matrix``.

    Examples
    --------
    >>> matrix = sp.Matrix([["a"], ["b"]])
    >>> normalize(matrix, norm=1)
    Matrix([
    [a/sqrt(a*conjugate(a) + b*conjugate(b))],
    [b/sqrt(a*conjugate(a) + b*conjugate(b))]])

    >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
    >>> normalize(matrix, norm="n")
    Matrix([
    [a*n/(a + d), b*n/(a + d)],
    [c*n/(a + d), d*n/(a + d)]])
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
    """Multiply ``matrix`` by a scalar value (``scalar``).

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be scaled.
    scalar : num | sym | str
        The value by which the state is multiplied.
        Defaults to ``1``.

    Returns
    -------
    mat
        The scaled version of ``matrix``.

    Examples
    --------
    >>> matrix = sp.Matrix([["1"], ["1"]])
    >>> coefficient(matrix, scalar=1 / sp.sqrt(2))
    Matrix([
    [sqrt(2)/2],
    [sqrt(2)/2]])

    >>> matrix = sp.Matrix([["a"], ["b"]])
    >>> coefficient(matrix, scalar="exp(I*x)")
    Matrix([
    [a*exp(I*x)],
    [b*exp(I*x)]])
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
        Defaults to ``[]``.
    discard : bool
        Whether the systems corresponding to the indices given in ``targets`` are to be
        discarded (``True``) or kept (``False``).
        Defaults to ``True``.
    dim : int
        The dimensionality of the matrix.
        Must be a non-negative integer.
        Defaults to ``2``.
    optimize : bool
        Whether to optimize the implementation's algorithm.
        Can greatly increase the computational efficiency at the cost of a larger memory footprint
        during computation.
        Defaults to ``True``.

    Returns
    -------
    mat
        The reduced matrix.

    Examples
    --------
    >>> matrix = sp.Matrix([["a"], ["b"], ["c"], ["d"]])
    >>> partial_trace(matrix, targets=[0], dim=2)
    Matrix([
    [a*conjugate(a) + c*conjugate(c), a*conjugate(b) + c*conjugate(d)],
    [b*conjugate(a) + d*conjugate(c), b*conjugate(b) + d*conjugate(d)]])
    >>> partial_trace(matrix, targets=[1], dim=2)
    Matrix([
    [a*conjugate(a) + b*conjugate(b), a*conjugate(c) + b*conjugate(d)],
    [c*conjugate(a) + d*conjugate(b), c*conjugate(c) + d*conjugate(d)]])

    >>> matrix = sp.Matrix([["a", 0, 0, 0], [0, "b", 0, 0], [0, 0, "c", 0], [0, 0, 0, "d"]])
    >>> partial_trace(matrix, targets=[0], discard=True, dim=2)
    Matrix([
    [a + c,     0],
    [    0, b + d]])
    >>> partial_trace(matrix, targets=[1], discard=True, dim=2)
    Matrix([
    [a + b,     0],
    [    0, c + d]])
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
    """Perform a quantum measurement on one or more systems (indicated in ``targets``)
    of ``matrix``.

    This function has two main modes of operation:

    - When ``statistics`` is ``True``,
      the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in ``targets``)
      is measured and the set of resulting statistics is returned.
      This takes the form of an ordered list of values :math:`\\{p_i\\}_i` associated with each given operator, where:

      - :math:`p_i = \\trace[\\Kraus_i^\\dagger \\Kraus_i \\op{\\rho}]` (measurement probabilities)
        when ``observable`` is ``False``
        (``operators`` is a list of Kraus operators or projectors :math:`\\Kraus_i`)
      - :math:`p_i = \\trace[\\Observable_i \\op{\\rho}]` (expectation values)
        when ``observable`` is ``True``
        (``operators`` is a list of observables :math:`\\Observable_i`)

    - When ``statistics`` is ``False``,
      the (reduced) state (:math:`\\op{\\rho}`) (residing on the systems indicated in ``targets``)
      is measured and mutated it according to its predicted post-measurement form
      (i.e., the sum of all possible measurement outcomes).
      This yields the transformed states:

      - When ``observable`` is ``False``:

      .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger.

      - When ``observable`` is ``True``:

      .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}] \\Observable_i.

    In the case where ``operators`` contains only a single item (:math:`\\Kraus`) and the
    current state (:math:`\\ket{\\psi}`) is a vector form, the transformation of the state
    is in accordance with the rule

    .. math::

       \\ket{\\psi^\\prime} = \\frac{\\Kraus \\ket{\\psi}}
           {\\sqrt{\\bra{\\psi} \\Kraus^\\dagger \\Kraus \\ket{\\psi}}}

    when ``observable`` is ``False``. In all other mutation cases, the post-measurement state
    is a matrix, even if the pre-measurement state was a vector.

    The items in the list ``operators`` can also be vectors (e.g., :math:`\\ket{\\xi_i}`),
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
        Indexing begins at ``0``.
        All other systems are discarded (traced over) in the course of performing the measurement.
    observable: bool
        Whether to treat the items in ``operators`` as observables instead of Kraus operators
        or projectors.
        Defaults to ``False``.
    statistics: bool
        Whether to return a list of probabilities (``True``) or transform ``matrix`` into a
        post-measurement probabilistic sum of all outcomes (``False``).
        Defaults to ``False``.
    dim : int
        The dimensionality of ``matrix`` and the item(s) of ``operators``.
        Must be a non-negative integer.
        Defaults to ``2``.

    Returns
    -------
    mat
        The post-measurement ``matrix``.
        Returned only if ``statistics`` is ``False``.
    num | sym | list[num | sym]
        A list of probabilities corresponding to each operator given in ``operators``.
        Returned only if ``statistics`` is ``True``.

    Note
    ----
    This method does not check for validity of supplied POVMs or the completeness of sets of
    observables, nor does it renormalize the post-measurement state.

    Examples
    --------
    >>> matrix = sp.Matrix([["a"], ["b"]])
    >>> plus = sp.Matrix([[1 / sp.sqrt(2)], [1 / sp.sqrt(2)]])
    >>> minus = sp.Matrix([[1 / sp.sqrt(2)], [-1 / sp.sqrt(2)]])
    >>> measure(matrix, operators=[plus, minus], targets=[0], observable=False, statistics=True)
    [a*conjugate(a)/2 + a*conjugate(b)/2 + b*conjugate(a)/2 + b*conjugate(b)/2,
     a*conjugate(a)/2 - a*conjugate(b)/2 - b*conjugate(a)/2 + b*conjugate(b)/2]
    >>> measure(matrix, operators=[plus, minus], targets=[0], observable=False, statistics=False)
    Matrix([
    [a*conjugate(a)/2 + b*conjugate(b)/2, a*conjugate(b)/2 + b*conjugate(a)/2],
    [a*conjugate(b)/2 + b*conjugate(a)/2, a*conjugate(a)/2 + b*conjugate(b)/2]])

    >>> matrix = sp.Matrix([["a"], ["b"]])
    >>> I = sp.Matrix([[1, 0], [0, 1]])
    >>> X = sp.Matrix([[0, 1], [1, 0]])
    >>> Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    >>> Z = sp.Matrix([[1, 0], [0, -1]])
    >>> measure(matrix, operators=[I, X, Y, Z], targets=[0], observable=True, statistics=True)
    [a*conjugate(a) + b*conjugate(b),
     a*conjugate(b) + b*conjugate(a),
     I*(a*conjugate(b) - b*conjugate(a)),
     a*conjugate(a) - b*conjugate(b)]
    >>> measure(matrix, operators=[I, X, Y, Z], targets=[0], observable=True, statistics=False)
    Matrix([
    [2*a*conjugate(a), 2*a*conjugate(b)],
    [2*b*conjugate(a), 2*b*conjugate(b)]])
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
    """Perform postselection on ``matrix`` against the operator(s) specified in ``postselections``.

    The postselections can be given in either vector or matrix form. For the former,
    the transformation of the vector :math:`\\ket{\\Psi}` follows the standard rule

    .. math:: \\ket{\\Psi^\\prime} = \\braket{\\phi}{\\Psi}

    where :math:`\\ket{\\phi}` is the postselection vector.
    In the case of a matrix form :math:`\\op{\\omega}`, the notion of postselection of a
    matrix :math:`\\op{\\rho}` naturally generalizes to

    .. math:: \\op{\\rho}^\\prime = \\trace_{\\{i\\}}[\\op{\\omega} \\op{\\rho}]

    where :math:`\\{i\\}` is the set of indices corresponding to the subsystem(s) upon which
    the postselection is performed.

    If multiple postselections are supplied, ``matrix`` will be successively postselected in
    the order in which they are given. If a vector ``matrix`` is postselected against a matrix form,
    it will automatically be transformed into its matrix form via the outer product as necessary.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The matrix to be measured.
    postselections: list[tuple[mat | arr | QuantumObject, int]]
        A list of 2-tuples of vectors or matrix operators paired with the first (smallest) index
        of their postselection target systems.
    dim : int
        The dimensionality of ``matrix`` and the item(s) of ``postselections``.
        Must be a non-negative integer.
        Defaults to ``2``.

    Returns
    -------
    mat
        The postselected form of ``matrix``.

    Examples
    --------
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
    """A mixin for endowing classes with the ability to have their ``matrix`` property mutated
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

        Examples
        --------
        >>> psi = QuantumState(spec=[("a", [0]), ("b", [1])], form="vector", label="ψ")
        >>> psi.print()
        |ψ⟩ = a|0⟩ + b|1⟩
        >>> psi.densify()
        >>> psi.print()
        |ψ⟩⟨ψ| = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|
        """
        self.matrix = densify(self)

    def dagger(self):
        """Perform conjugate transposition on the state.

        Examples
        --------
        >>> psi = QuantumState(spec=[("a", [0]), ("b", [1])], form="vector", label="ψ")
        >>> psi.print()
        |ψ⟩ = a|0⟩ + b|1⟩
        >>> psi.dagger()
        >>> psi.print()
        ⟨ψ| = conjugate(a)⟨0| + conjugate(b)⟨1|
        """
        self.matrix = dagger(self)

    def simplify(self):
        """Apply a forced simplification to the state using the values of its ``symbols`` and
        ``conditions`` properties.

        Useful if intermediate simplification is required during a sequence of mutating operations
        in order to process the state into a more desirable form.

        """
        self.matrix = simplify(self)

    def apply(self, function: Callable, arguments: dict[str, Any] | None = None):
        """Apply a Python function (``function``) to the state.

        Useful when used with SymPy's symbolic-manipulation functions, such as:

        - ``simplify()``
        - ``expand()``
        - ``factor()``
        - ``collect()``
        - ``cancel()``
        - ``apart()``

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
            A dictionary of keyword arguments (both keys and values as strings) to pass
            to the ``function`` call.
            Defaults to ``{}``.

        Examples
        --------
        >>> psi = QuantumState(
        ...     spec=[("a*b + b*c + c*a", [0]), ("x*y + y*z + z*x", [1])], form="vector", label="ψ"
        ... )
        >>> psi.print()
        |ψ⟩ = (a*b + a*c + b*c)|0⟩ + (x*y + x*z + y*z)|1⟩
        >>> psi.apply(sp.collect, {"syms": ["a", "x"]})
        >>> psi.print()
        |ψ⟩ = (a*(b + c) + b*c)|0⟩ + (x*(y + z) + y*z)|1⟩
        >>> psi.apply(sp.expand)
        >>> psi.print()
        |ψ⟩ = (a*b + a*c + b*c)|0⟩ + (x*y + x*z + y*z)|1⟩
        """
        self.matrix = apply(self, function=function, arguments=arguments)

    def rewrite(self, function: Callable):
        """Rewrite the elements of the state using the given mathematical function (``function``).

        Useful when used with SymPy's mathematical functions, such as:

        - ``exp()``
        - ``log()``
        - ``sin()``
        - ``cos()``

        Arguments
        ---------
        function : Callable
            A SymPy mathematical function.

        Examples
        --------
        >>> psi = QuantumState(spec=[("cos(θ)", [0]), ("sin(θ)", [1])], form="vector", label="ψ")
        >>> psi.print()
        |ψ⟩ = cos(θ)|0⟩ + sin(θ)|1⟩
        >>> psi.rewrite(sp.exp)
        >>> psi.print()
        |ψ⟩ = (exp(I*θ)/2 + exp(-I*θ)/2)|0⟩ + -I*(exp(I*θ) - exp(-I*θ))/2|1⟩
        """
        self.matrix = rewrite(self, function=function)

    def normalize(self, norm: num | sym | str | None = None):
        """Perform a forced (re)normalization on the state to the value specified (``norm``).

        Useful when applied to the current quantum state both before and after mutating operations,
        prior to any simplification (such as renormalization) performed on the processed output
        (obtained via the ``state()`` method).

        Arguments
        ---------
        norm : num | sym | str
            The value to which the state is normalized.
            Defaults to ``1``.

        Examples
        --------
        >>> identity = QuantumState(spec=[("1", [0]), ("1", [1])], label="I")
        >>> identity.print()
        I = |0⟩⟨0| + |1⟩⟨1|
        >>> identity.normalize()
        >>> identity.print()
        I = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

        >>> psi = QuantumState(spec=[("a", [0]), ("b", [1])], form="vector", label="ψ")
        >>> psi.print()
        |ψ⟩ = a|0⟩ + b|1⟩
        >>> psi.normalize()
        >>> psi.print()
        |ψ⟩ = a/sqrt(a*conjugate(a) + b*conjugate(b))|0⟩ + b/sqrt(a*conjugate(a) + b*conjugate(b))|1⟩
        """
        norm = 1 if norm is None else norm
        self.matrix = normalize(self, norm=norm)

    def coefficient(self, scalar: num | sym | str | None = None):
        """Multiply the state by a scalar value (``scalar``).

        Can be useful to manually (re)normalize states, or introduce a phase factor.

        Arguments
        ---------
        scalar : num | sym | str
            The value by which the state is multiplied.
            Defaults to ``1``.

        Examples
        --------
        >>> psi = QuantumState(spec=[("1", [0]), ("1", [1])], form="vector", label="ψ")
        >>> psi.print()
        |ψ⟩ = |0⟩ + |1⟩
        >>> psi.coefficient(1 / sp.sqrt(2))
        >>> psi.print()
        |ψ⟩ = sqrt(2)/2|0⟩ + sqrt(2)/2|1⟩
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

        Performs a total trace if ``targets`` is unspecified.

        Arguments
        ---------
        targets : int | list[int]
            The numerical index/indices of the subsystem(s) to be partially traced over.
            Indexing begins at ``0``.
            Defaults to ``[]``.
        discard : bool
            Whether the systems corresponding to the indices given in ``targets`` are to be
            discarded (``True``) or kept (``False``).
            Defaults to ``True``.
        optimize : bool
            Whether to optimize the partial trace implementation's algorithm.
            Can greatly increase the computational efficiency at the cost of a larger memory
            footprint during computation.
            Defaults to ``True``.

        Examples
        --------
        >>> psi = QuantumState(
        ...     spec=[("a*u", [0, 0]), ("b*u", [1, 0]), ("a*v", [0, 1]), ("b*v", [1, 1])],
        ...     form="vector",
        ...     conditions=[
        ...         ("a*conjugate(a) + b*conjugate(b)", "1"),
        ...         ("u*conjugate(u) + v*conjugate(v)", "1"),
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

        >>> bell = QuantumState(
        ...     spec=[("1", [0, 0]), ("1", [1, 1])], form="vector", norm=1, label="Φ"
        ... )
        >>> bell.print()
        |Φ⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩
        >>> bell.partial_trace([0])
        >>> bell.notation = "ρ"
        >>> bell.print()
        ρ = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|
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
        """Perform a quantum measurement on one or more systems (indicated in ``targets``)
        of the state.

        This method has two main modes of operation:

        - When ``statistics`` is ``True``,
          the (reduced) state (:math:`\\op{\\rho}`)
          (residing on the systems indicated in ``targets``)
          is measured and the set of resulting statistics is returned.
          This takes the form of an ordered list of values :math:`\\{p_i\\}_i` associated with
          each given operator, where:

          - :math:`p_i = \\trace[\\Kraus_i^\\dagger \\Kraus_i \\op{\\rho}]`
            (measurement probabilities) when ``observable`` is ``False``
            (``operators`` is a list of Kraus operators or projectors :math:`\\Kraus_i`)
          - :math:`p_i = \\trace[\\Observable_i \\op{\\rho}]`
            (expectation values) when ``observable`` is ``True``
            (``operators`` is a list of observables :math:`\\Observable_i`)

        - When ``statistics`` is ``False``,
          the (reduced) state (:math:`\\op{\\rho}`)
          (residing on the systems indicated in ``targets``)
          is measured and mutated it according to its predicted post-measurement form
          (i.e., the sum of all possible measurement outcomes).
          This yields the transformed states:

          - When ``observable`` is ``False``:

          .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger.

          - When ``observable`` is ``True``:

          .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}]\\Observable_i.

        In the case where ``operators`` contains only a single item (:math:`\\Kraus`) and
        the current state (:math:`\\ket{\\psi}`) is a vector form,
        the transformation of the state is in accordance with the rule

        .. math::

           \\ket{\\psi^\\prime} = \\frac{\\Kraus \\ket{\\psi}}
               {\\sqrt{\\bra{\\psi} \\Kraus^\\dagger \\Kraus \\ket{\\psi}}}

        when ``observable`` is ``False``. In all other mutation cases, the post-measurement state
        is a matrix, even if the pre-measurement state was a vector.

        The items in the list ``operators`` can also be vectors (e.g., :math:`\\ket{\\xi_i}`),
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
            Indexing begins at ``0``.
            All other systems are discarded (traced over) in the course of performing the measurement. Defaults to the value of ``self.systems``.
        observable: bool
            Whether to treat the items in ``operators`` as observables instead of Kraus operators
            or projectors.
            Defaults to ``False``.
        statistics: bool
            Whether to return a list of probabilities (``True``) or mutate the state into a
            post-measurement probabilistic sum of all outcomes (``False``).
            Defaults to ``False``.

        Returns
        -------
        None
            Returned only if ``statistics`` is ``False``.
        num | sym | list[num | sym]
            A list of probabilities corresponding to each operator given in ``operators``.
            Returned only if ``statistics`` is ``True``.

        Note
        ----
        This method does not check for validity of supplied POVMs or the completeness of
        sets of observables, nor does it renormalize the post-measurement state.

        Examples
        --------
        >>> psi = QuantumState(spec=[("a", [0]), ("b", [1])], form="vector", label="ψ")
        >>> psi.print()
        |ψ⟩ = a|0⟩ + b|1⟩
        >>> I = Pauli(index=0)
        >>> X = Pauli(index=1)
        >>> Y = Pauli(index=2)
        >>> Z = Pauli(index=3)
        >>> psi.measure(operators=[I, X, Y, Z], observable=True, statistics=True)
        [a*conjugate(a) + b*conjugate(b),
         a*conjugate(b) + b*conjugate(a),
         I*(a*conjugate(b) - b*conjugate(a)),
         a*conjugate(a) - b*conjugate(b)]
        >>> psi.measure(operators=[I, X, Y, Z], observable=True, statistics=False)
        >>> psi.simplify()
        >>> psi.coefficient(sp.Rational(1, 2))
        >>> psi.print()
        |ψ⟩⟨ψ| = a*conjugate(a)|0⟩⟨0| + a*conjugate(b)|0⟩⟨1| + b*conjugate(a)|1⟩⟨0| + b*conjugate(b)|1⟩⟨1|

        >>> from qhronology.mechanics.matrices import ket
        >>> psi = QuantumState(spec=[("a", [0]), ("b", [1])], form="vector", label="ψ")
        >>> psi.print()
        |ψ⟩ = a|0⟩ + b|1⟩
        >>> psi.measure(operators=[ket(0), ket(1)], observable=False, statistics=True)
        [a*conjugate(a), b*conjugate(b)]
        >>> psi.measure(operators=[ket(0), ket(1)], observable=False, statistics=False)
        >>> psi.notation = "ρ"
        >>> psi.print()
        ρ = a*conjugate(a)|0⟩⟨0| + b*conjugate(b)|1⟩⟨1|
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
        specified in ``postselections``.

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
        order in which they are given. If a vector state is postselected against a matrix form,
        it will automatically be transformed into its matrix form as necessary.

        Arguments
        ---------
        postselections: list[tuple[mat | arr | QuantumObject, int]]
            A list of 2-tuples of vectors or matrix operators paired with the first (smallest) index
            of their postselection target systems.

        Note
        ----
        Any classes given in ``postselections`` that are derived from the
        :py:class:`~qhronology.utilities.objects.QuantumObject` base class
        (such as :py:class:`~qhronology.quantum.states.QuantumState`
        and :py:class:`~qhronology.quantum.gates.QuantumGate`)
        will have their ``symbols`` and ``conditions`` properties merged into the current
        :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Examples
        --------
        >>> psi = QuantumState(spec=[("a", [0, 0]), ("b", [1, 1])], form="vector", label="Ψ")
        >>> phi = QuantumState(spec=[("c", [0]), ("d", [1])], form="vector", label="φ")
        >>> psi.print()
        |Ψ⟩ = a|0,0⟩ + b|1,1⟩
        >>> phi.print()
        |φ⟩ = c|0⟩ + d|1⟩
        >>> psi.postselect([(phi, [0])])
        >>> psi.label = "Ψ'"
        >>> psi.print()
        |Ψ'⟩ = a*conjugate(c)|0⟩ + b*conjugate(d)|1⟩

        >>> from qhronology.mechanics.matrices import ket
        >>> psi = QuantumState(spec=[("a", [0, 0]), ("b", [1, 1])], form="vector", label="Ψ")
        >>> psi.print()
        |Ψ⟩ = a|0,0⟩ + b|1,1⟩
        >>> psi.label = "Ψ'"
        >>> psi.postselect([(ket(0), [0])])
        >>> psi.print()
        |Ψ'⟩ = a|0⟩
        >>> psi.reset()
        >>> psi.postselect([(ket(1), [0])])
        >>> psi.print()
        |Ψ'⟩ = b|1⟩
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
