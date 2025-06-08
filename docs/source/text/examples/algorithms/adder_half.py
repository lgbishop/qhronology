from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
augend_state = VectorState(spec=[("a", [0]), ("b", [1])], label="x")
addend_state = VectorState(spec=[(1, [1])], label="y")
zero_state = VectorState(spec=[(1, [0])], label="0")

# Gates
CCN = Not(targets=[2], controls=[0, 1], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)

# Circuit
adder = QuantumCircuit(
    inputs=[augend_state, addend_state, zero_state], gates=[CCN, CNI]
)
adder.diagram()

# Output
sum_state = adder.state(label="s", traces=[0, 2])
carry_output_state = adder.state(label="c'", traces=[0, 1])

# Results
augend_state.print()
addend_state.print()
sum_state.print()
carry_output_state.print()
