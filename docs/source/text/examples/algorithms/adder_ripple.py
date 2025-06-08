from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.utilities.helpers import flatten_list
from qhronology.mechanics.matrices import encode, decode, decode_fast

import sympy as sp

import time

initial_time = time.time()

augend_integer = 1
addend_integer = 1
encoding_depth = 2

# Input
augend_state = VectorState(
    spec=encode(integer=augend_integer, num_systems=encoding_depth), label="x"
)
addend_state = VectorState(
    spec=encode(integer=addend_integer, num_systems=encoding_depth), label="y"
)

augend_states = []
addend_states = []
carry_states = []
zero_states = []
for i in range(0, encoding_depth):
    target_bit = i
    complement_bits = [n for n in range(0, encoding_depth) if n != target_bit]

    augend_state.partial_trace(complement_bits)
    addend_state.partial_trace(complement_bits)

    augend_bit = decode(augend_state.output())
    addend_bit = decode(addend_state.output())

    augend_bit_state = VectorState(
        spec=encode(augend_bit, 1),
        label=augend_state.label + str(encoding_depth - 1 - i),
    )
    addend_bit_state = VectorState(
        spec=encode(addend_bit, 1),
        label=addend_state.label + str(encoding_depth - 1 - i),
    )
    carry_state = VectorState(
        spec=encode(0, 1), label="c" + str(encoding_depth - 1 - i)
    )
    zero_state = VectorState(spec=encode(0, 1), label="0")

    augend_states.append(augend_bit_state)
    addend_states.append(addend_bit_state)
    carry_states.append(carry_state)
    zero_states.append(zero_state)

    augend_state.reset()
    addend_state.reset()

input_spec = flatten_list(
    [
        [augend_states[i], addend_states[i], carry_states[i], zero_states[i]]
        for i in range(0, encoding_depth)
    ]
)

# Gates
gates = []
for i in range(0, encoding_depth):
    system_shift = 4 * (encoding_depth - 1 - i)

    CCIN = Not(
        targets=[system_shift + 3],
        controls=[system_shift + 0, system_shift + 1],
        num_systems=4 * encoding_depth,
    )
    CNII = Not(
        targets=[system_shift + 1],
        controls=[system_shift + 0],
        num_systems=4 * encoding_depth,
    )
    ICCN = Not(
        targets=[system_shift + 3],
        controls=[system_shift + 1, system_shift + 2],
        num_systems=4 * encoding_depth,
    )
    ICNI = Not(
        targets=[system_shift + 2],
        controls=[system_shift + 1],
        num_systems=4 * encoding_depth,
    )

    adder_single = [CCIN, CNII, ICCN, ICNI, CNII]
    gates.append(adder_single)

    if i != max(range(0, encoding_depth)):
        CNOT = Not(
            targets=[system_shift - 2],
            controls=[system_shift + 3],
            num_systems=4 * encoding_depth,
        )
        adder_single.append(CNOT)

gates = flatten_list(gates)

# Circuit
adder = QuantumCircuit(inputs=input_spec, gates=gates)
adder.diagram()

# Output
sum_registers = [2 + i * 4 for i in range(0, encoding_depth)]
not_sum_registers = [i for i in range(0, 4 * encoding_depth) if i not in sum_registers]
sum_state = adder.state(label="s", traces=not_sum_registers)
sum_integer = decode_fast(sum_state.output())
sum_state = VectorState(spec=encode(sum_integer), label="s")

# Results
augend_state.print()
addend_state.print()
sum_state.print()

final_time = time.time()
computation = f"Computation: {augend_integer} + {addend_integer} = {sum_integer}"
duration = f"Duration: {sp.N(final_time - initial_time,8).round(3)} seconds"
print(computation)
print(duration)
