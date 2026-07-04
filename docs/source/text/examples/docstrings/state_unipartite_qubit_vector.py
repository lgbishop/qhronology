from qhronology.quantum.states import QuantumState

qubit_vector = QuantumState(
    spec=[("a", [0]), ("b", [1])],
    form="vector",
    symbols={"a": {"complex": True}, "b": {"complex": True}},
    substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    norm=1,
    label="ψ",
)
qubit_vector.diagram()
print(repr(qubit_vector.output(simplify=True)))
qubit_vector.print(simplify=True)
