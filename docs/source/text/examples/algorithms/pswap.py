from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Swap
from qhronology.quantum.circuits import QuantumCircuit

# Input
input_upper = VectorState(
    spec=[("a", [0]), ("b", [1])],
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    dim=2,
    norm=1,
    label="ψ",
)
input_lower = VectorState(
    spec=[("c", [0]), ("d", [1])],
    symbols={"c": {"complex": True}, "d": {"complex": True}},
    conditions=[("c*conjugate(c) + d*conjugate(d)", 1)],
    dim=2,
    norm=1,
    label="φ",
)

# Gate
S = Swap(
    targets=[0, 1],
    num_systems=2,
    exponent="p",
    symbols={"p": {"real": True}},
    notation="S^p",
)

# Circuit
pswap = QuantumCircuit(
    inputs=[input_upper, input_lower],
    gates=[S],
)
pswap.diagram()

# Output
input_state = pswap.input(label="ψ,φ", simplify=True)
output_state = pswap.state(label="(ψ,φ)′", simplify=True)

# Results
print(repr(pswap.gate()))
input_state.print()
output_state.print()
