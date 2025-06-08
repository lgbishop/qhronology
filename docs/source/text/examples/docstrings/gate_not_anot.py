from qhronology.quantum.gates import *

ANOT = Not(targets=[1], anticontrols=[0])
ANOT.diagram()
print(repr(ANOT.output()))
ANOT.print()
