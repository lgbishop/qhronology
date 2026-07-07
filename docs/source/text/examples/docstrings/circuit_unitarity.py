from qhronology.quantum.gates import QuantumGate
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.operations import dagger

import sympy as sp

# Construct unitary matrix, along with its substitutions and symbols
unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
substitutions = [
    ((dagger(unitary) * unitary)[i, j], sp.eye(2)[i, j])
    for i in range(0, 2)
    for j in range(0, 2)
]
symbols = {unitary[i, j]: {"complex": True} for i in range(0, 2) for j in range(0, 2)}

# Gates
U = QuantumGate(
    spec=unitary,
    symbols=symbols,
    substitutions=substitutions,
    label="U",
)
Ud = QuantumGate(
    spec=unitary,
    symbols=symbols,
    substitutions=substitutions,
    label="U^†",
    conjugate=True,
)

# Circuit
unitarity = QuantumCircuit(gates=[U, Ud])
unitarity.diagram(
    pad=(0, 0),
    sep=(1, 1),
    style="unicode",
    visible={"gates"},
)

# Output
print(repr(U))
print(repr(Ud))
print(repr(unitarity.gate(simplify=True)))
