from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import QuantumGate, Swap, Diagonal
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp
from sympy.physics.quantum import TensorProduct

# Input
clock_state_unevolved = VectorState(spec=[[0, 1, 1]], dim=3, norm=1, label="ψ")
clock_state_evolved = VectorState(spec=[[0, 1, -1]], dim=3, norm=1, label="ψ")

# Gates
I = QuantumGate(
    spec=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], targets=[0], num_systems=1, dim=3
)
zero = QuantumGate(
    spec=[[1, 0, 0], [0, 0, 0], [0, 0, 0]], targets=[0], num_systems=1, dim=3
)
S = Swap(targets=[0, 1], num_systems=2, dim=3)
IR = Diagonal(
    entries={2: "-pi*t"},
    exponentiation=True,
    symbols={"t": {"real": True, "positive": True}},
    targets=[1],
    num_systems=2,
    dim=3,
    label="R",
)

# Construct SWAP gate in clock subspace
S = sp.Matrix(9, 9, lambda i, j: 0 if i % 3 == 0 or j % 3 == 0 else S.matrix[i, j])

# Construct vacuum-excluding SWAP gate
S_vacuum = QuantumGate(
    spec=(
        TensorProduct(I.matrix, zero.matrix)
        + TensorProduct(zero.matrix, I.matrix)
        - TensorProduct(zero.matrix, zero.matrix)
        + S
    ),
    targets=[0, 1],
    num_systems=2,
    dim=3,
    family="SWAP",
)

# CTC
billiards = QuantumCTC(
    inputs=[clock_state_unevolved], gates=[S_vacuum, IR], systems_respecting=[0]
)
billiards.diagram()

# Output
# D-CTCs
billiards_DCTC = DCTC(circuit=billiards)
billiards_DCTC_respecting = billiards_DCTC.state_respecting(norm=False, label="ρ_D")
billiards_DCTC_violating = billiards_DCTC.state_violating(norm=False, label="τ_D")
billiards_DCTC_respecting.simplify()
billiards_DCTC_respecting.apply(sp.factor)

# P-CTCs
billiards_PCTC = PCTC(circuit=billiards)
billiards_PCTC_respecting = billiards_PCTC.state_respecting(norm=False, label="ψ_P")
billiards_PCTC_violating = billiards_PCTC.state_violating(norm=False, label="τ_P")
billiards_PCTC_respecting.normalize(1)

# Results
billiards_DCTC_respecting.print()
billiards_DCTC_violating.print()
billiards_PCTC_respecting.print()
billiards_PCTC_violating.print()
