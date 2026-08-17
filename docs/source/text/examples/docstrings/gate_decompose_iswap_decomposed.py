from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

iSWAP = QuantumGate(
    spec=[
        [1,    0,    0, 0],
        [0,    0, sp.I, 0],
        [0, sp.I,    0, 0],
        [0,    0,    0, 1],
    ],
    label="iSWAP",
)
decomposition = iSWAP.decompose(
    gates=[
        Not(targets=[0], controls=[1]),
        Phase(exponent=sp.Rational(1, 2), label="S"),
    ],
)[0]
QuantumCircuit(gates=decomposition).diagram(pad=(1, 0), sep=(2, 1), force_separation=True, visible={"gates"})
