from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not, Swap
from qhronology.quantum.prescriptions import QuantumCTC, DCTC, PCTC

# Input
mathematician_state = VectorState(spec=[(1, [0])], label="0")
book_state = VectorState(spec=[(1, [0])], label="0")

# Gates
NIC = Not(targets=[0], controls=[2], num_systems=3)
CNI = Not(targets=[1], controls=[0], num_systems=3)
IS = Swap(targets=[1, 2], num_systems=3)

# CTC
unproven = QuantumCTC(
    inputs=[mathematician_state, book_state],
    gates=[NIC, CNI, IS],
    systems_respecting=[0, 1],
)
unproven.diagram()

# Output
# D-CTCs
unproven_DCTC = DCTC(circuit=unproven)
unproven_DCTC_respecting = unproven_DCTC.state_respecting(norm=1, label="ρ_D")
unproven_DCTC_violating = unproven_DCTC.state_violating(norm=1, label="τ_D")

# P-CTCs
unproven_PCTC = PCTC(circuit=unproven)
unproven_PCTC_respecting = unproven_PCTC.state_respecting(norm=1, label="ψ_P")
unproven_PCTC_violating = unproven_PCTC.state_violating(norm=1, label="τ_P")

# Results
unproven_DCTC_respecting.print()
unproven_DCTC_violating.print()
unproven_PCTC_respecting.print()
unproven_PCTC_violating.print()
