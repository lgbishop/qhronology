# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

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
    sym,
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
    """Creates an ordered list of column vectors that form an orthonormal basis for a
    ``dim``-dimensional Hilbert space.

    Arguments
    ---------
    dim : int
        The dimensionality of the vector basis.
        Must be a non-negative integer.

    Returns
    -------
    list[int]
        An ordered list of basis vectors.

    Examples
    --------
    >>> vector_basis(2)
    [Matrix([
     [1],
     [0]]),
     Matrix([
     [0],
     [1]])]

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
    """
    return [sp.eye(dim).col(d) for d in range(0, dim)]


def ket(spec: int | list[int], dim: int | None = None) -> mat:
    """Creates a normalized ket (column) basis vector corresponding to the (multipartite)
    computational-basis value(s) of ``spec`` in a ``dim``-dimensional Hilbert space.

    In mathematical notation, ``spec`` describes the value of the ket vector, e.g., a ``spec`` of
    ``[i,j,k]`` corresponds to the ket vector :math:`\\ket{i,j,k}`
    (for some non-negative integers ``i``, ``j``, and ``k``).

    Arguments
    ---------
    spec : int | list[int]
        A non-negative integer or a list of such types.
    dim : int
        The dimensionality of the vector.
        Must be a non-negative integer.
        Defaults to ``2``.

    Returns
    -------
    mat
        A normalized column vector.

    Examples
    --------
    >>> ket(0)
    Matrix([
    [1],
    [0]])

    >>> ket(1)
    Matrix([
    [0],
    [1]])

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
    """
    spec = flatten_list([spec])
    dim = 2 if dim is None else dim
    basis = vector_basis(dim)
    return TensorProduct(*[sp.Matrix(basis[spec[n]]) for n in range(0, len(spec))])


def bra(spec: int | list[int], dim: int | None = None) -> mat:
    """Creates a normalized bra (row) basis vector corresponding to the (multipartite)
    computational-basis value(s) of ``spec`` in a ``dim``-dimensional dual Hilbert space.

    In mathematical notation, ``spec`` describes the value of the bra vector, e.g., a ``spec`` of
    ``[i,j,k]`` corresponds to the bra vector :math:`\\bra{i,j,k}`
    (for some non-negative integers ``i``, ``j``, and ``k``).

    Arguments
    ---------
    spec : int | list[int]
        A non-negative integer or a list of such types.
    dim : int
        The dimensionality of the vector.
        Must be a non-negative integer.
        Defaults to ``2``.

    Returns
    -------
    mat
        A normalized row vector.

    Examples
    --------
    >>> bra(0)
    Matrix([[1, 0]])

    >>> bra(1)
    Matrix([[0, 1]])

    >>> bra([0, 2], dim=3)
    Matrix([[0, 0, 1, 0, 0, 0, 0, 0, 0]])
    """
    spec = flatten_list([spec])
    dim = 2 if dim is None else dim
    return Dagger(ket(spec, dim))


def quantum_state(
    spec: (
        mat
        | arr
        | list[list[num | sym | str]]
        | list[tuple[num | sym | str, int | list[int]]]
    ),
    form: str | None = None,
    kind: str | None = None,
    dim: int | None = None,
) -> mat:
    """Constructs a ``dim``-dimensional matrix or vector representation of a quantum state from a
    given specification ``spec``.

    Arguments
    ---------
    spec
        The specification of the quantum state. Provides a complete description of the state's
        values in a standard ``dim``-dimensional basis. Can be one of:

        - a SymPy matrix (``mat``)
        - a NumPy array (``arr``)
        - a list of lists of numerical, symbolic, or string expressions that collectively specify
          a vector or (square) matrix (``list[list[num | sym | str]]``)
        - a list of 2-tuples of numerical, symbolic, or string coefficients paired their
          respective number-basis specification (``list[tuple[num | sym | str, int | list[int]]]``)

    form : str
        A string specifying the *form* for the quantum state to take.
        Can be either of ``"vector"`` or ``"matrix"``.
        Defaults to ``"matrix"``.
    kind : str
        A string specifying the *kind* for the quantum state to take.
        Can be either of ``"mixed"`` or ``"pure"``.
        Defaults to ``"mixed"``.
    dim : int
        The dimensionality of the quantum state's Hilbert space.
        Must be a non-negative integer.
        Defaults to ``2``.

    Returns
    -------
    mat
        The matrix or vector representation of the quantum state.

    Examples
    --------
    >>> quantum_state([("a", [0]), ("b", [1])], form="vector", kind="pure", dim=2)
    Matrix([
    [a],
    [b]])

    >>> quantum_state([("a", [0]), ("b", [1])], form="matrix", kind="pure", dim=2)
    Matrix([
    [a*conjugate(a), a*conjugate(b)],
    [b*conjugate(a), b*conjugate(b)]])

    >>> quantum_state([("a", [0]), ("b", [1])], form="matrix", kind="mixed", dim=2)
    Matrix([
    [a, 0],
    [0, b]])

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

    >>> quantum_state([["a", "b"], ["c", "d"]], form="matrix", kind="mixed", dim=2)
    Matrix([
    [a, b],
    [c, d]])

    >>> matrix = sp.Matrix([["a", "b"], ["c", "d"]])
    >>> quantum_state(matrix, form="matrix", kind="mixed", dim=2)
    Matrix([
    [a, b],
    [c, d]])
    """
    form = Forms.MATRIX.value if form is None else form
    if kind is None:
        kind = Kinds.PURE.value if form == Forms.VECTOR.value else Kinds.MIXED.value
    dim = 2 if dim is None else dim

    if form not in FORMS:
        raise ValueError(f"The given ``form`` ('{form}') is invalid.")
    if kind not in KINDS:
        raise ValueError(f"The given ``kind`` ('{kind}') is invalid.")
    if form not in COMPATIBILITIES[kind]:
        raise ValueError(
            f"The given ``kind`` ('{kind}') is incompatible with the given ``form`` ('{form}')."
        )

    if isinstance(spec, mat | arr | sp.matrices.immutable.ImmutableDenseMatrix) is True:
        state = sp.Matrix(spec)
    elif isinstance(spec, list) is True:
        if any(isinstance(item, list | tuple) is False for item in spec):
            raise ValueError(
                "The state's ``spec`` list must contain only lists or tuples."
            )
        elif any(isinstance(item, list) is False for item in spec) is False:
            state = sp.Matrix(spec)
        elif any(isinstance(item, tuple) is False for item in spec) is False:
            for twotuple in spec:
                if len(twotuple) != 2:
                    raise ValueError(
                        "One or more of the tuples in the given ``spec`` does not have exactly \
                        two (2) elements."
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
            raise ValueError("The given ``spec`` list is invalid.")
    else:
        raise ValueError("The given ``spec`` is invalid.")

    if matrix_shape(state) == "INVALID":
        raise ValueError(
            "The given ``spec`` does not correspond to either a square matrix or a vector."
        )

    if form == Forms.VECTOR.value:
        if matrix_shape(state) == "SQUARE":
            raise ValueError(
                "The given ``spec`` describes a square matrix and so cannot be cast into a \
                vector form."
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

    This is a kind of unsigned integer encoding. It creates a base-``dim`` numeral system
    representation of ``integer`` as an (ordered) list of encoded digits.
    Returns this list if ``output_list`` is ``True``, otherwise returns the corresponding
    ket vector (i.e., a ket vector with a spec of these digits).

    Arguments
    ---------
    integer : int
        The non-negative integer to be encoded.
    num_systems : int
        The number of systems (e.g., qubits) necessary to represent the integer in the encoding.
        Must be a non-negative integer.
        If ``None``, it automatically increases to the smallest possible number of systems
        with which the given ``integer`` can be encoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to ``2``.
    reverse : str
        Whether to reverse the ordering of the resulting encoded state.

        - If ``reverse`` is ``False``, the significance of the digits *decreases* along the
          list (i.e., the least-significant digit is last).
        - If ``reverse`` is ``True``, the significance of the digits *increases* along the
          list (i.e., the least-significant digit is first).

        Defaults to ``False``.
    output_list : bool
        Whether to output a list of encoded digits instead of an encoded state.
        Defaults to ``False``.

    Returns
    -------
    mat
        A normalized column vector (if ``output_list`` is ``False``).
    list[int]
        An ordered list of the encoded digits (if ``output_list`` is ``True``).

    Examples
    --------
    >>> encode(3, num_systems=2)
    Matrix([
    [0],
    [0],
    [0],
    [1]])

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

    >>> encode(264, num_systems=3, dim=10, output_list=True)
    [2, 6, 4]

    >>> encode(115, num_systems=8, output_list=True)
    [0, 1, 1, 1, 0, 0, 1, 1]

    >>> encode(115, num_systems=8, output_list=True, reverse=True)
    [1, 1, 0, 0, 1, 1, 1, 0]
    """
    dim = 2 if dim is None else dim
    reverse = False if reverse is None else reverse
    output_list = False if output_list is None else output_list

    digits = []
    integer = int(integer)
    if integer < 0:
        raise ValueError(f"The given ``integer`` ({integer}) cannot be less than zero.")
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
            f"The given ``num_systems`` ({num_systems}) is too few to encode the \
            ``integer`` ({integer}) in the ``dim`` ({dim})."
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
    For a faster algorithm, use the ``decode_fast()`` function.

    Note
    ----
    This function can also be called using the alias ``decode()``.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to ``2``.
    reverse : str
        Whether to reverse the digit ordering of the encoded state prior to decoding.

        - If ``reverse`` is ``False``, the significance of the digits should *decrease* along the
          list (i.e., the least-significant digit is last).
        - If ``reverse`` is ``True``, the significance of the digits should *increase* along the
          list (i.e., the least-significant digit is first).

        Defaults to ``False``.

    Returns
    -------
    int
        The decoded (unsigned) integer.

    Examples
    --------
    >>> decode_slow(encode(64))
    64

    >>> matrix = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0])
    >>> decode_slow(matrix)
    4
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
    The current method by which this particular implementation operates is fast but may be
    inaccurate (due to some computational shortcuts that may not work in all cases).
    For a slower but accurate algorithm, use the ``decode_slow()`` function.

    Note
    ----
    The output cannot be reversed like in ``decode_slow()``.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to ``2``.

    Returns
    -------
    int
        The decoded (unsigned) integer.

    Examples
    --------
    >>> decode_fast(encode(2048))
    2048

    >>> matrix = sp.Matrix([0, 0, 1, 0, 0, 0, 0])
    >>> decode_fast(matrix, dim=3)
    2
    """
    dim = 2 if dim is None else dim
    matrix = densify(extract_matrix(matrix))

    decoded = []
    for n in range(0, matrix.shape[0]):
        if matrix[n, n] != 0:
            decoded.append(n)

    if len(decoded) > 1:
        raise ValueError(
            "The given ``matrix`` encodes more than a single non-negative integer."
        )

    decoded = decoded[0]
    return decoded


def decode_multiple(
    matrix: mat | QuantumObject, dim: int | None = None, reverse: bool | None = None
) -> list[tuple[int, num | sym]]:
    """Decodes a quantum matrix or vector state to one or more unsigned integers with their respective probabilities.

    Arguments
    ---------
    matrix : mat | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to ``2``.
    reverse : str
        Whether to reverse the digit ordering of the encoded state prior to decoding.

        - If ``reverse`` is ``False``, the significance of the digits should *decrease* along the
          list (i.e., the least-significant digit is last).
        - If ``reverse`` is ``True``, the significance of the digits should *increase* along the
          list (i.e., the least-significant digit is first).

        Defaults to ``False``.

    Returns
    -------
    list[tuple[int, num | sym]]
        The list of tuples of pairs of decoded (unsigned) integers and their corresponding
        probabilities.

    Examples
    --------
    >>> a, b = sp.symbols("a, b")
    >>> matrix = a * encode(0) + b * encode(1)
    >>> decode_multiple(matrix)
    [(0, a*conjugate(a)), (1, b*conjugate(b))]

    >>> matrix = sp.Matrix(["x", 0, 0, "y"])
    >>> decode_multiple(matrix)
    [(0, x*conjugate(x)), (3, y*conjugate(y))]
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
