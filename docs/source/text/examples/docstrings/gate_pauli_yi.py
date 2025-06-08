from qhronology.quantum.gates import *

YI = Pauli(index=2, targets=[0], num_systems=2)
YI.diagram()
print(repr(YI.output()))
YI.print()
