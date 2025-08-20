from qhronology.quantum.states import QuantumState

qubit_mixed = QuantumState(
    spec=[("p", [0]), ("1 - p", [1])],
    form="matrix",
    kind="mixed",
    symbols={"p": {"real": True, "nonnegative": True}},
    norm=1,
    label="τ",
)
qubit_mixed.diagram()
print(repr(qubit_mixed.output()))
qubit_mixed.print()
