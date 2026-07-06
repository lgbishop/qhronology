from qhronology.quantum.gates import *

U = Unitary(parameters=("θ", "φ", "λ"))
U.diagram()
print(repr(U.output()))
U.print()
