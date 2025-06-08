from qhronology.quantum.gates import *

SIS = Swap(targets=[0, 2])
SIS.diagram()
print(repr(SIS.output()))
SIS.print()
