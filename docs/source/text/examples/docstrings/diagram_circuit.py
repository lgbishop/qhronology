from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Not, Measurement, Pauli, GateInterleave
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.matrices import ket

# Input
teleporting_state = VectorState(
    spec=[["a", "b"]],
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b)", "1")],
    label="ψ",
)
zero_state = VectorState(spec=[(1, [0, 0])], label="0,0")

# Gates
IHI = Hadamard(targets=[1], num_systems=3)
ICN = Not(targets=[2], controls=[1], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
HII = Hadamard(targets=[0], num_systems=3)
IMI = Measurement(
    operators=[ket(0), ket(1)], observable=False, targets=[1], num_systems=3
)
MII = Measurement(
    operators=[ket(0), ket(1)], observable=False, targets=[0], num_systems=3
)
MMI = GateInterleave(MII, IMI)
ICX = Pauli(index=1, targets=[2], controls=[1], num_systems=3)
CIZ = Pauli(index=3, targets=[2], controls=[0], num_systems=3)

# Circuit
circuit = QuantumCircuit(
    inputs=[teleporting_state, zero_state],
    gates=[IHI, ICN, CNI, HII, MMI, ICX, CIZ],
    traces=[0, 1],
)
