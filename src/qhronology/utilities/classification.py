# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

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
mat = sp.matrices.dense.MutableDenseMatrix
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

# Conversion dictionaries
# Useful for determining compatibilities between the various values
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


def matrix_form(matrix: mat) -> str | None:
    """Describe the form of ``matrix`` using the terminology of mathematics."""
    if matrix.shape[0] != 1 and matrix.shape[1] == 1:
        return Forms.VECTOR.value
    elif matrix.shape[0] == 1 and matrix.shape[1] != 1:
        return Forms.VECTOR.value
    elif matrix.shape[0] == matrix.shape[1]:
        return Forms.MATRIX.value
    else:
        raise ValueError(
            "The given ``matrix`` is invalid for describing either a vector or matrix state."
        )


def matrix_shape(matrix: mat) -> str | None:
    """Describe the shape of ``matrix`` using the terminology of mathematics."""
    if matrix.shape[0] != 1 and matrix.shape[1] == 1:
        return Shapes.COLUMN.value
    elif matrix.shape[0] == 1 and matrix.shape[1] != 1:
        return Shapes.ROW.value
    elif matrix.shape[0] == matrix.shape[1]:
        return Shapes.SQUARE.value
    else:
        raise ValueError(
            "The given ``matrix`` is invalid for describing either a vector or matrix state."
        )
