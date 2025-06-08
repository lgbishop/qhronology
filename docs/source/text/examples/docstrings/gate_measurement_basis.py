from qhronology.quantum.gates import *

basis_vectors = [ket(i) for i in [0, 1]]
M_basis = Measurement(operators=basis_vectors, observable=False)
M_basis.diagram()
print(repr(M_basis.output()))
M_basis.print()
