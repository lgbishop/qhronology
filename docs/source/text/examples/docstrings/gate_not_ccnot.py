from qhronology.quantum.gates import *

CCNOT = Not(targets=[2], controls=[0, 1])
CCNOT.diagram()
print(repr(CCNOT.output()))
CCNOT.print()
