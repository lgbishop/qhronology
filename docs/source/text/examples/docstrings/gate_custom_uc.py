from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
UC = QuantumGate(spec=unitary, targets=[0], controls=[1], label="U")
UC.diagram()
print(repr(UC.output()))
UC.print()
