from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
input_upper = VectorState(
    spec=[("a", [0]), ("b", [1])],
    substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    label="ψ",
)
input_lower = VectorState(
    spec=[("c", [0]), ("d", [1])],
    substitutions=[("c*conjugate(c) + d*conjugate(d)", 1)],
    label="φ",
)

# Gates
CN = Not(targets=[1], controls=[0])
NC = Not(targets=[0], controls=[1])

# Circuit
swapcnots = QuantumCircuit(
    inputs=[input_upper, input_lower],
    gates=[CN, NC, CN],
)
swapcnots.diagram()

# Output
output_total = swapcnots.state(label="(ψ⊗φ)′")
output_upper = swapcnots.state(traces=[1], label="ψ′")
output_lower = swapcnots.state(traces=[0], label="φ′")
output_upper.kind = "pure"
output_lower.kind = "pure"
output_upper.simplify()
output_lower.simplify()

# Results
print(repr(swapcnots.gate()))
input_upper.print()
input_lower.print()
swapcnots.input().print()

output_upper.print()
output_lower.print()
output_total.print()

print(output_upper.distance(input_lower))
print(output_lower.distance(input_upper))
print(output_upper.fidelity(input_lower))
print(output_lower.fidelity(input_upper))
