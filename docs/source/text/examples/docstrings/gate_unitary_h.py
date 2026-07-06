from qhronology.quantum.gates import *

H = Unitary(parameters=(sp.pi/2, 0, sp.pi), label="H")
H.diagram()
print(repr(H.output()))
H.print()
