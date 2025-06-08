.. include:: /styles.rst

.. _`sec:D-CTCs`:

The Deutsch model (D-CTCs)
==========================

In 1991, David Deutsch introduced a method of analysing the flow of information in a chronology-violating network. This prescription, now known as the *Deutsch model* :cite:p:`deutsch_quantum_1991`, consists of a quantum theory of computation applied to a CTC model where most of the geometry has been abstracted away. It is based on the requirement that time evolution of the local density operator (taken as a fundamental object) of a quantum system must be self-consistent.

One of the main results of Deutsch's work on time travel is his proposal for the time evolution of quantum states through a quantum circuit representation of a chronology-violating network (illustrated in :numref:`fig:circuit_ctc_dctc`), with particular note as to how it resolves time-travel paradoxes and indeterminism.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_dctc-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of Deutsch's model of quantum time travel.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_dctc-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of Deutsch's model of quantum time travel.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_dctc-light.png
   :name: fig:circuit_ctc_dctc
   :scale: 36 %
   :alt: A quantum circuit diagram of Deutsch's model of quantum time travel.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Deutsch's model of quantum time travel.

The mathematical formulation of his self-consistent evolution of a quantum state through a region with a time machine is provided by requiring that any given chronology-violating (CV) system enters the CTC in the state

.. math:: \StateCV \in \SpaceMixed(\SpaceHilbert_\CV),
   :label: eq:state_CV

and then emerges in the past in the same state despite having interacted with a chronology-respecting (CR) system in the state

.. math:: \StateCR \in \SpaceMixed(\SpaceHilbert_\CR)
   :label: eq:state_CR

through a unitary :math:`\Unitary` on :math:`\SpaceHilbert_\CR\otimes\SpaceHilbert_\CV`. The joint density operator entering the gate is simply the tensor product :math:`\StateCR \otimes \StateCV` on :math:`\SpaceHilbert_\CR\otimes\SpaceHilbert_\CV` so that the standard evolution through the unitary is given by

.. math:: \StateCR \otimes \StateCV \rightarrow \MapGeneral_{\Unitary}[\StateCR \otimes \StateCV] = \Unitary(\StateCR \otimes \StateCV)\Unitary^\dagger.
   :label: eq:D-CTCs_evolution

We can now trace the CV and CR subsystems out and denote the resulting maps as

.. math::
   :label: eq:D-CTCs_CV

   \begin{aligned}
       \MapDCTCsCV_{\Unitary}[\StateCR,\StateCV] &\equiv \trace_\CR\bigl[\Unitary(\StateCR \otimes \StateCV)\Unitary^\dagger\bigr],
   \end{aligned}

.. math::
   :label: eq:D-CTCs_CR

   \begin{aligned}
       \MapDCTCsCR_{\Unitary}[\StateCR,\StateCV] &\equiv \trace_\CV\bigl[\Unitary(\StateCR \otimes \StateCV)\Unitary^\dagger\bigr].
   \end{aligned}

Self-consistent solutions of the CTC state may then be identified as fixed points of the CV map :eq:`eq:D-CTCs_CV`, which are expressible via

.. math:: \StateCV = \MapDCTCsCV_{\Unitary}[\StateCR,\StateCV].
   :label: eq:D-CTCs_CTC

This condition essentially codifies the requirement that the "younger" CTC state (the right-hand side) exiting the gate is the same as the "older" CTC state (the left-hand side) entering the gate. Once solutions to equation :eq:`eq:D-CTCs_CTC` are determined, the evolution of the system state :math:`\StateCR` through the interaction :math:`\Unitary` in this Deutsch model is then simply given by the CR map :eq:`eq:D-CTCs_CR`. Deutsch's original construction specifically interprets D-CTCs as being portals between parallel universes---a time traveller on a D-CTC would pass in and out of such universes---and so the quantum states in this context describes a superposition of states where the time traveller does and does not exist.

The fact that the imposed self-consistency constraint in :eq:`eq:D-CTCs_CTC` is a fixed-point condition means that the non-linearity introduced to the laws of quantum mechanics is distinct from that of other models. Furthermore, as the rigid matching requirement is for the density matrix as opposed to the individual states in a pure state decomposition, the Deutsch model intrinsically treats density matrices ontologically as ontic ("real") objects rather than as epistemic knowledge representations.

Deutsch's picture: The rule of maximum entropy
----------------------------------------------

Of crucial significance is the fact that the Deutsch prescription resolves time-travel paradoxes without placing any constraints on the input system state. This is because Deutsch proved that at least one consistent solution of the (normalized) map

.. math::
   :label: eq:D-CTCs_entropy

   \begin{aligned}
       \normalized{\MapDCTCsCV_{\Unitary}^{\infty}}[\StateCR,\StateCV^{(0)}] \equiv \lim_{N\rightarrow\infty}\frac{1}{N+1} \sum_{k=0}^{N}\MapDCTCsCV_{\Unitary}^{k}(\StateCR,\StateCV^{(0)}) 
   \end{aligned}

exists for every unitary :math:`\Unitary` and input :math:`\StateCR`. Here, :math:`\StateCV^{(0)} \in \SpaceLinear(\SpaceHilbert_\CV)` represents some initial CV state, and :math:`\MapDCTCsCV^{k}` denotes :math:`k` compositions of the D-CTC CV map, i.e.,

.. math::
   :label: eq:D-CTCs_CV_compositions

   \begin{aligned}
       \MapDCTCsCV^{k}_{\Unitary}\bigl[\StateCR,\StateCV^{(0)}\bigr] &= (\,\underbrace{\MapDCTCsCV_{\Unitary} \circ \MapDCTCsCV_{\Unitary} \circ \ldots \circ \MapDCTCsCV_{\Unitary}}_{k \text{ times}}\,)\bigl[\StateCR,\StateCV^{(0)}\bigr] \\
       &= \MapDCTCsCV_{\Unitary}\biggl[ \StateCR,\MapDCTCsCV_{\Unitary}\Bigl[ \StateCR,\ldots,\MapDCTCsCV_{\Unitary}\bigl[\StateCR,\StateCV^{(0)}\bigr] \Bigr] \biggr].
   \end{aligned}

Note however that some interactions have a multiplicity of fixed points, which leads to non-determinism in the time evolution. This characteristic, known as the *uniqueness ambiguity* in the context of D-CTCs, may be interpreted as an indication that the theory is incomplete.

To overcome this problem, Deutsch argued that the "correct" solution is the one with the most von Neumann entropy :eq:`eq:entropy`. This proposition appeals to the principles of thermodynamics (the second law in particular), and asserts that the trapped CTC would naturally tend towards a maximally entropic equilibrium state. Given its lack of rigorous theoretical support however, Deutsch's rule of maximum entropy is often considered to be an unsatisfactory approach to overcoming the problem of plurality in the CTC state solution.

.. _`sec:ECP`:

Iterative picture: The equivalent circuit
-----------------------------------------

In 2010, Ralph and Myers introduced their equivalent-circuit picture (ECP) :cite:p:`ralph_information_2010,ralph_reply_2011,pienaar_quantum_2011,ralph_relativistic_2012,dong_ralphs_2017` of the D-CTC model. This approach was formulated as a method of deriving the maximum entropy rule and thus resolving the uniqueness ambiguity. It consists of essentially "unwrapping" the D-CTC time-loop fixed-point circuit (:numref:`fig:circuit_ctc_dctc`) into an infinite sequence of interactions with perfect copies of the input state, and is illustrated in :numref:`fig:circuit_ctc_dctc_ecp`.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_dctc_ecp-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_dctc_ecp-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_dctc_ecp-light.png
   :name: fig:circuit_ctc_dctc_ecp
   :scale: 36 %
   :alt: A quantum circuit diagram of the equivalent-circuit picture of a D-CTC.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The equivalent-circuit picture of a D-CTC.

In this model, the CTC-trapped state :math:`\StateCV^{(n-1)}` enters the :math:`n`\ th interaction :math:`\Unitary` and exits, according to the fixed-point condition :eq:`eq:D-CTCs_CTC`, in the state

.. math:: \StateCV^{(n)} = \MapDCTCsCV_{\Unitary}[\StateCR,\StateCV^{(n-1)}].
   :label: eq:ECP_single

The final output :math:`\StateCV^{(\infty)}` is then obtained by applying this map recursively *ad infinitum* to an initial state :math:`\StateCV^{(0)}`. Accordingly, one finds, in the limit,

.. math:: \StateCV^{(\infty)} = \lim_{N \rightarrow\infty}\MapDCTCsCV_{\Unitary}^{N}[\StateCR,\StateCV^{(0)}]
   :label: eq:ECP_CV

Given this framework, the ECP then introduces an arbitrarily small decoherence interaction :math:`\Decoherence`, parametrized by the decoherence strength :math:`0<\delta\ll1`, to each CTC iteration,

.. math::
   :label: eq:ECP_decoherence

   \begin{aligned}
       \StateCV^{(n)} &= \Decoherence\bigl[\MapDCTCsCV_{\Unitary}[\StateCR,\StateCV^{(n-1)}]\bigr] \\
       &= (1-\delta)\MapDCTCsCV_{\Unitary}[\StateCR,\StateCV^{(n-1)}] + \delta\normalized{\Identity}
   \end{aligned}

where

.. math::

   \begin{aligned}
       \normalized{\Identity} &\equiv \frac{1}{\dim(\SpaceHilbert)}\Identity, \\
       \Identity &\equiv \sum_{i}^{\dim(\SpaceHilbert)}\ket{i}\bra{i} \in \SpaceHilbert,
   \end{aligned}

are the unnormalized and normalized maximally mixed (identity) states, respectively. The corresponding final output is then

.. math:: \StateCV^{(\infty)} = \lim_{N\rightarrow\infty}\left[(1-\delta)^{N}\MapDCTCsCV_{\Unitary}^{N}[\StateCR,\StateCV^{(0)}] + \sum_{k=0}^{N-1}\delta^{k}(1-\delta)^{k}\MapDCTCsCV_{\Unitary}^{k}[\StateCR,\normalized{\Identity}]\right].
   :label: eq:ECP_CV_decoherence

From this result, it can be determined that the non-uniqueness in the solutions to the CV CTC map corresponds to sensitivity to the initial condition :math:`\StateCV^{(0)}`. Ralph and Myers then show that the result of :eq:`eq:ECP_CV_decoherence` converges to the unique solution of Deutsch's maximum entropy rule, and that this rule and result coincides with setting the initial state to be the maximally mixed CTC state :math:`\StateCV^{(0)}=\normalized{\Identity}` in :eq:`eq:ECP_CV`. The appealing feature of this picture is that Deutsch's maximum entropy rule is not merely a postulate of the theory; rather, it is a direct result.

Later, Allen :cite:p:`allen_treating_2014` noticed that the equivalent circuit does not always converge when there is decoherence interaction, and that Ralph and Myers's proof of the derivation of the maximum entropy rule was incomplete. However, Dong :cite:p:`dong_ralphs_2017` then showed that the ECP leads instead to a *revised* maximum entropy rule, one which is distinct from (and perhaps more valid than) Deutsch's original rule. It asserts that, when multiple valid solutions of the CV map exist, the Deutsch model "chooses" the *stable* fixed-point state with the most entropy (as determined by the equivalent model with a decoherence interaction). Additionally, note that the final fixed point as given by this revised rule is in general dependent on the decoherence strength (:math:`\delta`).

.. _`sec:Allen`:

Allen's picture: Noise incorporation
------------------------------------

In 2014, Allen :cite:p:`allen_treating_2014` proposed a different method of resolving the uniqueness ambiguity. It consists of the incorporation of noise into the CV channel via a noise channel :math:`\Depolarization` with depolarization parameter :math:`0<\nu<1`, which is accomplished by

.. math::
   :label: eq:depolarization

   \begin{aligned}
       \StateCV &= \Depolarization\bigl[\MapDCTCsCV_{\Unitary}[\StateCR,\StateCV]\bigr] \\
       &= (1-\nu)\MapDCTCsCV_{\Unitary}[\StateCR,\StateCV] + \nu\normalized{\Identity}.
   \end{aligned}

Allen then proves that this addition resolves the uniqueness ambiguity without requiring a maximum entropy rule, and that the unique fixed-point CTC state is :math:`\StateCV^{(0)}`-independent and given by

.. math::
   :label: eq:Allen

   \begin{aligned}
       \normalized{\Depolarization[\MapDCTCsCV_{\Unitary}^{\infty}]}(\StateCR) = \lim_{N\rightarrow\infty}\frac{1}{N+1} \sum_{k=0}^{N}\Depolarization\bigl[\MapDCTCsCV_{\Unitary}^{k}[\StateCR,\StateCV^{(0)}]\bigr].
   \end{aligned}

Given that :math:`\Depolarization` is a noise channel, then it should be *strictly contractive* (that is, its trace distance should always decrease under its action), leaving :eq:`eq:Allen` unique. Dong :cite:p:`dong_ralphs_2017` then show that Allen's picture is inequivalent to both Deutsch's and Ralph and Myers's pictures.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
