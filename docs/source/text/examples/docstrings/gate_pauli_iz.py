from qhronology.quantum.gates import *

IZ = Pauli(index=3, targets=[1])
IZ.diagram()
print(repr(IZ.output()))
IZ.print()
