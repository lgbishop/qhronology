from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp

# Input
rho = sp.MatrixSymbol("ρ", 2, 2).as_mutable()
input_state = MixedState(
    spec=rho,
    conditions=[(rho[1, 1], 1 - rho[0, 0])],  # For normalization
    label="ρ",
)

# Gate
CN = Not(targets=[0], controls=[1], num_systems=2)

# CTC
CNOT = QuantumCircuit(
    inputs=[input_state],
    gates=[CN],
)
CNOT = QuantumCTC(circuit=CNOT, systems_respecting=[1])
CNOT.diagram()

# Output
# D-CTCs
CNOT_DCTC = DCTC(circuit=CNOT)
CNOT_DCTC_CR = CNOT_DCTC.state_respecting(label="ρ_D")
CNOT_DCTC_CV = CNOT_DCTC.state_violating(label="τ_D")
CNOT_DCTC_CR.conditions = [(1 - rho[0, 0], rho[1, 1])]

# P-CTCs
CNOT_PCTC = PCTC(circuit=CNOT)
CNOT_PCTC_CR = CNOT_PCTC.state_respecting(norm=1, label="ρ_P")
CNOT_PCTC_CV = CNOT_PCTC.state_violating(label="τ_P")

# Results
CNOT_DCTC_CR.print()
CNOT_DCTC_CV.print()
CNOT_PCTC_CR.print()
CNOT_PCTC_CV.print()