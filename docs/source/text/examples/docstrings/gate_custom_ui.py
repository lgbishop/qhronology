from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
UI = QuantumGate(spec=unitary, targets=[0], num_systems=2, label="U")
UI.diagram()
print(repr(UI.output()))
UI.print()
