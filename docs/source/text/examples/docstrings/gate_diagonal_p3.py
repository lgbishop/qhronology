from qhronology.quantum.gates import *

D3 = Diagonal(
    entries={0: "a", 1: "b", 2: "c"},
    exponentiation=False,
    symbols={"a": {"real": True}, "b": {"real": True}, "c": {"real": True}},
    dim=3,
)
D3.diagram()
print(repr(D3.output()))
D3.print()
