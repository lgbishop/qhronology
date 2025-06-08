from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Rotation, Diagonal
from qhronology.quantum.circuits import QuantumCircuit

# Input
zero_state = VectorState(spec=[(1, [0])], label="0")

# Gates
R = Rotation(axis=1, angle="2*θ", symbols={"θ": {"real": True}}, label="R(2θ)")
P = Diagonal(
    entries={1: "φ + pi/2"},
    exponentiation=True,
    symbols={"φ": {"real": True}},
    label="P(φ + π/2)",
)

# Circuit
generator = QuantumCircuit(inputs=[zero_state], gates=[R, P])
generator.diagram(pad=(0, 0), sep=(1, 1), style="unicode")

# Output
arbitrary_state = generator.state(label="ψ")
arbitrary_state.simplify()

# Results
arbitrary_state.print()
