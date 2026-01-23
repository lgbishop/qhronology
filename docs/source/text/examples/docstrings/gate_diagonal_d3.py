from qhronology.quantum.gates import *

D3 = Diagonal(
    entries={0: "a", 1: "b", 2: "c"},
    dim=3,
)
D3.diagram()
print(repr(D3.output()))
D3.print()
