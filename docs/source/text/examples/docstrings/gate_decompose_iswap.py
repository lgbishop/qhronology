from qhronology.quantum.gates import *

iSWAP = QuantumGate(
    spec=[
        [1,    0,    0, 0],
        [0,    0, sp.I, 0],
        [0, sp.I,    0, 0],
        [0,    0,    0, 1],
    ],
    label="iSWAP",
)
iSWAP.diagram()
