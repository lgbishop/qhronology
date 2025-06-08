.. include:: /styles.rst

.. _`sec:continuous`:

**********************************************
Quantum mechanics on continuous Hilbert spaces
**********************************************

One of the more physically meaningful classes of Hilbert spaces are those which are *continuous*. Such systems typically describe the dynamics of quantum particles propagating in some physical continuum, that is, :math:`\Reals^\Dimension` for any :math:`\Dimension \in \IntegersPositive`. Mathematically, any continuous quantum system may be described by a state, which is a vector :math:`\ket{\WaveFunction}` residing in a Lebesgue space (a special function space that is also a type of Hilbert space), denoted :math:`\SpaceLebesgue^2(\SetSub)`, on certain set :math:`\SetSub` which is some configuration space (such as :math:`\Reals^3)`. The theory discussed here adapts the work presented in :cite:p:`ryder_quantum_1996,dimock_quantum_2011,zeidler_quantum_2006,zee_quantum_2010,townsend_modern_2012,griffiths_introduction_2018,schulten_notes_2014,dittrich_classical_2020,schulman_techniques_1981,dirac_principles_1982`.

Probabilities and the Born rule
===============================

For a (measurable) function :math:`\WaveFunction`, the condition :math:`\WaveFunction \in \SpaceLebesgue^2(\SetSub)` specifies that :math:`\WaveFunction` satisfies a finitely bound integral of the form

.. math:: \norm{\WaveFunction}_2 \equiv \left[\int_{\SetSub}\abs{\WaveFunction(\vec{\Coordinate})}^2 \, \diff{\Measure(\vec{\Coordinate})}\right]^{\frac{1}{2}} < \infty
   :label: eq:square_integrable

where :math:`\norm{\WaveFunction}_2` is the :math:`\SpaceLebesgue^2`-norm of :math:`\WaveFunction` and :math:`\Measure(\vec{\Coordinate})` is the appropriate measure of the set :math:`\SetSub`. A function for which :eq:`eq:square_integrable` holds true is said to be *square-integrable* (on :math:`\SetSub`), or an :math:`\SpaceLebesgue^2`-function. Note that such functions form an inner product space with the inner product given by

.. math:: \braket{\phi}{\WaveFunction} = \int_{\SetSub} \conj{\phi}{(\vec{\Coordinate})}\WaveFunction(\vec{\Coordinate})\,\diff{\Measure(\vec{\Coordinate})}, \qquad \phi,\WaveFunction\in \SpaceLebesgue^2(\vec{\Coordinate}).

With this, the Lebesgue space is now a Hilbert space, and we have the isomorphism :math:`\SpaceLebesgue^2 \cong \SpaceHilbert`. From here, if the norm defined in :eq:`eq:square_integrable` is equal to :math:`1`,

.. math:: \int_{\SetSub}\abs{\WaveFunction(\vec{\Coordinate})}^2 \, \diff{\Measure(\vec{\Coordinate})} = 1,
   :label: eq:normalization

then the element :math:`\WaveFunction\in \SpaceLebesgue^2(\SetSub)` defines a probability measure on :math:`\SetSub`. In the case that the measure :math:`\Measure(\vec{\Coordinate})` is continuous, then the real-valued function

.. math:: \Probability(\vec{\Coordinate}) = \abs{\WaveFunction(\vec{\Coordinate})}^2
   :label: eq:Born

is called a *probability density function* (PDF) and the complex-valued function :math:`\WaveFunction(\vec{\Coordinate})` is called a *probability amplitude*. If the measure :math:`\Measure(\vec{\Coordinate})` is instead discrete, then the integral becomes a sum and :math:`\abs{\WaveFunction(\vec{\Coordinate})}^2` defines the probability measure on the set :math:`\SetSub`---that is, the probability that the quantum system represented by :math:`\ket{\WaveFunction}` assumes the state with parameter :math:`\vec{\Coordinate} \in \SetSub`. The rule :eq:`eq:Born` is perhaps the archetypal representation of the Born rule.

The state vector :math:`\ket{\WaveFunction}` may be projected into different coordinate bases via the equivalence

.. math:: \WaveFunction(\vec{\Coordinate}) = \braket{\vec{\Coordinate}}{\WaveFunction} \quad \Longleftrightarrow \quad \ket{\WaveFunction} = \int \diff{\Measure(\vec{\Coordinate})} \, \WaveFunction(\vec{\Coordinate}) \ket{\vec{\Coordinate}},
   :label: eq:projection

where the configuration of the associated system in :math:`\Dimension`-dimensional space is represented by the :math:`\Dimension`-tuple of generalized coordinates :math:`(\Position_j)=\vec{\Position}`. Any such projection onto any basis is, by the usual interpretation of quantum mechanics, termed the *wave function* of the associated system. Commonly, this projection may be generalized to incorporate the state's time dependence,

.. math:: \WaveFunction(\vec{\Position},\Time) = \braket{\vec{\Position},\Time}{\WaveFunction},

which we interpret as the probability amplitude that the associated system (e.g., a particle) has position :math:`\vec{\Position}` at time :math:`\Time`. Accordingly, the PDF is given by the Born rule :eq:`eq:Born`,

.. math:: \Probability(\vec{\Position},\Time) = \abs{\WaveFunction(\vec{\Position},\Time)}^2,
   :label: eq:probability_density

which describes the probability of the particle's presence at and around the point :math:`(\vec{\Position},\Time)`.

Time evolution
==============

Suppose we have some (closed) system which is described by the state :math:`\ket{\WaveFunction(\TimeInitial)}` defined on a complex Hilbert space at some initial time :math:`\TimeInitial`. By :eq:`eq:evolution_closed_pure`, the time evolution of this system over the interval :math:`\TimeInitial \rightarrow \TimeFinal` to some final state :math:`\ket{\WaveFunction(\TimeFinal)}` is described by the form

.. math:: \ket{\WaveFunction(\TimeFinal)} = \UnitaryTime(\TimeFinal,\TimeInitial)\ket{\WaveFunction(\TimeInitial)}.
   :label: eq:evolution_time

Given that :math:`\WaveFunction(\Time)` must remain normalized for all :math:`\Time`, then the operator :math:`\UnitaryTime` must therefore be a unitary transformation. Importantly, this means that the transformation from past to future must be:

#. invertible :math:`\implies` information is conserved,

#. norm-preserving :math:`\implies` probability is conserved.

These facts imply that :math:`\UnitaryTime` may be expressed in general as the exponential map

.. math:: \UnitaryTime(\TimeFinal,\TimeInitial) = \mathcal{T} \exp\left[-\frac{\eye}{\hbar} \int_{\TimeInitial}^{\TimeFinal} \OperatorHamiltonian(\Time) \, \diff{\Time}\right]
   :label: eq:unitary_exponential_ordered

where, given that the Lie algebra of the unitary group is generated by Hermitian operators, then :math:`\OperatorHamiltonian` is a Hermitian operator, i.e., :math:`\OperatorHamiltonian^\dagger = \OperatorHamiltonian`. Here, the time-ordering symbol :math:`\mathcal{T}` permutes a product of non-commuting operators :math:`{\op{A}_n}` into the uniquely determined reordered expression

.. math:: \mathcal{T}[\op{A}_1(\Time_1)\cdot \op{A}_2(\Time_2)\cdot\ldots\cdot \op{A}_n(\Time_n)] = \op{A}_{i_1}(\Time_{i_1})\cdot \op{A}_{i_2}(\Time_{i_2})\cdot\ldots\cdot \op{A}_{i_n}(\Time_{i_n}), \qquad \Time_{i_1}\geq \Time_{i_2}\geq\ldots\geq \Time_{i_n}.

This result is a causal chain where the primary *cause* in the past is :math:`\op{A}_{i_n}(\Time_{i_n})` while the future *effect* is :math:`\op{A}_{i_1}(\Time_{i_1})`. In the case where :math:`\OperatorHamiltonian` is time-independent, the exponential map is simply

.. math:: \UnitaryTime(\TimeFinal,\TimeInitial) = \exp\left[-\frac{\eye}{\hbar} (\TimeFinal-\TimeInitial)\OperatorHamiltonian \right].
   :label: eq:unitary_exponential

Substituting this form into equation :eq:`eq:evolution_time`, letting :math:`(\TimeFinal,\TimeInitial)\rightarrow(\Time,0)` and then differentiating both sides with respect to :math:`\Time` yields

.. math:: \OperatorHamiltonian\ket{\WaveFunction(\Time)} = \eye\hbar\frac{\partial}{\partial \Time}\ket{\WaveFunction(\Time)}.
   :label: eq:Schrodinger

This is the *time-dependent Schrödinger equation* (TDSE), which is perhaps one of the most fundamental and important equations of non-relativistic quantum mechanics. Here, we identify the operator :math:`\OperatorHamiltonian` as the (time-independent) *Hamiltonian* operator, which corresponds to (or, more formally, has eigenvalues of) the total energy :math:`\Energy` of the state :math:`\WaveFunction`, i.e., :math:`\OperatorHamiltonian\ket{\WaveFunction} \equiv \Energy\ket{\WaveFunction}`. Schrödinger's equation is a partial differential equation that governs the temporal evolution of any time-dependent quantum system described by the arbitrary state :math:`\ket{\WaveFunction(\Time)}`. Essentially, it is the equation of motion which all non-relativistic systems must obey in order to be physical.

For any time-independent system, like a particle with (classical) kinetic energy :math:`\Kinetic` in a static potential field :math:`\Potential`, the Hamiltonian may be written as the sum of the (time-independent) total kinetic :math:`\OperatorKinetic` and potential :math:`\OperatorPotential` (operator) energies,

.. math:: \OperatorHamiltonian(\vec{\Position},\vec{\Momentum}) = \OperatorKinetic(\vec{\Position},\vec{\Momentum}) + \OperatorPotential(\vec{\Position})
   :label: eq:Hamiltonian_operator

where :math:`\vec{\Momentum}\equiv(\Momentum_j)` represents the :math:`\Dimension`-tuple of generalized momenta. Consequently, the TDSE is the mathematical statement that the time-independent Hamiltonian :math:`\OperatorHamiltonian` :eq:`eq:Hamiltonian_operator` is the infinitesimal generator of a one-parameter group parametrized by the time :math:`\Time`. This is to say that the time evolution of a state :math:`\ket{\WaveFunction(\TimeInitial)}` to a later state :math:`\ket{\WaveFunction(\TimeFinal)}` is generated by the Hamiltonian.

The time-evolution operator's utility can be observed in many different contexts. For example, consider an arbitrary single-body system located at position :math:`\vec{\Position}` at time :math:`\Time`. The state (or more specifically, the location) of such a system can be defined in the :math:`\vec{\Position}`-space (configuration) basis as

.. math:: \ket{\vec{\Position},\Time} \equiv \UnitaryTime(\Time,0)\ket{\vec{\Position}},

so that we may write the overlap between the past :math:`\ket{\vec{\PositionInitial},\TimeInitial}` and future :math:`\ket{\vec{\PositionFinal},\TimeFinal}` states as

.. math:: \braket{\vec{\PositionFinal},\TimeFinal}{\vec{\PositionInitial},\TimeInitial} = \bra{\vec{\PositionFinal}}\Unitary(\TimeFinal,\TimeInitial)\ket{\vec{\PositionInitial}},
   :label: eq:propagator_overlap

The physical significance of this quantity, known as the *transition amplitude*, shall next be discussed.

.. _`sec:path-integral`:

The path-integral formulation
=============================

The *path-integral formulation* :cite:p:`ryder_quantum_1996,kleinert_path_2009` (or the *sum-over-histories* approach) of quantum mechanics and field theory is a formalism that generalizes the principle of stationary action (from classical mechanics) to quantum mechanics. This formulation is based on the notion of the *propagator*,

.. math:: \Propagator(\vec{\PositionFinal},\TimeFinal;\vec{\PositionInitial},\TimeInitial) \equiv \braket{\vec{\PositionFinal},\TimeFinal}{\vec{\PositionInitial},\TimeInitial}, \qquad \TimeFinal>\TimeInitial
   :label: eq:propagator

which is a generalized function, defined as per :eq:`eq:propagator_overlap`. Of its many properties and applications, a primary use of the propagator is in its ability to evolve a wave function :math:`\WaveFunction(\vec{\PositionInitial},\TimeInitial)` to a later state via convolution, e.g.,

.. math:: \WaveFunction(\vec{\PositionFinal},\TimeFinal) = \int_{\Reals^\Dimension} \Propagator(\vec{\PositionFinal},\TimeFinal;\vec{\PositionInitial},\TimeInitial) \, \WaveFunction(\vec{\PositionInitial},\TimeInitial) \, \diff^\Dimension{\vec{\PositionInitial}}.
   :label: eq:kernel

Here,

.. math:: \WaveFunction(\vec{\Position},\Time) \equiv \braket{\vec{\Position},\Time}{\WaveFunction}

is the wave function of the system in state :math:`\ket{\WaveFunction}` projected into :math:`\vec{\Position}`-space at time :math:`\Time`. Given its convolution property in :eq:`eq:kernel` and its relation to the time-evolution operator in :eq:`eq:propagator_overlap`, we say that the propagator is the *Green's function* (or integral *kernel*) for the Schrödinger equation :eq:`eq:Schrodinger`.

Similar to how a wave function can describe the probability amplitude for a particle's location :math:`\vec{\Position}` at time :math:`\Time`, we may say that the propagator :math:`\Propagator(\vec{\PositionFinal},\TimeFinal;\vec{\PositionInitial},\TimeInitial)` is the probability amplitude for the *transition* of the particle from :math:`(\vec{\PositionInitial},\TimeInitial)` to :math:`(\vec{\PositionFinal},\TimeFinal)`. In :math:`\Dimension`-dimensional space, this transition could be accomplished through an infinite number of distinct and unique trajectories.

In general, the propagator can be written as the *phase-space path integral* over all paths :math:`\vec{\Position}(\Time)` and momentum evolutions :math:`\vec{\Momentum}(\Time)` from :math:`(\vec{\PositionInitial},\TimeInitial)` to :math:`(\vec{\PositionFinal},\TimeFinal)`,

.. math:: \Propagator(\vec{\PositionFinal},\TimeFinal;\vec{\PositionInitial},\TimeInitial) = \int_{\vec{\PositionInitial}}^{\vec{\PositionFinal}} \DifferentialPath\vec{\Position} \, \int_{\vec{\MomentumInitial}}^{\vec{\MomentumFinal}} \frac{\DifferentialPath\vec{\Momentum}}{(2\pi\hbar)^\Dimension} \, \e^{\eye \Action[\vec{\Position}]/\hbar}
   :label: eq:propagator_phase

where :math:`\Action[\vec{\Position}]` is the action of path :math:`\vec{\Position}(\Time)`. Here, we introduced the notation for the position and momentum differentials

.. math::
   :label: eq:differential_path_position

   \begin{aligned}
       \int_{\vec{\Position}_0}^{\vec{\Position}_\Number} \DifferentialPath\vec{\Position} &\equiv \lim\limits_{\Number \rightarrow \infty} \prod_{k=1}^{\Number-1} \int_{\Reals^\Dimension} \diff^\Dimension{\vec{\Position}_k},
   \end{aligned}

.. math::
   :label: eq:differential_path_momentum

   \begin{aligned}
       \int_{\vec{\Momentum}_0}^{\vec{\Momentum}_\Number} \DifferentialPath\vec{\Momentum} &\equiv \lim\limits_{\Number \rightarrow \infty} \prod_{n=0}^{\Number-1} \int_{\Reals^\Dimension} \diff^\Dimension{\vec{\Momentum}_n},
   \end{aligned}

which signify integration over all position :math:`\vec{\Position}(\Time)` and momentum :math:`\vec{\Momentum}(\Time)` evolutions through the :math:`\Number` subdivisions of our phase space. This discretization arises from our partitioning of the time coordinate into :math:`\Number` "slices"---physically, :math:`\vec{\Position}_n` represents the position of the particle at time :math:`\Time_n` (where :math:`n \in \Integers_1^\Number`)---and it is only after taking the continuum limit that we are able to recover smooth dynamics as described by :eq:`eq:propagator_phase`.

For a system with a Hamiltonian whose dependence on momentum is purely quadratic, the integral over the momentum evolutions :math:`\vec{\Momentum}(\Time)` in :eq:`eq:propagator_phase` can be directly computed. Subsequently, the propagator reduces to the *configuration-space path integral*,

.. math:: \Propagator(\vec{\PositionFinal},\TimeFinal;\vec{\PositionInitial},\TimeInitial) = \int_{\vec{\PositionInitial}}^{\vec{\PositionFinal}} \DifferentialPath^{\prime}\vec{\Position} \, \e^{\eye \Action[\vec{\Position}]/\hbar},
   :label: eq:propagator_configuration

where the "normalized" differential, compared to :eq:`eq:differential_path_position`, is defined as

.. math:: \int_{\vec{\Position}_0}^{\vec{\Position}_\Number} \DifferentialPath^{\prime}\vec{\Position} \equiv \lim\limits_{\Number \rightarrow \infty} \left[\frac{\Mass}{2\pi\eye\hbar(\TimeFinal - \TimeInitial)}\right]^\frac{\Number\Dimension}{2} \prod_{k=1}^{\Number-1} \int_{\Reals^\Dimension} \diff^\Dimension{\vec{\Position}_k}.
   :label: eq:differential_path_position_normalized

Here, :math:`\Mass` is the system's mass parameter. Note that this is an integral over *all* possible paths (both classical and quantum) and not just the classical path :math:`\classical{\vec{\Position}}(\Time)` (that which satisfies the relevant classical equations of motion) with action :math:`\classical{\Action} \equiv \Action[\classical{\vec{\Position}}]`. This expression is often presented as the typical form of the path integral.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
