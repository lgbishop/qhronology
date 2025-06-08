from qhronology.quantum.gates import *

HH = Hadamard(targets=[0, 1], label="H⊗H")
HH.diagram()
print(repr(HH.output()))
HH.print()
