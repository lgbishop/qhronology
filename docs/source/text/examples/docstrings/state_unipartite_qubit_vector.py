from qhronology.quantum.states import QuantumState

qubit_vector = QuantumState(
    spec=[("a", [0]), ("b", [1])],
    form="vector",
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b)", "1")],
    norm=1,
    label="ψ",
)
qubit_vector.diagram()
print(repr(qubit_vector.output()))
qubit_vector.print()
