from qhronology.quantum.states import VectorState, MatrixState
from qhronology.quantum.gates import Not, Hadamard, Phase, Pauli
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.utilities.helpers import flatten_list

import sympy as sp

# Input
tau = sp.MatrixSymbol("τ", 2, 2).as_mutable()
unknown_state = MatrixState(spec=tau, label="τ")

probe_state = VectorState(
    spec=[("sqrt((1 + ε)/2)", [0]), ("sqrt((1 - ε)/2)", [1])],
    symbols={"ε": {"real": True, "nonnegative": True}},
    conditions=[
        ("ε", "1 - ε"),
        ("ε", "1 - ε"),
    ],  # Describes the fact that ε is between 0 and 1 (inclusive)
    label="χ",
)

# Gates
CN = Not(targets=[1], controls=[0], num_systems=2)
HI = Hadamard(targets=[0], num_systems=2)
PI = Phase(exponent=1 / 2, targets=[0], num_systems=2)

VI = [[HI], [PI, HI], []]

# Circuits
evolved_probe_states = []
for gates in VI:
    gates_pre = gates
    gates_post = gates[::-1]
    for gate in gates_post:
        gate.conjugate = True

    tomography = QuantumCircuit(
        inputs=[unknown_state, probe_state],
        gates=flatten_list([gates_pre, CN, gates_post]),
        traces=[0],
    )
    tomography.diagram()
    evolved_probe_state = tomography.state(label="ω")
    evolved_probe_states.append(evolved_probe_state)

# Weak-measurement quantum state tomography
Z = Pauli(index=3, targets=[0], num_systems=1)
expectations = []
expectations.append(1)  # Expectation value corresponding to the identity operator
for state in evolved_probe_states:
    state.coefficient("1/ε")
    statistics = state.measure(
        operators=[Z], targets=[0], statistics=True, observable=True
    )
    expectation = statistics[0]
    expectations.append(expectation)

# Reconstruct state via Bloch-sphere representation using weak measurements
pauli_matrices = [
    Pauli(index=i, targets=[0], num_systems=1).output() for i in range(0, 4)
]
spec = sp.zeros(2)
for i in range(0, 4):
    spec += expectations[i] * pauli_matrices[i]
reconstructed_state = MatrixState(
    spec=sp.Matrix(spec),
    conditions=[(tau[1, 1], 1 - tau[0, 0]), (1 - tau[0, 0], tau[1, 1])],
    label="τ",
)
reconstructed_state.coefficient(sp.Rational(1, 2))  # Manually normalize
reconstructed_state.simplify()

# Results
unknown_state.print()
reconstructed_state.print()
