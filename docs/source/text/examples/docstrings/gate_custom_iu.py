from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
IU = QuantumGate(spec=unitary, targets=[1], num_systems=2, label="U")
IU.diagram()
print(repr(IU.output()))
IU.print()
