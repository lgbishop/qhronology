from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Summation
from qhronology.quantum.circuits import QuantumCircuit

num_systems = 4
dim = 4

# Input
zero_state = VectorState(spec=[(1, [0])], label="0", dim=dim)
input_states = [zero_state for i in range(0, num_systems)]

# Gates
HII = Hadamard(targets=[0], num_systems=num_systems, dim=dim)
CNOTs = [
    Summation(targets=[i + 1], controls=[i], num_systems=num_systems, dim=dim)
    for i in range(0, num_systems - 1)
]

gates = [HII] + CNOTs

# Circuit
generator = QuantumCircuit(inputs=input_states, gates=gates)
generator.diagram()

# Output
entangled_state = generator.state(label="GHZ")

# Results
entangled_state.print()
