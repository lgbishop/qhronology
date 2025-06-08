from qhronology.quantum.gates import *
from qhronology.mechanics.matrices import ket

plus = (ket(0) + ket(1)) / sp.sqrt(2)
minus = (ket(0) - ket(1)) / sp.sqrt(2)
M_pm = Measurement(
    operators=[plus, minus], observable=False, targets=[1], num_systems=2
)
M_pm.diagram()
print(repr(M_pm.output()))
M_pm.print()
