from qhronology.quantum.gates import *

RNOT = Not(targets=[0], exponent=sp.Rational(1, 2))
RNOT.diagram()
print(repr(RNOT.output()))
RNOT.print()
