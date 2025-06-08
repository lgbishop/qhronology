from qhronology.quantum.gates import *

ZZ = Pauli(index=3, targets=[0, 1], label="Z⊗Z")
ZZ.diagram()
print(repr(ZZ.output()))
ZZ.print()
