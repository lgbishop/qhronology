from qhronology.quantum.gates import *

RSWAP = Swap(targets=[0, 1], exponent=sp.Rational(1, 2), label="√SWAP", family="GATE")
RSWAP.diagram()
print(repr(RSWAP.output()))
RSWAP.print()
