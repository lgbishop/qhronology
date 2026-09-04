from qhronology.quantum.gates import *

S = Pauli(index=3, exponent=sp.Rational(1, 2), label="S")
S.diagram()
print(repr(S.output()))
S.print()