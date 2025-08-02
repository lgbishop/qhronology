from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
AUC = QuantumGate(spec=unitary, targets=[1], controls=[2], anticontrols=[0], label="U")
AUC.diagram()
print(repr(AUC.output()))
AUC.print()
