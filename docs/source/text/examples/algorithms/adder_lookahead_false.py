from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Not
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.utilities.helpers import flatten_list
from qhronology.mechanics.matrices import encode, decode

import sympy as sp

import time

initial_time = time.time()

augend_integer = 1
addend_integer = 1
encoding_depth = 2
overflow_qubit = False

# Input
augend_state = VectorState(
    spec=encode(integer=augend_integer, num_systems=encoding_depth, reverse=True),
    label="x",
)
addend_state = VectorState(
    spec=encode(integer=addend_integer, num_systems=encoding_depth, reverse=True),
    label="y",
)
zero_state = []
if overflow_qubit is True:
    zero_state = VectorState(spec=encode(integer=0, num_systems=1), label="0")

augend_states = []
addend_states = []
carry_states = []
for i in range(0, encoding_depth):
    target_bit = i
    complement_bits = [n for n in range(0, encoding_depth) if n != target_bit]

    augend_state.partial_trace(complement_bits)
    addend_state.partial_trace(complement_bits)

    augend_bit = decode(augend_state.output())
    addend_bit = decode(addend_state.output())

    augend_bit_state = VectorState(
        spec=encode(integer=augend_bit, num_systems=1),
        label=augend_state.label + str(i),
    )
    addend_bit_state = VectorState(
        spec=encode(integer=addend_bit, num_systems=1),
        label=addend_state.label + str(i),
    )
    carry_state = VectorState(spec=encode(integer=0, num_systems=1), label="c" + str(i))

    augend_states.append(augend_bit_state)
    addend_states.append(addend_bit_state)
    carry_states.append(carry_state)

    augend_state.reset()
    addend_state.reset()

input_spec = flatten_list(
    [
        [carry_states[i], augend_states[i], addend_states[i]]
        for i in range(0, encoding_depth)
    ]
    + [zero_state]
)

# Gates

# Construct sequence of CARRY gates
carries = []
for i in range(0, encoding_depth - 1 + int(overflow_qubit)):
    system_shift = 3 * i

    ICCN = Not(
        targets=[system_shift + 3],
        controls=[system_shift + 1, system_shift + 2],
        num_systems=3 * encoding_depth + int(overflow_qubit),
    )
    ICNI = Not(
        targets=[system_shift + 2],
        controls=[system_shift + 1],
        num_systems=3 * encoding_depth + int(overflow_qubit),
    )
    CICN = Not(
        targets=[system_shift + 3],
        controls=[system_shift + 0, system_shift + 2],
        num_systems=3 * encoding_depth + int(overflow_qubit),
    )

    carry = [ICCN, ICNI, CICN]
    carries.append(carry)

CNOT = []
if overflow_qubit is True:
    system_shift = 3 * (encoding_depth - 1)
    CNOT = Not(
        targets=[system_shift + 2],
        controls=[system_shift + 1],
        num_systems=3 * encoding_depth + int(overflow_qubit),
    )

# Construct sequence of ANTICARRY and SUM gates
anticarries_sums = []
for i in range(0, encoding_depth):
    system_shift = 3 * (encoding_depth - 1 - i)

    if i != min(range(0, encoding_depth)):
        CICN = Not(
            targets=[system_shift + 3],
            controls=[system_shift + 0, system_shift + 2],
            num_systems=3 * encoding_depth + int(overflow_qubit),
        )
        ICNI = Not(
            targets=[system_shift + 2],
            controls=[system_shift + 1],
            num_systems=3 * encoding_depth + int(overflow_qubit),
        )
        ICCN = Not(
            targets=[system_shift + 3],
            controls=[system_shift + 1, system_shift + 2],
            num_systems=3 * encoding_depth + int(overflow_qubit),
        )

        anticarry = [CICN, ICNI, ICCN]
        anticarries_sums.append(anticarry)

    ICNI = Not(
        targets=[system_shift + 2],
        controls=[system_shift + 1],
        num_systems=3 * encoding_depth + int(overflow_qubit),
    )
    CINI = Not(
        targets=[system_shift + 2],
        controls=[system_shift + 0],
        num_systems=3 * encoding_depth + int(overflow_qubit),
    )

    summation = [ICNI, CINI]
    anticarries_sums.append(summation)

gates = flatten_list(carries + [CNOT] + anticarries_sums)

# Circuit
adder = QuantumCircuit(inputs=input_spec, gates=gates)
adder.diagram()

# Output
sum_registers = [3 * i + 2 for i in range(0, encoding_depth)]
sum_registers_complement = [
    i
    for i in range(0, 3 * encoding_depth + int(overflow_qubit))
    if i not in sum_registers
]
sum_state = adder.state(label="s", traces=sum_registers_complement)
sum_integer = decode(matrix=sum_state.output(), reverse=True)
sum_state = VectorState(spec=encode(integer=sum_integer, reverse=True), label="s")

# Results
augend_state.print()
addend_state.print()
sum_state.print()

final_time = time.time()
computation = f"Computation: {augend_integer} + {addend_integer} = {sum_integer}"
duration = f"Duration: {sp.N(final_time - initial_time,8).round(3)} seconds"
print(computation)
print(duration)
