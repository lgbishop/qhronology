from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Rotation, Hadamard, Not, Pauli
from qhronology.quantum.circuits import QuantumCircuit

# Input
zero_state = VectorState(spec=[(1, [0])], label="0")

# Gates
RII = Rotation(axis=2, angle="2*acos(1/sqrt(3))", targets=[0], num_systems=3, label="R")
CHI = Hadamard(targets=[1], controls=[0], num_systems=3)
ICN = Not(targets=[2], controls=[1], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
XII = Pauli(index=1, targets=[0], num_systems=3)

# Circuit
generator = QuantumCircuit(
    inputs=[zero_state, zero_state, zero_state], gates=[RII, CHI, ICN, CNI, XII]
)
generator.diagram()

# Output
w_state = generator.state(label="W")

# Results
w_state.print()
