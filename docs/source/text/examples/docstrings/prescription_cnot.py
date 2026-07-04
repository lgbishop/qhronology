from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp

# Input
rho = sp.MatrixSymbol("ρ", 2, 2).as_mutable()
input_state = MixedState(
    spec=rho,
    substitutions=[(rho[0, 0] + rho[1, 1], 1)],  # For normalization
    label="ρ",
    norm=1,
)
input_state.simplify()

# Gate
CN = Not(targets=[0], controls=[1], num_systems=2)

# CTC
CNOT = QuantumCircuit(
    inputs=[input_state],
    gates=[CN],
)
CNOT_CTC = QuantumCTC(circuit=CNOT, systems_respecting=[1])
CNOT_CTC.diagram()

# Output
# D-CTCs
CNOT_DCTC = DCTC(circuit=CNOT_CTC)
CNOT_DCTC_CR = CNOT_DCTC.state_respecting(simplify=True, label="ρ_D")
CNOT_DCTC_CV = CNOT_DCTC.state_violating(simplify=True, label="τ_D")

# P-CTCs
CNOT_PCTC = PCTC(circuit=CNOT_CTC)
CNOT_PCTC_CR = CNOT_PCTC.state_respecting(simplify=True, norm=1, label="ρ_P")
CNOT_PCTC_CV = CNOT_PCTC.state_violating(simplify=True, label="τ_P")

# Results
CNOT_DCTC_CR.print()
CNOT_DCTC_CV.print()
CNOT_PCTC_CR.print()
CNOT_PCTC_CV.print()