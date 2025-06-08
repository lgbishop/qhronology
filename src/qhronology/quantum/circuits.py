# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lachlanbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.com.

"""
A class for the creation of quantum circuits.
"""

# https://peps.python.org/pep-0649/
# https://peps.python.org/pep-0749/
from __future__ import annotations

import copy
from typing import Any

import sympy as sp
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.dagger import Dagger

from qhronology.utilities.classification import (
    num,
    sym,
    mat,
    arr,
    Forms,
    Kinds,
    Shapes,
    matrix_form,
    matrix_shape,
)
from qhronology.utilities.diagrams import (
    Families,
    Sections,
    Styles,
    DiagramColumn,
    DiagramCircuit,
)
from qhronology.utilities.helpers import (
    flatten_list,
    check_systems_conflicts,
    adjust_targets,
    symbolize_expression,
    symbolize_tuples,
    extract_matrix,
    recursively_simplify,
    count_systems,
    extract_matrix,
)
from qhronology.utilities.objects import QuantumObject
from qhronology.utilities.symbolics import SymbolicsProperties

from qhronology.quantum.states import QuantumState
from qhronology.quantum.gates import (
    QuantumGate,
    _Single,
)

from qhronology.mechanics.operations import densify


class QuantumCircuit(SymbolicsProperties):
    """A class for creating quantum circuits and storing their metadata.

    Instances provide complete descriptions of quantum circuits, along with various associated
    attributes (such as mathematical conditions, including normalization).
    The circuit's input is recorded as a list of :py:class:`~qhronology.quantum.states.QuantumState`
    objects, with the composition of the elements of this forming the total input.
    Similarly, the circuit's transformation on its input is recorded as a list of
    :py:class:`~qhronology.quantum.gates.QuantumGate` objects, with the product of the (linear)
    elements of this list forming the total transformation (e.g., unitary matrix).

    Arguments
    ---------
    inputs : list[QuantumState]
        An ordered list of :py:class:`~qhronology.quantum.states.QuantumState` instances.
        The total input state is the tensor product of these individual states in the order
        in which they appear in ``inputs``.
        Must all have the same value of the ``dim`` property.
        Defaults to ``[]``.
    gates : list[QuantumGate]
        An ordered list of :py:class:`~qhronology.quantum.gates.QuantumGate` instances.
        The total gate is the product of these individual gates in the order in which they appear
        in ``gates``.
        Must all have the same values of the ``dim`` and ``num_systems`` properties.
        Defaults to ``[]``.
    traces : list[int]
        The numerical indices of the subsystems to be traced over.
        Defaults to ``[]``.
    postselections: list[tuple[mat | arr | QuantumObject, int | list[int]]]
        A list of 2-tuples of vectors or matrix operators paired with the first (smallest) index
        of their postselection target systems.
        Must all have the same value of the ``dim`` property.
        Defaults to ``[]``.
    symbols : dict[sym | str, dict[str, Any]]
        A dictionary in which the keys are individual symbols and the values are dictionaries
        of their respective SymPy keyword-argument ``assumptions``.
        The value of the ``symbols`` property of all states in ``inputs`` and gates in ``gates`` are automatically merged into the instance's corresponding ``symbols`` property.
        Defaults to ``{}``.
    conditions : list[tuple[num | sym | str, num | sym | str]]
        A list of :math:`2`-tuples of conditions to be applied to all objects (such as states and
        gates) computed from the circuit.
        All instances of the expression in each tuple's first element are replaced by the
        expression in the respective second element.
        This uses the same format as the SymPy ``subs()`` method.
        The order in which they are applied is simply their order in the list.
        The value of the ``conditions`` property of all states in ``inputs`` and gates in ``gates``
        are automatically merged into the instance's corresponding ``conditions`` property.
        Defaults to ``[]``.

    Note
    ----
    All states, gates, postselections, and measurement operators recorded in the instance must
    share the same dimensionality (i.e., the value of the ``dim`` property).

    Note
    ----
    The sum of the ``num_systems`` properties of the quantum states in ``inputs`` should match
    that of each of the gates in ``gates``.
    """

    def __init__(
        self,
        inputs: list[QuantumState] | None = None,
        gates: list[QuantumGate] | None = None,
        traces: list[int] | None = None,
        postselections: (
            list[tuple[mat | arr | QuantumObject, int | list[int]]] | None
        ) = None,
        symbols: dict[sym | str, dict[str, Any]] | None = None,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
    ):
        SymbolicsProperties.__init__(self, symbols=symbols, conditions=conditions)
        inputs = [] if inputs is None else inputs
        gates = [] if gates is None else gates
        postselections = [] if postselections is None else postselections
        traces = [] if traces is None else traces

        self.inputs = inputs
        self.gates = gates
        self._postselections = postselections
        self._traces = traces
        self.postselections = postselections
        self.traces = traces

    def __repr__(self) -> str:
        return repr(self.output())

    @property
    def inputs(self) -> list[QuantumState]:
        """An ordered list of :py:class:`~qhronology.quantum.states.QuantumState` instances.

        The total input state is the tensor product of these individual states in the order
        in which they appear in the list.

        Each state's ``symbols`` and ``conditions`` properties are merged into their counterparts
        in the instance upon their addition to the ``gates`` property.
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs: list[QuantumState]):
        inputs = flatten_list([copy.deepcopy(inputs)])
        for state in inputs:
            self.conditions += list(state.conditions)
            self.symbols |= dict(state.symbols)
        self._inputs = inputs

    @property
    def gates(self) -> list[QuantumGate]:
        """An ordered list of :py:class:`~qhronology.quantum.gates.QuantumGate` instances.

        The total gate is the product of these individual gates in the order in which they appear
        in the list.

        Must all have the same ``num_systems`` property.

        Each gate's ``symbols`` and ``conditions`` properties are merged into their counterparts
        in the instance upon their addition to the ``gates`` property.
        """
        return self._gates

    @gates.setter
    def gates(self, gates: list[QuantumGate]):
        gates = flatten_list([copy.deepcopy(gates)])
        for gate in gates:
            self.conditions += list(gate.conditions)
            self.symbols |= dict(gate.symbols)
        self._gates = gates

    @property
    def postselections(self) -> list[tuple[mat | arr | QuantumObject, int | list[int]]]:
        """A list of 2-tuples of vectors or matrix operators paired with the first (smallest)
        index of their postselection target systems.

        Any ``symbols`` and ``conditions`` properties of each postselection are merged into their
        counterparts in the instance upon their addition to the ``postselections`` property.
        """
        return self._postselections

    @postselections.setter
    def postselections(
        self, postselections: list[tuple[mat | arr | QuantumObject, int | list[int]]]
    ):
        if len(postselections) > 0:
            systems_postselections = []
            for postselection in postselections:
                length = count_systems(extract_matrix(postselection[0]), self.dim)
                listed = flatten_list([postselection[1]])
                systems = [(min(listed) + n) for n in range(0, length)]
                if len(listed) > 1:
                    if set(systems) != set(listed):
                        raise ValueError(
                            "Mismatch between the postselection's specified targets and its \
                            calculated size."
                        )
                systems_postselections += systems
            systems_postselections = list(set(systems_postselections))
            for k in systems_postselections:
                if k not in self.systems:
                    raise ValueError(
                        "At least one of the postselection's target systems does not exist."
                    )
            check_systems_conflicts(
                self.systems_traces, systems_postselections, self.systems_postselections
            )
            for operator, targets in postselections:
                if hasattr(operator, "_conditions") is True:
                    self.conditions += list(operator.conditions)
                if hasattr(operator, "_symbols") is True:
                    self.symbols |= dict(operator.symbols)
        self._postselections = postselections

    @property
    def traces(self) -> list[int]:
        """The numerical indices of the subsystems to be traced over."""
        return self._traces

    @traces.setter
    def traces(self, traces: list[int]):
        systems_traces = flatten_list([traces])
        for k in systems_traces:
            if k not in self.systems:
                raise ValueError(
                    "At least one of the partial trace target systems does not exist."
                )
        check_systems_conflicts(
            systems_traces, self.systems_traces, self.systems_postselections
        )
        self._traces = traces

    @property
    def systems_traces(self) -> list[int]:
        """The indices of the systems to be traced over."""
        return self.traces

    @property
    def systems_postselections(self) -> list[int]:
        """The indices of the systems to be postselected."""
        systems_postselections = []
        for postselection in self.postselections:
            length = count_systems(extract_matrix(postselection[0]), self.dim)
            listed = flatten_list([postselection[1]])
            systems = [(min(listed) + n) for n in range(0, length)]
            systems_postselections += systems
        return list(set(systems_postselections))

    @property
    def systems_removed(self) -> list[int]:
        """The indices of all of the systems targeted by the ``traces`` and ``postselections``
        properties."""
        return flatten_list(self.systems_traces + self.systems_postselections)

    @property
    def num_systems_inputs(self) -> int:
        """The total number of systems spanned by the circuit's input states."""
        num_systems_inputs = 0
        for state in self.inputs:
            num_systems_inputs += state.num_systems
        return num_systems_inputs

    @property
    def num_systems_gates(self) -> int:
        """The total number of systems spanned by the circuit's gates."""
        num_systems_gates = []
        for gate in self.gates:
            num_systems_gates.append(gate.num_systems)
        if len(num_systems_gates) > 0:
            if len(set(num_systems_gates)) != 1:
                raise ValueError(
                    "One or more of the gates in the circuit has mismatching ``num_systems``."
                )
        else:
            num_systems_gates = [0]
        return num_systems_gates[0]

    @property
    def num_systems_gross(self) -> int:
        """The total number of systems spanned by the circuit's states and gates prior to any
        system reduction (post-processing, i.e., traces and postselections])."""
        num_systems_gross = max([self.num_systems_inputs] + [self.num_systems_gates])
        return num_systems_gross

    @property
    def num_systems_net(self) -> int:
        """The total number of systems spanned by the circuit's states and gates after any
        system reduction (post-processing, i.e., traces and postselections])."""
        num_systems_net = self.num_systems_gross - len(self.systems_removed)
        return num_systems_net

    @property
    def num_systems(self) -> int:
        """Alias for ``num_systems_gross``."""
        return self.num_systems_gross

    @property
    def num_systems_removed(self) -> int:
        """The total number of systems removed via system reduction (post-processing,
        i.e., traces and postselections])."""
        return len(self.systems_removed)

    @property
    def systems(self) -> list[int]:
        """An ordered list of the numerical indices of the circuit's systems."""
        return [k for k in range(0, self.num_systems)]

    @property
    def dim(self) -> int:
        """The dimensionality of the circuit.
        Calculated from its states and gates, and so all must have the same value."""
        dim = None
        dim_input = None
        if self.inputs != []:
            dims_input = []
            for state in self.inputs:
                dims_input.append(state.dim)
            dim_input = list(set(dims_input))
            if len(dim_input) != 1:
                raise ValueError(
                    "One or more of the input states has mismatching dimensionality."
                )
            dim_input = dim_input[0]
            dim = dim_input
        dim_gate = None
        if self.gates != []:
            dims_gates = []
            for gate in self.gates:
                dims_gates.append(gate.dim)
            dim_gate = list(set(dims_gates))
            if len(dim_gate) != 1:
                raise ValueError(
                    "One or more of the gates has mismatching dimensionality."
                )
            dim_gate = dim_gate[0]
            dim = dim_gate
        if dim_input is not None and dim_gate is not None:
            if dim_input != dim_gate:
                raise ValueError(
                    "One or more of the gates has dimensionality different to that of the \
                    input state(s)."
                )
        return dim

    @property
    def input_is_vector(self) -> bool:
        """Whether all states in ``inputs`` are vector states."""
        is_vector = True
        if any(
            form != Forms.VECTOR.value for form in [state.form for state in self.inputs]
        ):
            is_vector = False
        if self.num_systems - self.num_systems_inputs != 0:
            is_vector = False
        return is_vector

    @property
    def gate_is_linear(self) -> bool:
        """Whether all gates are linear (i.e., not measurement operations)."""
        is_linear = True
        if any(
            family == Families.METER.value
            for family in [gate.family for gate in self.gates]
        ):
            is_linear = False
        return is_linear

    @property
    def post_is_vector(self) -> bool:
        """Whether any traces or non-vector postselections exist in the circuit's post-processing
        (trace and postselection) stage."""
        is_vector = True
        if len(self.systems_traces) != 0:
            is_vector = False
        if len(self.systems_postselections) != 0:
            for postselection in self.postselections:
                if matrix_form(extract_matrix(postselection[0])) != Forms.VECTOR.value:
                    is_vector = False
        return is_vector

    @property
    def output_is_vector(self) -> bool:
        """Whether or not the output from the entire circuit is a vector state."""
        is_vector = True
        if (
            not any(
                not boolean
                for boolean in [
                    self.input_is_vector,
                    self.gate_is_linear,
                    self.post_is_vector,
                ]
            )
            is False
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
        """Construct the composite input state of the quantum circuit as a
        :py:class:`~qhronology.quantum.states.QuantumState` instance and return it.

        This is computed as the tensor product of the individual gates in the order in which
        they appear in the ``inputs`` property.
        Is a vector state only when all of the component states are vectors.

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
        identity = (sp.Rational(1, self.dim)) * sp.eye(self.dim)
        for _ in range(0, self.num_systems_gross - self.num_systems_inputs):
            inputs.append(identity)
        input_state = sp.Matrix(TensorProduct(*inputs))

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

    def gate(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        exponent: num | sym | str | None = None,
        label: str | None = None,
        notation: str | None = None,
    ) -> QuantumGate:
        """Construct the combined gate describing the total sequence of gates in the quantum circuit
        as a :py:class:`~qhronology.quantum.gates.QuantumGate` instance and return it.

        This is computed as the matrix product of the individual gates in the reverse order
        in which they appear in the ``gates`` property.

        Arguments
        ---------
        conditions : list[tuple[num | sym | str, num | sym | str]]
            Algebraic conditions to be applied to the gate.
            Defaults to the value of ``self.conditions``.
        simplify : bool
            Whether to perform algebraic simplification on the gate.
            Defaults to ``False``.
        conjugate : bool
            Whether to perform Hermitian conjugation on the gate when it is called.
            Defaults to ``False``.
        exponent : num | sym | str
            A numerical or string representation of a scalar value to which gate's operator
            (residing on ``targets``) is exponentiated.
            Must be a non-negative integer.
            Defaults to ``1``.
        label : str
            The unformatted string used to represent the gate in mathematical expressions.
            Defaults to ``"U"``.
        notation : str
            The formatted string used to represent the gate in mathematical expressions.
            When not ``None``, overrides the value passed to ``label``.
            Not intended to be set by the user in most cases.
            Defaults to ``None``.

        Returns
        -------
        mat
            The matrix or vector representation of the total gate sequence.

        Note
        ----
        This construction excludes measurement gates as they do not have a corresponding
        matrix representation.

        """
        spec = sp.eye(self.dim**self.num_systems_gross)
        for gate in self.gates:
            gate = copy.deepcopy(gate)
            gate.num_systems = self.num_systems_gross
            spec = gate.output() * spec

        spec = symbolize_expression(spec, self.symbols_list)

        # Conditions
        conditions = self.conditions if conditions is None else conditions
        conditions = symbolize_tuples(conditions, self.symbols_list)
        spec = spec.subs(conditions)

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            spec = recursively_simplify(spec, conditions)

        gate_total = QuantumGate(
            spec=spec,
            targets=self.systems,
            controls=[],
            anticontrols=[],
            num_systems=self.num_systems,
            dim=self.dim,
            symbols=self.symbols,
            conditions=conditions,
            conjugate=conjugate,
            exponent=exponent,
            coefficient=1,
            label=label,
            notation=notation,
        )

        return gate_total

    @property
    def matrix(self) -> mat:
        """The matrix representation of the total output state prior to any post-processing
        (i.e., traces and postselections)."""
        input_state = sp.Matrix(self.input().output())
        if self.gate_is_linear is True:
            gate_total = sp.Matrix(self.gate().output())
            if self.input_is_vector is True:
                output_state = gate_total * input_state
            else:
                output_state = gate_total * input_state * Dagger(gate_total)
        else:  # Gate in nonlinear and nonunitary so destroys any vector purity.
            output_state = densify(input_state)
            for gate in self.gates:
                gate = copy.deepcopy(gate)
                gate.num_systems = self.num_systems_gross
                if hasattr(gate, "_observable") is True:
                    pre_measurement_state = output_state
                    post_measurement_state = sp.zeros(self.dim**self.num_systems_gross)
                    if gate.observable is False:
                        for matrix_measurement_operator in gate.matrices:
                            post_measurement_state += (
                                densify(matrix_measurement_operator)
                                * pre_measurement_state
                                * Dagger(densify(matrix_measurement_operator))
                            )
                    else:
                        for matrix_measurement_operator in gate.matrices:
                            post_measurement_state += sp.trace(
                                densify(matrix_measurement_operator)
                                * pre_measurement_state
                            ) * densify(matrix_measurement_operator)
                    output_state = post_measurement_state
                else:
                    gate_matrix = sp.Matrix(gate.output(conditions=[]))
                    output_state = gate_matrix * output_state * Dagger(gate_matrix)
        return output_state

    def output(
        self,
        conditions: list[tuple[num | sym | str, num | sym | str]] | None = None,
        simplify: bool | None = None,
        conjugate: bool | None = None,
        postprocess: bool | None = None,
    ) -> mat:
        """Compute the matrix representation of the total output state of the circuit
        (including any post-processing, i.e., traces and postselections) and return it.

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
            The matrix representation of the (post-processed) output state.

        """
        conditions = self.conditions if conditions is None else conditions
        output_state = self.matrix
        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        if self.input_is_vector is True:
            form = Forms.VECTOR.value
            kind = Kinds.PURE.value
        if self.gate_is_linear is False:
            form = Forms.MATRIX.value
            kind = Kinds.MIXED.value

        output_state = QuantumState(
            spec=output_state,
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
            output_state.partial_trace(targets=traces)
            systems_removed += traces

            # Postselections
            for postselection in self.postselections:
                length = count_systems(extract_matrix(postselection[0]), self.dim)
                listed = flatten_list([postselection[1]])
                systems = [(min(listed) + n) for n in range(0, length)]
                targets_postselection = adjust_targets(systems, systems_removed)
                output_state.postselect(
                    postselections=[(postselection[0], targets_postselection)]
                )
                systems_removed += systems

            if self.post_is_vector is False:
                form = Forms.MATRIX.value
                kind = Kinds.MIXED.value

        # Simplification
        simplify = False if simplify is None else simplify
        if simplify is True:
            output_state.simplify()

        # Conjugation
        conjugate = False if conjugate is None else conjugate
        if conjugate is True:
            output_state.dagger()

        output_state = QuantumState(
            spec=output_state.output(),
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

        return sp.Matrix(output_state.output())

    def state(
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
        """Compute the total output state of the circuit (including any post-processing,
        i.e., traces and postselections) as a :py:class:`~qhronology.quantum.states.QuantumState`
        instance and return it.

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
            A list of indices of the systems (relative to the entire circuit) on which to perform
            partial traces.
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
            The (post-processed) output state as a
            :py:class:`~qhronology.quantum.states.QuantumState` instance.

        """
        conditions = self.conditions if conditions is None else conditions
        simplify = False if simplify is None else simplify
        traces = [] if traces is None else traces
        postprocess = True if postprocess is None else postprocess

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value
        if self.input_is_vector is True:
            form = Forms.VECTOR.value
            kind = Kinds.PURE.value
        if self.gate_is_linear is False:
            form = Forms.MATRIX.value
            kind = Kinds.MIXED.value
        if postprocess is True:
            traces = list(set(traces) - set(self.systems_removed))
            traces = adjust_targets(traces, self.systems_removed)
            if self.post_is_vector is False:
                form = Forms.MATRIX.value
                kind = Kinds.MIXED.value
        if len(traces) != 0:
            form = Forms.MATRIX.value
            kind = Kinds.MIXED.value

        matrix = sp.Matrix(
            self.output(
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

    def measure(
        self,
        operators: list[mat | arr | QuantumObject],
        targets: int | list[int] | None = None,
        observable: bool | None = None,
        statistics: bool | None = None,
    ) -> QuantumState | list[num | sym]:
        """Perform a quantum measurement on one or more systems (indicated in ``targets``)
        of the circuit's total output state.
        This occurs prior to any post-processing (i.e., traces and postselections).

        This method has two main modes of operation:

        - When ``statistics`` is ``True``, the (reduced) state (:math:`\\op{\\rho}`)
          (residing on the systems indicated in ``targets``) is measured and the set of resulting
          statistics is returned. This takes the form of an ordered list of values
          :math:`\\{p_i\\}_i` associated with each given operator, where:

          - :math:`p_i = \\trace[\\Kraus_i^\\dagger \\Kraus_i \\op{\\rho}]`
            (measurement probabilities) when ``observable`` is ``False``
            (``operators`` is a list of Kraus operators or projectors :math:`\\Kraus_i`)
          - :math:`p_i = \\trace[\\Observable_i \\op{\\rho}]`
            (expectation values) when ``observable`` is ``True``
            (``operators`` is a list of observables :math:`\\Observable_i`)

        - When ``statistics`` is ``False``, the (reduced) state (:math:`\\op{\\rho}`)
          (residing on the systems indicated in ``targets``) is measured and mutated it according
          to its predicted post-measurement form (i.e., the sum of all possible measurement
          outcomes). This yields the transformed states:

          - When ``observable`` is ``False``:

          .. math:: \\op{\\rho}^\\prime = \\sum_i \\Kraus_i \\op{\\rho} \\Kraus_i^\\dagger.

          - When ``observable`` is ``True``:

          .. math::

             \\op{\\rho}^\\prime
                 = \\sum_i \\trace[\\Observable_i \\op{\\rho}] \\Observable_i.

        In the case where ``operators`` contains only a single item (:math:`\\Kraus`),
        and the current state (:math:`\\ket{\\psi}`) is a vector form,
        the transformation of the state is in accordance with the rule

        .. math::

           \\ket{\\psi^\\prime} = \\frac{\\Kraus \\ket{\\psi}}
               {\\sqrt{\\bra{\\psi} \\Kraus^\\dagger \\Kraus \\ket{\\psi}}}

        when ``observable`` is ``False``. In all other mutation cases, the post-measurement state
        is a matrix, even if the pre-measurement state was a vector.

        The items in the list ``operators`` can also be vectors (e.g., :math:`\\ket{\\xi_i}`),
        in which case each is converted into its corresponding operator matrix representation
        (e.g., :math:`\\ket{\\xi_i}\\bra{\\xi_i}`) prior to any measurements.

        Arguments
        ---------
        operators : list[mat | arr | QuantumObject]
            The operator(s) with which to perform the measurement.
            These would typically be a (complete) set of Kraus operators forming a POVM,
            a (complete) set of (orthogonal) projectors forming a PVM,
            or a set of observables constituting a complete basis for the relevant state space.
        targets : int | list[int]
            The numerical indices of the system(s) to be measured.
            They must be consecutive, and their number must match the number of systems spanned
            by all given operators.
            Indexing begins at ``0``.
            All other systems are discarded (traced over) in the course of performing the
            measurement.
        observable : bool
            Whether to treat the items in ``operators`` as observables
            (as opposed to Kraus operators or projectors).
            Defaults to ``False``.
        statistics : bool
            Whether to return a list of probabilities (``True``) or mutate the state into
            a post-measurement probabilistic sum of all outcomes (``False``).
            Defaults to ``False``.

        Returns
        -------
        list[num | sym]
            A list of probabilities corresponding to each operator given in ``operators``.
            Returned only if ``statistics`` is ``True``.
        QuantumState
            A quantum state that takes the form of the post-measurement probabilistic sum
            of all outcomes of measurements corresponding to each operator given in ``operators``.
            Returned only if ``statistics`` is ``False``.

        """

        statistics = False if statistics is None else statistics
        state = self.state(postprocess=False)
        if statistics is True:
            state = state.measure(
                operators=operators,
                targets=targets,
                observable=observable,
                statistics=statistics,
            )
        else:
            state.measure(
                operators=operators,
                targets=targets,
                observable=observable,
                statistics=statistics,
            )
        return state

    def diagram(
        self,
        pad: tuple[int, int] | None = None,
        sep: tuple[int, int] | None = None,
        uniform_spacing: bool | None = None,
        force_separation: bool | None = None,
        style: str | None = None,
        return_string: bool | None = None,
    ) -> None | str:
        """Print or return a diagram of the quantum circuit as a multiline string.

        Arguments
        ---------
        pad : tuple[int, int]
            A two-tuple describing the horizontal and vertical interior paddings between the content
            at the centre of each gate (e.g., label) and its outer edge (e.g., block border).
            Both integers must be non-negative.
            Defaults to ``(0, 0)``.
        sep : tuple[int, int]
            A two-tuple describing the horizontal and vertical exterior separation distances
            between the edges of neighbouring gates.
            Both integers must be non-negative.
            Defaults to ``(1, 1)``.
        uniform_spacing : bool
            Whether to uniformly space the gates horizontally such that the midpoint of each
            is equidistant from those of its neighbours.
            Defaults to ``False``.
        force_separation : bool
            Whether to force the horizontal gate separation to be exactly the value given
            in ``sep`` for all gates in the circuit.
            When not ``False``, the value of ``uniform_spacing`` is ignored.
            Defaults to ``False``.
        style : str
            A string specifying the style for the circuit visualization to take.
            Can be any of ``"ascii"``, ``"unicode"``, or ``"unicode_alt"``.
            Defaults to ``"unicode"``.
        return_string : bool
            Whether to return the assembled diagram as a multiline string.
            Defaults to ``False``.

        Returns
        -------
        None
            Returned only if ``return_string`` is ``False``.
        str
            The rendered circuit diagram. Returned only if ``return_string`` is ``True``.

        Note
        ----
        The quality of the visualization depends greatly on the output's configuration.
        For best results, the terminal should have a monospace font with good Unicode coverage.

        """
        pad = (0, 0) if pad is None else pad
        sep = (1, 1) if sep is None else sep
        if isinstance(sep, tuple) is True:
            sep = {"upper": sep[1], "lower": sep[1], "left": sep[0], "right": sep[0]}
        style = Styles.UNICODE.value if style is None else style

        uniform_spacing = False if uniform_spacing is None else uniform_spacing
        force_separation = False if force_separation is None else force_separation
        return_string = False if return_string is None else return_string

        cells_input = []

        if hasattr(self, "_systems_respecting") is True:
            for system in self.systems:
                if system == min(self.systems_respecting):
                    for state in self.inputs:
                        cells_input.append(
                            [*state.diagram_column(pad=pad, sep=sep, style=style).cells]
                        )
                else:
                    if system in self.systems_violating:
                        cells_input.append(
                            [
                                _Single(family=Families.WORMHOLE.value + "_PAST")
                                .diagram_column(pad=pad, sep=sep, style=style)
                                .cells
                            ]
                        )
        else:
            for state in self.inputs:
                cells_input.append(
                    [*state.diagram_column(pad=pad, sep=sep, style=style).cells]
                )
            if self.num_systems_inputs != 0:
                for _ in range(0, self.num_systems - self.num_systems_inputs):
                    identity = QuantumState(
                        form=Forms.MATRIX.value,
                        kind=Kinds.MIXED.value,
                        spec=sp.eye(self.dim),
                        symbols=dict(),
                        dim=self.dim,
                        conditions=[],
                        norm=1,
                        conjugate=False,
                        label="I",
                        notation=None,
                        debug=False,
                    )
                    cells_input.append(
                        [identity.diagram_column(pad=pad, sep=sep, style=style).cells]
                    )

        column_input = []
        if self.num_systems_inputs != 0:
            column_input = DiagramColumn(
                cells=flatten_list(cells_input),
                pad=(2, 0),
                section=Sections.INPUTS.value,
            )

        columns_gate = []
        for index_column, gate in enumerate(self.gates):
            gate = copy.deepcopy(gate)
            gate.num_systems = self.num_systems_gross
            columns_gate.append(gate.diagram_column(pad=pad, sep=sep, style=style))

        cells_output = []
        for system in self.systems:
            if (
                hasattr(self, "_systems_respecting") is True
                and system in self.systems_violating
            ):
                cells_output.append(
                    [
                        _Single(family=Families.WORMHOLE.value + "_FUTURE")
                        .diagram_column(pad=pad, sep=sep, style=style)
                        .cells
                    ]
                )
            elif system in self.systems_traces:
                cells_output.append(
                    [
                        _Single(family=Families.TRACE.value)
                        .diagram_column(pad=pad, sep=sep, style=style)
                        .cells
                    ]
                )
            elif system in self.systems_postselections:
                for postselection in self.postselections:
                    if system == min(flatten_list([postselection[1]])):
                        if hasattr(postselection[0], "_family") is True:
                            Postselection = postselection[0]
                            Postselection.family = Families.RSTICK.value
                            if (
                                matrix_shape(Postselection.matrix)
                                == Shapes.COLUMN.value
                            ):
                                Postselection.dagger()
                        else:
                            length = count_systems(
                                extract_matrix(postselection[0]), self.dim
                            )
                            Postselection = QuantumState(
                                form=Forms.MATRIX.value,
                                kind=Kinds.MIXED.value,
                                spec=sp.eye(self.dim**length),
                                symbols=dict(),
                                dim=self.dim,
                                conditions=[],
                                norm=1,
                                conjugate=False,
                                label="?",
                                notation=None,
                                family=Families.RSTICK.value,
                                debug=False,
                            )
                        cells_output.append(
                            [
                                Postselection.diagram_column(
                                    pad=pad, sep=sep, style=style
                                ).cells
                            ]
                        )
            else:
                cells_output.append(
                    [
                        _Single(family=Families.TERM.value)
                        .diagram_column(pad=pad, sep=sep, style=style)
                        .cells
                    ]
                )

        column_output = []
        if len(self.inputs) != 0:
            if len(self.gates) != 0 or self.num_systems_removed != 0:
                column_output = DiagramColumn(
                    cells=flatten_list(cells_output),
                    pad=(2, 0),
                    section=Sections.OUTPUTS.value,
                )

        grid = DiagramCircuit(
            columns=flatten_list([column_input, [*columns_gate], column_output])
        )
        if return_string is True:
            return grid.diagram(
                pad=pad,
                sep=sep,
                style=style,
                uniform_spacing=uniform_spacing,
                force_separation=force_separation,
                return_string=True,
            )
        else:
            grid.diagram(
                pad=pad,
                sep=sep,
                style=style,
                uniform_spacing=uniform_spacing,
                force_separation=force_separation,
                return_string=False,
            )
