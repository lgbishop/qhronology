from qhronology.quantum.states import QuantumState

qubit_pure = QuantumState(
    spec=[("α", [0]), ("β", [1])],
    form="matrix",
    kind="pure",
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("α*conjugate(α) + β*conjugate(β)", 1)],
    norm=1,
    label="ξ",
)
qubit_pure.diagram()
print(repr(qubit_pure.output()))
qubit_pure.print()
