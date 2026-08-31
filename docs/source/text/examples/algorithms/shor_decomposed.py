from qhronology.quantum.gates import GateStack, Hadamard, Pauli, QuantumGate, Fourier, Swap, Not
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.matrices import encode, decode
from qhronology.mechanics.operations import dagger

import math
from fractions import Fraction
import sympy as sp
import numpy as np

N = 15  # The number to be factorized
a = 2  # Should be coprime to N
decompose = True  # Whether to decompose the modular exponentiation

n = int(math.ceil(math.log(N + 1, 2)))  # Encoding depth

num_controls = 2 * n
num_targets = n
num_total = num_targets + num_controls

systems_controls = list(range(0, num_controls))
systems_targets = [k + num_controls for k in range(0, num_targets)]

# Gates
HX = GateStack(
    *[Hadamard()] * num_controls,
    Pauli(index=1),
)


# Function for computing modular exponentiation
def mod_exp_function(base: int, power: int, modulus: int) -> int:
    """Compute a^{2^j} (mod N)."""
    value = base
    for _ in range(power):
        value = int(value**2 % modulus)
    return value


# Function for constructing modular exponentiation operators
def mod_exp_operator(
    base: int,
    power: int,
    modulus: int,
    num_systems: int | None = None
) -> np.ndarray:
    """Compute U_{N,a}^{2^j}."""
    value = mod_exp_function(base, power, modulus)
    num_systems = (
        int(math.ceil(math.log(modulus + 1, 2)))
        if num_systems is None else num_systems
    )

    untransformed = list(range(0, 2**num_systems))
    transformed = [
        (value * k) % (2**num_systems - 1) for k in untransformed
    ]

    operator = np.zeros((2**num_systems, 2**num_systems), dtype=complex)
    for pair in zip(untransformed, transformed):
        operator += encode(
            pair[1], num_systems, numerical=True, array=True
        ) * dagger(encode(
            pair[0], num_systems, numerical=True, array=True
        ))
    operator[(0, -1)] = 0
    operator[(-1, -1)] = 1
    return operator


# Construct modular exponentiation gates
mod_exp_gates = []
for j in systems_controls:
    operator = mod_exp_operator(a, j, N)
    if (
        mod_exp_function(a, j, N) != 1
        or np.array_equal(operator, np.eye(2**n, dtype=complex)) is False
    ):
        mod_exp_gates.append(
            QuantumGate(
                spec=operator,
                targets=systems_targets,
                controls=[systems_controls[j]],
                num_systems=num_total,
                label=f"U[a^2^{j} % N]",
                numerical=True,
                array=True,
            )
        )

# Decompose modular exponentiation gates
# (Note: this is not possible for every combination of N and a)
if decompose is True:
    # Decompose into SWAP gates
    for g, gate in enumerate(mod_exp_gates):
        mod_exp_gates[g] = gate.decompose(
            gates=[Swap()],
            depth=n,
        )[0]
    mod_exp_gates = [
        gate for sequence in mod_exp_gates
        for gate in sequence
    ]
    # Decompose into CNOT gates
    for g, gate in enumerate(mod_exp_gates):
        mod_exp_gates[g] = gate.decompose(
            gates=[Not()],
            additional_nodes=(0, 1, 0),
        )[0]
    mod_exp_gates = [
        gate for sequence in mod_exp_gates
        for gate in sequence
    ]

IQFT = Fourier(
    targets=systems_controls,
    num_systems=num_total,
    composite=True,
    conjugation=True,
    label="QFT^†",
)

# Circuit
shor = QuantumCircuit(
    gates=[HX] + mod_exp_gates + [IQFT],
    numerical=True,
    array=True,
)
shor.diagram(pad=(1, 0), force_separation=True)

# Measurement
basis = [encode(k, num_controls) for k in range(0, 2**num_controls)]
probabilities = shor.measure(
    operators=basis,
    targets=systems_controls,
    observable=False,
    statistics=True,
)
probabilities = [np.real(probability) for probability in probabilities]

# Results
print(f"Input number: {N}")
threshold = 0.01
for k, probability in enumerate(probabilities):
    if probability >= threshold or probability == max(probabilities):
        probability = sp.N(probability).round(3)
        phase = decode(basis[k]) / 2**num_controls
        r = Fraction(phase).limit_denominator(N - 1).denominator
        bitstring = encode(
            decode(basis[k], reverse=True),
            num_controls,
            return_type=str,
        )

        suffix = "(period not suitable)"
        if r % 2 == 0:
            p = math.gcd(a ** int(r / 2) - 1, N)
            q = math.gcd(a ** int(r / 2) + 1, N)

            if not p * q == N:
                p, q = p * q, int(N / (p * q))
            if p * q == N and p > 1 and q > 1:
                suffix = f"Factors: {p} and {q}"
            else:
                suffix = "(algorithm failed)"

        print(
            f"Bitstring={bitstring}, "
            + f"Probability={probability}, "
            + f"Period={r}, "
            + f"{suffix}"
        )
