from qhronology.quantum.gates import Pauli
from qhronology.quantum.circuits import QuantumCircuit

X = Pauli(index=1)
Y = Pauli(index=2)
Z = Pauli(index=3)
pauli_sequence = QuantumCircuit(gates=[X, Y, Z])
pauli_sequence.diagram()
