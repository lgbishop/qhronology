from qhronology.quantum.gates import *

dim = 2
unitary = sp.eye(dim)
I = QuantumGate(spec=unitary, dim=dim, label="I")
I.diagram()
print(repr(I.output()))
I.print()
