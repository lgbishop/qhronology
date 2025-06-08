.. include:: /styles.rst

.. _`sec:CTCs`:

Closed timelike curves and time machines
========================================

Closed timelike curves (CTCs) form an interesting class of objects within the general theory of relativity as they present the possibility for an observer to travel back in time. Formally, a CTC is an entirely geometric entity, being simply a curve (a path in spacetime) that is both closed and everywhere (either future- or past-directed) timelike. As such, in a universe with CTCs, any physical system may be able to interact with its past self, and so the potential existence of CTCs within our own universe naturally evokes scientific investigation into time travel. The foremost focus of such research is on questions regarding the non-trivial causal structure of CTC spacetimes and the consistency of the standard laws of physics.

In some locally unobjectionable exact solutions to the Einstein field equations, CTCs naturally occur :cite:p:`lanczos_uber_1924,lewis_special_1932,van_stockum_gravitational_1938,papapetrou_static_1945,godel_example_1949,taub_empty_1951,newman_emptyspace_1963,kerr_gravitational_1963,levy_rotating_1964,papapetrou_champs_1966,tipler_rotating_1974,soares_inhomogeneous_1980,gott_closed_1991,bonnor_exact_2002,bonnor_double-kerr_2004,ori_class_2005,bonnor_exact_2005,ori_formation_2007,sarma_pure_2013,tippett_traversable_2017,fermi_time_2018,ralph_spinning_2020`. However, many such spacetimes are often considered to be globally unphysical (like the classic swirling dust solutions of van Stockum :cite:p:`van_stockum_gravitational_1938` and Gödel :cite:p:`godel_example_1949`), and so the presence of interior CTCs is usually considered to be an artefact of the theory. Despite this, it is believed that CTCs may be constructed (at least theoretically) through the use of a traversable *wormhole* :cite:p:`ellis_ether_1973,hawking_wormholes_1988,morris_wormholes_1988-1,morris_wormholes_1988,visser_traversable_1989-1,visser_traversable_1989,coule_wormholes_1990,visser_van_1994,visser_lorentzian_1995,visser_traversable_1997,carlini_euclidean_1997,hochberg_geometric_1997,barcelo_traversable_1999,barcelo_scalar_2000,barcelo_brane_2000,dadhich_r0_2002,visser_traversable_2003,kar_quantifying_2004,ralph_relativistic_2012,garcia_generic_2012,butcher_traversable_2015,bronnikov_scalar_2018,simpson_vaidya_2019,canate_ellis_2019,lobo_dynamic_2020,berry_thin-shell_2020`. It is important to stress however that the physicality of such models is often called into question in the literature. This is due mainly to the fact that these solutions to the Einstein field equations often appear to necessitate the existence of matter possessing a negative energy density, and as such they do not always correspond to stable spacetimes. Note therefore that other solutions (such as the Kerr metric :cite:p:`kerr_gravitational_1963`), being free of the requirement of negative energy density, may enable the manifestation of CTCs in a much less contentious manner.

.. _`sec:wormholes`:

Wormhole-based time machines
----------------------------

In popular culture, wormholes (either artificially constructed or naturally occurring) commonly provide a means of interstellar (or even intergalactic) transportation. They accomplish this by allowing spaceships to quickly traverse their short, tubiform interiors and emerge at distant locations far sooner than any alternative non-wormhole routes would allow. Alternatively, if two separate moments in time were to be linked by wormhole instead of two separate locations, one would possess a *time machine* :cite:p:`morris_wormholes_1988,novikov_analysis_1989,thorne_laws_1991,lossev_jinn_1992,ralph_relativistic_2012`, i.e., a mechanism which can produce CTCs. Thus, wormholes are theoretically able to facilitate both long-distance space travel and time travel. It is this basis on which many of the studies involving wormhole-based time machines is established.

In essence, a wormhole is an exotic, theoretical object that connects two distant regions in space. The simplest version of a topological wormhole :cite:p:`friedman_cauchy_1990,friedman_cauchy_1991,friedman_existence_1997,friedman_cauchy_2004` can be constructed by "cutting out" two spatially separated balls (denoted by :math:`\Mouth^\pm`, representing the two ends of the wormhole) in flat three-dimensional space and subsequently "gluing" (connecting) the surfaces (denoted by :math:`\partial\Mouth^\pm`) of these holes together. The resulting *mouths* (entrances) into the wormhole are thus *identified*, which is to say that entering into one results in simultaneous emergence from the other. See :numref:`fig:diagram_wormhole_mouths` for a visual depiction of such geometry. Note that the resulting spacetime is topologically and geometrically non-trivial since the space is not simply connected and the identified surfaces are not flat.

.. only:: html

   .. figure:: /figures/output/diagram_wormhole_mouths-dark.png
      :scale: 36 %
      :alt: A diagram of the surfaces of a simple topological wormholes.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/diagram_wormhole_mouths-light.png
      :scale: 36 %
      :alt: A diagram of the surfaces of a simple topological wormholes.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/diagram_wormhole_mouths-light.png
   :name: fig:diagram_wormhole_mouths
   :scale: 36 %
   :alt: A diagram of the surfaces of a simple topological wormholes.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   The surfaces of a simple topological wormhole.

To turn a wormhole into a time machine (thereby manifesting CTCs), a time "delay" has to be induced between the mouths. This can be accomplished in a few different ways, resulting in either of two distinct classes of time machine. The first class consists of those of which the time machine is *eternal* (meaning that CTCs are ever-present), and is accomplished simply by imposing a identification time difference (denoted :math:`\TimeDelta`) between the two mouths (so that the coordinate time :math:`\Time` on the "future" mouth :math:`\MouthFuture` corresponds to the time :math:`(\Time - \TimeDelta)` on the "past" mouth :math:`\MouthPast`). The second class consists of those created (theoretically) in a more physically realistic manner, such as moving one mouth (the future mouth) either into a strong gravitational field or accelerating it to relativistic speeds (and decelerating it back) :cite:p:`friedman_cauchy_1990`. For both classes of wormhole-based time machines, when the temporal difference between the mouths reaches a greater magnitude than their spatial separation, the mouths become causally connected, that is, CTCs manifest.

.. _`sec:paradoxes`:

Time-travel paradoxes
=====================

The emergence of inconsistencies due to retro-causal action in the evolution of a time-travelling physical system is an issue which is captured by the infamous *grandfather paradox* (detailed in :cite:p:`visser_lorentzian_1995`). This problem, which is perhaps the foremost example of a time-travel paradox, takes on many forms, all of which share the common characteristic of antichronological causation. The archetype of the paradox often features an observer who travels to the past and, through their actions (usually by interfering with the relationship between their young grandparents), prevents their own birth. Consequently, the observer is unable to travel back in time to preclude their existence, thus the paradox is evident.

.. _`sec:self-consistency`:

The principle of self-consistency
---------------------------------

Time-travel paradoxes and the concept of retro-causality lie at the foundation of the issues with CTCs. In particular, the inconsistencies associated with paradoxical causal sequences have led to uncertainty regarding the pathology of CTCs and hence their research suitability. However, there is a distinct lack of evidence suggesting that the inconsistencies of CTC paradoxes are entirely inescapable. One may simply regard these problems as ill-posed, given that the initial conditions (e.g., the observer's very existence and intent to intervene) are influenced by the future occurrences (e.g., observer stopping their grandparents from meeting). To resolve this problem, we could suppose that there exists some fundamental characteristic of reality which forbids any future event from paradoxically altering the past.

In particular, we could conjecture the existence of an innate law by which the universe operates, called the *principle of self-consistency* :cite:p:`friedman_cauchy_1990`, which prohibits paradoxical causal sequences from transpiring. Under this condition, a globally consistent solution of the local physical laws must exist. This means that, while a system is allowed to propagate into its own past, it must do so in a way that is consistent with its own original history. Any interaction that occurs must be compatible with the past, and causal sequences containing events solely of this nature are characterized as being self-consistent.

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames