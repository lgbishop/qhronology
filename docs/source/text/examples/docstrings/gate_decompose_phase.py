from qhronology.quantum.gates import *

n = 5
phase_power = Phase(phase="w", exponent=n, label=f"P^{n}")
phase_power.diagram()
