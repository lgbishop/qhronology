from qhronology.quantum.gates import *

CSWAP = Swap(targets=[1, 2], controls=[0])
CSWAP.diagram()
print(repr(CSWAP.output()))
CSWAP.print()
