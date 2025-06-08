from qhronology.quantum.gates import *

S = Phase(exponent=sp.Rational(1, 2), label="S")
S.diagram()
print(repr(S.output()))
S.print()
