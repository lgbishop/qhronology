from qhronology.quantum.gates import *

I = Unitary(parameters=(0, 0, 0), label="I")
I.diagram()
print(repr(I.output()))
I.print()
