# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
Composite types, enums, dictionaries, and functions for the classification of quantum states and gates.
Not intended to be used directly by the user.
"""

from enum import StrEnum
import numbers

import numpy as np
import sympy as sp

num = numbers.Number | np.generic | sp.Basic
sym = (
    sp.matrices.expressions.matexpr.MatrixSymbol
    | sp.matrices.expressions.matexpr.MatrixElement
    | sp.core.symbol.Symbol
)
expr = sp.core.expr.Expr
mat = sp.matrices.dense.MutableDenseMatrix | sp.matrices.immutable.ImmutableDenseMatrix
arr = np.ndarray


class Forms(StrEnum):
    VECTOR = "vector"
    MATRIX = "matrix"


class Kinds(StrEnum):
    PURE = "pure"
    MIXED = "mixed"


class Shapes(StrEnum):
    ROW = "row"
    COLUMN = "column"
    SQUARE = "square"
    INVALID = "invalid"


FORMS = {Forms.VECTOR.value, Forms.MATRIX.value}

KINDS = {Kinds.PURE.value, Kinds.MIXED.value}

SHAPES = {
    Shapes.ROW.value,
    Shapes.COLUMN.value,
    Shapes.SQUARE.value,
    Shapes.INVALID.value,
}

# Conversion dictionaries (useful for determining compatibilities between the various values):
FORM_SHAPE = {
    Forms.VECTOR.value: {Shapes.ROW.value, Shapes.COLUMN.value},
    Forms.MATRIX.value: {Shapes.SQUARE.value},
}

KIND_SHAPE = {
    Kinds.PURE.value: {Shapes.ROW.value, Shapes.COLUMN.value},
    Kinds.MIXED.value: {Shapes.SQUARE.value},
}

KIND_FORM = {
    Kinds.PURE.value: {Forms.VECTOR.value, Forms.MATRIX.value},
    Kinds.MIXED.value: {Forms.MATRIX.value},
}

FORM_KIND = {
    Forms.VECTOR.value: {Kinds.PURE.value},
    Forms.MATRIX.value: {Kinds.PURE.value, Kinds.MIXED.value},
}

COMPATIBILITIES = KIND_FORM | FORM_KIND


def count_rows(matrix: mat | arr) -> int:
    """Count the number of rows of :python:`matrix`."""
    rows = matrix.shape[0]
    try:
        matrix.shape[1]
    except:
        rows = 1
    return rows


def count_columns(matrix: mat | arr) -> int:
    """Count the number of columns of :python:`matrix`."""
    columns = 1
    try:
        columns = matrix.shape[1]
    except:
        columns = matrix.shape[0]
    return columns


def matrix_form(matrix: mat | arr) -> str:
    """Describe the form of :python:`matrix` using the terminology of mathematics."""
    rows = count_rows(matrix)
    columns = count_columns(matrix)
    if rows == columns and rows != 1:
        return Forms.MATRIX.value
    elif (rows == 1 and columns != 1) or (rows != 1 and columns == 1):
        return Forms.VECTOR.value
    else:
        raise ValueError(
            """The given `matrix` is invalid for describing either a vector or matrix state."""
        )


def matrix_shape(matrix: mat | arr) -> str:
    """Describe the shape of :python:`matrix` using the terminology of mathematics."""
    rows = count_rows(matrix)
    columns = count_columns(matrix)
    if rows != 1 and columns == 1:
        return Shapes.COLUMN.value
    elif rows == 1 and columns != 1:
        return Shapes.ROW.value
    elif rows == columns:
        return Shapes.SQUARE.value
    else:
        raise ValueError(
            """The given `matrix` is invalid for describing either a vector or matrix state."""
        )
