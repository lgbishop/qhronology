from qhronology.quantum.gates import *

S = Swap(targets=[0, 1])
S.diagram()
print(repr(S.output()))
S.print()
