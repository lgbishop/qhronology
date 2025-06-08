from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Rotation, Swap, Pauli, Diagonal, GateInterleave
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
IRy = Rotation(axis=2, angle="pi/2", targets=[1], num_systems=2)
RSWAP = Swap(targets=[0, 1], exponent=1 / 2)
ZI = Pauli(index=3, targets=[0], num_systems=2)
RzRz = Rotation(axis=3, angle="-pi/2", targets=[0, 1], num_systems=2)
IRy_dag = Rotation(axis=2, angle="-pi/2", targets=[1], num_systems=2, label="R")
PI = Diagonal(
    entries={0: "-pi/2", 1: "-pi/2"}, exponentiation=True, targets=[0], num_systems=2
)
PR = GateInterleave(IRy_dag, PI)

# Circuit
CNOT = QuantumCircuit(inputs=[psi, phi], gates=[IRy, RSWAP, ZI, RSWAP, RzRz, PR])
CNOT.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

# Output
print(repr(CNOT.gate(simplify=True)))
output = CNOT.state(label="(ψ⊗φ)'")
output.simplify()

CNOT.input().print()
output.print()
