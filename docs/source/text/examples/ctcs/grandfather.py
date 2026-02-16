from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import Not, Swap
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp

# Input
rho = sp.MatrixSymbol("ρ", 2, 2).as_mutable()
input_state = MixedState(
    spec=rho,
    conditions=[(rho[0, 0], 1 - rho[1, 1])],
    label="ρ",
)

# Gates
NC = Not(targets=[0], controls=[1], num_systems=2)
S = Swap(targets=[0, 1], num_systems=2)

# CTC
grandfather = QuantumCTC(
    inputs=[input_state],
    gates=[NC, S],
    systems_respecting=[0],
)
grandfather.diagram()

# Output
# D-CTCs
grandfather_DCTC = DCTC(circuit=grandfather)
grandfather_DCTC_CR = grandfather_DCTC.state_respecting(label="ρ_D")
grandfather_DCTC_CV = grandfather_DCTC.state_violating(label="τ_D")
grandfather_DCTC_CR.apply(sp.factor)

# P-CTCs
grandfather_PCTC = PCTC(circuit=grandfather)
grandfather_PCTC_CR = grandfather_PCTC.state_respecting(label="ρ_P")
grandfather_PCTC_CV = grandfather_PCTC.state_violating(label="τ_P")
grandfather_PCTC_CR.normalize()
grandfather_PCTC_CR.simplify()

# Results
grandfather_DCTC_CR.print()
grandfather_DCTC_CV.print()
grandfather_PCTC_CR.print()
grandfather_PCTC_CV.print()
