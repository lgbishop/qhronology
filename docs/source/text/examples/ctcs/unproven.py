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
    systems_violating=[2],
)
unproven.diagram()

# Output
# D-CTCs
unproven_DCTC = DCTC(circuit=unproven)
unproven_DCTC_CR = unproven_DCTC.state_respecting(label="ρ_D")
unproven_DCTC_CV = unproven_DCTC.state_violating(label="τ_D")

# P-CTCs
unproven_PCTC = PCTC(circuit=unproven)
unproven_PCTC_CR = unproven_PCTC.state_respecting(label="ψ_P")
unproven_PCTC_CV = unproven_PCTC.state_violating(label="τ_P")
unproven_PCTC_CR.normalize()

# Results
unproven_DCTC_CR.print()
unproven_DCTC_CV.print()
unproven_PCTC_CR.print()
unproven_PCTC_CV.print()
