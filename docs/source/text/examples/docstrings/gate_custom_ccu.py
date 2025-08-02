from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
CCU = QuantumGate(spec=unitary, targets=[2], controls=[0, 1], label="U")
CCU.diagram()
print(repr(CCU.output()))
CCU.print()
