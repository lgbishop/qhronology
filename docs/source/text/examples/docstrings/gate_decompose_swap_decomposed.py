from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

SWAP = Swap()
decomposition = SWAP.decompose(
    gates=[Not(targets=[0], controls=[1])]
)[0]
QuantumCircuit(gates=decomposition).diagram(pad=(1, 0), sep=(2, 1), force_separation=True, visible={"gates"})
