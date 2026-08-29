# Based on: https://arxiv.org/abs/1608.00263

from qhronology.quantum.gates import Hadamard, Pauli, Phase, GateInterleave
from qhronology.quantum.circuits import QuantumCircuit
from qhronology.utilities.helpers import flatten_list

import sympy as sp

num_systems = 5
num_cycles = 8
cycles = [[] for _ in range(0, num_cycles)]

H = [Hadamard(targets=[i]) for i in range(0, num_systems)]
cycles[0] = H

for cycle in range(1, num_cycles):
    # Controlled-phase (CZ) gates
    cycles[cycle] += [
        Pauli(
            index=3,
            targets=[i % num_systems + (cycle - 1) % 3],
            controls=[(i + 1) % num_systems + (cycle - 1) % 3],
            family="CTRL",
        )
        for i in range(0, num_systems, 3)
        if (i + 1) < num_systems
        and (i + 1) % num_systems + (cycle - 1) % 3 < num_systems
    ]

    # (non-Clifford) T gates
    cycles[cycle] += [
        Phase(exponent=sp.Rational(1, 4), targets=[i], label="T")
        for i in range(0, num_systems)
        if any(
            i in indices
            for indices in [
                gate.targets + gate.controls
                for gate in cycles[cycle]
            ]
        )
        is False
        and any(
            i in indices
            for indices in [
                gate.targets + gate.controls
                for gate in cycles[cycle - 1]
                if type(gate) is Pauli and gate.index == 3
            ]
        )
        is True
        and any(
            i in indices
            for indices in [
                gate.targets
                for gate in flatten_list(cycles)
                if type(gate) is Phase
            ]
        )
        is False
        and i + 1 <= num_systems
    ]

    # X^(1/2) and Y^(1/2) gates
    order_index = [1, 2]  # Corresponding to [X, Y]
    cycles[cycle] += [
        Pauli(
            index=order_index[i % 2],
            exponent=sp.Rational(1, 2),
            targets=[i],
        )
        for i in range(0, num_systems)
        if any(
            i in indices
            for indices in [
                gate.targets + gate.controls
                for gate in cycles[cycle]
            ]
        )
        is False
        and any(
            i in indices
            for indices in [
                gate.targets + gate.controls
                for gate in cycles[cycle - 1]
                if type(gate) is Pauli and gate.index == 3
            ]
        )
        is True
        and order_index[i % 2]
        not in [
            gate.index
            for gate in cycles[cycle - 1]
            if type(gate) is Pauli and i in gate.targets
        ]
        and i + 1 <= num_systems
    ]

for cycle in range(0, num_cycles):
    cycles[cycle] = GateInterleave(*cycles[cycle], merge=False)

circuit = QuantumCircuit(gates=cycles)
circuit.diagram(sep=(1, 2), force_separation=True)
circuit.decompactify()
circuit.diagram(sep=(0, 2), force_separation=True)