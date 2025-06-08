from qhronology.quantum.gates import *

X = Pauli(index=1)
Y = Pauli(index=2)
Z = Pauli(index=3)
XYZ = GateStack(X, Y, Z)
XYZ.diagram(sep=(1, 2))
print(repr(XYZ.output()))
XYZ.print()
