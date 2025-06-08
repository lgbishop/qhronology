.. include:: /styles.rst

.. _`sec:alternatives`:

Alternative formulations of quantum time travel
===============================================

It is evident from the discussion in :ref:`sec:comparison` that both D-CTCs and P-CTCs possess a myriad of undesirable traits. It is also clear that there is more than one way to extend ordinary quantum theory to include self-consistent antichronological time travel. Thus, one can hope that a quantum prescription of time travel which is an improvement over D-CTCs and P-CTCs may be able to be formulated. At the very least, constructing an alternative theory that is void of at least some of the problems discussed in prior sections should not be an impossible task. With this in mind, it is useful to specify a few of the desired characteristics (based on those in :cite:p:`allen_treating_2014`) of such a theory:

#. *Compatibility with standard quantum theory*: The prescription should reproduce ordinary quantum mechanics both along the CTC itself and in regions outside any chronology-violating sets. Compatibility with all experimental evidence of standard quantum mechanics is also desired. This means that the theory should follow all established features of quantum mechanics, such as obeyance of the no-cloning theorem.

#. *Existence and uniqueness of solutions*: The prescription should provide exactly one solution (CR state) for each combination of possible interaction and CV state (if applicable). If multiple such solutions exist, then the probabilities for each should be specified. In other words, the theory should not possess any uniqueness ambiguities like that of D-CTCs.

#. *Absence of pathological traits*: The prescription should be consistent with other generally accepted physical theories such as special relativity (at least in a local, approximate sense) and its associated causal structure. In particular, the theory should not permit *antichronological action*. This is, in essence, the concept where the very *existence* of a time machine in the future, no matter how distant, jeopardizes the agency of an observer in the past and present. For P-CTCs, this arises as restrictions on a system's state in the past as a function of the future, and constitutes a profoundly interesting (and undesirable) issue for the prescription.

There are of course other traits which may be considered, one such being prejudice in requiring either or both of the CR and CV states to be pure. This characteristic however is often left to the opinions of the physicist, given that there is no objective, *a priori* reasoning as to prefer pure states over mixed states as fundamental objects in any given theory of quantum time travel.

The search for alternatives to D-CTCs and P-CTCs that possess fewer pathological problems is a central theme of research into quantum time travel. Here, we briefly discuss several of the more prominent models (excluding some lesser-developed theories :cite:p:`pegg_quantum_2005, greenberger_quantum_2005`), some of which represent significant departures from the standard method of incorporating the principle of self-consistency into ordinary quantum mechanics.

.. _`sec:WD-CTCs`:

Weighted D-CTCs (WD-CTCs)
-------------------------

Perhaps the simplest "improved" prescription is that of *weighted D-CTCs* :cite:p:`allen_treating_2014`, which merely represents an extension of the ordinary D-CTCs model. The premise is simple: associate to each valid D-CTC fixed-point density operator :math:`\StateCV_\alpha` a weight :math:`w_\alpha \geq 0`, using which the unique, "correct" D-CTC CV state is then given by the integral over the space of all D-CTC fixed points, that is,

.. math:: \StateCV = \frac{\int \diff{\alpha} \, w_\alpha \StateCV_\alpha}{\int \diff{\alpha} \, w_\alpha}.
   :label: eq:WD-CTCs_CV

The generic meaning of integrating over the state space is to sum over all possibilities (see :ref:`sec:integrals` for a mathematical definition). The weighted mixture :eq:`eq:WD-CTCs_CV` therefore represents the combination of all elements in the (convex) subset of valid D-CTC CV states. Accordingly, the uniqueness ambiguity in the ordinary D-CTC prescription is resolved for any given set of weights.

The corresponding weighted D-CTC CR output is therefore given by the usual D-CTC CR map, that is,

.. math::
   :label: eq:WD-CTCs_CR

   \begin{aligned}
       \MapWDCTCsCR_{\Unitary}[\StateCR,\StateCV] &\equiv \trace_\CV\bigl[\Unitary(\StateCR \otimes \StateCV)\Unitary^\dagger\bigr] \\
       &= \frac{\int \diff{\alpha} \, w_\alpha \trace_\CV\bigl[\Unitary(\StateCR \otimes \StateCV_\alpha)\Unitary^\dagger\bigr]}{\int \diff{\alpha} \, w_\alpha}.
   \end{aligned}

The parametrization of the constituent states by :math:`\alpha` evidently describes a whole class of models based on both how the corresponding weights :math:`w_\alpha` are distributed, and the specific form of the integration measure one chooses to employ. For example, perhaps the simplest model is one in which all weights are equal, i.e., :math:`w_\alpha = 1`. This corresponds to a *uniform* weighted D-CTC theory that is manifestly unique, which immediately is an improvement over standard D-CTCs. More sophisticated models may opt to appoint the weights to represent certain transition probabilities of the CV state through the time-machine region---see :cite:p:`allen_treating_2014` for more discussion.

.. _`sec:T-CTCs`:

Transition probabilities (T-CTCs)
---------------------------------

The idea of quantum transition probabilities can be incorporated into P-CTCs, and the resultant *transition probabilities* prescription (T-CTCs) :cite:p:`allen_treating_2014` of quantum time travel shares many features of P-CTCs, while also gaining a few improvements in regards to the pathological problems possessed by the latter. Where a P-CTC preselects and postselects against a maximally entangled state, a T-CTC alternatively uses just a pure state :math:`\ket{\StateVector} \in \SpacePure(\SpaceHilbert_\CV)` in the CV system. This system is prejudicially assumed to be pure, as a postulate of the theory is that the primitive states of quantum mechanics are similarly pure. Thus, given the CR input :math:`\ket{\StatePure} \in \SpacePure(\SpaceHilbert_\CR)`, the evolution of the bipartite input is

.. math:: \ket{\StatePure}\bra{\StatePure} \otimes \ket{\StateVector}\bra{\StateVector} \rightarrow \Unitary \bigl(\ket{\StatePure}\bra{\StatePure} \otimes \ket{\StateVector}\bra{\StateVector}\bigr) \Unitary^\dagger

where :math:`\Unitary` describes the (unitary) interaction between the CR and CV modes. Self-consistency of the time-travelling CV state is achieved by postselection on the CV subsystem against the same input state. Doing so yields

.. math:: \bigl(\Identity \otimes \bra{\StateVector}\bigr) \Unitary \bigl(\ket{\StatePure}\bra{\StatePure} \otimes \ket{\StateVector}\bra{\StateVector}\bigr) \Unitary^\dagger \bigl(\Identity \otimes \ket{\StateVector}\bigr) = \Unitary_\StateVector \ket{\StatePure}\bra{\StatePure} \Unitary_\StateVector^\dagger

where

.. math:: \Unitary_\StateVector \equiv \bigl(\Identity \otimes \bra{\StateVector}\bigr) \Unitary \bigl(\Identity \otimes \ket{\StateVector}\bigr)

is an operator which acts on :math:`\SpaceHilbert_\CR` and is not unitary in general. The CR output state :math:`\MapTCTCsCR_{\Unitary}[\StatePure]` is then obtained when one integrates over all such CV states and subsequently renormalizes, i.e.,

.. math::
   :label: eq:T-CTCs_CR_integral

   \begin{aligned}
       \MapTCTCsCR_{\Unitary}[\StatePure] &= \frac{1}{\Normalization} \int_{\SpacePure(\SpaceHilbert_\CV)} \diff[\StateVector] \, \Unitary_\StateVector \ket{\StatePure}\bra{\StatePure} \Unitary_\StateVector^\dagger, \\
       \Normalization &\equiv \int_{\SpacePure(\SpaceHilbert_\CV)} \diff[\StateVector] \bra{\StatePure} \Unitary_\StateVector \Unitary_\StateVector^\dagger \ket{\StatePure}.
   \end{aligned}

Although the expression :eq:`eq:T-CTCs_CR_integral` is concise, it is difficult to ascertain the behaviour of the CR output state given the integral form. However, following the original work in :cite:p:`allen_treating_2014`, the form of :eq:`eq:T-CTCs_CR_integral` may be simplified and written in terms of only states and operators. Given an orthonormal basis :math:`\{\ket{\mu}\}_{\mu=0}^{\Dimension - 1}` for :math:`\SpaceHilbert_\CV`, we first expand the unitary interaction :math:`\Unitary` in the form

.. math:: \Unitary = \sum_{\alpha,\beta=0}^{\Dimension - 1} \OperatorPartial_{\alpha\beta} \otimes \ket{\alpha}\bra{\beta}

where :math:`\OperatorPartial_{\alpha\beta}` are operators on :math:`\SpaceHilbert_\CR`. Using this and the integrals

.. math:: \Integral_{\alpha\beta,\gamma\delta} \equiv \int_{\SpacePure(\SpaceHilbert_\CV)} \diff[\StateVector] \, \braket{\StateVector}{\alpha}  \braket{\beta}{\StateVector}  \braket{\StateVector}{\delta}  \braket{\gamma}{\StateVector} 
   :label: eq:T-CTCs_integrals

we may express :eq:`eq:T-CTCs_CR_integral` as

.. math:: \MapTCTCsCR_{\Unitary}[\StatePure] = \frac{1}{\Normalization} \sum_{\alpha,\beta,\gamma,\delta = 0}^{\Dimension - 1} \Integral_{\alpha\beta,\gamma\delta} \OperatorPartial_{\alpha\beta}\ket{\StatePure}\bra{\StatePure} \OperatorPartial_{\gamma\delta}^\dagger. 
   :label: eq:T-CTCs_CR_expansion

In the integral :eq:`eq:T-CTCs_integrals`, we expand both the state :math:`\ket{\StateVector}` and measure :math:`\diff[\StateVector]` using the Hurwitz parametrization [:eq:`eq:Hurwitz_state` and :eq:`eq:Hurwitz_measure`, respectively]. For each :math:`\ket{\mu}`, the :math:`\diff\varphi_\mu` component of the corresponding measure factors out, and so any integrand whose :math:`\varphi_\mu`-dependence is only an integer power of :math:`\e^{\eye \varphi_\mu}` necessarily integrates to zero due to the identity

.. math:: \int_{\varphi = 0}^{2\pi} \diff\varphi \, \e^{\eye (m - n) \varphi} = 2\pi\delta_{mn}, \quad m \neq n, \quad m,n\in\Integers.

This means that any integral :eq:`eq:T-CTCs_integrals` vanishes unless it is of the form,

.. math:: \Integral_{\alpha\alpha,\beta\beta} = \Integral_{\alpha\beta,\alpha\beta} = \int_{\SpacePure(\SpaceHilbert_\CV)} \diff[\StateVector] \, \abs{\braket{\alpha}{\StateVector}}^2  \abs{\braket{\beta}{\StateVector}}^2,
   :label: eq:T-CTCs_integrals_special

and so the only surviving terms in the expression :eq:`eq:T-CTCs_CR_expansion` are

.. math:: \MapTCTCsCR_{\Unitary}[\StatePure] = \frac{1}{\Normalization} \Biggl(\sum_{\substack{\alpha,\beta = 0 \\ \alpha \neq \beta}}^{\Dimension - 1} \Integral_{\alpha\beta,\alpha\beta} \OperatorPartial_{\alpha\beta} \ket{\StatePure}\bra{\StatePure} \OperatorPartial_{\alpha\beta}^\dagger + \sum_{\substack{\alpha,\beta = 0 \\ \alpha \neq \beta}}^{\Dimension - 1} \Integral_{\alpha\alpha,\beta\beta} \OperatorPartial_{\alpha\alpha}\ket{\StatePure}\bra{\StatePure} \OperatorPartial_{\beta\beta}^\dagger + \sum_{\alpha = 0}^{\Dimension - 1} \Integral_{\alpha\alpha,\alpha\alpha} \OperatorPartial_{\alpha\alpha}\ket{\StatePure}\bra{\StatePure} \OperatorPartial_{\alpha\alpha}^\dagger\Biggr). 
   :label: eq:T-CTCs_CR_expansion_contributions

The usefulness of having a parametrization for which the integration measure is invariant under unitary transformations now comes to the fore: one may rotate the state :math:`\ket{\StateVector}` in the integrals :eq:`eq:T-CTCs_integrals_special` so that only the :math:`\ket{\Dimension - 1}` and :math:`\ket{\Dimension - 2}` components contribute. Therefore, under the Hurwitz parametrization, we find for :math:`\alpha \neq \beta`,

.. math::

   \begin{aligned}
       \Integral_{\alpha\beta,\alpha\beta} = \Integral_{\alpha\alpha,\beta\beta} &= \int_{\SpacePure(\SpaceHilbert_\CV)} \diff[\StateVector] \, \abs{\braket{\Dimension - 1}{\StateVector}}^2 \, \abs{\braket{\Dimension - 2}{\StateVector}}^2 \\
       &= (2\pi)^{\Dimension - 1} \prod_{\gamma = 1}^{\Dimension - 3} \int_{\vartheta_\gamma \in [0, \tfrac{\pi}{2}]} \diff\vartheta_\gamma \, \cos(\vartheta_\gamma) \, \sin^{2\gamma - 1}(\vartheta_\gamma)\\
       &\quad \times \int_{\vartheta_{\Dimension - 2} \in [0,2\pi]} \diff\vartheta_{\Dimension - 2} \, \cos^3(\vartheta_{\Dimension - 2}) \sin^{2\Dimension - 5}(\vartheta_{\Dimension - 2}) \\
       &\quad \times \int_{\vartheta_{\Dimension - 1} \in [0,2\pi]} \diff\vartheta_{\Dimension - 1} \, \cos^3(\vartheta_{\Dimension - 1}) \sin^{2\Dimension - 1}(\vartheta_{\Dimension - 1}),
   \end{aligned}

while for :math:`\alpha = \beta`,

.. math::

   \begin{aligned}
       \Integral_{\alpha\alpha,\alpha\alpha} &= \int_{\SpacePure(\SpaceHilbert_\CV)} \diff[\StateVector] \, \abs{\braket{\Dimension - 1}{\StateVector}}^4 \\
       &= (2\pi)^{\Dimension - 1} \prod_{\gamma = 1}^{\Dimension - 3} \int_{\vartheta_\gamma \in [0, \tfrac{\pi}{2}]} \diff\vartheta_\gamma \, \cos(\vartheta_\gamma) \, \sin^{2\gamma - 1}(\vartheta_\gamma)\\
       &\quad \times \int_{\vartheta_{\Dimension - 2} \in [0,2\pi]} \diff\vartheta_{\Dimension - 2} \, \cos(\vartheta_{\Dimension - 2}) \sin^{2\Dimension - 5}(\vartheta_{\Dimension - 2}) \\
       &\quad \times \int_{\vartheta_{\Dimension - 1} \in [0,2\pi]} \diff\vartheta_{\Dimension - 1} \, \cos^5(\vartheta_{\Dimension - 1}) \sin^{2\Dimension - 3}(\vartheta_{\Dimension - 1}).
   \end{aligned}

Evaluation (numerical or otherwise) of the integrals in these forms reveals that

.. math:: \frac{\Integral_{\alpha\alpha,\alpha\alpha}}{\Integral_{\alpha\beta,\alpha\beta}} = \frac{\Integral_{\alpha\alpha,\alpha\alpha}}{\Integral_{\alpha\alpha,\beta\beta}} = 2, \quad \alpha \neq \beta,

which allows us to combine the distinct sums in :eq:`eq:T-CTCs_CR_expansion_contributions` and bring out a common multiplicative pre-factor (which we subsequently neglect due to the foresight of having to renormalize), yielding

.. math:: \MapTCTCsCR_{\Unitary}[\StateVector] \propto \sum_{\alpha,\beta = 0}^{\Dimension - 1} \left(\OperatorPartial_{\alpha\beta}\ket{\StatePure}\bra{\StatePure} \OperatorPartial_{\alpha\beta}^\dagger + \OperatorPartial_{\alpha\alpha}\ket{\StatePure}\bra{\StatePure} \OperatorPartial_{\beta\beta}^\dagger\right).

Finally, with the identities

.. math::

   \begin{aligned}
       \sum_{\alpha = 0}^{\Dimension - 1} \OperatorPartial_{\alpha\alpha} &= \trace_\CV[\Unitary], \\
       \sum_{\alpha,\beta = 0}^{\Dimension - 1} \OperatorPartial_{\alpha\beta} \ket{\StatePure}\bra{\StatePure} \OperatorPartial_{\alpha\beta}^\dagger &= \trace_\CV\bigl[\Unitary(\ket{\StatePure}\bra{\StatePure} \otimes \Identity)\Unitary^\dagger\bigr],
   \end{aligned}

we arrive at the result

.. math::
   :label: eq:T-CTCs

   \begin{aligned}
       \MapTCTCsCR_{\Unitary}[\StatePure] &= \frac{1}{\Normalization^{\prime}} \Bigl( \trace_\CV[\Unitary] \ket{\StatePure}\bra{\StatePure} \trace_\CV[\Unitary^\dagger] + \Dimension \, \trace_\CV\bigl[ \Unitary\bigl(\ket{\StatePure}\bra{\StatePure} \otimes \tfrac{1}{\Dimension}\Identity\bigr) \Unitary^\dagger\bigr] \Bigr), \\
       \Normalization^{\prime} &\equiv \trace\Bigl\{ \trace_\CV[\Unitary] \ket{\StatePure}\bra{\StatePure} \trace_\CV[\Unitary^\dagger] \Bigr\} + \Dimension.
   \end{aligned}

In general, the methodology of the T-CTC prescription may equally be applied to mixed CR input states, giving

.. math::
   :label: eq:T-CTCs_mixed

   \begin{aligned}
       \MapTCTCsCR_{\Unitary}[\StateCR] &= \frac{1}{\Normalization^{\prime}} \Bigl( \trace_\CV[\Unitary] \StateCR \, \trace_\CV[\Unitary^\dagger] + \Dimension \, \trace_\CV\bigl[ \Unitary\bigl(\StateCR \otimes \tfrac{1}{\Dimension}\Identity\bigr) \Unitary^\dagger\bigr] \Bigr), \\
       \Normalization^{\prime} &\equiv \trace\Bigl\{ \trace_\CV[\Unitary] \StateCR \, \trace_\CV[\Unitary^\dagger] \Bigr\} + \Dimension.
   \end{aligned}

In this form, it is immediately clear that the T-CTC equation of motion is a weighted mixture of the P-CTC equation of motion :eq:`eq:P-CTCs_CR` with an ordinary quantum channel, giving the impression that a T-CTC can be thought of as a noisy P-CTC. Therefore, T-CTCs, like P-CTCs, does not suffer from uniqueness ambiguities, while having the benefit of being consistent for any given :math:`\Unitary` and :math:`\StateCR`. This is because the condition

.. math:: \trace\bigl[\trace_\CV[\Unitary] \StateCR \, \trace_\CV[\Unitary^\dagger]\bigr] = 0,

while rendering P-CTCs inconsistent, poses no problems for T-CTCs. The prescription thus provides unique solutions to all paradoxes with the added advantage of not requiring either an adjunct condition or the introduction of noise in order to do so.

CTC as a ring resonator
-----------------------

In optics, a *ring resonator* involves a scattering process wherein a portion of the output is supplied back into the input. Czachor :cite:p:`czachor_time_2019` posits that the same formal structure is encountered in any looped quantum evolution, including time travel to the past (in the neighbourhood of a CTC). Given that the quantum theory of ring resonators is both well-developed and agrees closely with experiment, then it is therefore natural to treat the CTC as a ring resonator, and this provides an alternative prescription with which self-consistent solutions to quantum time travel problems can be formulated.

Czachor's scheme :cite:p:`czachor_time_2019` is in essence a topological one, and is thus independent of any spacetime geometry. As a theory of quantum time travel, it provides logically consistent solutions to any given time-travel paradox, with such solutions notably being inequivalent to those given by D-CTCs and P-CTCs. Indeed, while D-CTCs is characterized by an interaction between a time traveller and a copy of themselves on a singly looped CTC (meaning that at any given global time there can physically exist at most two time travellers), the ring resonator paradigm describes the time traveller as a single object that is in a state of superposition of being inside and outside the loop. Mathematically, the solutions in essence describe the ordinary quantum optical reflection of an input state off of the time machine. This is to say that the interaction with the CTC is in fact merely a self-interference effect, which is an inherently linear phenomenon. The result is a robust, linear, fully self-consistent prescription of quantum time travel that is free from many of the issues which plague D-CTCs and P-CTCs, including violation of the no-cloning theorem. It remains to be studied however whether this model possesses any advantages in the context of quantum information processing.

Indefinite causal structure and the process matrix formalism
------------------------------------------------------------

Under a complete theory of quantum gravity, it is expected that spacetime loses its classical properties :cite:p:`gibbs_small_1996,piazza_glimmers_2010`. One of the possible consequences of this is the emergence of indefinite causal structures :cite:p:`hardy_probability_2005,hardy_towards_2007,zych_bells_2019`, where the causal order of events is no longer definite and instead is in a quantum (probabilistic) superposition of all possible orderings. However, perhaps the foremost problem that arises when one abandons classical causality is the appearance of logical inconsistencies, themselves stemming from seemingly paradoxical physical scenarios. The usual procedure to eliminate these and restore self-consistency is to extend ordinary quantum mechanics (like in P-CTCs or D-CTCs), as discussed in the preceding sections.

A radically different approach involves the *process matrix formalism*. This theory provides an abstract framework for quantum mechanics on indefinite causal structures, and includes the study of which types of global processes are compatible with the assumption that the standard laws of physics are valid in a local sense :cite:p:`oreshkov_quantum_2012,araujo_witnessing_2015,feix_quantum_2015,oreshkov_causal_2016,branciard_simplest_2015,giacomini_indefinite_2016,baumann_appearance_2016,costa_quantum_2016,abbott_multipartite_2016,araujo_purification_2017,perinotti_causal_2017,abbott_genuinely_2017,shrapnel_updating_2018,jia_quantum_2018,bavaresco_semi-device-independent_2019,jia_causal_2019`. In other words, this formalism posits that all operations which are possible in ordinary spacetime are still allowed in local regions of any spacetime, regardless of the nature of the underlying causality. It is useful as a tool to study correlations between parties where the causal order among them is not specified *a priori*. Instead, the assumption that the probabilities of measurement outcomes are well-defined replaces the (often implicit) assumption of a definite causal order. This provides a powerful methodology---one that is in fact more general than (ordinary) quantum theory---as certain correlations that cannot be explained with a predefined causal order of the parties may arise. Interestingly, when applied to classical physics, the process matrix formalism has shown that there exist classical processes which are incompatible with any notion of causal order between events :cite:p:`baumeler_maximal_2014,baumeler_device-independent_2016,baumeler_space_2016`.

In :cite:p:`baumeler_reversible_2019`, Baumeler et al. propose a classical, deterministic version of the formalism as a possible model for CTCs. They consider the most general deterministic dynamics connecting classical degrees of freedom defined on a set of bounded spacetime regions, under the requirement that such dynamics are compatible with *arbitrary* operations performed in the local regions. Baumeler et al. show that this can be realized entirely through reversible interactions, and furthermore that consistency with local operations is compatible with non-trivial time travel. In particular, they found a simple characterization for all processes involving up to three regions. In other words, it is guaranteed that at least three parties are free to perform arbitrary local operations while interacting in such a way that all are both in the future and in the past of each other.

Tobar and Costa :cite:p:`tobar_reversible_2020` extend the characterization of deterministic processes to an arbitrary number of regions. Central to their results is the conclusion that CTCs are compatible not only with both determinism and a notion of freedom of choice regarding local operations, but also with a wide variety of dynamical processes and scenarios. This means that the way in which CTCs allow multiple observers in distinct regions to communicate with each other is not overly restricted by conflicts between locality, logical consistency, and freedom of choice. Given that this conclusion was reached using an abstract framework that is independent of both particular dynamics and geometry, then this hints at a deep, robust compatibility between time travel and the laws of physics, which is contrary to the previously discussed information-theoretic models of quantum time travel.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames