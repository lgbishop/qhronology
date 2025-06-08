from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import Swap, Pauli
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp

# Input
rho = sp.MatrixSymbol("ρ", 2, 2).as_mutable()
input_state = MixedState(
    spec=rho,
    conditions=[(rho[1, 1], 1 - rho[0, 0])],
    label="ρ",
)

# Gate
S = Swap(targets=[0, 1], num_systems=2)
I = Pauli(index=0, targets=[0, 1], num_systems=2)

# CTC
SWAP = QuantumCTC([input_state], [S], systems_respecting=[0])
SWAP.diagram()

# Output
# D-CTCs
SWAP_DCTC = DCTC(circuit=SWAP)
SWAP_DCTC_respecting = SWAP_DCTC.state_respecting(norm=False, label="ρ_D")
SWAP_DCTC_violating = SWAP_DCTC.state_violating(norm=False, label="τ_D")
SWAP_DCTC_respecting.conditions = [(1 - rho[0, 0], rho[1, 1])]
SWAP_DCTC_respecting.simplify()
SWAP_DCTC_violating.conditions = [(1 - rho[0, 0], rho[1, 1])]

# P-CTCs
SWAP_PCTC = PCTC(circuit=SWAP)
SWAP_PCTC_respecting = SWAP_PCTC.state_respecting(norm=False, label="ρ_P")
SWAP_PCTC_violating = SWAP_PCTC.state_violating(norm=False, label="τ_P")
SWAP_PCTC_respecting.conditions = [(1 - rho[0, 0], rho[1, 1])]
SWAP_PCTC_violating.conditions = [(1 - rho[0, 0], rho[1, 1])]

SWAP_PCTC_respecting.simplify()
SWAP_PCTC_violating.simplify()

# Results
SWAP_DCTC_respecting.print()
SWAP_DCTC_violating.print()
SWAP_PCTC_respecting.print()
SWAP_PCTC_violating.print()
