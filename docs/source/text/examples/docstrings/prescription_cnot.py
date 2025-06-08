from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp

# Input
rho = sp.MatrixSymbol("ρ", 2, 2).as_mutable()
input_state = MixedState(spec=rho, conditions=[(rho[1, 1], 1 - rho[0, 0])], label="ρ")

# Gate
CN = Not(targets=[0], controls=[1], num_systems=2)

# CTC
CNOT = QuantumCircuit(inputs=[input_state], gates=[CN])
CNOT = QuantumCTC(circuit=CNOT, systems_respecting=[1])
CNOT.diagram()

# Output
# D-CTCs
CNOT_DCTC = DCTC(circuit=CNOT)
CNOT_DCTC_respecting = CNOT_DCTC.state_respecting(norm=False, label="ρ_D")
CNOT_DCTC_violating = CNOT_DCTC.state_violating(norm=False, label="τ_D")
CNOT_DCTC_respecting.conditions = [(1 - rho[0, 0], rho[1, 1])]

# P-CTCs
CNOT_PCTC = PCTC(circuit=CNOT)
CNOT_PCTC_respecting = CNOT_PCTC.state_respecting(norm=True, label="ρ_P")
CNOT_PCTC_violating = CNOT_PCTC.state_violating(norm=False, label="τ_P")

# Results
CNOT_DCTC_respecting.print()
CNOT_DCTC_violating.print()
CNOT_PCTC_respecting.print()
CNOT_PCTC_violating.print()
