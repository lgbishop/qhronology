from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 3, 3).as_mutable()
U3 = QuantumGate(spec=unitary, label="U", dim=3)
U3.diagram()
print(repr(U3.output()))
U3.print()
