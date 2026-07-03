from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import Swap, Pauli
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp

# Input
rho = sp.MatrixSymbol("ρ", 2, 2).as_mutable()
input_state = MixedState(
    spec=rho,
    conditions=[(rho[0, 0] + rho[1, 1], 1)],  # For normalization
    label="ρ",
    norm=1,
)

# Gate
S = Swap(targets=[0, 1], num_systems=2)
I = Pauli(index=0, targets=[0, 1], num_systems=2)

# CTC
SWAP_CTC = QuantumCTC(
    inputs=[input_state],
    gates=[S],
    systems_respecting=[0],
)
SWAP_CTC.diagram()

# Output
# D-CTCs
SWAP_DCTC = DCTC(circuit=SWAP_CTC)
SWAP_DCTC_CR = SWAP_DCTC.state_respecting(simplify=True, label="ρ_D")
SWAP_DCTC_CV = SWAP_DCTC.state_violating(simplify=True, label="τ_D")

# P-CTCs
SWAP_PCTC = PCTC(circuit=SWAP_CTC)
SWAP_PCTC_CR = SWAP_PCTC.state_respecting(simplify=True, label="ρ_P")
SWAP_PCTC_CV = SWAP_PCTC.state_violating(simplify=True, label="τ_P")

# Results
SWAP_DCTC_CR.print()
SWAP_DCTC_CV.print()
SWAP_PCTC_CR.print()
SWAP_PCTC_CV.print()
