from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
psi = VectorState(
    spec=[("a", [0]), ("b", [1])],
    conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    label="ψ",
)
phi = VectorState(
    spec=[("c", [0]), ("d", [1])],
    conditions=[("c*conjugate(c) + d*conjugate(d)", 1)],
    label="φ",
)

# Gates
CN = Not(targets=[1], controls=[0])
NC = Not(targets=[0], controls=[1])

# Circuit
swapcnots = QuantumCircuit(inputs=[psi, phi], gates=[CN, NC, CN])
swapcnots.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

# Output
print(repr(swapcnots.gate()))
upper = swapcnots.state(traces=[1], label="ψ'")
lower = swapcnots.state(traces=[0], label="φ'")
upper.kind = "pure"
lower.kind = "pure"
upper.simplify()
lower.simplify()

# Results
psi.print()
upper.print()
phi.print()
lower.print()

print(upper.distance(phi))
print(lower.distance(psi))

print(upper.fidelity(phi))
print(lower.fidelity(psi))
