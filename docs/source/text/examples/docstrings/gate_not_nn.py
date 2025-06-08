from qhronology.quantum.gates import *

NN = Not(targets=[0, 1])
NN.diagram()
print(repr(NN.output()))
NN.print()
