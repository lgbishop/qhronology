from qhronology.quantum.gates import GateStack, Hadamard, Pauli, Phase, Fourier
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.matrices import encode, decode

import sympy as sp
import numpy as np

phase = 0.64  # The phase to be estimated
precision = 4  # The number of qubits used by the estimation

num_controls = precision
num_targets = 1
num_total = num_targets + num_controls

systems_controls = list(range(0, num_controls))
systems_targets = [m + num_controls for m in range(0, num_targets)]

# Gates
HX = GateStack(
    *[Hadamard()] * num_controls,
    Pauli(index=1),
)

unitaries = [
    Phase(
        phase=sp.exp(2 * sp.I * sp.pi * phase * 2**n),
        targets=systems_targets,
        controls=[systems_controls[n]],
        num_systems=num_total,
        label=f"U^{2**n}",
    )
    for n in range(0, num_controls)
]

IQFT = Fourier(
    targets=systems_controls,
    num_systems=num_total,
    composite=True,
    conjugation=True,
    label="QFT^†",
)

# Circuit
phase_estimator = QuantumCircuit(
    gates=[HX] + unitaries + [IQFT],
    numerical=True,
    array=True,
)
phase_estimator.diagram(pad=(1, 0), force_separation=True)

# Measurement
basis = [encode(k, num_controls) for k in range(0, 2**num_controls)]
probabilities = phase_estimator.measure(
    operators=basis,
    targets=systems_controls,
    observable=False,
    statistics=True,
)
probabilities = [np.real(probability) for probability in probabilities]

# Results
print(f"Input phase: {phase}")
expectation = 0
threshold = 0.001
for k, probability in enumerate(probabilities):
    value = decode(basis[k]) / 2**num_controls
    value = sp.N(value).round(precision)
    bitstring = encode(decode(basis[k]), num_controls, return_type=str)
    expectation += probability * value

    suffix = ""
    if probability == max(probabilities):
        suffix = " (most probable)"

    if probability >= threshold or probability == max(probabilities):
        probability = sp.N(probability).round(3)
        print(
            f"Bitstring={bitstring}, "
            + f"Probability={probability}, "
            + f"Phase={value}"
            + f"{suffix}"
        )

expectation = sp.N(expectation).round(precision)
print(f"Expectation (weighted average): {expectation}")
