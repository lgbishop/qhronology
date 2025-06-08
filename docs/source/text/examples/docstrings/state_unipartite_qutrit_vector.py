from qhronology.quantum.states import QuantumState

qutrit_vector = QuantumState(
    spec=[("a", [0]), ("b", [1]), ("c", [2])],
    form="vector",
    dim=3,
    symbols={"a": {"complex": True}, "b": {"complex": True}, "c": {"complex": True}},
    conditions=[("a*conjugate(a) + b*conjugate(b) + c*conjugate(c)", "1")],
    norm=1,
    label="φ",
)
qutrit_vector.diagram()
print(repr(qutrit_vector.output()))
qutrit_vector.print()
