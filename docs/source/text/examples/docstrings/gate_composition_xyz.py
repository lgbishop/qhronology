from qhronology.quantum.gates import *

XII = Pauli(index=1, targets=[0], num_systems=3)
IYI = Pauli(index=2, targets=[1], num_systems=3)
IIZ = Pauli(index=3, targets=[2], num_systems=3)
XYZ = GateInterleave(XII, IYI, IIZ)
XYZ.diagram(sep=(1, 2))
print(repr(XYZ.output()))
XYZ.print()
