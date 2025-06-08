from qhronology.quantum.gates import *

pauli_matrices = [Pauli(index=i).output() for i in [1, 2, 3]]
M_pauli = Measurement(
    operators=pauli_matrices, observable=True, targets=[0], num_systems=2
)
M_pauli.diagram()
print(repr(M_pauli.output()))
M_pauli.print()
