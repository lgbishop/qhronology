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

from qhronology.mechanics.operations import columnify, densify, partial_trace
from qhronology.utilities.classification import (
    COMPATIBILITIES,
    FORMS,
    Forms,
    KINDS,
    Kinds,
    arr,
    expr,
    mat,
    matrix_shape,
    num,
)
from qhronology.utilities.helpers import (
    cast,
    conjugate_transpose,
    count_rows,
    count_systems,
    dtype,
    extract_representation,
    flatten_list,
    generate_zeros,
    symbolize_expression,
    tensor_product,
    to_numerical,
)


def vector_basis(
    dim: int, numerical: bool | None = None, array: bool | None = None
) -> list[mat | arr]:
    """Creates an ordered list of column vectors that form an orthonormal basis for a :python:`dim`-dimensional Hilbert space.

    Arguments
    ---------
    dim : int
        The dimensionality of the vector basis.
        Must be a non-negative integer.
    numerical : bool
        Whether to cast the vector elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the vectors as NumPy arrays (:python:`True`) or SymPy matrices (:python:`False`).
        Defaults to :python:`False`.

    Returns
    -------
    list[mat | arr]
        An ordered list of basis vectors.
    """
    return [
        cast(sp.eye(dim).col(d), numerical=numerical, array=array)
        for d in range(0, dim)
    ]


def ket(
    spec: int | list[int],
    dim: int | None = None,
    numerical: bool | None = None,
    array: bool | None = None,
) -> mat | arr:
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
    numerical : bool
        Whether to cast the vector elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the vector as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.

    Returns
    -------
    mat | arr
        A normalized column vector.
    """
    spec = flatten_list([spec])
    dim = 2 if dim is None else dim
    basis = vector_basis(dim=dim, numerical=numerical, array=array)
    return tensor_product(*[basis[spec[n]] for n in range(0, len(spec))])


def bra(
    spec: int | list[int],
    dim: int | None = None,
    numerical: bool | None = None,
    array: bool | None = None,
) -> mat | arr:
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
    numerical : bool
        Whether to cast the vector elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the vector as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.

    Returns
    -------
    mat | arr
        A normalized row vector.
    """
    spec = flatten_list([spec])
    dim = 2 if dim is None else dim
    return conjugate_transpose(ket(spec, dim, numerical=numerical, array=array))


def quantum_object(
    spec: (
        mat
        | arr
        | list[list[num | expr | str]]
        | list[tuple[num | expr | str, int | list[int]]]
    ),
    form: str | None = None,
    kind: str | None = None,
    dim: int | None = None,
    numerical: bool | None = None,
    array: bool | None = None,
) -> mat | arr:
    """Constructs a :python:`dim`-dimensional matrix or vector representation of a quantum object from a given specification :python:`spec`.

    Arguments
    ---------
    spec
        The specification of the quantum object. Provides a description of the object's values in a standard :python:`dim`-dimensional basis. Can be one of:

        - a SymPy matrix (:python:`mat`)
        - a NumPy array (:python:`arr`)
        - a list of lists of numerical, symbolic, or string expressions that collectively describe a vector or (square) matrix (:python:`list[list[num | expr | str]]`)
        - a list of 2-tuples of numerical, symbolic, or string coefficients paired their respective number-basis specification (:python:`list[tuple[num | expr | str, int | list[int]]]`)

    form : str
        A string specifying the *form* for the quantum object to take.
        Can be either of :python:`"vector"` or :python:`"matrix"`.
        Defaults to :python:`"matrix"`.
    kind : str
        A string specifying the *kind* for the quantum object to take.
        Can be either of :python:`"mixed"` or :python:`"pure"`.
        Defaults to :python:`"mixed"`.
    dim : int
        The dimensionality of the quantum object's Hilbert space.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    numerical : bool
        Whether to cast the matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.

    Returns
    -------
    mat | arr
        The matrix or vector representation of the quantum object.
    """
    form = Forms.MATRIX.value if form is None else form
    if kind is None:
        kind = Kinds.PURE.value if form == Forms.VECTOR.value else Kinds.MIXED.value
    dim = 2 if dim is None else dim
    numerical = False if numerical is None else numerical
    array = False if array is None else array

    if form not in FORMS:
        raise ValueError(f"""The given `form` ('{form}') is invalid.""")
    if kind not in KINDS:
        raise ValueError(f"""The given `kind` ('{kind}') is invalid.""")
    if form not in COMPATIBILITIES[kind]:
        raise ValueError(
            f"""The given `kind` ('{kind}') is incompatible with the given `form` ('{form}')."""
        )

    if isinstance(spec, mat | arr | sp.matrices.immutable.ImmutableDenseMatrix) is True:
        matrix = cast(matrix=spec, numerical=numerical, array=array)
    elif isinstance(spec, list) is True:
        if any(isinstance(item, list | tuple) is False for item in spec):
            raise ValueError(
                """The object's `spec` list must contain only lists or tuples."""
            )
        elif any(isinstance(item, list) is False for item in spec) is False:
            matrix = cast(matrix=spec, numerical=numerical, array=array)
        elif any(isinstance(item, tuple) is False for item in spec) is False:
            for twotuple in spec:
                if len(twotuple) != 2:
                    raise ValueError(
                        """One or more of the tuples in the given `spec` does not have exactly two (2) elements."""
                    )
            coefficients = cast(
                matrix=[twotuple[0] for twotuple in spec],
                numerical=numerical,
                array=array,
            )
            levels = [twotuple[1] for twotuple in spec]

            if form == Forms.VECTOR.value or kind == Kinds.PURE.value:
                matrix = 0 * ket(levels[0], dim, numerical, array)
            else:
                matrix = (
                    0
                    * ket(levels[0], dim, numerical, array)
                    * bra(levels[0], dim, numerical, array)
                )
            for n in range(0, len(spec)):
                if isinstance(coefficients[n], str) is True:
                    coefficients[n] = sp.sympify(coefficients[n])
                if form == Forms.VECTOR.value or kind == Kinds.PURE.value:
                    matrix = matrix + coefficients[n] * ket(
                        levels[n], dim, numerical, array
                    )
                else:
                    matrix = matrix + coefficients[n] * ket(
                        levels[n], dim, numerical, array
                    ) * bra(levels[n], dim, numerical, array)
        else:
            raise ValueError("""The given `spec` list is invalid.""")
    else:
        raise ValueError("""The given `spec` is invalid.""")

    if matrix_shape(matrix) == "INVALID":
        raise ValueError(
            """The given `spec` does not correspond to either a square matrix or a vector."""
        )

    if form == Forms.VECTOR.value:
        if matrix_shape(matrix) == "SQUARE":
            raise ValueError(
                """The given `spec` describes a square matrix and so cannot be cast into a vector form."""
            )
        else:
            matrix = columnify(matrix)
    elif kind == Kinds.PURE.value:
        matrix = densify(matrix)
    else:
        matrix = densify(matrix)

    matrix = symbolize_expression(matrix)

    return cast(matrix, numerical=numerical, array=array)


def encode(
    integer: int,
    num_systems: int | None = None,
    dim: int | None = None,
    numerical: bool | None = None,
    array: bool | None = None,
    reverse: bool | None = None,
    return_type: list | tuple | str | None = None,
) -> mat | arr | list[int] | tuple[int] | str:
    """Encodes a non-negative integer as a single quantum state vector (ket).

    This is a kind of unsigned integer encoding. It creates a base-:python:`dim` numeral system representation of :python:`integer` as an (ordered) list, tuple, or string of encoded digits.
    Returns this output format if :python:`return_type` is not :python:`None`, otherwise returns the corresponding ket vector (i.e., a ket vector with a :python:`spec` of these digits).

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
    numerical : bool
        Whether to cast the vector elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the vector as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.
    reverse : bool
        Whether to reverse the ordering of the resulting encoded state.

        - If :python:`reverse` is :python:`False`, the significance of the digits *decreases* along the list (i.e., the least-significant digit is last).
        - If :python:`reverse` is :python:`True`, the significance of the digits *increases* along the list (i.e., the least-significant digit is first).

        Defaults to :python:`False`.
    return_type: list | tuple | str
        The desired output format as a list, tuple, or string of encoded digits (instead of an encoded vector state).
        If :python:`None`, returns the encoded ket vector.
        Defaults to :python:`None`.

    Returns
    -------
    mat | arr
        A normalized column vector (if :python:`return_type` is :python:`None`).
    list[int] | tuple[int] | str
        An ordered list, tuple, or string of the encoded digits (if :python:`return_type` is not :python:`None`).
    """
    dim = 2 if dim is None else dim
    reverse = False if reverse is None else reverse

    digits = []
    integer = int(integer)
    if integer < 0:
        raise ValueError(
            f"""The given `integer` ({integer}) cannot be less than zero."""
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
            f"""The given `num_systems` ({num_systems}) is too few to encode the `integer` ({integer}) with dimensionality `dim` ({dim})."""
        )

    padding = [0] * num_systems
    digits = padding + digits
    digits = digits[-num_systems:]

    if reverse is True:
        digits.reverse()

    encoded = digits
    if return_type is None:
        encoded = ket(digits, dim=dim, numerical=numerical, array=array)
    else:
        if return_type == list:
            encoded = list(encoded)
        if return_type == tuple:
            encoded = tuple(encoded)
        if return_type == str:
            encoded = [str(digit) for digit in encoded]
            encoded = "".join(encoded)

    return encoded


def decode(
    encoded: mat | arr | QuantumObject | list[int] | tuple[int] | str,
    dim: int | None = None,
    reverse: bool | None = None,
) -> int:
    """Decodes a matrix state, vector state, or bitstring to an unsigned integer.

    This only makes sense if the input state has exactly one non-zero entry.

    Arguments
    ---------
    encoded : mat | arr | QuantumObject | list[int] | tuple[int] | str
        The object to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    reverse : bool
        Whether to reverse the digit ordering of the encoded object prior to decoding.

        - If :python:`reverse` is :python:`False`, the significance of the digits should *decrease* along the list (i.e., the least-significant digit is last).
        - If :python:`reverse` is :python:`True`, the significance of the digits should *increase* along the list (i.e., the least-significant digit is first).

        Defaults to :python:`False`.

    Returns
    -------
    int
        The decoded (unsigned) integer.

    Note
    ----
    The current method by which this particular implementation operates is accurate but slow.
    For a faster algorithm (that only works for states), use the :py:func:`~qhronology.mechanics.matrices.decode_fast` function.
    """
    dim = 2 if dim is None else dim
    reverse = False if reverse is None else reverse

    if isinstance(encoded, list | tuple | str) is True:
        bitstring = list(encoded)

        if reverse is False:
            bitstring.reverse()

        decoded = sum(
            [int(bitstring[i]) * (dim ** (i)) for i in range(0, len(bitstring))]
        )
    else:
        matrix = densify(extract_representation(encoded))
        num_systems = count_systems(matrix, dim)

        digits = []
        for n in range(0, num_systems):
            discard = [k for k in range(0, num_systems) if k != n]
            quantum_unit = partial_trace(
                matrix=matrix, targets=discard, dim=dim, optimize=True
            )
            for m in range(0, count_rows(quantum_unit)):
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


def decode_fast(encoded: mat | arr | QuantumObject, dim: int | None = None) -> int:
    """Decodes a quantum matrix or vector state to an unsigned integer.

    This only makes sense if the input state has exactly one non-zero entry.

    Arguments
    ---------
    encoded : mat | arr | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to :python:`2`.

    Returns
    -------
    int
        The decoded (unsigned) integer.

    Note
    ----
    The current method by which this particular implementation operates is fast but may be inaccurate (due to some computational shortcuts that may not work in all cases).
    For a slower but accurate algorithm, use the :py:func:`~qhronology.mechanics.matrices.decode` function.

    Note
    ----
    The output cannot be reversed like in :py:func:`~qhronology.mechanics.matrices.decode`.
    """
    dim = 2 if dim is None else dim
    matrix = densify(extract_representation(encoded))

    decoded = []
    for n in range(0, count_rows(matrix)):
        if matrix[n, n] != 0:
            decoded.append(n)

    if len(decoded) > 1:
        raise ValueError(
            """The given `matrix` encodes more than a single non-negative integer."""
        )

    decoded = decoded[0]
    return decoded


def decode_multiple(
    encoded: mat | arr | QuantumObject,
    dim: int | None = None,
    reverse: bool | None = None,
) -> list[tuple[int, num | expr]]:
    """Decodes a quantum matrix or vector state to one or more unsigned integers with their respective probabilities.

    This only makes sense if the input state is both equiprobabilistic and non-symbolic.

    Arguments
    ---------
    encoded : mat | arr | QuantumObject
        The quantum (matrix or vector) state to be decoded.
    dim : int
        The dimensionality (or base) of the encoding.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    reverse : bool
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
    matrix = densify(extract_representation(encoded))

    matrix_num = True if issubclass(dtype(matrix), num) is True else False
    matrix_arr = True if isinstance(matrix, arr) is True else False

    decoded = []
    for n in range(0, count_rows(matrix)):
        if matrix[n, n] != 0:
            elementary = generate_zeros(
                count_rows(matrix), numerical=matrix_num, array=matrix_arr
            )
            elementary[n, n] = to_numerical(1, numerical=matrix_num)
            decoded.append(
                (decode(elementary, reverse=reverse), matrix[n, n])
            )

    return decoded
