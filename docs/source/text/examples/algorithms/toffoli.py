from qhronology.quantum.gates import Hadamard, Phase, Not, GateInterleave
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp

# Gates
IIH = Hadamard(targets=[2], num_systems=3)
TII = Phase(
    exponent=sp.Rational(1, 4),
    targets=[0],
    num_systems=3,
    label="T",
)
ITI = Phase(
    exponent=sp.Rational(1, 4),
    targets=[1],
    num_systems=3,
    label="T",
)
IIT = Phase(
    exponent=sp.Rational(1, 4),
    targets=[2],
    num_systems=3,
    label="T",
)
TTT = GateInterleave(TII, ITI, IIT)
NCI = Not(targets=[0], controls=[1], num_systems=3)
INC = Not(targets=[1], controls=[2], num_systems=3)
CIN = Not(targets=[2], controls=[0], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
ItI = Phase(
    exponent=sp.Rational(1, 4),
    conjugate=True,
    targets=[1],
    num_systems=3,
    label="T^†",
)
tII = Phase(
    exponent=sp.Rational(1, 4),
    conjugate=True,
    targets=[0],
    num_systems=3,
    label="T^†",
)
ttT = GateInterleave(tII, ItI, IIT)
NCH = GateInterleave(NCI, IIH)

# Circuit
toffoli = QuantumCircuit(
    gates=[IIH, TTT, NCI, INC, CIN, ItI, CNI, ttT, INC, CIN, NCH],
)
toffoli.diagram(force_separation=True, visible={"gates"})

# Results
print(repr(toffoli.gate(simplify=True)))