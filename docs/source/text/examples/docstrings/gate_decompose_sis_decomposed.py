from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

SWAP = Swap(targets=[0, 3])
decomposition = SWAP.decompose(
    gates=[Swap()],
    preserve_structure=True,
    include_empty=True,
)[0]
QuantumCircuit(gates=decomposition).diagram(sep=(2, 1), force_separation=True, visible={"gates"})
