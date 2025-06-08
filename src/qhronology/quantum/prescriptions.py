# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
A class for the creation of quantum circuits containing closed timelike curves.
Classes and functions implementing quantum prescriptions of time travel.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

import copy

import numpy as np
import sympy as sp
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import num, sym, mat, Forms, Kinds, matrix_form
from qhronology.utilities.helpers import (
    adjust_targets,
    count_systems,
    count_dims,
    extract_matrix,
    extract_conditions,
    flatten_list,
    assemble_composition,
    recursively_simplify,
)

from qhronology.quantum.states import QuantumState
from qhronology.quantum.gates import QuantumGate
from qhronology.quantum.circuits import QuantumCircuit

from qhronology.mechanics.operations import densify, columnify, partial_trace
from qhronology.mechanics.quantities import trace


class QuantumCTC(QuantumCircuit):
    """A class for creating quantum circuit models of quantum interactions near
    closed timelike curves and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class,
    and so inherits all of its attributes, properties, and methods.

    Instances provide complete descriptions of quantum circuits involving antichronological time
    travel. The class however does not possess any ability to compute the output state
    (e.g., resolve temporal paradoxes) of the circuit;
    this is functionality that is associated with the specific prescriptions of quantum time travel,
    and such prescriptions are implemented as subclasses.

    Arguments
    ---------
    *args
        Variable length argument list, passed directly to the constructor ``__init__``  of the
        superclass :py:class:`~qhronology.quantum.circuits.QuantumCircuit`.
    circuit : QuantumCircuit
        An instance of the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class.
        The values of its attributes override any other values specified in ``*args`` and
        ``**kwargs``.
        Defaults to ``None``.
    systems_respecting : int | list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
        Defaults to ``[]``.
    systems_violating : int | list[int]
        The numerical indices of the chronology-violating (CV) subsystems.
        Defaults to ``[]``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.circuits.QuantumCircuit`.

    Note
    ----
    The lists of indices specified in ``systems_respecting`` and ``systems_violating`` must both be
    contiguous.
    Additionally, the circuit's inputs (``inputs``) are treated as one contiguous total state,
    with the indices of its subsystems exactly matching those specified in ``systems_respecting``.

    Note
    ----
    It is best practice to specify only one of either ``systems_violating`` or
    ``systems_violating``, never both.
    The properties associated with both of these constructor arguments automatically ensure that
    they are always complementary (with respect to the entire system space), and so only one needs
    to be specified.

    Note
    ----
    The ``circuit`` argument can be used to merge the value of every attribute from a pre-existing
    :py:class:`~qhronology.quantum.circuits.QuantumCircuit` instance into the
    :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` instance.
    Any such mergers override the values of the attributes associated with the other arguments
    specified in the constructor. It is best practice to specify either of:

    - only ``circuit`` and one of either ``systems_respecting`` or ``systems_violating``

    - ``*args`` and ``**kwargs`` (like a typical initialization of a
      :py:class:`~qhronology.quantum.circuits.QuantumCircuit` instance)
      without specifying ``circuit``

    Note
    ----
    The total interaction between the CR and CV systems is expected to be unitary,
    and so the sequence of gates in ``gates`` cannot contain any non-unitary gates
    (e.g., measurement operations).

    Note
    ----
    Post-processing (e.g., traces and postselections) cannot be performed on any
    chronology-violating (CV) systems (i.e., those corresponding to indices specified in
    ``systems_violating``).
    """

    def __init__(
        self,
        *args,
        circuit: QuantumCircuit | None = None,
        systems_respecting: list[int] | None = None,
        systems_violating: list[int] | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        if circuit is not None:
            self.__dict__ = copy.deepcopy(circuit.__dict__)

        if hasattr(self, "_systems_respecting") is False:
            systems_respecting = (
                [] if systems_respecting is None else systems_respecting
            )
            systems_violating = [] if systems_violating is None else systems_violating
            if len(systems_respecting) == 0 and len(systems_violating) == 0:
                raise ValueError(
                    "Either ``systems_respecting`` or ``systems_violating`` must be set."
                )
            if len(systems_respecting) != 0 and len(systems_violating) != 0:
                if set(self.systems) != set(systems_respecting) | set(
                    systems_violating
                ):
                    raise ValueError(
                        "The union of ``systems_respecting`` and ``systems_violating`` is \
                        inequivalent to the entire system's structure."
                    )

            self.systems_respecting = systems_respecting

    @property
    def systems_respecting(self) -> list[int]:
        """The numerical indices of the chronology-respecting (CR) subsystems."""
        return self._systems_respecting

    @systems_respecting.setter
    def systems_respecting(self, systems_respecting: list[int]):
        self._systems_respecting = systems_respecting
        self._systems_respecting = list(set(self._systems_respecting))

    @property
    def systems_violating(self) -> list[int]:
        """The numerical indices of the chronology-violating (CV) subsystems."""
        return list(set(self.systems) ^ set(self.systems_respecting))

    @systems_violating.setter
    def systems_violating(self, systems_violating: list[int]):
        systems_respecting = list(set(self.systems) ^ set(systems_violating))
        self.systems_respecting = systems_respecting

    @property
    def input_is_vector(self) -> bool:
        """Whether all states in ``inputs`` are vector states."""
        is_vector = True
        if any(
            form != Forms.VECTOR.value for form in [state.form for state in self.inputs]
        ):
            is_vector = False
        return is_vector

    def input(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        norm: bool | num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        debug: bool | None = None,
    ) -> QuantumState:
        """Construct the composite chronology-respecting (CR) input state of the closed timelike
        curve as a :py:class:`~qhronology.quantum.states.QuantumState` instance and return it.

        This is computed as the tensor product of the individual gates in the order in which they
        appear in the ``inputs`` property.
        Is a vector state only when all of the component states are vectors.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the state.
            If ``False``, does not substitute the conditions.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the state.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the state.
            Defaults to ``False``.
        norm : bool | num | sym | str
            The value to which the state is normalized.
            If ``True``, normalizes to a value of :math:`1`.
            If ``False``, does not normalize.
            Defaults to ``False``.
        label : str
            The unformatted string used to represent the state in mathematical expressions.
            Must have a non-zero length.
            Defaults to ``"⊗".join([state.label for state in self.inputs])``.
        notation : str
            The formatted string used to represent the state in mathematical expressions.
            When not ``None``, overrides the value passed to ``label``.
            Must have a non-zero length.
            Not intended to be set by the user in most cases.
            Defaults to ``None``.
        debug : bool
            Whether to print the internal state (held in ``matrix``) on change.
            Defaults to ``False``.

        Returns
        -------
        mat
            The total input state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        """
        conditions = self.conditions if conditions is None else conditions
        label = (
            "⊗".join([state.label for state in self.inputs]) if label is None else label
        )
        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        if self.input_is_vector is True:
            form = Forms.VECTOR.value
            kind = Kinds.PURE.value
        inputs = [state.output(conjugate=False) for state in self.inputs]
        if self.input_is_vector is False:
            inputs = [densify(state) for state in inputs]
        input_state = sp.Matrix(TensorProduct(*inputs))

        if count_systems(input_state, self.dim) != len(self.systems_respecting):
            raise ValueError(
                "The size of the given input state(s) does not match that specified by the \
                property ``systems_respecting``."
            )

        input_state = QuantumState(
            spec=input_state,
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            input_state.simplify()

        input_state = QuantumState(
            form=form,
            kind=kind,
            spec=input_state.output(),
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            conjugate=conjugate,
            norm=norm,
            label=label,
            notation=notation,
            debug=debug,
        )

        return input_state

    # The four methods below merely output the reduced states, so the ``systems_respective`` and
    # ``systems_violating`` of the base class acts just like extra traces.
    def output_violating(self) -> mat:
        return self.state(traces=self.systems_respecting).output()

    def output_respecting(self) -> mat:
        return self.state(traces=self.systems_violating).output()

    def state_violating(self) -> QuantumState:
        return self.state(traces=self.systems_respecting)

    def state_respecting(self) -> QuantumState:
        return self.state(traces=self.systems_violating)


def dctc_violating(
    input_respecting: mat | QuantumState,
    gate: mat | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
    free_symbol: sym | str | None = None,
) -> mat:
    """Calculate the chronology-violating (CV) state(s) according to the D-CTC prescription by
    computing fixed points of the map

    .. math::

        \\MapDCTCsCV_{\\Unitary}[\\StateCR,\\StateCV]
            = \\trace_\\CR\\bigl[\\Unitary(\\StateCR \\otimes \\StateCV)\\Unitary^\\dagger\\bigr]

    given the chronology-respecting (CR) input state ``input_respecting`` (:math:`\\StateCR`)
    and (unitary) interaction described by ``gate`` (:math:`\\Unitary`).

    Arguments
    ---------
    input_respecting : mat | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    gate : mat | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the
        CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.
    free_symbol : sym | str
        The representation of the algebraic symbol to be used as the free parameter in the case
        where the CV map has a multiplicity of fixed points.
        Defaults to ``"g"``.

    Returns
    -------
    mat
        The fixed-point solution(s) of the D-CTC CV map.

    Note
    ----
    Please note that this function in its current form is considered to be *highly* experimental.

    """
    free_symbol = "g" if free_symbol is None else free_symbol
    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)), systems=systems_respecting
        )

    conditions_respecting = extract_conditions(input_respecting)
    trace_respecting = input_respecting.trace()
    input_respecting = densify(extract_matrix(input_respecting))

    # Use ``Symbol`` for persistent (structurally bound) variables.
    # Use ``Dummy`` for non-persistent (not structurally bound) variables.
    # The latter should be used so as to not interfere with any user-predefined variables.
    input_violating = sp.Matrix(
        [
            [sp.Dummy(f"τ_{i}{j}") for j in range(0, dim ** len(systems_violating))]
            for i in range(0, dim ** len(systems_violating))
        ]
    )

    input_total = assemble_composition(
        (input_respecting, systems_respecting), (input_violating, systems_violating)
    )

    gate = densify(extract_matrix(gate))
    output_total = gate * input_total * Dagger(gate)
    output_violating = partial_trace(
        matrix=output_total, targets=systems_respecting, dim=dim
    )
    output_violating = recursively_simplify(output_violating, conditions_respecting)

    equations = []
    unknowns_violating = [*input_violating]
    unknowns = list(unknowns_violating)

    for n in range(0, (dim ** len(systems_violating)) ** 2):
        equations.append(sp.Eq(output_violating[n], input_violating[n], evaluate=False))

    if trace_respecting == 1:
        equations += [sp.Eq(trace(input_respecting), 1, evaluate=False)]
        equations += [sp.Eq(trace(input_violating), 1, evaluate=False)]

    # Designed to loop twice: once without the trace equation, then once with it
    counter = 0
    while True:
        solutions = sp.solve(equations, unknowns, set=True)
        if solutions[1] == set() or solutions[1] == {tuple(0 for _ in unknowns)}:
            solutions = sp.nonlinsolve(equations, unknowns)
            if isinstance(solutions, sp.sets.sets.EmptySet) is True or solutions == {
                tuple(0 for _ in unknowns)
            }:
                solutions = set()
            solutions = (unknowns, solutions)
        if len(solutions[1]) == 1:
            break
        elif len(solutions[1]) == 0:
            # Remove final equation (possibly trace condition) and try again
            del equations[-1]
        else:
            raise NotImplementedError(
                "Support for multiple non-parametrized D-CTC CV solutions has not yet been \
                implemented."
            )
        counter += 1
        if counter == 2:
            raise NotImplementedError(
                "The D-CTC CV algorithm was unable to determine a solution (fixed point) \
                to the CV map. If you are certain that your circuit does indeed have a solution, \
                you are welcome to file a bug report."
            )

    solutions = list(solutions[1])[0]
    solutions = {key: value for key, value in zip(unknowns, solutions)}

    # Check for all zeroes solution and replace with CR input state if so
    # This assumes that a zero solution corresponds to the CR input
    if any(value != 0 for value in solutions.values()) is False:
        pairs = {
            key: value
            for key, value in zip(list(input_violating), list(input_respecting))
        }
        for key, value in solutions.items():
            solutions[key] = pairs[key]
        solutions = list(solutions.values())
    else:
        # Invert solution about τ_00 in the case of a single free parameter
        # so that the final result is consistent with the analytical approach
        if len(solutions[input_violating[0]].free_symbols) == 1:
            inverting_symbol = list(solutions[input_violating[0]].free_symbols)[0]
            if inverting_symbol in solutions.keys():
                inverting_equation = [
                    sp.Eq(
                        input_violating[0],
                        solutions[input_violating[0]],
                        evaluate=False,
                    )
                ]
                inverting_solution = sp.nonlinsolve(
                    inverting_equation, [inverting_symbol]
                )
                inverting_solution = list(inverting_solution)[0]
                inverting_solution = {
                    key: value
                    for key, value in zip([inverting_symbol], inverting_solution)
                }
                for key, value in solutions.items():
                    solutions[key] = sp.simplify(
                        value.subs(
                            inverting_symbol, inverting_solution[inverting_symbol]
                        )
                    )

        unknowns = unknowns_violating
        solutions = [
            sp.simplify(solutions[unknown]) if unknown in solutions.keys() else unknown
            for unknown in unknowns
        ]
        free_symbols = list(
            set().union(*[element.free_symbols for element in solutions])
        )
        unknowns_free = [symbol for symbol in free_symbols if symbol in unknowns]
        free_variables = []
        if len(unknowns_free) == 1:
            free_variables = [sp.Symbol(f"{free_symbol}")]
        if len(unknowns_free) > 1:
            free_variables = [
                sp.Symbol(f"{free_symbol}_{i}") for i in range(0, len(unknowns_free))
            ]
        if len(free_variables) != 0:
            solutions = [
                solution.subs(dict(zip(unknowns_free, free_variables)))
                for solution in solutions
            ]

    output_violating = sp.Matrix(
        np.array(solutions).reshape(
            dim ** len(systems_violating), dim ** len(systems_violating)
        )
    )

    return output_violating


def dctc_respecting(
    input_respecting: mat | QuantumState,
    input_violating: mat | QuantumState,
    gate: mat | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
) -> mat:
    """Calculate the chronology-respecting (CR) state(s) according to the D-CTC prescription's
    CR map

    .. math::

       \\MapDCTCsCR_{\\Unitary}[\\StateCR,\\StateCV]
           = \\trace_\\CV\\bigl[\\Unitary(\\StateCR \\otimes \\StateCV)\\Unitary^\\dagger\\bigr]

    given the chronology-respecting (CR) input state ``input_respecting`` (:math:`\\StateCR`),
    chronology-violating (CV) solution state ``input_violating`` (:math:`\\StateCV`),
    and (unitary) interaction described by ``gate`` (:math:`\\Unitary`).

    Arguments
    ---------
    input_respecting : mat | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    input_violating : mat | QuantumState
        The matrix representation of the chronology-violating (CR) solution state.
    gate : mat | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the
        CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.

    Returns
    -------
    mat
        The solution(s) of the D-CTC CR map.

    """
    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)), systems=systems_respecting
        )

    input_respecting = densify(extract_matrix(input_respecting))
    input_violating = densify(extract_matrix(input_violating))
    input_total = assemble_composition(
        (input_respecting, systems_respecting), (input_violating, systems_violating)
    )

    gate = densify(extract_matrix(gate))
    output_total = gate * input_total * Dagger(gate)
    output_respecting = partial_trace(
        matrix=output_total, targets=systems_violating, dim=dim
    )

    return output_respecting


class DCTC(QuantumCTC):
    """A subclass for creating closed timelike curves described by Deutsch's prescription (D-CTCs)
    of quantum time travel.

    This is built upon the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class,
    and so inherits all of its attributes, properties, and methods.

    Arguments
    ---------
    *args
        Variable-length argument list, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    free_symbol : sym | str
        The representation of the algebraic symbol to be used as the free parameter in the case
        where the CV map has a multiplicity of fixed points.
        Defaults to ``"g"``.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor ``__init__`` of the
        superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(self, *args, free_symbol: sym | str | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        free_symbol = "g" if free_symbol is None else free_symbol
        self.free_symbol = free_symbol

    @property
    def free_symbol(self) -> sym | str:
        """The representation of the algebraic symbol to be used as the free parameter in the case
        where the CV map has a multiplicity of fixed points."""
        return self._free_symbol

    @free_symbol.setter
    def free_symbol(self, free_symbol: sym | str):
        self._free_symbol = free_symbol

    @property
    def input_is_vector(self) -> bool:
        return False
        # D-CTC prescription requires density matrix inputs.

    @property
    def output_is_vector(self) -> bool:
        return False
        # The CR and CV maps of a D-CTC are non-linear, non-unitary (mixing) operations in general.

    @property
    def matrix(self) -> mat:
        """The matrix representation of the total D-CTC chronology-respecting (CR) output state
        prior to any post-processing."""
        output_respecting = dctc_respecting(
            input_respecting=self.input(conditions=[]),
            input_violating=self.state_violating(free_symbol=self.free_symbol),
            gate=self.gate(conditions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )
        return output_respecting

    def output_violating(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        free_symbol: sym | str | None = None,
    ) -> mat:
        """Compute the matrix representation of the D-CTC chronology-violating (CV) state(s).

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
            Defaults to ``False``.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter
            in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of ``self.free_symbol``.

        Returns
        -------
        mat
            The matrix representation of the CV output state.

        """
        free_symbol = self.free_symbol if free_symbol is None else free_symbol

        output_violating = dctc_violating(
            input_respecting=self.input(conditions=[]),
            gate=self.gate(conditions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
            free_symbol=free_symbol,
        )

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        output_violating = QuantumState(
            spec=output_violating,
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            output_violating.simplify()

        # Conjugation
        conjugate = False if conjugate is None else conjugate
        if conjugate is True:
            output_violating.dagger()

        output_violating = QuantumState(
            spec=output_violating.output(),
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        return sp.Matrix(output_violating.output())

    def output_respecting(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        postprocess: bool | None = None,
        free_symbol: sym | str | None = None,
    ) -> mat:
        """Compute the matrix representation of the D-CTC chronology-respecting (CR) state(s)
        (including any post-processing).

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
            Defaults to ``False``.
        postprocess : bool
            Whether to post-process the state
            (i.e., perform the circuit's traces and postselections).
            Defaults to ``True``.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter
            in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of ``self.free_symbol``.

        Returns
        -------
        mat
            The matrix representation of the (post-processed) CR output state.

        """
        conditions = self.conditions if conditions is None else conditions
        free_symbol = self.free_symbol if free_symbol is None else free_symbol

        output_respecting = dctc_respecting(
            input_respecting=self.input(conditions=[]),
            input_violating=self.state_violating(free_symbol=free_symbol),
            gate=self.gate(conditions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        output_respecting = QuantumState(
            spec=output_respecting,
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        postprocess = True if postprocess is None else postprocess
        if postprocess is True:
            systems_removed = []

            # Partial traces
            traces = adjust_targets(self.systems_traces, systems_removed)
            output_respecting.partial_trace(targets=traces)
            systems_removed += traces

            # Postselections
            for postselection in self.postselections:
                length = count_systems(extract_matrix(postselection[0]), self.dim)
                listed = flatten_list([postselection[1]])
                systems = [(min(listed) + n) for n in range(0, length)]
                targets_postselection = adjust_targets(systems, systems_removed)
                output_respecting.postselect(
                    postselections=[(postselection[0], targets_postselection)]
                )
                systems_removed += systems

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            output_respecting.simplify()

        # Conjugation
        conjugate = False if conjugate is None else conjugate
        if conjugate is True:
            output_respecting.dagger()

        output_respecting = QuantumState(
            spec=output_respecting.output(),
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        return sp.Matrix(output_respecting.output())

    def output(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        postprocess: bool | None = None,
        free_symbol: sym | str | None = None,
    ) -> mat:
        """An alias for the :py:meth:`~qhronology.quantum.prescriptions.DCTC.output_respecting` method.

        Useful for polymorphism.

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
            Defaults to ``False``.
        postprocess : bool
            Whether to post-process the state
            (i.e., perform the circuit's traces and postselections).
            Defaults to ``True``.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter
            in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of ``self.free_symbol``.

        Returns
        -------
        mat
            The matrix representation of the (post-processed) CR output state.
        """
        return self.output_respecting(
            conditions=conditions,
            simplify=simplify,
            conjugate=conjugate,
            postprocess=postprocess,
            free_symbol=free_symbol,
        )

    def state_violating(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        norm: bool | num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        debug: bool | None = None,
        free_symbol: sym | str | None = None,
    ) -> QuantumState:
        """Compute the D-CTC chronology-violating (CV) state(s) as a
        :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the state.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the state before committing it to the
            ``matrix`` property.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the state.
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
        traces : list[int]
            A list of indices of the CV systems (relative to the entire circuit) on which to
            perform partial traces.
            Defaults to ``[]``.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter
            in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of ``self.free_symbol``.
        debug : bool
            Whether to print the internal state (held in ``matrix``) on change.
            Defaults to ``False``.

        Returns
        -------
        QuantumState
            The CV output state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        """
        conditions = self.conditions if conditions is None else conditions
        traces = [] if traces is None else traces

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        state = QuantumState(
            form=form,
            kind=kind,
            spec=sp.Matrix(
                self.output_violating(
                    conditions=conditions,
                    simplify=simplify,
                    conjugate=False,
                    free_symbol=free_symbol,
                )
            ),
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            conjugate=conjugate,
            norm=norm,
            label=label,
            notation=notation,
            debug=debug,
        )
        traces = adjust_targets(traces, self.systems_removed + self.systems_respecting)
        state.partial_trace(targets=traces)
        return state

    def state_respecting(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        norm: bool | num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        postprocess: bool | None = None,
        debug: bool | None = None,
        free_symbol: sym | str | None = None,
    ) -> QuantumState:
        """Compute the D-CTC chronology-respecting (CR) state(s) as a
        :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the state.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the state before committing it to the
            ``matrix`` property.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the state.
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
        traces : list[int]
            A list of indices of the CR systems (relative to the entire circuit) on which to
            perform partial traces.
            Performed regardless of the value of ``postprocess``.
            Defaults to ``[]``.
        postprocess : bool
            Whether to post-process the state
            (i.e., perform the circuit's traces and postselections).
            Defaults to ``True``.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter
            in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of ``self.free_symbol``.
        debug : bool
            Whether to print the internal state (held in ``matrix``) on change.
            Defaults to ``False``.

        Returns
        -------
        QuantumState
            The (post-processed) CR output state as a
            :py:class:`~qhronology.quantum.states.QuantumState` instance.

        """
        conditions = self.conditions if conditions is None else conditions
        traces = [] if traces is None else traces
        postprocess = True if postprocess is None else postprocess

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        if postprocess is True:
            traces = adjust_targets(
                traces, self.systems_removed + self.systems_violating
            )
        else:
            traces = adjust_targets(traces, self.systems_violating)

        matrix = sp.Matrix(
            self.output_respecting(
                conditions=conditions,
                simplify=simplify,
                conjugate=False,
                postprocess=postprocess,
                free_symbol=free_symbol,
            )
        )

        state = QuantumState(
            form=form,
            kind=kind,
            spec=matrix,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            conjugate=conjugate,
            norm=norm,
            label=label,
            notation=notation,
            debug=debug,
        )
        state.partial_trace(targets=traces)
        return state


def pctc_violating(
    input_respecting: mat | QuantumState,
    gate: mat | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
) -> mat:
    """Calculate the chronology-violating (CV) state according to the P-CTC weak-measurement
    tomography expression for the prescription's CV map

    .. math::

       \\MapPCTCsCV_{\\Unitary}[\\StateCR]
           = \\trace_\\CR\\bigl[\\Unitary(\\StateCR \\otimes \\tfrac{1}{\\Dimension}\\Identity)
           \\Unitary^\\dagger\\bigr]

    given the chronology-respecting (CR) input state ``input_respecting`` (:math:`\\StateCR`)
    and (unitary) interaction described by ``gate`` (:math:`\\Unitary`).
    Here, :math:`\\Dimension` is the dimensionality of the CV system's Hilbert space
    (assumed to be equivalent to that of its CR counterpart), while :math:`\\Identity` is the
    :math:`\\Dimension \\times \\Dimension` identity matrix.

    Arguments
    ---------
    input_respecting : mat | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    gate : mat | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the
        CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.

    Returns
    -------
    mat
        The weak-measurement tomography expression for the P-CTC's CV state.

    Note
    ----
    The validity of the expression used in this function to compute the P-CTC CV state for
    *non-qubit* systems has not been proven.

    """
    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)), systems=systems_respecting
        )

    input_respecting = densify(extract_matrix(input_respecting))
    identity = (sp.Rational(1, dim) ** len(systems_violating)) * sp.eye(
        dim ** len(systems_violating)
    )

    input_total = assemble_composition(
        (input_respecting, systems_respecting), (identity, systems_violating)
    )

    gate = densify(extract_matrix(gate))
    output_total = gate * input_total * Dagger(gate)
    output_violating = partial_trace(
        matrix=output_total, targets=systems_respecting, dim=dim
    )

    return output_violating


def pctc_respecting(
    input_respecting: mat | QuantumState,
    gate: mat | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
) -> mat:
    """Calculate the (non-renormalized) chronology-respecting (CR) state according to the P-CTC prescription's non-renormalizing CR map

    .. math::

       \\MapPCTCsCR_{\\Unitary}[\\StateCR]
           \\propto \\OperatorPCTC \\StateCR \\OperatorPCTC^\\dagger

    given the chronology-respecting (CR) input state ``input_respecting`` (:math:`\\StateCR`)
    and (unitary) interaction described by ``gate`` (:math:`\\Unitary`).
    Here,

    .. math:: \\OperatorPCTC \\equiv \\trace_\\CV[\\Unitary]

    is the P-CTC operator.

    Note
    ----
    This function does not renormalize the output state as per the renormalized P-CTC map

    .. math::

       \\MapPCTCsCR_{\\Unitary}[\\StateCR]
           = \\frac{\\OperatorPCTC \\StateCR \\OperatorPCTC^\\dagger}
           {\\trace\\bigl[ \\OperatorPCTC \\StateCR \\OperatorPCTC^\\dagger\\bigr]}

    Arguments
    ---------
    input_respecting : mat | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    gate : mat | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the
        CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.

    Returns
    -------
    mat
        The solution of the P-CTC CR map.

    """
    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)), systems=systems_respecting
        )

    input_respecting = extract_matrix(input_respecting)
    gate = densify(extract_matrix(gate))

    gate_reduced = partial_trace(matrix=gate, targets=systems_violating, dim=dim)
    if matrix_form(input_respecting) == Forms.VECTOR.value:
        input_respecting = columnify(input_respecting)
        output_respecting = gate_reduced * input_respecting
        # renormalization = recursively_simplify(sp.sqrt(1/trace(output_respecting)))
        # output_respecting = renormalization*output_respecting
    else:
        output_respecting = gate_reduced * input_respecting * Dagger(gate_reduced)
        # renormalization = recursively_simplify(1/trace(output_respecting))
        # output_respecting = renormalization*output_respecting

    return output_respecting


class PCTC(QuantumCTC):
    """A subclass for creating closed timelike curves described by the postselected
    teleportation prescription (P-CTCs) of quantum time travel.

    This is built upon the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class,
    and so inherits all of its attributes, properties, and methods.

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
        super().__init__(*args, **kwargs)

    @property
    def matrix(self) -> mat:
        """The matrix representation of the total P-CTC CR output state prior to any
        post-processing."""
        output_respecting = pctc_respecting(
            input_respecting=self.input(conditions=[]),
            gate=self.gate(conditions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )
        return output_respecting

    def output_violating(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
    ) -> mat:
        """Compute the matrix representation of the P-CTC chronology-violating (CV) state.

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
            Defaults to ``False``.

        Returns
        -------
        mat
            The matrix representation of the CV output state.

        Note
        ----
        The validity of the expression used in this method to compute the P-CTC CV state for
        *non-qubit* systems has not been proven.
        """
        output_violating = pctc_violating(
            input_respecting=self.input(conditions=[]),
            gate=self.gate(conditions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        output_violating = QuantumState(
            spec=output_violating,
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            output_violating.simplify()

        # Conjugation
        conjugate = False if conjugate is None else conjugate
        if conjugate is True:
            output_violating.dagger()

        output_violating = QuantumState(
            spec=output_violating.output(),
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        return sp.Matrix(output_violating.output())

    def output_respecting(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        postprocess: bool | None = None,
    ) -> mat:
        """Compute the matrix representation of the P-CTC chronology-respecting (CR) state
        (including any post-processing).

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
            Defaults to ``False``.
        postprocess : bool
            Whether to post-process the state
            (i.e., perform the circuit's traces and postselections).
            Defaults to ``True``.

        Returns
        -------
        mat
            The matrix representation of the (post-processed) CR output state.

        Note
        ----
        The output state is not renormalized.
        """
        conditions = self.conditions if conditions is None else conditions

        output_respecting = pctc_respecting(
            input_respecting=self.input(conditions=[]),
            gate=self.gate(conditions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        if self.input_is_vector is True:
            form = Forms.VECTOR.value
            kind = Kinds.PURE.value
        if self.gate_is_linear is False:
            form = Forms.MATRIX.value
            kind = Kinds.MIXED.value
        output_respecting = QuantumState(
            spec=output_respecting,
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        postprocess = True if postprocess is None else postprocess
        if postprocess is True:
            systems_removed = []

            # Partial traces
            traces = adjust_targets(self.systems_traces, systems_removed)
            output_respecting.partial_trace(targets=traces)
            systems_removed += traces

            # Postselections
            for postselection in self.postselections:
                length = count_systems(extract_matrix(postselection[0]), self.dim)
                listed = flatten_list([postselection[1]])
                systems = [(min(listed) + n) for n in range(0, length)]
                targets_postselection = adjust_targets(systems, systems_removed)
                output_respecting.postselect(
                    postselections=[(postselection[0], targets_postselection)]
                )
                systems_removed += systems

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            output_respecting.simplify()

        # Conjugation
        conjugate = False if conjugate is None else conjugate
        if conjugate is True:
            output_respecting.dagger()

        output_respecting = QuantumState(
            spec=output_respecting.output(),
            form=form,
            kind=kind,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            norm=False,
            conjugate=False,
            label=None,
            notation=None,
            debug=False,
        )

        return sp.Matrix(output_respecting.output())

    def output(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        postprocess: bool | None = None,
    ) -> mat:
        """An alias for the :py:meth:`~qhronology.quantum.prescriptions.PCTC.output_respecting` method.

        Useful for polymorphism.

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
            Defaults to ``False``.
        postprocess : bool
            Whether to post-process the state
            (i.e., perform the circuit's traces and postselections).
            Defaults to ``True``.

        Returns
        -------
        mat
            The matrix representation of the (post-processed) CR output state.

        Note
        ----
        The output state is not renormalized.
        """
        return self.output_respecting(
            conditions=conditions,
            simplify=simplify,
            conjugate=conjugate,
            postprocess=postprocess,
        )

    def state_violating(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        norm: bool | num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        debug: bool | None = None,
    ) -> QuantumState:
        """Compute the P-CTC chronology-violating (CV) state as a
        :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the state.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the state before committing it in the
            ``matrix`` property.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the state.
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
        traces : list[int]
            A list of indices of the CV systems (relative to the entire circuit) on which to
            perform partial traces.
            Defaults to ``[]``.
        debug : bool
            Whether to print the internal state (held in ``matrix``) on change.
            Defaults to ``False``.

        Returns
        -------
        QuantumState
            The CV output state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Note
        ----
        The validity of the expression used in this method to compute the P-CTC CV state for
        *non-qubit* systems has not been proven.
        """
        traces = [] if traces is None else traces

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        state = QuantumState(
            form=form,
            kind=kind,
            spec=sp.Matrix(
                self.output_violating(
                    conditions=conditions, simplify=simplify, conjugate=False
                )
            ),
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            conjugate=conjugate,
            norm=norm,
            label=label,
            notation=notation,
            debug=debug,
        )
        traces = adjust_targets(traces, self.systems_removed + self.systems_respecting)
        state.partial_trace(targets=traces)
        return state

    def state_respecting(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        norm: bool | num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        postprocess: bool | None = None,
        debug: bool | None = None,
    ) -> QuantumState:
        """Compute the P-CTC chronology-respecting (CR) state as a
        :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the state.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the state before committing it to the
            ``matrix`` property.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the state.
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
        traces : list[int]
            A list of indices of the CR systems (relative to the entire circuit) on which to
            perform partial traces.
            Performed regardless of the value of ``postprocess``.
            Defaults to ``[]``.
        postprocess : bool
            Whether to post-process the state
            (i.e., perform the circuit's traces and postselections).
            Defaults to ``True``.
        debug : bool
            Whether to print the internal state (held in ``matrix``) on change.
            Defaults to ``False``.

        Returns
        -------
        QuantumState
            The (post-processed) CR output state as a
            :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Note
        ----
        The output state is not renormalized if ``norm`` is ``False``.
        """
        conditions = self.conditions if conditions is None else conditions
        traces = [] if traces is None else traces
        postprocess = True if postprocess is None else postprocess

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        if postprocess is True:
            if self.output_is_vector is True and len(traces) == 0:
                form = Forms.VECTOR.value
                kind = Kinds.PURE.value
            traces = adjust_targets(
                traces, self.systems_removed + self.systems_violating
            )
        else:
            if (
                self.input_is_vector is True
                and self.gate_is_linear is True
                and len(traces) == 0
            ):
                form = Forms.VECTOR.value
                kind = Kinds.PURE.value
            traces = adjust_targets(traces, self.systems_violating)

        matrix = sp.Matrix(
            self.output_respecting(
                conditions=conditions,
                simplify=simplify,
                conjugate=False,
                postprocess=postprocess,
            )
        )

        state = QuantumState(
            form=form,
            kind=kind,
            spec=matrix,
            symbols=self.symbols,
            dim=self.dim,
            conditions=conditions,
            conjugate=conjugate,
            norm=norm,
            label=label,
            notation=notation,
            debug=debug,
        )
        state.partial_trace(targets=traces)
        return state
