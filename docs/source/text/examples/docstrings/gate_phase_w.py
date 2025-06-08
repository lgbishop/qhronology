from qhronology.quantum.gates import *

W = Phase(phase="w", dim=3, label="W")
W.diagram()
print(repr(W.output()))
W.print()
