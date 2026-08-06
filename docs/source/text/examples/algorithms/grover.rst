.. _`eg:grover`:

Grover's algorithm
==================

Description
-----------

*Grover's algorithm* :cite:p:`grover_fast_1996` is a probabilistic quantum algorithm for performing an unstructured search on an input of size :math:`N` in a time (query) complexity of :math:`\BigO(\sqrt{N})`. In other words, Grover's algorithm finds (with high probability) a *marked* (or *target*) value contained within an input domain (which is usually taken to be some given dataset). This is achieved by first encoding the input domain as a quantum state (i.e., a quantum superposition of all possible values), following which the target state's probability amplitude in the superposition is amplified via *Grover iterations*---a sequence of oracles and *Grover diffusion operators*. Classically, an unstructured search would require, on average, exactly :math:`N/2` evaluations (queries) of the input to find the correct value, which corresponds to a query complexity of :math:`\BigO(N)`. Grover's algorithm therefore presents a quadratic speedup compared to the best classical algorithm.

Algorithm
---------

In Grover's algorithm, we have two inputs: the input size :math:`N \geq 1` and marked value :math:`\tilde{x} \geq 0`, both decimal integers with :math:`\tilde{x} < N`. The task is to, given the set of inputs,

.. math:: \Integers_N = \{ x \in \Integers \, : \, 0 \leq x \leq N - 1 \},

find the marked value :math:`\tilde{x} \in \Integers_N`. Note however that, as at least :math:`n = \lceil \log_{2}(N) \rceil` qubits are required to encode the entire input set, then the search will necessarily be conducted on the (larger) domain

.. math:: \Integers_{2^n} = \{ x \in \Integers \, : \, 0 \leq x \leq 2^n - 1 \}.

The quantum circuit representation of Grover's algorithm appears in :numref:`fig:circuit_algorithm_grover`. Here, the circuit's register is initialized in the state

.. math:: \ket{\Psi_0} = \ket{0}^{\otimes n}.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_grover-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of Grover's algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_grover-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of Grover's algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_grover-light.png
   :name: fig:circuit_algorithm_grover
   :scale: 34 %
   :alt: A quantum circuit diagram of Grover's algorithm.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Grover's algorithm.

We first apply a Hadamard gate to each system, which yields

.. math::

   \begin{aligned}
       \ket{\Psi_1} &= \Hadamard^{\otimes n}\ket{\Psi_0} \\
       &= \Hadamard^{\otimes n} \ket{0}^{\otimes n} \\
       &= \ket{+}^{\otimes n} \\
       &= \ket{\phi},
   \end{aligned}

where defined the *equiprobabilistic* or *uniform* superposition state :math:`\ket{\phi}` as

.. math:: \ket{\phi} \equiv \frac{1}{\sqrt{N}} \sum_{x=0}^{N - 1} \ket{x},

with :math:`N \equiv 2^n`. This state describes the (equal) superposition of all possible values in the input domain :math:`\Integers_{2^n}`.

Next, we perform the *Grover iterations*. Each iteration involves first applying the oracle :math:`\Oracle_{\tilde{x}}`, which has the action

.. math:: \Oracle_{\tilde{x}} = \Identity - 2 \ket{\tilde{x}}\bra{\tilde{x}},

where :math:`\tilde{x}` is the marked value. The role of the oracle is to flip the phase of the marked state: this is manifestly evident when we characterize the oracle by its action on a basis state :math:`\ket{x}`,

.. math:: \Oracle_{\tilde{x}} \ket{x} = (-1)^{f(x)} \ket{x},

where

.. math::

   f(x) =
   \begin{cases}
       1, & \text{if } x = \tilde{x}; \\
       0, & \text{if } x \neq \tilde{x}.
   \end{cases}

The second part of each Grover iteration is the transformation of the state under the *Grover diffusion operator*,

.. math::

   \begin{aligned}
       \Diffusion &= 2 \ket{\phi}\bra{\phi} - \Identity^{\otimes n} \\
       &= \Hadamard^{\otimes n} \cdot (2 \ket{0}\bra{0}^{\otimes n} - \Identity^{\otimes n}) \cdot \Hadamard^{\dagger \otimes n}.
   \end{aligned}

Applying this operator to any given state effectively performs an inversion of its amplitudes about the average. For the state in the algorithm immediately after transformation by the oracle, this results in the phase-flipped marked value's amplitude being inverted (phase-flipped) and subsequently amplified more than that of any of the other values.

After :math:`r` such iterations, arrive at the output state

.. math:: \ket{\Psi_2} = (\Diffusion \Oracle_{\tilde{x}})^r \ket{\Psi_1}.

Measuring this in the computational basis, we find that, for the most optimal number of iterations (which can be shown analytically to be approximately :math:`r \approx \pi\sqrt{N}/4`), the most probable state is :math:`\ket{\tilde{x}}`.

Implementation
--------------

.. raw:: latex

   \enlargethispage{-\baselineskip}

.. raw:: latex

   \begin{codetitled}{Grover's algorithm}{}

.. literalinclude:: /text/examples/algorithms/grover.py
   :name: code:grover
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> grover.diagram(pad=(1, 0), sep=(1, 2), force_separation=True)

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_grover.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_grover-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_grover-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex
   
   \end{code}

Results
^^^^^^^

Cumulative output from the various print statements:

.. raw:: latex

   \begin{code}

.. code:: output

   Input size: 10
   Marked value: 4
   Bitstring=0000, Probability=0.003, Value=0
   Bitstring=0001, Probability=0.003, Value=1
   Bitstring=0010, Probability=0.003, Value=2
   Bitstring=0011, Probability=0.003, Value=3
   Bitstring=0100, Probability=0.961, Value=4 (most probable)
   Bitstring=0101, Probability=0.003, Value=5
   Bitstring=0110, Probability=0.003, Value=6
   Bitstring=0111, Probability=0.003, Value=7
   Bitstring=1000, Probability=0.003, Value=8
   Bitstring=1001, Probability=0.003, Value=9
   Bitstring=1010, Probability=0.003, Value=10
   Bitstring=1011, Probability=0.003, Value=11
   Bitstring=1100, Probability=0.003, Value=12
   Bitstring=1101, Probability=0.003, Value=13
   Bitstring=1110, Probability=0.003, Value=14
   Bitstring=1111, Probability=0.003, Value=15
   Expectation (weighted average): 4.144

.. raw:: latex

   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage