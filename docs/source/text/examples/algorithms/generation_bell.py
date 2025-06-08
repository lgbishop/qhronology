from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
zero_state = VectorState(spec=[(1, [0])], label="0")

# Gates
HI = Hadamard(targets=[0], num_systems=2)
CN = Not(targets=[1], controls=[0], num_systems=2)

# Circuit
generator = QuantumCircuit(inputs=[zero_state, zero_state], gates=[HI, CN])
generator.diagram()

# Output
phi_plus = generator.state(label="Φ+")

# Results
phi_plus.print()
