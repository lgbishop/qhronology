.. include:: /styles.rst

.. _`sec:continuous`:

**********************************************
Quantum mechanics on continuous Hilbert spaces
**********************************************

One of the more physically meaningful classes of Hilbert spaces are those which are *continuous*. Such systems typically describe the dynamics of quantum particles propagating in some physical continuum, that is, :math:`\Reals^\Dimension` for any :math:`\Dimension \in \IntegersPositive`. Mathematically, any continuous quantum system may be described by a state, which is a vector :math:`\ket{\WaveFunction}` residing in a (continuous) *Lebesgue space* (a special function space that is also a type of Hilbert space), denoted by :math:`\SpaceLebesgue^2(\SetSub)`, on certain set :math:`\SetSub` which is some configuration space (such as :math:`\Reals^3)`. The theory discussed here adapts the work presented in :cite:p:`ryder_quantum_1996, dimock_quantum_2011, zeidler_quantum_2006, zee_quantum_2010, townsend_modern_2012, griffiths_introduction_2018, schulten_notes_2014, dittrich_classical_2020, schulman_techniques_1981, dirac_principles_1982`.

Probabilities and the Born rule
===============================

For a measurable function :math:`\WaveFunction`, the statement :math:`\WaveFunction \in \SpaceLebesgue^2(\SetSub)` specifies that :math:`\WaveFunction` satisfies a finitely bound integral of the form

.. math:: \norm{\WaveFunction}_2 \equiv \left[\int_{\SetSub}\abs{\WaveFunction(\vec{\Coordinate})}^2 \, \diff{\Measure(\vec{\Coordinate})}\right]^{\frac{1}{2}} < \infty,
   :label: eq:square_integrable

where :math:`\vec{\Coordinate} \in \SetSub`, :math:`\norm{\WaveFunction}_2` is the :math:`\SpaceLebesgue^2`-norm of :math:`\WaveFunction`, and :math:`\Measure(\vec{\Coordinate})` is an appropriate measure of the set :math:`\SetSub`. A function for which :eq:`eq:square_integrable` holds true is said to be *square-integrable* (on :math:`\SetSub`), or an :math:`\SpaceLebesgue^2`-function. Note that such functions form an inner product space, with the inner product given by

.. math:: \braket{\phi}{\WaveFunction} = \int_{\SetSub} \conj{\phi}{(\vec{\Coordinate})}\WaveFunction(\vec{\Coordinate})\,\diff{\Measure(\vec{\Coordinate})}, \qquad \phi,\WaveFunction\in \SpaceLebesgue^2(\vec{\Coordinate}).
   :label: eq:inner_product_continuous

With this, the Lebesgue space :math:`\SpaceLebesgue^2(\SetSub)` is now a Hilbert space :math:`\SpaceHilbert`, and we have the isomorphism :math:`\SpaceLebesgue^2 \cong \SpaceHilbert`. From here, if the norm defined in :eq:`eq:square_integrable` is equal to :math:`1`, i.e.,

.. math:: \int_{\SetSub}\abs{\WaveFunction(\vec{\Coordinate})}^2 \, \diff{\Measure(\vec{\Coordinate})} = 1,

then the element :math:`\WaveFunction\in \SpaceLebesgue^2(\SetSub)` defines a probability measure on :math:`\SetSub`. In the case that the measure :math:`\Measure(\vec{\Coordinate})` is continuous, then the real-valued function

.. math:: \Probability(\vec{\Coordinate}) = \abs{\WaveFunction(\vec{\Coordinate})}^2
   :label: eq:Born_rule_continuous

is called a *probability density function* (PDF), while the complex-valued function :math:`\WaveFunction(\vec{\Coordinate})` is called a *probability amplitude*. If the measure :math:`\Measure(\vec{\Coordinate})` is instead discrete, then the integral becomes a sum and :math:`\abs{\WaveFunction(\vec{\Coordinate})}^2` defines the probability measure on the set :math:`\SetSub`---that is, the probability that the quantum system represented by :math:`\ket{\WaveFunction}` assumes the state with parameter :math:`\vec{\Coordinate} \in \SetSub`. The form :eq:`eq:Born_rule_continuous` is perhaps the archetypal presentation of the Born rule for continuous quantum mechanics.

Coordinates and representations
===============================

Given a state vector :math:`\ket{\WaveFunction}` in a Hilbert space :math:`\SpaceHilbert`, the representation of its probability amplitude :math:`\WaveFunction` on a particular coordinate space can be obtained from the inner product

.. math:: \WaveFunction(\vec{\Coordinate}) = \braket{\vec{\Coordinate}}{\WaveFunction}.
   :label: eq:representation_coordinate

Here, the configuration of the associated system on the set :math:`\SpacePosition \subseteq \Reals^\Dimension` is represented by the vector :math:`\vec{\Coordinate}`, which is simply a :math:`\Dimension`-tuple of generalized coordinates :math:`\vec{\Coordinate} \equiv (\Coordinate_j)_{j=1}^{\Dimension}`. If we characterize the *position operator* :math:`\op{\vec{\Coordinate}}` point-wisely via

.. math:: \op{\vec{\Coordinate}} \, \WaveFunction(\vec{\Coordinate}) = \vec{\Coordinate} \, \WaveFunction(\vec{\Coordinate}), \qquad \forall \, \WaveFunction \in \SpaceLebesgue^2(\SpacePosition), \, \vec{\Coordinate} \in \SpacePosition,
   :label: eq:operator_coordinate_action

then the corresponding coordinate vectors :math:`\vec{\Coordinate}` are definitionally those vectors which satisfy the eigenvalue equation for :math:`\op{\vec{\Coordinate}}`, e.g.,

.. math:: \op{\vec{\Coordinate}} \ket{\vec{\Coordinate}} = \vec{\Coordinate} \ket{\vec{\Coordinate}}.
   :label: eq:eigenvector_coordinate

Formally, such vectors are termed *generalized* (*coordinate*) *eigenvectors* (also *eigenkets*) of :math:`\op{\vec{\Coordinate}}`, and collectively constitute an orthonormal basis only in the sense of distributions, by having orthonormality of the form

.. math:: \braket{\vec{\Coordinate}^{\prime\prime}}{\vec{\Coordinate}^{\prime}} = \delta^{(\Dimension)}(\vec{\Coordinate}^{\prime} - \vec{\Coordinate}^{\prime\prime}).
   :label: eq:orthonormality_coordinate

Here, :math:`\delta^{(\Dimension)}` is the :math:`\Dimension`-dimensional :math:`\delta`-*distribution*, which can be defined heuristically via the integral,

.. math:: \int_{\SpacePosition} \delta^{(\Dimension)}(\vec{\Coordinate} - \vec{y}) \, \FunctionTest(\vec{\Coordinate}) \, \diff^\Dimension{\vec{\Coordinate}} = \FunctionTest(\vec{y}),

for all test functions :math:`\FunctionTest`. Using these states, we can recover a probability amplitude's corresponding state vector as

.. math:: \ket{\WaveFunction} = \int_{\SpacePosition} \ket{\vec{\Coordinate}} \, \WaveFunction(\vec{\Coordinate}) \, \diff^\Dimension{\vec{\Coordinate}},
   :label: eq:reconstruction_coordinate

which is possible if and only if the eigenkets satisfy the *completeness relation*,

.. math:: \int_{\SpacePosition} \ket{\vec{\Coordinate}} \bra{\vec{\Coordinate}} \, \diff^\Dimension{\vec{\Coordinate}} = \Identity,
   :label: eq:completeness_coordinate

where :math:`\Identity` is the *identity operator*, i.e.,

.. math:: \Identity \ket{\WaveFunction} = \ket{\WaveFunction}, \qquad \forall \, \ket{\WaveFunction} \in \SpaceHilbert.

It is important to note that while the coordinate vectors :math:`\ket{\vec{\Coordinate}}` satisfying :eq:`eq:eigenvector_coordinate` can be used in the manner of :eq:`eq:representation_coordinate`, they are not states, (i.e., elements of :math:`\SpaceHilbert`), nor do they collectively constitute a countable orthonormal basis for :math:`\SpaceHilbert`. Integrals like :eq:`eq:representation_coordinate` and :eq:`eq:completeness_coordinate` can therefore only be properly understood when taken in the weak sense. Accordingly, our Hilbert space :math:`\SpaceHilbert` must be expanded to include distributions, and thus becomes a *rigged Hilbert space* (or *Gelfand triple*).

In non-relativistic mechanics (both classical and quantum), the configuration of a physical system (e.g., the positions of a collection of particles) can be represented by a set of parameters :math:`\{q_i\}_i` conventionally called *generalized positions*. These are typically combined into a vector (or collection of vectors), and the space defined by such vectors is known as *configuration space* :math:`Q`.

For dynamical (i.e., non-stationary) systems, configuration space alone however is insufficient to completely describe state evolution, as it does not incorporate the rate of change of the generalized positions with respect to time :math:`t`. This is instead captured by the *generalized velocities* :math:`\{\dot{q}_i \equiv \frac{\partial q_i}{\partial t}\}_i`, the set of which, by virtue of being comprised purely of derivatives of the generalized coordinates, defines a hyperplane :math:`T_q Q` that is tangent (as manifolds) to the plane of configuration space :math:`Q` at every point :math:`q \in Q`.

As velocity is related linearly to momentum via a Legendre transformation, then the set of momentum vectors forms a cotangent plane (as momentum vectors are linear functionals on :math:`T_q Q`), which is denoted by :math:`T_q^* Q` at :math:`q`. The associated parameters are called *generalized momenta* :math:`\{p_i\}_i`, and together with the generalized positions, constitute a physical system's *canonical coordinates*, which completely describe its state at any given time. Note that the set of canonical coordinates constitutes a larger manifold (the cotangent bundle :math:`T^* Q`) which is conventionally known as *phase space*, and the coordinates themselves are termed (*canonically*) *conjugate*, *dual*, or *complementary*.

.. Under the interpretation that the coordinate :math:`\vec{\Coordinate}` represents *position* in the description of the quantum system in the configuration space :math:`\SpacePosition \subseteq \Reals^\Dimension`, then elements :math:`\vec{\Wavevector}` of the dual (i.e., reciprocal) space :math:`\SpaceMomentum \subseteq \Reals^\Dimension` represent *spatial frequency*, by virtue of having the unit of reciprocal length. The quantity :math:`\vec{\Wavevector}` therefore corresponds to the *wave vector* of the associated system in a matter-wave description. Given that a particle's *momentum* :math:`\vec{\Momentum}` is related linearly to its wave vector in such a description, i.e., :math:`\vec{\Momentum} = \hbar \vec{\Wavevector}`, then the dual space is commonly taken to represent the quantum system's (canonical) momentum.

In the context of our treatment here, under the interpretation that the parameter-components of the vector :math:`\vec{\Coordinate}` constitute the system's generalized positions with a corresponding configuration space :math:`\SpacePosition \subseteq \Reals^\Dimension`, then we define the generalized momenta, canonically conjugate to :math:`\vec{\Coordinate}`, as the components of :math:`\vec{\Momentum}` in the dual space :math:`\SpaceMomentum \subseteq \Reals^\Dimension`. Any point in the associated phase space may therefore be represented by a 2-tuple of the form

.. math:: (\vec{\Coordinate}, \vec{\Momentum}) \in \SpacePosition \times \SpaceMomentum \subseteq \Reals^\Dimension \times \Reals^\Dimension.

.. Since the configuration and reciprocal spaces are each a subset of :math:`\Reals^\Dimension`, then the associated measures are the standard :math:`\Dimension`-forms,

.. .. math::

..    \begin{aligned}
..        \diff{\Measure(\vec{\Coordinate})} &= \diff^\Dimension{\vec{\Coordinate}}, \\
..        \diff{\tilde{\Measure}(\vec{\Momentum})} &= \diff^\Dimension{\vec{\Momentum}}.
..    \end{aligned}

The duality between :math:`\vec{\Coordinate}`-space and :math:`\vec{\Momentum}`-space means that the function

.. math:: \tilde{\WaveFunction}(\vec{\Momentum}) = \braket{\vec{\Momentum}}{\WaveFunction}
   :label: eq:representation_momentum

is simply an alternative description of the state :math:`\ket{\WaveFunction}` compared to :eq:`eq:representation_coordinate`. By construction, it is an eigenfunction of the *momentum operator* :math:`\op{\vec{\Momentum}}`, which can be characterized via its action,

.. math:: \op{\vec{\Momentum}} \, \tilde{\WaveFunction}(\vec{\Momentum}) = \vec{\Momentum} \, \tilde{\WaveFunction}(\vec{\Momentum}), \qquad \forall \, \tilde{\WaveFunction} \in \SpaceLebesgue^2(\SpaceMomentum), \, \vec{\Momentum} \in \SpaceMomentum.
   :label: eq:operator_momentum_action

Like their counterparts :eq:`eq:eigenvector_coordinate`, the associated *generalized* (*momentum*) *eigenvectors* :math:`\ket{\vec{\Momentum}}` satisfy

.. math:: \op{\vec{\Momentum}} \ket{\vec{\Momentum}} = \vec{\Momentum} \ket{\vec{\Momentum}},
   :label: eq:eigenvector_momentum

and, with the orthonomality

.. math:: \braket{\vec{\Momentum}^{\prime\prime}}{\vec{\Momentum}^{\prime}} = \delta^{(\Dimension)}(\vec{\Momentum}^{\prime} - \vec{\Momentum}^{\prime\prime}),
   :label: eq:orthonormality_momentum

such vectors collectively constitute an orthonormal basis in :math:`\vec{\Momentum}`-space in the sense of distributions.

As with :eq:`eq:reconstruction_coordinate`, we can recover the state vector :math:`\ket{\WaveFunction}` by integrating over all eigenvectors :math:`\ket{\vec{\Momentum}}` with weights :math:`\tilde{\WaveFunction}(\vec{\Momentum})`,

.. math:: \ket{\WaveFunction} = \int_{\SpaceMomentum} \ket{\vec{\Momentum}} \, \tilde{\WaveFunction}(\vec{\Momentum}) \, \diff^\Dimension{\vec{\Momentum}},
   :label: eq:reconstruction_momentum

provided :math:`\ket{\vec{\Momentum}}` are similarly complete, i.e.,

.. math:: \int_{\SpaceMomentum} \ket{\vec{\Momentum}} \bra{\vec{\Momentum}} \, \diff^\Dimension{\vec{\Momentum}} = \Identity.
   :label: eq:completeness_momentum

By taking the inner product of :eq:`eq:reconstruction_momentum` with the eigenbra :math:`\bra{\vec{\Coordinate}}`, and subsequently making the identification :eq:`eq:representation_coordinate`, we obtain

.. math:: \WaveFunction(\vec{\Coordinate}) = \int_{\SpaceMomentum} \braket{\vec{\Coordinate}}{\vec{\Momentum}} \, \tilde{\WaveFunction}(\vec{\Momentum}) \, \diff^\Dimension{\vec{\Momentum}}.
   :label: eq:duality_momentum

Accordingly, as the function :math:`\tilde{\WaveFunction}(\vec{\Momentum})` holds all the information necessary to be able to reconstruct :math:`\WaveFunction(\vec{\Coordinate})` (and vice versa), then :eq:`eq:duality_momentum` simply describes a transformation between the two descriptions. Here, the function :math:`\braket{\vec{\Coordinate}}{\vec{\Momentum}}` is sometimes called the *character* of the transformation, and can be denoted by

.. math:: \Character_{\vec{\Momentum}}(\vec{\Coordinate}) \equiv \braket{\vec{\Coordinate}}{\vec{\Momentum}}.
   :label: eq:character_momentum

By necessity, the character must be an eigenfunction of :math:`\op{\vec{\Momentum}}`, and to determine its exact form, we require the representation of :math:`\op{\vec{\Momentum}}` in coordinate space, which can be shown to be

.. math:: \op{\vec{\Momentum}} = -\eye\hbar \frac{\partial}{\partial \vec{\Coordinate}}.
   :label: eq:operator_momentum_representation_coordinate

With this, the character :eq:`eq:character_momentum` satisfies,

.. math:: \op{\vec{\Momentum}} \, \Character_{\vec{\Momentum}}(\vec{\Coordinate}) = \vec{\Momentum} \, \Character_{\vec{\Momentum}}(\vec{\Coordinate}),

which can be determined to have the form

.. math:: \Character_{\vec{\Momentum}}(\vec{\Coordinate}) = N \e^{\eye \vec{\Coordinate} \cdot \vec{\Momentum} / \hbar}, \qquad N \in \Reals.

Through normalization as per :eq:`eq:orthonormality_momentum`, we find

.. math::

   \begin{aligned}
       \braket{\vec{\Momentum}^{\prime\prime}}{\vec{\Momentum}^{\prime}} &= \int_{\SpacePosition} \braket{\vec{\Momentum}^{\prime\prime}}{\vec{\Coordinate}} \braket{\vec{\Coordinate}}{\vec{\Momentum}^{\prime}} \, \diff^\Dimension{\vec{\Coordinate}} \\
       &= N^2 \int_{\SpacePosition} \e^{\eye \vec{\Coordinate} \cdot (\vec{\Momentum}^{\prime} - \vec{\Momentum}^{\prime\prime}) / \hbar} \, \diff^\Dimension{\vec{\Coordinate}} \\
       &= N^2 (2\pi\hbar)^\Dimension \delta^{(\Dimension)}(\vec{\Momentum}^{\prime} - \vec{\Momentum}^{\prime\prime}),
   \end{aligned}

where we used :eq:`eq:completeness_coordinate` along with the heuristic identity

.. math:: \delta^{(\Dimension)}(\vec{\Wavevector}) = \frac{1}{(2\pi)^\Dimension} \int_{\SpacePosition} \e^{\eye \vec{\Coordinate} \cdot \vec{\Wavevector}} \, \diff^\Dimension{\vec{\Coordinate}}.

We subsequently find :math:`N = (\sqrt{2\pi\hbar})^{-\Dimension}`, and so

.. math:: \Character_{\vec{\Momentum}}(\vec{\Coordinate}) = \braket{\vec{\Coordinate}}{\vec{\Momentum}} = \frac{1}{(\sqrt{2\pi\hbar})^\Dimension} \e^{\eye \vec{\Coordinate} \cdot \vec{\Momentum} / \hbar}.

Thus, :eq:`eq:duality_momentum` may be written as

.. math:: \WaveFunction(\vec{\Coordinate}) = \frac{1}{(\sqrt{2\pi\hbar})^\Dimension} \int_{\SpaceMomentum} \tilde{\WaveFunction}(\vec{\Momentum}) \, \e^{\eye \vec{\Coordinate} \cdot \vec{\Momentum} / \hbar} \, \diff^\Dimension{\vec{\Momentum}},
   :label: eq:fourier_momentum

which can be identified as the inverse Fourier transform :math:`\Fourier^{-1}[\,{}\cdot{}\,] : \SpaceLebesgue^2(\SpaceMomentum) \rightarrow \SpaceLebesgue^2(\SpacePosition)`. Given that Fourier transforms come in pairs, then the (non-inverse) transform can be similarly determined: first, we obtain the momentum-space representation of the position operator,

.. math:: \op{\vec{\Coordinate}} = \eye\hbar \frac{\partial}{\partial \vec{\Momentum}}.
   :label: eq:operator_coordinate_representation_momentum

Its normalized eigenfunctions, i.e., those forms :math:`\Character_{\vec{\Coordinate}}(\vec{\Momentum}) \equiv \braket{\vec{\Momentum}}{\vec{\Coordinate}}` satisfying

.. math:: \op{\vec{\Coordinate}} \, \Character_{\vec{\Coordinate}}(\vec{\Momentum}) = \vec{\Coordinate} \, \Character_{\vec{\Coordinate}}(\vec{\Momentum}),

can be determined to be

.. math:: \Character_{\vec{\Momentum}}(\vec{\Coordinate}) = \braket{\vec{\Momentum}}{\vec{\Coordinate}} = \frac{1}{(\sqrt{2\pi\hbar})^\Dimension} \e^{-\eye \vec{\Coordinate} \cdot \vec{\Momentum} / \hbar}.
   :label: eq:eigenfunction_coordinate

Next, by taking the inner product of :eq:`eq:reconstruction_coordinate` with the eigenbra :math:`\bra{\vec{\Momentum}}`, we find

.. math:: \tilde{\WaveFunction}(\vec{\Momentum}) = \int_{\SpacePosition} \braket{\vec{\Momentum}}{\vec{\Coordinate}} \, \WaveFunction(\vec{\Coordinate}) \, \diff^\Dimension{\vec{\Coordinate}},
   :label: eq:duality_coordinate_overlap

with which substitution of :eq:`eq:eigenfunction_coordinate` yields

.. math:: \tilde{\WaveFunction}(\vec{\Momentum}) = \frac{1}{(\sqrt{2\pi\hbar})^\Dimension} \int_{\SpacePosition} \WaveFunction(\vec{\Coordinate}) \, \e^{-\eye \vec{\Coordinate} \cdot \vec{\Momentum} / \hbar} \, \diff^\Dimension{\vec{\Coordinate}}
   :label: eq:fourier_coordinate

i.e., the (non-inverse) Fourier transform :math:`\Fourier[{}\cdot{}] : \SpaceLebesgue^2(\SpacePosition) \rightarrow \SpaceLebesgue^2(\SpaceMomentum)`.

The Fourier transform is a powerful technique because it allows us to freely switch between representations of certain quantities in :math:`\vec{\Coordinate}`-space and :math:`\vec{\Momentum}`-space, such as the state vector :math:`\ket{\WaveFunction}` in the pair of :eq:`eq:fourier_coordinate` and :eq:`eq:fourier_momentum`. This also includes the generalized eigenvectors themselves,

.. math::

   \begin{aligned}
       \ket{\vec{\Coordinate}} &= \frac{1}{(\sqrt{2\pi\hbar})^\Dimension} \int_{\SpacePosition} \ket{\vec{\Momentum}} \, \e^{-\eye \vec{\Coordinate} \cdot \vec{\Momentum} / \hbar} \, \diff^\Dimension{\vec{\Momentum}}, \\
       \ket{\vec{\Momentum}} &= \frac{1}{(\sqrt{2\pi\hbar})^\Dimension} \int_{\SpaceMomentum} \ket{\vec{\Coordinate}} \, \e^{\eye \vec{\Coordinate} \cdot \vec{\Momentum} / \hbar} \, \diff^\Dimension{\vec{\Coordinate}}.
   \end{aligned}

The position and momentum operators (and their associated representations) are therefore said to be *unitarily equivalent*, with the unitary map corresponding to the Fourier transform.

Translations
============

In configuration space, the *translation operator* is defined as a linear map :math:`\op{T}(\vec{r})` that facilitates the shift of a position eigenvector by an amount :math:`\vec{r}`, e.g., :math:`\ket{\vec{\Coordinate}} \rightarrow \ket{\vec{\Coordinate} + \vec{r}}`, or more explicitly,

.. math:: \op{T}(\vec{r}) \ket{\vec{\Coordinate}} = \ket{\vec{\Coordinate} + \vec{r}}.

Given this transformation, the operator :math:`\op{T}` must have the general form

.. math:: \op{T}(\vec{r}) = \int_{\SpacePosition} \ket{\vec{\Coordinate} + \vec{r}}\bra{\vec{\Coordinate}} \, \diff^\Dimension{\vec{\Coordinate}}.

The primary purpose of the translation operator is to shift representations of quantum states in configuration space. To obtain an exact representation of :math:`\op{T}` in terms of the canonical coordinate operators, we first translate an expansion of the state :math:`\ket{\WaveFunction}` in the form of :eq:`eq:reconstruction_coordinate`, yielding

.. math::

   \begin{aligned}
       \op{T}(\vec{r}) \ket{\WaveFunction} &= \int_{\SpacePosition} \op{T}(\vec{r})\ket{\vec{\Coordinate}} \, \WaveFunction(\vec{\Coordinate}) \, \diff^\Dimension{\vec{\Coordinate}} \\
       &= \int_{\SpacePosition} \ket{\vec{\Coordinate} + \vec{r}} \, \WaveFunction(\vec{\Coordinate}) \, \diff^\Dimension{\vec{\Coordinate}}.
   \end{aligned}

Performing a coordinate substitution :math:`\vec{\Coordinate} \rightarrow \vec{\Coordinate} - \vec{r}` allows the integral to be reexpressed as

.. math::
   :label: eq:translation_integral

   \op{T}(\vec{r}) \ket{\WaveFunction} = \int_{\SpacePosition} \ket{\vec{\Coordinate}} \, \WaveFunction(\vec{\Coordinate} - \vec{r}) \, \diff^\Dimension{\vec{\Coordinate}},

from which we can see that the transformation rule for a general state :math:`\WaveFunction \in \SpaceHilbert` is

.. math:: \op{T}(\vec{r}) \WaveFunction(\vec{\Coordinate}) = \WaveFunction(\vec{\Coordinate} - \vec{r}).

Without loss of generality, we assume that the function :math:`\WaveFunction` is analytic, and so can be expanded in a Taylor series about the point :math:`\vec{\Coordinate}`,

.. math::

   \begin{aligned}
       \WaveFunction(\vec{\Coordinate} - \vec{r}) &= \WaveFunction(\vec{\Coordinate}) - \vec{r} \cdot \frac{\partial \WaveFunction(\vec{\Coordinate})}{\partial \vec{\Coordinate}} + \vec{r}^2 \cdot \frac{\partial^2 \WaveFunction(\vec{\Coordinate})}{\partial \vec{\Coordinate}^2} - \vec{r}^3 \cdot \frac{\partial^3 \WaveFunction(\vec{\Coordinate})}{\partial \vec{\Coordinate}^3} + \BigO(\vec{r}^4) \\
       &= \sum_{n = 0}^{\infty} \frac{(-1)^n}{n!} \vec{r}^n \cdot \frac{\partial^n \WaveFunction(\vec{\Coordinate})}{\partial \vec{\Coordinate}^n}.
   \end{aligned}

Using this result, the translation operator can be identified as being equivalent to

.. math:: \op{T}(\vec{r}) = \sum_{n = 0}^{\infty} \frac{(-1)^n}{n!} \vec{r}^n \cdot \left(\frac{\partial}{\partial \vec{\Coordinate}}\right)^n.
   :label: eq:translation_summation

By comparing this with the Taylor series of the exponential function,

.. math:: \exp[\op{A}] = \sum_{n = 0}^{\infty} \frac{1}{n!} \op{A}^n,

the translation form :eq:`eq:translation_summation` can be rewritten as

.. math:: \op{T}(\vec{r}) = \exp\left[- \vec{r} \cdot \frac{\partial}{\partial \vec{\Coordinate}}\right].
   :label: eq:translation_exponent

The canonical momentum operator :math:`\op{\vec{\Momentum}}` can then be defined as the (vector) derivative (i.e., gradient) of the translation operator near the origin (with appropriate coefficients), that is,

.. math:: \op{\vec{\Momentum}} \equiv \eye\hbar \left.\frac{\partial \op{T}(\vec{r})}{\partial \vec{r}}\right|_{\vec{r} = \vec{0}}.
   :label: eq:operator_momentum_definition

For :eq:`eq:translation_exponent` to satisfy this, we must identify

.. math:: \op{\vec{\Momentum}} = -\eye\hbar \frac{\partial}{\partial \vec{\Coordinate}},

(as previously seen in :eq:`eq:operator_momentum_representation_coordinate`), with which the translation operator becomes

.. math:: \op{T}(\vec{r}) = \exp\left[- \frac{\eye}{\hbar} \vec{r} \cdot \op{\vec{\Momentum}}\right].
   :label: eq:translation_final

Some of the useful properties satisfied by this operator are as follows:

.. math::

   \begin{aligned}
       \text{(i):}& \quad &\op{T}(\vec{0}) &= \Identity,\\
       \text{(ii):}& &\op{T}(\vec{r})^\dagger &= \op{T}(\vec{r})^{-1} = \op{T}(-\vec{r}),\\
       \text{(iii):}& &\op{T}(\vec{r}_1)\op{T}(\vec{r}_2) &= \op{T}(\vec{r}_1 + \vec{r}_2),\\
       \text{(iv):}& &\op{T}(\vec{r}_1)\op{T}(\vec{r}_2) &= \op{T}(\vec{r}_2)\op{T}(\vec{r}_1).
   \end{aligned}

In classical mechanics, momentum is the generator of translation, which is exactly described by the result :eq:`eq:translation_final`. The factor of :math:`\eye` in the definition :eq:`eq:operator_momentum_definition` therefore serves to ensure that this final form of the translation operator is manifestly unitary, as required of any coordinate transformation on Hilbert space.

Expectation values and observables
==================================

Let :math:`\op{\Observable}` be a Hermitian operator on a Hilbert space :math:`\SpaceHilbert`. By definition, such operators are equal to their own Hermitian conjugate,

.. math:: \op{\Observable}^\dagger = \op{\Observable},

and so have real eigenvalues,

.. math:: \op{\Observable} \ket{\StatePure} = \Observable_{\StatePure} \ket{\StatePure}, \qquad \Observable_{\StatePure} \in \Reals \ \forall \ \ket{\StatePure} \in \SpaceHilbert.

By virtue of having real eigenvalues, Hermitian operators can represent observable quantities in quantum systems, and those that do are commonly called *observables*. These objects are so-named because they assign values, corresponding to the eigenvalues of the operator, to the outcomes of performing particular measurements on a system. If these outcomes represent physical states, then the eigenvalues are necessarily real. Note that not every Hermitian operator corresponds to a physically meaningful observable, nor are all such observables associated with *Hermitian* operators.

We can define the *expectation value* of an operator :math:`\op{\Observable}` in the state :math:`\ket{\WaveFunction}` as the scalar

.. math:: \langle \op{\Observable} \rangle_\WaveFunction \equiv \bra{\WaveFunction} \op{\Observable} \ket{\WaveFunction},
   :label: eq:observable_expectation

which corresponds to the mean of the :math:`\ket{\WaveFunction}` eigenvalues of :math:`\op{\Observable}` with eigenvector :math:`\ket{\WaveFunction}`. If :math:`\op{\Observable}` is an observable, then its expectation value can be interpreted as being the weighted average of all possible results of performing a measurement of :math:`\op{\Observable}` on :math:`\ket{\WaveFunction}`. Note however that this does not necessarily correspond to the most probable outcome, nor may it even be physical (i.e., not equal to any of the eigenvalues themselves).

By choosing a particular basis, the inner product can be expanded as per :eq:`eq:inner_product_continuous`. For example, in :math:`1`-dimensional configuration space :math:`\SpacePosition \subseteq \Reals`, we have

.. math:: \langle \op{\Observable} \rangle_\WaveFunction = \int_{\SpacePosition} \conj{\WaveFunction}(\Coordinate) \op{\Observable}_{\Coordinate} \WaveFunction(\Coordinate) \, \diff{\Coordinate},

where :math:`\op{\Observable}_{\Coordinate}` is the representation of the operator in the associated basis. Here, we used the inner product :eq:`eq:inner_product_continuous` and subsequently expanded the integral in position space. Note that this can similarly be expressed in alternative bases (such as momentum space), provided an appropriate representation of :math:`\op{\Observable}` in such spaces is known.

The position operator :eq:`eq:operator_coordinate_action` constitutes an observable which, in its own basis, has the expectation value

.. math:: \langle \op{\Coordinate} \rangle_\WaveFunction = \int_{\SpacePosition} \Coordinate \, \abs{\WaveFunction(\Coordinate)}^2 \, \diff{\Coordinate}.

This quantifies the most probable result of performing a position measurement on the system (e.g., the average location of a particle describe by the associated wave function). Similarly, for the momentum operator :eq:`eq:operator_momentum_action` in the same basis :eq:`eq:operator_momentum_representation_coordinate`,

.. math:: \langle \op{\Momentum} \rangle_\WaveFunction = -\eye\hbar \int_{\SpacePosition} \conj{\WaveFunction}(\Coordinate) \frac{\partial \WaveFunction(\Coordinate)}{\partial \Coordinate} \, \diff{\Coordinate}.

Using the expectation value :eq:`eq:observable_expectation`, the (squared) *standard deviation* of :math:`\op{\Observable}` can be constructed as

.. math:: \sigma_\Observable^2 = \langle \op{\Observable}^2 \rangle_\WaveFunction - \langle \op{\Observable} \rangle_\WaveFunction^2,

which quantifies the variance in the result of a measurement of :math:`\op{\Observable}` in the state :math:`\ket{\WaveFunction}` (about the value :math:`\langle \op{\Observable} \rangle_\WaveFunction`). From this, the standard deviations in the measurements of position and momentum are simply

.. math:: \sigma_\Coordinate = \sqrt{\langle \op{\Coordinate}^2 \rangle_\WaveFunction - \langle \op{\Coordinate} \rangle_\WaveFunction^2},

.. math:: \sigma_\Momentum = \sqrt{\langle \op{\Momentum}^2 \rangle_\WaveFunction - \langle \op{\Momentum} \rangle_\WaveFunction^2}.

It can be shown that these satisfy (*Heisenberg's*) *uncertainty principle*,

.. math:: \sigma_\Coordinate \sigma_\Momentum \geq \frac{\hbar}{2},

for any state :math:`\ket{\WaveFunction} \in \SpaceHilbert`. This inequality asserts that there is a fundamental limit to the precision with which a system's position and momentum can be known simultaneously. In classical mechanics, the position and momentum of any given system can be measured and known exactly, and so the inability for this to be accomplished in quantum mechanics constitutes a defining characteristic of the theory. The uncertainty principle therefore encapsulates a uniquely quantum phenomenon, one which is a quintessential component of the concept of wave-particle duality.

It is important to note that the uncertainty principle is not limited to just position and momentum---the standard deviations of any pair of canonically conjugate observables, e.g., :math:`\op{A}` and :math:`\op{B}`, can be shown to satisfy the general equality

.. math:: \sigma_A \sigma_B \geq \frac{1}{2} \abs{\langle [\op{A}, \op{B}] \rangle_\WaveFunction},

where we used the commutator :eq:`eq:commutator`. This holds for all states :math:`\WaveFunction` whose representations in the bases corresponding to the conjugate observables are normalized :math:`\SpaceLebesgue^2`-functions. For the particular case of (multidimensional) phase space, we have the *canonical conjugation relation*,

.. math:: [\op{\Coordinate}_i, \op{\Momentum}_j] = \eye\hbar \delta_{ij} \Identity,

where :math:`\op{\Coordinate}_i` and :math:`\op{\Momentum}_j` are the operators (in the same representation) corresponding to the :math:`i`\ th and :math:`j`\ th components of the canonical coordinates :math:`\vec{\Coordinate}` and canonical momenta :math:`\vec{\Momentum}`, respectively. This non-commutative property implies that no quantum state can be an eigenstate of both position and momentum simultaneously.

Time evolution
==============

Any such projection onto a basis in the manner of :eq:`eq:representation_coordinate` or :eq:`eq:representation_momentum` is, by the standard interpretation of quantum mechanics, termed the *wave function* of the associated system. Commonly, such a projection may be generalized to incorporate the state's time (:math:`\Time \in \Reals`) dependence,

.. math:: \WaveFunction(\vec{\Coordinate},\Time) = \braket{\vec{\Coordinate},\Time}{\WaveFunction},

which we interpret as the probability amplitude that the associated system (e.g., a particle) has position :math:`\vec{\Coordinate}` at time :math:`\Time`. Accordingly, the PDF is given by the Born rule :eq:`eq:Born_rule_continuous`,

.. math:: \Probability(\vec{\Coordinate},\Time) = \abs{\WaveFunction(\vec{\Coordinate},\Time)}^2,
   :label: eq:probability_density

which describes the probability of the particle's presence at and around the point :math:`(\vec{\Coordinate},\Time) \in \SpacePosition \times \Reals`.

Suppose we have some (closed) system which is described by the state :math:`\ket{\WaveFunction(\TimeInitial)}` defined on a complex Hilbert space at some initial time :math:`\TimeInitial`. By :eq:`eq:evolution_closed_pure`, the time evolution of this system over the interval :math:`\TimeInitial \rightarrow \TimeFinal` to some final state :math:`\ket{\WaveFunction(\TimeFinal)}` is described by the form

.. math:: \ket{\WaveFunction(\TimeFinal)} = \UnitaryTime(\TimeFinal,\TimeInitial)\ket{\WaveFunction(\TimeInitial)},
   :label: eq:evolution_time

where :math:`\UnitaryTime` is the *time-evolution operator*. In many cases, its dependence on time concerns only the difference of its two parameters (e.g., :math:`\TimeFinal - \TimeInitial`), and so can often be expressed in a one-parameter form, which has the action

.. math:: \ket{\WaveFunction(\Time + \TimeDelta)} = \UnitaryTime(\TimeDelta)\ket{\WaveFunction(\Time)}.

Given that we require the state :math:`\ket{\WaveFunction(\Time)}` to remain normalized for all :math:`\Time`, then :math:`\UnitaryTime` is required to be unitary. The transformation it facilitates from past to future must therefore be:

#. Invertible :math:`\implies` Information is conserved.

#. Norm-preserving :math:`\implies` Probability is conserved.

These facts imply that :math:`\UnitaryTime` may be expressed in general as the exponential map

.. math:: \UnitaryTime(\TimeFinal,\TimeInitial) = \mathcal{T} \left\{\exp\left[-\frac{\eye}{\hbar} \int_{\TimeInitial}^{\TimeFinal} \OperatorHamiltonian(\Time) \, \diff{\Time}\right]\right\},
   :label: eq:unitary_exponential_ordered

where, given that the Lie algebra of the unitary group is generated by Hermitian operators, :math:`\OperatorHamiltonian` is necessarily Hermitian. Here, the time-ordering symbol :math:`\mathcal{T}` permutes a product of :math:`N` non-commuting operators :math:`\{\op{A}_n\}_{n=1}^{N}` into the uniquely determined reordered expression

.. math:: \mathcal{T}\{\op{A}_1(\Time_1) \cdot \op{A}_2(\Time_2) \cdot \ldots \cdot \op{A}_N(\Time_N)\} = \op{A}_{i_N}(\Time_{i_N}) \cdot \ldots \cdot \op{A}_{i_2}(\Time_{i_2}) \cdot \op{A}_{i_1}(\Time_{i_1}), \quad \Time_{i_N} > \ldots > \Time_{i_2} > \Time_{i_1}.

This result is a causal chain of :math:`N` events where the primary *cause* in the past is :math:`\op{A}_{i_1}(\Time_{i_1})` while the future *effect* is :math:`\op{A}_{i_N}(\Time_{i_N})`. In the case where :math:`\OperatorHamiltonian` is time-independent, :eq:`eq:unitary_exponential_ordered` reduces to

.. math:: \UnitaryTime(\TimeFinal,\TimeInitial) = \exp\left[-\frac{\eye}{\hbar} (\TimeFinal-\TimeInitial)\OperatorHamiltonian \right].
   :label: eq:unitary_exponential

Substituting this form into the time-evolution equation :eq:`eq:evolution_time`, subsequently letting :math:`(\TimeFinal,\TimeInitial)\rightarrow(\Time,0)`, and then differentiating both sides with respect to :math:`\Time` yields

.. math:: \OperatorHamiltonian\ket{\WaveFunction(\Time)} = \eye\hbar\frac{\partial}{\partial \Time}\ket{\WaveFunction(\Time)}.
   :label: eq:Schrodinger

This is the (*time-dependent*) *Schrödinger equation*, which is perhaps one of the most fundamental and important equations of non-relativistic quantum mechanics. Here, we identify :math:`\OperatorHamiltonian` as the (time-independent) *Hamiltonian operator*, which corresponds to (or, more formally, has eigenvalues of) the total energy :math:`\Energy` of the state :math:`\WaveFunction`, i.e., :math:`\OperatorHamiltonian\ket{\WaveFunction} \equiv \Energy\ket{\WaveFunction}`. More explicitly, for any time-independent system, such as a particle with (classical) kinetic energy :math:`\Kinetic` in a static potential field :math:`\Potential`, the time-independent Hamiltonian may be written as the sum of the (similarly time-independent) total kinetic :math:`\OperatorKinetic` and potential :math:`\OperatorPotential` (operator) energies,

.. math:: \OperatorHamiltonian(\op{\vec{\Coordinate}},\op{\vec{\Momentum}}) = \OperatorKinetic(\op{\vec{\Coordinate}},\op{\vec{\Momentum}}) + \OperatorPotential(\op{\vec{\Coordinate}}),
   :label: eq:Hamiltonian_operator

where :math:`\op{\vec{\Coordinate}}` and :math:`\op{\vec{\Momentum}}` represent the canonical position and momentum vector operators, respectively.

Schrödinger's equation is a partial differential equation which governs the temporal evolution of any time-dependent quantum system describable by a state :math:`\ket{\WaveFunction(\Time)}`. It is a mathematical statement that encapsulates the notion that the time-independent Hamiltonian :math:`\OperatorHamiltonian` is the infinitesimal generator of a one-parameter group parametrized by the time :math:`\Time`, which is a special case of *Stone's theorem* (on one-parameter unitary groups). In other words, the time evolution of a state :math:`\ket{\WaveFunction(\TimeInitial)}` to a later state :math:`\ket{\WaveFunction(\TimeFinal)}` is generated by the Hamiltonian, and so Schrödinger's equation is the equation of motion that all physical non-relativistic systems are theoretically expected to obey.

The time-evolution operator's utility can be observed in many different contexts. For example, consider an arbitrary single-body system located at position :math:`\vec{\Coordinate}` at time :math:`\Time`. The state (or, more specifically, the position) of such a system can be defined in the :math:`\vec{\Coordinate}`-space basis as the vector

.. math:: \ket{\vec{\Coordinate},\Time} \equiv \UnitaryTime(\Time,0)\ket{\vec{\Coordinate}},

so that we may write the overlap between the past :math:`\ket{\vec{\CoordinateInitial},\TimeInitial}` and future :math:`\ket{\vec{\CoordinateFinal},\TimeFinal}` vectors as

.. math:: \braket{\vec{\CoordinateFinal},\TimeFinal}{\vec{\CoordinateInitial},\TimeInitial} = \bra{\vec{\CoordinateFinal}}\Unitary(\TimeFinal,\TimeInitial)\ket{\vec{\CoordinateInitial}}.
   :label: eq:propagator_overlap

Quantities of this form are commonly referred to as *transition amplitudes*.

.. _`sec:path-integral`:

The path-integral formulation
=============================

The *path-integral formulation* :cite:p:`ryder_quantum_1996, kleinert_path_2009` of quantum mechanics, also known as the *sum-over-histories* approach, is a formalism that generalizes the principle of stationary action (from classical mechanics) to quantum mechanics. It is based on the notion of the *propagator*,

.. math:: \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) \equiv \braket{\vec{\CoordinateFinal},\TimeFinal}{\vec{\CoordinateInitial},\TimeInitial},
   :label: eq:propagator

which is, in general, a generalized function (often specifically a kind of distribution), and is defined as per :eq:`eq:propagator_overlap`. Of its many properties and applications, the primary utility of the propagator lies in its ability to evolve a wave function :math:`\WaveFunction(\vec{\CoordinateInitial},\TimeInitial)` to a later state, e.g.,

.. math:: \WaveFunction(\vec{\CoordinateFinal},\TimeFinal) = \int_{\SpacePosition} \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) \, \WaveFunction(\vec{\CoordinateInitial},\TimeInitial) \, \diff^\Dimension{\vec{\CoordinateInitial}}, \qquad \TimeFinal > \TimeInitial.
   :label: eq:kernel

Here,

.. math:: \WaveFunction(\vec{\Coordinate},\Time) \equiv \braket{\vec{\Coordinate},\Time}{\WaveFunction}

is the wave function of the system in state :math:`\ket{\WaveFunction}` projected into some :math:`\Dimension`-dimensional :math:`\vec{\Coordinate}`-space (e.g., :math:`\SpacePosition = \Reals^\Dimension`) at time :math:`\Time`. From this perspective, the propagator can be identified as the *kernel* for the integral transform :eq:`eq:kernel` associated with time-dependent state evolution characterized by the differential operator

.. math:: \op{D} \equiv \OperatorHamiltonian - \eye\hbar\frac{\partial}{\partial \Time}

of the Schrödinger equation :eq:`eq:Schrodinger`. If the propagator's spatial dependence is only on the difference :math:`\vec{\CoordinateFinal} - \vec{\CoordinateInitial}`, then :eq:`eq:kernel` constitutes a convolution operation between the propagator and the wave function.

Given both :eq:`eq:propagator` and its relation to the time-evolution operator in :eq:`eq:propagator_overlap`, we can construct the form

.. math:: \Green(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) \equiv \Theta(\TimeFinal - \TimeInitial) \, \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial),
   :label: eq:green

where

.. math::

   \Theta(t) \equiv
       \begin{cases}
           1, & \text{if } t \geq 0; \\
           0, & \text{if } t < 0, \\
       \end{cases}

is the *Heaviside step function*. As this is the solution to the inhomogeneous variant of the Schrödinger equation :eq:`eq:Schrodinger`, i.e.,

.. math:: \left(\OperatorHamiltonian - \eye\hbar\frac{\partial}{\partial \Time}\right) \Green(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) = -\eye\hbar \, \delta^{(\Dimension)}(\vec{\CoordinateFinal} - \vec{\CoordinateInitial}) \, \delta(\TimeFinal - \TimeInitial),

then :math:`\Green` is called the *Green's function* for the Schrödinger equation, and can be used in the same way as the propagator. The sole difference between the two is the presence of the step function in the former, which ensures that only future-directed (i.e., :math:`\TimeFinal > \TimeInitial`) time evolutions are captured, as required of any physically meaningful process in non-relativistic quantum mechanics. If we insist however that the propagator :eq:`eq:propagator` definitionally vanishes when :math:`\TimeFinal < \TimeInitial`, then it is exactly equivalent to the Green's function :eq:`eq:green`.

Similar to how a wave function can describe the probability amplitude for a particle's location :math:`\vec{\Coordinate}` at time :math:`\Time`, we may say that the propagator :math:`\Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial)` is the probability amplitude for the transition of the particle from :math:`(\vec{\CoordinateInitial},\TimeInitial)` to :math:`(\vec{\CoordinateFinal},\TimeFinal)`. In :math:`\Dimension`-dimensional space, this transition could be accomplished through an infinite number of distinct trajectories. The *product rule* for the propagator, also known as the *causality relation*, characterizes how sequential evolutions, demarcated at time :math:`\Time^*`, can be merged by integrating over all intermediate positions :math:`\vec{\Coordinate}^*`,

.. math:: \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) = \int_{\SpacePosition} \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\Coordinate}^*,\Time^*) \, \Propagator(\vec{\Coordinate}^*,\Time^*;\vec{\CoordinateInitial},\TimeInitial) \, \diff^\Dimension{\vec{\Coordinate}^*}, \qquad \TimeFinal > \Time^* > \TimeInitial.
   :label: eq:propagator_product

In general, the propagator can be written as the *phase-space path integral* over all paths :math:`\vec{\Coordinate}(\Time)` and momentum evolutions :math:`\vec{\Momentum}(\Time)` from :math:`(\vec{\CoordinateInitial},\TimeInitial)` to :math:`(\vec{\CoordinateFinal},\TimeFinal)`,

.. math:: \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) = \int_{\vec{\CoordinateInitial}}^{\vec{\CoordinateFinal}} \DifferentialPath[\vec{\Coordinate}(\Time)] \, \int_{\vec{\MomentumInitial}}^{\vec{\MomentumFinal}} \frac{\DifferentialPath[\vec{\Momentum}(\Time)]}{(2\pi\hbar)^\Dimension} \, \e^{\eye \Action[\vec{\Coordinate}(\Time)]/\hbar},
   :label: eq:propagator_phase

where

.. math:: \Action[\vec{\Coordinate}(\Time)] \equiv \int_{\vec{\CoordinateInitial}}^{\vec{\CoordinateFinal}} \Lagrangian(\vec{\Coordinate}(\Time), \dot{\vec{\Coordinate}}(\Time), \Time) \, \diff{\Time}
   :label: eq:action

is the *action* of the path :math:`\vec{\Coordinate}(\Time)`, and

.. math::
   :label: eq:lagrangian

   \begin{aligned}
       \Lagrangian(\vec{\Coordinate}, \dot{\vec{\Coordinate}}, \Time) &\equiv \dot{\vec{\Coordinate}} \cdot \vec{\Momentum} - \Hamiltonian(\vec{\Coordinate}, \vec{\Momentum}, \Time) \\
       &= \Kinetic(\vec{\Coordinate}, \dot{\vec{\Coordinate}}, \Time) - \Potential(\vec{\Coordinate}, \Time)
   \end{aligned}

is the *Lagrangian*, as defined from a *Legendre transformation* of the classical Hamiltonian, with

.. math::

   \begin{aligned}
       \dot{\vec{\Coordinate}} &\equiv \frac{\partial \vec{\Coordinate}}{\partial \Time}, \\
       \vec{\Momentum} &\equiv \frac{\partial \Lagrangian}{\partial \dot{\vec{\Coordinate}}},
   \end{aligned}

being the velocity and canonical momentum, respectively. Here, we introduced the notation for the position and momentum differentials

.. math::
   :label: eq:differential_path_position

   \begin{aligned}
       \int_{\vec{\CoordinateInitial}}^{\vec{\CoordinateFinal}} \DifferentialPath[\vec{\Coordinate}(\Time)] &\equiv \lim\limits_{\Number \rightarrow \infty} \prod_{k=1}^{\Number-1} \int_{\SpacePosition} \diff^\Dimension{\vec{\Coordinate}_k},
   \end{aligned}

.. math::
   :label: eq:differential_path_momentum

   \begin{aligned}
       \int_{\vec{\MomentumInitial}}^{\vec{\MomentumFinal}} \DifferentialPath[\vec{\Momentum}(\Time)] &\equiv \lim\limits_{\Number \rightarrow \infty} \prod_{k=1}^{\Number-1} \int_{\SpacePosition} \diff^\Dimension{\vec{\Momentum}_k},
   \end{aligned}

which signify integration over all position :math:`\vec{\Coordinate}(\Time)` and momentum :math:`\vec{\Momentum}(\Time)` evolutions from :math:`(\vec{\CoordinateInitial}, \vec{\MomentumInitial})` to :math:`(\vec{\CoordinateFinal}, \vec{\MomentumFinal})` through the :math:`\Number + 1` subdivisions of the phase space. This discretization arises from the partitioning of the time coordinate into :math:`\Number + 1` "slices", i.e.,

.. math::

   \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) = \left(\prod_{k=1}^{\Number - 1} \int_{\SpacePosition} \diff^\Dimension{\vec{\Coordinate}_k}\right) \prod_{n=0}^{\Number - 1} \braket{\vec{\Coordinate}_{n+1},\Time_{n+1}}{\vec{\Coordinate}_{n},\Time_{n}},

as per :eq:`eq:propagator_product`. Here, :math:`\vec{\Coordinate}_n \equiv \vec{\Coordinate}(\Time_n)` represents the position of the particle at time :math:`\Time_n` (where :math:`n \in \Integers_{0}^{\Number}`), and we identified

.. math::

   \begin{aligned}
      (\vec{\Coordinate}_{0}, \Time_{0}) &\equiv (\vec{\CoordinateInitial}, \TimeInitial), \\
      (\vec{\Coordinate}_{\Number}, \Time_{\Number}) &\equiv (\vec{\CoordinateFinal}, \TimeFinal).
   \end{aligned}

It is only after taking the continuum limit that we are able to recover smooth dynamics as described by :eq:`eq:propagator_phase`.

For a system with a Hamiltonian whose dependence on momentum is purely quadratic, e.g.,

.. math:: \Hamiltonian(\vec{\Coordinate},\vec{\Momentum}) = \frac{\vec{\Momentum}^2}{2\Mass} + \Potential(\vec{\Coordinate}),

the integration over the momentum evolutions :math:`\vec{\Momentum}(\Time)` in :eq:`eq:propagator_phase` can be performed. Subsequently, the propagator reduces to the *configuration-space path integral*,

.. math:: \Propagator(\vec{\CoordinateFinal},\TimeFinal;\vec{\CoordinateInitial},\TimeInitial) = \int_{\vec{\CoordinateInitial}}^{\vec{\CoordinateFinal}} \bar{\DifferentialPath}[\vec{\Coordinate}(\Time)] \, \e^{\eye \Action[\vec{\Coordinate}(\Time)]/\hbar},
   :label: eq:propagator_configuration

where the "normalized" differential (compared to :eq:`eq:differential_path_position`) is defined as

.. math:: \int_{\vec{\Coordinate}_0}^{\vec{\Coordinate}_\Number} \bar{\DifferentialPath}[\vec{\Coordinate}(\Time)] \equiv \lim\limits_{\Number \rightarrow \infty} \left[\frac{\Mass}{2\pi\eye\hbar(\TimeFinal - \TimeInitial)}\right]^\frac{(\Number + 1)\Dimension}{2} \prod_{k=1}^{\Number-1} \int_{\SpacePosition} \diff^\Dimension{\vec{\Coordinate}_k}.
   :label: eq:differential_path_position_normalized

Here, :math:`\Mass` is the system's mass parameter. Note that this is an integral over *all* possible paths (both classical and quantum)---not just the classical path :math:`\classical{\vec{\Coordinate}}(\Time)` (i.e., that which satisfies the relevant classical equations of motion) with action :math:`\classical{\Action} \equiv \Action[\classical{\vec{\Coordinate}}(\Time)]`. This expression is often presented as the typical form of the path integral.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
