# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
Classes for the creation of quantum gates.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

import itertools
from typing import Any

import sympy as sp
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import num, sym, mat, arr, Forms
from qhronology.utilities.diagrams import Families
from qhronology.utilities.helpers import (
    flatten_list,
    check_systems_conflicts,
    symbolize_expression,
    recursively_simplify,
    default_arguments,
    fix_arguments,
    count_systems,
    arrange,
    symbolize_tuples,
    extract_matrix,
    stringify,
)
from qhronology.utilities.objects import QuantumObject

from qhronology.mechanics.matrices import ket, bra
from qhronology.mechanics.operations import densify


class QuantumGate(QuantumObject):
    """A class for creating quantum gates and storing their metadata.

    This class forms the base upon which all quantum gates are built.
    Instances of this base class and its derivatives (subclasses) provide complete descriptions of
    quantum gates.
    This means that they describe a complete vertical column (or "slice") in the quantum
    circuitry picturalism, including control nodes, anticontrol nodes, empty wires, and the
    (unitary) gate operator itself.
    The details of any algebraic symbols, mathematical conditions, and visualization labels are
    also recorded.
    Note that, unlike the internal matrix representations contained within instances of the
    :py:class:`~qhronology.quantum.states.QuantumState` class (and its derivatives),
    the matrix representations of subclass instances of
    :py:class:`~qhronology.quantum.gates.QuantumGate` are *not* mutable.

    Arguments
    ---------
    spec : mat | arr | list[list[num | sym | str]]
        The specification of the quantum gate's matrix representation in a standard
        ``dim``-dimensional basis.
        Can be one of:

        - a SymPy matrix (``mat``)
        - a NumPy array (``arr``)
        - a list of lists of numerical, symbolic, or string expressions that collectively specify
          a matrix (``list[list[num | sym | str]]``)

        Defaults to the single-system ``dim``-dimensional Identity operator.
    targets : list[int]
        The numerical indices of the subsystems on which the gate elements reside.
        Defaults to ``[0]`` (if ``num_systems`` is ``None``)
        or ``[i for i in range(num_systems)]`` (if ``num_systems`` is not ``None``).
    controls : list[int]
        The numerical indices of the subsystems on which control nodes reside.
        Defaults to ``[]``.
    anticontrols : list[int]
        The numerical indices of the subsystems on which anticontrol nodes reside.
        Defaults to ``[]``.
    num_systems : int
        The (total) number of systems which the gate spans.
        Must be a non-negative integer.
        Defaults to
        ``max(targets + controls + anticontrols + [count_systems(sp.Matrix(spec), dim)]) + 1``.
    dim : int
        The dimensionality of the quantum gate's Hilbert space.
        Must be a non-negative integer.
        Defaults to ``2``.
    symbols : dict[sym | str, dict[str, Any]]
        A dictionary in which the keys are individual symbols (usually found within the gate
        specification ``spec``) and the values are dictionaries of their respective SymPy
        keyword-argument ``assumptions``.
        Defaults to ``{}``.
    conditions : list[tuple[num | sym | str, num | sym | str]]
        A list of :math:`2`-tuples of conditions to be applied to the gate.
        All instances of the expression in each tuple's first element are replaced by the
        expression in the respective second element.
        This uses the same format as the SymPy ``subs()`` method.
        The order in which they are applied is simply their order in the list.
        Defaults to ``[]``.
    conjugate : bool
        Whether to perform Hermitian conjugation on the gate when it is called.
        Defaults to ``False``.
    exponent : num | sym | str
        A numerical or string representation of a scalar value to which gate's operator (residing
        on ``targets``) is exponentiated.
        Must be a non-negative integer.
        Useful for computing powers of gates (such as PSWAP), but is only guaranteed to return a
        valid power of a gate if its corresponding matrix representation (e.g., :math:`\\op{A}`)
        is involutory (i.e., :math:`\\op{A}^2 = \\Identity`).
        Defaults to ``1``.
    coefficient : num | sym | str
        A numerical or string representation of a scalar value by which the gate's matrix
        (occupying ``targets``) is multiplied.
        Performed after exponentiation.
        Useful for multiplying the gate by a phase factor.
        Defaults to ``1``.
    label : str
        The unformatted string used to represent the gate in mathematical expressions.
        Defaults to ``"U"``.
    notation : str
        The formatted string used to represent the gate in mathematical expressions.
        When not ``None``, overrides the value passed to ``label``.
        Not intended to be set by the user in most cases.
        Defaults to ``None``.
    family : str
        A string expressing the kind of block element for which the gate is to be visualized.
        Not intended to be set by the user.
        Defaults to ``"GATE"``.

    Note
    ----
    The indices specified in ``targets``, ``controls``, and ``anticontrols`` must be distinct.
    """

    def __init__(
        self,
        spec: mat | arr | list[list[num | sym | str]] | None,
        targets: list[int] | None = None,
        controls: list[int] | None = None,
        anticontrols: list[int] | None = None,
        num_systems: int | None = None,
        dim: int | None = None,
        symbols: dict | None = None,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        conjugate: bool | None = None,
        exponent: num | sym | str | None = None,
        coefficient: num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        family: str | None = None,
    ):
        targets = [0] if targets is None else targets
        controls = [] if controls is None else controls
        anticontrols = [] if anticontrols is None else anticontrols
        dim = 2 if dim is None else dim
        spec_num_systems = 0
        if spec is None:
            spec = sp.eye(dim)
        else:
            spec_num_systems = count_systems(sp.Matrix(spec), dim)
        num_systems = (
            (max(spec_num_systems, max(targets + controls + anticontrols) + 1))
            if num_systems is None
            else num_systems
        )
        if (
            any(len(indices) != 0 for indices in [targets, controls, anticontrols])
            is False
        ):
            targets = [n for n in range(0, num_systems)]

        exponent = 1 if exponent is None else exponent
        coefficient = 1 if coefficient is None else coefficient
        label = "U" if label is None else label
        family = Families.GATE.value if family is None else family

        # Automatically resize
        num_systems = max(flatten_list([num_systems, targets, controls, anticontrols]))

        QuantumObject.__init__(
            self,
            form=Forms.MATRIX.value,
            dim=dim,
            num_systems=num_systems,
            symbols=symbols,
            conditions=conditions,
            conjugate=conjugate,
            label=label,
            notation=notation,
            family=family,
            debug=False,
        )

        self.spec = spec
        self.targets = targets
        self.controls = controls
        self.anticontrols = anticontrols
        self.exponent = exponent
        self.coefficient = coefficient

    @property
    def spec(self) -> mat | arr | list[list[num | sym | str]]:
        """The matrix representation of the quantum gate's operator.
        Provides a complete description of the operator in a standard ``dim``-dimensional basis.
        """
        return self._spec

    @spec.setter
    def spec(self, spec: mat | arr | list[list[num | sym | str]]):
        self._spec = spec

    @property
    def matrix(self) -> mat:
        """The matrix representation of the total gate across all of its systems."""
        operator = sp.Matrix(self.spec)
        identity = sp.eye(self.dim)
        ordered = []
        for i in self.systems:
            if i not in self.targets:
                ordered.append(identity)
            if i == min(self.targets):
                ordered.append(operator)
        matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass

    @property
    def targets(self) -> list[int]:
        """The numerical indices of the subsystems on which the gate elements reside."""
        return list(set(self._targets))

    @targets.setter
    def targets(self, targets: list[int]):
        if (
            hasattr(self, "_controls") is True
            and hasattr(self, "_anticontrols") is True
        ):
            if (
                check_systems_conflicts(targets, self.controls, self.anticontrols)
                is True
            ):
                raise ValueError(
                    "The ``targets``, ``controls``, and ``anticontrols`` lists cannot have any \
                    elements in common."
                )
        self._targets = targets

    @property
    def controls(self) -> list[int]:
        """The numerical indices of the subsystems on which control nodes reside.
        
        For example, a controlled-:math:`\\Unitary` gate in :math:`\\Dimension` dimensions
        takes the form

        .. math::

           \\begin{aligned}
               \\Control^{0} \\Unitary^{1} &= \\sum\\limits_{k=0}^{\\Dimension - 1} \\ket{k}\\bra{k}\\otimes\\Unitary^{k} \\\\
               &= \\ket{0}\\bra{0}\\otimes\\Identity + \\ket{1}\\bra{1}\\otimes\\Unitary
                   + \\ket{2}\\bra{2}\\otimes\\Unitary^{2} + \\ldots
                   + \\ket{\\Dimension - 1}\\bra{\\Dimension - 1}\\otimes\\Unitary^{\\Dimension - 1}
            \\end{aligned}
        """
        return list(set(self._controls))

    @controls.setter
    def controls(self, controls: list[int]):
        controls = flatten_list(list(controls))
        if hasattr(self, "_controls") is False:
            self._controls = []
        if hasattr(self, "_anticontrols") is False:
            self._anticontrols = []
        if check_systems_conflicts(self.targets, controls, self.anticontrols) is True:
            raise ValueError(
                "The ``targets``, ``controls``, and ``anticontrols`` lists cannot have any \
                elements in common."
            )
        self._controls = sorted(list(set(controls)))

    @property
    def anticontrols(self) -> list[int]:
        """The numerical indices of the subsystems on which anticontrol nodes reside.

        For example, an anticontrolled-:math:`\\Unitary` gate in :math:`\\Dimension` dimensions
        takes the form

        .. math::

           \\begin{aligned}
               \\Anticontrol^{0} \\Unitary^{1} &= \\sum\\limits_{k=0}^{\\Dimension - 1} \\ket{k}\\bra{k}\\otimes\\Unitary^{\\Dimension - 1 - k} \\\\
               &= \\ket{0}\\bra{0}\\otimes\\Unitary^{\\Dimension - 1} + \\ket{1}\\bra{1}\\otimes\\Unitary^{\\Dimension - 2}
                   + \\ket{2}\\bra{2}\\otimes\\Unitary^{\\Dimension - 3} + \\ldots
                   + \\ket{\\Dimension - 1}\\bra{\\Dimension - 1}\\otimes\\Identity
           \\end{aligned}
        """
        return list(set(self._anticontrols))

    @anticontrols.setter
    def anticontrols(self, anticontrols: list[int]):
        anticontrols = flatten_list(list(anticontrols))
        if hasattr(self, "_controls") is False:
            self._controls = []
        if hasattr(self, "_anticontrols") is False:
            self._anticontrols = []
        if check_systems_conflicts(self.targets, self.controls, anticontrols) is True:
            raise ValueError(
                "The ``targets``, ``controls``, and ``anticontrols`` lists cannot have any \
                elements in common."
            )
        self._anticontrols = sorted(list(set(anticontrols)))

    @property
    def boundaries(self) -> list[int]:
        """An ordered list of indices of the object's boundaries corresponding to its ``labels``.
        Used exclusively by the visualization engine."""
        return [max(flatten_list([self.targets, self.controls, self.anticontrols]))]

    @property
    def exponent(self) -> num | sym | str:
        """A numerical or string representation of a scalar value specifying the value to which
        the gate's matrix representation is exponentiated.
        Is guaranteed to produce valid powers only for involutory matrices.

        For an involutory matrix :math:`\\op{A}`, that is :math:`\\op{A}^2 = \\Identity` (where
        :math:`\\Identity` is the identity matrix), we have the identity,

        .. math::

           \\exp[\\eye x \\op{A}] = \\cos(x)\\Identity + \\eye\\sin(x)\\op{A},

        for any :math:`x \\in \\Complexes`. In the case of :math:`x = -\\frac{\\pi}{2}`, this becomes

        .. math::

           \\exp\\Bigl[-\\eye\\frac{\\pi}{2}\\op{A}\\Bigr] = -\\eye\\op{A},
        
        which can be rearranged to give

        .. math::

           \\begin{aligned}
               \\op{A} &= \\eye \\exp\\Bigl[-\\eye\\frac{\\pi}{2}\\op{A}\\Bigr] \\\\
               &= \\exp\\Bigl[\\eye\\frac{\\pi}{2}\\Bigr] \\cdot
                   \\exp\\Bigl[-\\eye\\frac{\\pi}{2}\\op{A}\\Bigr].
           \\end{aligned}

        Simply taking this expression to an arbitrary power :math:`p \\in \\mathbb{C}` thus yields
        the identity

        .. math::

           \\begin{aligned}
               \\op{A}^p &= \\exp\\Bigl[\\eye\\frac{\\pi}{2} p\\Bigr] \\cdot
                   \\exp\\Bigl[-\\eye\\frac{\\pi}{2} p \\op{A}\\Bigr] \\\\
               &= \\exp\\Bigl[\\eye\\frac{\\pi}{2} p\\Bigr]
                   \\Bigl[\\cos\\Bigl(\\frac{\\pi}{2} p\\Bigr) \\Identity
                   - \\eye \\sin\\Bigl(\\frac{\\pi}{2} p\\Bigr) \\op{A}\\Bigr] \\\\
               &= \\frac{1 + \\e^{\\eye \\pi p}}{2} \\Identity +
                   \\frac{1 - \\e^{\\eye \\pi p}}{2} \\op{A}.
           \\end{aligned}
        """
        return self._exponent

    @exponent.setter
    def exponent(self, exponent: num | sym | str):
        self._exponent = exponent

    @property
    def coefficient(self) -> num | sym | str:
        """A numerical or string representation of a scalar value by which the gate's matrix
        (occupying ``targets``) is multiplied."""
        return self._coefficient

    @coefficient.setter
    def coefficient(self, coefficient: num | sym | str):
        self._coefficient = coefficient

    def output(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        exponent: bool | num | sym | str | None = None,
        coefficient: bool | num | sym | str | None = None,
    ) -> mat:
        """Construct the gate and return its matrix representation.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the gate.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the gate.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the gate.
            If ``False``, does not conjugate.
            Defaults to the value of ``self.conjugate``.
        exponent : bool | num | sym | str
            The scalar value by which the gate's matrix representation is exponentiated.
            If ``False``, does not exponentiate.
            Defaults to the value of ``self.exponent``.
        coefficient : num | sym | str
            The scalar value by which the gate's matrix representation is multiplied.
            If ``False``, does not multiply the gate by the coefficient.
            Defaults to the value of ``self.coefficient``.

        Returns
        -------
        mat
            The constructed quantum gate.
        """
        gate = self.matrix

        # Exponentiate
        if exponent is None or exponent is True:
            exponent = self.exponent
        if exponent != 1 and exponent is not False:
            exponent = symbolize_expression(exponent, self.symbols_list)
            gate = ((1 + sp.exp(sp.I * sp.pi * exponent)) / 2) * sp.eye(
                self.dim**self.num_systems
            ) + ((1 - sp.exp(sp.I * sp.pi * exponent)) / 2) * gate

        # Coefficient
        if coefficient is None or coefficient is True:
            coefficient = self.coefficient
        if coefficient is not False:
            coefficient = symbolize_expression(self.coefficient, self.symbols_list)
        gate *= coefficient

        gate = symbolize_expression(gate, self.symbols_list)

        controllers = self.controls + self.anticontrols
        if len(controllers) > 0:
            operator = gate
            identity = sp.eye(self.dim)
            for n in controllers:
                controller_compliment = list(set(self.systems) ^ set([n]))
                matrix = sp.zeros(self.dim**self.num_systems)
                for k in range(0, self.dim):
                    controller = identity
                    if n in self.controls:
                        controller = ket(k, self.dim) * bra(k, self.dim)
                    if n in self.anticontrols:
                        controller = ket(self.dim - 1 - k, self.dim) * bra(
                            self.dim - 1 - k, self.dim
                        )
                    ordered = arrange(
                        [controller_compliment, [n]], [identity] + [controller]
                    )
                    controlling = sp.Matrix(TensorProduct(*ordered))

                    matrix += controlling * operator**k
                operator = matrix
            gate = matrix

        # Conditions
        conditions = self.conditions if conditions is None else conditions
        conditions = symbolize_tuples(conditions, self.symbols_list)
        gate = gate.subs(conditions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            gate = recursively_simplify(gate, conditions)

        # Conjugation
        conjugate = self.conjugate if conjugate is None else conjugate
        if conjugate is True:
            gate = Dagger(gate)

        return gate


class Pauli(QuantumGate):
    """A subclass for creating Pauli gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems
    corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    index : int
        The index of the desired Pauli matrix. Can take the following values:

        - ``0`` (:math:`2`-dimensional identity matrix :math:`\\Identity`)
        - ``1`` (Pauli-X :math:`\\Pauli_x`)
        - ``2`` (Pauli-Y :math:`\\Pauli_y`)
        - ``3`` (Pauli-Z :math:`\\Pauli_z`)

    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    The Pauli gates are defined only for :math:`2`-dimensional (i.e., binary/qubit) systems.
    This means that the constructor does not take ``dim`` as an argument, nor can the associated property be set.
    """

    DIM = 2
    MATRICES = {
        0: sp.Matrix([[1, 0], [0, 1]]),
        1: sp.Matrix([[0, 1], [1, 0]]),
        2: sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        3: sp.Matrix([[1, 0], [0, -1]]),
    }
    LABELS = {0: "I", 1: "X", 2: "Y", 3: "Z"}

    def __init__(self, *args, index: int, **kwargs):
        self.index = index
        args, kwargs = default_arguments(
            args, kwargs, QuantumGate, [("label", Pauli.LABELS[index])]
        )
        args, kwargs = fix_arguments(
            args, kwargs, QuantumGate, [("dim", 2), ("spec", None)]
        )
        super().__init__(*args, **kwargs)

    @property
    def dim(self) -> int:
        return Pauli.DIM

    @dim.setter
    def dim(self, dim: int):
        pass

    @property
    def index(self) -> int:
        """The index of the desired Pauli matrix."""
        return self._index

    @index.setter
    def index(self, index: int):
        self._index = index

    @property
    def matrix(self) -> mat:
        operator = Pauli.MATRICES[self.index]
        identity = sp.eye(self.dim)
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


PAULI = Pauli


class GellMann(QuantumGate):
    """A subclass for creating Gell-Mann gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems
    corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    index : int
        The index of the desired Gell-Mann matrix. Can take the following values:

        - ``0`` (:math:`3`-dimensional identity matrix :math:`\\Identity`)
        - ``1`` (:math:`\\GellMann_1`)
        - ``2`` (:math:`\\GellMann_2`)
        - ``3`` (:math:`\\GellMann_3`)
        - ``4`` (:math:`\\GellMann_4`)
        - ``5`` (:math:`\\GellMann_5`)
        - ``6`` (:math:`\\GellMann_6`)
        - ``7`` (:math:`\\GellMann_7`)
        - ``8`` (:math:`\\GellMann_8`)

    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    The Gell-Mann gates are defined only for :math:`3`-dimensional (i.e., ternary/qutrit) systems.
    This means that the constructor does not take ``dim`` as an argument, nor can the associated
    property be set."""

    DIM = 3
    MATRICES = {
        0: sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        1: sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        2: sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]]),
        3: sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        4: sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        5: sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]]),
        6: sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        7: sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]]),
        8: (1 / sp.sqrt(3)) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),
    }
    LABELS = {
        0: "λ_0",
        1: "λ_1",
        2: "λ_2",
        3: "λ_3",
        4: "λ_4",
        5: "λ_5",
        6: "λ_6",
        7: "λ_7",
        8: "λ_8",
    }

    def __init__(self, *args, index: int, **kwargs):
        self.index = index
        args, kwargs = default_arguments(
            args, kwargs, QuantumGate, [("label", GellMann.LABELS[index])]
        )
        args, kwargs = fix_arguments(
            args, kwargs, QuantumGate, [("dim", 3), ("spec", None)]
        )
        super().__init__(*args, **kwargs)

    @property
    def dim(self) -> int:
        return GellMann.DIM

    @dim.setter
    def dim(self, dim: int):
        pass

    @property
    def index(self) -> int:
        """The index of the desired Gell-Mann matrix."""
        return self._index

    @index.setter
    def index(self, index: int):
        self._index = index

    @property
    def matrix(self) -> mat:
        operator = GellMann.MATRICES[self.index]
        identity = sp.eye(self.dim)
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


GM = GellMann


class Rotation(QuantumGate):
    """A subclass for creating rotation gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    The elementary rotation matrices :math:`\\Rotation_i` are a set of three :math:`2 \\times 2`
    matrices,

    .. math::

       \\begin{aligned}
           \\Rotation_x &= \\e^{-\\eye\\Pauli_{x}\\theta/2} =
               \\begin{bmatrix} \\cos(\\theta/2) & -\\eye\\sin(\\theta/2) \\\\
               -\\eye\\sin(\\theta/2) & \\cos(\\theta/2)  \\end{bmatrix} \\\\
           \\Rotation_y &= \\e^{-\\eye\\Pauli_{y}\\theta/2} =
               \\begin{bmatrix} \\cos(\\theta/2) & -\\sin(\\theta/2) \\\\
               \\sin(\\theta/2) & \\cos(\\theta/2) \\end{bmatrix} \\\\
           \\Rotation_z &= \\e^{-\\eye\\Pauli_{z}\\theta/2} =
               \\begin{bmatrix} \\e^{-\\eye\\theta/2} & 0 \\\\
               0 & \\e^{\\eye\\theta/2} \\end{bmatrix}
       \\end{aligned}

    where :math:`\\theta` is the rotation angle (``angle``).

    These are fundamentally single-system gates, and so a copy of the specified gate is placed on
    each of the subsystems corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    axis : int
        The index corresponding to the axis of the desired rotation matrix.
        Can take the following values:

        - ``1`` (:math:`x`-rotation :math:`\\Rotation_x`)
        - ``2`` (:math:`y`-rotation :math:`\\Rotation_y`)
        - ``3`` (:math:`z`-rotation :math:`\\Rotation_z`)

    angle : num | sym | str
        The scalar value to be used as the rotation angle.
        Defaults to ``0``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    The rotation gates are defined only for :math:`2`-dimensional (i.e., binary/qubit) systems.
    This means that the constructor does not take ``dim`` as an argument, nor can the associated
    property be set.
    """

    DIM = 2

    def __init__(
        self, *args, axis: int, angle: num | sym | str | None = None, **kwargs
    ):
        angle = 0 if angle is None else angle
        self.axis = axis
        self.angle = angle
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "R")])
        args, kwargs = fix_arguments(
            args, kwargs, QuantumGate, [("dim", 2), ("spec", None)]
        )
        super().__init__(*args, **kwargs)

    @property
    def dim(self) -> int:
        return Rotation.DIM

    @dim.setter
    def dim(self, dim: int):
        pass

    @property
    def axis(self) -> int:
        """The index corresponding to the axis of the desired rotation matrix."""
        return self._axis

    @axis.setter
    def axis(self, axis: int):
        self._axis = axis

    @property
    def angle(self) -> num | sym | str:
        """The scalar value to be used as the rotation angle."""
        return self._angle

    @angle.setter
    def angle(self, angle: num | sym | str):
        self._angle = angle

    @property
    def matrix(self) -> mat:
        operator = sp.eye(self.dim)
        angle = symbolize_expression(self.angle, self.symbols_list)
        if self.axis == 1:
            operator = sp.Matrix(
                [
                    [sp.cos(angle / 2), -sp.I * sp.sin(angle / 2)],
                    [-sp.I * sp.sin(angle / 2), sp.cos(angle / 2)],
                ]
            )
        if self.axis == 2:
            operator = sp.Matrix(
                [
                    [sp.cos(angle / 2), -sp.sin(angle / 2)],
                    [sp.sin(angle / 2), sp.cos(angle / 2)],
                ]
            )
        if self.axis == 3:
            operator = sp.Matrix(
                [[sp.exp(-sp.I * angle / 2), 0], [0, sp.exp(sp.I * angle / 2)]]
            )
        identity = sp.eye(self.dim)
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


ROT = Rotation


class Phase(QuantumGate):
    """A subclass for creating phase gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    In :math:`\\Dimension` dimensions, a phase operator :math:`\\Phase` may be represented as a
    :math:`\\Dimension \\times \\Dimension` diagonal matrix

    .. math::

       \\Phase(\\omega) =
           \\sum\\limits_{k=0}^{\\Dimension - 1} \\omega^k \\ket{k}\\bra{k}

    where :math:`\\omega` is the *phase* factor.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems
    corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    phase : num | sym | str
        The phase value.
        Defaults to the unit root given by ``sp.exp(2 * sp.pi * sp.I / self.dim)``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(
        self,
        *args,
        phase: num | sym | str | None = None,
        **kwargs,
    ):
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "P")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)
        phase = sp.exp(2 * sp.pi * sp.I / self.dim) if phase is None else phase
        self.phase = phase

    @property
    def phase(self) -> num | sym | str:
        """The phase value."""
        return self._phase

    @phase.setter
    def phase(self, phase: num | sym | str):
        self._phase = phase

    @property
    def matrix(self) -> mat:
        identity = sp.eye(self.dim)
        operator = sp.eye(self.dim)
        phase = symbolize_expression(self.phase, self.symbols_list)
        operator = sp.zeros(self.dim)
        for k in range(0, self.dim):
            operator += phase**k * ket(k, self.dim) * bra(k, self.dim)
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


PHS = Phase


class Diagonal(QuantumGate):
    """A subclass for creating diagonal gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    In :math:`\\Dimension` dimensions, a diagonal operator :math:`\\Diagonal` may be represented
    as a :math:`\\Dimension \\times \\Dimension` diagonal matrix

    .. math::

       \\Diagonal(\\lambda_0, \\lambda_1, \\ldots, \\lambda_{\\Dimension - 1}) =
           \\sum\\limits_{k=0}^{\\Dimension - 1} \\lambda_k\\ket{k}\\bra{k},
           \\quad \\lambda_k \\in \\Complexes, \\; \\abs{\\lambda_k} = 1

    where :math:`\\{\\lambda_k\\}_{k=0}^{\\Dimension - 1}` are the main diagonal *entries*.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems
    corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    entries : dict[int | list[int], num | sym | str]
        A dictionary in which the keys are level specifications (integer or list of integers) and
        the values are scalars.
    exponentiation : bool
        Whether to exponentiate (with imaginary unit) the values given in ``entries``.
        Defaults to ``False``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    Levels that are unspecified in the ``entries`` argument all have a corresponding matrix
    element of ``1``, regardless of the value of ``exponentiation``.
    """

    def __init__(
        self,
        *args,
        entries: dict[int | list[int], num | sym | str],
        exponentiation: bool | None = None,
        **kwargs,
    ):
        self.entries = entries
        exponentiation = False if exponentiation is None else exponentiation
        self.exponentiation = exponentiation
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "D")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)

    @property
    def entries(self) -> dict[int | list[int], num | sym | str]:
        """A dictionary in which the keys are level specifications (integer or list of integers)
        and the values are scalars."""
        return self._entries

    @entries.setter
    def entries(self, entries: dict[int | list[int], num | sym | str]):
        self._entries = entries

    @property
    def exponentiation(self) -> bool:
        """Whether to exponentiate (with imaginary unit) the values given in ``entries``."""
        return self._exponentiation

    @exponentiation.setter
    def exponentiation(self, exponentiation: bool):
        self._exponentiation = exponentiation

    @property
    def matrix(self) -> mat:
        identity = sp.eye(self.dim)
        operator = sp.eye(self.dim)
        for key, value in self.entries.items():
            if self.exponentiation is True:
                coefficient = symbolize_expression(
                    "exp(I*(" + str(value) + "))", self.symbols_list
                )
            else:
                coefficient = symbolize_expression(str(value), self.symbols_list)
            projector = ket(key, self.dim) * bra(key, self.dim)
            operator = operator + (coefficient - 1) * projector
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


DIAG = Diagonal


class Permutation(QuantumGate):
    """A subclass for creating permutation gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    TODO
    ----
    Change this gate such that permutations can be defined on subsets of the total system space
    and so do not have to contain the index of every subsystem. This means that the gates should
    also be controllable.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    permutation : int
        A list of system indices representing the positional arrangement of the systems as a
        result of the transformation. Must contain all of the system indices.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    When specifying a value for the ``permutation`` argument at instantiation, a value for the
    ``targets`` argument need not be supplied as the associated property will automatically be set.
    """

    def __init__(self, *args, permutation: list[int], **kwargs):
        self.permutation = permutation
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "P")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)

    @property
    def permutation(self) -> list[int]:
        return self._permutation

    @permutation.setter
    def permutation(self, permutation: list[int]):
        self._permutation = permutation
        self.targets = list(set(flatten_list(permutation)))

    @property
    def targets(self) -> list[int]:
        return list(set(flatten_list(self.permutation)))

    @targets.setter
    def targets(self, targets: list[int]):
        pass

    @property
    def matrix(self) -> mat:
        possibility = [k for k in range(0, self.dim)]
        possibilities = [possibility for k in self.systems]
        combinations = list(itertools.product(*possibilities))
        matrix = sp.zeros(self.dim**self.num_systems)
        for n in range(0, self.dim**self.num_systems):
            level = list(combinations[n])
            permuted = [level[self.permutation[k]] for k in self.targets]
            matrix = matrix + ket(permuted, self.dim) * bra(level, self.dim)
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


PERM = Permutation


class Swap(QuantumGate):
    """A subclass for creating SWAP (exchange) gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    In :math:`\\Dimension` dimensions, a SWAP operator :math:`\\Swap` between two (neighbouring)
    systems :math:`A` and :math:`B` may be represented as a
    :math:`\\Dimension^2 \\times \\Dimension^2` matrix

    .. math::

       \\Swap^{A,B} =
           \\sum\\limits_{j,k=0}^{\\Dimension - 1}
           {\\ket{j}\\bra{k}}^A \\otimes {\\ket{k}\\bra{j}}^B,

    where the identity operator acts on all other systems.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    targets : list[int, int]
        A list of exactly two indices corresponding to the systems to be swapped.
        Is an argument of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`,
        so can be specified positionally in ``*args``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`."""

    def __init__(self, *args, **kwargs):
        args, kwargs = default_arguments(
            args, kwargs, QuantumGate, [("label", "S"), ("family", "SWAP")]
        )
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)
        if len(self.targets) != 2:
            raise ValueError(
                "A ``targets`` list of exactly two (2) system indices must be provided."
            )

    @property
    def matrix(self) -> mat:
        permutation = [k for k in range(0, self.num_systems)]
        permutation[self.targets[0]], permutation[self.targets[1]] = (
            permutation[self.targets[1]],
            permutation[self.targets[0]],
        )
        possibility = [k for k in range(0, self.dim)]
        possibilities = [possibility for _ in range(0, self.num_systems)]
        combinations = list(itertools.product(*possibilities))
        matrix = sp.zeros(self.dim**self.num_systems)
        for n in range(0, self.dim**self.num_systems):
            level = list(combinations[n])
            permuted = [level[permutation[k]] for k in range(0, self.num_systems)]
            matrix = matrix + ket(permuted, self.dim) * bra(level, self.dim)
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


SWAP = Swap


class Summation(QuantumGate):
    """A subclass for creating SUM (summation) gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    The SUM gate is essentially a generalization of the NOT gate. In :math:`\\Dimension` dimensions,
    it is defined as the operator

    .. math:: \\SUM(n) = \\sum\\limits_{k=0}^{\\Dimension - 1} \\ket{k \\oplus n}\\bra{k}

    where :math:`n` (``shift``) is the *shift* parameter,
    and :math:`k \\oplus n \\equiv k + n \\mathrel{\\mathrm{mod}} \\Dimension`.

    The case of :math:`n = 1` is known as the *shift* operator, and represents a (non-Hermitian)
    generalization of the Pauli-X :math:`\\Pauli_x` operator to :math:`\\Dimension` dimensions.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems
    corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    shift : int
        The summation shift parameter.
        Must be a non-negative integer.
        Defaults to ``1``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`."""

    def __init__(self, *args, shift: int | None = None, **kwargs):
        shift = 1 if shift is None else shift
        self.shift = shift
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "Σ")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)

    @property
    def shift(self) -> int:
        """The summation shift parameter."""
        return self._shift

    @shift.setter
    def shift(self, shift: int):
        self._shift = shift

    @property
    def matrix(self) -> mat:
        identity = sp.eye(self.dim)
        summation = sp.zeros(self.dim)
        for k in range(0, self.dim):
            oplus = (k + self.shift) % self.dim
            summation = summation + ket(oplus, self.dim) * bra(k, self.dim)
        matrix = sp.Matrix([1])
        for m in range(0, self.num_systems):
            if m in list(self.targets):
                matrix = sp.Matrix(TensorProduct(matrix, summation))
            else:
                matrix = sp.Matrix(TensorProduct(matrix, identity))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


SUM = Summation


class Not(Summation):
    """A subclass for creating NOT (negation or "bit-flip") gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    The NOT gate is essentially a specialization of the SUM gate to :math:`2`-dimensional
    (i.e., binary/qubit) systems, and is exactly equivalent to the Pauli-X gate. As such,
    this class exists purely to simplify access to this operation.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems
    corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    NOT gates are defined only for :math:`2`-dimensional (i.e., binary/qubit) systems.
    This means that the constructor does not take ``dim`` as an argument,
    nor can the associated property be set."""

    DIM = 2

    def __init__(self, *args, **kwargs):
        args, kwargs = default_arguments(
            args, kwargs, QuantumGate, [("label", "X"), ("family", "TARG")]
        )
        args, kwargs = fix_arguments(
            args, kwargs, QuantumGate, [("dim", 2), ("spec", None)]
        )
        super().__init__(*args, shift=1, **kwargs)

    @property
    def dim(self) -> int:
        return Not.DIM

    @dim.setter
    def dim(self, dim: int):
        pass


NOT = Not


class Hadamard(QuantumGate):
    """A subclass for creating Hadamard gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    The elementary Hadamard gate :math:`\\Hadamard` (for qubits) may be represented as the
    :math:`2 \\times 2` operator

    .. math::
       
       \\begin{aligned}
           \\Hadamard &= \\frac{1}{\\sqrt{2}}\\sum\\limits_{j,k=0}^{1} (-1)^{jk} \\ket{j}\\bra{k} \\\\
           &= \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix}.
       \\end{aligned}
    
    This can be generalized to the following :math:`\\Dimension`-dimensional form for qudits,

    .. math::
       
       \\begin{aligned}
           \\Hadamard_\\Dimension &= \\frac{1}{\\sqrt{\\Dimension}}\\sum\\limits_{j,k=0}^{\\Dimension - 1}
               \\omega_\\Dimension^{k(\\Dimension - j)} \\ket{j}\\bra{k} \\\\
           &= \\begin{bmatrix} 1 & 1 & 1 & \\ldots & 1 \\\\
               1 & \\omega^{\\Dimension - 1} & \\omega^{2(\\Dimension - 1)} & \\ldots & \\omega^{(\\Dimension - 1)^2} \\\\
               1 & \\omega^{\\Dimension - 2} & \\omega^{2(\\Dimension - 2)} & \\ldots & \\omega^{(\\Dimension - 1)(\\Dimension - 2)} \\\\
               \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
               1 & \\omega & \\omega^{2} & \\ldots & \\omega^{\\Dimension - 1} \\end{bmatrix}
       \\end{aligned}

    where :math:`\\omega_\\Dimension \\equiv \\e^{\\frac{2\\pi\\eye}{\\Dimension}}`.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems
    corresponding to the indices in the ``targets`` property.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "H")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)

    @property
    def matrix(self) -> mat:
        # operator = (1 / sp.sqrt(2)) * sp.Matrix([[1, 1], [1, -1]])
        omega = sp.exp(2 * sp.pi * sp.I / self.dim)
        operator = sp.zeros(self.dim)
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                operator += (
                    omega ** (j * (self.dim - i))
                    * ket(i, dim=self.dim)
                    * bra(j, dim=self.dim)
                )
        operator *= 1 / sp.sqrt(self.dim)
        identity = sp.eye(self.dim)
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


HAD = Hadamard


class Fourier(QuantumGate):
    """A subclass for creating Fourier (quantum discrete Fourier transform [QDFT]) gates and
    storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    The elementary Fourier operator :math:`\\QFT` for a single :math:`\\Dimension`-dimensional
    qudit may be represented as the :math:`\\Dimension \\times \\Dimension` matrix

    .. math::
        
        \\begin{aligned}
            \\QFT &= \\frac{1}{\\sqrt{\\Dimension}} \\sum\\limits_{j,k=0}^{\\Dimension - 1}
                \\omega_{\\Dimension}^{jk} \\ket{j}\\bra{k} \\\\
            &= \\frac{1}{\\sqrt{\\Dimension}} \\begin{bmatrix} 1 & 1 & 1 & 1 & \\ldots & 1 \\\\
            1 & \\omega & \\omega^2 & \\omega^3 & \\ldots & \\omega^{\\Dimension - 1} \\\\
            1 & \\omega^2 & \\omega^4 & \\omega^6 & \\ldots & \\omega^{2(\\Dimension - 1)} \\\\
            1 & \\omega^3 & \\omega^6 & \\omega^9 & \\ldots & \\omega^{3(\\Dimension - 1)} \\\\
            \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
            1 & \\omega^{\\Dimension - 1} & \\omega^{2(\\Dimension - 1)}
                & \\omega^{3(\\Dimension - 1)} & \\ldots
                & \\omega^{(\\Dimension - 1)(\\Dimension - 1)} \\\\
            \\end{bmatrix}
        \\end{aligned}

    where :math:`\\omega_{\\Dimension} = \\e^{\\frac{2\\pi\\eye}{\\Dimension}} = \\omega`.

    In the case of :math:`N` qudits, the action of the multipartite Fourier operator :math:`\\QFT_N`
    on the basis state
    :math:`\\bigotimes\\limits_{\\ell=1}^{N} \\ket{j_\\ell} \\equiv \\ket{j_1, \\ldots, j_N}`
    (where :math:`j_\\ell \\in \\Integers_{0}^{\\Dimension - 1}`) is

    .. math::
        
        \\ket{j_1, \\ldots, j_N} \\stackrel{\\QFT_N}{\\longrightarrow}
            \\frac{1}{\\sqrt{\\Dimension^N}}
            \\bigotimes\\limits_{\\ell=1}^{N}
            \\sum\\limits_{k_\\ell=0}^{\\Dimension - 1}
            \\e^{2\\pi\\eye j k_\\ell \\Dimension^{-\\ell}} \\ket{k_\\ell}
    
    where :math:`j \\equiv \\sum\\limits_{\\ell=1}^{N} j_\\ell \\Dimension^{N - \\ell}`.

    If ``composite`` is ``True``, a copy of the elementary form :math:`\\QFT` is placed on
    each of the subsystems corresponding to the indices in the ``targets`` property.

    If ``composite`` is ``False``, the composite form :math:`\\QFT_N` is applied to the subsystems
    specified by ``targets`` in:
    
    - *ascending* order if ``reverse`` is ``False``
    - *descending* order if ``reverse`` is ``True``

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    composite : bool
        Whether the composite (multipartite) Fourier gate is to be used.
        If ``False``, copies of the elementary Fourier gate are placed on each index specified in
        ``targets``.
        Defaults to ``True``.
    reverse : bool
        Whether to reverse the order in which the composite (multipartite) Fourier gate is applied.
        Only applies when ``composite`` is ``False``.
        Defaults to ``False``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(
        self,
        *args,
        composite: bool | None = None,
        reverse: bool | None = None,
        **kwargs,
    ):
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "F")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        composite = True if composite is None else composite
        reverse = False if reverse is None else reverse
        super().__init__(*args, **kwargs)
        self.composite = composite
        self.reverse = reverse

    @property
    def composite(self) -> bool:
        """Whether the composite (multipartite) Fourier gate is to be used."""
        return self._composite

    @composite.setter
    def composite(self, composite: bool):
        self._composite = composite

    @property
    def reverse(self) -> bool:
        """Whether to reverse the order in which the composite (multipartite) Fourier gate is
        applied.
        Has no effect when ``self.composite`` is ``False``.
        """
        return self._reverse

    @reverse.setter
    def reverse(self, reverse: bool):
        self._reverse = reverse

    @property
    def matrix(self) -> mat:
        if self.composite is True:
            # Easy way: use decomposition instead of QFT definition
            targets = sorted(self.targets, reverse=self.reverse)
            size = len(targets)
            QFT = []
            for i, t in enumerate(targets):
                count = size - i
                for j in range(0, count):
                    if j == 0:
                        QFT.append(
                            Hadamard(
                                targets=[t], dim=self.dim, num_systems=self.num_systems
                            )
                        )
                    else:
                        QFT.append(
                            Phase(
                                targets=[targets[i + j]],
                                controls=[t],
                                exponent=sp.Rational(1, (self.dim**j)),
                                dim=self.dim,
                                num_systems=self.num_systems,
                                label=f"1 / {self.dim**j}",
                                family="GATE",
                            )
                        )
            matrix = sp.eye(self.dim**self.num_systems)
            for gate in QFT:
                matrix = gate.output() * matrix
        else:
            omega = sp.exp(2 * sp.pi * sp.I / self.dim)
            operator = sp.zeros(self.dim)
            for i in range(0, self.dim):
                for j in range(0, self.dim):
                    operator += (
                        omega ** (j * i) * ket(i, dim=self.dim) * bra(j, dim=self.dim)
                    )
            operator *= 1 / sp.sqrt(self.dim)
            identity = sp.eye(self.dim)
            targets_compliment = list(set(self.systems) ^ set(self.targets))
            ordered = arrange(
                [targets_compliment, self.targets], [identity] + [operator]
            )
            matrix = sp.Matrix(TensorProduct(*ordered))
        return matrix

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


QDFT = Fourier


class Measurement(QuantumGate):
    """A subclass for creating measurement gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so inherits all of its attributes, properties, and methods.

    Instances of this class each describe a (non-linear) operation in which the input state
    (:math:`\\op{\\rho}`) is quantum-mechanically *measured* (against the forms in specified in
    ``operators``) and subsequently mutated according to its predicted post-measurement form
    (i.e., the sum of all possible measurement outcomes). This yields the transformed states:

    - When ``observable`` is ``False``
      (``operators`` is a list of Kraus operators or projectors :math:`\\Kraus_i`):

    .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger.

    - When ``observable`` is ``True``
      (``operators`` is a list of observables :math:`\\Observable_i`):

    .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}] \\Observable_i.

    The items in the list ``operators`` can also be vectors (e.g., :math:`\\ket{\\xi_i}`),
    in which case each is converted into its corresponding matrix representation
    (e.g., :math:`\\Kraus_i = \\ket{\\xi_i}\\bra{\\xi_i}`) prior to any measurements.

    Note also that this method does not check for validity of supplied POVMs or the completeness
    of sets of observables, nor does it renormalize the post-measurement state.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    operators : list[mat | arr | QuantumObject]
        The operator(s) with which to perform the measurement.
        These would typically be a (complete) set of Kraus operators forming a POVM,
        a (complete) set of (orthogonal) projectors forming a PVM,
        or a set of observables constituting a complete basis for the relevant state space.
    observable : bool
        Whether to treat the items in ``operators`` as observables (as opposed to Kraus operators
        or projectors).
        Defaults to ``False``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    Measurement operations in quantum physics are, in general, non-linear and non-unitary
    operations on (normalized) state vectors and density operators. As such, they cannot be
    represented by matrices, and so the ``matrix`` property therefore does not return a valid
    representation of the measurement operation. Instead, it returns an identity matrix of the
    appropriate size for its number of dimensions and systems.

    Note
    ----
    The ``targets`` argument must be specified as a list of numerical indices of the subsystem(s)
    to be measured. These indices must be consecutive, and their number must match the number of
    systems spanned by all given operators."""

    def __init__(
        self,
        *args,
        operators: list[mat | arr | QuantumObject],
        observable: bool | None = None,
        **kwargs,
    ):
        self.operators = operators
        observable = False if observable is None else observable
        self.observable = observable
        args, kwargs = default_arguments(
            args,
            kwargs,
            QuantumGate,
            [("label", "M"), ("family", Families.METER.value)],
        )
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)

    @property
    def operators(self) -> list[mat | arr | QuantumObject]:
        """The operator(s) with which to perform the measurement."""
        return self._operators

    @operators.setter
    def operators(self, operators: list[mat | arr | QuantumObject]):
        self._operators = operators

    @property
    def observable(self) -> bool:
        """Whether to treat the items in the ``operators`` property as observables (as opposed to
        Kraus operators or projectors)."""
        return self._observable

    @observable.setter
    def observable(self, observable: bool):
        self._observable = observable

    @property
    def matrices(self) -> list[mat]:
        """A list of matrix representations of all operators in the ``operators`` property.

        Is a read-only property.

        This is used specifically in the :py:class:`~qhronology.quantum.circuits.QuantumCircuit`
        class when instances of it contain ``Measurement`` gate instances in their ``gates``
        property.
        """
        matrices = []
        identity = sp.eye(self.dim)
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        for operator in self.operators:
            operator = densify(extract_matrix(operator))
            ordered = arrange(
                [targets_compliment, self.targets], [identity] + [operator]
            )
            matrix = sp.Matrix(TensorProduct(*ordered))
            matrices.append(matrix)
        return matrices

    @property
    def matrix(self) -> mat:
        return sp.eye(self.dim**self.num_systems)

    @matrix.setter
    def matrix(self, matrix: mat):
        pass

    @property
    def form(self) -> str:
        return Forms.MATRIX.value

    @form.setter
    def form(self, form: str):
        pass


METER = Measurement


class GateInterleave(QuantumGate):
    """Compose two or more :py:class:`~qhronology.quantum.gates.QuantumGate` instances together
    by interleaving them.

    This is achieved by multiplying the matrix representations of the gates together. For example,
    for gates described by the multipartite operators :math:`\\op{A} \\otimes \\Identity`
    and :math:`\\Identity \\otimes \\op{B}`, their interleaved composition is

    .. math::

       (\\op{A} \\otimes \\Identity) \\cdot (\\Identity \\otimes \\op{B}) = \\op{A} \\otimes \\op{B}.

    While this is a subclass of :py:class:`~qhronology.quantum.gates.QuantumGate`,
    all of its inherited properties, except for those corresponding to arguments in its constructor,
    are read-only. This is because they are calculated from their corresponding properties in the
    individual instances contained within the ``gates`` property.

    Arguments
    ---------
    *gates : QuantumGate
        Variable-length argument list of :py:class:`~qhronology.quantum.gates.QuantumGate`
        instances to be interleaved.
    merge : bool
        Whether to merge the gates together diagrammatically.
        Defaults to ``False``.
    conjugate : bool
        Whether to perform Hermitian conjugation on the composite gate when it is called.
        Defaults to ``False``.
    exponent : num | sym | str
        A numerical or string representation of a scalar value to which composite gate's total
        matrix representation is exponentiated.
        Must be a non-negative integer.
        Defaults to ``1``.
    coefficient : num | sym | str
        A numerical or string representation of a scalar value by which the composite gate's
        matrix representation is multiplied.
        Performed after exponentiation.
        Defaults to ``1``.
    label : str
        The unformatted string used to represent the gate in mathematical expressions.
        Defaults to ``"⊗".join([gate.label for gate in [*gates]])``.
    notation : str
        The formatted string used to represent the gate in mathematical expressions.
        When not ``None``, overrides the value passed to ``label``.
        Not intended to be set by the user in most cases.
        Defaults to ``None``.

    Note
    ----
    Care should be taken to ensure that gates passed to this class all have the same ``num_systems``
    value and do not have overlapping ``targets``, ``controls``, and ``anticontrols`` properties.

    Note
    ----
    The resulting visualization (using the ``diagram()`` method or in circuit diagrams)
    may not be accurate in every case. However, the composed matrix should still be correct.
    """

    def __init__(
        self,
        *gates: QuantumGate,
        merge: bool | None = None,
        conjugate: bool | None = None,
        exponent: num | sym | str | None = None,
        coefficient: num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
    ):
        self.gates = [*gates]
        merge = False if merge is None else merge
        self.merge = merge
        label = "⊗".join([gate.label for gate in [*gates]]) if label is None else label

        super().__init__(
            spec=None,
            conjugate=conjugate,
            exponent=exponent,
            coefficient=coefficient,
            label=label,
            notation=notation,
        )

    def __str__(self) -> str:
        return str(self.notation) + " = " + stringify(self.output(), self.dim)

    def __repr__(self) -> str:
        return repr(self.output())

    @property
    def merge(self) -> bool:
        """Whether to merge the gates together diagrammatically."""
        return self._merge

    @merge.setter
    def merge(self, merge: bool):
        self._merge = merge

    @property
    def labels(self) -> list[str]:
        labels = [gate.label for gate in self.gates]
        if self.merge is True:
            labels = self.label
        return labels

    @property
    def notations(self) -> str | list[str]:
        notations = [gate.notation for gate in self.gates]
        if self.merge is True:
            notations = self.notation
        return notations

    @property
    def gates(self) -> list[QuantumGate]:
        """Variable-length list of :py:class:`~qhronology.quantum.gates.QuantumGate` instances
        to be composited."""
        return self._gates

    @gates.setter
    def gates(self, gates: list[QuantumGate]):
        self._gates = gates

    @property
    def boundaries(self) -> list[int]:
        boundaries = flatten_list([max(gate.boundaries) for gate in self.gates])
        if self.merge is True:
            boundaries = [self.num_systems]
        return boundaries

    @property
    def family(self) -> str | list[str]:
        family = [gate.family for gate in self.gates]
        if self.merge is True:
            family = Families.GATE.value
        return family

    @family.setter
    def family(self, family: str | list[str]):
        pass

    @property
    def targets(self) -> list[int]:
        return list(set(flatten_list([gate.targets for gate in self.gates])))

    @targets.setter
    def targets(self, targets: list[int]):
        pass

    @property
    def controls(self) -> list[int]:
        return list(set(flatten_list([gate.controls for gate in self.gates])))

    @controls.setter
    def controls(self, controls: list[int]):
        pass

    @property
    def anticontrols(self) -> list[int]:
        return list(set(flatten_list([gate.anticontrols for gate in self.gates])))

    @anticontrols.setter
    def anticontrols(self, anticontrols: list[int]):
        pass

    @property
    def num_systems(self) -> int:
        num_systems = list(set(flatten_list([gate.num_systems for gate in self.gates])))
        if len(num_systems) != 1:
            raise ValueError("Mismatch between one or more of the number of systems.")
        return num_systems[0]

    @num_systems.setter
    def num_systems(self, num_systems: int):
        pass

    @property
    def symbols(self) -> dict[sym | str, dict[str, Any]]:
        symbols_collection = [gate.symbols for gate in self.gates]
        symbols_merged = {}
        for symbols in symbols_collection:
            symbols_merged.update(symbols)
        return symbols_merged

    @symbols.setter
    def symbols(self, symbols):
        pass

    @property
    def dim(self) -> int:
        dim = list(set(flatten_list([gate.dim for gate in self.gates])))
        if len(dim) != 1:
            raise ValueError("Mismatch between one or more of the dimensions.")
        return dim[0]

    @dim.setter
    def dim(self, dim: int):
        pass

    @property
    def conditions(self) -> list[tuple[num | sym | str, num | sym | str]]:
        conditions = []
        for gate in self.gates:
            conditions += gate.conditions
        return conditions

    @conditions.setter
    def conditions(self, conditions):
        pass

    @property
    def matrix(self) -> mat:
        spec = sp.eye(self.dim**self.num_systems)
        for gate in self.gates:
            spec = (
                gate.output(conditions=gate.conditions, exponent=gate.exponent) * spec
            )
        return spec

    @matrix.setter
    def matrix(self, matrix: mat):
        pass

    def output(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        exponent: bool | num | sym | str | None = None,
        coefficient: bool | num | sym | str | None = None,
    ) -> mat:
        """Construct the composite gate and return its matrix representation.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the gate.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the gate.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the gate.
            If ``False``, does not conjugate.
            Defaults to the value of ``self.conjugate``.
        exponent : bool | num | sym | str
            The scalar value by which the gate's matrix representation is exponentiated.
            If ``False``, does not exponentiate.
            Defaults to the value of ``self.exponent``.
        coefficient : num | sym | str
            The scalar value by which the gate's matrix representation is multiplied.
            If ``False``, does not multiply the gate by the coefficient.
            Defaults to the value of ``self.coefficient``.

        Returns
        -------
        mat
            The constructed quantum gate.
        """
        gate = self.matrix

        # Exponentiate
        if exponent is None or exponent is True:
            exponent = self.exponent
        if exponent != 1 and exponent is not False:
            exponent = symbolize_expression(exponent, self.symbols_list)
            gate = ((1 + sp.exp(-sp.I * sp.pi * exponent)) / 2) * sp.eye(
                self.dim**self.num_systems
            ) + ((1 - sp.exp(-sp.I * sp.pi * exponent)) / 2) * gate

        # Coefficient
        if coefficient is None or coefficient is True:
            coefficient = self.coefficient
        if coefficient is not False:
            coefficient = symbolize_expression(self.coefficient, self.symbols_list)
        gate *= coefficient

        gate = symbolize_expression(gate, self.symbols_list)

        # Conditions
        conditions = self.conditions if conditions is None else conditions
        conditions = symbolize_tuples(conditions, self.symbols_list)
        gate = gate.subs(conditions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            gate = recursively_simplify(gate, conditions)

        # Conjugation
        conjugate = self.conjugate if conjugate is None else conjugate
        if conjugate is True:
            gate = Dagger(gate)

        return gate


INTERLEAVE = GateInterleave


class GateStack(GateInterleave):
    """Compose two or more :py:class:`~qhronology.quantum.gates.QuantumGate` instances together
    by "stacking" them vertically.

    This is achieved by computing the tensor product matrix representations of the gates together.
    For example, for gates described by the multipartite operators
    :math:`\\op{A} \\otimes \\Identity` and :math:`\\Identity \\otimes \\op{B}`,
    their stacked composition is

    .. math::

       (\\op{A} \\otimes \\Identity) \\otimes (\\Identity \\otimes \\op{B})
       = \\op{A} \\otimes \\Identity \\otimes \\Identity \\otimes \\op{B}.

    This class is derived from the :py:class:`~qhronology.quantum.gates.QuantumGate` class,
    and so should be used in much the same way.

    Arguments
    ---------
    *gates : QuantumGate
        Variable-length argument list of :py:class:`~qhronology.quantum.gates.QuantumGate`
        instances to be stacked.
    merge : bool
        Whether to merge the gates together diagrammatically.
        Defaults to ``False``.
    conjugate : bool
        Whether to perform Hermitian conjugation on the composite gate when it is called.
        Defaults to ``False``.
    exponent : num | sym | str
        A numerical or string representation of a scalar value to which composite gate's total
        matrix representation is exponentiated.
        Defaults to ``1``.
    coefficient : num | sym | str
        A numerical or string representation of a scalar value by which the composite gate's
        matrix representation is multiplied.
        Performed after exponentiation.
        Defaults to ``1``.
    label : str
        The unformatted string used to represent the gate in mathematical expressions.
        Defaults to ``"⊗".join([gate.label for gate in [*gates]])``.
    notation : str
        The formatted string used to represent the gate in mathematical expressions.
        When not ``None``, overrides the value passed to ``label``.
        Not intended to be set by the user in most cases.
        Defaults to ``None``."""

    def __init__(
        self,
        *gates: QuantumGate,
        merge: bool | None = None,
        conjugate: bool | None = None,
        exponent: num | sym | str | None = None,
        coefficient: num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
    ):
        super().__init__(
            *gates,
            merge=merge,
            conjugate=conjugate,
            exponent=exponent,
            coefficient=coefficient,
            label=label,
            notation=notation,
        )

    @property
    def boundaries(self) -> list[int]:
        num_systems = [gate.num_systems for gate in self.gates]
        boundaries = [
            max(gate.boundaries) + sum(num_systems[:n])
            for n, gate in enumerate(self.gates)
        ]
        if self.merge is True:
            boundaries = [self.num_systems]
        return boundaries

    @property
    def targets(self) -> list[int]:
        targets = []
        num_systems = [gate.num_systems for gate in self.gates]
        for n, gate in enumerate(self.gates):
            targets_current = [target + sum(num_systems[:n]) for target in gate.targets]
            targets.append(targets_current)
        return list(set(flatten_list(targets)))

    @targets.setter
    def targets(self, targets: list[int]):
        pass

    @property
    def controls(self) -> list[int]:
        controls = []
        num_systems = [gate.num_systems for gate in self.gates]
        for n, gate in enumerate(self.gates):
            controls_current = [
                control + sum(num_systems[:n]) for control in gate.controls
            ]
            controls.append(controls_current)
        return list(set(flatten_list(controls)))

    @controls.setter
    def controls(self, controls: list[int]):
        pass

    @property
    def anticontrols(self) -> list[int]:
        anticontrols = []
        num_systems = [gate.num_systems for gate in self.gates]
        for n, gate in enumerate(self.gates):
            anticontrols_current = [
                anticontrol + sum(num_systems[:n]) for anticontrol in gate.anticontrols
            ]
            anticontrols.append(anticontrols_current)
        return list(set(flatten_list(anticontrols)))

    @anticontrols.setter
    def anticontrols(self, anticontrols: list[int]):
        pass

    @property
    def num_systems(self) -> int:
        return sum([gate.num_systems for gate in self.gates])

    @num_systems.setter
    def num_systems(self, num_systems: int):
        pass

    @property
    def matrix(self) -> mat:
        matrices = [
            gate.output(conditions=gate.conditions, exponent=gate.exponent)
            for gate in self.gates
        ]
        return sp.Matrix(TensorProduct(*matrices))

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


STACK = GateStack


class _Single(QuantumGate):
    """A :py:class:`~qhronology.quantum.gates.QuantumGate` subclass for creating single-cell
    abstract quantum gates.

    Used internally exclusively for visualization purposes."""

    def __init__(
        self, *args, family: str | None = None, label: str | None = None, **kwargs
    ):
        family = Families.TERM.value if family is None else family
        label = " " if label is None else label
        super().__init__(
            *args,
            spec=None,
            targets=[0],
            num_systems=1,
            family=family,
            label=label,
            **kwargs,
        )

    @property
    def matrix(self) -> mat:
        return sp.eye(self.dim**self.num_systems)

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


class _Empty(QuantumGate):
    """A :py:class:`~qhronology.quantum.gates.QuantumGate` subclass for creating single-cell
    empty quantum gates.

    Used internally exclusively for visualization purposes."""

    def __init__(self, *args, family: str | None = None, **kwargs):
        family = Families.TERM.value if family is None else family
        super().__init__(
            *args, spec=None, targets=[0], num_systems=1, family=family, **kwargs
        )

    @property
    def matrix(self) -> mat:
        return sp.eye(self.dim**self.num_systems)

    @matrix.setter
    def matrix(self, matrix: mat):
        pass


class _Wormhole(QuantumGate):
    """A :py:class:`~qhronology.quantum.gates.QuantumGate` subclass for creating single-cell
    wormhole (mouth) quantum gates.

    Used internally exclusively for visualization purposes.
    """

    def __init__(self, *args, family: str | None = None, **kwargs):
        family = Families.WORMHOLE.value if family is None else family
        super().__init__(
            *args, spec=None, targets=[0], num_systems=1, family=family, **kwargs
        )

    @property
    def matrix(self) -> mat:
        return sp.eye(self.dim**self.num_systems)

    @matrix.setter
    def matrix(self, matrix: mat):
        pass
