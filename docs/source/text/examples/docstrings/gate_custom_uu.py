from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 4, 4).as_mutable()
UU = QuantumGate(spec=unitary, targets=[0, 1], num_systems=2, label="U")
UU.diagram()
print(repr(UU.output()))
UU.print()
