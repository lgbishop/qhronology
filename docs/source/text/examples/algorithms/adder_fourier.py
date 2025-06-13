from qhronology.quantum.states import VectorState
from qhronology.quantum.gates import Hadamard, Phase, Fourier
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.utilities.helpers import flatten_list
from qhronology.mechanics.matrices import encode, decode

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

QFT = []
IQFT = []
for i in range(0, encoding_depth):
    count = encoding_depth - i
    for j in range(0, count):
        if j == 0:
            QFT.append(
                Hadamard(
                    targets=[i + encoding_depth],
                    num_systems=2 * encoding_depth,
                    conjugate=False,
                    label="H",
                )
            )
            IQFT.append(
                Hadamard(
                    targets=[i + encoding_depth],
                    num_systems=2 * encoding_depth,
                    conjugate=True,
                    label="H^†",
                )
            )
        else:
            QFT.append(
                Phase(
                    targets=[i + j + encoding_depth],
                    controls=[i + encoding_depth],
                    exponent=sp.Rational(1, (2**j)),
                    num_systems=2 * encoding_depth,
                    conjugate=False,
                    label=f"{2**j}",
                    family="GATE",
                )
            )
            IQFT.append(
                Phase(
                    targets=[i + j + encoding_depth],
                    controls=[i + encoding_depth],
                    exponent=sp.Rational(1, (2**j)),
                    num_systems=2 * encoding_depth,
                    conjugate=True,
                    label=f"{2**j}^†",
                    family="GATE",
                )
            )

IQFT = IQFT[::-1]

CPHASE = []
for i in range(0, encoding_depth):
    count = encoding_depth - i
    for j in range(0, count):
        CPHASE.append(
            Phase(
                targets=[i + encoding_depth],
                controls=[j + i],
                exponent=sp.Rational(1, (2**j)),
                num_systems=2 * encoding_depth,
                label=f"{2**j}",
                family="GATE",
            )
        )

gates = flatten_list(QFT + CPHASE + IQFT)

# Circuit
adder = QuantumCircuit(inputs=[augend_state, addend_state], gates=gates)
adder.diagram()

# Output
sum_registers = [(i + encoding_depth) for i in range(0, encoding_depth)]
sum_registers_complement = [
    i for i in range(0, 2 * encoding_depth) if i not in sum_registers
]
sum_state = adder.state(label="s", traces=sum_registers_complement)
sum_integer = decode(sum_state.output())

# Results
augend_state.print()
addend_state.print()
sum_state.print()

final_time = time.time()
computation = f"Computation: {augend_integer} + {addend_integer} = {sum_integer}"
duration = f"Duration: {sp.N(final_time - initial_time,8).round(3)} seconds"
print(computation)
print(duration)
