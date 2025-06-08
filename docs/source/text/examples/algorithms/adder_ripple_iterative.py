from qhronology.quantum.states import QuantumState, VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.matrices import encode, decode

import sympy as sp
from sympy.physics.quantum import TensorProduct

import time

initial_time = time.time()

augend_integer = 31
addend_integer = 217
encoding_depth = 8

# Input
augend_state = VectorState(
    spec=encode(integer=augend_integer, num_systems=encoding_depth), label="x_i"
)
addend_state = VectorState(
    spec=encode(integer=addend_integer, num_systems=encoding_depth), label="y_i"
)
carry_state = VectorState(spec=encode(0, 1), label="c_i")
zero_state = VectorState(spec=encode(0, 1), notation="0")

# Gates
CCIN = Not(targets=[3], controls=[0, 1], num_systems=4)
CNII = Not(targets=[1], controls=[0], num_systems=4)
ICCN = Not(targets=[3], controls=[1, 2], num_systems=4)
ICNI = Not(targets=[2], controls=[1], num_systems=4)

# Circuits
sum_qubits = []
for i in range(encoding_depth - 1, -1, -1):
    target_bit = i
    complement_bits = [n for n in range(0, encoding_depth) if n != target_bit]

    augend_state.reset()
    addend_state.reset()

    augend_state.partial_trace(complement_bits)
    addend_state.partial_trace(complement_bits)

    adder = QuantumCircuit(
        inputs=[augend_state, addend_state, carry_state, zero_state],
        gates=[CCIN, CNII, ICCN, ICNI, CNII],
    )

    sum_qubit = adder.state(label="s", traces=[0, 1, 3])
    carry_state = adder.state(label="c_i", traces=[0, 1, 2])
    sum_qubits = [sum_qubit.output()] + sum_qubits

adder.diagram()

# Output
sum_state = QuantumState(spec=sp.Matrix(TensorProduct(*sum_qubits)), label="s")
sum_integer = decode(sum_state.output())
sum_state = VectorState(spec=encode(sum_integer), label="s")

augend_state.reset()
addend_state.reset()

augend_state.label = "x"
addend_state.label = "y"

# Results
augend_state.print()
addend_state.print()
sum_state.print()

final_time = time.time()
computation = f"Computation: {augend_integer} + {addend_integer} = {sum_integer}"
duration = f"Duration: {sp.N(final_time - initial_time,8).round(3)} seconds"
print(computation)
print(duration)
