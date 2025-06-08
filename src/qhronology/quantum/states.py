# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
Classes for the creation of quantum states.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

from typing import Any

from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import (
    num,
    sym,
    mat,
    arr,
    Forms,
    Kinds,
    COMPATIBILITIES,
)
from qhronology.utilities.diagrams import Families
from qhronology.utilities.helpers import (
    symbolize_expression,
    symbolize_tuples,
    recursively_simplify,
    count_systems,
    fix_arguments,
)
from qhronology.utilities.objects import QuantumObject

from qhronology.mechanics.matrices import quantum_state
from qhronology.mechanics.operations import normalize, OperationsMixin
from qhronology.mechanics.quantities import QuantitiesMixin


class QuantumState(QuantitiesMixin, OperationsMixin, QuantumObject):
    """A class for creating quantum states and storing their metadata.

    Instances provide complete descriptions of both vector and matrix quantum states, along with
    various associated attributes (such as mathematical conditions, including normalization).
    The internal state of the class is expressly mutable, and a selection of useful methods are
    provided with which the state can be manipulated and otherwise transformed in various
    quantum-mechanically significant ways. This includes:

    - normalization
    - (partial) trace
    - measurement
    - postselection

    Arguments
    ---------
    spec
        The specification of the quantum state. Provides a complete description of the state's
        values in a standard ``dim``-dimensional basis. Can be one of:

        - a SymPy matrix (``mat``)
        - a NumPy array (``arr``)
        - a list of lists of numerical, symbolic, or string expressions (that collectively specify
          a matrix) (``list[list[num | sym | str]]``)
        - a list of 2-tuples of numerical, symbolic, or string coefficients and their respective
          number-basis specifications (``list[tuple[num | sym | str, int | list[int]]]``)

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
    symbols : dict[sym | str, dict[str, Any]]
        A dictionary in which the keys are individual symbols (usually found within the state
        specification ``spec``) and the values are dictionaries of their respective SymPy
        keyword-argument ``assumptions``.
        Defaults to ``{}``.
    conditions : list[tuple[num | sym | str, num | sym | str]]
        A list of :math:`2`-tuples of conditions to be applied to the state.
        All instances of the expression in each tuple's first element are replaced by the
        expression in the respective second element.
        This uses the same format as the SymPy ``subs()`` method.
        The order in which they are applied is simply their order in the list.
        Defaults to ``[]``.
    conjugate : bool
        Whether to perform Hermitian conjugation on the state when it is called.
        Defaults to ``False``.
    norm : bool | num | sym | str
        The value to which the state is normalized.
        If ``True``, normalizes to a value of :math:`1`.
        If ``False``, does not normalize.
        Defaults to ``False``.
    label : str
        The unformatted string used to represent the state in mathematical expressions.
        Must have a non-zero length.
        Defaults to ``"ρ"`` (if ``form == "matrix"``) or ``"ψ"`` (if ``form == "vector"``).
    notation : str
        The formatted string used to represent the state in mathematical expressions.
        When not ``None``, overrides the value passed to ``label``.
        Must have a non-zero length.
        Not intended to be set by the user in most cases.
        Defaults to ``None``.
    family : str
        A string expressing the kind of block element for which the object is to be visualized.
        Not intended to be set by the user.
        Defaults to ``"LSTICK"``.
    debug : bool
        Whether to print the internal state (held in ``matrix``) on change.
        Defaults to ``False``.
    """

    def __init__(
        self,
        spec: (
            mat
            | arr
            | list[list[num | sym | str]]
            | list[tuple[num | sym | str, int | list[int]]]
        ),
        form: str | None = None,
        kind: str | None = None,
        dim: int | None = None,
        symbols: dict[sym | str, dict[str, Any]] | None = None,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        conjugate: bool | None = None,
        norm: bool | num | sym | str | None = None,
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

        self.kind = kind
        self.spec = spec
        self.norm = norm

        matrix = quantum_state(spec=spec, form=form, kind=kind, dim=dim)

        QuantumObject.__init__(
            self,
            form=form,
            dim=dim,
            matrix=matrix,
            symbols=symbols,
            conditions=conditions,
            conjugate=conjugate,
            label=label,
            notation=notation,
            family=family,
            debug=debug,
        )

    @property
    def kind(self) -> str:
        """The *kind* of quantum state.
        Can be either of ``"mixed"`` or ``"pure"``."""
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        if hasattr(self, "_form"):
            if kind not in COMPATIBILITIES[self.form]:
                raise AttributeError(
                    f"The given ``kind`` ('{kind}') is incompatible with the given ``form`` \
                    ('{self.form}')."
                )
        self._kind = kind

    @property
    def spec(
        self,
    ) -> (
        mat
        | arr
        | list[list[num | sym | str]]
        | list[tuple[num | sym | str, int | list[int]]]
    ):
        """The matrix representation of the quantum state.
        Provides a complete description of the state in a standard ``dim``-dimensional basis.
        """
        return self._spec

    @spec.setter
    def spec(
        self,
        spec: (
            mat
            | arr
            | list[list[num | sym | str]]
            | list[tuple[num | sym | str, int | list[int]]]
        ),
    ):
        self._spec = spec

    @property
    def norm(self) -> bool | num | sym | str:
        """The value to which the state is normalized.
        If ``True``, normalizes to a value of :math:`1`.
        If ``False``, does not normalize.

        Examples of valid values include:

        - ``1/2``
        - ``"1/d"``
        - ``"a*conjugate(a) + b*conjugate(b)"``
        """
        return self._norm

    @norm.setter
    def norm(self, norm: bool | num | sym | str):
        self._norm = norm

    @property
    def num_systems(self) -> int:
        """Read-only property containing the number of systems which the state spans.
        The current value is calculated from the state's matrix representation and its
        dimensionality ``dim``.
        """
        return count_systems(self.matrix, self.dim)

    @num_systems.setter
    def num_systems(self, num_systems: int):
        pass

    def output(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        norm: bool | num | sym | str | None = None,
    ) -> mat:
        """Construct the state's matrix representation, perform any necessary transformations on it,
        and return it.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the state.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the state.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the state.
            If ``False``, does not conjugate.
            Defaults to the value of ``self.conjugate``.
        norm : bool | num | sym | str
            The value to which the state is normalized.
            If ``False``, does not normalize.
            Defaults to the value of ``self.norm``.

        Returns
        -------
        mat
            The matrix or vector representation of the quantum state.
        """
        state = self.matrix
        state = symbolize_expression(state, self.symbols_list)

        # Normalization
        norm = self.norm if norm is None else norm
        norm = 1 if norm is True else norm
        if norm is not False:
            state = normalize(state, norm=norm)

        # Conditions
        conditions = self.conditions if conditions is None else conditions
        conditions = symbolize_tuples(conditions, self.symbols_list)
        state = state.subs(conditions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            state = recursively_simplify(state, conditions)

        # Conjugation
        conjugate = self.conjugate if conjugate is None else conjugate
        if conjugate is True:
            state = Dagger(state)

        return state

    def reset(self):
        """Reset the quantum state's internal matrix state (specifically its ``matrix`` property)
        to its original value at instantiation.

        Note
        ----
        This reset only the ``matrix`` property of the instance.
        All other attributes and properties are unchanged.
        """
        self.matrix = quantum_state(
            spec=self.spec, form=self._form, kind=self._kind, dim=self.dim
        )


class VectorState(QuantumState):
    """A specialized subclass for creating *vector* states and storing their metadata.

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class,
    and so inherits all of its attributes, properties, and methods.
    The distinction is that this ``VectorState`` class fixes both the ``form`` and ``kind``
    arguments to the values of ``"vector"`` and ``"pure"``, respectively, at instantiation.
    This means that neither ``*args`` or ``**kwargs`` must contain these arguments.

    Examples
    --------
    >>> qubit_vector = VectorState(spec=[(1, [0]), (1, [1])], norm=1)
    >>> qubit_vector.print()
    |ψ⟩ = sqrt(2)/2|0⟩ + sqrt(2)/2|1⟩
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

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class,
    and so inherits all of its attributes, properties, and methods.
    The distinction is that this ``MatrixState`` class fixes the ``form`` argument to a value of
    ``"matrix"`` at instantiation.
    This means that neither ``*args`` or ``**kwargs`` must contain this argument.

    Examples
    --------
    >>> qubit_matrix_pure = MatrixState(spec=[(1, [0]), (1, [1])], kind="pure", norm=1)
    >>> qubit_matrix_pure.print()
    |ψ⟩⟨ψ| = 1/2|0⟩⟨0| + 1/2|0⟩⟨1| + 1/2|1⟩⟨0| + 1/2|1⟩⟨1|

    >>> qubit_matrix_mixed = MatrixState(spec=[(1, [0]), (1, [1])], kind="mixed", norm=1)
    >>> qubit_matrix_mixed.print()
    ρ = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = fix_arguments(
            args, kwargs, QuantumState, [("form", Forms.MATRIX.value)]
        )
        super().__init__(*args, **kwargs)


class PureState(QuantumState):
    """A specialized subclass for creating *pure* states and storing their metadata.

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class,
    and so inherits all of its attributes, properties, and methods. The distinction is that
    this ``PureState`` class fixes the ``kind`` argument to a value of ``"pure"`` at instantiation.
    This means that neither ``*args`` or ``**kwargs`` must contain this argument.

    Examples
    --------
    >>> qubit_pure_vector = PureState(spec=[(1, [0]), (1, [1])], form="vector", norm=1)
    >>> qubit_pure_vector.print()
    |ψ⟩ = sqrt(2)/2|0⟩ + sqrt(2)/2|1⟩

    >>> qubit_pure_matrix = PureState(spec=[(1, [0]), (1, [1])], form="matrix", norm=1)
    >>> qubit_pure_matrix.print()
    |ψ⟩⟨ψ| = 1/2|0⟩⟨0| + 1/2|0⟩⟨1| + 1/2|1⟩⟨0| + 1/2|1⟩⟨1|
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = fix_arguments(
            args, kwargs, QuantumState, [("kind", Kinds.PURE.value)]
        )
        super().__init__(*args, **kwargs)


class MixedState(QuantumState):
    """A specialized subclass for creating *mixed* states and storing their metadata.

    This is a wrapper on the :py:class:`~qhronology.quantum.states.QuantumState` class,
    and so inherits all of its attributes, properties, and methods. The distinction is that
    this ``MixedState`` class fixes both the ``form`` and ``kind`` arguments to the values of
    ``"matrix"`` and ``"mixed"``, respectively, at instantiation.
    This means that neither ``*args`` or ``**kwargs`` must contain these arguments.

    Examples
    --------
    >>> qubit_mixed = MixedState(spec=[(1, [0]), (1, [1])], norm=1)
    >>> qubit_mixed.print()
    ρ = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = fix_arguments(
            args,
            kwargs,
            QuantumState,
            [("form", Forms.MATRIX.value), ("kind", Kinds.MIXED.value)],
        )
        super().__init__(*args, **kwargs)
