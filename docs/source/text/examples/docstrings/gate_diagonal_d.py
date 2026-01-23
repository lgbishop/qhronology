from qhronology.quantum.gates import *

D = Diagonal(entries={0: "u", 1: "v"})
D.diagram()
print(repr(D.output()))
D.print()
