.. _`eg:tomography_strong`:

Quantum state tomography
========================

Description
-----------

Quantum state tomography is a technique that consists of the determination of an unknown quantum state by measuring it with respect to all elements of an appropriate *tomographically* or *informationally* complete operator basis. In practise, any such basis is usually a set of observables, with some of the most prominent examples being the Pauli matrices (including the identity matrix) for qubits and the Gell-Mann matrices (also including the identity matrix) for qutrits.

Presented here is a simple tomographical reconstruction of an arbitrary qubit density matrix. Once the unknown state (or rather, an ensemble of identically prepared quantum states) has been measured exhaustively in a suitable basis, the resulting statistics (i.e., expectation values) enable the determination of the Bloch vector via :eq:`eq:matrix_qudit`, which is equivalent to precise identification of the associated (and previously unknown) state.

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/tomography_strong.py
   :name: code:tomography_strong
   :language: python
   :caption:

Output
------

States
^^^^^^

.. code:: python

   >>> unknown_state.print()
   τ = τ[0, 0]|0⟩⟨0| + τ[0, 1]|0⟩⟨1| + τ[1, 0]|1⟩⟨0| + τ[1, 1]|1⟩⟨1|

.. code:: python

   >>> reconstructed_state.print()
   τ = τ[0, 0]|0⟩⟨0| + τ[0, 1]|0⟩⟨1| + τ[1, 0]|1⟩⟨0| + τ[1, 1]|1⟩⟨1|

.. raw:: latex
   
   \newpage