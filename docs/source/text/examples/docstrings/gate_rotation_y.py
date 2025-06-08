from qhronology.quantum.gates import *

R_y = Rotation(axis=2, angle="φ", label="R_y")
R_y.diagram()
print(repr(R_y.output()))
R_y.print()
