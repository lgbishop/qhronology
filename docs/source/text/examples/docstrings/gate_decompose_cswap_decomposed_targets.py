from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

CSWAP = Swap(targets=[0, 2], controls=[1])
decomposition = CSWAP.decompose(
    gates=[Not()],
    additional_nodes=(0, 2, 0),
    only_targets=False,
)[0]
QuantumCircuit(gates=decomposition).diagram(sep=(2, 1), force_separation=True, visible={"gates"})
