from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit

import sympy as sp

# Input
augend_state = VectorState(
    spec=[("a", [0]), ("b", [1])],
    substitutions=[("a*conjugate(a) + b*conjugate(b)", 1)],
    label="x",
)
addend_state = VectorState(
    spec=[("u", [0]), ("v", [1])],
    substitutions=[("u*conjugate(u) + v*conjugate(v)", 1)],
    label="y",
)
carry_input_state = VectorState(spec=[(1, [1])], label="c")
zero_state = VectorState(spec=[(1, [0])], label="0")

# Gates
CCIN = Not(targets=[3], controls=[0, 1], num_systems=4)
CNII = Not(targets=[1], controls=[0], num_systems=4)
ICCN = Not(targets=[3], controls=[1, 2], num_systems=4)
ICNI = Not(targets=[2], controls=[1], num_systems=4)

# Circuit
adder = QuantumCircuit(
    inputs=[augend_state, addend_state, carry_input_state, zero_state],
    gates=[CCIN, CNII, ICCN, ICNI, CNII],
)
adder.diagram()

# Output
sum_state = adder.state(label="s", traces=[0, 1, 3])
carry_output_state = adder.state(label="c′", traces=[0, 1, 2])
carry_output_state.apply(sp.collect, arguments={"syms": ["b*conjugate(b)"]})

# Results
augend_state.print()
addend_state.print()
carry_input_state.print()
sum_state.print()
carry_output_state.print(simplification=True)
