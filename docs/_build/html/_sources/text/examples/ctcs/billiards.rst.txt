.. _`eg:billiards`:

Billiard-ball paradox
=====================

Description
-----------

In this example, a quantum model of the billiard-ball paradox (see :ref:`sec:billiards`) is studied, with the analysis closely following the work in :cite:p:`bishop_time-traveling_2021`. The basic idea is as follows:

i. We consider a simplified :math:`(1+1)`-dimensional version of the classical problem (see :numref:`fig:diagram_billiard-ball_paradox`) in which, by virtue of the spacetime dimensionality and geometry of the CTC-wormhole, there are *only* two possible classical paths.
ii. This problem is mapped to a quantum circuit representation and we use a vacuum state to allow the particles to be present or absent from particular paths.
iii. An internal degree of freedom that operates like a clock is included into the particle's quantum description, meaning that a measurement of the clock's final state can reveal its path's proper time and therefore which of the two classical alternatives was realized.
    
It is emphasized that the scenario presented here being effectively :math:`(1+1)`-dimensional [point (i)] is not a characteristic specified by Friedman et al. in their original study :cite:p:`friedman_cauchy_1990`, but is part of the modelling of the paradox. In addition, the model is based upon two distinct mechanisms. The first of these [point (ii)] involves the introduction of a "vacuum" state: by considering such a state to represent the absence of a billiard ball, we can use it to allow the associated clock to either travel unperturbed (if there is nothing, i.e., a vacuum, in the CTC) or otherwise be scattered into the CTC (if the billiard ball's future self is trapped inside the CTC). The second mechanism [point (iii)] of the model consists of an internal degree of freedom which is incorporated into the billiard ball's quantum description. Using this modification, we can measure the proper time of the model's distinct classical evolutions, which is to say that the billiard ball effectively functions like a clock. This allows us to operationally extract which-way information, i.e., determine which history the billiard ball experienced. This is necessary to give operational meaning to the probabilities associated with the two classical paths, which are indistinguishable by position measurements alone.

It is important to reiterate that it is only the functionality of the clock which makes the two evolutions of the billiard-ball paradox distinguishable. In the Friedman et al. conjecture :cite:p:`friedman_cauchy_1990`, the use of a semiclassical sum-over-histories approach is only meaningful when the evolutions :math:`\EvolutionNoninteracting` and :math:`\EvolutionInteracting` are treated distinctly *a priori*. This enables one to assign evolution probabilities without the need for conventional which-way information. It should be stressed that Friedman et al. do not provide an operational prescription on how to associate paths with probability, which is the reason why we employ a quantum clock.

One of the open questions in the study of the quantum mechanics of time travel that can be investigated using this model is whether a quantum description does indeed address the issue of evolution indeterminism. As we shall see, a parametrization of the solutions in the D-CTCs description is observed. Although usually interpreted as solution multiplicity, this arises naturally as a choice of initial state in the CTC. Alternatively, in P-CTCs, only one quantum state is offered by the prescription as a solution to the paradox. This state takes the form of a pure superposition of the clock having evolved and not evolved on the CTC during its history through the time machine region. A focus of these P-CTC findings is how this superposition lends credence to the semiclassical billiard-ball conjecture of Friedman et al. in :cite:p:`friedman_cauchy_1990`. The well-known problem of how P-CTCs place constraints on the initial data (where such restrictions depend on the future of the time-travelling state), and how this limits the actions that one is able to perform in the billiard-ball interaction, is also discussed.

.. only:: html

   .. figure:: /figures/output/diagram_billiard-ball_clocks-dark.png
      :scale: 36 %
      :alt: A spatial diagram of the simplified billiard-ball paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/diagram_billiard-ball_clocks-light.png
      :scale: 36 %
      :alt: A spatial diagram of the simplified billiard-ball paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/diagram_billiard-ball_clocks-light.png
   :name: fig:diagram_billiard-ball_clocks
   :scale: 36 %
   :alt: A spatial diagram of the simplified billiard-ball paradox.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A simplified, :math:`(1+1)`-dimensional version of the billiard-ball paradox (:numref:`fig:diagram_billiard-ball_paradox`). This diagram visualizes the basic idea of the model under study in the reference frame of the clock. (a) The history where the clock travels through the CTC-wormhole region with no interaction; (b) the history of a clock which elastically interacts with itself. The times as measured by the clock at specific points along the histories are given in brackets next to their analogue clock symbols. The clocks begin at time :math:`\Time=0` and, due to their initial velocity, measure the proper times :math:`\Time_\EvolutionNoninteracting=\TimeInbound+\TimeOutbound` and :math:`\Time_\EvolutionInteracting=\TimeInbound+\TimeDelta+\TimeOutbound = \Time_\EvolutionNoninteracting + \TimeDelta` for evolutions :math:`\EvolutionNoninteracting` and :math:`\EvolutionInteracting`, respectively. This means that we denote the duration of the segment on the CTC in evolution :math:`\EvolutionInteracting` to be :math:`\TimeDelta`, while the inbound and outbound times to and from the wormhole axis (dashed line) are :math:`\TimeInbound` and :math:`\TimeOutbound`, respectively. It is important to note that the final position bears no information about the path the ball has taken.

Model
^^^^^

A quantum "billiard ball" can be modelled simply as a quantum particle, described by a qudit state, that moves though a :math:`(1+1)`-dimensional spacetime. For the billiard-ball paradox, such a spacetime consists of a time-machine wormhole, the mouths of which appear and disappear in such a way as to allow only the two desired paths (see :numref:`fig:diagram_billiard-ball_clocks`). We use the quantum billiard ball's qudit degree of freedom to encode a "clock", as described in the subsequent section. It is important to note that the particle's position degree of freedom begins as a semiclassical wave packet, with negligible probability that it falls into the time machine by its own free evolution. This is a significant point, as it allows us to justify both dropping position from the particle's description and the consideration of only the two trajectories :math:`\EvolutionNoninteracting` and :math:`\EvolutionInteracting`. It also connects with the WKB approximation mentioned by Friedman et al., who propose to apply the sum-over-histories only to the semiclassical trajectories (thus excluding trajectories which pass into the time machine without collision).

For simplicity and rigour, we work in :math:`(1+1)`-dimensions, which means the only interaction that can occur between the billiard-ball clock's future and past selves is a complete exchange of momentum. This is a useful characteristic, as a quantum SWAP gate between two qudit systems perfectly replicates this action within the quantum circuit framework. Additionally, to allow the billiard-ball paradox for the clock to function as intended, we also require the time machine to be dynamic. This means that, at least in the geometrical picture, the mouths of the wormhole appear and disappear at exactly the right points in the spacetime to allow the clock to evolve in two distinct ways within the chronology-violating region.

It is also important to note that in practice, the methods discussed in :ref:`sec:wormholes` are likely incapable of constructing a time machine precisely to this required specification. However, as the physical origin of this time machine is not relevant to the quantum mechanics of the problem at hand, we simply do not concern ourselves with such details. We therefore proceed under the assumption that CTCs exactly satisfying our conditions may not strictly be physically realizable, but it is nevertheless the consequences of their existence, not their existence itself, in which we are interested. In addition to this, it is important to note that, due to our abstracting the geometry of the problem away, the findings from this quantum model are independent of the specific kind of CTC (such as those in, e.g., the wormhole-based time machine, the Gödel universe, the Kerr solution, etc.) employed to facilitate the requisite time-travel mechanism. In the billiard-ball paradox's original, motivating formulation (:ref:`sec:billiards`), the CTCs are generated specifically by a wormhole-based time machine, but this fact has no consequence in our abstract, quantum formulation of the paradox---the time-travel trajectories in the quantum picture are CTCs in perhaps the purest sense of the concept---and so any CTC possessing the necessary characteristics will suffice.

In any case, the resulting non-collisional evolution :math:`\EvolutionNoninteracting` from this specification of the time machine is trivial: the particle remains stationary as the past wormhole mouth appears and disappears behind it, while the future mouth later appears and disappears in front of the particle. Nothing passes in or out of the time machine. On the other hand, in the collisional evolution :math:`\EvolutionInteracting`, a moving particle emerges from the appearing past mouth and strikes the stationary particle, transferring all of its momentum to it. The struck particle then travels into the future mouth that appears directly in front of it, while the other particle becomes stationary and remains so in place of its collision partner. While these trajectories are classical, the particle can be in superpositions of being absent or present on either path. It is stressed that the particle's position degree of freedom factors out of the evolution because the two classical trajectories coincide in final position and velocity. Therefore, the only relevant degrees of freedom are the internal states of the clock.

It is also important to note that the incoming past and outgoing future momenta of the billiard-ball clock must exactly match. Assuming a perfectly elastic collision, the combination of the dynamical time machine and the law of conservation of momentum collectively constrains the velocity of the billiard-ball clock on the CTC to a single value (determined by both the geometry of the wormhole and mass of the billiard ball). As a result, there is no need to restrict the paths of the clock (e.g., with waveguides) or its initial velocity because the two distinct, desired histories of our model arise naturally as the *only* two paths through the spacetime. With this, we can represent the two evolutions of our clock in its reference frame through the chronology-violating region as per :numref:`fig:diagram_billiard-ball_clocks`, where we denote the proper travel time of the clock through the wormhole to be exactly :math:`\TimeDelta`.

Quantum clocks
^^^^^^^^^^^^^^

For our analysis, we employ the :math:`\Dimension`-level, pure, equiprobabilistic quantum *clock* state

.. math:: \ket{\qclock} = \frac{1}{\sqrt{\Dimension}}\sum_{n=1}^{\Dimension}\ket{n}.
   :label: eq:clock_vector

Here, the number states :math:`\{\ket{n}\}_{n=1}^\Dimension`, which obey orthonormality via the condition :math:`\braket{m}{n} = \delta_{nm}`, collectively form a basis for the :math:`\Dimension`-dimensional Hilbert space in which the clock resides. With this, let us define the clock Hamiltonian as

.. math:: \OperatorHamiltonian_\Clock = \sum_{n=1}^{\Dimension} \Energy_n\ket{n}\bra{n}
   :label: eq:clock_Hamiltonian

where :math:`\Energy_n` is the energy of the :math:`n`-th eigenstate :math:`\ket{n}`. Time evolution of a state over the times :math:`\TimeInitial\rightarrow\TimeFinal` is then generated by the time-evolution unitary, which in its standard form may be written

.. math:: \Rotation(\TimeFinal;\TimeInitial) \equiv \Rotation(\TimeFinal-\TimeInitial) = \e^{-\eye\OperatorHamiltonian_\Clock(\TimeFinal-\TimeInitial)/\hbar}.
   :label: eq:clock_evolution

This is written using the standard notation for the rotation operator :math:`\Rotation` because the transformation of a clock state produced by "time evolution" *is* simply a standard rotation operation. Given this form, the evolution of an initial clock state :math:`\ket{\qclock(\Time)}` (at time :math:`\Time`) to a later state :math:`\ket{\qclock(\Time+\TimeDelta)}` (at time :math:`\Time+\TimeDelta`) is simply

.. math:: \ket{\qclock(\Time+\TimeDelta)} = \Rotation(\TimeDelta)\ket{\qclock(\Time)} = \e^{-\eye\OperatorHamiltonian_\Clock\TimeDelta/\hbar}\ket{\qclock(\Time)}.
   :label: eq:clock_ticked

Expanding :eq:`eq:clock_evolution` via a Taylor series and subsequently using the Hamiltonian expansion :eq:`eq:clock_Hamiltonian` allows us to express an evolved state :math:`\ket{\qclock(\Time)}` in terms of its constituent basis states :math:`\{\ket{n}\}_{n=1}^\Dimension` as

.. math:: \ket{\qclock(\Time)} = \frac{1}{\sqrt{\Dimension}}\sum_{n=1}^{\Dimension}\e^{-\eye \Energy_n \Time/\hbar}\ket{n}.
   :label: eq:clock_evolved

The overlap between two states at different stages of time evolution is easily calculable as

.. math:: \braket{\qclock(\Time)}{\qclock(\Time+\TimeDelta)} = \frac{1}{\Dimension} \sum_{n=1}^{\Dimension} \e^{-\eye \Energy_n\TimeDelta/\hbar},
   :label: eq:clock_overlap

which quantifies the distinguishability (i.e., coherence) between the two clock states. Now, given our freedom of choice in specifying the energies without losing generality or functionality of the clock, we may choose them to be equally spaced such that

.. math:: \EnergyDelta = \Energy_n - \Energy_{n-1}.

Accordingly, the :math:`n`-th energy :math:`\Energy_n` can be expressed in terms of the ground state :math:`\Energy_1` and the spacing :math:`\EnergyDelta` as

.. math:: \Energy_n = \Energy_1 + (n-1)\EnergyDelta.
   :label: eq:clock_energies

From this, we introduce the orthogonalization time of our :math:`\Dimension`-level clock, defined as

.. math:: \TimeOrthogonalization = \frac{2\pi\hbar}{\Dimension\EnergyDelta},
   :label: eq:time_orthogonalization

which represents the minimal time needed for a clock to evolve (under the equally spaced Hamiltonian :eq:`eq:clock_Hamiltonian`) into an orthogonal one. A system with finite :math:`\TimeOrthogonalization` can be thought of as a clock which "ticks" at a rate proportional to :math:`\TimeOrthogonalization^{-1}`. Now, using the form :eq:`eq:time_orthogonalization` and the energy level relation :eq:`eq:clock_energies` allows us to write the clock overlap :eq:`eq:clock_overlap` as

.. math:: \braket{\qclock(\Time)}{\qclock(\Time+\TimeDelta)} = \frac{\e^{-\eye \Energy_1\TimeDelta/\hbar}}{\Dimension} \sum_{n=1}^{\Dimension} \exp\left[-2\pi\eye\frac{n-1}{\Dimension}\frac{\TimeDelta}{\TimeOrthogonalization}\right].
   :label: eq:clock_overlap_orthogonalization

A point to note is that these clocks, when composed of equally spaced energy eigenstates as imposed by :eq:`eq:clock_energies`, are dependent on only two parameters: the time :math:`\Time` of their evolution and the energy :math:`\Energy_1` of their ground state :math:`\ket{1}`. Mathematically, this can be shown by using :eq:`eq:clock_energies` and :eq:`eq:time_orthogonalization` to express :eq:`eq:clock_evolved` as

.. math:: \ket{\qclock(\Time)} = \frac{\e^{-\eye \Energy_1 \Time/\hbar}}{\sqrt{\Dimension}}\sum_{n=1}^{\Dimension}\exp\left[-2\pi\eye\frac{n-1}{\Dimension}\frac{\Time}{\TimeOrthogonalization}\right]\ket{n}.
   :label: eq:clock_evolved_orthogonalization

In any case, by the series identity

.. math:: \sum_{n=1}^{\Dimension} r^{n-1} = \frac{1-r^\Dimension}{1-r}, \qquad r\neq 1,

we may write :eq:`eq:clock_overlap_orthogonalization` as

.. math:: \braket{\qclock(\Time)}{\qclock(\Time+\TimeDelta)} = \frac{\e^{-\eye \Energy_1\TimeDelta/\hbar}}{\Dimension} \frac{1 - \exp\left[-2\pi\eye\frac{\TimeDelta}{\TimeOrthogonalization}\right]}{1 - \exp\left[-2\pi\eye\frac{1}{\Dimension}\frac{\TimeDelta}{\TimeOrthogonalization}\right]}.
   :label: eq:clock_evolved_orthogonalization_identity

Evidently, in the case that the evolution time difference is equal to the orthogonalization time, i.e., :math:`\TimeDelta = \TimeOrthogonalization`, then from :eq:`eq:clock_evolved_orthogonalization_identity` it is easy to see that the clock overlap vanishes, i.e.

.. math:: \left.\braket{\qclock(\Time)}{\qclock(\Time+\TimeDelta)}\right|_{\TimeDelta = \TimeOrthogonalization} = 0.

The case of :math:`\TimeDelta = \TimeOrthogonalization` can thus be interpreted as when the clock's "resolution" exactly matches the time difference between the relevant states. This is the key mechanism with which one can investigate temporal differences between the multiple trajectories (such as the two paths in the simple billiard-ball paradox) that are generated via the indeterminism present in spacetimes containing CTCs. Note that such modelling of an internal clock to track a quantum particle's proper time was first described in :cite:p:`zych_quantum_2011`.

As a final point, note that the simple form of the clock state and its associated Hamiltonian are only convenient choices---the results we obtain from the model of the billiard-ball paradox are completely independent of them (provided the initial clock is not an energy eigenstate but is a superposition of different energies). In particular, given that any quantum system can be decomposed into an orthogonal energy basis, then the use of such a basis poses no restrictions on any findings. The use of uniform :math:`1/\sqrt{\Dimension}` weights in the initial state also merely provides simplicity compared to that of general amplitudes :math:`\{c_n\}_{n=1}^{\Dimension}`. In the same vein, the fact that the energy levels are chosen to be equally spaced means that the orthogonalization time is the same between orthogonal states. Non-equally spaced energies on the other hand would only prevent the simplification of the D-CTC solutions. Indeed, the only consequential assumption which we make of the clock system is that it is finite-dimensional, a fact that can be justified by assuming that the clock states must belong to some set of bound states.

Quantum circuit model of the billiard-ball paradox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We now turn our attention to constructing the quantum circuit model of the simplified billiard-ball paradox.
For simplicity, we choose the initial (unevolved) clock state,

.. math:: \StateCR = \ket{\qclock(0)}\bra{\qclock(0)},
   :label: eq:clock_density

to be the CR input along the trajectories illustrated in :numref:`fig:diagram_billiard-ball_clocks`. Given these trajectories, it is easy to construct quantum circuit formulations for the clock states, and such circuits appear in :numref:`fig:circuit_ctc_billiards_evolutions`.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_billiards_evolutions-dark.png
      :scale: 36 %
      :alt: Quantum circuit diagrams of the individual evolutions in the billiard-ball paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_billiards_evolutions-light.png
      :scale: 36 %
      :alt: Quantum circuit diagrams of the individual evolutions in the billiard-ball paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_billiards_evolutions-light.png
   :name: fig:circuit_ctc_billiards_evolutions
   :scale: 36 %
   :alt: Quantum circuit diagrams of the individual evolutions in the billiard-ball paradox.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   Quantum circuit models of the two trajectories of :numref:`fig:diagram_billiard-ball_clocks` under study.

Here, the elastic self-collision of the clock between its past and future selves may be represented by the SWAP gate,

.. math:: \Swap = \sum_{j,k=1}^{\Dimension}{\ket{j}\bra{k}}_\CR\otimes{\ket{k}\bra{j}}_\CV.
   :label: eq:swap

In effect, this exchange of the CV (trapped CTC) and CR (incoming system) quantum states mimics the momentum-exchange collision interaction between the billiard ball's past and future selves [which necessarily occurs in :math:`(1+1)` dimensions]. (Note that here, the basis states correspond to those from which the particle's wave function is constructed. This means that, in the case of a quantum clock, these basis states represent the number states of the clock's Hilbert space.) This is because the complete transference of momentum between two particles (here, the past and future versions of the billiard ball) is necessarily an exchange of quantum clock state, provided the associated particles are otherwise identical. To clarify, in a particle's quantum description, the clock degree of freedom is the identifying attribute, while momentum performs the same function in its classical description. As such, the two necessarily correspond such that when a pair of classically indistinguishable particles trade momentum, they exchange their clocks, i.e., :math:`\Swap \ket{\qclock(\Time_1)} \otimes \ket{\qclock(\Time_2)} = \ket{\qclock(\Time_2)} \otimes \ket{\qclock(\Time_1)}`.

Additionally, for simplicity, the rotations of the clock on the path sections outside of the CTC (on the CV system between the time machine) have been neglected. This is valid because these time evolutions (namely the inbound :math:`\TimeInbound` and outbound :math:`\TimeOutbound` times) are experienced by both paths, and so contribute the same to the clock's total time evolution. This means that a clock which does not interact with the CTC will not evolve, while one which does interact will evolve (by the CTC "duration" :math:`\TimeDelta`).
 
Next, in order to combine the two separate subcircuits of :numref:`fig:circuit_ctc_billiards_evolutions` into a single circuit, we introduce a "vacuum" state :math:`\ket{0}` (orthonormal to the existing number states) into both the CR and CV Hilbert spaces. Of the many consequences of doing so, perhaps the most significant is that, because the clock's subspace has :math:`\Dimension` dimensions, the total space now has :math:`\Dimension + 1` dimensions.

In order to model the paradox faithfully, we mandate that the vacuum and clock cannot "collide" with each other. This effect will be enforced by modifying the SWAP gate to the form

.. math:: \VacuumSwap = \VacuumIdentity_\CR\otimes\ket{0}\bra{0}_\CV + \ket{0}\bra{0}_\CR\otimes\VacuumIdentity_\CV - \ket{0}\bra{0}_\CR\otimes\ket{0}\bra{0}_\CV + \Swap
   :label: eq:swap_vacuum

where :math:`\VacuumIdentity = \Identity + \ket{0}\bra{0}` is the identity matrix in a vacuum-inclusive Hilbert space. This altered SWAP simply excludes the vacuum from swapping with the non-vacuous states, e.g.,

.. math::

   \begin{aligned}
      \VacuumSwap \ket{0} \otimes \ket{0} &= \ket{0} \otimes \ket{0}, \\
      \VacuumSwap \ket{\qclock} \otimes \ket{0} &= \ket{\qclock} \otimes \ket{0}, \\
      \VacuumSwap \ket{0} \otimes \ket{\qclock} &= \ket{0} \otimes \ket{\qclock}, \\
      \VacuumSwap \ket{\qclock(\Time_1)} \otimes \ket{\qclock(\Time_2)} &= \ket{\qclock(\Time_2)} \otimes \ket{\qclock(\Time_1)}.
   \end{aligned}

In this interpretation, the state :math:`\ket{0}` represents the physical absence of a clock :math:`\ket{\qclock}`, hence the "vacuum" nomenclature.

In the associated extended Hilbert space, we write the vacuum-inclusive time-evolution operator as

.. math:: \VacuumRotation(\TimeFinal - \TimeInitial) = \ket{0}\bra{0} + \Rotation(\TimeFinal - \TimeInitial).
   :label: eq:rotation_vacuum

This form describes the special case where, without loss of generality in the model's results, the vacuum has vanishing energy such that its time-evolution phase coefficient is unity, i.e.,

.. math:: \bra{0}\VacuumRotation\ket{0} = 1.
   :label: eq:rotation_vacuum_unity

With this in mind, the corresponding vacuum-modified unitary operator is

.. math:: \UnitaryVacuum = \bigl[\VacuumIdentity_\CR\otimes\VacuumRotation_\CV(\TimeDelta)\bigr]\VacuumSwap.
   :label: eq:unitary_vacuum

Under this, the input state may either self-consistently interact with the CTC, or it may pass straight through the circuit, thus allowing it to evolve through the circuit in the two paths of :numref:`fig:diagram_billiard-ball_clocks`.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_billiards-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the billiard-ball paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_billiards-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the billiard-ball paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_billiards-light.png
   :name: fig:circuit_ctc_billiards
   :scale: 36 %
   :alt: A quantum circuit diagram of the billiard-ball paradox.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum model of the (simplified) billiard-ball paradox. Here, the SWAP gate is a modified :math:`\ket{0}`-excluding variant as defined in :eq:`eq:swap_vacuum`.

Solutions
---------

The D-CTC solutions can be calculated to be

.. math::

   \begin{aligned}
      \StateCR_{\MapDCTCsCR} &= \ParameterFree\ket{\qclock(0)}\bra{\qclock(0)} + (1 - \ParameterFree)\ket{\qclock(\TimeDelta)}\bra{\qclock(\TimeDelta)}\\
      \StateCV_{\MapDCTCsCR} &= \ParameterFree\ket{0}\bra{0} + (1 - \ParameterFree)\ket{\qclock(\TimeDelta)}\bra{\qclock(\TimeDelta)}.
   \end{aligned}

Here, :math:`0 \leq \ParameterFree \leq 1` is the multiplicity parameter that assumes a value of :math:`\ParameterFree = \frac{1}{\Dimension + 1}` in the case of Deutsch's rule of maximal entropy.

For P-CTCs on the other hand, we first compute the P-CTC operator,

.. math::
   :label: eq:billiards_P-CTCs_operator

   \begin{aligned}
       \OperatorPCTC &\equiv \trace_\CV[\Unitary] \\
       &= \trace\bigl[\VacuumRotation(\TimeDelta)\bigr] \ket{0}\bra{0} + \Identity + \Rotation(\TimeDelta).
   \end{aligned}

with which the corresponding solution can be determined to be

.. math:: \ket{\StatePure_{\MapPCTCsCR}} = \frac{1}{\sqrt{\Normalization}} \bigl[\ket{\qclock(0)} + \ket{\qclock(\TimeDelta)}\bigr],

where

.. math::

   \begin{aligned}
      \Normalization &= \trace[\OperatorPCTC \StateCR \OperatorPCTC^\dagger],\\
      &= 2 + \frac{1}{\Dimension}\Bigl(\trace\bigl[\Rotation(\TimeDelta)\bigr] + \trace\bigl[\Rotation^\dagger(\TimeDelta)\bigr]\Bigr).
   \end{aligned}

is the normalization factor. Additionally, although it has not been proven to be valid for non-qubit systems, the generalized weak-measurement tomography expression of the P-CTC CV state yields

.. math:: \StateCV_{\MapPCTCsCR} = \frac{1}{\Dimension + 1}\bigl[\ket{0}\bra{0} + \Dimension \ket{\qclock(0)}\bra{\qclock(0)}\bigr].

Note how this is exactly the maximally entropic version of the D-CTC solution, as predicted by the theory.

Qubit clocks
^^^^^^^^^^^^

A particularly eludicating special case of the model discussed so far is one in which the clock's subspace is an ordinary qubit space with basis vectors :math:`\{\ket{1},\ket{2}\}`. Accordingly, an initial (unevolved) clock state appears as

.. math:: \ket{\qclock(0)} = \frac{1}{\sqrt{2}}\bigl(\ket{1} + \ket{2}\bigr).
   :label: eq:clock_qubit

By :eq:`eq:clock_energies` and :eq:`eq:time_orthogonalization`, the associated clock gate may be written as

.. math:: \Rotation(\TimeDelta) = \e^{-\eye \Energy_1\Delta\Time/\hbar}\bigl(\ket{1}\bra{1} + \e^{-\eye \pi \TimeDelta/\TimeOrthogonalization}\ket{2}\bra{2}\bigr),

so that the orthogonalization time :math:`\TimeDelta = \TimeOrthogonalization` transforms the initial clock qubit :eq:`eq:clock_qubit` into the orthogonal state

.. math:: \ket{\qclock(\TimeOrthogonalization)} = \Rotation(\TimeOrthogonalization)\ket{\qclock(0)} = \frac{\e^{-\eye \Energy_1\TimeOrthogonalization/\hbar}}{\sqrt{2}}\bigl(\ket{1}-\ket{2}\bigr).
   :label: eq:clock_qubit_orthogonal

Importantly, note that qubit clocks only have two mutually orthogonal states, which means that multiple loops of the CTC cannot be distinguished by such clocks.

In this :math:`3`-dimensional total Hilbert space (of both the vacuum and the clock), we compute the D-CTC solutions to be

.. math::

   \begin{aligned}
      \StateCR_{\MapDCTCsCR} &= \frac{1}{2}\Bigl[\ket{1}\bra{1} + \bigl(\ParameterFree + (1 - \ParameterFree)\e^{\eye \pi \TimeDelta/\TimeOrthogonalization}\bigr)\ket{1}\bra{2} + \bigl(\ParameterFree + (1 - \ParameterFree)\e^{-\eye \pi \TimeDelta/\TimeOrthogonalization}\bigr)\ket{2}\bra{1} + \ket{2}\bra{2}\Bigr]\\
      \StateCV_{\MapDCTCsCR} &= \ParameterFree\ket{0}\bra{0} + (1 - \ParameterFree)\frac{1}{2}\bigl[\ket{1}\bra{1} + \e^{\eye \pi \TimeDelta/\TimeOrthogonalization}\ket{1}\bra{2} + \e^{-\eye \pi \TimeDelta/\TimeOrthogonalization}\ket{2}\bra{1} + \ket{2}\bra{2}\bigr],
   \end{aligned}

while the P-CTC solutions are

.. math::

   \begin{aligned}
      \ket{\StatePure_{\MapPCTCsCR}} &= \frac{1}{\sqrt{3 + \cos\left(\frac{\TimeDelta}{\TimeOrthogonalization}\pi\right)}} \bigl[\ket{\qclock(0)} + \ket{\qclock(\TimeDelta)}\bigr] \\
      &\propto 2\ket{1} + (1 + \e^{-\eye \pi \TimeDelta/\TimeOrthogonalization})\ket{2}, \\
      \StateCV_{\MapPCTCsCR} &= \frac{1}{3}\bigl[\ket{0}\bra{0} + 2 \ket{\qclock(0)}\bra{\qclock(0)}\bigr].
   \end{aligned}

P-CTC restrictions on initial data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One interesting general characteristic of P-CTCs is that they can pose constraints on initial conditions. Due to the renormalization, such constraints depend on the future of the time-travelling state. Here, we explicitly demonstrate the restrictions associated with the P-CTCs description of the circuit.

Given the :math:`\Dimension`-level clock :eq:`eq:clock_vector`, there exist exactly :math:`\Dimension` mutually orthogonal, equally spaced states :math:`\bigl\{\ket{\qclock^{(k)}(\TimeOrthogonalization)}\bigr\}_{k=0}^{\Dimension-1}` of which it can assume. As a consequence, one may express the clock gate :eq:`eq:clock_evolution` in terms of the ground-state energy :math:`\Energy_1` (defined via :eq:`eq:clock_energies`) as

.. math:: \Rotation(\TimeFinal - \TimeInitial) = \e^{-\eye \Energy_1 (\TimeFinal - \TimeInitial)/\hbar} \sum_{n=1}^{\Dimension}\exp\left[-2\pi\eye\frac{n-1}{\Dimension}\frac{\TimeFinal - \TimeInitial}{\TimeOrthogonalization}\right]\ket{n}\bra{n}.
   :label: eq:rotation_global

From this, it is easy to conclude that

.. math:: \Rotation^\Dimension(\TimeOrthogonalization) = \e^{-\eye \Dimension \Energy_1 \TimeOrthogonalization/\hbar}\Identity,
   :label: eq:rotation_orthogonalization

which simply indicates that :math:`\Dimension` orthogonal rotations of the clock return it to its initial state, up to the global phase :math:`\e^{-\eye \Dimension \Energy_1 \TimeOrthogonalization/\hbar}`. Accordingly, a clock :math:`\ket{\qclock}` that orthogonalizes :math:`p\in\Integers_{>0}` times accumulates :math:`p` such phases. Therefore, judicious choice of the clock's orthogonalization time :math:`\TimeOrthogonalization`, such that it is related to the CTC time delay :math:`\TimeDelta` by

.. math:: \TimeDelta = p \Dimension \TimeOrthogonalization,
   :label: eq:orthogonalization_time_multiple

means that a clock which completes one journey on the CTC would orthogonally evolve :math:`p` times. In such a case, the P-CTC reduced operator :eq:`eq:billiards_P-CTCs_operator` becomes

.. math:: \left.\OperatorPCTC\right|_{\TimeDelta = p \Dimension \TimeOrthogonalization} = \left(1 + \Dimension \e^{-\eye p \Dimension \Energy_1 \TimeOrthogonalization/\hbar}\right)\ket{0}\bra{0} + \left(1 + \e^{-\eye p \Dimension \Energy_1 \TimeOrthogonalization/\hbar}\right)\Identity.
   :label: eq:billiards_P-CTCs_operator_orthogonalization

Additionally, if we construct the clock so that its ground-state energy :math:`\Energy_1` satisfies

.. math:: \Energy_1 = \frac{\pi\hbar}{p \Dimension \TimeOrthogonalization}(1 + 2q),\quad q\in\Integers_{\geq 0},
   :label: eq:billiards_P-CTCs_energy_vanish

then the operator :eq:`eq:billiards_P-CTCs_operator_orthogonalization` further reduces to

.. math:: \OperatorPCTC' = \left.\OperatorPCTC\right|_{\substack{\TimeDelta = p \Dimension \TimeOrthogonalization\\ \Energy_1 = \frac{\pi\hbar}{p \Dimension \TimeOrthogonalization}(1 + 2q)}} = \left(1 - \Dimension\right)\ket{0}\bra{0}.
   :label: eq:billiards_P-CTCs_operator_constrained

After renormalization, the corresponding P-CTC output is then, of course, simply the vacuum state, i.e., :math:`\ket{0}`. This cannot be valid however, because the initial input state :eq:`eq:clock_density` did not include any vacuum term. So what happened to the clock?

To answer this question, we can use the vacuum-including entangled state

.. math:: \ket{\StatePure}_{\text{rec},\CR} = \sqrt{\ParameterVacuum}\ket{0}_\text{rec}\otimes\ket{0}_\CR + \sqrt{1 - \ParameterVacuum}\ket{\qclock(0)}_\text{rec}\otimes\ket{\qclock(0)}_\CR, \quad 0 \leq \ParameterVacuum \leq 1,
   :label: eq:billiards_P-CTCs_entangled

as input to our circuit. Here, the state existing in the first system may be interpreted as a record of what we send into the CR system. With this entanglement, we find the P-CTC unnormalized pure-state output, corresponding to our circuit's ordinary operator :math:`\VacuumIdentity_\text{rec}\otimes\OperatorPCTC_\CR` from :eq:`eq:billiards_P-CTCs_operator`, to be

.. math::

   \begin{aligned}
      \bigl(\VacuumIdentity_\text{rec}\otimes\OperatorPCTC_\CR\bigr)\ket{\StatePure}_{\text{rec},\CR} &\propto \sqrt{\ParameterVacuum}\,\trace[\VacuumRotation(\TimeDelta)]\,\ket{0}_\text{rec}\otimes\ket{0}_\CR \\
      &\quad + \sqrt{1 - \ParameterVacuum}\,\ket{\qclock(0)}_\text{rec}\otimes\bigl[\ket{\qclock(0)}_\CR + \ket{\qclock(\TimeDelta)}_\CR\bigr].
   \end{aligned}

The persistence of the entanglement means that when the record indicates that we did not send in a clock, we will not observe a clock in the CR output. Conversely, when we definitely did send in a clock, we must observe a clock exiting the CTC region, which is exactly what one intuitively expects. However, under the conditions :eq:`eq:orthogonalization_time_multiple` and :eq:`eq:billiards_P-CTCs_energy_vanish` which yield the operator :eq:`eq:billiards_P-CTCs_operator_constrained`, the entanglement of our input state :eq:`eq:billiards_P-CTCs_entangled` breaks,

.. math:: \bigl(\VacuumIdentity_\text{rec}\otimes\OperatorPCTC'_\CR\bigr)\ket{\StatePure}_{\text{rec},\CR} \propto \ket{0}_\text{rec}\otimes\ket{0}_\CR,

regardless of the value of :math:`\ParameterVacuum` (provided it is non-zero). Thus, the mere presence of the interaction with the CTC in the future implies that the record subsystem will show that no clock was ever prepared, even though the initial state :eq:`eq:billiards_P-CTCs_entangled` included the possibility that a clock was there (which would show up in the record if the future interaction with the CTC was avoided).

Given the path-integral correspondence of P-CTCs, the conditions :eq:`eq:orthogonalization_time_multiple` and :eq:`eq:billiards_P-CTCs_energy_vanish` collectively form a case in which *no* clocks can evolve through the circuit due to destructive interference in the path integral. This is to say that P-CTCs suppress all evolutions of non-vacuous states as a result of the particular future evolution of clock states in our model, thereby posing constraints on the initial state. This issue highlights the well-known problem of antichronological and superluminal influence with P-CTCs :cite:p:`ralph_relativistic_2012,bub_quantum_2014,ghosh_quantum_2018`. In contrast, the initial data for D-CTCs are never affected by the presence (or absence) of a CTC in the future.

Implementation
--------------

This implementation is strictly for qubits. For simplicity, we set :math:`\frac{\TimeDelta}{\TimeOrthogonalization} \equiv t`.

.. literalinclude:: /text/examples/ctcs/billiards.py
   :name: code:billiards
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> billiards.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_billiards-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_ctcs_billiards-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> billiards_DCTC_respecting.print()
   ρ_D = 1/2|1⟩⟨1| + -(g*exp(I*pi*t) - g - exp(I*pi*t))/2|1⟩⟨2| + (g*exp(I*pi*t) - g + 1)*exp(-I*pi*t)/2|2⟩⟨1| + 1/2|2⟩⟨2|

.. code:: python

   >>> billiards_DCTC_violating.print()
   τ_D = g|0⟩⟨0| + (1/2 - g/2)|1⟩⟨1| + (1 - g)*exp(I*pi*t)/2|1⟩⟨2| + (1 - g)*exp(-I*pi*t)/2|2⟩⟨1| + (1/2 - g/2)|2⟩⟨2|

.. code:: python

   >>> billiards_PCTC_respecting.print()
   |ψ_P⟩ = sqrt(2)*sqrt(1/(cos(pi*t) + 3))|1⟩ + sqrt(2)*(1 + exp(-I*pi*t))*sqrt(1/(cos(pi*t) + 3))/2|2⟩

.. code:: python

   >>> billiards_PCTC_violating.print()
   τ_P = 1/3|0⟩⟨0| + 1/3|1⟩⟨1| + exp(I*pi*t)/3|1⟩⟨2| + exp(-I*pi*t)/3|2⟩⟨1| + 1/3|2⟩⟨2|

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage