from qhronology.quantum.states import QuantumState

custom_vector = QuantumState(spec=[["μ"], ["ν"]], kind="mixed", label="η")
custom_vector.diagram()
print(repr(custom_vector.output()))
custom_vector.print()
