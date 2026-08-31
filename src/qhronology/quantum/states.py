# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
Classes for the creation of quantum states.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations
from typing import Any

from qhronology.mechanics.matrices import quantum_object
from qhronology.mechanics.operations import OperationsMixin, normalize
from qhronology.mechanics.quantities import QuantitiesMixin
from qhronology.utilities.classification import Forms, Kinds, arr, expr, mat, num, sym
from qhronology.utilities.diagrams import Families
from qhronology.utilities.helpers import (
    apply_substitutions,
    cast,
    conjugate_transpose,
    count_systems,
    fix_arguments,
    recursively_simplify,
    stringify,
    symbolize_substitutions,
    symbolize_expression,
)
from qhronology.utilities.objects import QuantumObject


class QuantumState(QuantitiesMixin, OperationsMixin, QuantumObject):
    """A class for creating quantum states and storing their metadata.

    Instances provide complete descriptions of both vector and matrix quantum states, along with various associated attributes (such as mathematical conditions, including normalization).
    The internal state of the class is expressly mutable, and a selection of useful methods are provided with which it can be manipulated and otherwise transformed in various quantum-mechanically significant ways.
    This includes:

    - normalization
    - partial trace
    - measurement
    - postselection

    Arguments
    ---------
    spec : mat | arr | list[list[num | expr | str]] | list[tuple[num | expr | str, int | list[int]]]
        The specification of the quantum state. Provides a description of the state's values in a standard :python:`dim`-dimensional basis.
        Can be one of:

        - a SymPy matrix (:python:`mat`)
        - a NumPy array (:python:`arr`)
        - a list of lists of numerical, symbolic, or string expressions that collectively describe a matrix (:python:`list[list[num | expr | str]]`)
        - a list of 2-tuples of numerical, symbolic, or string coefficients and their respective number-basis specifications (:python:`list[tuple[num | expr | str, int | list[int]]]`)

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
    numerical : bool
        Whether to cast the state's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the state's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.
    symbols : dict[sym | str, dict[str, Any]]
        A dictionary in which the keys are individual symbols (usually found within the state specification :python:`spec`) and the values are dictionaries of their respective SymPy keyword-argument :python:`assumptions`.
        Defaults to :python:`{}`.
    substitutions : list[tuple[num | expr | str, num | expr | str]]
        A list of 2-tuples of substitutions to be applied to the state.
        All instances of the expression in each tuple's first element are replaced by the expression in the respective second element.
        This uses the same format as the SymPy :python:`subs()` method.
        Defaults to :python:`[]`.
    simplification : bool
        Whether to perform mathematical simplification on the state when it is called.
        If :python:`False`, does not simplify.
        Defaults to :python:`False`.
    conjugation : bool
        Whether to perform Hermitian conjugation on the state when it is called.
        If :python:`False`, does not conjugate.
        Defaults to :python:`False`.
    norm : bool | num | expr | str
        The value to which the state is normalized.
        If :python:`True`, normalizes to a value of :math:`1`.
        If :python:`False`, does not normalize.
        Defaults to :python:`False`.
    label : str
        The unformatted string used to represent the state in mathematical expressions.
        Must have a non-zero length.
        Defaults to :python:`"ρ"` (if :python:`form == "matrix"`) or :python:`"ψ"` (if :python:`form == "vector"`).
    notation : str
        The formatted string used to represent the state in mathematical expressions.
        When not :python:`None`, overrides the value passed to :python:`label`.
        Must have a non-zero length.
        Not intended to be set by the user in most cases.
        Defaults to :python:`None`.
    family : str
        A string expressing the kind of block element for which the object is to be visualized.
        Not intended to be set by the user.
        Defaults to :python:`"LSTICK"`.
    debug : bool
        Whether to print the internal state (held in :python:`matrix`) on change.
        If :python:`False`, does not print.
        Defaults to :python:`False`.
    """

    def __init__(
        self,
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
        symbols: dict[sym | str, dict[str, Any]] | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        family: str | None = None,
        debug: bool | None = None,
    ):
        form = Forms.MATRIX.value if form is None else form
        if kind is None:
            kind = Kinds.PURE.value if form == Forms.VECTOR.value else Kinds.MIXED.value
        dim = 2 if dim is None else dim
        if label is None:
            label = "ρ"
            if form == Forms.VECTOR.value or kind == Kinds.PURE.value:
                label = "ψ"
        family = Families.LSTICK.value if family is None else family
        norm = False if norm is None else norm

        self.norm = norm
        self.current = quantum_object(
            spec=spec,
            form=form,
            kind=kind,
            dim=dim,
            numerical=numerical,
            array=array,
        )

        QuantumObject.__init__(
            self,
            spec=spec,
            form=form,
            kind=kind,
            dim=dim,
            numerical=numerical,
            array=array,
            symbols=symbols,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            label=label,
            notation=notation,
            family=family,
            debug=debug,
        )

    @property
    def current(self) -> mat | arr:
        """The current (unprocessed) matrix representation of the quantum state."""
        return self._current

    @current.setter
    def current(self, current: mat | arr):
        self._current = current

    @property
    def norm(self) -> bool | num | expr | str:
        """The value to which the state is normalized.
        If :python:`True`, normalizes to a value of :math:`1`.
        If :python:`False`, does not normalize.

        Examples of valid values include:

        - :python:`1/2`
        - :python:`"1/d"`
        - :python:`"a*conjugate(a) + b*conjugate(b)"`
        """
        return self._norm

    @norm.setter
    def norm(self, norm: bool | num | expr | str):
        self._norm = norm

    @property
    def num_systems(self) -> int:
        """Read-only property containing the number of systems which the state spans.
        The current value is calculated from the state's matrix representation and its dimensionality :python:`dim`.
        """
        return count_systems(self.current, self.dim)

    @num_systems.setter
    def num_systems(self, num_systems: int):
        pass

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        """Compute the unprocessed matrix representation of the state.

        Arguments
        ---------
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
            Defaults to the value of :python:`self.array`.

        Returns
        -------
        mat | arr
            The unprocessed matrix representation of the state.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        return cast(self.current, numerical=numerical, array=array)

    def output(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
    ) -> mat | arr:
        """Compute the processed matrix representation of the state.

        Arguments
        ---------
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
            Defaults to the value of :python:`self.array`.
        substitutions : list[tuple[num | expr | str, num | expr | str]]
            Algebraic substitutions to be applied to the state.
            Defaults to the value of :python:`self.substitutions`.
        simplification : bool
            Whether to perform mathematical simplification on the state.
            If :python:`False`, does not simplify.
            Defaults to the value of :python:`self.simplification`.
        conjugation : bool
            Whether to perform Hermitian conjugation on the state.
            If :python:`False`, does not conjugate.
            Defaults to the value of :python:`self.conjugation`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`False`, does not normalize.
            Defaults to the value of :python:`self.norm`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the object.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        state = self.matrix(numerical=numerical, array=array_intermediate)
        state = symbolize_expression(state, self.symbols_list)

        # Normalization
        norm = self.norm if norm is None else norm
        norm = 1 if norm is True else norm
        if norm is not False:
            state = normalize(state, norm=norm)

        # Substitutions
        substitutions = self.substitutions if substitutions is None else substitutions
        substitutions = symbolize_substitutions(substitutions, self.symbols_list)
        state = apply_substitutions(state, substitutions)

        # Simplification
        simplification = self.simplification if simplification is None else simplification
        if simplification is True:
            state = recursively_simplify(state, substitutions)

        # Conjugation
        conjugation = self.conjugation if conjugation is None else conjugation
        if conjugation is True:
            state = conjugate_transpose(state)

        return cast(state, numerical=numerical, array=array)

    def print(
        self,
        delimiter: str | None = None,
        product: bool | None = None,
        return_string: bool | None = None,
        numerical: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
    ) -> None | str:
        """Print or return a mathematical expression of the quantum state as a string.

        Note that this method is essentially a wrapper on the :py:meth:`~qhronology.quantum.states.QuantumState.output` method, and so includes its arguments.

        Arguments
        ---------
        delimiter : str
            A string containing the character(s) with which to delimit (i.e., separate) the values in the ket and/or bra terms in the mathematical expression.
            Defaults to :python:`","`.
        product : bool
            Whether to represent the mathematical expression using tensor products.
            Only applies if the state is a multipartite composition.
            Defaults to :python:`False`.
        return_string : bool
            Whether to return the mathematical expression as a string.
            Defaults to :python:`False`.
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        substitutions : list[tuple[num | expr | str, num | expr | str]]
            Algebraic substitutions to be applied to the state.
            Defaults to the value of :python:`self.substitutions`.
        simplification : bool
            Whether to perform mathematical simplification on the state.
            If :python:`False`, does not simplify.
            Defaults to the value of :python:`self.simplification`.
        conjugation : bool
            Whether to perform Hermitian conjugation on the state.
            If :python:`False`, does not conjugate.
            Defaults to the value of :python:`self.conjugation`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`False`, does not normalize.
            Defaults to the value of :python:`self.norm`.

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
                    substitutions=substitutions,
                    simplification=simplification,
                    conjugation=conjugation,
                    norm=norm,
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

    def reset(self):
        """Reset the quantum state's internal matrix state (specifically its :python:`current` property) to its original value at instantiation.

        Note
        ----
        This resets only the :python:`current` property of the instance.
        All other attributes and properties are unchanged.
        """
        self.current = quantum_object(
            spec=self.spec,
            form=self._form,
            kind=self._kind,
            dim=self.dim,
            numerical=self.numerical,
            array=self.array,
        )


class VectorState(QuantumState):
    """A specialized subclass for creating *vector* states and storing their metadata.

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class, and so inherits all of its attributes, properties, and methods.
    The distinction is that this :python:`VectorState` class fixes both the :python:`form` and :python:`kind` arguments to the values of :python:`"vector"` and :python:`"pure"`, respectively, at instantiation.
    This means that neither :python:`*args` or :python:`**kwargs` must contain these arguments.
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = fix_arguments(
            args,
            kwargs,
            QuantumState,
            [("form", Forms.VECTOR.value), ("kind", Kinds.PURE.value)],
        )
        super().__init__(*args, **kwargs)


class MatrixState(QuantumState):
    """A specialized subclass for creating *matrix* states and storing their metadata.

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class, and so inherits all of its attributes, properties, and methods.
    The distinction is that this :python:`MatrixState` class fixes the :python:`form` argument to a value of :python:`"matrix"` at instantiation.
    This means that neither :python:`*args` or :python:`**kwargs` must contain this argument.
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = fix_arguments(
            args, kwargs, QuantumState, [("form", Forms.MATRIX.value)]
        )
        super().__init__(*args, **kwargs)


class PureState(QuantumState):
    """A specialized subclass for creating *pure* states and storing their metadata.

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class, and so inherits all of its attributes, properties, and methods.
    The distinction is that this :python:`PureState` class fixes the :python:`kind` argument to a value of :python:`"pure"` at instantiation.
    This means that neither :python:`*args` or :python:`**kwargs` must contain this argument.
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = fix_arguments(
            args, kwargs, QuantumState, [("kind", Kinds.PURE.value)]
        )
        super().__init__(*args, **kwargs)


class MixedState(QuantumState):
    """A specialized subclass for creating *mixed* states and storing their metadata.

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class, and so inherits all of its attributes, properties, and methods.
    The distinction is that this :python:`MixedState` class fixes both the :python:`form` and :python:`kind` arguments to the values of :python:`"matrix"` and :python:`"mixed"`, respectively, at instantiation.
    This means that neither :python:`*args` or :python:`**kwargs` must contain these arguments.
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = fix_arguments(
            args,
            kwargs,
            QuantumState,
            [("form", Forms.MATRIX.value), ("kind", Kinds.MIXED.value)],
        )
        super().__init__(*args, **kwargs)
