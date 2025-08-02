from qhronology.quantum.states import QuantumState

ghz_state = QuantumState(
    spec=[(1, [0, 0, 0]), (1, [1, 1, 1])],
    form="vector",
    norm=1,
    label="GHZ",
)
ghz_state.diagram()
print(repr(ghz_state.output()))
ghz_state.print()
