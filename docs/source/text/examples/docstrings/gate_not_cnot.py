from qhronology.quantum.gates import *

CNOT = Not(targets=[1], controls=[0])
CNOT.diagram()
print(repr(CNOT.output()))
CNOT.print()
