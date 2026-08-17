from qhronology.quantum.gates import *

CNOT = Not(targets=[2], controls=[0])
CNOT.diagram(sep=(2, 1))
