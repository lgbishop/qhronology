from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

CN = Not(targets=[1], controls=[0])
NC = Not(targets=[0], controls=[1])

swapcnots = QuantumCircuit(gates=[CN, NC, CN])
SWAP = swapcnots.gate(label="S")
SWAP.diagram()
