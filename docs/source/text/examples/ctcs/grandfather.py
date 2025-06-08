from qhronology.quantum.states import MixedState
from qhronology.quantum.gates import Not, Swap
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

import sympy as sp

# Input
rho = sp.MatrixSymbol("ρ", 2, 2).as_mutable()
input_state = MixedState(spec=rho, conditions=[(rho[0, 0], 1 - rho[1, 1])], label="ρ")

# Gates
NC = Not(targets=[0], controls=[1], num_systems=2)
S = Swap(targets=[0, 1], num_systems=2)

# CTC
grandfather = QuantumCTC([input_state], gates=[NC, S], systems_respecting=[0])
grandfather.diagram()

# Output
# D-CTCs
grandfather_DCTC = DCTC(circuit=grandfather)
grandfather_DCTC_respecting = grandfather_DCTC.state_respecting(norm=False, label="ρ_D")
grandfather_DCTC_violating = grandfather_DCTC.state_violating(norm=False, label="τ_D")
grandfather_DCTC_respecting.apply(sp.factor)

# P-CTCs
grandfather_PCTC = PCTC(circuit=grandfather)
grandfather_PCTC_respecting = grandfather_PCTC.state_respecting(norm=1, label="ρ_P")
grandfather_PCTC_violating = grandfather_PCTC.state_violating(norm=1, label="τ_P")
grandfather_PCTC_respecting.coefficient("1/(sqrt(2))")  # Manually renormalize
grandfather_PCTC_respecting.simplify()
grandfather_PCTC_violating.simplify()

# Results
grandfather_DCTC_respecting.print()
grandfather_DCTC_violating.print()
grandfather_PCTC_respecting.print()
grandfather_PCTC_violating.print()
