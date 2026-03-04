# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
Core functions for constructing matrices in quantum mechanics.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

import sympy as sp
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import (
    mat,
    arr,
    num,
    expr,
    Forms,
    Kinds,
    FORMS,
    KINDS,
    COMPATIBILITIES,
    matrix_shape,
)
from qhronology.utilities.helpers import (
    flatten_list,
    count_systems,
    extract_matrix,
    symbolize_expression,
)

from qhronology.mechanics.operations import densify, columnify, partial_trace


def vector_basis(dim: int) -> list[mat]:
    """Creates an ordered list of column vectors that form an orthonormal basis for a :python:`dim`-dimensional Hilbert space.

    Arguments
    ---------
    dim : int
        The dimensionality of the vector basis.
        Must be a non-negative integer.

    Returns
    -------
    list[int]
        An ordered list of basis vectors.
    """
    return [sp.eye(dim).col(d) for d in range(0, dim)]


def ket(spec: int | list[int], dim: int | None = None) -> mat:
    """Creates a normalized ket (column) basis vector corresponding to the (multipartite) computational-basis value(s) of :python:`spec` in a :python:`dim`-dimensional Hilbert space.

    In mathematical notation, :python:`spec` describes the value of the ket vector, e.g., a :python:`spec` of :python:`[i,j,k]` corresponds to the ket vector :math:`\\ket{i,j,k}` (for some non-negative integers :python:`i`, :python:`j`, and :python:`k`).

    Arguments
    ---------
    spec : int | list[int]
        A non-negative integer or a list of such types.
    dim : int
        The dimensionality of the vector.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    mat
        A normalized column vector.
    """
    spec = flatten_list([spec])
    dim = 2 if dim is None else dim
    basis = vector_basis(dim)
    return TensorProduct(*[sp.Matrix(basis[spec[n]]) for n in range(0, len(spec))])


def bra(spec: int | list[int], dim: int | None = None) -> mat:
    """Creates a normalized bra (row) basis vector corresponding to the (multipartite) computational-basis value(s) of :python:`spec` in a :python:`dim`-dimensional dual Hilbert space.

    In mathematical notation, :python:`spec` describes the value of the bra vector, e.g., a :python:`spec` of :python:`[i,j,k]` corresponds to the bra vector :math:`\\bra{i,j,k}` (for some non-negative integers :python:`i`, :python:`j`, and :python:`k`).

    Arguments
    ---------
    spec : int | list[int]
        A non-negative integer or a list of such types.
    dim : int
        The dimensionality of the vector.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    mat
        A normalized row vector.
    """
    spec = flatten_list([spec])
    dim = 2 if dim is None else dim
    return Dagger(ket(spec, dim))


def quantum_state(
    spec: (
        mat
        | arr
        | list[list[num | expr | str]]
        | list[tuple[num | expr | str, int | list[int]]]
    ),
    form: str | None = None,
    kind: str | None = None,
    dim: int | None = None,
) -> mat:
    """Constructs a :python:`dim`-dimensional matrix or vector representation of a quantum state from a given specification :python:`spec`.

    Arguments
    ---------
    spec
        The specification of the quantum state. Provides a complete description of the state's values in a standard :python:`dim`-dimensional basis. Can be one of:

        - a SymPy matrix (:python:`mat`)
        - a NumPy array (:python:`arr`)
        - a list of lists of numerical, symbolic, or string expressions that collectively specify a vector or (square) matrix (:python:`list[list[num | expr | str]]`)
        - a list of 2-tuples of numerical, symbolic, or string coefficients paired their respective number-basis specification (:python:`list[tuple[num | expr | str, int | list[int]]]`)

    form : str
        A string specifying the *form* for the quantum state to take.
        Can be either of :python:`"vector"` or :python:`"matrix"`.
        Defaults to :python:`"matrix"`.
    kind : str
        A string specifying the *kind* for the quantum state to take.
        Can be either of :python:`"mixed"` or :python:`"pure"`.
        Defaults to :python:`"mixed"`.
    dim : int
        The dimensionality of the quantum state's Hilbert space.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    mat
        The matrix or vector representation of the quantum state.
    """
    form = Forms.MATRIX.value if form is None else form
    if kind is None:
        kind = Kinds.PURE.value if form == Forms.VECTOR.value else Kinds.MIXED.value
    dim = 2 if dim is None else dim

    if form not in FORMS:
        raise ValueError(f"""The given :python:`form` ('{form}') is invalid.""")
    if kind not in KINDS:
        raise ValueError(f"""The given :python:`kind` ('{kind}') is invalid.""")
    if form not in COMPATIBILITIES[kind]:
        raise ValueError(
            f"""The given :python:`kind` ('{kind}') is incompatible with the given :python:`form` ('{form}')."""
        )

    if isinstance(spec, mat | arr | sp.matrices.immutable.ImmutableDenseMatrix) is True:
        state = sp.Matrix(spec)
    elif isinstance(spec, list) is True:
        if any(isinstance(item, list | tuple) is False for item in spec):
            raise ValueError(
                """The state's :python:`spec` list must contain only lists or tuples."""
            )
        elif any(isinstance(item, list) is False for item in spec) is False:
            state = sp.Matrix(spec)
        elif any(isinstance(item, tuple) is False for item in spec) is False:
            for twotuple in spec:
                if len(twotuple) != 2:
                    raise ValueError(
                        """One or more of the tuples in the given :python:`spec` does not have exactly two (2) elements."""
                    )
            coefficients = sp.Matrix([twotuple[0] for twotuple in spec])
            levels = [twotuple[1] for twotuple in spec]

            if form == Forms.VECTOR.value or kind == Kinds.PURE.value:
                state = 0 * ket(levels[0], dim)
            else:
                state = 0 * ket(levels[0], dim) * bra(levels[0], dim)
            for n in range(0, len(spec)):
                if form == Forms.VECTOR.value or kind == Kinds.PURE.value:
                    state = state + coefficients[n] * ket(levels[n], dim)
                else:
                    state = state + coefficients[n] * ket(levels[n], dim) * bra(
                        levels[n], dim
                    )
        else:
            raise ValueError("""The given :python:`spec` list is invalid.""")
    else:
        raise ValueError("""The given :python:`spec` is invalid.""")

    if matrix_shape(state) == "INVALID":
        raise ValueError(
            """The given :python:`spec` does not correspond to either a square matrix or a vector."""
        )

    if form == Forms.VECTOR.value:
        if matrix_shape(state) == "SQUARE":
            raise ValueError(
                """The given :python:`spec` describes a square matrix and so cannot be cast into a vector form."""
            )
        else:
            state = columnify(state)
    elif kind == Kinds.PURE.value:
        state = densify(state)
    else:
        state = densify(state)

    state = symbolize_expression(state)

    return state


def encode(
    integer: int,
    num_systems: int | None = None,
    dim: int | None = None,
    reverse: bool | None = None,
    output_list: bool | None = None,
) -> mat:
    """Encodes a non-negative integer as a single quantum state vector (ket).

    This is a kind of unsigned integer encoding. It creates a base-:python:`dim` numeral system representation of :python:`integer` as an (ordered) list of encoded digits.
    Returns this list if :python:`output_list` is :python:`True`, otherwise returns the corresponding ket vector (i.e., a ket vector with a spec of these digits).

    Arguments
    ---------
    integer : int
        The non-negative integer to be encoded.
    num_systems : int
        The number of systems (e.g., qubits) necessary to represent the integer in the encoding.
        Must be a non-negative integer.
        If :python:`None`, it automatically increases to the smallest possible number of systems with which the given :python:`integer` can be encoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    reverse : str
        Whether to reverse the ordering of the resulting encoded state.

        - If :python:`reverse` is :python:`False`, the significance of the digits *decreases* along the list (i.e., the least-significant digit is last).
        - If :python:`reverse` is :python:`True`, the significance of the digits *increases* along the list (i.e., the least-significant digit is first).

        Defaults to :python:`False`.
    output_list : bool
        Whether to output a list of encoded digits instead of an encoded state.
        Defaults to :python:`False`.

    Returns
    -------
    mat
        A normalized column vector (if :python:`output_list` is :python:`False`).
    list[int]
        An ordered list of the encoded digits (if :python:`output_list` is :python:`True`).
    """
    dim = 2 if dim is None else dim
    reverse = False if reverse is None else reverse
    output_list = False if output_list is None else output_list

    digits = []
    integer = int(integer)
    if integer < 0:
        raise ValueError(
            f"""The given :python:`integer` ({integer}) cannot be less than zero."""
        )
    if integer != 0:
        while integer != 0:
            integer, remainder = divmod(integer, dim)
            digits.append(remainder)
    else:
        digits.append(0)
    digits.reverse()

    num_systems = len(digits) if num_systems is None else num_systems
    if len(digits) > num_systems:
        raise ValueError(
            f"""The given :python:`num_systems` ({num_systems}) is too few to encode the :python:`integer` ({integer}) with dimensionality :python:`dim` ({dim})."""
        )

    padding = [0] * num_systems
    digits = padding + digits
    digits = digits[-num_systems:]

    if reverse is True:
        digits.reverse()

    encoded = digits
    if output_list is False:
        encoded = ket(digits, dim)

    return encoded


def decode_slow(
    matrix: mat | QuantumObject, dim: int | None = None, reverse: bool | None = None
) -> int:
    """Decodes a quantum matrix or vector state to an unsigned integer.

    Note
    ----
    The current method by which this particular implementation operates is accurate but slow.
    For a faster algorithm, use the :py:func:`~qhronology.mechanics.matrices.decode_fast` function.

    Note
    ----
    This function can also be called using the alias :py:func:`~qhronology.mechanics.matrices.decode`.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    reverse : str
        Whether to reverse the digit ordering of the encoded state prior to decoding.

        - If :python:`reverse` is :python:`False`, the significance of the digits should *decrease* along the list (i.e., the least-significant digit is last).
        - If :python:`reverse` is :python:`True`, the significance of the digits should *increase* along the list (i.e., the least-significant digit is first).

        Defaults to :python:`False`.

    Returns
    -------
    int
        The decoded (unsigned) integer.
    """
    dim = 2 if dim is None else dim
    reverse = False if reverse is None else reverse

    matrix = densify(extract_matrix(matrix))
    num_systems = count_systems(matrix, dim)

    digits = []
    decoding = [str(k) for k in range(0, dim)]
    for n in range(0, num_systems):
        discard = [k for k in range(0, num_systems) if k != n]
        quantum_unit = partial_trace(
            matrix=matrix, targets=discard, dim=dim, optimize=True
        )
        for m in range(0, quantum_unit.shape[0]):
            if quantum_unit[m, m] != 0:
                digits.append(m)

    if reverse is True:
        digits.reverse()

    decoded = sum(
        [
            digits[n] * dim ** ((len(digits) - 1) - n)
            for n in range(len(digits) - 1, 0 - 1, -1)
        ]
    )
    return decoded


decode = decode_slow
"""An alias for the :py:func:`~qhronology.mechanics.matrices.decode_slow` function."""


def decode_fast(matrix: mat | QuantumObject, dim: int | None = None) -> int:
    """Decodes a quantum matrix or vector state to an unsigned integer.

    Note
    ----
    The current method by which this particular implementation operates is fast but may be inaccurate (due to some computational shortcuts that may not work in all cases).
    For a slower but accurate algorithm, use the :py:func:`~qhronology.mechanics.matrices.decode_slow` function.

    Note
    ----
    The output cannot be reversed like in :py:func:`~qhronology.mechanics.matrices.decode_slow`.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    int
        The decoded (unsigned) integer.
    """
    dim = 2 if dim is None else dim
    matrix = densify(extract_matrix(matrix))

    decoded = []
    for n in range(0, matrix.shape[0]):
        if matrix[n, n] != 0:
            decoded.append(n)

    if len(decoded) > 1:
        raise ValueError(
            """The given :python:`matrix` encodes more than a single non-negative integer."""
        )

    decoded = decoded[0]
    return decoded


def decode_multiple(
    matrix: mat | QuantumObject, dim: int | None = None, reverse: bool | None = None
) -> list[tuple[int, num | expr]]:
    """Decodes a quantum matrix or vector state to one or more unsigned integers with their respective probabilities.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    reverse : str
        Whether to reverse the digit ordering of the encoded state prior to decoding.

        - If :python:`reverse` is :python:`False`, the significance of the digits should *decrease* along the list (i.e., the least-significant digit is last).
        - If :python:`reverse` is :python:`True`, the significance of the digits should *increase* along the list (i.e., the least-significant digit is first).

        Defaults to :python:`False`.

    Returns
    -------
    list[tuple[int, num | expr]]
        The list of tuples of pairs of decoded (unsigned) integers and their corresponding probabilities.
    """
    dim = 2 if dim is None else dim
    reverse = False if reverse is None else reverse
    matrix = densify(extract_matrix(matrix))

    decoded = []
    for n in range(0, matrix.shape[0]):
        if matrix[n, n] != 0:
            elementary = sp.zeros(matrix.shape[0])
            elementary[n, n] = 1
            decoded.append(
                (decode_slow(matrix=elementary, reverse=reverse), matrix[n, n])
            )

    return decoded
