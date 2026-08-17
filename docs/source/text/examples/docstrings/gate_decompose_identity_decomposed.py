from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

phased_identity = Pauli(index=0, coefficient=-sp.I, label="-iI")
decomposition = phased_identity.decompose(
    gates=[Pauli(index=1), Pauli(index=2), Pauli(index=3)]
)[0]
QuantumCircuit(gates=decomposition).diagram(pad=(1, 0), uniform_spacing=True, visible={"gates"})
