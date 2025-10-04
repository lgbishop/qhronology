from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

CN = Not(targets=[1], controls=[0])
NC = Not(targets=[0], controls=[1])

swapcnots = QuantumCircuit(gates=[CN, NC, CN])
swapcnots.diagram(sep=(2, 1), force_separation=True)
