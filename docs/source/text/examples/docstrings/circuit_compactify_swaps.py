from qhronology.quantum.gates import Swap
from qhronology.quantum.circuits import QuantumCircuit

def indices(num_systems, num_gates, separation, include_edges):
    count = 0
    number = 0
    while count < num_gates:
        index = ((separation + 2) * number) % num_systems
        if (index + 1) % num_systems != 0 or include_edges is True:
            yield index
            count += 1
        number += 1

num_systems = 7
num_gates = 18
separation = 0
include_edges = False

gates = [
    Swap(targets=[i % num_systems, (i + 1) % num_systems])
    for i in indices(num_systems, num_gates, separation, include_edges)
]

circuit = QuantumCircuit(
    gates=gates,
)
circuit.diagram(sep=(2, 1), force_separation=True, visible={"gates"})
circuit.compactify()
circuit.diagram(sep=(2, 1), force_separation=True, visible={"gates"})