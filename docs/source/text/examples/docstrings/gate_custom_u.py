from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
U = QuantumGate(spec=unitary, label="U")
U.diagram()
print(repr(U.output()))
U.print()
