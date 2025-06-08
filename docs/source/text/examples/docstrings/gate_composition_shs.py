from qhronology.quantum.gates import *

SIS = Swap(targets=[0, 2], num_systems=3)
IHI = Hadamard(targets=[1], num_systems=3)
SHS = GateInterleave(SIS, IHI)
SHS.diagram(sep=(1, 2))
print(repr(SHS.output()))
SHS.print()
