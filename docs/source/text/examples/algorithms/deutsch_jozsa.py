from qhronology.quantum.gates import Pauli, GateStack, Hadamard, QuantumGate
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.mechanics.matrices import ket

import random
import numpy as np
from scipy.linalg import block_diag

n = 4  # The number of qubits in the address register

constant = None  # Whether the function is constant (True) or balanced (False)
constant = random.choice([True, False]) if constant is None else constant


class Oracle:
    def __init__(self, constant: bool, num_address: int):
        self.constant = constant
        self.num_address = num_address

        if self.constant is True:
            image = [random.choice([0, 1])] * 2**num_address
        else:
            image = [0] * (2**num_address // 2) + [1] * (2**num_address // 2)
        random.shuffle(image)
        self.image = image

    def f(self, x: int) -> int:
        return self.image[x]

    def operator(self) -> np.ndarray:
        blocks = [
            (1 - self.f(x)) * np.eye(2) + self.f(x) * np.eye(2)[::-1]
            for x in range(0, len(self.image))
        ]
        return np.array(block_diag(*blocks))


# Gates
IX = Pauli(index=1, targets=[n], num_systems=n + 1)
HH = GateStack(*[Hadamard()] * (n + 1))

oracle = Oracle(constant=constant, num_address=n)
O = QuantumGate(
    spec=oracle.operator(),
    targets=list(range(0, n + 1)),
    num_systems=n + 1,
    label=" O ",
)

HI = GateStack(*[Hadamard()] * n, Pauli(index=0, family="WIRE_QN"))

# Circuit
deutsch_jozsa = QuantumCircuit(
    gates=[IX, HH, O, HI],
    numerical=True,
    array=True,
)
deutsch_jozsa.diagram(pad=(1, 0), sep=(1, 2), force_separation=True)

# Measurement
probabilities = deutsch_jozsa.measure(
    operators=[ket([0] * n)],
    targets=list(range(0, n)),
    observable=False,
    statistics=True,
)
probability_zeroes = np.round(np.real(probabilities[0])).astype(int)

result_constant = True if probability_zeroes == 1 else False
result_function = "constant" if oracle.constant is True else "balanced"
result_algorithm = "constant" if result_constant is True else "balanced"

# Results
print(f"The function: {result_function}")
print(f"The Deutsch-Jozsa result: {result_algorithm}")
