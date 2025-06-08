from qhronology.quantum.states import QuantumState

tripartite_zero = QuantumState(spec=[(1, [0, 0, 0])], form="vector", label="0,0,0")
tripartite_zero.diagram()
print(repr(tripartite_zero.output()))
tripartite_zero.print()
