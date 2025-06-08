from qhronology.quantum.gates import *

D = Diagonal(entries={0: "u", 1: "v"}, exponentiation=False)
D.diagram()
print(repr(D.output()))
D.print()
