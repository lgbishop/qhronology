from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Phase, Not, GateInterleave
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp

# Input
first_state = VectorState(
    spec=[("a", [0]), ("b", [1])],
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b)", "1")],
    label="x",
)
second_state = VectorState(
    spec=[("c", [0]), ("d", [1])],
    symbols={"c": {"complex": True}, "d": {"complex": True}},
    conditions=[("c*conjugate(c) + d*conjugate(d)", "1")],
    label="y",
)
third_state = VectorState(
    spec=[("u", [0]), ("v", [1])],
    symbols={"u": {"complex": True}, "v": {"complex": True}},
    conditions=[("u*conjugate(u) + v*conjugate(v)", "1")],
    label="z",
)

# Gates
IIH = Hadamard(targets=[2], num_systems=3)
TII = Phase(exponent=sp.Rational(1, 4), targets=[0], num_systems=3, label="T")
ITI = Phase(exponent=sp.Rational(1, 4), targets=[1], num_systems=3, label="T")
IIT = Phase(exponent=sp.Rational(1, 4), targets=[2], num_systems=3, label="T")
TTT = GateInterleave(TII, ITI, IIT)
NCI = Not(targets=[0], controls=[1], num_systems=3)
INC = Not(targets=[1], controls=[2], num_systems=3)
CIN = Not(targets=[2], controls=[0], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
ItI = Phase(
    exponent=sp.Rational(1, 4), conjugate=True, targets=[1], num_systems=3, label="T^†"
)
tII = Phase(
    exponent=sp.Rational(1, 4), conjugate=True, targets=[0], num_systems=3, label="T^†"
)
ttT = GateInterleave(tII, ItI, IIT)
NCH = GateInterleave(NCI, IIH)

# Circuit
circuit = QuantumCircuit(
    inputs=[first_state, second_state, third_state],
    gates=[IIH, TTT, NCI, INC, CIN, ItI, CNI, ttT, INC, CIN, NCH],
)
circuit.diagram(force_separation=True)

# Output
output_state = circuit.state(label="x, y, z ⊕ xy")

# Results
first_state.print()
second_state.print()
third_state.print()
output_state.print()
