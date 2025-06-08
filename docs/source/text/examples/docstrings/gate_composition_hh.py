from qhronology.quantum.gates import *

HI = Hadamard(targets=[0], num_systems=2)
IH = Hadamard(targets=[1], num_systems=2)
HH = GateInterleave(HI, IH, merge=True)
HH.diagram(sep=(1, 2))
print(repr(HH.output()))
HH.print()
