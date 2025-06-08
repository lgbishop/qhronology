from qhronology.quantum.gates import *

T = Phase(exponent=sp.Rational(1, 4), label="T")
T.diagram()
print(repr(T.output()))
T.print()
