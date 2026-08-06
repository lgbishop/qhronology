from qhronology.quantum.gates import GateStack, Hadamard, QuantumGate
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.matrices import ket, bra, encode, decode
from qhronology.mechanics.operations import densify

import math
import sympy as sp
import numpy as np

N = 10  # The size of the input space (domain)
marked = 4  # The value to find (should be smaller than N)

n = int(math.ceil(math.log(N, 2)))  # Encoding depth
iterations = int(math.pi * math.sqrt(2**n) / 4)

# Gates
H = GateStack(*[Hadamard()] * n)

# Construct the oracle from its definition
oracle = QuantumGate(
    spec=sp.eye(2**n) - 2 * densify(encode(marked, num_systems=n)),
    targets=list(range(0, n)),
    num_systems=n,
    label="O",
)

# Construct the Grover diffusion gate from its definition
diffusion = QuantumCircuit(
    gates=[H]
    + [
        QuantumGate(
            spec=2 * ket([0] * n) * bra([0] * n) - sp.eye(2**n),
            targets=list(range(0, n)),
        )
    ]
    + [H]
).gate(label="D")

# Construct the gate sequence of the Grover iterations
grover_iterations = [oracle, diffusion] * iterations

# Circuit
grover = QuantumCircuit(
    gates=[H] + grover_iterations,
    numerical=True,
    array=True,
)
grover.diagram(pad=(1, 0), sep=(1, 2), force_separation=True)

# Measurement
basis = [encode(k, n) for k in range(0, 2**n)]
probabilities = grover.measure(
    operators=basis,
    observable=False,
    statistics=True,
)
probabilities = [np.real(probability) for probability in probabilities]

# Results
print(f"Input size: {N}")
print(f"Marked value: {marked}")
expectation = 0
threshold = 0.001
for k, probability in enumerate(probabilities):
    value = decode(basis[k])
    bitstring = encode(value, n, return_type=str)
    expectation += probability * value

    suffix = ""
    if probability == max(probabilities):
        suffix = " (most probable)"

    if probability >= threshold or probability == max(probabilities):
        probability = sp.N(probability).round(3)
        print(
            f"Bitstring={bitstring}, "
            + f"Probability={probability}, "
            + f"Value={value}"
            + f"{suffix}"
        )

expectation = sp.N(expectation).round(3)
print(f"Expectation (weighted average): {expectation}")
