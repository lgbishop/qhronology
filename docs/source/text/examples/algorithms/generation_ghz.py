from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Not
from qhronology.quantum.circuits import QuantumCircuit

# Input
zero_state = VectorState(spec=[(1, [0])], label="0")

# Gates
HII = Hadamard(targets=[0], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
ICN = Not(targets=[2], controls=[1], num_systems=3)

# Circuit
generator = QuantumCircuit(
    inputs=[zero_state, zero_state, zero_state], gates=[HII, CNI, ICN]
)
generator.diagram()

# Output
ghz_state = generator.state(label="GHZ")

# Results
ghz_state.print()
