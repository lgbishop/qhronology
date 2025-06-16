.. _`eg:tomography_weak`:

Quantum state tomography via weak measurements
==============================================

Description
-----------

The quantum state tomography methodology presented in :ref:`eg:tomography_strong` is a standard scheme that uses ordinary ("strong") measurements---those which by necessity disturb (i.e., collapse the wave function of) the quantum system under consideration. Thus, in order to perform state tomography without (significantly) disrupting the unknown system, we can use so-called *weak measurements*, that is, quantum measurements which minimize disturbance by leaving the measured state unaffected (to first order in the strength of the measurement). The idea of performing quantum state tomography using weak measurements constitutes a powerful technique that has been used with great success in a plethora of past experimental applications :cite:p:`knight_weak_1990, hosten_observation_2008, lundeen_experimental_2009, dixon_ultrasensitive_2009, kim_reversing_2009, cho_weak_2010, goggin_violation_2011, zilberberg_charge_2011, lundeen_direct_2011, kocsis_observing_2011, feizpour_amplifying_2011, kim_protecting_2012, rozema_violation_2012, vijay_stabilizing_2012, hatridge_quantum_2013, salvail_full_2013, groen_partial-measurement_2013, malik_direct_2014, blok_manipulating_2014, magana-loaiza_amplification_2014, denkmayr_observation_2014, mirhosseini_compressive_2014, shi_scan-free_2015, mahler_experimental_2016, thekkadath_direct_2016, piacentini_measuring_2016, hallaji_weak-value_2017, kim_direct_2018, nirala_measuring_2019`.

The scheme presented here follows the work in :cite:p:`bishop_quantum_2025`. It is limited to *qubits*, though is it thought to be generalizable to qudits without too much difficulty. Note that while most treatments consider weak measurements characterized by weakly coupled interactions (that is, unitary operators close to identity), this formalism is based on :cite:p:`pryde_measuring_2004,pryde_measurement_2005`, in which a near eigenstate of the NOT (Pauli-X) gate is perturbed *weakly* by a control state via the standard CNOT interaction. See, e.g., :cite:p:`wu_weak_2009, kofman_nonperturbative_2012, wu_state_2013, svensson_pedagogical_2013, tamir_introduction_2013, dressel_colloquium_2014` for pedagogical exposition of weak measurements and the associated weak values, and :cite:p:`story_weak_1991, wu_state_2013, kim_direct_2018, botero_weak_2018` for good examples of weak-measurement tomography.

At the heart of this methodology is an ancillary qubit, which is also known as the *target* or *probe*. In the :math:`z`-basis :math:`\left\{\ket{0},\ket{1}\right\}`, it may be expressed as

.. math:: \ket{\Probe} = \sqrt{\frac{1+\Strength}{2}}\ket{0} + \sqrt{\frac{1-\Strength}{2}}\ket{1}, \quad 0 \leq \Strength \leq 1.
   :label: eq:probe

Its function is to transform in response to the state of an unknown system :math:`\StateCV`. This is achieved by coupling the two states together, thereby enabling direct measurement of the ancilla to yield information regarding :math:`\StateCV`. If the interaction is sufficiently weak, then this state remains undisturbed. Note that of course, a quantum state cannot be fully characterized by performing just a single measurement. The best we can accomplish for qubits, at least using weak measurements, is to infer the expectation value of the unknown system along one of the three axes of the Bloch sphere. The original state :math:`\StateCV` may then be completely reconstructed from the combined statistics, by way of the determination of the state's Bloch vector.

Perhaps the simplest coupling between an unknown state and the probe that will permit this tomography scheme is the CNOT gate, which we write as

.. math:: \Control^0 \NOT^1 \equiv {\ket{0}\bra{0}}^0 \otimes \Identity^1 + {\ket{1}\bra{1}}^0 \otimes \Pauli_x^1.

As we wish to measure along each of three Bloch axes, this can be combined with basis transformation gates :math:`\UnitaryBasis^{(\dagger)}_k`, yielding the system-probe unitary interaction

.. math::
   :label: eq:unitary_tomography_weak

   \begin{aligned}
      \Tomography &= \bigl(\UnitaryBasis^{\dagger}_k \otimes \Identity\bigr) \cdot \Control^0 \NOT^1 \cdot \bigl(\UnitaryBasis_k \otimes \Identity\bigr) \\
      &= \ket{0_k}\bra{0_k} \otimes \Identity + \ket{1_k}\bra{1_k} \otimes \Pauli_x.
   \end{aligned}

This is depicted diagrammatically as a quantum circuit in :numref:`fig:circuit_algorithm_tomography_weak`, where we denote the evolved ancilla by :math:`\StateProbe_k`. Here, the aforementioned basis gates :math:`\UnitaryBasis^{(\dagger)}_k` (where :math:`k=1,2,3`) represent transformations that map the :math:`z`-basis eigenstates :math:`\left\{\ket{0},\ket{1}\right\}` into either the :math:`x`- (:math:`k=1`), :math:`y`- (:math:`k=2`) or :math:`z`- (:math:`k=3`) bases. Specifically, we write

.. math::
   :label: eq:tomography_eigenstates

   \begin{aligned}
      \UnitaryBasis^\dagger_k  \ket{0} &= \ket{0_k}, \\
      \UnitaryBasis^\dagger_k  \ket{1} &= \ket{1_k},
   \end{aligned}

where :math:`\left\{\ket{0_k},\ket{1_k}\right\}` are eigenstates of the three bases of our qubit Hilbert space. This means that, given the Pauli matrices :eq:`eq:Pauli`, the states defined by :eq:`eq:tomography_eigenstates` necessarily satisfy

.. math::

   \begin{aligned}
      \Pauli_k  \ket{0_k} &= \ket{0_k}, \\
      \Pauli_k  \ket{1_k} &= -\ket{1_k}.
   \end{aligned}

For this to be fulfilled, we must have

.. math::
   :label: eq:tomography_transformations

   \begin{aligned}
      \UnitaryBasis_1 &= \Hadamard, \\
      \UnitaryBasis_2 &= \Hadamard \Phase^\dagger, \\
      \UnitaryBasis_3 &= \Identity,
   \end{aligned}

where

.. math:: \Hadamard \equiv \frac{1}{\sqrt{2}} \bigl(\ket{0}\bra{0} + \ket{0}\bra{1} + \ket{1}\bra{0} - \ket{1}\bra{1}\bigr)

is the Hadamard gate, and

.. math:: \Phase \equiv \ket{0}\bra{0} + \eye\ket{1}\bra{1}

is a phase shift gate.

.. only:: html

   .. figure:: /figures/output/circuit_algorithm_tomography_weak-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum state tomography algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_algorithm_tomography_weak-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a quantum state tomography algorithm.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_algorithm_tomography_weak-light.png
   :name: fig:circuit_algorithm_tomography_weak
   :scale: 36 %
   :alt: A quantum circuit diagram of a quantum state tomography algorithm.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum state weak-measurement tomography algorithm.

With these definitions in mind, a weak measurement can be easily computed in a number of steps. First, given the unknown system :math:`\StateCV`, the ancilla :math:`\ket{\Probe}`, and the weak-measurement unitary :eq:`eq:unitary_tomography_weak`, the evolution of the product state :math:`\StateCV\otimes\ket{\Probe}\bra{\Probe}` is the standard unitary map

.. math::
   :label: eq:tomography_evolution

   \begin{aligned}
      \MapGeneral_{\Tomography}\bigl[\StateCV\otimes\ket{\Probe}\bra{\Probe}\bigr] &= \Tomography\bigl(\StateCV\otimes\ket{\Probe}\bra{\Probe}\bigr)\Tomography^\dagger \\\
      %= \; & \aket{0_k}\abra{0_k} \StateCV \aket{0_k}\abra{0_k} \otimes \aket{\Probe}\abra{\Probe} \\
      %&+ \aket{0_k}\abra{0_k} \StateCV \aket{1_k}\abra{1_k} \otimes \aket{\Probe}\abra{\Probe}\Pauli_x \\
      %&+ \aket{1_k}\abra{1_k} \StateCV \aket{0_k}\abra{0_k} \otimes \Pauli_x\aket{\Probe}\abra{\Probe} \\
      %&+ \aket{1_k}\abra{1_k} \StateCV \aket{1_k}\abra{1_k} \otimes \Pauli_x\aket{\Probe}\abra{\Probe}\Pauli_x \\
      &= \sum_{n,m=0}^{1} \ket{n_k}\bra{n_k}  \StateCV  \ket{m_k}\bra{m_k} \otimes \Pauli^n_x  \ket{\Probe}\bra{\Probe}  \Pauli_x^{m}.
   \end{aligned}

The state of the evolved system :math:`\StateCV^\prime` after the interaction is computed by performing a partial trace on the probe's Hilbert space,

.. math::
   :label: eq:tomography_evolved_unknown

   \begin{aligned}
      \StateCV^\prime = \; & \trace_{1}\bigl[\Tomography\bigl(\StateCV\otimes\ket{\Probe}\bra{\Probe}\bigr)\Tomography^\dagger\bigr] \\
      %= \; & \aket{0_k}\abra{0_k} \StateCV \aket{0_k}\abra{0_k} \\
      %&+ \abra{\Probe}{\Pauli_x}\aket{\Probe} \aket{0_k}\abra{0_k} \StateCV \aket{1_k}\abra{1_k} \\
      %&+ \abra{\Probe}{\Pauli_x}\aket{\Probe} \aket{1_k}\abra{1_k} \StateCV \aket{0_k}\abra{0_k} \\
      %&+ \aket{1_k}\abra{1_k} \StateCV \aket{1_k}\abra{1_k}.
      = \; & \sum_{n,m=0}^{1} \bra{\Probe}  \Pauli_x^{m} \Pauli_x^n  \ket{\Probe} \cdot \ket{n_k}\bra{n_k}  \StateCV  \ket{m_k}\bra{m_k}.
   \end{aligned}

To show that the measurement is necessarily weak, thereby leaving this evolved state unperturbed for sufficiently small :math:`\Strength`, we first use the definition of our normalized probe state :eq:`eq:probe` to compute

.. math:: \bra{\Probe} \Pauli_x  \ket{\Probe} = \sqrt{1-\Strength^2}.
   :label: eq:probe_overlap

A Taylor series expansion of this lets us write

.. math:: \sqrt{1-\Strength^2} = 1 - \frac{\Strength^2}{2} + \mathcal{O}(\Strength^4),

with which we may express the evolved system :eq:`eq:tomography_evolved_unknown` as

.. math::
   :label: eq:tomography_expansion

   \begin{aligned}
      \StateCV^\prime %=\; & \ket{0_k}\bra{0_k} \StateCV \ket{0_k}\bra{0_k} \\
      %&+ \aket{0_k}\abra{0_k} \StateCV \aket{1_k}\abra{1_k} \\
      %&+ \aket{1_k}\abra{1_k} \StateCV \aket{0_k}\abra{0_k} \\
      %&+ \aket{1_k}\abra{1_k} \StateCV \aket{1_k}\abra{1_k} \\
      %&- \left(\frac{\Strength^2}{2} - \mathcal{O}(\Strength^4)\right) \left[\aket{0_k}\abra{0_k} \StateCV \aket{1_k}\abra{1_k} + \aket{1_k}\abra{1_k} \StateCV \aket{0_k}\abra{0_k}\right] \\
      %=\; & \sum_{n,m=0}^{1} \aket{n_k}\abra{n_k} \StateCV \aket{m_k}\abra{m_k} \\
      %&- \left(\frac{\Strength^2}{2} - \mathcal{O}(\Strength^4)\right) \left[\aket{0_k}\abra{0_k} \StateCV \aket{1_k}\abra{1_k} + \aket{1_k}\abra{1_k} \StateCV \aket{0_k}\abra{0_k}\right] \\
      =\; & \sum_{n,m=0}^{1} \ket{n_k}\bra{n_k}  \StateCV  \ket{m_k}\bra{m_k} + \mathcal{O}(\Strength^2).
   \end{aligned}

By comparing this to our probe density, which can be expanded as

.. math::
   :label: eq:probe_density

   \begin{aligned}
      \ket{\Probe}\bra{\Probe} %&= \Identity + \Strength\Pauli_z + \sqrt{1-\Strength^2}\Pauli_x, \\
      %&= \ket{+}\bra{+} + \Strength\Pauli_z - \left(\frac{\Strength^2}{2} -\mathcal{O}(\Strength^4)\right)\Pauli_x, \\
      &= \ket{+}\bra{+} + \frac{\Strength}{2}\Pauli_z + \mathcal{O}(\Strength^2),
   \end{aligned}

it is easy to see that for sufficiently small :math:`\Strength`, e.g., :math:`\abs{\Strength} \ll 1` such that :math:`\mathcal{O}(\Strength^2) \approx 0`, the system state :eq:`eq:tomography_expansion` approximates its unperturbed form,

.. math::

   \begin{aligned}
      \StateCV^\prime \approx\; & \sum_{n,m=0}^{1} \ket{n_k}\bra{n_k}  \StateCV  \ket{m_k}\bra{m_k} \\
      %=\; & \aket{0_k}\abra{0_k} \StateCV \aket{0_k}\abra{0_k} \\
      %&+ \aket{0_k}\abra{0_k} \StateCV \aket{1_k}\abra{1_k} \\
      %&+ \aket{1_k}\abra{1_k} \StateCV \aket{0_k}\abra{0_k} \\
      %&+ \aket{1_k}\abra{1_k} \StateCV \aket{1_k}\abra{1_k} \\
      =\; & \StateCV,
   \end{aligned}

while the probe :eq:`eq:probe_density`, containing a first-order power of :math:`\Strength`, becomes

.. math:: \ket{\Probe}\bra{\Probe} \approx \ket{+}\bra{+} + \frac{\Strength}{2}\Pauli_z.

This is exactly what we desire, since if the probe were to become exactly an eigenstate of the Pauli-X operator :math:`\Pauli_x`, i.e.,

.. math:: \ket{\pm} \equiv \frac{1}{\sqrt{2}}\bigl(\ket{0} \pm \ket{1}\bigr),

then it would not be perturbed by the CNOT gate in its coupling :eq:`eq:unitary_tomography_weak` with the unknown system state. In other words, it would be unable to provide any information regarding :math:`\StateCV`, and would thus be tomographically useless. As however the probe state :eq:`eq:probe_density` does not assume the form of an eigenstate of :math:`\Pauli_x` while the system remains unperturbed by the interaction (provided :math:`\Strength` is sufficiently small), then we can in principle infer the state of :math:`\StateCV` via strong measurements of the evolved ancilla state :math:`\StateProbe_k` (for all :math:`k`). This is the meaning of a weak measurement, and we call :math:`\Strength` the *strength* of the measurement.

Let us now demonstrate how the qubit system :math:`\StateCV` may be reconstructed by measuring the probe in the :math:`z` basis. Starting with :eq:`eq:tomography_evolution`, we perform a partial trace on the first subsystem to obtain the evolved probe state,

.. math::
   :label: eq:state_probe

   \begin{aligned}
      \StateProbe_k &\equiv \trace_{0}\bigl[\Tomography\bigl(\StateCV\otimes\ket{\Probe}\bra{\Probe}\bigr)\Tomography^\dagger\bigr] \\
      %&= \abra{0_k} \StateCV \aket{0_k} \aket{\Probe}\abra{\Probe} + \abra{1_k} \StateCV \aket{1_k} \Pauli_x\aket{\Probe}\abra{\Probe}\Pauli_x \\
      &= \sum_{n=0}^{1} \bra{n_k}  \StateCV  \ket{n_k} \cdot \Pauli^n_x  \ket{\Probe}\bra{\Probe}  \Pauli_x^{n}.
   \end{aligned}

Computing the expectation value of :math:`\Pauli_z` for this form then yields

.. math::
   :label: eq:tomography_connection

   \begin{aligned}
      \trace\left[\Pauli_z\StateProbe_k\right] &= \bra{0}  \StateProbe_k  \ket{0} - \bra{1}  \StateProbe_k  \ket{1} \\
      &= \Strength \bigl(\bra{0_k}  \StateCV  \ket{0_k} - \bra{1_k}  \StateCV  \ket{1_k}\bigr) \\
      &= \Strength \, \trace\left[\Pauli_k \StateCV\right],
   \end{aligned}

where we used the fact that

.. math:: \Pauli_k = \ket{0_k}\bra{0_k} - \ket{1_k}\bra{1_k}.

Rescaling by a factor :math:`\tfrac{1}{\Strength}` then allows us to make the connection between performing a :math:`z`-basis measurement on the probe state :eq:`eq:state_probe` and inferring the expectation value of :math:`\Pauli_k` for the state of the unknown system. This is because, up to the factor :math:`\Strength`, the two operations are equivalent. Note that, for brevity, we will write

.. math:: \Expectation_k \equiv \frac{1}{\Strength}\trace\left[\Pauli_z\StateProbe_k\right] = \trace\left[\Pauli_k \StateCV\right],
   :label: eq:tomography_expectation

which is often denoted in the literature as :math:`\big<\Pauli_k\big>`.

If we define :math:`\Pauli_0 \equiv \Identity`, then the set of operators :math:`\{\Pauli_k\}_{k=0}^3` forms a complete basis for the space of complex :math:`2 \times 2` matrices. Since this coincides with the space of linear operators :math:`\SpaceLinear(\SpaceHilbert)` on our qubit (:math:`2`-dimensional) Hilbert space :math:`\SpaceHilbert`, then any state :math:`\StateCV \in \SpaceLinear(\SpaceHilbert)` can accordingly be reconstructed via the linear combination,

.. math::
   :label: eq:tomography_reconstruction

    \StateCV = \frac{1}{2}\sum_{k=0}^{3} \trace\left[\Pauli_k \StateCV\right] \Pauli_k.

Since the coefficient for :math:`k = 0` is fixed by normalization (i.e., :math:`\trace\left[\Pauli_0 \tau \right] = 1`), then the state is fully determined by the *Bloch vector*, which is defined, for an :math:`\Dimension`-dimensional state, as the :math:`(\Dimension^2-1)`-dimensional real vector of parameters :math:`\trace\left[\Pauli_k \tau \right]` (for :math:`k \in \Integers_{1}^{\Dimension^2 - 1}`). Accordingly, the linear combination :eq:`eq:tomography_reconstruction` is said to be the *Bloch sphere representation* of the state :math:`\tau`. Thus, since we have shown that we can infer expectation values :eq:`eq:tomography_expectation` for an unknown state by coupling it with a probe via a CNOT and subsequently performing a measurement of the probe in the :math:`z`-basis, then we can characterize the state completely without directly measuring it.

Implementation
--------------

.. literalinclude:: /text/examples/algorithms/tomography_weak.py
   :name: code:tomography_weak
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> tomography.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_algorithms_tomography_weak-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_algorithms_tomography_weak-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> unknown_state.print()
   τ = τ[0, 0]|0⟩⟨0| + τ[0, 1]|0⟩⟨1| + τ[1, 0]|1⟩⟨0| + τ[1, 1]|1⟩⟨1|

.. code:: python

   >>> reconstructed_state.print()
   τ = τ[0, 0]|0⟩⟨0| + τ[0, 1]|0⟩⟨1| + τ[1, 0]|1⟩⟨0| + τ[1, 1]|1⟩⟨1|

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage