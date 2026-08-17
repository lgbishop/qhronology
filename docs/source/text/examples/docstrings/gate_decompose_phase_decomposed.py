from qhronology.quantum.gates import *
from qhronology.quantum.circuits import *

n = 5
phase_power = Phase(phase="w", exponent=n, label=f"P^{n}")
decomposition = phase_power.decompose(
    gates=[Phase(phase="w")],
    only_targets=False,
)[0]
QuantumCircuit(gates=decomposition).diagram(pad=(1, 0), uniform_spacing=True, visible={"gates"})
