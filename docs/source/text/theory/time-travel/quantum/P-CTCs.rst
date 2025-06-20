.. include:: /styles.rst

.. _`sec:P-CTCs`:

Postselected teleportation (P-CTCs)
===================================

The other main prescription of the quantum mechanics of time travel, *postselected teleportation* (P-CTCs) :cite:p:`lloyd_quantum_2011,lloyd_closed_2011` (based on unpublished work in :cite:p:`bennett_simulated_2005`, and also due independently to :cite:p:`svetlichny_effective_2009` as discussed in :cite:p:`svetlichny_time_2011`), also provides self-consistent resolutions to general time-travel paradoxes. P-CTCs are motivated as mechanisms for facilitating the quantum teleportation of quantum systems to the past :cite:p:`bennett_simulated_2005`. The contemporary mathematical description of the prescription is based upon postselection, and essentially consists of a quantum communication channel that is formed through teleportation.

The CV (CTC) quantum channel is replaced with a maximally entangled state :math:`\ket{\Bell}` (i.e., a Bell state for qubits), allowing for states to be transported between a sender and receiver through shared entanglement. Quantum teleportation further combined with postselection results in a quantum channel to the past. Antichronological time travel then manifests due to the entanglement between the forward and backward parts of the curve, and one thus obtains a possible theoretical description of quantum mechanics near CTCs. Note that the replacement of the CTC channel with the postselection of a maximally entangled state is equivalent to a path-integral formulation (developed in :cite:p:`politzer_path_1994`) in which the CTC state's wave function evolves in accordance with self-consistent boundary conditions (specifically, the initial and final coordinates are the same). This is why we say that P-CTCs has the important feature of being equivalent to the path-integral formulation of quantum mechanics. Here, we demonstrate the model.

The path-integral formulation in the presence of CTCs
-----------------------------------------------------

The path-integral formulation of quantum mechanics allows us to formulate the transition amplitude for a quantum system which evolves from an initial state :math:`\ket{\WaveFunctionInitial}` to a final state :math:`\ket{\WaveFunctionFinal}` as an integral over the paths of the action. In one spatial dimension :math:`\Position(\Time)`, we may simply write

.. math:: \bra{\WaveFunctionFinal}\Unitary(\TimeFinal,\TimeInitial)\ket{\WaveFunctionInitial} = \iint\diff{\PositionInitial}\,\diff{\PositionFinal} \, \WaveFunctionInitial(\PositionInitial) \conj{\WaveFunctionFinal}{(\PositionFinal)}\int_{\PositionInitial}^{\PositionFinal} \DifferentialPath^{\prime}\Position \, \e^{\eye \Action[\Position]/\hbar}.
   :label: eq:path_amplitude

Here, :math:`\Unitary(\TimeFinal,\TimeInitial)` is the time-evolution operator that describes the state evolution from initial time :math:`\TimeInitial` to final time :math:`\TimeFinal`,

.. math::

   \begin{aligned}
       \Position(\TimeInitial) &\equiv \PositionInitial, \\
       \Position(\TimeFinal) &\equiv \PositionFinal,
   \end{aligned}

are the initial and final coordinates respectively,

.. math::

   \begin{aligned}
       \ket{\WaveFunctionInitial} &= \int \diff{\PositionInitial} \, \WaveFunctionInitial(\PositionInitial)\ket{\PositionInitial}, \\
       \ket{\WaveFunctionFinal} &= \int \diff{\PositionFinal} \, \WaveFunctionFinal(\PositionFinal)\ket{\PositionFinal},
   \end{aligned}

are the position representations of the initial and final states, and

.. math:: \Action[\Position] \equiv \int_{\TimeInitial}^{\TimeFinal} \Lagrangian\bigl(\Time,\Position(\Time),\dot{\Position}(\Time)\bigr) \, \diff{\Time},

is the action of path :math:`\Position(\Time)` with Lagrangian :math:`\Lagrangian\bigl(\Time,\Position(\Time),\dot{\Position}(\Time)\bigr)`.

To incorporate a CTC into the path-integral formulation, we first divide the spacetime into two parts, or more formally, two separate systems: a CR system :math:`\ket{\WaveFunction}\in\SpaceHilbert_\CR` and a CV system :math:`\ket{\WaveFunctionCTC}\in\SpaceHilbert_\CV`. Let their position-space representations be parametrized by the coordinates :math:`u` and :math:`v` respectively, so that the initial and final position representations are

.. math::

   \begin{aligned}
       \ket{\WaveFunctionInitial} &= \int \diff{u^{\prime}} \, \WaveFunctionInitial(u^{\prime})\ket{u^{\prime}} \quad &\rightarrow \quad \ket{\WaveFunctionFinal} &= \int \diff{u^{\prime\prime}} \, \WaveFunctionInitial(u^{\prime\prime})\ket{u^{\prime\prime}}, \\
       \ket{\WaveFunctionCTCInitial} &= \int \diff{v^{\prime}} \, \WaveFunctionCTCInitial(v^{\prime})\ket{v^{\prime}} \quad &\rightarrow \quad \ket{\WaveFunctionCTCFinal} &= \int \diff{v^{\prime\prime}} \,\WaveFunctionCTCInitial(v^{\prime\prime})\ket{v^{\prime\prime}}.
   \end{aligned}

This means that, with time-evolution unitary :math:`\Unitary(\TimeInitial,\TimeFinal)` on :math:`\SpaceHilbert_\CR\otimes\SpaceHilbert_\CV`, the joint input state evolves as per :math:`\ket{\WaveFunctionInitial}\otimes\ket{\WaveFunctionCTCInitial} \rightarrow \ket{\WaveFunctionFinal}\otimes\ket{\WaveFunctionCTCFinal}` over the spatial coordinates :math:`(u^{\prime},v^{\prime})\rightarrow(u^{\prime\prime},v^{\prime\prime})`. Using equation :eq:`eq:path_amplitude`, this evolution has a corresponding path-integral representation of

.. math::
   :label: eq:path_amplitude_split

   \begin{aligned}
       (\bra{\WaveFunctionFinal}\otimes\bra{\WaveFunctionCTCFinal})\Unitary(\TimeFinal,\TimeInitial)(\ket{\WaveFunctionInitial}\otimes\ket{\WaveFunctionCTCInitial}) &= \iiiint\diff{u^{\prime}}\,\diff{u^{\prime\prime}}\,\diff{v^{\prime}}\,\diff{v^{\prime\prime}} \, \WaveFunctionInitial(u^{\prime}) \conj{\WaveFunctionFinal}{(u^{\prime\prime})}\WaveFunctionCTCInitial(v^{\prime}) \conj{\WaveFunctionCTCFinal}{(v^{\prime\prime})} \int_{(u^{\prime},v^{\prime})}^{(u^{\prime\prime},v^{\prime\prime})} \DifferentialPath^{\prime}\Position \, \e^{\eye \Action[\Position]/\hbar}.
   \end{aligned}

Now, to include a CTC in this scheme, we mandate that the initial and final coordinates for the chronology-violating system are the same, just like in a CTC. Mathematically, we impose the boundary condition :math:`v^{\prime}=v^{\prime\prime}` a :math:`\delta`-function in :eq:`eq:path_amplitude_split`, and the resulting transition amplitude for the chronology-respecting system with an incorporated CTC may be written as

.. math:: (\bra{\WaveFunctionFinal}\otimes\Identity)\Unitary(\TimeFinal,\TimeInitial)(\ket{\WaveFunctionInitial}\otimes\Identity) = \iiiint\diff{u^{\prime}}\,\diff{u^{\prime\prime}}\,\diff{v^{\prime}}\,\diff{v^{\prime\prime}} \, \WaveFunctionInitial(u^{\prime}) \conj{\WaveFunctionFinal}{(u^{\prime\prime})} \delta(v^{\prime}-v^{\prime\prime}) \int_{(u^{\prime},v^{\prime})}^{(u^{\prime\prime},v^{\prime\prime})} \DifferentialPath^{\prime}\Position \, \e^{\eye \Action[\Position]/\hbar}.
   :label: eq:P-CTCs_path

The coherent addition of all possible initial and final conditions for the CTC is captured through the :math:`v^{\prime}` and :math:`v^{\prime\prime}` integrals, hence the removal of the CTC states :math:`\ket{\WaveFunctionCTCInitial}` and :math:`\ket{\WaveFunctionCTCFinal}`. This indicates that it is not possible to assign a state to the CTC system (at least in this context), which in turn means that compatibility with the boundary conditions implies that the CR system is not in a forbidden state.

Equivalence of CTC path integrals and postselected teleportation
----------------------------------------------------------------

Given the form :eq:`eq:P-CTCs_path` of the transition amplitude obtained using path-integral methods, we now wish to show that it is equal to the form which one obtains from postselected teleportation methods. To do this, let us first define our maximally entangled bipartite state of choice :math:`\ket{\Bell}\in\SpaceHilbert_\CV\otimes\SpaceHilbert_\Teleportation` in a :math:`w`-space representation as

.. math:: \ket{\Bell} = \int \diff{w} \, \Bell(w) \, \ket{w}\otimes\ket{w}
   :label: eq:Bell_continuous

where we assume that :math:`\Bell(w)` satisfies the normalization condition

.. math:: 1 = \braket{\Bell}{\Bell} = \int \diff{w}\, \abs{\Bell(w)}^2.

Furthermore, note how :eq:`eq:Bell_continuous` can be put in a more useful form by using a :math:`\delta`-function,

.. math:: \ket{\Bell} = \iint \diff{v}\,\diff{w} \, \Bell(v,w)\delta(v-w) \ket{v}\otimes\ket{w}.
   :label: eq:Bell_continuous_delta

From here, we replace the CV state :math:`\ket{\WaveFunctionCTC}` with the maximally entangled :math:`\ket{\Bell}`, thereby meaning that our input state :math:`\ket{\WaveFunctionInitial}\otimes\ket{\WaveFunctionCTCInitial}` evolves under a transformation described by the composition :math:`\Unitary(\TimeFinal,\TimeInitial)\otimes\Identity`. To clarify, the time-evolution operator :math:`\Unitary` only acts on the :math:`\SpaceHilbert_\CR` (CR) and :math:`\SpaceHilbert_\CV` (CV) Hilbert spaces while the identity :math:`\Identity` acts on the third (teleportation) Hilbert space :math:`\SpaceHilbert_\Teleportation`. With this, we then postselect on the output being in the state :math:`\ket{\WaveFunctionFinal}\otimes\ket{\Bell}`, which physically represents the teleportation Hilbert space :math:`\SpaceHilbert_\Teleportation` being used to send this conditional selection back in time, thereby yielding the necessary postselected teleportation. This entire sequence can be formulated by replacing the CTC state in :eq:`eq:path_amplitude_split` with our maximally entangled state :eq:`eq:Bell_continuous_delta`, which yields

.. math::
   :label: eq:P-CTCs_postselection

   \begin{aligned}
       (\bra{\WaveFunctionFinal}\otimes\bra{\Bell})(\Unitary(\TimeFinal,\TimeInitial)\otimes\Identity)(\ket{\WaveFunctionInitial}\otimes\ket{\Bell}) &= \iint \diff{v^{\prime\prime}}\,\diff{w^{\prime\prime}}\,\conj{\Bell}{(v^{\prime\prime},w^{\prime\prime})}\delta(v^{\prime\prime}-w^{\prime\prime})(\bra{\WaveFunctionFinal}\otimes\bra{v^{\prime\prime}}\otimes\bra{w^{\prime\prime}}) \\
       &\quad\times(\Unitary(\TimeFinal,\TimeInitial)\otimes\Identity)\\
       &\quad\times\iint \diff{v^{\prime}}\,\diff{w^{\prime}}\,\Bell(v^{\prime},w^{\prime})\delta(v^{\prime}-w^{\prime})(\ket{\WaveFunctionInitial}\otimes\ket{v^{\prime}}\otimes\ket{w^{\prime}})\\
       &= \iiiint \diff{v^{\prime}}\,\diff{v^{\prime\prime}}\,\diff{w^{\prime}}\,\diff{w^{\prime\prime}}\,\Bell(v^{\prime},w^{\prime})\conj{\Bell}{(v^{\prime\prime},w^{\prime\prime})}\delta(v^{\prime}-w^{\prime})\delta(v^{\prime\prime}-w^{\prime\prime}) \\
       &\quad\times(\bra{\WaveFunctionFinal}\otimes\bra{v^{\prime\prime}}\otimes\bra{w^{\prime\prime}})(\Unitary^{\prime}(\TimeFinal,\TimeInitial)\otimes\Identity)(\ket{\WaveFunctionInitial}\otimes\ket{v^{\prime}}\otimes\ket{w^{\prime}})\\
       &= \iiiint \diff{v^{\prime}}\,\diff{v^{\prime\prime}}\,\diff{w^{\prime}}\,\diff{w^{\prime\prime}}\,\Bell(v^{\prime},w^{\prime})\conj{\Bell}{(v^{\prime\prime},w^{\prime\prime})}\delta(v^{\prime}-w^{\prime})\delta(v^{\prime\prime}-w^{\prime\prime}) \\
       &\quad\times\iint \diff{u^{\prime}}\,\diff{u^{\prime\prime}}\, \WaveFunctionInitial(u^{\prime})\conj{\WaveFunctionFinal}{(u^{\prime\prime})}\int_{(u^{\prime},v^{\prime})}^{(u^{\prime\prime},v^{\prime\prime})} \DifferentialPath^{\prime}\Position \, \e^{\eye \Action[\Position]/\hbar} \cdot \underbrace{\bra{w^{\prime\prime}}\Identity\ket{w^{\prime}}}_{=\delta(w^{\prime\prime}-w^{\prime})} \\
       &= \iiint \diff{v^{\prime}}\,\diff{v^{\prime\prime}}\,\diff{w^{\prime}}\,\Bell(v^{\prime},w^{\prime})\conj{\Bell}{(v^{\prime\prime},w^{\prime})}\delta(v^{\prime}-w^{\prime})\delta(v^{\prime\prime}-w^{\prime}) \\
       &\quad\times\iint \diff{u^{\prime}}\,\diff{u^{\prime\prime}}\, \WaveFunctionInitial(u^{\prime})\conj{\WaveFunctionFinal}{(u^{\prime\prime})}\int_{(u^{\prime},v^{\prime})}^{(u^{\prime\prime},v^{\prime\prime})} \DifferentialPath^{\prime}\Position \, \e^{\eye \Action[\Position]/\hbar} \\
       &= \iint \diff{v^{\prime}}\,\diff{v^{\prime\prime}}\,\Bell(v^{\prime})\conj{\Bell}{(v^{\prime\prime})}\delta(v^{\prime}-v^{\prime\prime}) \\
       &\quad\times\iint \diff{u^{\prime}}\,\diff{u^{\prime\prime}}\, \WaveFunctionInitial(u^{\prime})\conj{\WaveFunctionFinal}{(u^{\prime\prime})}\int_{(u^{\prime},v^{\prime})}^{(u^{\prime\prime},v^{\prime\prime})} \DifferentialPath^{\prime}\Position \, \e^{\eye \Action[\Position]/\hbar} \\
       &= \iiiint \diff{u^{\prime}}\,\diff{u^{\prime\prime}}\,\diff{v^{\prime}}\,\diff{v^{\prime\prime}}\,\WaveFunctionInitial(u^{\prime})\conj{\WaveFunctionFinal}{(u^{\prime\prime})}\delta(v^{\prime}-v^{\prime\prime}) \\
       &\quad\times\int_{(u^{\prime},v^{\prime})}^{(u^{\prime\prime},v^{\prime\prime})} \DifferentialPath^{\prime}\Position \, \e^{\eye \Action[\Position]/\hbar}.
   \end{aligned}

Thus, we can see that the path-integral formulation :eq:`eq:P-CTCs_path` is equivalent to postselection :eq:`eq:P-CTCs_postselection`, that is,

.. math:: (\bra{\WaveFunctionFinal}\otimes\Identity)\Unitary(\TimeFinal,\TimeInitial)(\ket{\WaveFunctionInitial}\otimes\Identity) = (\bra{\WaveFunctionFinal}\otimes\bra{\Bell})(\Unitary(\TimeFinal,\TimeInitial)\otimes\Identity)(\ket{\WaveFunctionInitial}\otimes\ket{\Bell}).

Of course, being based on the path-integral formulation, these quantities are in general not normalized, and so must be renormalized in order to ensure that the probabilistic interpretation of the theory remains intact.

General form of P-CTC system evolution
--------------------------------------

Here we show how a CR system state :math:`\StateCR\in\SpaceHilbert_\CR` in the Dirac bra-ket formalism evolves through the postselected teleportation chronology-violating network depicted in :numref:`fig:circuit_ctc_pctc`.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_pctc-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the postselected teleportation model of quantum time travel.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_pctc-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the postselected teleportation model of quantum time travel.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_pctc-light.png
   :name: fig:circuit_ctc_pctc
   :scale: 36 %
   :alt: A quantum circuit diagram of the postselected teleportation model of quantum time travel.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The postselected teleportation model of quantum time travel.

In the P-CTCs formalism, self-consistent resolutions to quantum time-travel paradoxes are provided by way of quantum teleportation. This is achieved by first introducing a teleportation system to the pre-existing CR and CV pair. On the CV and teleportation modes, a maximally entangled state :math:`\ket{\Bell} \in \SpacePure(\SpaceHilbert_\CV \otimes \SpaceHilbert_\Teleportation)` is placed (preselected). Here, :math:`\SpaceHilbert_\Teleportation` is the Hilbert space of the teleportation system. With this, the evolution of the product input state :math:`\StateCR \otimes \ket{\Bell}\bra{\Bell}` under the unitary :math:`\Unitary \otimes \Identity` is simply

.. math:: \StateCR \otimes \ket{\Bell}\bra{\Bell} \rightarrow \MapGeneral_{\Unitary \otimes \Identity}[\StateCR \otimes \ket{\Bell}\bra{\Bell}] = \bigl(\Unitary \otimes \Identity\bigr)\bigl(\StateCR \otimes \ket{\Bell}\bra{\Bell}\bigr)\bigl(\Unitary^\dagger \otimes \Identity\bigr).
   :label: eq:P-CTCs_evolved

In accordance with the protocol of quantum teleportation, subsequent postselection against the same entangled state results in a quantum channel to the past (on the system :math:`\SpaceHilbert_\Teleportation`). Mathematically, the evolved CR state becomes

.. math::
   :label: eq:P-CTCs_CR_unnormalized

   \begin{aligned}
       \MapPCTCsCR_{\Unitary}[\StateCR] &\propto \bigl(\Identity \otimes \bra{\Bell}\bigr)\bigl(\Unitary \otimes \Identity\bigr)\bigl(\StateCR \otimes \ket{\Bell}\bra{\Bell}\bigr)\bigl(\Unitary^\dagger \otimes \Identity\bigr)\bigl(\Identity \otimes \ket{\Bell}\bigr) \\
       &= \trace_\CV[\Unitary]\,\StateCR\,\trace_\CV[\Unitary^\dagger],
   \end{aligned}

where we computed

.. math:: \bigl(\Identity \otimes \bra{\Bell}\bigr)\bigl(\Unitary \otimes \Identity\bigr)\bigl(\Identity \otimes \ket{\Bell}\bigr) \propto \trace_\CV[\Unitary].

The P-CTCs evolution of the input state :math:`\StateCR` is then given by the renormalized form of the non-unitary map :eq:`eq:P-CTCs_CR_unnormalized`, that is,

.. math:: \MapPCTCsCR_{\Unitary}[\StateCR] = \frac{\OperatorPCTC \StateCR \OperatorPCTC^\dagger}{\trace[ \OperatorPCTC \StateCR \OperatorPCTC^\dagger]}.
   :label: eq:P-CTCs_CR

where we defined the P-CTC operator

.. math:: \OperatorPCTC \equiv \trace_\CV[\Unitary].
   :label: eq:P-CTCs_operator

In the case of a pure CR input state :math:`\StateCR = \ket{\StatePure}\bra{\StatePure}`, the associated P-CTC CR map on the corresponding vector state is simply

.. math:: \MapPCTCsCR_{\Unitary}\bigl[\ket{\StatePure}\bigr] = \frac{\OperatorPCTC \ket{\StatePure}}{\sqrt{ \bigl| \bigl| \OperatorPCTC \ket{\StatePure} \bigr| \bigr|}}.
   :label: eq:P-CTCs_CR_pure

As each :math:`\StateCR` is mapped onto a specific :math:`\MapPCTCsCR_{\Unitary}[\StateCR]` by :eq:`eq:P-CTCs_CR`, P-CTCs do not suffer from uniqueness ambiguities, unlike D-CTCs. An important point to note however is that because :eq:`eq:P-CTCs_operator` is not in general unitary, the theory must be renormalized, which preserves its probabilistic interpretation at the cost of linearity.

Determination of the P-CTC CV state
-----------------------------------

A striking observation in a comparison of D-CTCs and P-CTCs is the sheer incompatibility between them. Of their many differences, perhaps the most perplexing of all is that one cannot assign a state to the system on the P-CTC :cite:p:`lloyd_quantum_2011`, while the determinability of the state on the D-CTC is crucial to the success of the theory. For the former, provided all boundary conditions in the path-integral picture :cite:p:`politzer_path_1994` are satisfied by the CV state (residing on the P-CTC), then the ability of the P-CTC prescription to resolve any given time-travel paradox is entirely independent of, and agnostic to, this state. The D-CTC model on the other hand relies fundamentally on the CV state being definable, as it is upon this object which the notion of temporal self-consistency is imposed, with the CR output state being directly dependent on it.

Although the state on the P-CTC is ordinarily unassignable, the P-CTC itself is the conduit by which information is necessarily transported to the past. In principle, this means that some CV state exists physically, and so must admit a definite form. It is therefore natural to ponder exactly what state the quantum system on the P-CTC assumes for any given scenario. A methodology which provides the ability to investigate the CV states in quantum prescriptions of time travel would therefore be both useful and enlightening.

To solve this problem, one might think of employing the well-established technique of *quantum state tomography* :cite:p:`james_measurement_2001, thew_qudit_2002, mauro_dariano_quantum_2003, dariano_2_2004, nielsen_quantum_2010`. This essentially consists of the determination of an unknown quantum state by measuring it with respect to all elements of an appropriate *tomographically* or *informationally* complete basis (set of observables). Examples of such bases include the Pauli matrices (plus the identity matrix) :eq:`eq:Pauli` for qubits, and the Gell-Mann matrices (also with the identity) :eq:`eq:Gell-Mann` for qutrits. Once the unknown state (or rather, an ensemble of identically prepared quantum states) has been measured exhaustively in a suitable basis, the resulting statistics (i.e., expectation values) enable the determination of the Bloch vector via :eq:`eq:matrix_qudit`, which is equivalent to precise identification of the associated (and previously unknown) state.

At first glance, this could conceivably allow for the determination of the state of the time-travelling (CV) system in any given quantum prescription of antichronological time travel. A problem with this methodology however is its incompatibility with the requirement of resolving the state without simultaneously disturbing it (i.e., collapsing the wave function). Such a feature is essential, as an ordinary ("strong") measurement would necessarily disturb the CV state, thereby disrupting the relevant self-consistency condition(s) in any given quantum formulation of CTCs (like D-CTCs and P-CTCs). Therefore, in order to measure the state on the CTC without (significantly) perturbing the system, one can use so-called *weak measurements* :cite:p:`aharonov_quantum_2005, aharonov_how_1988, peres_quantum_1989, leggett_comment_1989, aharonov_aharonov_1989, duck_sense_1989, aharonov_properties_1990, knight_weak_1990, story_weak_1991, johansen_weak_2004, vaidman_weak_2009, wu_weak_2009, kedem_modular_2010, wu_weak_2011, nakamura_evaluation_2012, lundeen_procedure_2012, pang_weak_2012, kofman_nonperturbative_2012`, that is, quantum measurements which minimize disturbance by leaving the measured state unaffected (to first order). This technique and its findings were first presented in :cite:p:`bishop_quantum_2025`.

Using this methodology, it is possible to rigorously assign a state to the system on the P-CTC, with such a state taking the form

.. math:: \MapPCTCsCV_{\Unitary}[\StateCR] \equiv \trace_\CR\bigl[\Unitary(\StateCR \otimes \tfrac{1}{2}\Identity)\Unitary^\dagger\bigr].
   :label: eq:P-CTCs_CV

In contrast to its D-CTC counterpart, this state can be computed, and is in fact also unique, for *every* given combination of interaction :math:`\Unitary` and input state :math:`\StateCR`. Another interesting observation is that it is exactly equivalent to the CV output state from the first iteration of a maximally mixed seed state in the D-CTC ECP :ref:`sec:ECP`. In essence, this means that a P-CTC can be thought of as being somewhat like a "partial" D-CTC---one in which the self-consistency condition is not fully realized (at least according to D-CTCs). This is curious result, as it suggests that despite their striking differences, the distinct notions of self-consistency that underpin both P-CTCs and D-CTCs may be more similar than originally thought.

An important point to note is that the result :eq:`eq:P-CTCs_CV` is applicable only to :math:`2`-dimensional (qubit) systems, and that a similar expression for :math:`\Dimension`-dimensional (qudit) systems has yet to be determined analytically. One such candidate however is the natural generalization

.. math:: \MapPCTCsCV_{\Unitary}[\StateCR] \equiv \trace_\CR\bigl[\Unitary(\StateCR \otimes \tfrac{1}{\Dimension}\Identity)\Unitary^\dagger\bigr].

It is important to reiterate that while this expression may seem perfectly reasonable, its validity as the P-CTC CV state has not been proven. While likely highly non-trivial, it is expected however that such generalization is an entirely possible task. Therefore, an interesting next step would be to study the application of the weak-measurement tomography scheme to :math:`\Dimension`-level (qudit) systems, as such work should provide more insight into the generality of the methodology and its results.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
