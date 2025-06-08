# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
The base class for constructing quantum states and gates.
Not intended to be used directly by the user.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

from typing import Any

import sympy as sp
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import (
    mat,
    num,
    sym,
    Forms,
    Kinds,
    Shapes,
    matrix_form,
    matrix_shape,
)
from qhronology.utilities.diagrams import VisualizationMixin
from qhronology.utilities.helpers import count_systems, stringify
from qhronology.utilities.symbolics import SymbolicsProperties


class QuantumObject(VisualizationMixin, SymbolicsProperties):
    """A base class forming the backbone of the QuantumState and QuantumGate classes.

    Not intended to be instantiated directly itself, but rather indirectly via the constructors
    of its derived classes."""

    def __init__(
        self,
        form: str | None = None,
        matrix: mat | None = None,
        dim: int | None = None,
        num_systems: int | None = None,
        symbols: dict[sym | str, dict[str, Any]] | None = None,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        conjugate: bool | None = None,
        label: str | None = None,
        notation: str | None = None,
        family: str | None = None,
        debug: bool | None = None,
    ):
        form = Forms.MATRIX.value if form is None else form
        matrix = sp.zeros(2) if matrix is None else matrix
        dim = 2 if dim is None else dim
        conjugate = False if conjugate is None else conjugate
        num_systems = count_systems(matrix, dim) if num_systems is None else num_systems
        label = "A" if label is None else label
        notation = None if notation is None else notation
        family = "PUSH" if family is None else family
        debug = False if debug is None else debug
        SymbolicsProperties.__init__(self, symbols=symbols, conditions=conditions)

        self.form = form
        self.matrix = matrix
        self.dim = dim
        self.num_systems = num_systems
        self.conjugate = conjugate
        self.label = label
        self.notation = notation
        self.family = family
        self.debug = debug

    def __str__(self) -> str:
        return str(self.notation) + " = " + stringify(self.output(), self.dim)

    def __repr__(self) -> str:
        return repr(self.output())

    def print(self):
        print(self)

    def output(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
    ) -> mat:
        """Return the object's simplified matrix representation.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the state.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the object.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the object.
            If ``False``, does not conjugate.
            Defaults to the value of ``self.conjugate``.

        Returns
        -------
        mat
            The object's simplified matrix representation.

        """
        output = self.matrix

        output = symbolize_expression(output, self.symbols_list)

        # Conditions
        conditions = self.conditions if conditions is None else conditions
        conditions = symbolize_tuples(conditions, self.symbols_list)
        output = output.subs(conditions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            output = recursively_simplify(output, conditions)

        # Conjugation
        conjugate = self.conjugate if conjugate is None else conjugate
        if conjugate is True:
            output = Dagger(output)

        return output

    @property
    def form(self) -> str:
        """The *form* of the object.
        Can be either of ``"vector"`` or ``"matrix"``.
        Only :py:class:`~qhronology.quantum.states.QuantumState` objects can be ``"vector"``.
        """
        return matrix_form(self.matrix)

    @form.setter
    def form(self, form: str):
        if hasattr(self, "_kind"):
            if form == Forms.VECTOR.value and self.kind == Kinds.MIXED.value:
                raise AttributeError(
                    f"The given ``form`` ('{form}') is incompatible with the given ``kind`` ('{self.kind}')."
                )
        self._form = form

    @property
    def is_vector(self) -> bool:
        """Test for whether the object is a vector.
        Returns ``True`` if so, otherwise ``False``."""
        is_vector = False
        if self.form == Forms.VECTOR.value:
            is_vector = True
        return is_vector

    @property
    def dim(self) -> int:
        """The dimensionality of the quantum object.
        Must be a non-negative integer."""
        return self._dim

    @dim.setter
    def dim(self, dim: int):
        if hasattr(self, "_dim") is True:
            raise AttributeError(
                "The ``dim`` attribute cannot be set after instancing."
            )
        self._dim = dim

    @property
    def label(self) -> str:
        """The unformatted string used to represent the object in mathematical expressions.
        Must have a non-zero length."""
        return self._label

    @label.setter
    def label(self, label: str):
        self._label = label

    @property
    def labels(self) -> list[str]:
        """An ordered list of the object's labels corresponding to its ``boundaries``.
        Used exclusively by the visualization engine."""
        return [self.notation]

    @property
    def notation(self) -> str:
        """The formatted string used to represent the object in mathematical expressions.
        When set, overrides the value of the ``label`` property.
        Must have a non-zero length.
        Not intended to be set by the user in most cases."""
        if self._notation is None:
            if self.is_vector is True:
                if matrix_shape(self.matrix) == Shapes.COLUMN.value:
                    notation = "|" + self.label + "⟩"
                elif matrix_shape(self.matrix) == Shapes.ROW.value:
                    notation = "⟨" + self.label + "|"
                else:
                    notation = self.label
            else:
                notation = self.label
                if hasattr(self, "_kind"):
                    if self.kind == Kinds.PURE.value:
                        notation = "|" + self.label + "⟩⟨" + self.label + "|"
        else:
            notation = self._notation
        return notation

    @notation.setter
    def notation(self, notation: str):
        self._notation = notation

    @property
    def family(self) -> str:
        """The code of the block element that the object is to be visualized as.
        Not intended to be set by the user."""
        return self._family

    @family.setter
    def family(self, family: str):
        self._family = family

    @property
    def boundaries(self) -> list[int]:
        """An ordered list of indices of the object's boundaries corresponding to its ``labels``.
        Used exclusively by the visualization engine."""
        return [self.num_systems]

    @property
    def num_systems(self) -> int:
        """The number of systems that the object spans.
        Must be a non-negative integer.
        Should not be set for states."""
        return self._num_systems

    @num_systems.setter
    def num_systems(self, num_systems: int):
        self._num_systems = num_systems

    @property
    def systems(self) -> list[int]:
        """Read-only property containing an ordered list of the numerical indices
        of the object's systems."""
        return [k for k in range(0, self.num_systems)]

    @property
    def targets(self) -> list[int]:
        """An ordered list of the numerical indices of the object's target systems."""
        return self.systems

    @property
    def controls(self) -> list[int]:
        """An ordered list of the numerical indices of the object's control systems."""
        return []

    @property
    def anticontrols(self) -> list[int]:
        """An ordered list of the numerical indices of the object's anticontrol systems."""
        return []

    @property
    def matrix(self) -> mat:
        """The matrix representation of the object.

        Considered read-only (this is strictly enforced by
        :py:class:`~qhronology.quantum.gates.QuantumGate` class and its derivatives),
        though can be (indirectly) mutated by some derived classes
        (such as :py:class:`~qhronology.quantum.states.QuantumState`).
        Not intended to be set directly by the user."""
        return sp.Matrix(self._matrix)

    @matrix.setter
    def matrix(self, matrix: mat):
        self._matrix = matrix
        if hasattr(self, "_debug"):
            if self.debug is True:
                print(repr(self._matrix))

    @property
    def conjugate(self) -> bool:
        """Whether to perform Hermitian conjugation on the object when it is called."""
        return self._conjugate

    @conjugate.setter
    def conjugate(self, conjugate: bool):
        self._conjugate = conjugate

    @property
    def debug(self) -> bool:
        """Whether to print the object's matrix representation (stored in the ``matrix`` property)
        on mutation."""
        return self._debug

    @debug.setter
    def debug(self, debug: bool):
        self._debug = debug
