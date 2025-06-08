from qhronology.quantum.gates import *

S3 = Swap(targets=[0, 1], dim=3)
S3.diagram()
print(repr(S3.output()))
S3.print()
