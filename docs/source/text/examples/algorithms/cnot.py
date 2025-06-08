from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
first_state = VectorState(
    spec=[("a", [0]), ("b", [1])],
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b)", "1")],
    label="x",
)
second_state = VectorState(
    spec=[("c", [0]), ("d", [1])],
    symbols={"c": {"complex": True}, "d": {"complex": True}},
    conditions=[("c*conjugate(c) + d*conjugate(d)", "1")],
    label="y",
)

# Gate
CN = Not(targets=[1], controls=[0], num_systems=2)

# Circuit
circuit = QuantumCircuit(inputs=[first_state, second_state], gates=[CN])
circuit.diagram()

# Output
output_state = circuit.state(label="x, x ⊕ y")

# Results
first_state.print()
second_state.print()
output_state.print()
