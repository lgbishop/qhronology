from qhronology.quantum.gates import *

paulis = [Pauli(index=i) for i in range(1,4)]
XYZ = GateStack(*paulis)
XYZ.diagram()
