from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

paulis = [Pauli(index=i) for i in range(1,4)]
XYZ = GateStack(*paulis)
decomposition = XYZ.decompose(gates=paulis)[0]
QuantumCircuit(gates=decomposition).diagram(pad=(1, 0), uniform_spacing=True, visible={"gates"})
