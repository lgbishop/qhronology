from qhronology.quantum.gates import *

P = Diagonal(
    entries={1: "p"}, exponentiation=True, symbols={"p": {"real": True}}, label="P"
)
P.diagram()
print(repr(P.output()))
P.print()
