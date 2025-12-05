from qhronology.quantum.gates import *

RNOT = Not(targets=[0], exponent=sp.Rational(1, 2), label="√NOT", family="GATE")
RNOT.diagram()
print(repr(RNOT.output()))
RNOT.print()
