from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

n = 4
CXXXX = Not(targets=list(range(1, n + 1)), controls=[0])
decomposition = CXXXX.decompose(gates=[Not()])[0]
QuantumCircuit(gates=decomposition).diagram(sep=(2, 1), force_separation=True, visible={"gates"})
