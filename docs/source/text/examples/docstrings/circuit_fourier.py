from qhronology.quantum.states import MatrixState
from qhronology.quantum.gates import Hadamard, Phase, Fourier
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp

size = 4  # Adjust the number of qudits
dim = 2  # Adjust the dimensionality of the Fourier transform

# Input
rho = sp.MatrixSymbol("ρ", dim**size, dim**size).as_mutable()
input_state = MatrixState(spec=rho, dim=dim, label="ρ")

# Gates
QFT = []
for i in range(0, size):
    count = size - i
    for j in range(0, count):
        if j == 0:
            QFT.append(Hadamard(targets=[i], dim=dim, num_systems=size))
        else:
            QFT.append(
                Phase(
                    targets=[i + j],
                    controls=[i],
                    exponent=sp.Rational(1, dim**j),
                    dim=dim,
                    num_systems=size,
                    label=f"{dim**j}",
                    family="GATE",
                )
            )

# Circuit
fourier = QuantumCircuit(inputs=[input_state], gates=QFT)
fourier.diagram(pad=(0, 0), sep=(0, 1), style="unicode")

# Output
print(repr(fourier.gate()))
