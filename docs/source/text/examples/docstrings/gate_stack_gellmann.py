from qhronology.quantum.gates import *

gates = [GellMann(index=i) for i in range(1, 9)]
L = GateStack(*gates)
L.diagram(sep=(1, 1))
print(repr(L.output()))
L.print()
