from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import QuantumGate
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp
from sympy.physics.quantum.dagger import Dagger

iterations = 1
dimensionality = 2

# Input
rho = sp.MatrixSymbol("ρ", dimensionality, dimensionality).as_mutable()
respecting_state = MixedState(
    spec=rho, dim=dimensionality, conditions=[(sp.trace(rho), 1)], label="ρ"
)
seed_state = MixedState(
    spec=sp.eye(dimensionality), dim=dimensionality, norm=1, label="τ_0"
)

# Gate
unitary = sp.MatrixSymbol("U", dimensionality**2, dimensionality**2).as_mutable()
U = QuantumGate(spec=unitary, targets=[0, 1], num_systems=2, dim=dimensionality)

# Construct conditions
conditions_respecting = [(sp.trace(rho), 1)]
conditions_unitary = [
    ((unitary * Dagger(unitary))[n], (sp.eye(dimensionality**2))[n])
    for n in range(0, len(unitary))
]
conditions = conditions_respecting + conditions_unitary

# Circuit
violating_state = seed_state
for n in range(1, iterations + 1):
    iteration = QuantumCircuit(
        inputs=[respecting_state, violating_state],
        gates=[U],
        conditions=conditions,
        traces=[0],
    )
    iteration.diagram(pad=(1, 0), sep=(0, 1), style="unicode")
    violating_state = iteration.state(label=f"τ_{n}")

# Output
final_state = violating_state

# Results
seed_state.print()
