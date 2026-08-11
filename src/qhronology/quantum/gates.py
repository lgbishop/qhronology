# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

"""
Classes for the creation of quantum gates.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations
import copy
import itertools
from typing import Any

import numpy as np
import sympy as sp

from qhronology.mechanics.matrices import bra, ket, quantum_object
from qhronology.mechanics.operations import densify
from qhronology.utilities.classification import Forms, Kinds, arr, expr, mat, num, sym
from qhronology.utilities.diagrams import Families
from qhronology.utilities.helpers import (
    apply_substitutions,
    arrange,
    cast,
    check_systems_conflicts,
    conjugate_transpose,
    count_systems,
    default_arguments,
    extract_representation,
    fix_arguments,
    flatten_list,
    generate_identity,
    generate_zeros,
    matrix_multiplication,
    recursively_simplify,
    stringify,
    symbolize_substitutions,
    symbolize_expression,
    tensor_product,
    to_matrix,
    to_numerical,
)
from qhronology.utilities.objects import QuantumObject


class QuantumGate(QuantumObject):
    """A class for creating quantum gates and storing their metadata.

    This class forms the base upon which all quantum gates are built.
    Instances of this base class and its derivatives (subclasses) provide complete descriptions of quantum gates.
    This means that they describe a complete vertical column (or "slice") in the quantum circuitry picturalism, including control nodes, anticontrol nodes, empty wires, and the (unitary) gate operator itself.
    The details of any algebraic symbols, mathematical substitutions, and visualization labels are also recorded.
    Note that, unlike the internal matrix representations contained within instances of the :py:class:`~qhronology.quantum.states.QuantumState` class (and its derivatives), the matrix representations of subclass instances of :py:class:`~qhronology.quantum.gates.QuantumGate` are *not* mutable.

    Arguments
    ---------
    spec : mat | arr | list[list[num | expr | str]]
        The specification of the quantum gate's matrix representation in a standard :python:`dim`-dimensional basis.
        Can be one of:

        - a SymPy matrix (:python:`mat`)
        - a NumPy array (:python:`arr`)
        - a list of lists of numerical, symbolic, or string expressions that collectively describe a matrix (:python:`list[list[num | expr | str]]`)

        Defaults to the single-system :python:`dim`-dimensional identity operator.
    targets : list[int]
        The numerical indices of the subsystems on which the gate elements reside.
        Defaults to :python:`[0]` (if :python:`num_systems` is :python:`None`) or :python:`[i for i in range(num_systems)]` (if :python:`num_systems` is not :python:`None`).
    controls : list[int]
        The numerical indices of the subsystems on which control nodes reside.
        Defaults to :python:`[]`.
    anticontrols : list[int]
        The numerical indices of the subsystems on which anticontrol nodes reside.
        Defaults to :python:`[]`.
    num_systems : int
        The (total) number of systems which the gate spans.
        Must be a non-negative integer.
        Defaults to :python:`max(targets + controls + anticontrols + [count_systems(sp.Matrix(spec), dim)]) + 1`.
    dim : int
        The dimensionality of the quantum gate's Hilbert space.
        Must be a non-negative integer.
        Defaults to :python:`2`.
    numerical : bool
        Whether to cast the gate's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the gate's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.
    symbols : dict[sym | str, dict[str, Any]]
        A dictionary in which the keys are individual symbols (usually found within the gate specification :python:`spec`) and the values are dictionaries of their respective SymPy keyword-argument :python:`assumptions`.
        Defaults to :python:`{}`.
    substitutions : list[tuple[num | expr | str, num | expr | str]]
        A list of 2-tuples of substitutions to be applied to the gate.
        All instances of the expression in each tuple's first element are replaced by the expression in the respective second element.
        This uses the same format as the SymPy :python:`subs()` method.
        Defaults to :python:`[]`.
    conjugate : bool
        Whether to perform Hermitian conjugation on the gate when it is called.
        Defaults to :python:`False`.
    exponent : num | expr | str
        A numerical or string representation of a scalar value to which gate's operator (residing on :python:`targets`) is exponentiated.
        Must be a non-negative integer.
        Useful for computing powers of gates (such as PSWAP), but is only guaranteed to return a valid power of a gate if its corresponding matrix representation (e.g., :math:`\\op{A}`) is involutory (i.e., :math:`\\op{A}^2 = \\Identity`).
        Defaults to :python:`1`.
    coefficient : num | expr | str
        A numerical or string representation of a scalar value by which the gate's matrix (occupying :python:`targets`) is multiplied.
        Performed after exponentiation.
        Useful for multiplying the gate by a phase factor.
        Defaults to :python:`1`.
    label : str
        The unformatted string used to represent the gate in mathematical expressions.
        Defaults to :python:`"U"`.
    notation : str
        The formatted string used to represent the gate in mathematical expressions.
        When not :python:`None`, overrides the value passed to :python:`label`.
        Not intended to be set by the user in most cases.
        Defaults to :python:`None`.
    family : str
        A string expressing the kind of block element for which the gate is to be visualized.
        Not intended to be set by the user.
        Defaults to :python:`"GATE"`.

    Note
    ----
    The indices specified in :python:`targets`, :python:`controls`, and :python:`anticontrols` must be distinct.
    """

    def __init__(
        self,
        spec: mat | arr | list[list[num | expr | str]] | None,
        targets: list[int] | None = None,
        controls: list[int] | None = None,
        anticontrols: list[int] | None = None,
        num_systems: int | None = None,
        dim: int | None = None,
        numerical: bool | None = None,
        array: bool | None = None,
        symbols: dict | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        conjugate: bool | None = None,
        exponent: num | expr | str | None = None,
        coefficient: num | expr | str | None = None,
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
            if isinstance(spec, list) is True:
                spec_num_systems = count_systems(to_matrix(spec), dim)
            else:
                spec_num_systems = count_systems(spec, dim)
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

        # Automatically resize.
        num_systems = max(flatten_list([num_systems, targets, controls, anticontrols]))

        self.targets = targets
        self.controls = controls
        self.anticontrols = anticontrols
        self.exponent = exponent
        self.coefficient = coefficient

        QuantumObject.__init__(
            self,
            spec=spec,
            form=Forms.MATRIX.value,
            kind=Kinds.MIXED.value,
            dim=dim,
            numerical=numerical,
            num_systems=num_systems,
            array=array,
            symbols=symbols,
            substitutions=substitutions,
            conjugate=conjugate,
            label=label,
            notation=notation,
            family=family,
            debug=False,
        )

    @property
    def is_vector(self) -> bool:
        return False

    @property
    def form(self) -> str:
        return Forms.MATRIX.value

    @form.setter
    def form(self, form: str):
        pass

    @property
    def current(self) -> mat | arr:
        """The current (unprocessed) matrix representation of the quantum gate."""
        return quantum_object(
            spec=self.spec,
            form=self.form,
            kind=self.kind,
            dim=self.dim,
            numerical=self.numerical,
            array=self.array,
        )

    @current.setter
    def current(self, current: mat | arr):
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
                    """The :python:`targets`, :python:`controls`, and :python:`anticontrols` lists cannot have any elements in common."""
                )
        self._targets = targets

    @property
    def controls(self) -> list[int]:
        """The numerical indices of the subsystems on which control nodes reside.
        
        For example, a controlled-:math:`\\Unitary` gate in :math:`\\Dimension` dimensions takes the form

        .. math::

           \\begin{aligned}
               \\Control^{\\indices{0}} \\Unitary^{\\indices{1}} &= \\sum\\limits_{k=0}^{\\Dimension - 1} \\ket{k}\\bra{k}\\otimes\\Unitary^{k} \\\\
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
                """The :python:`targets`, :python:`controls`, and :python:`anticontrols` lists cannot have any elements in common."""
            )
        self._controls = sorted(list(set(controls)))

    @property
    def anticontrols(self) -> list[int]:
        """The numerical indices of the subsystems on which anticontrol nodes reside.

        For example, an anticontrolled-:math:`\\Unitary` gate in :math:`\\Dimension` dimensions takes the form

        .. math::

           \\begin{aligned}
               \\Anticontrol^{\\indices{0}} \\Unitary^{\\indices{1}} &= \\sum\\limits_{k=0}^{\\Dimension - 1} \\ket{k}\\bra{k}\\otimes\\Unitary^{\\Dimension - 1 - k} \\\\
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
                """The :python:`targets`, :python:`controls`, and :python:`anticontrols` lists cannot have any elements in common."""
            )
        self._anticontrols = sorted(list(set(anticontrols)))

    @property
    def num_systems(self) -> int:
        """The number of systems that the gate spans.
        Must be a non-negative integer."""
        return self._num_systems

    @num_systems.setter
    def num_systems(self, num_systems: int):
        if num_systems < max(self.targets + self.controls + self.anticontrols) + 1:
            raise ValueError(
                f"""The specified number of systems ({num_systems}) is smaller than the largest index given in the targets, controls, and anticontrols."""
            )
        self._num_systems = num_systems

    @property
    def boundaries(self) -> list[int]:
        """An ordered list of indices of the object's boundaries corresponding to its :python:`labels`.
        Used exclusively by the visualization engine."""
        return [max(flatten_list([self.targets, self.controls, self.anticontrols]))]

    @property
    def exponent(self) -> num | expr | str:
        """A numerical or string representation of a scalar value specifying the value to which the gate's matrix representation is exponentiated.
        Is guaranteed to produce valid powers only for involutory matrices.

        For an involutory matrix :math:`\\op{A}`, that is :math:`\\op{A}^2 = \\Identity` (where :math:`\\Identity` is the identity matrix), we have the identity,

        .. math::

           \\exp[\\eye z \\op{A}] = \\cos(z)\\Identity + \\eye\\sin(z)\\op{A},

        for any :math:`z \\in \\Complexes`. In the case of :math:`z = -\\frac{\\pi}{2}`, this becomes

        .. math::

           \\exp\\Bigl[-\\eye\\frac{\\pi}{2}\\op{A}\\Bigr] = -\\eye\\op{A},
        
        which can be rearranged to give

        .. math::

           \\begin{aligned}
               \\op{A} &= \\eye \\exp\\Bigl[-\\eye\\frac{\\pi}{2}\\op{A}\\Bigr] \\\\
               &= \\exp\\Bigl[\\eye\\frac{\\pi}{2}\\Bigr] \\cdot
                   \\exp\\Bigl[-\\eye\\frac{\\pi}{2}\\op{A}\\Bigr].
           \\end{aligned}

        Simply taking this expression to an arbitrary power :math:`p \\in \\mathbb{C}` thus yields the identity

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
    def exponent(self, exponent: num | expr | str):
        self._exponent = exponent

    @property
    def coefficient(self) -> num | expr | str:
        """A numerical or string representation of a scalar value by which the gate's matrix (occupying :python:`targets`) is multiplied."""
        return self._coefficient

    @coefficient.setter
    def coefficient(self, coefficient: num | expr | str):
        self._coefficient = coefficient

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        """Compute the unprocessed matrix representation of the gate.

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
            The unprocessed matrix representation of the gate.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        operator = cast(self.current, numerical=numerical, array=array_intermediate)
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        ordered = []
        for i in self.systems:
            if i not in self.targets:
                ordered.append(identity)
            if i == min(self.targets):
                ordered.append(operator)
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)

    def output(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        exponent: bool | num | expr | str | None = None,
        coefficient: bool | num | expr | str | None = None,
    ) -> mat | arr:
        """Compute the processed matrix representation of the constructed gate (including any controls, anticontrols, and empty systems).

        Arguments
        ---------
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
            Defaults to the value of :python:`self.array`.
        substitutions : list[tuple[num | expr | str, num | expr | str]]
            Algebraic substitutions to be applied to the gate.
            Defaults to the value of :python:`self.substitutions`.
        simplify : bool
            Whether to perform mathematical simplification on the gate.
            If :python:`False`, does not simplify.
            Defaults to :python:`False`.
        conjugate : bool
            Whether to perform Hermitian conjugation on the gate.
            If :python:`False`, does not conjugate.
            Defaults to the value of :python:`self.conjugate`.
        exponent : bool | num | expr | str
            The scalar value by which the gate's matrix representation is exponentiated.
            If :python:`False`, does not exponentiate.
            Defaults to the value of :python:`self.exponent`.
        coefficient : bool | num | expr | str
            The scalar value by which the gate's matrix representation is multiplied.
            If :python:`False`, does not multiply the gate by the coefficient.
            Defaults to the value of :python:`self.coefficient`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the constructed gate.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        gate = self.matrix(numerical=numerical, array=array_intermediate)

        # Exponentiate
        if exponent is None or exponent is True:
            exponent = self.exponent
        if exponent != 1 and exponent is not False:
            exponent = symbolize_expression(exponent, self.symbols_list)
            plus = to_numerical(
                (1 + sp.exp(sp.I * sp.pi * exponent)) / 2, numerical=numerical
            )
            minus = to_numerical(
                (1 - sp.exp(sp.I * sp.pi * exponent)) / 2, numerical=numerical
            )
            identity = generate_identity(
                self.dim**self.num_systems,
                numerical=numerical,
                array=array_intermediate,
            )
            gate = plus * identity + minus * gate

        # Coefficient
        if coefficient is None or coefficient is True:
            coefficient = self.coefficient
        if coefficient is not False:
            coefficient = symbolize_expression(coefficient, self.symbols_list)
        else:
            coefficient = 1
        if coefficient != 1 and coefficient is not False:
            coefficient = to_numerical(coefficient, numerical=numerical)
            gate = coefficient * gate

        gate = symbolize_expression(gate, self.symbols_list)

        controllers = self.controls + self.anticontrols
        if len(controllers) > 0:
            operator = gate
            identity = generate_identity(
                self.dim, numerical=numerical, array=array_intermediate
            )
            for n in controllers:
                controller_compliment = list(set(self.systems) ^ set([n]))
                matrix = generate_zeros(
                    self.dim**self.num_systems,
                    numerical=numerical,
                    array=array_intermediate,
                )
                for k in range(0, self.dim):
                    controller = identity
                    if n in self.controls:
                        controller = ket(
                            k,
                            dim=self.dim,
                            numerical=numerical,
                            array=array_intermediate,
                        ) * bra(
                            k,
                            dim=self.dim,
                            numerical=numerical,
                            array=array_intermediate,
                        )
                    if n in self.anticontrols:
                        controller = ket(
                            self.dim - 1 - k,
                            dim=self.dim,
                            numerical=numerical,
                            array=array_intermediate,
                        ) * bra(
                            self.dim - 1 - k,
                            dim=self.dim,
                            numerical=numerical,
                            array=array_intermediate,
                        )
                    ordered = arrange(
                        [controller_compliment, [n]], [identity] + [controller]
                    )
                    controlling = tensor_product(*ordered)
                    if numerical is False:
                        operator_power = cast(
                            to_matrix(operator) ** k,
                            numerical=numerical,
                            array=array_intermediate,
                        )
                    else:
                        operator_power = np.linalg.matrix_power(operator, k)

                    controlling = cast(
                        controlling, numerical=numerical, array=array_intermediate
                    )
                    operator_power = cast(
                        operator_power, numerical=numerical, array=array_intermediate
                    )

                    matrix = matrix + matrix_multiplication(controlling, operator_power)
                operator = matrix
            gate = matrix

        # Conditions
        substitutions = self.substitutions if substitutions is None else substitutions
        substitutions = symbolize_substitutions(substitutions, self.symbols_list)
        gate = apply_substitutions(gate, substitutions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            gate = recursively_simplify(gate, substitutions)

        # Conjugation
        conjugate = self.conjugate if conjugate is None else conjugate
        if conjugate is True:
            gate = conjugate_transpose(gate)

        return cast(gate, numerical=numerical, array=array)

    def print(
        self,
        delimiter: str | None = None,
        product: bool | None = None,
        return_string: bool | None = None,
        numerical: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        exponent: bool | num | expr | str | None = None,
        coefficient: bool | num | expr | str | None = None,
    ) -> None | str:
        """Print or return a mathematical expression of the quantum gate as a string.

        Note that this method is essentially a wrapper on the :py:meth:`~qhronology.quantum.gates.QuantumGate.output` method, and so includes its arguments.

        Arguments
        ---------
        delimiter : str
            A string containing the character(s) with which to delimit (i.e., separate) the values in the ket and/or bra terms in the mathematical expression.
            Defaults to :python:`","`.
        product : bool
            Whether to represent the mathematical expression using tensor products.
            Only applies if the gate is a multipartite composition.
            Defaults to :python:`False`.
        return_string : bool
            Whether to return the mathematical expression as a string.
            Defaults to :python:`False`.
        numerical : bool
            Whether to cast the matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        substitutions : list[tuple[num | expr | str, num | expr | str]]
            Algebraic substitutions to be applied to the gate.
            Defaults to the value of :python:`self.substitutions`.
        simplify : bool
            Whether to perform mathematical simplification on the gate.
            If :python:`False`, does not simplify.
            Defaults to :python:`False`.
        conjugate : bool
            Whether to perform Hermitian conjugation on the gate.
            If :python:`False`, does not conjugate.
            Defaults to the value of :python:`self.conjugate`.
        exponent : bool | num | expr | str
            The scalar value by which the gate is exponentiated.
            If :python:`False`, does not exponentiate.
            Defaults to the value of :python:`self.exponent`.
        coefficient : bool | num | expr | str
            The scalar value by which the gate is multiplied.
            If :python:`False`, does not multiply the gate by the coefficient.
            Defaults to the value of :python:`self.coefficient`.

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
                    simplify=simplify,
                    conjugate=conjugate,
                    exponent=exponent,
                    coefficient=coefficient,
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


class Unitary(QuantumGate):
    """A subclass for creating unitary gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    A square matrix :math:`\\Unitary` is said to be *unitary* if its matrix inverse is equal to its conjugate tranpose (Hermitian conjugate). Mathematically, this is the condition

    .. math:: \\Unitary^\\dagger = \\Unitary^{-1},

    which equivalently means that any unitary matrix satisfies

    .. math:: \\Unitary^\\dagger \\Unitary = \\Unitary \\Unitary^\\dagger = \\Identity,

    where :math:`\\Identity` is the identity matrix. Evidently, the inverse of a unitary matrix is another unitary matrix. Additionally, the product of any two unitary matrices is unitary, and so the set of all unitary matrices consitutes a group, called the *unitary group* (written :math:`\\GroupUnitary(n)` for the group of :math:`n \\times n` unitary matrices), with the group operation being matrix multiplication.

    Unitary gates for qubits correspond to :math:`2 \\times 2` unitary matrices, with one parametrization of such matrices being

    .. math::

       \\Unitary(\\theta,\\phi,\\lambda) =
           \\begin{bmatrix} \\cos(\\theta/2) & -\\e^{\\eye\\lambda}\\sin(\\theta/2) \\\\
           \\e^{\\eye\\phi}\\sin(\\theta/2) & \\e^{\\eye(\\phi + \\lambda)}\\cos(\\theta/2) \\end{bmatrix},

    where the *parameters* (:python:`parameters`) :math:`\\theta, \\phi, \\lambda \\in \\Reals` can be interpreted as angles. Note that this form is :math:`2\\pi`-periodic in each of its three parameters, and specifies any element of :math:`\\GroupUnitary(2)` (up to a global phase).

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    parameters : tuple[num | expr | str, num | expr | str, num | expr | str]
        A 3-tuple of scalar values corresponding to the parameters :math:`(\\theta, \\phi, \\lambda)` in the given definition.
        Defaults to :python:`(0, 0, 0)`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    The unitary gate is defined only for :math:`2`-dimensional (i.e., binary/qubit) systems.
    This means that the constructor does not take :python:`dim` as an argument, nor can the associated property be set.
    """

    DIM = 2

    def __init__(
        self,
        *args,
        parameters: (
            tuple[num | expr | str, num | expr | str, num | expr | str] | None
        ) = None,
        **kwargs,
    ):
        parameters = (0, 0, 0) if parameters is None else parameters
        self.parameters = parameters
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "U")])
        args, kwargs = fix_arguments(
            args, kwargs, QuantumGate, [("dim", 2), ("spec", None)]
        )
        super().__init__(*args, **kwargs)

    @property
    def dim(self) -> int:
        return Unitary.DIM

    @dim.setter
    def dim(self, dim: int):
        pass

    @property
    def parameters(self) -> tuple[num | expr | str, num | expr | str, num | expr | str]:
        """The 3-tuple of scalar values to be used as the parameter values."""
        return self._parameters

    @parameters.setter
    def parameters(
        self, parameters: tuple[num | expr | str, num | expr | str, num | expr | str]
    ):
        self._parameters = parameters

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        operator = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        param_theta = symbolize_expression(self.parameters[0], self.symbols_list)
        param_phi = symbolize_expression(self.parameters[1], self.symbols_list)
        param_lambda = symbolize_expression(self.parameters[2], self.symbols_list)
        operator = sp.Matrix(
            [
                [
                    sp.cos(param_theta / 2),
                    -sp.exp(sp.I * param_lambda) * sp.sin(param_theta / 2),
                ],
                [
                    sp.exp(sp.I * param_phi) * sp.sin(param_theta / 2),
                    sp.exp(sp.I * (param_phi + param_lambda)) * sp.cos(param_theta / 2),
                ],
            ]
        )
        operator = cast(operator, numerical=numerical, array=array_intermediate)
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


UNI = Unitary


class Pauli(QuantumGate):
    """A subclass for creating Pauli gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    The *Pauli matrices* :math:`\\Pauli_i` are a set of three :math:`2 \\times 2` matrices,

    .. math::

        \\begin{aligned}
            \\Pauli_1 &= \\Pauli_x \\equiv \\ket{0}\\bra{1} + \\ket{1}\\bra{0}
                = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}, \\\\
            \\Pauli_2 &= \\Pauli_y \\equiv -\\eye \\ket{0}\\bra{1} + \\eye \\ket{1}\\bra{0}
                = \\begin{bmatrix} 0 & -\\eye \\\\ \\eye & 0 \\end{bmatrix}, \\\\
            \\Pauli_3 &= \\Pauli_z \\equiv \\ket{0}\\bra{0} - \\ket{1}\\bra{1}
                = \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix},
        \\end{aligned}

    indexed here by :math:`i` (:python:`index`), which additionally includes the :math:`2`-dimensional identity matrix for :math:`i=0`.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    index : int
        The index of the desired Pauli matrix. Can take the following values:

        - :python:`0` (:math:`2`-dimensional identity matrix :math:`\\Identity`)
        - :python:`1` (Pauli-:math:`X` :math:`\\Pauli_x`)
        - :python:`2` (Pauli-:math:`Y` :math:`\\Pauli_y`)
        - :python:`3` (Pauli-:math:`Z` :math:`\\Pauli_z`)

    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    The Pauli gates are defined only for :math:`2`-dimensional (i.e., binary/qubit) systems.
    This means that the constructor does not take :python:`dim` as an argument, nor can the associated property be set.
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

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        operator = cast(
            Pauli.MATRICES[self.index], numerical=numerical, array=array_intermediate
        )
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


PAULI = Pauli


class GellMann(QuantumGate):
    """A subclass for creating Gell-Mann gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    The *Gell-Mann matrices* :math:`\\GellMann_i` are a set of eight :math:`3 \\times 3` matrices,

    .. raw:: latex

        \\begin{adjustwidth}{-2.5em}{0cm}

    .. math::

        \\begin{aligned}
            &\\GellMann_1 \\equiv \\ket{0}\\bra{1} + \\ket{1}\\bra{0}
                = \\begin{bmatrix} 0 & 1 & 0 \\\\ 1 & 0 & 0 \\\\ 0 & 0 & 0 \\end{bmatrix}, \\\\
            &\\GellMann_3 \\equiv \\ket{0}\\bra{0} - \\ket{1}\\bra{1}
                = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 0 \\end{bmatrix}, \\\\
            &\\GellMann_5 \\equiv -\\eye\\ket{0}\\bra{2} + \\eye\\ket{2}\\bra{0}
                = \\begin{bmatrix} 0 & 0 & -\\eye \\\\ 0 & 0 & 0 \\\\ \\eye & 0 & 0 \\end{bmatrix}, \\\\
            &\\GellMann_7 \\equiv -\\eye\\ket{2}\\bra{3} + \\eye\\ket{3}\\bra{2}
                = \\begin{bmatrix} 0 & 0 & 0 \\\\ 0 & 0 & -\\eye \\\\ 0 & \\eye & 0 \\end{bmatrix},
        \\end{aligned}
        \\quad
        \\begin{aligned}
            &\\GellMann_2 \\equiv -\\eye\\ket{0}\\bra{1} + \\eye \\ket{1}\\bra{0}
                = \\begin{bmatrix} 0 & -\\eye & 0 \\\\ \\eye & 0 & 0 \\\\ 0 & 0 & 0 \\end{bmatrix}, \\\\
            &\\GellMann_4 \\equiv \\ket{0}\\bra{2} + \\ket{2}\\bra{0}
                = \\begin{bmatrix} 0 & 0 & 1 \\\\ 0 & 0 & 0 \\\\ 1 & 0 & 0 \\end{bmatrix}, \\\\
            &\\GellMann_6 \\equiv \\ket{2}\\bra{3} + \\ket{3}\\bra{2}
                = \\begin{bmatrix} 0 & 0 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 1 & 0 \\end{bmatrix}, \\\\
            &\\GellMann_8 \\equiv \\frac{1}{\\sqrt{3}}\\bigl(\\ket{0}\\bra{0} + \\ket{1}\\bra{1} - 2\\ket{2}\\bra{2}\\bigr)
                = \\frac{1}{\\sqrt{3}}\\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & -2 \\end{bmatrix},
        \\end{aligned}

    .. raw:: latex

        \\end{adjustwidth}

    indexed here by :math:`i` (:python:`index`), which additionally includes the :math:`3`-dimensional identity matrix for :math:`i=0`.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    index : int
        The index of the desired Gell-Mann matrix. Can take the following values:

        - :python:`0` (:math:`3`-dimensional identity matrix :math:`\\Identity`)
        - :python:`1` (:math:`\\GellMann_1`)
        - :python:`2` (:math:`\\GellMann_2`)
        - :python:`3` (:math:`\\GellMann_3`)
        - :python:`4` (:math:`\\GellMann_4`)
        - :python:`5` (:math:`\\GellMann_5`)
        - :python:`6` (:math:`\\GellMann_6`)
        - :python:`7` (:math:`\\GellMann_7`)
        - :python:`8` (:math:`\\GellMann_8`)

    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    The Gell-Mann gates are defined only for :math:`3`-dimensional (i.e., ternary/qutrit) systems.
    This means that the constructor does not take :python:`dim` as an argument, nor can the associated property be set.
    """

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

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        operator = cast(
            GellMann.MATRICES[self.index], numerical=numerical, array=array_intermediate
        )
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


GM = GellMann


class Rotation(QuantumGate):
    """A subclass for creating rotation gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    The elementary *rotation matrices* :math:`\\Rotation_i` are a set of three :math:`2 \\times 2` matrices,

    .. math::

       \\begin{aligned}
           \\Rotation_1 &= \\Rotation_x = \\e^{-\\eye\\Pauli_{x}\\theta/2} =
               \\begin{bmatrix} \\cos(\\theta/2) & -\\eye\\sin(\\theta/2) \\\\
               -\\eye\\sin(\\theta/2) & \\cos(\\theta/2)  \\end{bmatrix}, \\\\
           \\Rotation_2 &= \\Rotation_y = \\e^{-\\eye\\Pauli_{y}\\theta/2} =
               \\begin{bmatrix} \\cos(\\theta/2) & -\\sin(\\theta/2) \\\\
               \\sin(\\theta/2) & \\cos(\\theta/2) \\end{bmatrix}, \\\\
           \\Rotation_3 &= \\Rotation_z = \\e^{-\\eye\\Pauli_{z}\\theta/2} =
               \\begin{bmatrix} \\e^{-\\eye\\theta/2} & 0 \\\\
               0 & \\e^{\\eye\\theta/2} \\end{bmatrix},
       \\end{aligned}

    where :math:`\\theta \\in \\Reals` is the *rotation angle* (:python:`angle`).

    These are fundamentally single-system gates, and so a copy of the specified gate is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    axis : int
        The index corresponding to the axis of the desired rotation matrix.
        Can take the following values:

        - :python:`1` (:math:`x`-rotation :math:`\\Rotation_x`)
        - :python:`2` (:math:`y`-rotation :math:`\\Rotation_y`)
        - :python:`3` (:math:`z`-rotation :math:`\\Rotation_z`)

    angle : num | expr | str
        The scalar value to be used as the rotation angle.
        Defaults to :python:`0`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

      .. raw:: latex

         \\vspace*{-0.5\\baselineskip}

    Note
    ----
    The rotation gates are defined only for :math:`2`-dimensional (i.e., binary/qubit) systems.
    This means that the constructor does not take :python:`dim` as an argument, nor can the associated property be set.
    """

    DIM = 2

    def __init__(
        self, *args, axis: int, angle: num | expr | str | None = None, **kwargs
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
    def angle(self) -> num | expr | str:
        """The scalar value to be used as the rotation angle."""
        return self._angle

    @angle.setter
    def angle(self, angle: num | expr | str):
        self._angle = angle

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        operator = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
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
                [
                    [sp.exp(-sp.I * angle / 2), 0],
                    [0, sp.exp(sp.I * angle / 2)],
                ]
            )
        operator = cast(operator, numerical=numerical, array=array_intermediate)
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


ROT = Rotation


class Phase(QuantumGate):
    """A subclass for creating phase gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    In :math:`\\Dimension` dimensions, a *phase operator* :math:`\\Phase` may be represented as a :math:`\\Dimension \\times \\Dimension` diagonal matrix

    .. math::

       \\begin{aligned}
           \\Phase(\\omega) &= \\sum\\limits_{k=0}^{\\Dimension - 1} \\omega^k \\ket{k}\\bra{k} \\\\
           &=
           \\begin{bmatrix}
               1 & 0 & 0 & \\ldots & 0 \\\\
               0 & \\omega & 0 & \\ldots & 0 \\\\
               0 & 0 & \\omega^2 & \\ldots & 0 \\\\
               \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
               0 & 0 & 0 & \\ldots & \\omega^{\\Dimension - 1}
           \\end{bmatrix}
       \\end{aligned}

    where :math:`\\omega \\in \\Complexes` is the *phase factor* (:python:`phase`).

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    phase : num | expr | str
        The phase factor.
        Defaults to the unit root given by :python:`sp.exp(2 * sp.pi * sp.I / self.dim)`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(
        self,
        *args,
        phase: num | expr | str | None = None,
        **kwargs,
    ):
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "P")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)
        phase = sp.exp(2 * sp.pi * sp.I / self.dim) if phase is None else phase
        self.phase = phase

    @property
    def phase(self) -> num | expr | str:
        """The phase value."""
        return self._phase

    @phase.setter
    def phase(self, phase: num | expr | str):
        self._phase = phase

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        operator = generate_zeros(
            self.dim, numerical=numerical, array=array_intermediate
        )
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        phase = to_numerical(
            symbolize_expression(self.phase, self.symbols_list), numerical=numerical
        )
        for k in range(0, self.dim):
            operator = operator + phase**k * ket(
                k, dim=self.dim, numerical=numerical, array=array_intermediate
            ) * bra(k, dim=self.dim, numerical=numerical, array=array_intermediate)
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


PHS = Phase


class Diagonal(QuantumGate):
    """A subclass for creating diagonal gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    In :math:`\\Dimension` dimensions, a *diagonal operator* :math:`\\Diagonal` may be represented as a :math:`\\Dimension \\times \\Dimension` diagonal matrix

    .. math::

       \\begin{aligned}
           \\Diagonal(\\lambda_0, \\lambda_1, \\ldots, \\lambda_{\\Dimension - 1})
           &= \\sum\\limits_{k=0}^{\\Dimension - 1} \\lambda_k\\ket{k}\\bra{k} \\\\
           &=
           \\begin{bmatrix}
               \\lambda_0 & 0 & 0 & \\ldots & 0 \\\\
               0 & \\lambda_1 & 0 & \\ldots & 0 \\\\
               0 & 0 & \\lambda_2 & \\ldots & 0 \\\\
               \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
               0 & 0 & 0 & \\ldots & \\lambda_{\\Dimension - 1}
           \\end{bmatrix}
       \\end{aligned}

    where :math:`\\{\\lambda_k : \\lambda_k \\in \\Complexes, \\; \\abs{\\lambda_k} = 1\\}_{k=0}^{\\Dimension - 1}` are the main diagonal *entries* (:python:`entries`).

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    entries : dict[int | list[int], num | expr | str]
        A dictionary in which the keys are level specifications (integer or list of integers) and the values are scalars.
    exponentiation : bool
        Whether to exponentiate (with imaginary unit) the values given in :python:`entries`.
        Defaults to :python:`False`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    Levels that are unspecified in the :python:`entries` argument all have a corresponding matrix element of :python:`1`, regardless of the value of :python:`exponentiation`.
    """

    def __init__(
        self,
        *args,
        entries: dict[int | list[int], num | expr | str],
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
    def entries(self) -> dict[int | list[int], num | expr | str]:
        """A dictionary in which the keys are level specifications (integer or list of integers) and the values are scalars."""
        return self._entries

    @entries.setter
    def entries(self, entries: dict[int | list[int], num | expr | str]):
        self._entries = entries

    @property
    def exponentiation(self) -> bool:
        """Whether to exponentiate (with imaginary unit) the values given in :python:`entries`."""
        return self._exponentiation

    @exponentiation.setter
    def exponentiation(self, exponentiation: bool):
        self._exponentiation = exponentiation

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        operator = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        for key, value in self.entries.items():
            if self.exponentiation is True:
                coefficient = symbolize_expression(
                    "exp(I*(" + str(value) + "))", self.symbols_list
                )
            else:
                coefficient = symbolize_expression(str(value), self.symbols_list)
            coefficient = to_numerical(coefficient, numerical=numerical)
            projector = ket(
                key, dim=self.dim, numerical=numerical, array=array_intermediate
            ) * bra(key, dim=self.dim, numerical=numerical, array=array_intermediate)
            operator = operator + (coefficient - 1) * projector
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


DIAG = Diagonal


class Swap(QuantumGate):
    """A subclass for creating SWAP (exchange) gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    In :math:`\\Dimension` dimensions, a *SWAP operator* :math:`\\Swap` between two systems :math:`A` and :math:`B` may be represented as a :math:`\\Dimension^2 \\times \\Dimension^2` matrix

    .. math::

       \\Swap^{\\indices{A,B}} =
           \\sum\\limits_{j,k=0}^{\\Dimension - 1}
           {\\ket{j}\\bra{k}}^{\\indices{A}} \\otimes {\\ket{k}\\bra{j}}^{\\indices{B}}

    where the identity operator acts on all other systems.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    targets : list[int, int]
        A list of exactly two indices corresponding to the systems to be swapped.
        Is an argument of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`, so can be specified positionally in :python:`*args`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = default_arguments(
            args, kwargs, QuantumGate, [("label", "S"), ("family", "SWAP")]
        )
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)
        if len(self.targets) != 2:
            raise ValueError(
                """A :python:`targets` list of exactly two (2) system indices must be provided."""
            )

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        permutation = [k for k in range(0, self.num_systems)]
        permutation[self.targets[0]], permutation[self.targets[1]] = (
            permutation[self.targets[1]],
            permutation[self.targets[0]],
        )
        possibility = [k for k in range(0, self.dim)]
        possibilities = [possibility for _ in range(0, self.num_systems)]
        combinations = list(itertools.product(*possibilities))

        matrix = generate_zeros(
            self.dim**self.num_systems, numerical=numerical, array=array_intermediate
        )
        for n in range(0, self.dim**self.num_systems):
            level = list(combinations[n])
            permuted = [level[permutation[k]] for k in range(0, self.num_systems)]
            matrix = matrix + ket(
                permuted, dim=self.dim, numerical=numerical, array=array_intermediate
            ) * bra(level, dim=self.dim, numerical=numerical, array=array_intermediate)
        return cast(matrix, numerical=numerical, array=array)


SWAP = Swap


class Summation(QuantumGate):
    """A subclass for creating SUM (summation) gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    The *SUM gate* is essentially a generalization of the NOT gate. In :math:`\\Dimension` dimensions, it is defined as the operator

    .. math:: \\SUM(n) = \\sum\\limits_{k=0}^{\\Dimension - 1} \\ket{k \\oplus n}\\bra{k}

    where :math:`n \\in \\Integers_{\\geq 0}` (:python:`shift`) is the *shift* parameter, and :math:`k \\oplus n \\equiv k + n \\mathrel{\\mathrm{mod}} \\Dimension`.

    The case of :math:`n = 1` is known as the *shift* operator, and represents a (non-Hermitian) generalization of the Pauli-:math:`X` :math:`\\Pauli_x` operator to :math:`\\Dimension` dimensions.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    shift : int
        The summation shift parameter.
        Must be a non-negative integer.
        Defaults to :python:`1`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

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

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        summation = generate_zeros(
            self.dim, numerical=numerical, array=array_intermediate
        )
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )
        for k in range(0, self.dim):
            oplus = (k + self.shift) % self.dim
            summation = summation + ket(
                oplus, dim=self.dim, numerical=numerical, array=array_intermediate
            ) * bra(k, dim=self.dim, numerical=numerical, array=array_intermediate)
        matrix = generate_identity(1, numerical=numerical, array=array_intermediate)
        for m in range(0, self.num_systems):
            if m in list(self.targets):
                matrix = tensor_product(matrix, summation)
            else:
                matrix = tensor_product(matrix, identity)
        return cast(matrix, numerical=numerical, array=array)


SUM = Summation


class Not(Summation):
    """A subclass for creating NOT (logical *negation* or "bit-flip") gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    The *NOT gate* is essentially a specialization of the SUM gate to :math:`2`-dimensional systems. In other words, this means that it is exactly equivalent to the Pauli-:math:`X` gate, having the matrix representation

    .. math::
       
       \\begin{aligned}
           \\NOT &= \\ket{0}\\bra{1} + \\ket{1}\\bra{0} \\\\
           &= \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}.
       \\end{aligned}

    As such, this class exists purely to simplify access to this operation.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    NOT gates are defined only for :math:`2`-dimensional (i.e., binary/qubit) systems.
    This means that the constructor does not take :python:`dim` as an argument, nor can the associated property be set.
    """

    DIM = 2
    SHIFT = 1

    def __init__(self, *args, **kwargs):
        args, kwargs = default_arguments(
            args, kwargs, QuantumGate, [("label", "X"), ("family", "TARG")]
        )
        args, kwargs = fix_arguments(
            args, kwargs, QuantumGate, [("dim", 2), ("spec", None)]
        )
        super().__init__(*args, **kwargs)

    @property
    def dim(self) -> int:
        return Not.DIM

    @dim.setter
    def dim(self, dim: int):
        pass

    @property
    def shift(self) -> int:
        return Not.SHIFT

    @shift.setter
    def shift(self, shift: int):
        pass


NOT = Not


class Hadamard(QuantumGate):
    """A subclass for creating Hadamard gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    The elementary *Hadamard gate* :math:`\\Hadamard` (for qubits) corresponds to the :math:`2 \\times 2` *Hadamard matrix*

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
           &=
           \\begin{bmatrix}
               1 & 1 & 1 & \\ldots & 1 \\\\
               1 & \\omega^{\\Dimension - 1} & \\omega^{2(\\Dimension - 1)} & \\ldots & \\omega^{(\\Dimension - 1)^2} \\\\
               1 & \\omega^{\\Dimension - 2} & \\omega^{2(\\Dimension - 2)} & \\ldots & \\omega^{(\\Dimension - 1)(\\Dimension - 2)} \\\\
               \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
               1 & \\omega & \\omega^{2} & \\ldots & \\omega^{\\Dimension - 1}
           \\end{bmatrix}
       \\end{aligned}

    where :math:`\\omega_\\Dimension \\equiv \\e^{2\\pi\\eye/\\Dimension}`.

    This is fundamentally a single-system gate, and so a copy is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(self, *args, **kwargs):
        args, kwargs = default_arguments(args, kwargs, QuantumGate, [("label", "H")])
        args, kwargs = fix_arguments(args, kwargs, QuantumGate, [("spec", None)])
        super().__init__(*args, **kwargs)

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        omega = to_numerical(sp.exp(2 * sp.pi * sp.I / self.dim), numerical=numerical)
        operator = generate_zeros(
            self.dim, numerical=numerical, array=array_intermediate
        )
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                operator = operator + (
                    omega ** (j * (self.dim - i))
                    * ket(
                        i, dim=self.dim, numerical=numerical, array=array_intermediate
                    )
                    * bra(
                        j, dim=self.dim, numerical=numerical, array=array_intermediate
                    )
                )
        operator = operator * to_numerical(1 / sp.sqrt(self.dim), numerical=numerical)
        identity = generate_identity(
            self.dim, numerical=numerical, array=array_intermediate
        )

        targets_compliment = list(set(self.systems) ^ set(self.targets))
        ordered = arrange([targets_compliment, self.targets], [identity] + [operator])
        matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


HAD = Hadamard


class Fourier(QuantumGate):
    """A subclass for creating Fourier (quantum [discrete] Fourier transform [QFT]) gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    The elementary *Fourier operator* :math:`\\QFT` for a single :math:`\\Dimension`-dimensional qudit may be represented as the :math:`\\Dimension \\times \\Dimension` matrix

    .. math::
        
        \\begin{aligned}
            \\QFT &= \\frac{1}{\\sqrt{\\Dimension}} \\sum\\limits_{j,k=0}^{\\Dimension - 1}
                \\omega_{\\Dimension}^{jk} \\ket{j}\\bra{k} \\\\
            &= \\frac{1}{\\sqrt{\\Dimension}}
            \\begin{bmatrix}
                1 & 1 & 1 & 1 & \\ldots & 1 \\\\
                1 & \\omega & \\omega^2 & \\omega^3 & \\ldots & \\omega^{\\Dimension - 1} \\\\
                1 & \\omega^2 & \\omega^4 & \\omega^6 & \\ldots & \\omega^{2(\\Dimension - 1)} \\\\
                1 & \\omega^3 & \\omega^6 & \\omega^9 & \\ldots & \\omega^{3(\\Dimension - 1)} \\\\
                \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
                1 & \\omega^{\\Dimension - 1} & \\omega^{2(\\Dimension - 1)} & \\omega^{3(\\Dimension - 1)} & \\ldots & \\omega^{(\\Dimension - 1)(\\Dimension - 1)} \\\\
            \\end{bmatrix}
        \\end{aligned}

    where :math:`\\omega \\equiv \\omega_{\\Dimension} \\equiv \\e^{2\\pi\\eye/\\Dimension}`.

    In the case of :math:`N` qudits, it is easier to characterize the *multipartite Fourier operator* :math:`\\QFT_N` not by its matrix form but by the transformation it imposes, to which its action on the basis state :math:`\\bigotimes\\limits_{\\ell=1}^{N} \\ket{j_\\ell} \\equiv \\ket{j_1, \\ldots, j_N}` (where :math:`j_\\ell \\in \\Integers_{0}^{\\Dimension - 1}`) is

    .. math::
        
        \\ket{j_1, \\ldots, j_N} \\stackrel{\\QFT_N}{\\longrightarrow}
            \\frac{1}{\\sqrt{\\Dimension^N}}
            \\bigotimes\\limits_{\\ell=1}^{N}
            \\sum\\limits_{k_\\ell=0}^{\\Dimension - 1}
            \\e^{2\\pi\\eye j k_\\ell \\Dimension^{-\\ell}} \\ket{k_\\ell}
    
    where :math:`j \\equiv \\sum\\limits_{\\ell=1}^{N} j_\\ell \\Dimension^{N - \\ell}`.

    If :python:`composite` is :python:`True`, the composite form :math:`\\QFT_N` is applied to the subsystems specified by :python:`targets` in:
    
    - *ascending* order if :python:`reverse` is :python:`False`
    - *descending* order if :python:`reverse` is :python:`True`

    If :python:`composite` is :python:`False`, a copy of the elementary form :math:`\\QFT` is placed on each of the subsystems corresponding to the indices in the :python:`targets` property.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    composite : bool
        Whether the composite (multipartite) Fourier gate is to be used.
        If :python:`False`, copies of the elementary Fourier gate are placed on each index specified in :python:`targets`.
        Defaults to :python:`True`.
    reverse : bool
        Whether to reverse the order in which the composite (multipartite) Fourier gate is applied.
        Has no effect when :python:`composite` is :python:`False`.
        Defaults to :python:`False`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
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
        """Whether to reverse the order in which the composite (multipartite) Fourier gate is applied.
        Has no effect when :python:`self.composite` is :python:`False`.
        """
        return self._reverse

    @reverse.setter
    def reverse(self, reverse: bool):
        self._reverse = reverse

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        if self.composite is True:
            # Easy way: use decomposition instead of QFT definition.
            targets = sorted(self.targets, reverse=self.reverse)
            size = len(targets)
            QFT = []
            for i, t in enumerate(targets):
                count = size - i
                for j in range(0, count):
                    if j == 0:
                        QFT.append(
                            Hadamard(
                                targets=[t],
                                num_systems=self.num_systems,
                                dim=self.dim,
                                numerical=numerical,
                                array=array_intermediate,
                            )
                        )
                    else:
                        QFT.append(
                            Phase(
                                targets=[t],
                                controls=[targets[i + j]],
                                num_systems=self.num_systems,
                                dim=self.dim,
                                numerical=numerical,
                                array=array_intermediate,
                                exponent=sp.Rational(1, (self.dim**j)),
                                label=f"1 / {self.dim**j}",
                                family="GATE",
                            )
                        )
            matrix = generate_identity(
                self.dim**self.num_systems,
                numerical=numerical,
                array=array_intermediate,
            )
            for gate in QFT:
                matrix = matrix_multiplication(gate.output(), matrix)
        else:
            omega = to_numerical(
                sp.exp(2 * sp.pi * sp.I / self.dim), numerical=numerical
            )
            operator = generate_zeros(
                self.dim, numerical=numerical, array=array_intermediate
            )
            for i in range(0, self.dim):
                for j in range(0, self.dim):
                    operator = operator + (
                        omega ** (j * i)
                        * ket(
                            i,
                            dim=self.dim,
                            numerical=numerical,
                            array=array_intermediate,
                        )
                        * bra(
                            j,
                            dim=self.dim,
                            numerical=numerical,
                            array=array_intermediate,
                        )
                    )
            operator = operator * to_numerical(
                1 / sp.sqrt(self.dim), numerical=numerical
            )
            identity = generate_identity(
                self.dim, numerical=numerical, array=array_intermediate
            )
            targets_compliment = list(set(self.systems) ^ set(self.targets))
            ordered = arrange(
                [targets_compliment, self.targets], [identity] + [operator]
            )
            matrix = tensor_product(*ordered)
        return cast(matrix, numerical=numerical, array=array)


QFT = Fourier


class Measurement(QuantumGate):
    """A subclass for creating measurement gates and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so inherits all of its attributes, properties, and methods.

    Instances of this class each describe a (non-linear) operation in which the input state (:math:`\\op{\\rho}`) is quantum-mechanically *measured* (against the forms in specified in :python:`operators`) and subsequently mutated according to its predicted post-measurement form (i.e., the sum of all possible measurement outcomes). This yields the transformed states:

    - When :python:`observable` is :python:`False`
      (:python:`operators` is a list of Kraus operators or projectors :math:`\\Kraus_i`):

    .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger

    - When :python:`observable` is :python:`True`
      (:python:`operators` is a list of observables :math:`\\Observable_i`):

    .. math:: \\op{\\rho}^\\prime = \\sum_i \\trace[\\Observable_i \\op{\\rho}] \\Observable_i

    The items in the list :python:`operators` can also be vectors (e.g., :math:`\\ket{\\xi_i}`), in which case each is converted into its corresponding matrix representation (e.g., :math:`\\Kraus_i = \\ket{\\xi_i}\\bra{\\xi_i}`) prior to any measurement(s).

    Note also that this method does not check for validity of supplied POVMs or the completeness of sets of observables, nor does it renormalize the post-measurement state.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    operators : list[mat | arr | QuantumObject]
        The operator(s) with which to perform the measurement.
        These would typically be a (complete) set of Kraus operators forming a POVM,
        a (complete) set of (orthogonal) projectors forming a PVM,
        or a set of observables constituting a complete basis for the relevant state space.
    observable : bool
        Whether to treat the items in :python:`operators` as observables (as opposed to Kraus operators or projectors).
        Defaults to :python:`False`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.

    Note
    ----
    In quantum mechanics, measurement operations constitute (in general) non-linear and non-unitary transformations of (normalized) state vectors and density operators. As such, they cannot be represented by matrices, and so the :python:`matrix` property therefore does not return a valid representation of the measurement operation.

    Note
    ----
    The :python:`targets` argument must be specified as a list of numerical indices of the subsystem(s) to be measured. These indices must be consecutive, and their number must match the number of systems spanned by all given operators.
    """

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
        """Whether to treat the items in the :python:`operators` property as observables (as opposed to Kraus operators or projectors)."""
        return self._observable

    @observable.setter
    def observable(self, observable: bool):
        self._observable = observable

    def matrices(
        self, numerical: bool | None = None, array: bool | None = None
    ) -> list[mat | arr]:
        """A list of matrix representations of all operators in the :python:`operators` property.

        Is a read-only property.

        This is used specifically in the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class when instances of it contain :python:`Measurement` gate instances in their :python:`gates` property.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        matrices = []
        identity = generate_identity(
            self.dim, numerical=self.numerical, array=array_intermediate
        )
        targets_compliment = list(set(self.systems) ^ set(self.targets))
        for operator in self.operators:
            operator = densify(extract_representation(operator))
            operator = cast(operator, numerical=numerical, array=array_intermediate)
            ordered = arrange(
                [targets_compliment, [min(self.targets)]], [identity] + [operator]
            )
            matrix = tensor_product(*ordered)
            matrices.append(cast(matrix, numerical=numerical, array=array))
        return matrices

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        return generate_identity(
            self.dim**self.num_systems, numerical=numerical, array=array
        )


METER = Measurement


class GateInterleave(QuantumGate):
    """Compose two or more :py:class:`~qhronology.quantum.gates.QuantumGate` instances together by interleaving them.

    This is achieved by multiplying the gates' matrix representations. For example, for gates described by the multipartite operators :math:`\\op{A} \\otimes \\Identity` and :math:`\\Identity \\otimes \\op{B}`, their interleaved composition is

    .. math::

       (\\op{A} \\otimes \\Identity) \\cdot (\\Identity \\otimes \\op{B}) = \\op{A} \\otimes \\op{B}.

    While this is a subclass of :py:class:`~qhronology.quantum.gates.QuantumGate`, all of its inherited properties, except for those corresponding to arguments in its constructor, are read-only. This is because they are calculated from their corresponding properties in the individual instances contained within the :python:`gates` property.

    Arguments
    ---------
    *gates : QuantumGate
        :py:class:`~qhronology.quantum.gates.QuantumGate` instances to be interleaved.
    merge : bool
        Whether to merge the gates together diagrammatically.
        Defaults to :python:`False`.
    num_systems : int
        The (total) number of systems which the gate spans.
        Must be a non-negative integer.
        Defaults to :python:`max([gate.num_systems for gate in gates])`.
    numerical : bool
        Whether to cast the gate's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the gate's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.
    conjugate : bool
        Whether to perform Hermitian conjugation on the composite gate when it is called.
        Defaults to :python:`False`.
    exponent : num | expr | str
        A numerical or string representation of a scalar value to which composite gate's total matrix representation is exponentiated.
        Must be a non-negative integer.
        Defaults to :python:`1`.
    coefficient : num | expr | str
        A numerical or string representation of a scalar value by which the composite gate's matrix representation is multiplied.
        Performed after exponentiation.
        Defaults to :python:`1`.
    label : str
        The unformatted string used to represent the gate in mathematical expressions.
        Defaults to :python:`"⊗".join([gate.label for gate in gates])`.
    notation : str
        The formatted string used to represent the gate in mathematical expressions.
        When not :python:`None`, overrides the value passed to :python:`label`.
        Not intended to be set by the user in most cases.
        Defaults to :python:`None`.

    Note
    ----
    Care should be taken to ensure that gates passed to this class all have the same :python:`num_systems` value and do not have overlapping :python:`targets`, :python:`controls`, and :python:`anticontrols` properties.

    Note
    ----
    The resulting visualization (using the inherited :py:meth:`~qhronology.quantum.gates.QuantumGate.diagram` method or in circuit diagrams) may not be accurate in every case. However, the composed matrix should still be correct.
    """

    def __init__(
        self,
        *gates: QuantumGate,
        merge: bool | None = None,
        num_systems: int | None = None,
        numerical: bool | None = None,
        array: bool | None = None,
        conjugate: bool | None = None,
        exponent: num | expr | str | None = None,
        coefficient: num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
    ):
        self.gates = [copy.deepcopy(gate) for gate in gates]
        merge = False if merge is None else merge
        self.merge = merge
        label = "⊗".join([gate.label for gate in gates]) if label is None else label
        num_systems = max([gate.num_systems for gate in gates]) if num_systems is None else num_systems

        super().__init__(
            spec=None,
            num_systems=num_systems,
            numerical=numerical,
            array=array,
            conjugate=conjugate,
            exponent=exponent,
            coefficient=coefficient,
            label=label,
            notation=notation,
        )

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
        """Variable-length list of :py:class:`~qhronology.quantum.gates.QuantumGate` instances to be composited."""
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
        return self._num_systems

    @num_systems.setter
    def num_systems(self, num_systems: int):
        num_systems_min = max(
            [
                max(gate.targets + gate.controls + gate.anticontrols) + 1
                for gate in self.gates
            ]
        )
        if num_systems < num_systems_min:
            raise ValueError(
                f"""One or more of the interleaved gates cannot have its number of systems set to {num_systems}."""
            )
        else:
            for index, gate in enumerate(self.gates):
                self.gates[index].num_systems = num_systems
        self._num_systems = num_systems

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
            raise ValueError("""Mismatch between one or more of the dimensions.""")
        return dim[0]

    @dim.setter
    def dim(self, dim: int):
        pass

    @property
    def substitutions(self) -> list[tuple[num | expr | str, num | expr | str]]:
        substitutions = []
        for gate in self.gates:
            substitutions += gate.substitutions
        return substitutions

    @substitutions.setter
    def substitutions(self, substitutions):
        pass

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        matrix = generate_identity(
            self.dim**self.num_systems, numerical=numerical, array=array_intermediate
        )
        for gate in self.gates:
            matrix = matrix_multiplication(
                gate.output(numerical=numerical, array=array_intermediate), matrix
            )
        return cast(matrix, numerical=numerical, array=array)

    def output(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        exponent: bool | num | expr | str | None = None,
        coefficient: bool | num | expr | str | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        gate = self.matrix(numerical=numerical, array=array_intermediate)

        # Exponentiate
        if exponent is None or exponent is True:
            exponent = self.exponent
        if exponent != 1 and exponent is not False:
            exponent = symbolize_expression(exponent, self.symbols_list)
            plus = to_numerical(
                (1 + sp.exp(sp.I * sp.pi * exponent)) / 2, numerical=numerical
            )
            minus = to_numerical(
                (1 - sp.exp(sp.I * sp.pi * exponent)) / 2, numerical=numerical
            )
            identity = generate_identity(
                self.dim**self.num_systems,
                numerical=numerical,
                array=array_intermediate,
            )
            gate = plus * identity + minus * gate

        # Coefficient
        if coefficient is None or coefficient is True:
            coefficient = self.coefficient
        if coefficient is not False:
            coefficient = symbolize_expression(coefficient, self.symbols_list)
        else:
            coefficient = 1
        if coefficient != 1 and coefficient is not False:
            coefficient = to_numerical(coefficient, numerical=numerical)
            gate = coefficient * gate

        gate = symbolize_expression(gate, self.symbols_list)

        # Conditions
        substitutions = self.substitutions if substitutions is None else substitutions
        substitutions = symbolize_substitutions(substitutions, self.symbols_list)
        gate = apply_substitutions(gate, substitutions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            gate = recursively_simplify(gate, substitutions)

        # Conjugation
        conjugate = self.conjugate if conjugate is None else conjugate
        if conjugate is True:
            gate = conjugate_transpose(gate)

        return cast(gate, numerical=numerical, array=array)


INTERLEAVE = GateInterleave


class GateStack(GateInterleave):
    """Compose two or more :py:class:`~qhronology.quantum.gates.QuantumGate` instances together by "stacking" them vertically.

    This is achieved by computing the tensor product of the gates' matrix representations.
    For example, for gates described by the multipartite operators :math:`\\op{A} \\otimes \\Identity` and :math:`\\Identity \\otimes \\op{B}`, their stacked composition is

    .. math::

       (\\op{A} \\otimes \\Identity) \\otimes (\\Identity \\otimes \\op{B})
       = \\op{A} \\otimes \\Identity \\otimes \\Identity \\otimes \\op{B}.

    This class is derived from the :py:class:`~qhronology.quantum.gates.QuantumGate` class, and so should be used in much the same way.

    Arguments
    ---------
    *gates : QuantumGate
        :py:class:`~qhronology.quantum.gates.QuantumGate` instances to be stacked.
    merge : bool
        Whether to merge the gates together diagrammatically.
        Defaults to :python:`False`.
    num_systems : int
        The (total) number of systems which the gate spans.
        Must be a non-negative integer.
        Defaults to :python:`sum([gate.num_systems for gate in gates])`.
    numerical : bool
        Whether to cast the gate's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
        Defaults to :python:`False`.
    array : bool
        Whether to cast the gate's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
        Defaults to :python:`False`.
    conjugate : bool
        Whether to perform Hermitian conjugation on the composite gate when it is called.
        Defaults to :python:`False`.
    exponent : num | expr | str
        A numerical or string representation of a scalar value to which composite gate's total matrix representation is exponentiated.
        Defaults to :python:`1`.
    coefficient : num | expr | str
        A numerical or string representation of a scalar value by which the composite gate's matrix representation is multiplied.
        Performed after exponentiation.
        Defaults to :python:`1`.
    label : str
        The unformatted string used to represent the gate in mathematical expressions.
        Defaults to :python:`"⊗".join([gate.label for gate in gates])`.
    notation : str
        The formatted string used to represent the gate in mathematical expressions.
        When not :python:`None`, overrides the value passed to :python:`label`.
        Not intended to be set by the user in most cases.
        Defaults to :python:`None`.
    """

    def __init__(
        self,
        *gates: QuantumGate,
        merge: bool | None = None,
        num_systems: int | None = None,
        numerical: bool | None = None,
        array: bool | None = None,
        conjugate: bool | None = None,
        exponent: num | expr | str | None = None,
        coefficient: num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
    ):
        num_systems = sum([gate.num_systems for gate in gates]) if num_systems is None else num_systems
        super().__init__(
            *gates,
            merge=merge,
            num_systems=num_systems,
            numerical=numerical,
            array=array,
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
        return self._num_systems

    @num_systems.setter
    def num_systems(self, num_systems: int):
        gate_last = self.gates[-1]
        num_systems_last_min = (
            max(gate_last.targets + gate_last.controls + gate_last.anticontrols) + 1
        )
        num_systems_except_last = max(
            0, sum([gate.num_systems for gate in self.gates[0:-1]])
        )
        num_systems_total_min = num_systems_last_min + num_systems_except_last
        if num_systems < num_systems_total_min:
            raise ValueError(
                f"""The number of systems of the stack of gates ({num_systems_total_min}) cannot be less than the number of systems specified ({num_systems})."""
            )
        else:
            self.gates[-1].num_systems = num_systems_last_min + (
                num_systems - num_systems_total_min
            )
        self._num_systems = num_systems

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        matrices = [
            gate.output(numerical=numerical, array=array_intermediate)
            for gate in self.gates
        ]
        matrix = tensor_product(*matrices)
        return cast(matrix, numerical=numerical, array=array)


STACK = GateStack


class _Single(QuantumGate):
    """A :py:class:`~qhronology.quantum.gates.QuantumGate` subclass for creating single-cell abstract quantum gates.

    Used exclusively internally (for visualization purposes).
    """

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

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        return generate_identity(
            self.dim**self.num_systems, numerical=numerical, array=array
        )


class _Empty(QuantumGate):
    """A :py:class:`~qhronology.quantum.gates.QuantumGate` subclass for creating single-cell empty quantum gates.

    Used exclusively internally (for visualization purposes).
    """

    def __init__(self, *args, family: str | None = None, **kwargs):
        family = Families.TERM.value if family is None else family
        super().__init__(
            *args, spec=None, targets=[0], num_systems=1, family=family, **kwargs
        )

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        return generate_identity(
            self.dim**self.num_systems, numerical=numerical, array=array
        )


class _Wormhole(QuantumGate):
    """A :py:class:`~qhronology.quantum.gates.QuantumGate` subclass for creating single-cell wormhole (mouth) quantum gates.

    Used exclusively internally (for visualization purposes).
    """

    def __init__(self, *args, family: str | None = None, **kwargs):
        family = Families.WORMHOLE.value if family is None else family
        super().__init__(
            *args, spec=None, targets=[0], num_systems=1, family=family, **kwargs
        )

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        return generate_identity(
            self.dim**self.num_systems, numerical=numerical, array=array
        )
