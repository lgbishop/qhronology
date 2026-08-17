from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

CNOT = Not(targets=[2], controls=[0])
decomposition = CNOT.decompose(
    gates=[Not(targets=[1], controls=[0])],
    only_targets=False,
    preserve_structure=True,
)[0]
QuantumCircuit(gates=decomposition).diagram(sep=(2, 1), force_separation=True, visible={"gates"})
