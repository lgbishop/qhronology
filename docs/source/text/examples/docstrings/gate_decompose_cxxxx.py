from qhronology.quantum.gates import *

n = 4
CXXXX = Not(targets=list(range(1, n + 1)), controls=[0])
CXXXX.diagram(sep=(2, 1))
