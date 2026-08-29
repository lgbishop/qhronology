from qhronology.quantum.gates import Hadamard, Phase, Not
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp

IIH = Hadamard(targets=[2])
TII = Phase(exponent=sp.Rational(1, 4), targets=[0], label="T")
ITI = Phase(exponent=sp.Rational(1, 4), targets=[1], label="T")
IIT = Phase(exponent=sp.Rational(1, 4), targets=[2], label="T")
NCI = Not(targets=[0], controls=[1])
INC = Not(targets=[1], controls=[2])
CIN = Not(targets=[2], controls=[0])
CNI = Not(targets=[1], controls=[0])
ItI = Phase(exponent=sp.Rational(1, 4), targets=[1], label="t", conjugate=True)
tII = Phase(exponent=sp.Rational(1, 4), targets=[0], label="t", conjugate=True)

circuit = QuantumCircuit(
    gates=[IIH, TII, ITI, IIT, NCI, INC, CIN, ItI, CNI, tII, ItI, IIT, INC, CIN, NCI, IIH],
)
circuit.compactify()
circuit.diagram(sep=(1, 2), force_separation=True, visible={"gates"})