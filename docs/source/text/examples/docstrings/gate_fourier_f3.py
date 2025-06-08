from qhronology.quantum.gates import *

F3 = Fourier(dim=3)
F3.diagram()
print(repr(F3.output()))
F3.print()
