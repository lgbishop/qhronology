from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Rotation, Not
from qhronology.quantum.circuits import QuantumCircuit

num_systems = 4

# Input
zero_state = VectorState(spec=[(1, [0])], label="0")
input_states = [zero_state for _ in range(0, num_systems)]

# Gates
ROTs = [
    Rotation(
        axis=2,
        angle=f"2*acos(sqrt(1/({num_systems})))",
        targets=[0],
        num_systems=num_systems,
    )
] + [
    Rotation(
        axis=2,
        angle=f"2*acos(sqrt(1/({num_systems} - {i})))",
        targets=[i],
        controls=[i - 1],
        num_systems=num_systems,
    )
    for i in range(1, num_systems - 1)
]
NOTs = [
    Not(
        targets=[num_systems - (i + 1)],
        controls=[num_systems - i - 2],
        num_systems=num_systems,
    )
    for i in range(0, num_systems - 1)
] + [
    Not(
        targets=[0],
        num_systems=num_systems,
    )
]

gates = ROTs + NOTs

# Circuit
generator = QuantumCircuit(inputs=input_states, gates=gates)
generator.diagram()

# Output
w_state = generator.state(label="W")
w_state.simplify()

# Results
w_state.print()
