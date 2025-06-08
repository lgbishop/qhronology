from qhronology.quantum.states import QuantumState

custom_matrix = QuantumState(spec=[["w", "x"], ["y", "z"]], kind="mixed", label="ω")
custom_matrix.diagram()
print(repr(custom_matrix.output()))
custom_matrix.print()
