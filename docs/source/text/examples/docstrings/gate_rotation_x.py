from qhronology.quantum.gates import *

R_x = Rotation(axis=1, angle="θ", label="R_x")
R_x.diagram()
print(repr(R_x.output()))
R_x.print()
