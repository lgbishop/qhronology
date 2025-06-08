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
third_state = VectorState(
    spec=[("u", [0]), ("v", [1])],
    symbols={"u": {"complex": True}, "v": {"complex": True}},
    conditions=[("u*conjugate(u) + v*conjugate(v)", "1")],
    label="z",
)

# Gate
CCN = Not(targets=[2], controls=[0, 1], num_systems=3)

# Circuit
circuit = QuantumCircuit(inputs=[first_state, second_state, third_state], gates=[CCN])
circuit.diagram()

# Output
output_state = circuit.state(label="x, y, z ⊕ xy")

# Results
first_state.print()
second_state.print()
third_state.print()
output_state.print()
