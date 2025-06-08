from qhronology.quantum.gates import *

N = Not(targets=[0])
N.diagram()
print(repr(N.output()))
N.print()
