# Based on: https://arxiv.org/abs/2106.06015

from qhronology.quantum.gates import Hadamard, Pauli, Not, Phase, GateStack
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp

HXH = GateStack(Hadamard(), Pauli(index=1), Hadamard())
CNI = Not(targets=[1], controls=[0])
YTZ = GateStack(
    Pauli(index=2),
    Phase(exponent=sp.Rational(1, 4), label="T"),
    Pauli(index=3),
)
INC = Not(targets=[1], controls=[2])

gates = [HXH, CNI, YTZ, INC]

circuit = QuantumCircuit(gates=gates)
circuit.diagram(sep=(0, 2), uniform_spacing=True)
circuit.decompactify()
circuit.diagram(sep=(0, 2), uniform_spacing=True)