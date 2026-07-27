from qhronology.quantum.states import MatrixState
from qhronology.quantum.gates import Hadamard, Phase
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp

size = 4  # The number of qudits
dim = 2  # The dimensionality of the Fourier transform

# Gates
QFT = []
for i in range(0, size):
    count = size - i
    for j in range(0, count):
        if j == 0:
            QFT.append(
                Hadamard(
                    targets=[i],
                    num_systems=size,
                    dim=dim,
                )
            )
        else:
            QFT.append(
                Phase(
                    targets=[i],
                    controls=[i + j],
                    exponent=sp.Rational(1, dim**j),
                    num_systems=size,
                    dim=dim,
                    label=f"{dim**j}",
                    family="GATE",
                )
            )

# Circuit
fourier = QuantumCircuit(gates=QFT)
fourier.diagram(sep=(0, 1), visible={"gates"})

# Results
print(repr(fourier.gate()))
