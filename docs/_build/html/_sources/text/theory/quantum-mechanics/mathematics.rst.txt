.. include:: /styles.rst

.. _`sec:mathematics`:

*********************************************
Mathematical foundations of quantum mechanics
*********************************************

Quantum mechanics, one of the cornerstones of our modern view of reality, is founded on the mathematical formalism of linear algebra, which itself is built upon structures known as vector spaces. The following mathematical preliminaries have been adapted from :cite:p:`nielsen_quantum_2010,zeidler_quantum_2006,audretsch_entangled_2007,dimock_quantum_2011,shankar_principles_2012,ohya_mathematical_2011,ballentine_quantum_2014,holevo_quantum_2012,watrous_theory_2018,prugovecki_quantum_1982,hiai_introduction_2014,dirac_principles_1982`.

Vector spaces
=============

A (linear) *vector space* over a field :math:`\Fields` is a non-empty set :math:`\SpaceVector` which is closed under the operations of addition and scalar multiplication. This is to say that, for elements (termed *vectors*) :math:`\psi, \phi, \chi \in \SpaceVector`, closure under addition requires the following axioms to be satisfied:

.. math::
   :label: eq:vector_identities

   \begin{aligned}
       \text{(i) } &\text{(commutativity):} &\psi + \phi &= \phi + \psi,\\
       \text{(ii) } &\text{(associativity):} &\psi + (\phi + \chi) &= (\psi + \phi) + \chi,\\
       \text{(iii) } &\text{(identity):} &\exists! \ \vec{0} \in \SpaceVector \quad \text{such that} \quad \psi + \vec{0} &= \psi.
   \end{aligned}

Similarly, :eq:`eq:vector_identities` given some scalars :math:`a,b,c \in \Fields`, closure under multiplication with a scalar likewise requires

.. math::

   \begin{aligned}
       \text{(i) } &\text{(distributivity over }\SpaceHilbert\text{):} &c(\psi + \phi) &= c\phi + c\psi,\\
       \text{(ii) } &\text{(distributivity in }\Fields\text{):} &(a+b)\psi &= a\psi + b\psi,\\
       \text{(iii) } &\text{(identity):} &\exists! \ 1 \in \Fields \quad \text{such that} \quad 1\psi &= \psi.
   \end{aligned}

Formally, we say that :math:`\SpaceVector` is an :math:`\Fields`-vector space if it is an (additive) Abelian group with a function (scalar multiplication) :math:`\Fields \times \SpaceVector \rightarrow \SpaceVector` which satisfies the above axioms.

A subset of vectors :math:`\{\Basis_i\}_{i=1}^{\Dimension}` in :math:`\SpaceVector` is said to be *linearly independent* if and only if the equation

.. math:: \sum_{i=1}^{\Dimension}c_i\Basis_i = 0

has the sole solution :math:`c_i = 0` for all :math:`n` (where :math:`c_i \in \Fields`). Otherwise, the set of vectors is said to be *linearly dependent*. The *dimension* of a vector space :math:`\SpaceVector`, denoted by :math:`\dim(\SpaceVector)`, is defined as the least upper bound of linearly independent vectors in :math:`\SpaceVector`. Informally, this is the largest possible number of linearly independent vectors which reside in :math:`\SpaceVector`. A vector space is said to have infinite dimension if there is no such largest number.

Furthermore, a subset :math:`\{\Basis_i\}_{i=1}^{\Dimension}` is said to *span* the vector space :math:`\SpaceVector` if and only if every vector :math:`\psi \in \SpaceVector` can be expressed as a (finite) linear combination of the form

.. math:: \psi = \sum_{i=1}^{\Dimension} \psi_i \Basis_i
   :label: eq:linear_combination

where :math:`\psi_i \in \Fields` collectively characterize the vector :math:`\psi`. To this end, we often write

.. math:: \psi = (\psi_i)_{i=1}^{\Dimension} = (\psi_1,\psi_2,\ldots,\psi_\Dimension)^\transpose.

Moreover, if :math:`\{\Basis_i\}_{i=1}^{\Dimension}` is both linearly independent and spans :math:`\SpaceVector`, then this subset is a (vector) *basis* for :math:`\SpaceVector`, and its linear combinations are unique.

Inner product space
-------------------

Let :math:`\SpaceVector` be a vector space over :math:`\Complexes`. Such a vector space is an *inner product space* if it is equipped with an *inner product*, which is defined as the positive-definite symmetric bilinear map

.. math:: \inner{{}\cdot{}}{{}\cdot{}} : \SpaceVector \times \SpaceVector \rightarrow \Complexes.
   :label: eq:inner_map

that by definition obeys

.. math::
   :label: eq:inner_axioms

   \begin{aligned}
       \text{(i) } &\text{(conjugate symmetry):} &\inner{\phi}{\psi} &= \conj{\inner{\psi}{\phi}}{}, \\
       \text{(ii) } &\text{(linearity):} &\inner{\phi}{a\psi} &= a\inner{\phi}{\psi},\\
       \text{(iii) } &\text{(additivity):} &\inner{\phi}{\psi + \chi} &= \inner{\phi}{\psi} + \inner{\phi}{\chi}, \\
       \text{(iv) } &\text{(positive-definiteness):} &\inner{\psi}{\psi} &> 0 \quad \text{if} \quad \psi \neq \vec{0}. 
   \end{aligned}

Here, :math:`\conj{z}{}` is the complex conjugate of :math:`z\in\Complexes`. Note that together :eq:`eq:inner_axioms`-(i) and :eq:`eq:inner_axioms`-(ii) imply that the definition is *antilinear* in its first argument, e.g., :math:`\inner{a\phi}{\psi} = \conj{a}{}\inner{\phi}{\psi}`, which aligns with the convention in the physics literature.

A pair of vectors :math:`\psi,\phi \in \SpaceVector` are *orthogonal* if

.. math:: \inner{\phi}{\psi} = 0.

Furthermore, a set of vectors :math:`\{\phi_i\}_{i=1}^{\Dimension}` is said to be *orthonormal* with respect to the inner product :eq:`eq:inner_map` if

.. math:: \inner{\phi_i}{\phi_j} = \delta_{ij}

where

.. math::

   \delta_{ij} \equiv
       \begin{cases}
           0 & \text{when } i \neq j; \\
           1 & \text{when } i = j.
       \end{cases}

is the *Kronecker delta*. Orthonormality is a useful property: given an orthonormal basis :math:`\{\Basis_i\}_{i=1}^{\Dimension}`, the coefficients in the linear expansion :eq:`eq:linear_combination` may be (uniquely) determined by taking the inner product, i.e.,

.. math:: \inner{\Basis_i}{\psi} = \inner{\Basis_i}{\sum_{j=1}^{\Dimension} \psi_j \Basis_j } = \sum_{j=1}^{\Dimension}\psi_j\inner{\Basis_i}{\Basis_j} = \psi_i.

Using this, we may rewrite the linear combination :eq:`eq:linear_combination` as

.. math:: \psi = \sum_{i=1}^{\Dimension} \inner{\Basis_i}{\psi} \Basis_i,

with which we can express the inner product of two vectors as

.. math:: \inner{\phi}{\psi} = \sum_{i=1}^{\Dimension} \inner{\phi}{\Basis_i} \inner{\Basis_i}{\psi} = \sum_{i=1}^{\Dimension} \conj{\phi_i}{} \psi_i.
   :label: eq:inner_expansion

Vector norm
-----------

The vector :math:`p`-*norm* is a (non-negative-valued) map

.. math:: \norm{{}\cdot{}}_p : \SpaceVector \rightarrow \Reals

which characterizes the notion of the "length" of a vector. With :math:`p \geq 1`, it is defined for any :math:`\psi \in \SpaceVector` as

.. math:: \norm{\psi}_p = \left[\sum_{i=1}^{\Dimension}\abs{\psi_i}^p\right]^{\frac{1}{p}},

and possesses the following properties:

.. math::

   \begin{aligned}
       \text{(i) } &\text{(scalar multiplication):} &\norm{c\psi}_p &= \abs{c} \norm{\psi}_p,\\
       \text{(ii) } &\text{(positive-definiteness):} &\norm{\psi}_p &> 0 \quad \text{if} \quad \psi \neq \vec{0},\\
       \text{(iii) } &\text{(triangle inequality):} &\norm{\psi + \phi}_p &\leq \norm{\psi}_p + \norm{\phi}_p.
   \end{aligned}

*Hölder's inequality* provides a useful relation between the inner product of two vectors :math:`\psi,\phi \in \SpaceVector` and their :math:`p`-norms,

.. math:: \inner{\psi}{\phi} \leq \norm{\psi}_p \norm{\phi}_q, \quad \frac{1}{p} + \frac{1}{q} = 1.
   :label: eq:Holder

A vector :math:`\psi \in \SpaceVector` is said to be *normalized* if

.. math:: \norm{\psi}_p = 1

for any :math:`p\geq 0`.

An inner product is an important tool because it defines a way to multiply vectors together, with the result being a scalar. A useful consequence of this is our ability to define the 2-norm as

.. math:: \norm{\psi}_2 = \sqrt{\inner{\psi}{\psi}},
   :label: eq:norm-2

which, given an orthonormal basis :math:`\{\Basis_i\}_{i=1}^{\Dimension}` and the expansion :eq:`eq:inner_expansion`, yields *Parseval's identity*,

.. math:: \norm{\psi}_2 = \sqrt{\sum_{i=1}^{\Dimension} \abs{\inner{\Basis_i}{\psi}}^2}.
   :label: eq:Parseval

Additionally, in the case if :math:`p=2`, Hölder's inequality :eq:`eq:Holder` becomes the *Cauchy-Schwarz inequality*,

.. math:: \inner{\psi}{\phi} \leq \norm{\psi}_2 \norm{\phi}_2 = \sqrt{\inner{\psi}{\psi}} \sqrt{\inner{\phi}{\phi}}.
   :label: eq:Cauchy-Schwarz

Dual space
----------

Any vector space :math:`\SpaceVector` has a corresponding *dual vector space* :math:`\dual{\SpaceVector}{}`, which is the space of all linear forms (functionals) on :math:`\SpaceVector`. Mathematically, this is to say that an element :math:`\varphi \in \dual{\SpaceVector}{}` defines a map

.. math:: \varphi : \psi \mapsto \varphi(\psi) \in \Complexes

for every :math:`\psi \in \SpaceVector` such that

.. math:: \varphi(a\psi + b\chi) = a\varphi(\psi) + b\varphi(\chi)

for all :math:`\psi,\chi` and :math:`a,b \in \Complexes`. Elements of the dual space :math:`\dual{\SpaceVector}{}` are often termed *covectors*, and the space itself becomes a vector space when equipped with addition and scalar multiplication, that is,

.. math::

   \begin{aligned}
       \text{(i) } &\text{(additivity):} &(\varphi_1 + \varphi_2)(\psi) &= \varphi_1(\psi) + \varphi_2(\psi),\\
       \text{(ii) } &\text{(scalar multiplication):} &(c\varphi)(\psi)&= c\varphi(\psi),
   \end{aligned}

for all :math:`\varphi, \varphi_1, \varphi_2 \in \dual{\SpaceVector}{}`, :math:`\psi \in \SpaceVector`, and :math:`c \in \Complexes`.

The most straightforward way of constructing linear maps in a dual space is to use the inner product: given some vector :math:`\phi \in \SpaceVector`, we may define a map :math:`\inner{\phi}{{}\cdot{}} \in \dual{\SpaceVector}{}` which has the action

.. math:: \inner{\phi}{{}\cdot{}} : \psi \mapsto \inner{\phi}{\psi}.
   :label: eq:dual_map

Being based on the inner product, this form is guaranteed to be linear in its argument.

Hilbert space
-------------

An inner product vector space equipped with a norm is called a *normed space*. A sequence :math:`(\psi_i)_{n=1}^{\infty}` in such a space is termed a *Cauchy sequence* if

.. math:: \norm{\psi_i - \psi_j}_p \rightarrow 0 \quad \text{as} \quad i,j\rightarrow\infty.

If all Cauchy sequences converge (as per the above condition) in :math:`\SpaceVector`, then the normed space :math:`\SpaceVector` is said to be *complete*. This is to say that there exists a vector :math:`\psi\in\SpaceVector` such that

.. math:: \lim_{i\rightarrow\infty}\norm{\psi_i - \psi}_p = 0.

A complete normed space is called a *Banach space*.

The special case of a normed inner product space that is complete with respect to the 2-norm :eq:`eq:norm-2` is known as a *Hilbert space*. This construction is central to the formalism of quantum theory. The *Riesz representation theorem* establishes that any linear map :math:`\varphi : \SpaceHilbert \rightarrow \Complexes` can be *uniquely* written as :eq:`eq:dual_map` for some fixed choice of :math:`\phi \in \SpaceHilbert`. Consequently, the inner product provides a vector space isomorphism

.. math:: \dual{\SpaceHilbert}{} \cong \SpaceHilbert,
   :label: eq:Hilbert_isomorphism

regardless of the dimensionality of :math:`\SpaceHilbert`. Importantly, this holds true for infinite-dimensional Hilbert spaces, which makes them especially easy to work with.

The simplest Hilbert space :math:`\SpaceHilbert` is one which has a finite number of dimensions :math:`\Dimension \in \IntegersPositive`. In this case, we have :math:`\SpaceHilbert \cong \Complexes^\Dimension`, and such a space is always isomorphic to one with the inner product :eq:`eq:inner_expansion` and corresponding norm :eq:`eq:Parseval`. In physics, finite-dimensional Hilbert spaces often arise as idealized descriptions of phenomena that would otherwise require more complex treatment. This usually appears where one is concerned with just a finite-dimensional subspace of a larger physical system.

Infinite-dimensional Hilbert spaces on the other hand are slightly more nuanced. A simple generalization to such dimensionality involves the space of infinite sequences of complex numbers :math:`\psi \equiv (\psi_i)_{i=1}^{\infty}` with converging norm, i.e.,

.. math:: \norm{\psi}_2 = \sqrt{\sum_{i=1}^{\infty} \abs{\psi_i}^2} < \infty.

If this holds, then :math:`\psi \in \ell^2` where :math:`\ell^2` is the space of *square-summable sequences*, which heuristically can be thought of as :math:`\SpaceHilbert = \ell^2 \cong \Complexes^\infty`. The associated inner product is then simply the generalization of :eq:`eq:inner_expansion`,

.. math:: \inner{\phi}{\psi} = \sum_{i=1}^{\infty} \conj{\phi_i}{} \psi_i,

which, as per the Cauchy-Schwarz inequality :eq:`eq:Cauchy-Schwarz`, converges provided the individual vector norms do. Importantly, the notion of completeness of :math:`\ell^2` with respect to its norm enables us to perform calculus in this space, including computing limits and derivatives of vectors :math:`\psi \in \ell^2`. Generalizations to other sequence spaces, e.g., :math:`\ell^p` with :math:`p \geq 1` and the associated norm

.. math:: \norm{\psi}_p = \left[\sum_{i=1}^{\infty} \abs{\psi_i}^p\right]^{\frac{1}{p}} < \infty.

are of course possible, but note that only in the case of :math:`p=2` is the sequence space a Hilbert space.

Dirac notation
--------------

Here we establish the notational convention that is used nearly universally in the formalism of quantum mechanics on Hilbert spaces. This standard system is known as *Dirac notation* or *bra-ket notation*. In this notation, a vector :math:`\psi \in \SpaceHilbert` is represented by :math:`\ket{\psi}` and is called a *ket*. Similarly, a covector in the dual space :math:`\phi \in \dual{\SpaceHilbert}{}` is denoted by :math:`\bra{\phi}` and called a *bra*. With these constructs, the value of the dual map :eq:`eq:dual_map` is given by

.. math:: \phi(\psi) \equiv \braket{\phi}{\psi} \equiv \inner{\phi}{\psi}.

This form is known as a *bra-ket*, and is simply a representation of the inner product in Dirac notation. Note that this implicitly uses the isomorphism :eq:`eq:Hilbert_isomorphism` provided by the inner product, meaning that we have the antilinear correspondence between bras and kets,

.. math:: \conj{\lambda}{}\bra{\psi} \longleftrightarrow \lambda\ket{\psi}.

Given an orthonormal basis :math:`\{\ket{\Basis_i}\}` of a discrete Hilbert space :math:`\SpaceHilbert`, we can expand in Dirac notation a general ket :math:`\ket{\psi} \in \SpaceHilbert` in terms of the basis as

.. math:: \ket{\psi} = \sum_{i} \psi_i \ket{\Basis_i}, \quad \psi_i = \braket{\Basis_i}{\psi}.

This notation is slightly cumbersome, and so it is conventional to simplify it by making the basis identification

.. math:: \ket{\Basis_i} \equiv \ket{i},

with which the above expansion appears as

.. math:: \ket{\psi} = \sum_{i} \braket{i}{\psi} \ket{i}.

The alternative notation for the basis :math:`\{\ket{i}\}` is known as the *standard basis* (in the nomenclature of mathematics) or the *computational basis* (in the nomenclature of quantum computing). It is always assumed to be orthonormal, and necessarily spans :math:`\SpaceHilbert`. As these objects (kets) reside in a :math:`\Dimension`-dimensional Hilbert space :math:`\SpaceHilbert \cong \Complexes^\Dimension`, they have corresponding representations in :math:`\Complexes^\Dimension` as column vectors, the standard choice being explicitly

.. math::
   :label: eq:basis_qudit
   
   \ket{0} = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix},
   \qquad \ket{1} = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix},
   \qquad \ldots
   \qquad \ket{\Dimension - 1} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}.

Here, the :math:`i`-th element (indexing from zero, as customary in computer science) of the :math:`i`-th vector contains a :math:`1`, while all of its other entries are :math:`0`. The corresponding covectors (bras) in the dual space :math:`\dual{\SpaceHilbert}{} \cong \Complexes^{*\Dimension}` have similar representations as row vectors,

.. math::
   \begin{aligned}
       \bra{0} &= \begin{bmatrix} 1 & 0 & \ldots & 0 \end{bmatrix}, \\
       \bra{1} &= \begin{bmatrix} 0 & 1 & \ldots & 0 \end{bmatrix}, \\
       &\;\;\vdots \\
       \bra{\Dimension - 1} &= \begin{bmatrix} 0 & 0 & \ldots & 1 \end{bmatrix}.
   \end{aligned}

In a finite-dimensional Hilbert space, any basis of linearly independent vectors has the same (finite) number of members, irrespective of their orthogonality.

Linear operators and operations
===============================

A *linear operator* :math:`\op{A}` on a Hilbert space :math:`\SpaceHilbert` is a map

.. math:: \op{A} : \Domain(\op{A}) \rightarrow \Range(\op{A})
   :label: eq:operator_linear_map

which preserves linear combinations of vectors :math:`\ket{\psi},\ket{\phi} \in \SpaceHilbert`, that is,

.. math:: \op{A}\bigl(\mu\ket{\psi} + \nu\ket{\phi}\bigr) = \mu\op{A}\ket{\psi} + \nu\op{A}\ket{\phi},
   :label: eq:operator_linear_preservation

for all :math:`\mu,\nu \in \Complexes`. Here, the space :math:`\Domain(\op{A}) \subseteq \SpaceHilbert` denotes the domain of :math:`\op{A}` while :math:`\Range(\op{A}) \subseteq \SpaceHilbert` denotes its range. For an infinite-dimensional :math:`\SpaceHilbert`, operators are often not defined on the whole space, and so :math:`\Domain(\op{A})` may be a proper subset of :math:`\SpaceHilbert`. For finite-dimensional Hilbert spaces on the other hand, linear operators may always be defined on the entire space such that :math:`\Domain(\op{A}) = \Range(\op{A}) = \SpaceHilbert`. The space of all linear operators on :math:`\SpaceHilbert` is denoted by :math:`\SpaceLinear(\SpaceHilbert)`. All the operators we will discuss are linear, and so we will henceforth omit the "linear" descriptor.

Bounded operators
-----------------

An operator :math:`\op{A}` is said to be *bounded* if :math:`\Domain(\op{A}) = \SpaceHilbert` and there exists some fixed :math:`M>0` such that for all :math:`\ket{\psi} \in \SpaceHilbert`,

.. math:: \bigl| \bigl| \op{A}\ket{\psi} \bigr| \bigr|_2 \leq M \bigl| \bigl| \ket{\psi} \bigr| \bigr|_2.

Otherwise, the operator is said to be *unbounded*. Bounded (linear) operators preserve the normalizability of vectors, that is, they map normalizable vectors to vectors that are likewise normalizable. This means that they necessarily act on the whole Hilbert space :math:`\SpaceHilbert`, and the space of such bounded operators is denoted :math:`\SpaceBounded(\SpaceHilbert)`.

Operator algebra
----------------

Given two such operators :math:`\op{A}` and :math:`\op{B}`, we can define their sum to be

.. math:: (\alpha\op{A} + \beta\op{B}) : \ket{\psi} \mapsto \alpha\op{A}\ket{\psi} + \beta\op{B}\ket{\psi}

for all :math:`\alpha, \beta \in \Complexes` and :math:`\ket{\psi} \in \SpaceHilbert`. We can also define their product to be the composition

.. math:: \op{A}\op{B} : \ket{\psi} \mapsto \op{A} \circ \op{B} \ket{\psi} = \op{A}(\op{B}\ket{\psi})

for all :math:`\ket{\psi} \in \SpaceHilbert`. It is easy to prove that both of these definitions provide forms that are linear in the original sense :eq:`eq:operator_linear_map`, and thus operators form an algebra.

In general, operators do not commute, e.g., :math:`\op{A}\op{B} \neq \op{B}\op{A}`, and so the associated algebra is non-Abelian, or non-commutative. The difference between these orderings is captured by the *commutator*,

.. math:: [\op{A},\op{B}] = \op{A}\op{B} - \op{B}\op{A},

which possesses the following properties:

.. math::

   \begin{aligned}
       \text{(i) } &\text{(antisymmetry):} &[\op{A},\op{B}] &= -[\op{B},\op{A}],\\
       \text{(ii) } &\text{(linearity):} &[\alpha_1\op{A}_1 + \alpha_2\op{A}_2,\op{B}] &= \alpha_1[\op{A}_1,\op{B}] + \alpha_2[\op{A}_2,\op{B}] \quad \forall \, \alpha_1,\alpha_2 \in \Complexes,\\
       \text{(iii) } &\text{(Leibniz identity):} &[\op{A},\op{B}\op{C}] & = [\op{A},\op{B}]\op{C} + \op{B}[\op{A},\op{C}],\\
       \text{(iv) } &\text{(Jacobi identity):} &\bigl[\op{A},[\op{B},\op{C}]\bigr] + \bigl[\op{B},[\op{C},\op{A}]\bigr] + \bigl[\op{C},[\op{A},\op{B}]\bigr] &=0.
   \end{aligned}

Outer product
-------------

In addition to the inner product, we may also use the Dirac notation to easily express the *outer product* of a vector :math:`\ket{\psi} \in \SpaceHilbert_1` and a covector :math:`\bra{\phi} \in \dual{\SpaceHilbert_2}{}`,

.. math::
   :label: eq:outer_product
   
   \begin{aligned}
       \ket{\psi}\bra{\phi} &\equiv \ket{\psi} \otimes \bra{\phi} \\
       &= \sum_{i,j} \braket{i}{\psi} \braket{\phi}{j} \, \ket{i}\bra{j} \\
       &= \sum_{i,j} \psi_i \conj{\phi_j}{} \ket{i}\bra{j}.
   \end{aligned}

Here, :math:`\phi \otimes \psi` denotes the tensor product between two vectors :math:`\phi` and :math:`\psi` (see :ref:`sec:composite`). The resulting form :math:`\ket{\psi}\bra{\phi} \in \SpaceHilbert` is a linear operator in its own right and exists in the space

.. math:: \SpaceHilbert = \SpaceHilbert_1 \otimes \dual{\SpaceHilbert_2}{},

which itself is a Hilbert space.

Eigenvectors and eigenvalues
----------------------------

A vector :math:`\ket{\psi} \in \SpaceHilbert` is said to be an *eigenvector* of an operator :math:`\op{A}` if

.. math:: \op{A}\ket{\psi} = a_\psi \ket{\psi}

where the number :math:`a_\psi \in \Complexes` is called the *eigenvalue*. Given this definition, we can single out two important operators:

-  The *identity* operator :math:`\Identity` is the (unique) operator that satisfies

   .. math:: \Identity\ket{\psi} = \ket{\psi}, \quad \forall \, \ket{\psi} \in \SpaceHilbert.

   Given any orthonormal basis :math:`\{\ket{i}\}`, we may write

   .. math:: \Identity = \sum_{i} \ket{i}\bra{i}.

-  The *zero* operator :math:`\op{0}` is the (unique) operator that satisfies

   .. math:: \op{0}\ket{\psi} = \vec{0}, \quad \forall \, \ket{\psi} \in \SpaceHilbert,

   where :math:`\vec{0}` is the zero vector (i.e., the additive identity).

An operator :math:`\op{A}` is called *invertible* if an operator :math:`\op{B}` exists such that

.. math:: \op{A}\op{B} = \op{B}\op{A} = \Identity.

If such a :math:`\op{B}` exists, then it is the (unique) inverse of :math:`\op{A}`, and we denote it by :math:`\op{B} = \op{A}^{-1}`. The *spectrum* of :math:`\op{A}` is the set of all complex numbers :math:`\lambda` for which the operator :math:`\op{A} - \lambda\Identity` fails to be invertible. In a finite-dimensional Hilbert space, the spectrum of :math:`\op{A}` is simply the set of eigenvalues of :math:`\op{A}`. The same is not true in general for infinite dimensions. The number of linearly independent eigenvectors possessing the same eigenvalue is called the *degeneracy* of that eigenvalue. Additionally, the *support* of an operator :math:`\op{A}` is the vector space spanned by the eigenvectors of :math:`\op{A}` with non-zero eigenvalues.

Transposition and conjugation
-----------------------------

Given a finite-dimensional Hilbert space :math:`\SpaceHilbert`, each operator :math:`\op{A} \in \SpaceLinear(\SpaceHilbert)` can be expanded in an orthonormal basis as

.. math:: \op{A} = \sum_{i,j} \ket{i}\bra{i}\op{A}\ket{j}\bra{j} = \sum_{i,j} A_{ij}\ket{i}\bra{j}

where

.. math:: A_{ij} \equiv \bra{i}\op{A}\ket{j}

are the elements of the corresponding matrix representation of the operator (in the given basis). Similarly, the product of two operators may be written as

.. math:: \op{A}\op{B} = \sum_{i,j,k} A_{ik}B_{kj}\ket{i}\bra{j}

where :math:`B_{kj} \equiv \bra{k}\op{B}\ket{j}`. These expressions make it easy to characterize the action of operations on such operators. Our primary interest lies in the *transpose* and the *conjugate transpose* (or *adjoint*), which are defined for any orthonormally expandable :math:`\op{A}` by

.. math::

   \begin{aligned}
       \text{transpose:}& \quad &\op{A}^\transpose &= \sum_{i,j} A_{ij}\ket{j}\bra{i}, \\
       \text{conjugate transpose:}& &\op{A}^\dagger &= \sum_{i,j} \conj{A_{ij}}{}\ket{j}\bra{i} = \conj{(\op{A}^\transpose)}{} = (\conj{\op{A}}{})^\transpose.
   \end{aligned}

From these, it is easy to deduce the following properties:

.. math::

   \begin{aligned}
       \text{(i):}& \quad &(\op{A}^\transpose)^\transpose &= \op{A} \qquad \qquad \quad &(\op{A}^\dagger)^\dagger &= \op{A},\\
       \text{(ii):}& &(\op{A}\op{B})^\transpose &= \op{B}^\transpose \op{A}^\transpose &(\op{A}\op{B})^\dagger &= \op{B}^\dagger \op{A}^\dagger,\\
       \text{(iii):}& &(\alpha \op{A})^\transpose &= \alpha \op{A}^\transpose &(\alpha \op{A})^\dagger &= \conj{\alpha}{} \op{A}^\dagger,\\
       \text{(iv):}& &(\op{A} + \op{B})^\transpose &= \op{A}^\transpose + \op{B}^\transpose &(\op{A} + \op{B})^\dagger &= \op{A}^\dagger + \op{B}^\dagger.
   \end{aligned}

Note also that the conjugate transpose of the eigenvalue equation :math:`\op{A}\ket{\psi} = a_\psi \ket{\psi}` is

.. math:: \bra{\psi}\op{A}^\dagger = \bra{\psi}\conj{a_\psi}{}

where :math:`\op{A}^\dagger` is taken to act to the left on the covector :math:`\bra{\psi}`.

Trace
-----

Another useful operation is the *trace*,

.. math:: \trace[{}\cdot{}] : \SpaceLinear(\SpaceHilbert) \rightarrow \Complexes,

defined on an operator :math:`\op{A} \in \SpaceLinear(\SpaceHilbert)` as

.. math:: \trace[\op{A}] \equiv \sum_{i} \bra{i}\op{A}\ket{i} = \sum_{i} A_{ii}

where :math:`\{\ket{i}\}` is any orthonormal basis. The trace has the following properties:

.. math::

   \begin{aligned}
       \text{(i):}& \quad &\trace[\op{A} + \op{B}] &= \trace[\op{A}] + \trace[\op{B}],\\
       \text{(ii):}& &\trace[\op{A}\op{B}] &= \trace[\op{B}\op{A}],\\
       \text{(iii):}& &\trace[\op{A}^\dagger] &= \conj{\trace[\op{A}]}{},\\
       \text{(iv):}& &\trace\bigl[\ket{\psi}\bra{\psi}\op{A}\bigr] &= \bra{\psi}\op{A}\ket{\psi}.
   \end{aligned}

In a matrix representation of linear operators, the trace is simply the sum of the elements on the main diagonal of an operator's corresponding matrix form.

Normal operators
----------------

An important class of operators are the *normal* operators, which are characterized by their commutation with their own conjugate transpose, i.e.,

.. math:: \op{N}^\dagger\op{N} = \op{N}\op{N}^\dagger.

The *spectral theorem* states that any normal operator :math:`\op{N}` admits a suitable *eigendecomposition*, that is, the eigenvectors :math:`\{\ket{v_i}\}` of :math:`\op{N}` form an orthonormal basis, and can be used in conjunction with the corresponding eigenvalues :math:`\{\lambda_i\}` to allow us to write

.. math:: \op{N} = \sum_{i} \lambda_i \ket{v_i}\bra{v_i}, \quad \lambda_i \in \Complexes.
   :label: eq:spectral_theorem

The converse holds true, such that any orthogonally diagonalizable operator is normal. A useful consequence of this theorem is that it is easy to compute the function of an operator,

.. math:: f(\op{N}) = \sum_{i} f(\lambda_i) \ket{v_i}\bra{v_i}.

Normal operators arise in many special forms, including:

-  *Hermitian* (or *self-adjoint*) operators :math:`\op{H}`, defined by

   .. math:: \op{H}^\dagger = \op{H}.

   If :math:`\op{H}` is Hermitian, then

   .. math:: \bra{\psi}\op{H}\ket{\psi} \in \Reals,\quad \forall \, \ket{\psi} \in \SpaceHilbert,

   that is, :math:`\op{H}` has only real eigenvalues.

-  *skew-Hermitian* operators :math:`\op{S}`, defined by

   .. math:: \op{S}^\dagger = -\op{S}.

-  *Unitary* operators :math:`\op{U}`, defined by

   .. math:: \op{U}^\dagger \op{U} = \op{U}\op{U}^\dagger = \Identity,

   or equivalently,

   .. math:: \op{U}^\dagger = \op{U}^{-1}.

   The characterizing nature of unitary operators is their preservation of the inner product, i.e.,

   .. math:: \bra{\phi}\op{U}^\dagger \op{U}\ket{\psi} = \braket{\phi}{\psi}, \quad \forall \,\ket{\psi},\ket{\phi} \in \SpaceHilbert,

   which motivates the given definition.

-  *Positive* operators :math:`\op{P}`, defined by

   .. math:: \bra{\psi}\op{P}\ket{\psi} \geq 0, \quad \forall \, \ket{\psi} \in \SpaceHilbert.

   Operators that fulfill this condition are said to be *positive-semidefinite*, and they may be constructed from any :math:`\op{A} \in \SpaceLinear(\SpaceHilbert)` as

   .. math:: \op{P} = \op{A}^\dagger \op{A},

   or using the spectral theorem,

   .. math:: \op{P} = \sum_{i} P_i \ket{v_i}\bra{v_i}

   given eigenvalues :math:`P_i \geq 0` and eigenvectors :math:`\{\ket{v_i}\}`. Note that :math:`\op{P}` is called *positive-definite* if

   .. math:: \bra{\psi}\op{P}\ket{\psi} > 0, \quad \forall \, \ket{\psi} \in \SpaceHilbert.

   In the special case where

   .. math:: \trace[\op{P}] = \sum_{i} P_i = 1,

   then :math:`\op{P}` is called a *density* operator.

-  *Projection* operators :math:`\op{\Pi}`, defined by

   .. math:: \op{\Pi}^2 = \op{\Pi} = \op{\Pi}^\dagger,

   which is to say that :math:`\op{\Pi}` is both idempotent and Hermitian.

-  *Involutory* operators :math:`\op{Q}`, defined by

   .. math:: \op{Q}^2 = \Identity.

   Involutory operators include those which are both Hermitian and unitary.

.. _`sec:composite`:

Composite systems
=================

Hilbert spaces are vector spaces over :math:`\Complexes`, so we can construct composite spaces and the corresponding tensor product in much the same way as we would for less equipped spaces. We will first discuss the *bipartite* case, which may be easily generalized to larger composite systems (termed *multipartite*). Let :math:`\SpaceHilbert_1` and :math:`\SpaceHilbert_2` be a pair of finite-dimensional Hilbert spaces, with bases :math:`\{\ket{\mu_m}\}_{m=1}^{M}` and :math:`\{\ket{\nu_n}\}_{n=1}^{N}`, respectively. The tensor product space :math:`\SpaceHilbert_1 \otimes \SpaceHilbert_2` is spanned by all pairs of elements :math:`\ket{\mu_m} \otimes \ket{\nu_n}` chosen from the two bases. Note in particular that :math:`\{\ket{\mu_m}\otimes\ket{\nu_n}\}_{m,n}` is an orthonormal basis of the composite space. Thus, if we have the linear combinations,

.. math::
   
   \begin{aligned}
       \ket{\psi} &= \sum_{m=1}^{M} \psi_m \ket{\mu_m},\\
       \ket{\phi} &= \sum_{n=1}^{N} \phi_m \ket{\nu_n},\\
   \end{aligned}


for any :math:`\ket{\psi} \in \SpaceHilbert_1` and :math:`\ket{\phi} \in \SpaceHilbert_2`, we can formally express their *tensor product* as

.. math::
   :label: eq:tensor_product

   \ket{\psi} \otimes \ket{\phi} = \sum_{m,n} \psi_m \phi_n \ket{\mu_m} \otimes \ket{\nu_n}.

This is often equivalently written as :math:`\ket{\psi} \ket{\phi}`, :math:`\ket{\psi, \phi}`, or even simply :math:`\ket{\psi \phi}`. It follows that

.. math:: \dim(\SpaceHilbert_1 \otimes \SpaceHilbert_2) = \dim(\SpaceHilbert_1) \times \dim(\SpaceHilbert_2),

and for any elements :math:`\ket{\psi},\ket{\phi} \in \SpaceHilbert_1` and :math:`\ket{\psi^{\prime}},\ket{\phi^{\prime}} \in \SpaceHilbert_2` we have the rules:

.. math::

   \begin{aligned}
       \text{(i) } &\text{(linearity in }\SpaceHilbert_1\text{):} & \bigl(\ket{\psi} + \ket{\phi}\bigr) \otimes \ket{\psi^{\prime}} &= \ket{\psi} \otimes \ket{\psi^{\prime}} + \ket{\phi} \otimes \ket{\psi^{\prime}},\\
       \text{(ii) } &\text{(linearity in }\SpaceHilbert_2\text{):} &\ket{\psi} \otimes \bigl(\ket{\psi^{\prime}} + \ket{\phi^{\prime}}\bigr) &= \ket{\psi} \otimes \ket{\psi^{\prime}} + \ket{\psi} \otimes \ket{\phi^{\prime}},\\
       \text{(iii) } &\text{(scalar multiplication):} &\lambda\bigl(\ket{\psi} \otimes \ket{\psi^{\prime}}\bigr) &= \bigl(\lambda\ket{\psi}\bigr) \otimes \ket{\psi^{\prime}} = \ket{\psi} \otimes \bigl(\lambda\ket{\psi^{\prime}}\bigr).
   \end{aligned}

Thus, the composite space :math:`\SpaceHilbert_1 \otimes \SpaceHilbert_2` is a vector space over :math:`\Complexes`, and becomes a Hilbert space when we endow it with an inner product. This is accomplished in the obvious way, where if :math:`\ket{\Psi},\ket{\Phi} \in \SpaceHilbert_1 \otimes \SpaceHilbert_2` are two composite forms defined in general as

.. math::

   \begin{aligned}
       \ket{\Psi} &= \sum_{m,n} \Psi_{m,n} \ket{\mu_m} \otimes \ket{\nu_n},\\
       \ket{\Phi} &= \sum_{m,n} \Phi_{m,n} \ket{\mu_m} \otimes \ket{\nu_n},
   \end{aligned}

then their inner product is

.. math::

   \begin{aligned}
       \braket{\Psi}{\Phi} &= \sum_{i,j,k,l} \conj{\Phi_{ij}}{} \Psi_{kl} \bigl(\bra{\mu_i} \otimes \bra{\nu_j}\bigr)\bigl(\ket{\mu_k} \otimes \ket{\nu_l}\bigr) \\
       &= \sum_{i,j,k,l} \conj{\Phi_{ij}}{} \Psi_{kl} {\braket{\mu_i}{\mu_k}}_1 {\braket{\nu_j}{\nu_l}}_2 \\
       &= \sum_{i,j} \conj{\Phi_{ij}}{} \Psi_{ij}
   \end{aligned}

by the orthonormality of the bases. Here, :math:`{\braket{{}\cdot{}}{{}\cdot{}}}_1` and :math:`{\braket{{}\cdot{}}{{}\cdot{}}}_2` denote the inner products on :math:`\SpaceHilbert_1` and :math:`\SpaceHilbert_2`, respectively. In the special case where the composite vectors are simple tensor products, e.g.,

.. math::

   \begin{aligned}
       \ket{\Psi} &= \ket{\psi} \otimes \ket{\psi^{\prime}},\\
       \ket{\Phi} &= \ket{\phi} \otimes \ket{\phi^{\prime}},
   \end{aligned}

then their inner product becomes

.. math:: \braket{\Phi}{\Psi} = \bigl(\bra{\phi} \otimes \bra{\phi^{\prime}}\bigr)\bigl(\ket{\psi} \otimes \ket{\psi^{\prime}}\bigr) = {\braket{\phi}{\psi}}_1 {\braket{\phi^{\prime}}{\psi^{\prime}}}_2.

Systems which are to be understood as not being constructable from tensor products of Hilbert spaces (subsystems) are said to be *non-composite* and are often termed *unipartite*.

As far as linear operators on composite Hilbert spaces are concerned, if :math:`\op{A} \in \SpaceLinear(\SpaceHilbert_A)` and :math:`\op{B} \in \SpaceLinear(\SpaceHilbert_B)` are two operators, then their tensor product

.. math:: \op{A} \otimes \op{B} \in \SpaceLinear(\SpaceHilbert_A) \otimes \SpaceLinear(\SpaceHilbert_B) = \SpaceLinear(\SpaceHilbert_A \otimes \SpaceHilbert_B)

is defined by the action on the product state :math:`\ket{\psi} \otimes \ket{\phi} \in \SpaceHilbert_A \otimes \SpaceHilbert_B` as

.. math:: (\op{A} \otimes \op{B})\bigl(\ket{\psi} \otimes \ket{\phi}\bigr) = \op{A}\ket{\psi} \otimes \op{B}\ket{\phi}.

This has the following properties:

.. math::

   \begin{aligned}
       \text{(i):}& \quad &(\op{A}_1 + \op{A}_2)\otimes\op{B} &= \op{A}_1\otimes\op{B} + \op{A}_2\otimes\op{B},\\
       \text{(ii):}& &\op{A}\otimes(\op{B}_1 + \op{B}_2) &= \op{A}\otimes\op{B}_1 + \op{A}\otimes\op{B}_2,\\
       \text{(iii):}& &(\op{A}\otimes\op{B})^\dagger &= \op{A}^\dagger\otimes\op{B}^\dagger,\\
       \text{(iv):}& &\trace[\op{A}\otimes\op{B}] &= \trace[\op{A}]\trace[\op{B}],\\
       \text{(v):}& &(\lambda\op{A})\otimes\op{B} &= \op{A}\otimes(\lambda\op{B}).
   \end{aligned}

In general, an operator :math:`\op{Q} \in \SpaceLinear(\SpaceHilbert_A \otimes \SpaceHilbert_B)` may be expanded as

.. math:: \op{Q} = \sum_{i,j,k,l} Q_{ik}^{jl} \ket{i}\bra{j} \otimes \ket{k}\bra{l},

where :math:`\{\ket{i}\},\{\ket{k}\}` are orthonormal bases in :math:`\SpaceHilbert_A` and :math:`\{\ket{j}\},\{\ket{l}\}` are orthonormal bases in :math:`\SpaceHilbert_B`. The partial transposes of such an operator over each space :math:`\SpaceHilbert_A` and :math:`\SpaceHilbert_B` are defined respectively as

.. math::

   \begin{aligned}
       \op{Q}^{\transpose_A} &= \sum_{i,j,k,l} Q_{ik}^{jl} \bigl(\ket{i}\bra{j}\bigr)^\transpose \otimes \ket{k}\bra{l} = \sum_{i,j,k,l} Q_{ik}^{jl} \ket{j}\bra{i} \otimes \ket{k}\bra{l}, \\
       \op{Q}^{\transpose_B} &= \sum_{i,j,k,l} Q_{ik}^{jl} \ket{i}\bra{j} \otimes \bigl(\ket{k}\bra{l}\bigr)^\transpose = \sum_{i,j,k,l} Q_{ik}^{jl} \ket{i}\bra{j} \otimes \ket{l}\bra{k},
   \end{aligned}

Similarly, the partial traces over :math:`\SpaceHilbert_A` and :math:`\SpaceHilbert_B` are definable as

.. math::

   \begin{aligned}
       \trace_{A}[\op{Q}] &= \sum_{m} \bigl(\bra{m} \otimes \Identity\bigr)\op{Q}\bigl(\ket{m} \otimes \Identity\bigr) = \sum_{m,k,l} Q_{mk}^{ml} \ket{k}\bra{l}, \\
       \trace_{B}[\op{Q}] &= \sum_{n} \bigl(\Identity \otimes \bra{n}\bigr)\op{Q}\bigl(\Identity \otimes \ket{n}\bigr) = \sum_{n,i,j} Q_{in}^{jn} \ket{i}\bra{j},
   \end{aligned}

where :math:`\{\ket{m}\}` and :math:`\{\ket{n}\}` are orthonormal bases of :math:`\SpaceHilbert_A` and :math:`\SpaceHilbert_B`, respectively.

Schmidt decomposition
---------------------

A useful theorem for expressing composite vectors is the *Schmidt decomposition*: given a bipartite vector :math:`\ket{\psi} \in \SpaceHilbert_A \otimes \SpaceHilbert_B`, there exists sets of orthonormal states :math:`\{\ket{k_A}\}` and :math:`\{\ket{k_B}\}` for systems :math:`A` and :math:`B`, respectively, such that

.. math:: \ket{\psi} = \sum_k \lambda_k \ket{k_A} \otimes \ket{k_B}.
   :label: eq:schmidt_decomposition

Here, :math:`\lambda_k` are non-negative real numbers, known as *Schmidt coefficients* that satisfy

.. math:: \sum_k \lambda_k^2 = \braket{\psi}{\psi}.

The number of (non-zero) Schmidt coefficients is called the *Schmidt number* of the vector :math:`\ket{\psi}`, and the bases :math:`\{\ket{k_A}\}` and :math:`\{\ket{k_B}\}` are called the *Schmidt bases*.

The Schmidt decomposition :eq:`eq:schmidt_decomposition` is simply a way of expressing a vector in the tensor product of two inner product spaces (such as Hilbert spaces), and our ability to do so is a very powerful result. For example, given a normalized bipartite vector :math:`\ket{\psi}` with decomposition :eq:`eq:schmidt_decomposition`, the reduced operators for each system can be calculated to be

.. math::

   \begin{aligned}
       \StateDensity^A &\equiv \trace_B\bigl[\ket{\psi}\bra{\psi}\bigr] = \sum_k \lambda_k^2 \ket{k_A}\bra{k_A}, \\
       \StateDensity^B &\equiv \trace_A\bigl[\ket{\psi}\bra{\psi}\bigr] = \sum_k \lambda_k^2 \ket{k_B}\bra{k_B}.
   \end{aligned}

The fact that the eigenvalues of both of these operators are identical (simply equal to :math:`\lambda_k^2`) is a significant result. This is because many of the important properties of operators are completely determined by their eigenvalues. Consequently, such properties of the reduced operators of a vector on a composite system will automatically be the same, regardless of the structure of the composite vector.

Multiple systems of arbitrary dimension
---------------------------------------

We now turn our attention to :math:`\Dimension`-dimensional Hilbert spaces, which we denote as :math:`\SpaceHilbert_\Dimension`. On such spaces, there always exists a vector basis :math:`\{\ket{\Basis_i}\}_{i=1}^{\Dimension }` with which any :math:`\ket{\psi} \in \SpaceHilbert_\Dimension` can be expressed as

.. math::

   \ket{\psi} = \sum_{i=1}^{\Dimension} \psi_i \ket{\Basis_i}.

If we instead have :math:`\Number` such systems :math:`\{\ket{\psi_n}\}_{n=1}^{\Number}`, each residing in the same Hilbert space :math:`\ket{\psi_n} \in \SpaceHilbert_{\Dimension}`, then their composition is

.. math::
   :label: eq:composition_state

   \begin{aligned}
       \ket{\psi_1} \otimes \ket{\psi_2} \otimes \ldots \otimes \ket{\psi_\Number} &\equiv \bigotimes_{n=1}^{\Number} \ket{\psi_n} \\
       &= \bigotimes_{n=1}^{\Number} \sum_{i=1}^{\Dimension} \psi_{i_n} \ket{\Basis_{i_n}} \\
       &= \sum_{\{i_n\}_{n=1}^{\Number} = 1}^{\Dimension} \psi_{i_1} \psi_{i_2} \ldots \psi_{i_\Number} \ket{\Basis_{i_1}} \otimes \ket{\Basis_{i_2}} \otimes \ldots \otimes \ket{\Basis_{i_\Number}} \\
       &= \sum_{i=1}^{\Dimension} \left( \prod_{n=1}^{\Number} \psi_{i_n} \right) \bigotimes_{n=1}^{\Number} \ket{\Basis_{i_n}} \\
       &= \sum_{i=1}^{\Dimension} \psi_{i_1, i_2, \ldots, i_\Number} \ket{\Basis_{i_1, i_2, \ldots, i_\Number}} \\
   \end{aligned}

where :math:`\psi_{i_n}` is the :math:`i_n`-th component of the :math:`n`-th state (with basis :math:`\{\ket{\Basis_{i_n}}\}_{i_n = 1}^{\Dimension} \equiv \{\ket{\Basis_i}\}_{i = 1}^{\Dimension}` for all :math:`n`), i.e.,

.. math::

   \ket{\psi_n} = \sum_{i_n = 1}^{\Dimension} \psi_{i_n} \ket{\Basis_{i_n}},

the amalgamated components are

.. math::

   \psi_{i_1, i_2, \ldots, i_\Number} \equiv \prod_{n=1}^{\Number} \psi_{i_n} = \psi_{i_1} \psi_{i_2} \ldots \psi_{i_\Number},

and we introduced the composite vector

.. math::

   \ket{\Basis_{\{i_n\}}} \equiv \ket{\Basis_{i_1, i_2, \ldots, i_\Number}} \equiv \bigotimes_{n=1}^{\Number} \ket{\Basis_{i_n}}.

Since :math:`\{\ket{\Basis_{i_n}}\}_{i_n = 1}^{\Dimension}` is a basis for the Hilbert space :math:`\SpaceHilbert_{\Dimension}`, then accordingly the set of states

.. math::

   \begin{aligned}
      \Bigl\{\ket{\Basis_{\{i_n\}}} : 1 \leq i_n \leq \Dimension, \, 1 \leq n \leq \Number \Bigr\} &\equiv \left\{\bigotimes_{n=1}^{\Number} \ket{\Basis_{i_n}}\right\}_{\{i_n\}_{n=1}^{\Number} = 1}^{\Dimension} \\
      &= \bigl\{\ket{\Basis_{i_1}} \otimes \ket{\Basis_{i_2}} \otimes \ldots \otimes \ket{\Basis_{i_\Number}}\bigr\}_{\{i_n\}_{n=1}^{\Number} = 1}^{\Dimension},
   \end{aligned}

makes a basis for the composite space

.. math::

   \SpaceHilbert_{\Dimension}^{\otimes \Number} \equiv \bigotimes_{i=1}^{\Number} \SpaceHilbert_{\Dimension} \equiv \underbrace{\SpaceHilbert_{\Dimension} \otimes \SpaceHilbert_{\Dimension} \otimes \ldots \otimes \SpaceHilbert_{\Dimension}}_{\Number \text{ times}}.

As this is :math:`\Number` compositions of :math:`\Dimension`-dimensional systems, there are a total of :math:`\Dimension^\Number` basis states :math:`\ket{\Basis_{\{i_n\}}}` which span :math:`\SpaceHilbert_{\Dimension}^{\otimes \Number}`. This :math:`\Dimension^\Number`-dimensional composite space may therefore be written as :math:`\SpaceHilbert_{\Dimension^\Number}`, and we have the isomorphism

.. math:: \SpaceHilbert_{\Dimension^\Number} \cong \SpaceHilbert_{\Dimension}^{\otimes \Number}.

In other words, a :math:`\Dimension^\Number`-dimensional Hilbert space :math:`\SpaceHilbert_{\Dimension^\Number}` is decomposable into exactly :math:`\Number` tensor products :math:`\SpaceHilbert_{\Dimension}^{\otimes \Number}` of a :math:`\Dimension`-dimensional Hilbert space :math:`\SpaceHilbert_\Dimension`. Importantly, this means any linear operator :math:`\op{A} \in \SpaceHilbert_{\Dimension^\Number}` may be embedded in :math:`\SpaceHilbert_{\Dimension}^{\otimes N}` via a decomposition into tensor products of generalized Gell-Mann matrices (with the identity :math:`\GellMannGeneralized_{0} \equiv \Identity_{\Dimension}`) (see :ref:`sec:qudits`),

.. math::
   :label: eq:operator_decomposition

   \op{A} = \frac{1}{\Dimension^\Number}\sum_{\{i_n\}_{n=1}^{\Number} = 0}^{\Dimension^2 - 1} A_{i_1, i_2, \ldots, i_\Number} \GellMannGeneralized_{i_1} \otimes \GellMannGeneralized_{i_2} \otimes \ldots \otimes \GellMannGeneralized_{i_\Number}

where the coefficients

.. math:: A_{i_1, i_2, \ldots, i_\Number} = \trace\bigl[(\GellMannGeneralized_{i_1} \otimes \GellMannGeneralized_{i_2} \otimes \ldots \otimes \GellMannGeneralized_{i_\Number})\op{A}\bigr]

collectively characterize :math:`\op{A}` under this decomposition. For example, a bipartite operator on :math:`\Dimension`-dimensional subsystems can be written as

.. math::

   \op{A} = \frac{1}{\Dimension^2}\sum_{i_1,i_2=0}^{\Dimension^2 - 1} A_{i_1,i_2} \GellMannGeneralized_{i_1} \otimes \GellMannGeneralized_{i_2}

with :math:`A_{i_1, i_2} = \trace\bigl[(\GellMannGeneralized_{i_1} \otimes \GellMannGeneralized_{i_2})\op{A}\bigr]`. Alternatively, in the case of binary (:math:`\Dimension = 2`) systems (see :ref:`sec:qubits`), this decomposition :eq:`eq:operator_decomposition` is accomplished using the Pauli matrices :eq:`eq:Pauli` (with the identity :math:`\Pauli_{0} \equiv \Identity_{2}`),

.. math::

   \op{A} = \frac{1}{2^\Number}\sum_{\{i_n\}_{n=1}^{\Number} = 0}^{3} A_{i_1, i_2, \ldots, i_\Number} \Pauli_{i_1} \otimes \Pauli_{i_2} \otimes \ldots \otimes \Pauli_{i_\Number}

where

.. math:: A_{i_1, i_2, \ldots, i_\Number} = \trace\bigl[(\Pauli_{i_1} \otimes \Pauli_{i_2} \otimes \ldots \otimes \Pauli_{i_\Number})\op{A}\bigr].

Superoperators
==============

A *superoperator* is a linear map :math:`\MapGeneral` on the space of (linear) operators :math:`\SpaceLinear(\SpaceHilbert)`,

.. math:: \MapGeneral[{}\cdot{}] : \SpaceLinear(\SpaceHilbert) \rightarrow \SpaceLinear(\SpaceHilbert),

which preserves linear combinations of operators, that is,

.. math:: \MapGeneral[\mu\op{A} + \nu\op{B}] = \mu\MapGeneral[\op{A}] + \nu\MapGeneral[\op{B}]

for all :math:`\op{A},\op{B} \in \SpaceLinear(\SpaceHilbert)` and :math:`\mu,\nu \in \Complexes`. Any such superoperator may satisfy any number of additional properties:

.. math::

   \begin{aligned}
       \text{(i) } &\text{(positivity):} &\MapGeneral[\op{P}] & \ \text{is positive if} \ \op{P} \ \text{is positive}, \\
       \text{(ii) } &\text{(complete positivity):} &\MapGeneral[\op{P}] \otimes \Identity & \ \text{is positive if} \ \op{P} \otimes \Identity \ \text{is positive}, \\
       \text{(iii) } &\text{(Hermiticity preservation):} &\MapGeneral[\op{H}]^\dagger&= \MapGeneral[\op{H}] \ \text{if} \ \op{H}^\dagger = \op{H}, \\
       \text{(iv) } &\text{(trace preservation):} &\trace\bigl[\MapGeneral[\op{A}]\bigr] &= \trace[\op{A}] \quad \forall \, \op{A} \in \SpaceLinear(\SpaceHilbert).
   \end{aligned}

Concavity and convexity
=======================

A Hilbert space :math:`\SpaceHilbert` is said to be *convex* if for any finite collection of its elements :math:`\{\op{A}_i\}`, the linear combination satisfies

.. math:: \sum_{i} p_i \op{A}_i \in \SpaceHilbert

for any probability distribution :math:`\SetProbability = \{p_i\}`. If this does not hold, then :math:`\SpaceHilbert` is said to be *concave*. An element :math:`\op{A}_i \in \SpaceHilbert` in a convex space is called *extreme* if it cannot be represented as a non-trivial combination of other elements (that is, it can only be expressed with a single non-zero :math:`p_i`).

A (real) map

.. math:: f({}\cdot{}) : \SpaceHilbert \rightarrow \Reals

is said to be convex if

.. math:: f\biggl(\sum_{i} p_i \op{A}_i\biggr) \leq \sum_{i} p_i f(\op{A}_i)

and concave if

.. math:: f\biggl(\sum_{i} p_i \op{A}_i\biggr) > \sum_{i} p_i f(\op{A}_i).

.. Matrix spaces
.. =============

.. - space of (complex) matrices represented by M(N,C).

.. - norm replaced by trace.

.. - inner product is replace by trace of product.

.. - Hilbert-Schmidt operators.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames
