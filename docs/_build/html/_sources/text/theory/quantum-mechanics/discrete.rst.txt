.. include:: /styles.rst

.. _`sec:discrete`:

********************************************
Quantum mechanics on discrete Hilbert spaces
********************************************

The theory of *quantum mechanics* seeks to explain the dynamics of the particles of which our universe is composed. It differs from classical physics in that certain properties (such as energy and momentum) of bound systems are restricted to being within sets of discrete values---a characteristic known as *quantization*. Additionally, objects described by quantum mechanics have properties distinctive of both waves and particles (termed *wave-particle duality*), and there are fundamental limits to the accuracy with which values of specific physical quantities can be predicted prior to their measurement (described by the *uncertainty principle*). The theory presented here is based on the treatments in :cite:p:`nielsen_quantum_2010,zeidler_quantum_2006,wilde_quantum_2017,bengtsson_geometry_2017,williams_explorations_2010,dimock_quantum_2011,schlosshauer_decoherence_2007,moret-bonillo_adventures_2017,serrano_quantum_2022,dirac_principles_1982,yanofsky_quantum_2008`.

Quantum states
==============

In a formal setup, any system in the discrete theory of quantum mechanics is a collection of identifiable physical properties at a given time. This is represented by a Hilbert space, which may be either infinite- or finite-dimensional. A usual presentation of that Hilbert space is a special function space, such as :math:`\ell^2` or :math:`\Complexes^\Dimension`.

A *quantum state* is then simply a particular value (or, more properly, a probabilistic assignment) of these properties. It is this object which provides the probability distribution for the outcomes of each possible measurement on a system. Formally, we say that a quantum state represents (or is characterized by) a statistical ensemble :math:`\SetProbability = \{p_i\}_i` of independent, identically prepared copies of a quantum system. This is represented in general by a positive semi-definite Hermitian operator :math:`\StateDensity` of trace one (that is, a density operator) on the (discrete) Hilbert space :math:`\SpaceHilbert`. As the space of all density operators on :math:`\SpaceHilbert` is convex, then subsequently any convex combination of such operators is also a density operator, which allows us to express any :math:`\StateDensity` as

.. math:: \StateDensity = \sum_{i} p_i \StateDensity_i.
   :label: eq:state_general

This describes a mixture of the density operators :math:`\{\StateDensity_i\}_i` corresponding to the statistical ensemble :math:`\SetProbability`. According to the spectral theorem :eq:`eq:spectral_theorem`, we are able to express any quantum state :math:`\StateDensity` in a :math:`\Dimension`-dimensional Hilbert space :math:`\SpaceHilbert` equivalently as a convex combination of at most :math:`\Dimension` vectors :math:`\ket{\psi_i}`, i.e.,

.. math:: \StateDensity = \sum_{i} p_i \ket{\psi_i}\bra{\psi_i}
   :label: eq:state_combination_pure

where the coefficients :math:`p_i` collectively characterize :math:`\StateDensity`.

Pure states
-----------

An extreme point in the convex space spanned by operators :eq:`eq:state_general` is called a *pure state*, which we can denote in general as the outer product

.. math:: \StateDensity = \ket{\psi}\bra{\psi}.
   :label: eq:state_pure

This is necessarily a projection operator, i.e., :math:`\StateDensity^2 = \StateDensity`. Due to this form, any given pure state can be completely (and uniquely) represented by the vector

.. math:: \ket{\psi} = \sum_{i} c_i \ket{\Basis_i}
   :label: eq:state_superposition

where :math:`\{\ket{\Basis_i}\}_i` is an orthonormal basis for the associated Hilbert space, and :math:`c_i \in \Complexes` are the state-characterizing probability amplitudes.

The set of physical pure states :math:`\SpacePure(\SpaceHilbert)` on a Hilbert space :math:`\SpaceHilbert` is the set of all normalized (unit) vectors on :math:`\SpaceHilbert`, with vectors equal up to a global phase considered to be equivalent (as such global phase differences are not observable, i.e., constitute measurable quantities). Compactly, we write

.. math:: \SpacePure(\SpaceHilbert) \equiv \bigl\{ \ket{\psi} \in \SpaceHilbert : \norm{\ket{\psi}}_2 = 1, \, \ket{\psi} \cong \e^{\eye \theta} \ket{\psi} \, \, \forall \, \, \theta \in \Reals \bigr\}.

.. note::

   The concept of vectors which differ only up to a multiplicate constant of magnitude :math:`1` (i.e., a phase factor :math:`\e^{\eye \theta}`) being identified is a direct consequence of the fact that such states are physically indistinguishable---that is, there is no performable experiment which is able to differentiate them. This leads to the idea that the notion of a pure "state" in quantum mechanics is perhaps better described by a more complete (and unique) object called a *ray*, residing in a projective Hilbert space. Put simply, a ray :math:`\underline{\StatePure}` is the set of all state vectors :math:`\StatePure` which are scalar non-zero multiples of each other, i.e.,

   .. math:: \underline{\StatePure} = \bigl\{\e^{\eye \theta} \StatePure : \StatePure \in \SpaceHilbert, \, \norm{\psi}_2 = 1, \, \theta \in \Reals \bigr\}.

   The vectors in this set are all physically equivalent and called *representants* of :math:`\underline{\StatePure}`. For example, if :math:`\psi \in \underline{\psi}`, then :math:`\phi` is also a representant of :math:`\underline{\psi}` if and only if :math:`\phi = \e^{\eye \theta}\psi` for some :math:`\theta \in \Reals`, and therefore corresponds to the same physical state. In fact, in this formalism, a (pure) "quantum state" is more properly identified as the ray itself, not just a (single) vector. Given a Hilbert space :math:`\SpaceHilbert`, any two :math:`\psi_1,\psi_2 \in \SpaceHilbert` satisfy the equivalence relation :math:`\psi_1 \sim \psi_2` if and only if :math:`\psi_1,\psi_2 \in \underline{\psi}`. As such, the rays of :math:`\SpaceHilbert` form the equivalence classes of this equivalence equation, which correspond physically to distinguishable quantum states. Thus, when we (imprecisely) describe a quantum state using a vector :math:`\ket{\StatePure}` in the context of quantum mechanics, we systematically use any one element of the corresponding ray as its representant, albeit with the specific choice being completely inconsequential to any predictions of the theory.

Mixed states
------------

States which are not pure are termed *mixed*, and cannot be expressed in the form :eq:`eq:state_pure`. A mixed state characterized by a uniform probability distribution :math:`\SetProbability` is called *maximally mixed* and takes the form

.. math:: \StateDensity = \frac{1}{\Dimension}\Identity_{\Dimension}

where :math:`\Identity_{\Dimension}` is the :math:`\Dimension \times \Dimension` identity operator. It is useful to think of linear combinations such as that in :eq:`eq:state_combination_pure` as "classical" superpositions in the sense that they involve the correspondingly classical mixing of otherwise fully quantum-mechanical states :math:`\StateDensity_i = \ket{\psi_i}\bra{\psi_i}`. In other words, a mixed quantum state is a *statistical ensemble* of pure states, and is also known simply as a *mixed ensemble*. Importantly, this contrasts with the physically distinct notion of *quantum superposition*, which is encapsulated by :eq:`eq:state_superposition`.

Unlike pure states, mixed states cannot be represented as a state vector (e.g., :math:`\ket{\psi}`). Both objects however may be described as a density operator (e.g., :math:`\StateDensity`), which serves as a generalization of the concept of state vectors (wave functions). The set of physical density operators (including both pure and mixed states) on a Hilbert space :math:`\SpaceHilbert` is the set of all Hermitian trace-one (linear) operators on :math:`\SpaceHilbert`, and we denote this as

.. math:: \SpaceMixed(\SpaceHilbert) \equiv \bigl\{ \StateDensity \in \SpaceLinear(\SpaceHilbert) : \StateDensity^\dagger = \StateDensity, \, \trace[\StateDensity] = 1 \bigr\}.

Density operators representing mixed (impure) quantum states arise in quantum mechanics in two distinct situations. The first of these is when the preparation of a system is not fully known. In this case, the (incomplete/limited) knowledge of the quantum state can be captured only by a density operator that describes a statistical (i.e., mixture) of all possible preparations. The second situation is when one wants to describe a physical system that is entangled with another. Quantum entanglement theoretically prevents the existence of complete knowledge about subsystems in an entangled state, and so it is impossible to represent the state of any such subsystems as a pure state.

.. note::

   A useful concept in the formalism of quantum information theory is that of *purification*. This process refers to the fact that any mixed state in a finite-dimensional Hilbert space can be viewed as the reduced state of some pure state. To see this, let :math:`\StateDensity \in \SpaceMixed(\SpaceHilbert_A)` be a density matrix where :math:`\dim(\SpaceHilbert_A)` is finite. Given this, it is always possible to introduce an additional Hilbert space :math:`\SpaceHilbert_B`, corresponding to a fictitious system often called a *reference* system (and has no direct physical significance), alongside a pure state :math:`\ket{\psi} \in \SpacePure(\SpaceHilbert_A \otimes \SpaceHilbert_B)` such that

   .. math:: \trace_B \bigl[\ket{\psi}\bra{\psi}\bigr] = \StateDensity.
      :label: eq:purification

   We say that :math:`\ket{\psi}` *purifies* :math:`\StateDensity`, which is a consequence that is only made possible by the fact that we have access to a larger (composite) Hilbert space.

.. _`sec:qubits`:

Qubits
------

Many physical applications of this theory in quantum mechanics involve Boolean (i.e., binary, or two-valued) logic, which is describable completely by a pair of orthonormal vectors that are often labelled :math:`\ket{0}` and :math:`\ket{1}`. The representations in :math:`\Complexes^2` of these vectors is typically the pair

.. math:: \ket{0} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \qquad \ket{1} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.
   :label: eq:basis_qubit

Together, these form a computational basis that is canonically known as the :math:`z`-basis (and is referred to by many simply as the *computational* basis), given that each is an eigenvector of the Pauli-:math:`Z` operator :math:`\Pauli_z` :eq:`eq:Pauli`. Any quantum state with such binary dimensionality is called a *qubit* (though this nomenclature is often used solely in the context of *pure* binary states), and describes a two-level system that forms the basic unit of quantum information (analogous to the bit in classical computing). In the computational basis :math:`\{\ket{0},\ket{1}\}`, the simplest qubit which we can express is the quantum superposition

.. math:: \ket{\StateVector} = \alpha\ket{0} + \beta\ket{1}, \quad \abs{\alpha}^2 + \abs{\beta}^2 = 1, \quad \alpha,\beta \in \Complexes.
   :label: eq:vector_qubit

In the :math:`\Complexes^2`-representation :eq:`eq:basis_qubit`, this state can be expressed as

.. math:: \ket{\StateVector} = \alpha \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \beta \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} \alpha \\ \beta \end{bmatrix}.
   :label: eq:vector_qubit_column

An alternative parametrisation of the qubit vector state :eq:`eq:vector_qubit` takes the form

.. math:: \ket{\StateVector} = \e^{\eye\varsigma}\left[\cos\biggl(\frac{\vartheta}{2}\biggr)\ket{0} + \e^{\eye\varphi}\sin\biggl(\frac{\vartheta}{2}\biggr)\ket{1}\right], \quad \varsigma,\vartheta,\varphi \in \Reals.
   :label: eq:vector_qubit_sphere

Given that the factor :math:`\e^{\eye\varsigma}` represents a global phase, then all states with fixed :math:`\vartheta,\varphi` but different :math:`\varsigma` are physically equivalent, and so this factor can be disregarded. We are therefore left with a parametrization of a qubit wherein the numbers :math:`\vartheta` and :math:`\varphi` define a point on the surface of a unit sphere, known as the *Bloch sphere* (illustrated in :numref:`fig:diagram_bloch_sphere`). This is essentially a unique mapping of the :math:`2`-dimensional Hilbert space to the :math:`3`-dimensional real space :math:`\Reals^3` (with basis vectors :math:`\{\uv{e}_1,\uv{e}_2,\uv{e}_3\}`), which is accomplished by choosing the antipodal points on unit sphere in :math:`\Reals^3` to correspond to the pair of mutually orthogonal basis vectors :math:`\ket{0}` and :math:`\ket{1}`. In this sense, the qubit state :math:`\vec{r}_\StateVector \in \Reals^3`, which corresponds to its Hilbert space counterpart :eq:`eq:vector_qubit`, may be written exactly as

.. math:: \vec{r}_\StateVector = \sin(\vartheta)\cos(\varphi)\uv{e}_1 + \sin(\vartheta)\sin(\varphi)\uv{e}_2 + \cos(\vartheta)\uv{e}_3.

Similarly, a :math:`2`-dimensional density operator :math:`\StateDensity` in the same representation corresponds to the vector

.. math:: \vec{r}_{\StateDensity} = \trace[\StateDensity \Pauli_1]\uv{e}_1 + \trace[\StateDensity \Pauli_2]\uv{e}_2 + \trace[\StateDensity \Pauli_3]\uv{e}_3

where

.. math::
   :label: eq:Pauli

   \begin{aligned}
       \Pauli_1 &= \Pauli_x \equiv \ket{0}\bra{1} + \ket{1}\bra{0} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \\
       \Pauli_2 &= \Pauli_y \equiv -\eye \ket{0}\bra{1} + \eye \ket{1}\bra{0} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & -\eye \\ \eye & 0 \end{bmatrix}, \\
       \Pauli_3 &= \Pauli_z \equiv \ket{0}\bra{0} - \ket{1}\bra{1} \!\!\!\!\!\! & &= \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix},
   \end{aligned}

are the *Pauli matrices*.

.. only:: html

   .. figure:: /figures/output/diagram_bloch_sphere-dark.png
      :scale: 36 %
      :alt: A diagram of the Bloch sphere.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/diagram_bloch_sphere-light.png
      :scale: 36 %
      :alt: A diagram of the Bloch sphere.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/diagram_bloch_sphere-light.png
   :name: fig:diagram_bloch_sphere
   :scale: 36 %
   :alt: A diagram of the Bloch sphere.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The Bloch sphere.

The Pauli matrices :math:`\{\Pauli_k\}_{k=1}^{3}` are Hermitian, and so represent observables in the context of quantum mechanics. Together with the identity operator (writing :math:`\Pauli_0 = \Identity_2`), the set :math:`\{\Pauli_\mu\}_{\mu=0}^{3}` forms a complete basis for the space of complex :math:`2 \times 2` matrices. Since this coincides with the space of linear operators :math:`\SpaceLinear(\SpaceHilbert)` on a qubit Hilbert space :math:`\SpaceHilbert`, then any (density) operator :math:`\StateDensity \in \SpaceLinear(\SpaceHilbert)` can be expressed as the linear combination

.. math:: \StateDensity = \frac{1}{2}\sum_{\mu=0}^{3} \trace[\Pauli_\mu \StateDensity]\Pauli_\mu.
   :label: eq:matrix_qubit

In the context of density operators, since the coefficient for :math:`\mu = 0` in :eq:`eq:matrix_qubit` is fixed by normalization (i.e., :math:`\trace[\Pauli_0 \StateDensity] = 1`), then the state :math:`\StateDensity` is completely (and uniquely) determined by the *Bloch vector*, which is defined, for an :math:`\Dimension`-dimensional state, as the :math:`(\Dimension^2 - 1)`-dimensional real vector of parameters :math:`\trace[\Pauli_k \StateDensity]` (for :math:`k \geq 1`). Accordingly, the linear combination :eq:`eq:matrix_qubit` is said to be the *Bloch sphere representation* of the state :math:`\StateDensity`. Note also of course that any appropriate basis, not just the Pauli basis (with identity), allows for reconstruction of any qubit state in the manner of :eq:`eq:matrix_qubit`.

The Bloch vector provides a complete description of a quantum system because it represents the expectation values of specific informationally complete observables. In general, a complex :math:`\Dimension \times \Dimension` density matrix, which represents the state of an :math:`\Dimension`-dimensional quantum system, is geometrically equivalent to a vector in an :math:`(\Dimension^2 - 1)`-dimensional real space. This is because the space of density matrices is a (bounded) convex subset of :math:`\Reals^{\Dimension^2}`, with its elements possessing certain properties (namely Hermiticity, positive semi-definiteness, and trace equal to :math:`1`). Since this real space coincides with that of the (generalized) *Bloch ball*, including both the surface (the *Bloch sphere*, on which points correspond to pure states) and interior (in which points correspond to mixed states), then this is why determination of the Bloch vector is equivalent to identification of the quantum state. Therefore, as the Pauli operators form a set of informationally complete observables for qubit systems, then the inclusion of the identity operator to this set yields a *tomographically complete* basis for the space of :math:`2 \times 2` Hermitian matrices, of which the space of :math:`2`-dimensional density matrices is a subset.

.. _`sec:qutrits`:

Qutrits
-------

Quantum states realized by :math:`3`-dimensional systems are commonly known as *qutrits*. These objects are analogous to the "trit" unit of information in classical computing and so are useful for performing calculations with ternary logic. Such systems are typically described using a set of orthonormal (basis) vectors :math:`3`-dimensional :math:`\{\ket{0},\ket{1},\ket{2}\}` , with which a qutrit can in general be expressed as

.. math:: \ket{\StateVector} = \alpha\ket{0} + \beta\ket{1} + \gamma\ket{2}, \quad \abs{\alpha}^2 + \abs{\beta}^2 + \abs{\gamma}^2 = 1, \quad \alpha,\beta,\gamma \in \Complexes.
   :label: eq:vector_qutrit

In the :math:`\Complexes^3`-representation, the basis vectors can take the form

.. math:: \ket{0} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \qquad \ket{1} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \qquad \ket{2} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix},
   :label: eq:basis_qutrit

with which :eq:`eq:vector_qutrit` can be rewritten as

.. math:: \ket{\StateVector} = \alpha \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + \beta \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + \gamma \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} \alpha \\ \beta \\ \gamma \end{bmatrix}.
   :label: eq:vector_qutrit_column

Qutrits described by :math:`3`-dimensional density operators have corresponding representations as :math:`3 \times 3` density matrices. One way of expressing such a state is via the linear combination

.. math:: \StateDensity = \frac{1}{3}\sum_{\mu=0}^{8} \trace[\GellMann_\mu \StateDensity]\GellMann_\mu.
   :label: eq:matrix_qutrit

where :math:`\{\Pauli_\mu\}_{\mu=0}^{3}` is a complete basis for the space of :math:`3 \times 3` complex matrices. Perhaps the most notable choice of matrices with which to construct a such a basis are the *Gell-Mann matrices*,

.. math::
   :label: eq:Gell-Mann

   \begin{aligned}
       \GellMann_1 &\equiv \ket{0}\bra{1} + \ket{1}\bra{0} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \\
       \GellMann_2 &\equiv -\eye\ket{0}\bra{1} + \eye \ket{1}\bra{0} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & -\eye & 0 \\ \eye & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \\
       \GellMann_3 &\equiv \ket{0}\bra{0} - \ket{1}\bra{1} \!\!\!\!\!\! & &= \begin{bmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \\
       \GellMann_4 &\equiv \ket{0}\bra{2} + \ket{2}\bra{0} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix}, \\
       \GellMann_5 &\equiv -\eye\ket{0}\bra{2} + \eye\ket{2}\bra{0} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & 0 & -\eye \\ 0 & 0 & 0 \\ \eye & 0 & 0 \end{bmatrix}, \\
       \GellMann_6 &\equiv \ket{2}\bra{3} + \ket{3}\bra{2} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \\
       \GellMann_7 &\equiv -\eye\ket{2}\bra{3} + \eye\ket{3}\bra{2} \!\!\!\!\!\! & &= \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & -\eye \\ 0 & \eye & 0 \end{bmatrix}, \\
       \GellMann_8 &\equiv \frac{1}{\sqrt{3}}\bigl(\ket{0}\bra{0} + \ket{1}\bra{1} - 2\ket{2}\bra{2}\bigr) \!\!\!\!\!\! & &= \frac{1}{\sqrt{3}}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -2 \end{bmatrix},
   \end{aligned}

in addition to :math:`\GellMann_0 \equiv \Identity_3`.

.. _`sec:qudits`:

Qudits
------

Quantum vector states in a :math:`\Dimension`-dimensional Hilbert space :math:`\SpaceHilbert_\Dimension` can in general be expressed as the superposition

.. math:: \ket{\StateVector} = \sum_{i=0}^{\Dimension - 1} c_i \ket{i}, \quad \sum_{i=0}^{\Dimension - 1} \abs{c_i}^2 = 1, \quad c_i \in \Complexes.
   :label: eq:vector_qudit

which is often referred to as a *qudit*. Here, :math:`\{\ket{i}\}_{i=0}^{\Dimension - 1}` is a vector basis for :math:`\SpaceHilbert_\Dimension`, and may be expressed in a :math:`\Complexes^\Dimension`-representation using the vectors in :eq:`eq:basis_qudit`. With this, we can write :eq:`eq:vector_qudit` as

.. math:: \ket{\StateVector} = c_0 \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix} + c_1 \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix} + \ldots + c_{\Dimension - 1} \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix} = \begin{bmatrix} c_0 \\ c_1 \\ \vdots \\ c_{\Dimension - 1} \end{bmatrix}.
   :label: eq:vector_qudit_column

Just like in the cases of qubits and qutrits, general :math:`\Dimension`-dimensional states described by density operators can be expressed via a linear combination of the form

.. math:: \StateDensity = \frac{1}{\Dimension}\sum_{\mu=0}^{\Dimension^2 - 1} \trace[\GellMann_\mu \StateDensity]\GellMann_\mu.
   :label: eq:matrix_qudit

In order for this to be true, the matrices :math:`\{\GellMann_\mu\}_{\mu=0}^{\Dimension^2 - 1}` must form a basis for the space of :math:`\Dimension \times \Dimension` density matrices. Though there are multiple ways to find such a basis, doing so is a non-trivial task. Our construction here closely follows the work of :cite:p:`thew_qudit_2002`, in which a suitable generalization of the Gell-Mann (or Pauli) matrices :eq:`eq:Gell-Mann` is obtained.

We begin by introducing the elementary matrices :math:`\{\Basis_{i}^{j}\}_{i,j = 1}^{\Dimension}` which satisfy

.. math:: (\Basis_{i}^{j})_{nm} = \delta_{ni} \delta_{mj}, \qquad 1 \leq n \leq d, \quad 1 \leq m \leq d.

This defines a total of :math:`\Dimension^2` matrices, each of which possesses one entry equal to unity and all others equal to zero. Using these, we can construct :math:`\Dimension (\Dimension - 1)` traceless off-diagonal matrices,

.. math::
   :label: eq:generators_off-diagonal
   
   \begin{aligned}
       \alpha_{i}^{j} &= \Basis_{i}^{j} + \Basis_{j}^{i} \\
       \beta_{i}^{j} &= -\eye(\Basis_{i}^{j} - \Basis_{j}^{i}), \qquad 1 \leq j < i \leq d
   \end{aligned}

and :math:`\Dimension - 1` traceless diagonal matrices,

.. math:: \gamma_{j}^{j} = \sqrt{\frac{2}{j(j+1)}} \left[\sum_{k=1}^{j} \Basis_{k}^{k} - j \Basis_{j+1}^{j+1}\right].
   :label: eq:generators_on-diagonal

In total, we obtain :math:`\Dimension^2 - 1` traceless matrices. Note that these matrices are in fact the generators of :math:`\mathrm{SU}(\Dimension)` (the group of :math:`\Dimension \times \Dimension` unitary matrices with determinant :math:`1`), meaning that they form a basis for the corresponding Lie algebra :math:`\mathfrak{su}(\Dimension)` (the space of :math:`\Dimension \times \Dimension` traceless Hermitian matrices). As the space of :math:`\Dimension \times \Dimension` Hermitian matrices has a real dimensionality of :math:`\Dimension^2`, then the difference between this space and :math:`\mathfrak{su}(\Dimension)` is a single degree of freedom that accounts for the ability of the matrices in the former to be non-traceless. This missing property can be incorporated into the latter by including the :math:`\Dimension`-dimensional identity matrix :math:`\Identity_\Dimension` into any of its valid bases. In other words, the set of matrices that consists of both the generators of :math:`\mathrm{SU}(\Dimension)` and the identity :math:`\Identity_\Dimension` necessarily forms a basis for the entire space of :math:`\Dimension \times \Dimension` Hermitian matrices (both traceless and non-traceless).

With this in mind, we can use :eq:`eq:generators_off-diagonal` and :eq:`eq:generators_on-diagonal` to assemble a set of matrices,

.. math::
   
   \begin{aligned}
       \GellMann_{(i-1)^2 + 2(j - 1)} &\equiv \alpha_{i}^{j}, \\
       \GellMann_{(i-1)^2 + 2j - 1} &\equiv \beta_{i}^{j}, \\
       \GellMann_{i^2 - 1} &\equiv \gamma_{i-1}^{i-1}.
   \end{aligned}

These matrices are known as the *generalized Gell-Mann matrices*. In conjunction with the identity matrix :math:`\GellMann_0 \equiv \Identity_\Dimension`, they form a suitable basis for the space of :math:`\Dimension`-dimensional Hermitian matrices, meaning that any density matrix can indeed be expressed as the linear combination :eq:`eq:matrix_qudit` using this basis.

Quantum quantities
==================

Purity
------

The mixedness of a state may be quantified by the *purity* function,

.. math:: \Purity(\StateDensity) \equiv \trace[\StateDensity^2],

which defines a measure on the degree by which a state deviates from being (completely) pure. The purity of normalized :math:`\Dimension`-dimensional states is bounded from above by :math:`1` (perfect purity) and below by :math:`\frac{1}{\Dimension}` (maximal mixing), e.g.,

.. math:: \frac{1}{\Dimension} \leq \Purity(\StateDensity) \leq 1,

and so a state :math:`\StateDensity` is pure if and only if :math:`\Purity(\StateDensity) = 1` (else it has some degree of mixing).

Trace distance
--------------

The *trace distance* is a metric on the space of density matrices, thereby providing a measure of the "distance" (or distinguishability) between two states. It is a generalization of the *Kolmogorov distance* for classical probability distributions to quantum density operators, and is defined for any two such operators :math:`\op{\rho}` and :math:`\op{\tau}` as

.. math:: \TraceDistance(\op{\rho},\op{\tau}) \equiv \frac{1}{2} \trace \bigl| \op{\rho} - \op{\tau} \bigr|.
   :label: eq:trace_distance

Here, we defined :math:`\bigl| \op{A} \bigr| \equiv \sqrt{\op{A}^\dagger\op{A}}` to be the absolute value of an operator :math:`\op{A}`. Being a metric, the trace distance between density operators is always non-negative, i.e.,

.. math:: \TraceDistance(\op{\rho},\op{\tau}) \geq 0,

with equality (with zero) if and only if :math:`\op{\rho} = \op{\tau}`. It is also necessarily symmetric, e.g., :math:`\TraceDistance(\op{\rho},\op{\tau}) = \TraceDistance(\op{\tau},\op{\rho})`, and satisfies the *triangle inequality*, e.g.,

.. math:: \TraceDistance(\op{\rho},\op{\tau}) \leq \TraceDistance(\op{\rho},\op{\sigma})  + \TraceDistance(\op{\sigma},\op{\tau}),

for all density operators :math:`\op{\rho}`, :math:`\op{\tau}`, and :math:`\op{\sigma}`. In the case of normalized quantum states, the trace distance is bounded from above by unity, e.g.,

.. math:: 0 \leq \TraceDistance(\op{\rho},\op{\tau}) \leq 1.

Fidelity
--------

Another measure between two quantum states is the *fidelity*, which characterizes their similarity or "closeness". It is defined for two density operators :math:`\op{\rho}` and :math:`\op{\tau}` as

.. math:: \Fidelity(\op{\rho},\op{\tau}) \equiv \left(\trace\sqrt{\sqrt{\op{\rho}} \, \op{\tau}\sqrt{\op{\rho}}}\right)^2,
   :label: eq:fidelity

where the square roots of :math:`\op{\rho}` and :math:`\sqrt{\op{\rho}}\op{\tau}\sqrt{\op{\rho}}` (both positive-semidefinite matrices) are well-defined by the spectral theorem :eq:`eq:spectral_theorem`. While the fidelity is not a suitable metric on the space of density matrices, it still provides many of the properties that are expected of a useful distance measure. For example, it is non-negative for any input, e.g.,

.. math:: 0 \leq \Fidelity(\op{\rho},\op{\tau}) \leq 1,

with equivalence to its upper bound of unity if and only if :math:`\op{\rho} = \op{\tau}`.

The fidelity expressed in :eq:`eq:fidelity` is the original, traditional form that is often cumbersome to use and inefficient to compute. Simpler yet equivalent reformulations are therefore desired, and perhaps the most encountered of such expressions is

.. math:: \Fidelity(\op{\rho},\op{\tau}) \equiv \left(\trace\abs{\sqrt{\op{\rho}} \, \sqrt{\op{\tau}}}\right)^2,

where :math:`\bigl| \op{A} \bigr| \equiv \sqrt{\op{A}^\dagger\op{A}}`. Recent work :cite:p:`baldwin_efficiently_2023, muller_simplified_2023` has shown that, by leveraging the fact that the trace of a diagonalizable square matrix is equal to the sum of its eigenvalues, an even simpler expression for the fidelity can be written as

.. math:: \Fidelity(\op{\rho},\op{\tau}) \equiv \left(\trace\sqrt{\op{\rho} \op{\tau}}\right)^2,

which holds true regardless of whether :math:`\op{\rho}` and :math:`\op{\tau}` do or do not commute.

In the case where either density matrix is pure, we can write

.. math::

   \Fidelity(\op{\rho},\op{\tau}) = \trace[\op{\rho}\op{\tau}] =
       \begin{cases}
           \bra{\psi_\rho}\op{\tau}\ket{\psi_\rho} & \text{when } \op{\rho} = \ket{\psi_\rho}\bra{\psi_\rho}; \\
           \bra{\psi_\tau}\op{\rho}\ket{\psi_\tau} & \text{when } \op{\tau} = \ket{\psi_\tau}\bra{\psi_\tau}; \\
       \end{cases}

which further reduces to the overlap

.. math:: \Fidelity(\op{\rho},\op{\tau}) = \abs{\braket{\psi_\rho}{\psi_\tau}}^2

when both states are pure.

Lastly, note that an alternative definition of the fidelity exists that specifies the same expression as :eq:`eq:fidelity` except without the square, i.e.,

.. math:: \Fidelity(\op{\rho},\op{\tau}) \equiv \trace\sqrt{\sqrt{\op{\rho}} \, \op{\tau}\sqrt{\op{\rho}}}.

This form, sometimes called the *root fidelity*, shares many of the same properties as :eq:`eq:fidelity`, but is ostensibly less common in the literature.

Entropy
-------

In statistical physics, the concept of *entropy* commonly provides a quantification of how much uncertainty there is in the state of a physical system. In other words, it characterizes the "amount" of mixedness of a quantum state (that is, the degree to which the state is mixed). For quantum systems, the standard measure of entropy is the *von Neumann entropy*, defined for an arbitrary state :math:`\StateDensity` as

.. math:: \Entropy(\StateDensity) \equiv -\trace[\StateDensity \log_\Base \StateDensity].
   :label: eq:entropy

This definition can be equivalently expressed as

.. math:: \Entropy(\StateDensity) = -\sum_{k} \lambda_k \log_\Base \lambda_k
   :label: eq:entropy_eigenvalues

where :math:`\lambda_k` denote the non-zero eigenvalues in the spectrum of :math:`\StateDensity`. Here, the matrix logarithm is taken to base :math:`\Base`, which is the dimensionality of the unit of information in which the entropy is measured. For example, if :math:`\Base = 2`, then :math:`\Entropy(\StateDensity)` will be measured in "bits". Many definitions of the von Neumann entropy alternatively specify :math:`\Base = \e`, for which the entropy is measured in so-called "nats".

The von Neumann entropy is the quantum counterpart of the *Shannon entropy* in classical information theory. For a pure state, it is always zero, while for a mixed state, it is strictly positive with an upper bound of :math:`\log_\Base \Dimension` (achieved with a maximally mixed state) in a unipartite :math:`\Dimension`-dimensional Hilbert space. Mathematically, we can write

.. math:: 0 \leq \Entropy(\StateDensity) \leq \log_\Base \Dimension

with :math:`\Entropy(\StateDensity) = 0` if and only if :math:`\StateDensity` is pure.

The quantum *relative entropy* provides a measure of distinguishability between two quantum density matrices, and is defined as

.. math::
   :label: eq:entropy_relative

   \begin{aligned}
       \Entropy(\op{\rho} \Vert \op{\tau}) &\equiv -\trace[\op{\rho} \log_\Base \op{\tau}] - \Entropy(\op{\rho}) \\
       &= \trace\bigl[\op{\rho}(\log_\Base \op{\rho} - \log_\Base \op{\tau})\bigr],
   \end{aligned}

where :math:`\op{\rho}` and :math:`\op{\tau}` are arbitrary quantum states of the same dimensionality. It is analogous to the notion of relative entropy from classical information theory, wherein it characterizes the "distance" between two probability distributions. *Klein's inequality* states that the quantum relative entropy is non-negative, i.e.,

.. math:: \Entropy(\op{\rho} \Vert \op{\tau}) \geq 0,

for any two density matrices :math:`\op{\rho}` and :math:`\op{\tau}`, with equality if and only if :math:`\op{\rho} = \op{\tau}`.

Mutual information
------------------

The quantum *mutual information* is a measure of correlation between the subsystems of a multipartite quantum system. Let :math:`\op{\rho}^{A,B}` be a bipartite state for a composite system with Hilbert space :math:`\SpaceHilbert_A \otimes \SpaceHilbert_B`, and let

.. math::

   \begin{aligned}
       \op{\rho}^{A} &\equiv \trace_B[\op{\rho}^{A,B}], \\
       \op{\rho}^{B} &\equiv \trace_A[\op{\rho}^{A,B}],
   \end{aligned}

be the reduced states on subsystems :math:`A` and :math:`B`, respectively. Using these, we can define the mutual information between these subsystems as

.. math:: \MutualInformation(A : B) \equiv \Entropy(\op{\rho}^{A}) + \Entropy(\op{\rho}^{B}) - \Entropy(\op{\rho}^{A,B}),

where :math:`\Entropy(\op{\rho})` is the von Neumann entropy of a state :math:`\op{\rho}` as defined in :eq:`eq:entropy`. An equivalent expression uses the relative entropy :eq:`eq:entropy_relative` to write

.. math:: \MutualInformation(A : B) = \Entropy(\op{\rho}^{A,B} \Vert \op{\rho}^{A} \otimes \op{\rho}^{B}).

The quantum mutual information is analogous to the *Shannon mutual information* in classical information theory. It is a non-negative quantity, i.e.,

.. math:: \MutualInformation(A : B) \geq 0,

with equality if and only if the subsystems are independent (and are thus uncorrelated).

Separability and entanglement
=============================

A vector state :math:`\ket{\psi} \in \SpacePure(\SpaceHilbert_0 \otimes \SpaceHilbert_1 \otimes \ldots \otimes \SpaceHilbert_{N - 1})` over :math:`N` subsystems is called *separable* or a *product state* if it can be written in the form

.. math::

   \begin{aligned}
       \ket{\psi} &= \ket{\psi_0} \otimes \ket{\psi_1} \otimes \ldots \otimes \ket{\psi_{N - 1}} \\
       &= \bigotimes_{n=0}^{N - 1} \ket{\psi_n},
   \end{aligned}

where :math:`\ket{\psi_n} \in \SpacePure(\SpaceHilbert_n)` is a vector state on the :math:`n`-th subsystem. Similarly, a mixed state :math:`\StateDensity \in \SpaceMixed(\SpaceHilbert_0 \otimes \SpaceHilbert_1 \otimes \ldots \otimes \SpaceHilbert_{N - 1})` over :math:`N` subsystems is separable if it can be expressed as

.. math::

   \begin{aligned}
       \StateDensity &= \sum_{k} p_k \StateDensity_k^0 \otimes \StateDensity_k^1 \otimes \ldots \otimes \StateDensity_k^{N - 1} \\
       &= \sum_{k} p_k \bigotimes_{n=0}^{N - 1} \StateDensity_k^n,
   \end{aligned}

where :math:`\StateDensity_k^n \in \SpaceMixed(\SpaceHilbert_n)` are density operators representing the :math:`n`-th subsystem, and the coefficients :math:`p_k` are non-negative real numbers that collectively satisfy :math:`\sum_{k} p_k = 1`. If there exists only a single non-zero :math:`p_k`, then the state is called *simply separable* or, similarly to the separable vector state case, a *product state*.

A quantum state that is not separable (*non-separable*) is said to be *entangled*. The corresponding phenomenon, *quantum entanglement*, is one of the most fascinating features of quantum mechanics. It manifests physically as quantum correlations (of various quantum properties such as observable quantities) between the individual subsystems of a composite quantum system. For example, a group of particles is entangled when the quantum state of each individual particle cannot be described independently of the state of the other particles in a collective description. This behaviour is realized to varying degrees in many different kinds of physical situations, including most interestingly when the particles are spacelike separated.

Quantum entanglement is also necessarily characterized by *unrealized* correlations, such that the outcomes of measurements on the quantum system(s) are completely undecided until the measurement occurs. This means that the very act of performing a measurement on one subsystem of an entangled composition affects the entire system as a whole (i.e., apparent and irreversible collapse of the wave function). Though any such influence occurs seemingly instantaneously, quantum entanglement however does not allow any information to propagate superluminally (i.e., faster than the speed of light), despite the possibility that the subsystems of an entangled system are spacelike separated.

A quantum system is said to be *maximally entangled* if it cannot be separated into pure states on each of its subsystems. This can only occur between exactly two particles, which is to say that a single particle cannot be maximally entangled with more than one other particle at a time. This is a property called *monogamy*, and is a restriction that results in perfect quantum correlations between any two such entangled subsystems. For qubits, the maximally entangled states are the *Bell states*, of which there are four:

.. math::
   :label: eq:Bell_state

   \begin{aligned}
       \ket{\Phi^+} &\equiv \frac{1}{\sqrt{2}} \bigl(\ket{0} \otimes \ket{0} + \ket{1} \otimes \ket{1} \bigr), \\
       \ket{\Phi^-} &\equiv \frac{1}{\sqrt{2}} \bigl(\ket{0} \otimes \ket{0} - \ket{1} \otimes \ket{1} \bigr), \\
       \ket{\Psi^+} &\equiv \frac{1}{\sqrt{2}} \bigl(\ket{0} \otimes \ket{1} + \ket{1} \otimes \ket{0} \bigr), \\
       \ket{\Psi^-} &\equiv \frac{1}{\sqrt{2}} \bigl(\ket{0} \otimes \ket{1} - \ket{1} \otimes \ket{0} \bigr).
   \end{aligned}

For systems composed of three or more subsystems (e.g., particles), any multipartite entanglement that manifests cannot be maximal as in the bipartite case (due to the monogamy), but still exists in many quantitatively different types. An example of an entangled three-qubit system is the *Greenberger-Horne-Zeilinger (GHZ) state*,

.. math:: \ket{\mathrm{GHZ}} = \frac{1}{\sqrt{2}} \bigl(\ket{0} \otimes \ket{0} \otimes \ket{0} + \ket{1} \otimes \ket{1} \otimes \ket{1}\bigr).
   :label: eq:GHZ_state

Discarding (tracing out) any of its subsystems results in a separable state. Dissimilarly, for the three-qubit *W state*,

.. math:: \ket{\mathrm{W}} = \frac{1}{\sqrt{3}} \bigl(\ket{0} \otimes \ket{0} \otimes \ket{1} + \ket{0} \otimes \ket{1} \otimes \ket{0} + \ket{1} \otimes \ket{0} \otimes \ket{0}\bigr),
   :label: eq:W_state

discarding any single subsystem yields a bipartite state that is still entangled.

Quantum operations
==================

A *quantum operation* is a linear, trace-non-increasing, completely positive map

.. math:: \MapGeneral : \StateDensity \mapsto \MapGeneral[\StateDensity] \in \SpaceMixed(\SpaceHilbert).

It is convenient to express such maps using the general form

.. math:: \MapGeneral[\StateDensity] = \sum_{i} \Kraus^\dagger_i \StateDensity \Kraus_i

where :math:`\SetKraus = \{\Kraus_i\}` is a set of linear operators, known as *Kraus operators*. The characteristic of *trace-non-increasing* is the requirement that :math:`\trace[\StateDensity] \geq \trace\bigl[\MapGeneral[\StateDensity]\bigr]`. Since it is (almost) always assumed that the input state :math:`\StateDensity` satisfies :math:`\trace[\StateDensity] = 1`, then the Kraus operators of a trace-non-increasing quantum operation in turn satisfy

.. math:: \sum_{i} \Kraus^\dagger_i \Kraus_i \leq \Identity.

In the case of equivalence, the operation is said to be *complete* (and *trace-preserving*), otherwise it is *incomplete* (and *trace-decreasing*). An operation :math:`\MapGeneral[\StateDensity]` is also said to be *physical* if it satisfies

.. math:: 0 \leq \trace\bigl[\MapGeneral[\StateDensity]\bigr] \leq 1.
   
Quantum operations are fundamental to an information-theoretic treatment of quantum mechanics as they provide the general basic formalism by which both state evolution and measurement can be described.

Quantum evolutions
==================

In quantum mechanics, the term *evolution* refers to the transformation (either continuous or discrete) of quantum states over some parameter space (usually time). In general, there are two fundamentally distinct types of quantum evolution: those of which are *closed*, and those of which are *open*.

Closed quantum systems
----------------------

In a closed quantum system, the evolution of a quantum state :math:`\StateDensity` is described simply by a unitary transformation :math:`\Unitary` of the state, which can be expressed as the quantum operation

.. math:: \MapGeneral[\StateDensity] = \Unitary\StateDensity\Unitary^\dagger.
   :label: eq:evolution_closed_mixed

This is naturally a trace-preserving map, that is, :math:`\trace\bigl[\MapGeneral[\StateDensity]\bigr]=\trace[\StateDensity]`, since :math:`\Unitary` is a unitary operator. In the specific case of a state that is initially a vector, we have

.. math:: \MapGeneral[\psi] = \Unitary\ket{\psi}.
   :label: eq:evolution_closed_pure

Perhaps the most prevailing example is the time evolution of the state :math:`\ket{\psi}`, which is describable by a unitary of the form

.. math:: \Unitary(\Time) = \exp\left[-\frac{\eye}{\hbar}\OperatorHamiltonian\Time\right]

where :math:`\Time` is the time duration, :math:`\OperatorHamiltonian` is a Hermitian operator corresponding to the Hamiltonian of the system, and :math:`\hbar` is the reduced Planck constant.

Open quantum systems
--------------------

In an open quantum system, the evolution :math:`\MapGeneral[\StateDensity]` of a quantum state :math:`\StateDensity` is described by the trace-preserving quantum operation

.. math:: \MapGeneral[\StateDensity] = \sum_{i} \Kraus_i \StateDensity \Kraus^\dagger_i
   :label: eq:evolution_open

where the Kraus operators are given by

.. math:: \Kraus_i = \bra{\Basis_i}\Unitary\ket{\psi}.

This form, which is sometimes called the *operator-sum representation*, describes the evolution of some system in the Hilbert space :math:`\SpaceHilbert_\mathrm{S}` that interacts with an environment system (a separate system with Hilbert space :math:`\SpaceHilbert_\mathrm{E}`) some unitary :math:`\Unitary`. In this bipartite setup, the environment is initially in the state :math:`\ket{\psi}` (with :math:`\{\ket{\Basis_i}\}` denoting an orthonormal basis). Dropping the assumption that the environment is initially pure, we may in general write

.. math:: \MapGeneral[\StateDensity] = \trace_\mathrm{E} \bigl[\Unitary(\StateDensity_\mathrm{S} \otimes \op{\tau}_\mathrm{E})\Unitary^\dagger\bigr]

where :math:`\op{\tau}` is the environment state. The output of the environment under this evolution is complementarily given by

.. math:: \tilde{\MapGeneral}[\op{\tau}] = \trace_\mathrm{S} \bigl[\Unitary(\StateDensity_\mathrm{S} \otimes \op{\tau}_\mathrm{E})\Unitary^\dagger\bigr].

Quantum operations of this kind, i.e., those which are both completely positive (CP) and trace-preserving (TP), are known as *CPTP maps* or, more popularly, *quantum channels*. Note however that there is no loss in generality in making the assumption that the environment is in a pure state, since it can always be purified by the introduction of an additional system.

Quantum measurements
====================

A *quantum measurement* of a quantum state is expressible in general as the map

.. math:: \MapGeneral_i[\StateDensity] = \Kraus_i \StateDensity \Kraus^\dagger_i.

Here, :math:`\{\Kraus_i\}` are Kraus operators which necessarily satisfy the completeness relation

.. math:: \sum_{i} \Kraus^\dagger_i \Kraus_i = \Identity

since all possible measurement values together must necessarily form a complete quantum operation. Note that by writing the form

.. math:: \Kraus_i = \Unitary_i \sqrt{\op{M}_i}

where :math:`\SetUnitary = \{\Unitary_i\}` is a set of unitary operators and :math:`\SetObservable = \{\op{M}_i\}` is a set of positive operators, we can, due to the relation :math:`\Kraus^\dagger_i \Kraus_i = \op{M}_i` and the completeness of the Kraus operators, conclude that

.. math:: \sum_i \op{M}_i = \Identity.

The set :math:`\SetObservable` is therefore called a *quantum observable*, or more formally, a *positive operator-valued measure* (POVM), and has an associated probability distribution :math:`\SetProbability = \{p_i\}` given by

.. math:: p_i = \trace[\StateDensity\op{M}_i] = \trace[\Kraus_i \StateDensity \Kraus^\dagger_i].

Given that preservation of the trace cannot be guaranteed under the measurement, then accordingly the post-measurement state :math:`\StateDensity^\prime` can be normalized if required, i.e.,

.. math:: \StateDensity^\prime = \frac{\MapGeneral_i[\StateDensity]}{\trace\bigl[\MapGeneral_i[\StateDensity]\bigr]}.

This is to ensure that a physical post-measurement state is always recovered, which is to say that :math:`\trace[\StateDensity^\prime] = 1`. Quantum measurement can therefore be thought as the extension of the concept of trace-non-preserving quantum operations to include normalization, the procedure of which makes it distinct from such ordinary quantum operations (being necessarily linear). In essence, a quantum measurement describes the probability of obtaining a particular outcome of a quantum operation on a system, in addition to the change in the state of that affected system. If however the result of the measurement is lost, then the post-measurement quantum state is (probabilistically) the sum of all possible outcomes (without renormalization) of the associated POVM,

.. math:: \StateDensity^\prime = \sum_{i} \Kraus_i \StateDensity \Kraus^\dagger_i.

This defines a linear, trace-preserving, completely positive map.

A quantum observable :math:`\SetObservable = \{\op{\Pi}_i\}` is said to be *sharp* if, in addition to having positive operators, each operator :math:`\op{\Pi}_i` is a projector, that is, :math:`\op{\Pi}_i = \op{\Pi}^2_i`. According to the spectral theorem :eq:`eq:spectral_theorem`, every Hermitian operator :math:`\op{H}` may be expressed as

.. math:: \op{H} = \sum_i \lambda_i \op{\Pi}_i

with eigenvalues :math:`\lambda_i`. This means that the entire observable :math:`\SetObservable` is representable by the single Hermitian operator :math:`\op{H}`, which is why such operators are typically referred to simply as *observables* in standard quantum theory. Given this expression, the probability of measuring an eigenvalue :math:`\lambda_i` is given by

.. math:: p_i = \trace[\StateDensity \op{\Pi}_i],

which is known as the *Born rule*, and is one of the key principles of quantum mechanics. Accordingly, the *expected value* of the associated observable is simply

.. math:: \langle\op{H}\rangle = \trace[\StateDensity \op{H}].

.. _`sec:integrals`:

Integrals over quantum states
=============================

Let :math:`\SpaceHilbert` denote the Hilbert space for a :math:`\Dimension`-dimensional quantum system. The integral over quantum states :math:`\StateDensity \in \SpaceMixed(\SpaceHilbert)` is defined :cite:p:`bengtsson_geometry_2017,allen_treating_2014` as

.. math:: \Integral = \int_{\SpaceMixed(\SpaceHilbert)} \diff[\StateDensity] \, \FunctionIntermediate(\StateDensity) 
   :label: eq:integral_mixed

where :math:`\FunctionIntermediate : \SpaceMixed(\SpaceHilbert) \rightarrow \Complexes` is any scalar function, and :math:`\diff[\StateDensity]` is the integration measure over :math:`\SpaceMixed(\SpaceHilbert)`. To compute the integral, an explicit form of the measure must be defined, and we are typically free to choose any such form in accordance with what we wish to accomplish. In the case of mixed states :math:`\StateDensity \in \SpaceMixed(\SpaceHilbert)`, there is in fact no unique natural measure on :math:`\SpaceMixed(\SpaceHilbert)`. One must therefore be chosen (along with a way to parametrize :math:`\StateDensity`), which means that that is no unique, natural way to define the integral :math:`\Integral`, as it will depend on the choice of measure used.

For the specific case of pure states :math:`\ket{\StateVector} \in \SpacePure(\SpaceHilbert)` however, we are able to define both a suitable measure and parametrization. Given some :math:`\FunctionIntermediate : \SpacePure(\SpaceHilbert) \rightarrow \Complexes`, the integral over pure states :cite:p:`bengtsson_geometry_2017,allen_treating_2014` is

.. math:: \Integral = \int_{\SpacePure(\SpaceHilbert)} \diff[\StateVector] \, \FunctionIntermediate(\StateVector) 
   :label: eq:integral_pure

An important class of unitary transformations consists of random unitary matrices distributed according to the Haar measure on the group of :math:`\Dimension\times\Dimension` unitary matrices :math:`\GroupUnitary(\Dimension)`. This is significant for our purposes, as conveniently there exists a unique, natural measure over :math:`\SpacePure(\SpaceHilbert)` that is invariant under such transformations, and perhaps the best way to write this is in the Hurwitz parametrization :cite:p:`hurwitz_uber_1897,zyczkowski_induced_2001,bengtsson_geometry_2017`. Let us first introduce the Bloch sphere parametrization, often used for qubits, which involves the rotationally invariant area measure on a (unit) :math:`2`-sphere:

.. math::

   \begin{aligned}
       \ket{\StateVector} &= \sin(\vartheta)\ket{0} + \e^{\eye\varphi}\cos(\vartheta)\ket{1},\\
       \diff[\StateVector] &\propto \sin(2\vartheta) \, \diff(2\vartheta) \, \diff\varphi.
   \end{aligned}

The Hurwitz parametrization is then simply a generalization of this Bloch sphere parametrization to :math:`\Dimension`-dimensional (pure) states. Therefore, given some orthonormal basis :math:`\{\ket{\mu}\}_{\mu=0}^{\Dimension - 1}` of :math:`\SpaceHilbert`, any pure state :math:`\ket{\StateVector} \in \SpacePure(\SpaceHilbert)` may be expressed in this parametrization as

.. math:: \ket{\StateVector} = \prod_{\nu=\Dimension - 1}^{1} \sin(\vartheta_\nu) \ket{0} + \sum_{\mu = 1}^{\Dimension - 2} \e^{\eye \varphi_\mu}\cos(\vartheta_\mu) \prod_{\nu = \Dimension - 1}^{\mu + 1} \sin(\vartheta_\nu) \ket{\mu} + \e^{\eye \varphi_{\Dimension - 1}} \cos(\vartheta_{\Dimension - 1}) \ket{\Dimension - 1} 
   :label: eq:Hurwitz_state

for parameters :math:`\vartheta_\mu \in [0,\tfrac{\pi}{2}]` and :math:`\varphi_\mu \in [0,2\pi)`. The corresponding integration measure (unique up to a multiplicative constant) in this parametrization takes the form

.. math:: \diff[\StateVector(\vartheta_\mu,\varphi_\mu)] = \prod_{\mu = 1}^{\Dimension - 1} \cos(\vartheta_\mu) \, \sin^{2\mu - 1}(\vartheta_\mu) \, \diff\vartheta_\mu \, \diff\varphi_\mu, 
   :label: eq:Hurwitz_measure

which provides a natural measure for integrating over pure quantum states. Importantly, this is invariant under unitary operations, so that under :math:`\ket{\StateVector} \rightarrow \Unitary\ket{\StateVector}`, the measure transforms as :math:`\diff[\StateVector] \rightarrow \diff[\Unitary\StateVector] = \diff[\StateVector]`.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
