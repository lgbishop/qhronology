from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
input_state = VectorState(spec=[("a", [0]), ("b", [1])], label="ψ")

# Gate
NOT = Not()

# Circuit
bitflip = QuantumCircuit(inputs=[input_state], gates=[NOT])
bitflip.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

# Output
output_state = bitflip.state(label="ψ'")

# Results
input_state.print()
output_state.print()
