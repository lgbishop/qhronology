from qhronology.quantum.gates import *

R_z = Rotation(axis=3, angle="t", label="R_z")
R_z.diagram()
print(repr(R_z.output()))
R_z.print()
