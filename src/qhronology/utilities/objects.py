# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
The base class for constructing quantum states and gates.
Not intended to be used directly by the user.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations
from typing import Any

import sympy as sp

from qhronology.mechanics.matrices import quantum_object
from qhronology.utilities.classification import (
    COMPATIBILITIES,
    Forms,
    Kinds,
    Shapes,
    arr,
    expr,
    mat,
    matrix_form,
    matrix_shape,
    num,
    sym,
)
from qhronology.utilities.diagrams import VisualizationMixin
from qhronology.utilities.helpers import (
    apply_conditions,
    cast,
    conjugate_transpose,
    count_systems,
    recursively_simplify,
    stringify,
    symbolize_conditions,
    symbolize_expression,
)
from qhronology.utilities.symbolics import SymbolicsProperties


class QuantumObject(VisualizationMixin, SymbolicsProperties):
    """A base class forming the backbone of the QuantumState and QuantumGate classes.

    Not intended to be instantiated directly itself, but rather indirectly via the constructors of its derived classes.
    """

    def __init__(
        self,
        spec: (
            mat
            | arr
            | list[list[num | expr | str]]
            | list[tuple[num | expr | str, int | list[int]]]
            | None
        ) = None,
        form: str | None = None,
        kind: str | None = None,
        dim: int | None = None,
        numerical: bool | None = None,
        array: bool | None = None,
        num_systems: int | None = None,
        symbols: dict[sym | str, dict[str, Any]] | None = None,
        conditions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        conjugate: bool | None = None,
        label: str | None = None,
        notation: str | None = None,
        family: str | None = None,
        debug: bool | None = None,
    ):
        spec = sp.zeros(2) if spec is None else spec
        form = Forms.MATRIX.value if form is None else form
        kind = Kinds.MIXED.value if kind is None else kind
        dim = 2 if dim is None else dim
        numerical = False if numerical is None else numerical
        array = False if array is None else array
        conjugate = False if conjugate is None else conjugate
        matrix = quantum_object(
            spec=spec, form=form, kind=kind, dim=dim, numerical=numerical, array=array
        )
        num_systems = count_systems(matrix, dim) if num_systems is None else num_systems
        label = "A" if label is None else label
        notation = None if notation is None else notation
        family = "PUSH" if family is None else family
        debug = False if debug is None else debug
        SymbolicsProperties.__init__(self, symbols=symbols, conditions=conditions)

        self.spec = spec
        self.form = form
        self.kind = kind
        self.dim = dim
        self.array = array
        self.num_systems = num_systems
        self.conjugate = conjugate
        self.numerical = numerical
        self.label = label
        self.notation = notation
        self.family = family
        self.debug = debug

    def __str__(self) -> str:
        return str(self.notation) + " = " + stringify(self.output(), dim=self.dim)

    def __repr__(self) -> str:
        return repr(self.output())

    @property
    def spec(
        self,
    ) -> (
        mat
        | arr
        | list[list[num | expr | str]]
        | list[tuple[num | expr | str, int | list[int]]]
    ):
        """The specification of the quantum object.
        Provides a complete description of the object in a standard :python:`dim`-dimensional basis.
        """
        return self._spec

    @spec.setter
    def spec(
        self,
        spec: (
            mat
            | arr
            | list[list[num | expr | str]]
            | list[tuple[num | expr | str, int | list[int]]]
        ),
    ):
        self._spec = spec

    @property
    def current(self) -> mat | arr:
        """The current (unprocessed) matrix representation of the quantum object."""
        return self._current

    @current.setter
    def current(self, current: mat | arr):
        self._current = current

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        """Compute the unprocessed matrix representation of the object.

        Arguments
        ---------
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) or integer values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
            Defaults to the value of :python:`self.array`.

        Returns
        -------
        mat | arr
            The unprocessed matrix representation of the object.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        return quantum_object(
            spec=self.spec,
            form=self.form,
            kind=self.kind,
            dim=self.dim,
            numerical=numerical,
            array=array,
        )

    def output(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        conditions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
    ) -> mat | arr:
        """Compute the processed matrix representation of the object.

        Arguments
        ---------
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) or integer values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
            Defaults to the value of :python:`self.array`.
        conditions : list[tuple[num | expr | str, num | expr | str]]
            Algebraic conditions to be applied to the state.
            Defaults to the value of :python:`self.conditions`.
        simplify : bool
            Whether to perform mathematical simplification on the object.
            If :python:`False`, does not simplify.
            Defaults to :python:`False`.
        conjugate : bool
            Whether to perform Hermitian conjugation on the object.
            If :python:`False`, does not conjugate.
            Defaults to the value of :python:`self.conjugate`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the object.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        output = self.matrix(numerical=numerical, array=array_intermediate)
        output = symbolize_expression(output, self.symbols_list)

        # Conditions
        conditions = self.conditions if conditions is None else conditions
        conditions = symbolize_conditions(conditions, self.symbols_list)
        output = apply_conditions(output, conditions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            output = recursively_simplify(output, conditions)

        # Conjugation
        conjugate = self.conjugate if conjugate is None else conjugate
        if conjugate is True:
            output = conjugate_transpose(output)

        return cast(output, numerical=numerical, array=array)

    def print(
        self,
        delimiter: str | None = None,
        product: bool | None = None,
        return_string: bool | None = None,
        numerical: bool | None = None,
        conditions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
    ) -> None | str:
        """Print or return a mathematical expression of the quantum object as a string.

        Note that this method is essentially a wrapper on the :py:meth:`~qhronology.utilities.objects.QuantumObject.output` method, and so includes all of its arguments.

        Arguments
        ---------
        delimiter : str
            A string containing the character(s) with which to delimit (i.e., separate) the values in the ket and/or bra terms in the mathematical expression.
            Defaults to :python:`","`.
        product : bool
            Whether to represent the mathematical expression using tensor products.
            Only applies if the object is a multipartite composition.
            Defaults to :python:`False`.
        return_string : bool
            Whether to return the mathematical expression as a string.
            Defaults to :python:`False`.
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) or integer values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        conditions : list[tuple[num | expr | str, num | expr | str]]
            Algebraic conditions to be applied to the object.
            Defaults to the value of :python:`self.conditions`.
        simplify : bool
            Whether to perform mathematical simplification on the object.
            If :python:`False`, does not simplify.
            Defaults to :python:`False`.
        conjugate : bool
            Whether to perform Hermitian conjugation on the object.
            If :python:`False`, does not conjugate.
            Defaults to the value of :python:`self.conjugate`.

        Returns
        -------
        None
            Returned if :python:`return_string` is :python:`False`.
        str
            The constructed mathematical expression. Returned if :python:`return_string` is :python:`True`.
        """
        expression = (
            str(self.notation)
            + " = "
            + stringify(
                self.output(
                    numerical=numerical,
                    conditions=conditions,
                    simplify=simplify,
                    conjugate=conjugate,
                ),
                dim=self.dim,
                delimiter=delimiter,
                product=product,
            )
        )
        if return_string is True:
            return expression
        else:
            print(expression)

    @property
    def form(self) -> str:
        """The *form* of the object.
        Can be either of :python:`"vector"` or :python:`"matrix"`.
        Only :py:class:`~qhronology.quantum.states.QuantumState` objects can be :python:`"vector"`.
        """
        return matrix_form(self.current)

    @form.setter
    def form(self, form: str):
        if hasattr(self, "_kind"):
            if form == Forms.VECTOR.value and self.kind == Kinds.MIXED.value:
                raise AttributeError(
                    f"""The given :python:`form` ('{form}') is incompatible with the given :python:`kind` ('{self.kind}')."""
                )
        self._form = form

    @property
    def kind(self) -> str:
        """The *kind* of quantum object.
        Can be either of :python:`"mixed"` or :python:`"pure"`."""
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        if kind not in COMPATIBILITIES[self.form]:
            raise AttributeError(
                f"""The given :python:`kind` ('{kind}') is incompatible with the given :python:`form` ('{self.form}')."""
            )
        self._kind = kind

    @property
    def is_vector(self) -> bool:
        """Test for whether the object is a vector.
        Returns :python:`True` if so, otherwise :python:`False`."""
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
                """The :python:`dim` attribute cannot be set after instancing."""
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
        """An ordered list of the object's labels corresponding to its :python:`boundaries`.
        Used exclusively by the visualization engine."""
        return [self.notation]

    @property
    def notation(self) -> str:
        """The formatted string used to represent the object in mathematical expressions.
        When set, overrides the value of the :python:`label` property.
        Must have a non-zero length.
        Not intended to be set by the user in most cases."""
        if self._notation is None:
            if self.is_vector is True:
                if (
                    matrix_shape(self.current) == Shapes.COLUMN.value
                    and self.conjugate == False
                ) or (
                    matrix_shape(self.current) == Shapes.ROW.value
                    and self.conjugate == True
                ):
                    notation = "|" + self.label + "⟩"
                elif (
                    matrix_shape(self.current) == Shapes.ROW.value
                    and self.conjugate == False
                ) or (
                    matrix_shape(self.current) == Shapes.COLUMN.value
                    and self.conjugate == True
                ):
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
    def notation(self, notation: str | None):
        self._notation = notation

    @property
    def family(self) -> str | list[str]:
        """The code of the block element that the object is to be visualized as.
        Not intended to be set by the user."""
        return self._family

    @family.setter
    def family(self, family: str | list[str]):
        self._family = family

    @property
    def boundaries(self) -> list[int]:
        """An ordered list of indices of the object's boundaries corresponding to its :python:`labels`.
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
        """Read-only property containing an ordered list of the numerical indices of the object's systems."""
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
    def conjugate(self) -> bool:
        """Whether to perform Hermitian conjugation on the object when it is called."""
        return self._conjugate

    @conjugate.setter
    def conjugate(self, conjugate: bool):
        self._conjugate = conjugate

    @property
    def numerical(self) -> bool:
        """Whether to cast the object's matrix elements as floating-point values or integer values."""
        return self._numerical

    @numerical.setter
    def numerical(self, numerical: bool):
        self._numerical = numerical

    @property
    def array(self) -> bool:
        """Whether to cast the object's matrix as a NumPy array or SymPy matrix."""
        return self._array

    @array.setter
    def array(self, array: bool):
        self._array = array

    @property
    def debug(self) -> bool:
        """Whether to print the object's matrix representation (stored in the :python:`matrix` property) on mutation."""
        return self._debug

    @debug.setter
    def debug(self, debug: bool):
        self._debug = debug
