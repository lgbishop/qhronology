from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Swap
from qhronology.quantum.circuits import QuantumCircuit

# Input
input_upper = VectorState(
    spec=[("a", [0]), ("b", [1])],
    conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    label="ψ",
)
input_lower = VectorState(
    spec=[("c", [0]), ("d", [1])],
    conditions=[("c*conjugate(c) + d*conjugate(d)", 1)],
    label="φ",
)

# Gate
SWAP = Swap(targets=[0, 1])

# Circuits
circuit = QuantumCircuit(inputs=[input_upper, input_lower], gates=[SWAP])
circuit_upper = QuantumCircuit(
    inputs=[input_upper, input_lower], gates=[SWAP], traces=[0]
)
circuit_lower = QuantumCircuit(
    inputs=[input_upper, input_lower], gates=[SWAP], traces=[1]
)

circuit_lower.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

# Output
output_total = circuit.state(label="(ψ⊗φ)′")
output_lower = circuit_upper.state(simplify=True, label="ψ")
output_upper = circuit_lower.state(simplify=True, label="φ")
output_lower.kind = "pure"
output_upper.kind = "pure"

output_total.print(product=True)
output_lower.print(product=True)
output_upper.print(product=True)
