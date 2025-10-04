from qhronology.quantum.states import QuantumState
from qhronology.quantum.circuits import QuantumCircuit

input_upper = QuantumState(spec=[("a", [0]), ("b", [1])], form="vector", label="ψ")
input_lower = QuantumState(spec=[("c", [0]), ("d", [1])], form="vector", label="φ")
bipartite_inputs = QuantumCircuit(inputs=[input_upper, input_lower])

input_both = bipartite_inputs.input(merge=False)
input_both.diagram()
