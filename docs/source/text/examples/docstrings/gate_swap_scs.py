from qhronology.quantum.gates import *

SCS = Swap(targets=[0, 2], controls=[1])
SCS.diagram()
print(repr(SCS.output()))
SCS.print()
