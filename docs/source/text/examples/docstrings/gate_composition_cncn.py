from qhronology.quantum.gates import *

CNII = Not(targets=[1], controls=[0], num_systems=4)
IINC = Not(targets=[2], controls=[3], num_systems=4)
CNNC = GateInterleave(CNII, IINC)
CNNC.diagram()
print(repr(CNNC.output()))
CNNC.print()
