from qhronology.quantum.gates import *

L = GellMann(index=8)
L.diagram()
print(repr(L.output()))
L.print()
