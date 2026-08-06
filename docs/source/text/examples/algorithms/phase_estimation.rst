.. _`eg:phase_estimation`:

Quantum phase estimation
========================

Description
-----------

If :math:`\lambda` is an eigenvalue of a given unitary operator :math:`\Unitary` corresponding to a given eigenvector :math:`\ket{\psi}`, then we have

.. math:: \Unitary\ket{\psi} = \lambda\ket{\psi}.

Since unitary operators represent transformations around the unit circle, then their eigenvalues necessarily have unit modulus, i.e., :math:`\abs{\lambda} = 1`. This means that any such eigenvalue can be written in the form

.. math:: \lambda = \e^{2\pi\eye\theta},

and so is characterized completely by its phase :math:`\theta \in \Reals`. Note that, due to the peridocity of the complex exponential, this may be taken on the restricted domain :math:`0 \leq \theta < 1`. *Quantum phase estimation* is then simply a procedure for estimating this phase :math:`\theta` given both a unitary operator :math:`\Unitary` and an eigenvector :math:`\ket{\psi}`.

Algorithm
---------

In the canonical quantum phase estimation algorithm, introduced by Kitaev :cite:p:`kitaev_quantum_1995` and depicted in :numref:`fig:circuit_algorithm_phase_estimation`, we require two registers. The first (upper), called the *estimation* (or *control*) register, consists of :math:`n` qubits (on the Hilbert space :math:`\SpaceHilbert_2^{\otimes n}`), with each initialized to :math:`\ket{0}`. The second (lower), called the *eigenvector* (or *target*) register, is in the state of a eigenvector :math:`\ket{\psi}` of the given :math:`\Unitary` over :math:`m` qubits (on Hilbert space :math:`\SpaceHilbert_2^{\otimes m}`). The total initial state may therefore be written as

.. math:: \ket{\Psi_0} = \ket{0}^{\otimes n} \otimes \ket{\psi}.

The first step consists of transforming the estimation register to an equal superposition state. This is achieved via an :math:`n`-qubit Hadamard gate operation :math:`\Hadamard^{\otimes n}`, which gives

.. math::

   \begin{aligned}
       \ket{\Psi_1} &= (\Hadamard^{\otimes n} \otimes \Identity^{\otimes m})\ket{\Psi_0} \\
       &= \ket{+}^{\otimes n} \otimes \ket{\psi} \\
       &= \frac{1}{2^{n/2}}\sum_{x=0}^{2^n - 1} \ket{x} \otimes \ket{\psi}.
   \end{aligned}

Here, :math:`\ket{x}` is an :math:`n`-ary representation of states in the :math:`n`-qubit register, e.g.,

.. math:: \ket{x} = \bigotimes_{\ell = 0}^{n - 1} \ket{x_\ell},

where the binary decomposition of :math:`x` is simply

.. math:: x = \sum_{\ell = 0}^{n - 1} x_\ell 2^\ell.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_phase_estimation-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a quantum phase estimation algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_phase_estimation-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of a quantum phase estimation algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_phase_estimation-light.png
   :name: fig:circuit_algorithm_phase_estimation
   :scale: 34 %
   :alt: A quantum circuit diagram of a quantum phase estimation algorithm.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum phase estimation algorithm.

.. raw:: latex

   \vspace*{-\baselineskip}

A sequence of controlled-:math:`\Unitary` operations, each of the form,

.. math:: \Control^{\indices{\ell}} \Unitary^{2^\ell} = \sum_{k=0}^{1} {\ket{k}\bra{k}}^{\indices{\ell}} \otimes \bigl(\Unitary^{2^\ell}\bigr)^k

is then applied, where :math:`\ell` is the index of the system in the estimation register. The total transformation incurred by this sequence may be written as

.. math:: \Unitary_\Control = \prod_{\ell = 0}^{n - 1} \Control^{\indices{\ell}} \Unitary = \sum_{k=0}^{2^n - 1} \ket{k}\bra{k} \otimes \Unitary^k,

under which the circuit's state becomes

.. math::

   \begin{aligned}
       \ket{\Psi_2} &= \Unitary_\Control \ket{\Psi_1} \\
       &= \frac{1}{\sqrt{2^n}} \sum_{k=0}^{2^n - 1} \e^{2\pi\eye\theta k} \ket{k} \otimes \ket{\psi}.
   \end{aligned}

Note that here we introduced the eigenvalue of :math:`\Unitary` as :math:`\lambda = \e^{2\pi\eye\theta}` (corresponding to the eigenvector :math:`\ket{\psi}`), and subsequently used the fact that

.. math:: \Unitary^{k} \ket{\psi} = \e^{2\pi\eye\theta k} \ket{\psi}.

Performing an :math:`n`-qubit inverse Fourier transform :math:`\QFT_n^\dagger`,

.. math:: \ket{k} \stackrel{\QFT_n^\dagger}{\longrightarrow} \frac{1}{\sqrt{2^n}} \sum\limits_{x=0}^{2^n - 1} \e^{-2\pi\eye k x 2^{-n}} \ket{x},

on the estimation register then yields the output state

.. math::

   \begin{aligned}
       \ket{\Psi_3} &= (\QFT_n^\dagger \otimes \Identity) \ket{\Psi_2} \\
       &= \frac{1}{\sqrt{2^n}} \sum_{k=0}^{2^n - 1} \e^{2\pi\eye\theta k} \left(\frac{1}{\sqrt{2^n}} \sum\limits_{x=0}^{2^n - 1} \e^{-2\pi\eye k x 2^{-n}} \ket{x}\right) \otimes \ket{\psi} \\
       &= \frac{1}{2^{n}} \sum_{k=0}^{2^n - 1} \sum\limits_{x=0}^{2^n - 1} \e^{2\pi\eye k (\theta - x 2^{-n})} \ket{x} \otimes \ket{\psi}.
   \end{aligned}

By inspection, the amplitude associated with each :math:`\ket{x}` simply takes the form

.. math:: c_x = \frac{1}{2^{n}} \sum_{k = 0}^{2^n - 1} \e^{2\pi\eye k (\theta - x 2^{-n})},

and so performing a measurement in the computational basis on the estimation register yields the outcome :math:`\ket{y}` with probability

.. math:: p_y = |c_y|^2 = \frac{1}{2^{2n}} \abs{\sum_{k = 0}^{2^n - 1} \e^{2\pi\eye k (\theta - y 2^{-n})}}^2.

With foresight, we can define the substitution

.. math:: \theta = \frac{z}{2^{n}} + \delta

where :math:`z/2^{n}` is the nearest integer to :math:`\theta`, and the discrepancy :math:`\delta` satisfies :math:`0 \leq \abs{\delta} \leq 1/2`. In effect, this approximates :math:`\theta \in [0, 1]` by rounding its value to the nearest integer. With this, the probabilities take the form

.. math:: p_y = \frac{1}{2^{2n}} \abs{\sum_{k = 0}^{2^n - 1} \e^{\frac{2\pi\eye k}{2^n} (z - y)} \e^{2\pi\eye k \delta}}^2.

If :math:`\delta = 0`, the corresponding probability to find such a value :math:`z` is

.. math:: p_z = \frac{1}{2^{2n}} \abs{\sum_{k = 0}^{2^n - 1} 1}^2 = 1.

Evidently, in such a case, the outcome is always found to be :math:`y = z`, and so the phase can decoded as :math:`\theta = z / 2^n`. Alternatively, if :math:`\delta \neq 0`, then the probability to find :math:`z` is

.. math::

   \begin{aligned}
       p_z &= \frac{1}{2^{2n}} \abs{\sum_{k = 0}^{2^n - 1} \e^{2\pi\eye k \delta}}^2 \\
       &= \frac{1}{2^{2n}} \abs{\frac{1 - \e^{2\pi\eye 2^n \delta}}{1 - \e^{2\pi\eye \delta}}}^2,
   \end{aligned}

where we used the identity

.. math:: \sum_{n = 0}^{N - 1} a^n = \frac{1 - a^N}{1 - a}, \quad a \neq 1.

With a little effort, it can be shown that

.. math:: p_z \geq \frac{4}{\pi^2} \approx 0.405

for any :math:`\delta \neq 0`, from which we can conclude that the algorithm provides an estimate of :math:`\theta` (to within :math:`1/2^n` of the actual value) with a probability of at least :math:`4/\pi^2`.

Implementation
--------------

In this implementation, the target register consists of a single qubit :math:`\ket{\psi} = \ket{1}`, with which the unitary operator is the phase gate, specifically,

.. math:: \Unitary(\theta) = \ket{0}\bra{0} + \e^{2\pi\eye\theta} \ket{1}\bra{1}.

.. raw:: latex

   \vspace*{-\baselineskip}

.. raw:: latex

   \begin{codetitled}{Quantum phase estimation}{}

.. literalinclude:: /text/examples/algorithms/phase_estimation.py
   :name: code:phase_estimation
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

   >>> phase_estimator.diagram(pad=(1, 0), force_separation=True)

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.12cm]{text_examples_algorithms_phase_estimation.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_phase_estimation-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_phase_estimation-light.png
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

   Input phase: 0.64
   Bitstring=0000, Probability=0.002, Phase=0
   Bitstring=0001, Probability=0.002, Phase=0.0625
   Bitstring=0010, Probability=0.002, Phase=0.1250
   Bitstring=0011, Probability=0.002, Phase=0.1875
   Bitstring=0100, Probability=0.002, Phase=0.2500
   Bitstring=0101, Probability=0.002, Phase=0.3125
   Bitstring=0110, Probability=0.003, Phase=0.3750
   Bitstring=0111, Probability=0.005, Phase=0.4375
   Bitstring=1000, Probability=0.010, Phase=0.5000
   Bitstring=1001, Probability=0.031, Phase=0.5625
   Bitstring=1010, Probability=0.825, Phase=0.6250 (most probable)
   Bitstring=1011, Probability=0.083, Phase=0.6875
   Bitstring=1100, Probability=0.016, Phase=0.7500
   Bitstring=1101, Probability=0.007, Phase=0.8125
   Bitstring=1110, Probability=0.004, Phase=0.8750
   Bitstring=1111, Probability=0.003, Phase=0.9375
   Expectation (weighted average): 0.6245

.. raw:: latex

   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage