from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
CU = QuantumGate(spec=unitary, targets=[1], controls=[0], label="U")
CU.diagram()
print(repr(CU.output()))
CU.print()
