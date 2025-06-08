from qhronology.quantum.states import MatrixState
from qhronology.quantum.gates import Pauli

import sympy as sp

import copy

# Construct symbolic density matrix
tau = sp.MatrixSymbol("τ", 2, 2).as_mutable()
unknown_state = MatrixState(spec=tau, label="τ")

# Construct observables
I = Pauli(index=0, targets=[0], num_systems=1)
X = Pauli(index=1, targets=[0], num_systems=1)
Y = Pauli(index=2, targets=[0], num_systems=1)
Z = Pauli(index=3, targets=[0], num_systems=1)

# Perform measurements on the unknown state over all observables
unknown_state.measure(operators=[I, X, Y, Z], observable=True)
reconstructed_state = copy.deepcopy(unknown_state)
unknown_state.reset()
reconstructed_state.coefficient(sp.Rational(1, 2))  # Manually normalize
reconstructed_state.simplify()

# Results
unknown_state.print()
reconstructed_state.print()
