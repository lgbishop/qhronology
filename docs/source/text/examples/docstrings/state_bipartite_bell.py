from qhronology.quantum.states import QuantumState

bell_state = QuantumState(
    spec=[(1, [0, 0]), (1, [1, 1])], form="vector", norm=1, label="Φ"
)
bell_state.diagram()
print(repr(bell_state.output()))
bell_state.print()
