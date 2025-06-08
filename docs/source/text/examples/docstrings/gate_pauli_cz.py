from qhronology.quantum.gates import *

CZ = Pauli(index=3, targets=[1], controls=[0])
CZ.diagram()
print(repr(CZ.output()))
CZ.print()
