from qhronology.quantum.states import VectorState
from qhronology.quantum.circuits import QuantumCircuit

# Input
input_state = VectorState(
    spec=[("a", [0]), ("b", [1])],
    conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    label="ψ",
)
bell = VectorState(spec=[(1, [0, 0]), (1, [1, 1])], norm=False, label="Φ")

# Circuit
postselection = QuantumCircuit(
    inputs=[input_state, bell], gates=[], postselections=[(bell, [0, 1])]
)
postselection.diagram(pad=(0, 0), sep=(4, 1), style="unicode")

# Output
output_state = postselection.state(label="ψ'")
input_state.print()
output_state.print()
