from qhronology.quantum.gates import *

SUM3 = Summation(shift=1, dim=3)
SUM3.diagram()
print(repr(SUM3.output()))
SUM3.print()
