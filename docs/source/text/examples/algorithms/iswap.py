from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Pauli, Hadamard, Not, GateStack
from qhronology.quantum.circuits import QuantumCircuit

# Input
psi = VectorState(
    spec=[("a", [0]), ("b", [1])],
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b)", "1")],
    label="ψ",
)
phi = VectorState(
    spec=[("c", [0]), ("d", [1])],
    symbols={"c": {"complex": True}, "d": {"complex": True}},
    conditions=[("c*conjugate(c) + d*conjugate(d)", "1")],
    label="φ",
)

# Gates
S = Pauli(index=3, exponent=1 / 2, label="S")
SS = GateStack(S, S)
HI = Hadamard(targets=[0], num_systems=2)
CN = Not(targets=[1], controls=[0])
NC = Not(targets=[0], controls=[1])
IH = Hadamard(targets=[1], num_systems=2)

# Circuit
iswap = QuantumCircuit(inputs=[psi, phi], gates=[SS, HI, CN, NC, IH])
iswap.diagram()

# Output
input_state = QuantumCircuit(inputs=[psi, phi]).state(label="ψ,φ")
output_state = iswap.state(label="(ψ,φ)'")
output_state.simplify()

# Results
print(repr(iswap.gate(simplify=True)))
input_state.print()
output_state.print()
