from qhronology.quantum.gates import *

CSWAP = Swap(targets=[0, 2], controls=[1])
CSWAP.diagram(sep=(2, 1))
