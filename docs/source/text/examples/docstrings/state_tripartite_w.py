from qhronology.quantum.states import QuantumState

w_state = QuantumState(
    spec=[(1, [0, 0, 1]), (1, [0, 1, 0]), (1, [1, 0, 0])],
    form="vector",
    norm=1,
    label="W",
)
w_state.diagram()
print(repr(w_state.output()))
print(repr(w_state.output(numerical=True, array=True)))
w_state.print()
