from qhronology.quantum.gates import *

SUM = Summation(shift=1)
SUM.diagram()
print(repr(SUM.output()))
SUM.print()
