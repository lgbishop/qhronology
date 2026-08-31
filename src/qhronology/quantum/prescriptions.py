# Project: Qhronology (https://github.com/lgbishop/qhronology)
# Author: lgbishop <lgbishop@protonmail.com>
# Copyright: Lachlan G. Bishop 2025
# License: AGPLv3 (non-commercial use), proprietary (commercial use)
# For more details, see the README in the project repository:
# https://github.com/lgbishop/qhronology,
# or visit the website:
# https://qhronology.org.

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

from qhronology.mechanics.operations import columnify, densify, partial_trace
from qhronology.mechanics.quantities import entropy, trace
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.quantum.gates import QuantumGate
from qhronology.quantum.states import QuantumState
from qhronology.utilities.classification import (
    Forms,
    Kinds,
    arr,
    expr,
    mat,
    matrix_form,
    num,
    sym,
)
from qhronology.utilities.helpers import (
    adjust_targets,
    assemble_composition,
    cast,
    conjugate_transpose,
    count_dims,
    count_systems,
    dtype,
    extract_substitutions,
    extract_matrix,
    flatten_list,
    matrix_multiplication,
    recursively_simplify,
)


class QuantumCTC(QuantumCircuit):
    """A class for creating quantum circuit models of quantum interactions near closed timelike curves and storing their metadata.

    This is built upon the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class, and so inherits all of its attributes, properties, and methods.

    Instances provide complete descriptions of quantum circuits involving antichronological time travel. The class however does not possess any ability to compute the output state (e.g., resolve temporal paradoxes) of the circuit; that functionality is associated with the specific prescriptions of quantum time travel, which are implemented as subclasses.

    Arguments
    ---------
    *args
        Variable length argument list, passed directly to the constructor :python:`__init__`  of the superclass :py:class:`~qhronology.quantum.circuits.QuantumCircuit`.
    circuit : QuantumCircuit
        An instance of the :py:class:`~qhronology.quantum.circuits.QuantumCircuit` class.
        The values of its attributes override any other values specified in :python:`*args` and :python:`**kwargs`.
        Defaults to :python:`None`.
    systems_respecting : int | list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
        Defaults to :python:`[]`.
    systems_violating : int | list[int]
        The numerical indices of the chronology-violating (CV) subsystems.
        Defaults to :python:`[]`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.circuits.QuantumCircuit`.

    Note
    ----
    The :python:`circuit` argument can be used to merge the value of every attribute from a pre-existing :py:class:`~qhronology.quantum.circuits.QuantumCircuit` instance into the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` instance. Any such merges override the values of the attributes associated with the other arguments specified in the constructor. It is therefore best practice to specify the circuit via either of the following two ways:

    - the :python:`circuit` argument

    - :python:`*args` and :python:`**kwargs` like a typical initialization of a :py:class:`~qhronology.quantum.circuits.QuantumCircuit` instance (without using :python:`circuit`)

    Note that this is in addition to specifying either of :python:`systems_respecting` or :python:`systems_violating`.

    Note
    ----
    The lists of indices specified in either of :python:`systems_respecting` or :python:`systems_violating` must be contiguous.
    Additionally, the circuit's inputs (:python:`inputs`) are treated as one contiguous total state, with the indices of its subsystems exactly matching those specified in :python:`systems_respecting`.

    Note
    ----
    It is best practice to specify only one of either :python:`systems_violating` or :python:`systems_violating`, never both.
    The properties associated with both of these constructor arguments automatically ensure that they are always complementary (with respect to the entire system space), and so only one needs to be specified.

    Note
    ----
    The total interaction between the CR and CV systems is expected to be unitary, and so the sequence of gates in :python:`gates` cannot contain any non-unitary gates (e.g., measurement operations).

    Note
    ----
    Post-processing (e.g., traces and postselections) cannot be performed on any chronology-violating (CV) systems (i.e., those corresponding to indices specified in :python:`systems_violating`).
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
        for key, value in kwargs.items():
            setattr(self, key, value)

        if hasattr(self, "_systems_respecting") is False:
            systems_respecting = (
                [] if systems_respecting is None else systems_respecting
            )
            systems_violating = [] if systems_violating is None else systems_violating
            if len(systems_respecting) == 0 and len(systems_violating) == 0:
                raise ValueError(
                    """Either :python:`systems_respecting` or :python:`systems_violating` must be set."""
                )
            if len(systems_respecting) != 0 and len(systems_violating) != 0:
                if set(self.systems) != set(systems_respecting) | set(
                    systems_violating
                ):
                    raise ValueError(
                        """The union of :python:`systems_respecting` and :python:`systems_violating` is inequivalent to the entire system's structure."""
                    )

            self.systems_respecting = systems_respecting

    def __repr__(self) -> str:
        return repr(self.output_respecting())

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        """Compute the unprocessed matrix representation of the circuit's total output state (combined CR and CV systems).

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
            The unprocessed matrix representation of the circuit's total output state.
        """
        return QuantumCircuit(
            inputs=self.inputs,
            gates=self.gates,
            traces=self.traces,
            postselections=self.postselections,
            numerical=self.numerical,
            array=self.array,
            symbols=self.symbols,
            substitutions=self.substitutions,
        ).matrix(numerical=numerical, array=array)

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
        """Whether all states in :python:`inputs` are vector states."""
        is_vector = False
        if all(state.is_vector for state in self.inputs):
            is_vector = True
        return is_vector

    def input(
        self,
        merge: bool | None = None,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        debug: bool | None = None,
    ) -> QuantumState:
        """Construct the composite chronology-respecting (CR) input state of the closed timelike curve as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        This is computed as the tensor product of the individual gates in the order in which they appear in the :python:`inputs` property.

        Is a vector state only when all of the component states are vectors.

        Arguments
        ---------
        merge : bool
            Whether to merge the labels of the individual quantum states into a single product, separated by :python:`"⊗"` operators, prior to any notational processing.
            Only relevant when all states are vectors.
            Defaults to :python:`True`.
        numerical : bool
            Whether to cast the state's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the state's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
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
            Defaults to :python:`False`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`True`, normalizes to a value of :math:`1`.
            If :python:`False`, does not normalize.
            Defaults to :python:`False`.
        label : str
            The unformatted string used to represent the state in mathematical expressions.
            Must have a non-zero length.
            Defaults to :python:`"⊗".join([state.label for state in self.inputs])`.
        notation : str
            The formatted string used to represent the state in mathematical expressions.
            When not :python:`None`, overrides the value passed to :python:`label`.
            Must have a non-zero length.
            Not intended to be set by the user in most cases.
            Defaults to :python:`"⊗".join([state.notation for state in self.inputs])` if :python:`label` is :python:`None` and either :python:`merge` is :python:`False` or the input states are all vectors, else :python:`None`.
        debug : bool
            Whether to print the internal state (held in :python:`matrix`) on change.
            If :python:`False`, does not print.
            Defaults to :python:`False`.

        Returns
        -------
        QuantumState
            The circuit's total input state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Note
        ----
        Passing a value of :python:`False` to the :python:`merge` argument results in a state whose :python:`notation` is fixed and incompatible with any subsequent changes (including densification).
        This behaviour may be improved in the future.
        """
        return super().input(
            merge=merge,
            numerical=numerical,
            array=array,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            norm=norm,
            label=label,
            notation=notation,
            debug=debug,
        )

    # The four methods below merely output the reduced states, so the :python:`systems_respective` and :python:`systems_violating` of the base class acts just like extra traces.
    def output_violating(self) -> mat | arr:
        return (
            QuantumCircuit(
                inputs=self.inputs,
                gates=self.gates,
                traces=self.traces,
                postselections=self.postselections,
                numerical=self.numerical,
                array=self.array,
                symbols=self.symbols,
                substitutions=self.substitutions,
                simplification=self.simplification,
            )
            .state(traces=self.systems_respecting)
            .output()
        )

    def output_respecting(self) -> mat | arr:
        return (
            QuantumCircuit(
                inputs=self.inputs,
                gates=self.gates,
                traces=self.traces,
                postselections=self.postselections,
                numerical=self.numerical,
                array=self.array,
                symbols=self.symbols,
                substitutions=self.substitutions,
                simplification=self.simplification,
            )
            .state(traces=self.systems_violating)
            .output()
        )

    def state_violating(self) -> QuantumState:
        return QuantumCircuit(
            inputs=self.inputs,
            gates=self.gates,
            traces=self.traces,
            postselections=self.postselections,
            numerical=self.numerical,
            array=self.array,
            symbols=self.symbols,
            substitutions=self.substitutions,
            simplification=self.simplification,
        ).state(traces=self.systems_respecting)

    def state_respecting(self) -> QuantumState:
        return QuantumCircuit(
            inputs=self.inputs,
            gates=self.gates,
            traces=self.traces,
            postselections=self.postselections,
            numerical=self.numerical,
            array=self.array,
            symbols=self.symbols,
            substitutions=self.substitutions,
            simplification=self.simplification,
        ).state(traces=self.systems_violating)


def dctc_violating(
    input_respecting: mat | arr | QuantumState,
    gate: mat | arr | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
    free_symbol: sym | str | None = None,
    maximum_entropy: bool | None = None,
) -> mat | arr:
    """Calculate the chronology-violating (CV) state according to the D-CTC prescription by computing fixed points of the map

    .. math::

        \\MapDCTCsCV_{\\Unitary}[\\StateCR,\\StateCV]
            = \\trace_\\CR\\bigl[\\Unitary(\\StateCR \\otimes \\StateCV)\\Unitary^\\dagger\\bigr]

    given the chronology-respecting (CR) input state :python:`input_respecting` (:math:`\\StateCR`) and (unitary) interaction described by :python:`gate` (:math:`\\Unitary`).

    Arguments
    ---------
    input_respecting : mat | arr | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    gate : mat | arr | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.
    free_symbol : sym | str
        The representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points.
        Defaults to :python:`"g"`.
    maximum_entropy : bool
        Whether to, in the case of solution multiplicity, return the CV state that possesses the most (von Neumann) entropy, in accordance with Deutsch's original prescription.
        If :python:`False`, simply returns the ordinary (single or parametrized) solution.
        Defaults to :python:`False`.

    Returns
    -------
    mat | arr
        The fixed-point solution(s) of the D-CTC CV map.

    Note
    ----
    Please note that this function in its current form is considered to be *highly* experimental.
    """
    free_symbol = "g" if free_symbol is None else free_symbol
    maximum_entropy = False if maximum_entropy is None else maximum_entropy

    if isinstance(input_respecting, mat | arr) is True:
        matrix_num = True if issubclass(dtype(input_respecting), num) is True else False
        matrix_arr = True if isinstance(input_respecting, arr) is True else False
    else:
        try:
            matrix_num = (
                True
                if issubclass(dtype(input_respecting.output()), num) is True
                else False
            )
            matrix_arr = (
                True if isinstance(input_respecting.output(), arr) is True else False
            )
        except:
            raise TypeError(
                """A matrix or array cannot be extracted from the given input state."""
            )

    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)),
            num_systems=len(systems_respecting),
        )

    substitutions_respecting = extract_substitutions(input_respecting)
    input_respecting = densify(extract_matrix(input_respecting))
    trace_respecting = input_respecting.trace()
    gate = densify(extract_matrix(gate))

    # Use :python:`Symbol` for persistent (structurally bound) variables.
    # Use :python:`Dummy` for non-persistent (not structurally bound) variables.
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

    output_total = matrix_multiplication(gate, input_total, conjugate_transpose(gate))
    output_violating = partial_trace(
        matrix=output_total, targets=systems_respecting, dim=dim
    )
    output_violating = recursively_simplify(output_violating, substitutions_respecting)

    equations = []
    unknowns_violating = [*input_violating]
    unknowns = list(unknowns_violating)

    for n in range(0, (dim ** len(systems_violating)) ** 2):
        equations.append(sp.Eq(output_violating[n], input_violating[n], evaluate=False))

    equations += [sp.Eq(trace(input_respecting), trace_respecting, evaluate=False)]
    equations += [sp.Eq(trace(input_violating), trace_respecting, evaluate=False)]

    # Designed to loop twice: once without the trace equation, then once with it.
    counter = 0
    while True:
        solutions = sp.solve(equations, unknowns, set=True)
        if solutions[1] == set() or solutions[1] == {tuple(0 for _ in unknowns)}:
            solutions = sp.nonlinsolve(equations, unknowns)
            if isinstance(solutions, sp.sets.sets.EmptySet) is True or solutions == {
                tuple(0 for _ in unknowns) or tuple(0.0 for _ in unknowns)
            }:
                solutions = set()
            solutions = (unknowns, solutions)
        if len(solutions[1]) == 1:
            values = list(solutions[1])[0]
            if not (len(set(values)) == 1 and values[0] in [0, 0.0]):
                break
        elif len(solutions[1]) == 0:
            # Remove final equation (initially a trace condition) and try again.
            del equations[-1]
        else:
            raise NotImplementedError(
                """Support for multiple non-parametrized D-CTC CV solutions has not yet been implemented."""
            )
        counter += 1
        if counter == 4:
            raise NotImplementedError(
                """The D-CTC CV algorithm was unable to determine a solution (fixed point) to the CV map.
                If you are certain that your circuit does indeed have a solution, you are welcome to file a bug report."""
            )

    solutions = list(solutions[1])[0]
    solutions = {key: value for key, value in zip(unknowns, solutions)}

    free_variables = []
    # Check for all zeroes solution and, if found, replace it with the CR input state.
    # This assumes that a zero solution corresponds to the CR input.
    if any(value != 0 for value in solutions.values()) is False:
        pairs = {
            key: value
            for key, value in zip(list(input_violating), list(input_respecting))
        }
        for key, value in solutions.items():
            solutions[key] = pairs[key]
        solutions = list(solutions.values())
    else:
        # Invert solution about τ_00 in the case of a single free parameter so that the final result is consistent with the analytical approach.
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
        if len(unknowns_free) == 1:
            free_variables = [sp.Symbol(f"{free_symbol}")]
        if len(unknowns_free) > 1:
            free_variables = [
                sp.Symbol(f"{free_symbol}_{i}") for i in range(0, len(unknowns_free))
            ]
        if len(free_variables) > 0:
            solutions = [
                solution.subs(dict(zip(unknowns_free, free_variables)))
                for solution in solutions
            ]

    output_violating = sp.Matrix(
        np.array(solutions).reshape(
            dim ** len(systems_violating), dim ** len(systems_violating)
        )
    )

    if maximum_entropy is True and len(free_variables) > 0:
        S = entropy(output_violating, base=dim)
        dS = [sp.diff(S, variable) for variable in free_variables]
        ddS = [sp.diff(first, variable) for first in dS for variable in free_variables]
        hessian_matrix = sp.Matrix(len(free_variables), len(free_variables), ddS)
        stationary_points = sp.solve(dS, free_variables, set=False)
        maxima = []
        for point in stationary_points:
            substitutions = [
                (free_variables[n], point[n]) for n in range(0, len(point))
            ]
            hessian_matrix_point = hessian_matrix.subs(substitutions)
            eigenvalues = list(hessian_matrix_point.eigenvals().keys())
            if all(
                eigenvalue < 0 for eigenvalue in eigenvalues
            ):  # Check for a local maximum.
                maxima.append(point)
        if len(maxima) == 0:
            print("No maximally entropic D-CTC CV state found.")
        if len(maxima) > 1:
            print("More than one maximally entropic D-CTC CV state found.")
        if len(maxima) == 1:
            output_violating = output_violating.subs(
                [
                    (free_variables[n], maxima[0][n])
                    for n in range(0, len(free_variables))
                ]
            )

    return cast(output_violating, numerical=matrix_num, array=matrix_arr)


def dctc_respecting(
    input_respecting: mat | arr | QuantumState,
    input_violating: mat | arr | QuantumState,
    gate: mat | arr | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
) -> mat | arr:
    """Calculate the chronology-respecting (CR) state according to the D-CTC prescription's CR map

    .. math::

       \\MapDCTCsCR_{\\Unitary}[\\StateCR,\\StateCV]
           = \\trace_\\CV\\bigl[\\Unitary(\\StateCR \\otimes \\StateCV)\\Unitary^\\dagger\\bigr]

    given the chronology-respecting (CR) input state :python:`input_respecting` (:math:`\\StateCR`), chronology-violating (CV) solution state :python:`input_violating` (:math:`\\StateCV`), and (unitary) interaction described by :python:`gate` (:math:`\\Unitary`).

    Arguments
    ---------
    input_respecting : mat | arr | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    input_violating : mat | arr | QuantumState
        The matrix representation of the chronology-violating (CR) solution state.
    gate : mat | arr | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.

    Returns
    -------
    mat | arr
        The solution(s) of the D-CTC CR map.
    """
    if isinstance(input_respecting, mat | arr) is True:
        matrix_num = True if issubclass(dtype(input_respecting), num) is True else False
        matrix_arr = True if isinstance(input_respecting, arr) is True else False
    else:
        try:
            matrix_num = (
                True
                if issubclass(dtype(input_respecting.output()), num) is True
                else False
            )
            matrix_arr = (
                True if isinstance(input_respecting.output(), arr) is True else False
            )
        except:
            raise TypeError(
                """A matrix or array cannot be extracted from the given input state."""
            )

    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)),
            num_systems=len(systems_respecting),
        )

    input_respecting = densify(extract_matrix(input_respecting))
    input_violating = densify(extract_matrix(input_violating))
    input_total = assemble_composition(
        (input_respecting, systems_respecting), (input_violating, systems_violating)
    )

    gate = densify(extract_matrix(gate))
    output_total = matrix_multiplication(gate, input_total, conjugate_transpose(gate))
    output_respecting = partial_trace(
        matrix=output_total, targets=systems_violating, dim=dim
    )

    return cast(output_respecting, numerical=matrix_num, array=matrix_arr)


class DCTC(QuantumCTC):
    """A subclass for creating closed timelike curves described by Deutsch's prescription (D-CTCs) of quantum time travel.

    This is built upon the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class, and so inherits all of its attributes, properties, and methods.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    free_symbol : sym | str
        The representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points.
        Defaults to :python:`"g"`.
    maximum_entropy : bool
        Whether to, in the case of solution multiplicity, return solutions that correspond to the maximally entropic CV state, in accordance with Deutsch's original prescription.
        If :python:`False`, simply returns the ordinary (single or parametrized) solution.
        Defaults to :python:`False`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(
        self,
        *args,
        free_symbol: sym | str | None = None,
        maximum_entropy: bool | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        free_symbol = "g" if free_symbol is None else free_symbol
        maximum_entropy = False if maximum_entropy is None else maximum_entropy
        self.free_symbol = free_symbol
        self.maximum_entropy = maximum_entropy

    @property
    def free_symbol(self) -> sym | str:
        """The representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points."""
        return self._free_symbol

    @free_symbol.setter
    def free_symbol(self, free_symbol: sym | str):
        self._free_symbol = free_symbol

    @property
    def maximum_entropy(self) -> bool:
        """Whether to, in the case of solution multiplicity, return solutions that correspond to the maximally entropic CV state, in accordance with Deutsch's original prescription."""
        return self._maximum_entropy

    @maximum_entropy.setter
    def maximum_entropy(self, maximum_entropy: bool):
        self._maximum_entropy = maximum_entropy

    @property
    def input_is_vector(self) -> bool:
        return False
        # D-CTC prescription requires density matrix inputs.

    @property
    def output_is_vector(self) -> bool:
        return False
        # The CR and CV maps of a D-CTC are non-linear, non-unitary (mixing) operations in general.

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        """Compute the unprocessed matrix representation of the D-CTC chronology-respecting (CR) output state.

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
            The unprocessed matrix representation of the D-CTC CR output state.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array

        output_respecting = dctc_respecting(
            input_respecting=self.input(substitutions=[]),
            input_violating=self.state_violating(
                free_symbol=self.free_symbol,
                maximum_entropy=self.maximum_entropy,
            ),
            gate=self.gate(substitutions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )
        return cast(output_respecting, numerical=numerical, array=array)

    def output_violating(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        free_symbol: sym | str | None = None,
        maximum_entropy: bool | None = None,
    ) -> mat | arr:
        """Compute the processed matrix representation of the D-CTC chronology-violating (CV) state.

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
            Defaults to :python:`False`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`True`, normalizes to a value of :math:`1`.
            If :python:`False`, does not normalize.
            Defaults to :python:`False`.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of :python:`self.free_symbol`.
        maximum_entropy : bool
            Whether to, in the case of solution multiplicity, return the CV state that possesses the most (von Neumann) entropy, in accordance with Deutsch's original prescription.
            If :python:`False`, simply returns the ordinary (single or parametrized) solution.
            Defaults to the value of :python:`self.maximum_entropy`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the D-CTC CV output state.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        free_symbol = self.free_symbol if free_symbol is None else free_symbol
        maximum_entropy = (
            self.maximum_entropy if maximum_entropy is None else maximum_entropy
        )

        output_violating = dctc_violating(
            input_respecting=self.input(substitutions=[]),
            gate=self.gate(substitutions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
            free_symbol=free_symbol,
            maximum_entropy=maximum_entropy,
        )

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        output_violating = QuantumState(
            spec=output_violating,
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=False,
            norm=False,
            conjugation=False,
            label=None,
            notation=None,
            debug=False,
        )

        # Normalization
        norm = False if norm is None else norm
        norm = 1 if norm is True else norm
        if norm is not False:
            output_violating.normalize(norm)

        # Simplification
        simplification = self.simplification if simplification is None else simplification
        if simplification is True:
            output_violating.simplify()

        # Conjugation
        conjugation = False if conjugation is None else conjugation
        if conjugation is True:
            output_violating.dagger()

        output_violating = QuantumState(
            spec=output_violating.output(numerical=numerical, array=array_intermediate),
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            norm=False,
            conjugation=False,
            label=None,
            notation=None,
            debug=False,
        )

        return output_violating.output(numerical=numerical, array=array)

    def output_respecting(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        postprocess: bool | None = None,
        free_symbol: sym | str | None = None,
        maximum_entropy: bool | None = None,
    ) -> mat | arr:
        """Compute the matrix representation of the D-CTC chronology-respecting (CR) output state (including any post-processing, i.e., traces and postselections).

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
            Defaults to :python:`False`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`True`, normalizes to a value of :math:`1`.
            If :python:`False`, does not normalize.
            Defaults to :python:`False`.
        postprocess : bool
            Whether to post-process the state (i.e., perform the circuit's traces and postselections).
            Defaults to :python:`True`.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of :python:`self.free_symbol`.
        maximum_entropy : bool
            Whether to, in the case of solution multiplicity, return the CR solution that corresponds to the maximally entropic CV state, in accordance with Deutsch's original prescription.
            If :python:`False`, simply returns the ordinary (single or parametrized) solution.
            Defaults to the value of :python:`maximum_entropy`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the D-CTC CR output state.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        substitutions = self.substitutions if substitutions is None else substitutions
        free_symbol = self.free_symbol if free_symbol is None else free_symbol
        maximum_entropy = (
            self.maximum_entropy if maximum_entropy is None else maximum_entropy
        )

        output_respecting = dctc_respecting(
            input_respecting=self.input(
                numerical=numerical, array=array_intermediate, substitutions=[]
            ),
            input_violating=self.state_violating(
                numerical=numerical,
                array=array_intermediate,
                free_symbol=free_symbol,
                maximum_entropy=maximum_entropy,
            ),
            gate=self.gate(
                numerical=numerical, array=array_intermediate, substitutions=[]
            ),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        output_respecting = QuantumState(
            spec=output_respecting,
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=False,
            conjugation=False,
            norm=False,
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

        # Normalization
        norm = False if norm is None else norm
        norm = 1 if norm is True else norm
        if norm is not False:
            output_respecting.normalize(norm)

        # Simplification
        simplification = self.simplification if simplification is None else simplification
        if simplification is True:
            output_respecting.simplify()

        # Conjugation
        conjugation = False if conjugation is None else conjugation
        if conjugation is True:
            output_respecting.dagger()

        output_respecting = QuantumState(
            spec=output_respecting.output(
                numerical=numerical, array=array_intermediate
            ),
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            norm=False,
            conjugation=False,
            label=None,
            notation=None,
            debug=False,
        )
        return output_respecting.output(numerical=numerical, array=array)

    def output(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        postprocess: bool | None = None,
        free_symbol: sym | str | None = None,
        maximum_entropy: bool | None = None,
    ) -> mat | arr:
        """An alias for the :py:meth:`~qhronology.quantum.prescriptions.DCTC.output_respecting` method.

        Useful for polymorphism.

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
            Defaults to :python:`False`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`True`, normalizes to a value of :math:`1`.
            If :python:`False`, does not normalize.
            Defaults to :python:`False`.
        postprocess : bool
            Whether to post-process the state (i.e., perform the circuit's traces and postselections).
            Defaults to :python:`True`.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of :python:`self.free_symbol`.
        maximum_entropy : bool
            Whether to, in the case of solution multiplicity, return the CR solution that corresponds to the maximally entropic CV state, in accordance with Deutsch's original prescription.
            If :python:`False`, simply returns the ordinary (single or parametrized) solution.
            Defaults to the value of :python:`self.maximum_entropy`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the D-CTC CR output state.
        """
        return self.output_respecting(
            numerical=numerical,
            array=array,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            norm=norm,
            postprocess=postprocess,
            free_symbol=free_symbol,
            maximum_entropy=maximum_entropy,
        )

    def state_violating(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        debug: bool | None = None,
        free_symbol: sym | str | None = None,
        maximum_entropy: bool | None = None,
    ) -> QuantumState:
        """Compute the D-CTC chronology-violating (CV) state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        numerical : bool
            Whether to cast the state's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the state's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
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
        traces : list[int]
            A list of indices of the CV systems (relative to the entire circuit) on which to perform partial traces.
            Defaults to :python:`[]`.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of :python:`self.free_symbol`.
        maximum_entropy : bool
            Whether to, in the case of solution multiplicity, return the CV state that possesses the most (von Neumann) entropy, in accordance with Deutsch's original prescription.
            If :python:`False`, simply returns the ordinary (single or parametrized) solution.
            Defaults to the value of :python:`self.maximum_entropy`.
        debug : bool
            Whether to print the internal state (held in :python:`matrix`) on change.
            If :python:`False`, does not print.
            Defaults to :python:`False`.

        Returns
        -------
        QuantumState
            The D-CTC CV output state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False
        substitutions = self.substitutions if substitutions is None else substitutions
        simplification = self.simplification if simplification is None else simplification
        traces = [] if traces is None else traces

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        state = QuantumState(
            form=form,
            kind=kind,
            spec=self.output_violating(
                numerical=numerical,
                array=array_intermediate,
                substitutions=substitutions,
                simplification=simplification,
                conjugation=False,
                norm=norm,
                free_symbol=free_symbol,
                maximum_entropy=maximum_entropy,
            ),
            dim=self.dim,
            numerical=numerical,
            array=array,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            norm=False,
            label=label,
            notation=notation,
            debug=debug,
        )
        traces = adjust_targets(traces, self.systems_removed + self.systems_respecting)
        state.partial_trace(targets=traces)
        return state

    def state_respecting(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        postprocess: bool | None = None,
        debug: bool | None = None,
        free_symbol: sym | str | None = None,
        maximum_entropy: bool | None = None,
    ) -> QuantumState:
        """Compute the D-CTC chronology-respecting (CR) state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        numerical : bool
            Whether to cast the state's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the state's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
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
        traces : list[int]
            A list of indices of the CR systems (relative to the entire circuit) on which to perform partial traces.
            Performed regardless of the value of :python:`postprocess`.
            Defaults to :python:`[]`.
        postprocess : bool
            Whether to post-process the state (i.e., perform the circuit's traces and postselections).
            Defaults to :python:`True`.
        free_symbol : str
            The string representation of the algebraic symbol to be used as the free parameter in the case where the CV map has a multiplicity of fixed points.
            Defaults to the value of :python:`self.free_symbol`.
        maximum_entropy : bool
            Whether to, in the case of solution multiplicity, return the CR solution that corresponds to the maximally entropic CV state, in accordance with Deutsch's original prescription.
            If :python:`False`, simply returns the ordinary (single or parametrized) solution.
            Defaults to the value of :python:`self.maximum_entropy`.
        debug : bool
            Whether to print the internal state (held in :python:`matrix`) on change.
            If :python:`False`, does not print.
            Defaults to :python:`False`.

        Returns
        -------
        QuantumState
            The D-CTC CR output state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False
        substitutions = self.substitutions if substitutions is None else substitutions
        simplification = self.simplification if simplification is None else simplification
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

        state = QuantumState(
            spec=self.output_respecting(
                numerical=numerical,
                array=array_intermediate,
                substitutions=substitutions,
                simplification=simplification,
                conjugation=False,
                norm=norm,
                postprocess=postprocess,
                free_symbol=free_symbol,
                maximum_entropy=maximum_entropy,
            ),
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            norm=False,
            label=label,
            notation=notation,
            debug=debug,
        )
        state.partial_trace(targets=traces)
        return state


def pctc_violating(
    input_respecting: mat | arr | QuantumState,
    gate: mat | arr | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
) -> mat | arr:
    """Calculate the chronology-violating (CV) state according to the P-CTC weak-measurement tomography expression for the prescription's CV map

    .. math::

       \\MapPCTCsCV_{\\Unitary}[\\StateCR]
           = \\trace_\\CR\\bigl[\\Unitary(\\StateCR \\otimes \\tfrac{1}{\\Dimension}\\Identity)
           \\Unitary^\\dagger\\bigr]

    given the chronology-respecting (CR) input state :python:`input_respecting` (:math:`\\StateCR`) and interaction described by :python:`gate` (:math:`\\Unitary`).
    Here, :math:`\\Dimension` is the dimensionality of the CV Hilbert space (assumed to be equivalent to that of its CR counterpart), while :math:`\\Identity` is the :math:`\\Dimension \\times \\Dimension` identity matrix.

    Arguments
    ---------
    input_respecting : mat | arr | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    gate : mat | arr | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.

    Returns
    -------
    mat
        The weak-measurement tomography expression for the P-CTC CV state.

    Note
    ----
    The validity of the expression used in this function to compute the P-CTC CV state for *non-qubit* systems has not been proven.
    """
    if isinstance(input_respecting, mat | arr) is True:
        matrix_num = True if issubclass(dtype(input_respecting), num) is True else False
        matrix_arr = True if isinstance(input_respecting, arr) is True else False
    else:
        try:
            matrix_num = (
                True
                if issubclass(dtype(input_respecting.output()), num) is True
                else False
            )
            matrix_arr = (
                True if isinstance(input_respecting.output(), arr) is True else False
            )
        except:
            raise TypeError(
                """A matrix or array cannot be extracted from the given input state."""
            )

    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)),
            num_systems=len(systems_respecting),
        )

    input_respecting = densify(extract_matrix(input_respecting))
    identity = (sp.Rational(1, dim) ** len(systems_violating)) * sp.eye(
        dim ** len(systems_violating)
    )

    input_total = assemble_composition(
        (input_respecting, systems_respecting), (identity, systems_violating)
    )

    gate = densify(extract_matrix(gate))
    output_total = matrix_multiplication(gate, input_total, conjugate_transpose(gate))
    output_violating = partial_trace(
        matrix=output_total, targets=systems_respecting, dim=dim
    )
    return cast(output_violating, numerical=matrix_num, array=matrix_arr)


def pctc_respecting(
    input_respecting: mat | arr | QuantumState,
    gate: mat | arr | QuantumGate,
    systems_respecting: list[int],
    systems_violating: list[int],
) -> mat | arr:
    """Calculate the (non-renormalized) chronology-respecting (CR) state according to the P-CTC prescription's non-renormalizing CR map

    .. math::

       \\MapPCTCsCR_{\\Unitary}[\\StateCR]
           \\propto \\OperatorPCTC \\StateCR \\OperatorPCTC^\\dagger

    given the chronology-respecting (CR) input state :python:`input_respecting` (:math:`\\StateCR`) and (unitary) interaction described by :python:`gate` (:math:`\\Unitary`).
    Here,

    .. math:: \\OperatorPCTC \\equiv \\trace_\\CV[\\Unitary]

    is the P-CTC operator.

    Note
    ----
    This function does not renormalize the output state as per the renormalized P-CTC map

    .. math::

       \\MapPCTCsCR_{\\Unitary}[\\StateCR]
           = \\frac{\\OperatorPCTC \\StateCR \\OperatorPCTC^\\dagger}
           {\\trace\\bigl[ \\OperatorPCTC \\StateCR \\OperatorPCTC^\\dagger\\bigr]}.

    Arguments
    ---------
    input_respecting : mat | arr | QuantumState
        The matrix representation of the chronology-respecting (CR) input state.
    gate : mat | arr | QuantumGate
        The matrix representation of the gate describing the (unitary) interaction between the CR and CV systems.
    systems_respecting : list[int]
        The numerical indices of the chronology-respecting (CR) subsystems.
    systems_violating : list[int]
        The numerical indices of the chronology-violating (CV) subsystems.

    Returns
    -------
    mat
        The solution of the P-CTC CR map.
    """
    if isinstance(input_respecting, mat | arr) is True:
        matrix_num = True if issubclass(dtype(input_respecting), num) is True else False
        matrix_arr = True if isinstance(input_respecting, arr) is True else False
    else:
        try:
            matrix_num = (
                True
                if issubclass(dtype(input_respecting.output()), num) is True
                else False
            )
            matrix_arr = (
                True if isinstance(input_respecting.output(), arr) is True else False
            )
        except:
            raise TypeError(
                """A matrix or array cannot be extracted from the given input state."""
            )

    systems_respecting = list(set(systems_respecting))
    systems_violating = list(set(systems_violating))
    try:
        dim = input_respecting.dim
    except:
        dim = count_dims(
            matrix=densify(extract_matrix(input_respecting)),
            num_systems=len(systems_respecting),
        )

    input_respecting = extract_matrix(input_respecting)
    gate = densify(extract_matrix(gate))

    gate_reduced = partial_trace(matrix=gate, targets=systems_violating, dim=dim)
    if matrix_form(input_respecting) == Forms.VECTOR.value:
        input_respecting = columnify(input_respecting)
        output_respecting = gate_reduced * input_respecting
        # renormalization = recursively_simplify(sp.sqrt(1/trace(output_respecting)))
        # output_respecting = renormalization * output_respecting
    else:
        output_respecting = (
            gate_reduced * densify(input_respecting) * conjugate_transpose(gate_reduced)
        )
        # renormalization = recursively_simplify(1/trace(output_respecting))
        # output_respecting = renormalization * output_respecting
    return cast(output_respecting, numerical=matrix_num, array=matrix_arr)


class PCTC(QuantumCTC):
    """A subclass for creating closed timelike curves described by the postselected teleportation prescription (P-CTCs) of quantum time travel.

    This is built upon the :py:class:`~qhronology.quantum.prescriptions.QuantumCTC` class, and so inherits all of its attributes, properties, and methods.

    Arguments
    ---------
    *args
        Positional arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    **kwargs
        Arbitrary keyword arguments, passed directly to the constructor :python:`__init__` of the superclass :py:class:`~qhronology.quantum.gates.QuantumGate`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def matrix(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
    ) -> mat | arr:
        """Compute the unprocessed matrix representation of the P-CTC chronology-respecting (CR) output state.

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
            The unprocessed matrix representation of the P-CTC CR output state.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array

        output_respecting = pctc_respecting(
            input_respecting=self.input(substitutions=[]),
            gate=self.gate(substitutions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )
        return cast(output_respecting, numerical=numerical, array=array)

    def output_violating(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
    ) -> mat | arr:
        """Compute the processed matrix representation of the P-CTC chronology-violating (CV) state.

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
            Defaults to :python:`False`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`True`, normalizes to a value of :math:`1`.
            If :python:`False`, does not normalize.
            Defaults to :python:`False`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the D-CTC CV output state.

        Note
        ----
        The validity of the expression used in this method to compute the P-CTC CV state for *non-qubit* systems has not been proven.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False

        output_violating = pctc_violating(
            input_respecting=self.input(substitutions=[]),
            gate=self.gate(substitutions=[]),
            systems_respecting=self.systems_respecting,
            systems_violating=self.systems_violating,
        )

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        output_violating = QuantumState(
            spec=output_violating,
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=False,
            conjugation=False,
            norm=False,
            label=None,
            notation=None,
            debug=False,
        )

        # Normalization
        norm = False if norm is None else norm
        norm = 1 if norm is True else norm
        if norm is not False:
            output_violating.normalize(norm)

        # Simplification
        simplification = self.simplification if simplification is None else simplification
        if simplification is True:
            output_violating.simplify()

        # Conjugation
        conjugation = False if conjugation is None else conjugation
        if conjugation is True:
            output_violating.dagger()

        output_violating = QuantumState(
            spec=output_violating.output(numerical=numerical, array=array_intermediate),
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            norm=False,
            conjugation=False,
            label=None,
            notation=None,
            debug=False,
        )
        return output_violating.output(numerical=numerical, array=array)

    def output_respecting(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        postprocess: bool | None = None,
    ) -> mat | arr:
        """Compute the matrix representation of the P-CTC chronology-respecting (CR) output state (including any post-processing, i.e., traces and postselections).

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
            Defaults to :python:`False`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`True`, normalizes to a value of :math:`1`.
            If :python:`False`, does not normalize.
            Defaults to :python:`False`.
        postprocess : bool
            Whether to post-process the state (i.e., perform the circuit's traces and postselections).
            Defaults to :python:`True`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the P-CTC CR output state.

        Note
        ----
        The output state is not renormalized.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False
        substitutions = self.substitutions if substitutions is None else substitutions

        output_respecting = pctc_respecting(
            input_respecting=self.input(substitutions=[]),
            gate=self.gate(substitutions=[]),
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
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=False,
            conjugation=False,
            norm=False,
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

        # Normalization
        norm = False if norm is None else norm
        norm = 1 if norm is True else norm
        if norm is not False:
            output_respecting.normalize(norm)

        # Simplification
        simplification = self.simplification if simplification is None else simplification
        if simplification is True:
            output_respecting.simplify()

        # Conjugation
        conjugation = False if conjugation is None else conjugation
        if conjugation is True:
            output_respecting.dagger()

        output_respecting = QuantumState(
            spec=output_respecting.output(
                numerical=numerical, array=array_intermediate
            ),
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array_intermediate,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            norm=False,
            conjugation=False,
            label=None,
            notation=None,
            debug=False,
        )
        return output_respecting.output(numerical=numerical, array=array)

    def output(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        postprocess: bool | None = None,
    ) -> mat | arr:
        """An alias for the :py:meth:`~qhronology.quantum.prescriptions.PCTC.output_respecting` method.

        Useful for polymorphism.

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
            Defaults to :python:`False`.
        norm : bool | num | expr | str
            The value to which the state is normalized.
            If :python:`True`, normalizes to a value of :math:`1`.
            If :python:`False`, does not normalize.
            Defaults to :python:`False`.
        postprocess : bool
            Whether to post-process the state (i.e., perform the circuit's traces and postselections).
            Defaults to :python:`True`.

        Returns
        -------
        mat | arr
            The processed matrix representation of the P-CTC CR output state.

        Note
        ----
        The output state is not renormalized.
        """
        return self.output_respecting(
            numerical=numerical,
            array=array,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            norm=norm,
            postprocess=postprocess,
        )

    def state_violating(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        debug: bool | None = None,
    ) -> QuantumState:
        """Compute the P-CTC chronology-violating (CV) state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        numerical : bool
            Whether to cast the state's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the state's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
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
        traces : list[int]
            A list of indices of the CV systems (relative to the entire circuit) on which to perform partial traces.
            Defaults to :python:`[]`.
        debug : bool
            Whether to print the internal state (held in :python:`matrix`) on change.
            If :python:`False`, does not print.
            Defaults to :python:`False`.

        Returns
        -------
        QuantumState
            The P-CTC CV output state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Note
        ----
        The validity of the expression used in this method to compute the P-CTC CV state for *non-qubit* systems has not been proven.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False
        substitutions = self.substitutions if substitutions is None else substitutions
        simplification = self.simplification if simplification is None else simplification
        traces = [] if traces is None else traces

        form = Forms.MATRIX.value
        kind = Kinds.MIXED.value

        state = QuantumState(
            form=form,
            kind=kind,
            spec=self.output_violating(
                numerical=numerical,
                array=array_intermediate,
                substitutions=substitutions,
                simplification=simplification,
                conjugation=False,
                norm=norm,
            ),
            dim=self.dim,
            numerical=numerical,
            array=array,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            norm=False,
            label=label,
            notation=notation,
            debug=debug,
        )
        traces = adjust_targets(traces, self.systems_removed + self.systems_respecting)
        state.partial_trace(targets=traces)
        return state

    def state_respecting(
        self,
        numerical: bool | None = None,
        array: bool | None = None,
        substitutions: list[tuple[num | expr | str, num | expr | str]] | None = None,
        simplification: bool | None = None,
        conjugation: bool | None = None,
        norm: bool | num | expr | str | None = None,
        label: str | None = None,
        notation: str | None = None,
        traces: list[int] | None = None,
        postprocess: bool | None = None,
        debug: bool | None = None,
    ) -> QuantumState:
        """Compute the P-CTC chronology-respecting (CR) state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Arguments
        ---------
        numerical : bool
            Whether to cast the state's matrix elements as floating-point values (:python:`True`) (if possible) or exact values (:python:`False`).
            Defaults to the value of :python:`self.numerical`.
        array : bool
            Whether to cast the state's matrix as a NumPy array (:python:`True`) or SymPy matrix (:python:`False`).
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
        traces : list[int]
            A list of indices of the CR systems (relative to the entire circuit) on which to perform partial traces.
            Performed regardless of the value of :python:`postprocess`.
            Defaults to :python:`[]`.
        postprocess : bool
            Whether to post-process the state (i.e., perform the circuit's traces and postselections).
            Defaults to :python:`True`.
        debug : bool
            Whether to print the internal state (held in :python:`matrix`) on change.
            If :python:`False`, does not print.
            Defaults to :python:`False`.

        Returns
        -------
        QuantumState
            The P-CTC CR output state as a :py:class:`~qhronology.quantum.states.QuantumState` instance.

        Note
        ----
        The output state is not renormalized if :python:`norm` is :python:`False`.
        """
        numerical = self.numerical if numerical is None else numerical
        array = self.array if array is None else array
        array_intermediate = True if numerical is True else False
        substitutions = self.substitutions if substitutions is None else substitutions
        simplification = self.simplification if simplification is None else simplification
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

        state = QuantumState(
            spec=self.output_respecting(
                numerical=numerical,
                array=array_intermediate,
                substitutions=substitutions,
                simplification=simplification,
                conjugation=False,
                norm=norm,
                postprocess=postprocess,
            ),
            form=form,
            kind=kind,
            dim=self.dim,
            numerical=numerical,
            array=array,
            symbols=self.symbols,
            substitutions=substitutions,
            simplification=simplification,
            conjugation=conjugation,
            norm=False,
            label=label,
            notation=notation,
            debug=debug,
        )
        state.partial_trace(targets=traces)
        return state
