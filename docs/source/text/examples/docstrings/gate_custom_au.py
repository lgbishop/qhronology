from qhronology.quantum.gates import *

unitary = sp.MatrixSymbol("U", 2, 2).as_mutable()
AU = QuantumGate(spec=unitary, targets=[1], anticontrols=[0], label="U")
AU.diagram()
print(repr(AU.output()))
AU.print()
