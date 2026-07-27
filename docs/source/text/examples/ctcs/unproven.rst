.. _`eg:unproven`:

Unproven-theorem paradox
========================

Description
-----------

The *unproven-theorem paradox* :cite:p:`deutsch_quantum_1991, lloyd_closed_2011, allen_treating_2014` (depicted in :numref:`fig:circuit_ctc_unproven`) is, as we shall see, not as straightforward as other temporal paradoxes. Here, the CR system is comprised of two subsystems: the first (upper) is the *mathematician*, and the second (lower) is the *book*.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_unproven-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the unproven-theorem paradox under the D-CTCs prescription.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_unproven-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the unproven-theorem paradox under the D-CTCs prescription.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_unproven-light.png
   :name: fig:circuit_ctc_unproven
   :scale: 34 %
   :alt: A quantum circuit diagram of the unproven-theorem paradox under the D-CTCs prescription.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum model of the unproven-theorem paradox under the D-CTCs prescription.

.. raw:: latex

   \vspace*{-\baselineskip}

Described by the unitary

.. math:: \Unitary = \Swap^{\indices{1,2}} \cdot \Control^{\indices{0}} \NOT^{\indices{1}} \cdot \Control^{\indices{2}} \NOT^{\indices{0}},
   :label: eq:unproven_unitary

the unproven-theorem paradox encapsulates the scenario in which the proof of a theorem that a mathematician reads in the past is the very same proof which they write down in the future book (with the book having travelled back in time). We therefore denote the absence and presence of the proof in each subsystem intuitively by :math:`\ket{0}` and :math:`\ket{1}`, respectively. Under this interpretation, when the mathematician and/or the book are in the state :math:`\ket{1}`, they possess a "correct" proof, while being in the state :math:`\ket{0}` means that they do not. (Alternatively, one can think of these qubit levels as denoting different answers to some problem the mathematician is working on. They can then encode their proof of some theorem into an :math:`\Number`-bit binary string by using :math:`\Number` copies of the circuit :cite:p:`allen_treating_2014`.) Thus, we will use the CR input state

.. math:: \StateCR = \ket{0}\bra{0}\otimes\ket{0}\bra{0},
   :label: eq:unproven_input

which describes both the book and mathematician as not initially possessing the proof.

Solutions
---------

D-CTCs
^^^^^^

To find the D-CTC solutions, we first compute the standard evolution through the circuit with the CR input state :eq:`eq:unproven_input`,

.. math::

   \begin{aligned}
       \MapGeneral_{\Unitary} [\StateCR \otimes \StateCV] &= \Unitary \bigl(\ket{0}\bra{0}\otimes\ket{0}\bra{0} \otimes \StateCV\bigr) \Unitary^\dagger \\
       &= \Swap^{\indices{1,2}} \cdot \Control^{\indices{0}} \NOT^{\indices{1}} \cdot \Control^{\indices{2}} \NOT^{\indices{0}} \bigl(\ket{0}\bra{0}\otimes\ket{0}\bra{0} \otimes \StateCV\bigr) \Control^{\indices{2}} \NOT^{\dagger \indices{0}} \cdot \Control^{\indices{0}} \NOT^{\dagger \indices{1}} \cdot \Swap^{\dagger \indices{1,2}} \\
       &= \Swap^{\indices{1,2}} \cdot \Control^{\indices{0}} \NOT^{\indices{1}} \bigl(\ket{0}\bra{0}\otimes\ket{0}\bra{0} \otimes \ket{0}\bra{0}\StateCV\ket{0}\bra{0} \\
       & \qquad\qquad\qquad\;\; + \ket{0}\bra{1}\otimes\ket{0}\bra{0} \otimes \ket{0}\bra{0}\StateCV\ket{1}\bra{1} \\
       & \qquad\qquad\qquad\;\; + \ket{1}\bra{0}\otimes\ket{0}\bra{0} \otimes \ket{1}\bra{1}\StateCV\ket{0}\bra{0} \\
       & \qquad\qquad\qquad\;\; + \ket{1}\bra{1}\otimes\ket{0}\bra{0} \otimes \ket{1}\bra{1}\StateCV\ket{1}\bra{1}\bigr) \Control^0 \NOT^{\dagger 1} \cdot \Swap^{\dagger 1,2} \\
       &= \Swap^{\indices{1,2}} \bigl(\ket{0}\bra{0}\otimes\ket{0}\bra{0} \otimes \ket{0}\bra{0}\StateCV\ket{0}\bra{0} \\
       & \qquad\quad\;\; + \ket{0}\bra{1}\otimes\ket{0}\bra{1} \otimes \ket{0}\bra{0}\StateCV\ket{1}\bra{1} \\
       & \qquad\quad\;\; + \ket{1}\bra{0}\otimes\ket{1}\bra{0} \otimes \ket{1}\bra{1}\StateCV\ket{0}\bra{0} \\
       & \qquad\quad\;\; + \ket{1}\bra{1}\otimes\ket{1}\bra{1} \otimes \ket{1}\bra{1}\StateCV\ket{1}\bra{1}\bigr) \Swap^{\dagger \indices{1,2}} \\
       &= \ket{0}\bra{0} \otimes \ket{0}\bra{0}\StateCV\ket{0}\bra{0} \otimes \ket{0}\bra{0} \\
       & \quad\; + \ket{0}\bra{1} \otimes \ket{0}\bra{0}\StateCV\ket{1}\bra{1} \otimes \ket{0}\bra{1} \\
       & \quad\; + \ket{1}\bra{0} \otimes \ket{1}\bra{1}\StateCV\ket{0}\bra{0} \otimes \ket{1}\bra{0} \\
       & \quad\; + \ket{1}\bra{1} \otimes \ket{1}\bra{1}\StateCV\ket{1}\bra{1} \otimes \ket{1}\bra{1}.
   \end{aligned}

Subsequently tracing out the CR system (subsystems :math:`0` and :math:`1`) yields the CV map,

.. math::

   \begin{aligned}
       \MapDCTCsCV_{\Unitary} [\StateCR,\StateCV] &= \trace_{0, 1} \bigl[\Unitary \bigl(\ket{0}\bra{0} \otimes \ket{0}\bra{0} \otimes \StateCV\bigr) \Unitary^\dagger\bigr] \\
       &= \bra{0}\StateCV\ket{0} \cdot \ket{0}\bra{0} + \bra{1}\StateCV\ket{1} \cdot \ket{1}\bra{1},
   \end{aligned}

while tracing out the CV system (subsystem :math:`2`) gives the CR map,

.. math::

   \begin{aligned}
       \MapDCTCsCR_{\Unitary} [\StateCR,\StateCV] &= \trace_{2} \bigl[\Unitary \bigl(\ket{0}\bra{0} \otimes \ket{0}\bra{0} \otimes \StateCV\bigr) \Unitary^\dagger\bigr] \\
       &= \bra{0}\StateCV\ket{0} \cdot \ket{0}\bra{0} \otimes \ket{0}\bra{0} + \bra{1}\StateCV\ket{1} \cdot \ket{1}\bra{1} \otimes \ket{1}\bra{1}.
   \end{aligned}

According to D-CTCs, solutions to the CV map are given as fixed points, which we can calculate as any density matrix :math:`\StateCV` that satisfies

.. math:: \StateCV = \bra{0}\StateCV\ket{0} \cdot \ket{0}\bra{0} + \bra{1}\StateCV\ket{1} \cdot \ket{1}\bra{1}.

Comparing the terms (entries) of the density matrix then gives the simultaneous equations

.. math::

   \begin{aligned}
       \bra{0}\StateCV\ket{0} &= \bra{0}\StateCV\ket{0}, \\
       \bra{1}\StateCV\ket{0} &= 0, \\
       \bra{0}\StateCV\ket{1} &= 0, \\
       \bra{1}\StateCV\ket{1} &= \bra{1}\StateCV\ket{1}.
   \end{aligned}

These equations, along with the trace condition

.. math:: \trace[\StateCV] = \bra{0}\StateCV\ket{0} + \bra{1}\StateCV\ket{1} = 1,

(which describes the expectation that any given CV state is normalized), are solved when

.. math:: \bra{1}\StateCV\ket{1} = 1 - \bra{0}\StateCV\ket{0},

with all other terms equal to zero. This expresses a continuum of solutions that can be expressed in a parametrized form, with one such way being the natural choice

.. math::

   \begin{aligned}
       \bra{0}\StateCV\ket{0} &= \ParameterFree, \\
       \bra{1}\StateCV\ket{1} &= 1 - \ParameterFree.
   \end{aligned}

Here, we introduced the free parameter :math:`0 \leq \ParameterFree \leq 1`, which encapsulates the notion of (infinite) multiplicity in the solutions to the D-CTC CV map. With this parametrization, the corresponding CV state can be written as

.. math:: \StateCV_{\MapDCTCsCR} = \ParameterFree\ket{0}\bra{0} + (1 - \ParameterFree)\ket{1}\bra{1}.
   :label: eq:unproven_D-CTCs_CR

For the CR solution, we simply use the calculated CV state in our computation of the CR map, and accordingly find

.. math:: \StateCR_{\MapDCTCsCR} = \ParameterFree\ket{0}\bra{0}\otimes\ket{0}\bra{0} + (1 - \ParameterFree)\ket{1}\bra{1}\otimes\ket{1}\bra{1}.
   :label: eq:unproven_D-CTCs_CV

P-CTCs
^^^^^^

To compute the P-CTC CR solution, we first calculate the P-CTC operator,

.. math::
   :label: eq:unproven_P-CTCs_operator

   \begin{aligned}
       \OperatorPCTC &\equiv \trace_\CV[\Unitary] \\
       &= \trace_2\bigl[\Swap^{\indices{1,2}} \cdot \Control^{\indices{0}} \NOT^{\indices{1}} \cdot \Control^{\indices{2}} \NOT^{\indices{0}}\bigr] \\
       &= \trace_2\bigl[\Swap^{\indices{1,2}} \cdot \bigl(\ket{0}\bra{0} \otimes \Identity \otimes \Identity + \ket{1}\bra{1} \otimes \Pauli_x \otimes \Identity\bigr) \cdot \bigl(\Identity \otimes \Identity \otimes \ket{0}\bra{0} + \Pauli_x \otimes \Identity \otimes \ket{1}\bra{1}\bigr)\bigr] \\
       &= \trace_2\bigl[\Swap^{\indices{1,2}} \cdot \bigl(\ket{0}\bra{0} \otimes \Identity \otimes \ket{0}\bra{0} \\
       &\qquad\qquad\quad\;\;\; + \ket{1}\bra{1} \otimes \Pauli_x \otimes \ket{0}\bra{0} \\
       &\qquad\qquad\quad\;\;\; + \ket{0}\bra{1} \otimes \Identity \otimes \ket{1}\bra{1} \\
       &\qquad\qquad\quad\;\;\; + \ket{1}\bra{0} \otimes \Pauli_x \otimes \ket{1}\bra{1}\bigr)\bigr] \\
       &= \trace_2\bigl[\Swap^{\indices{1,2}} \cdot \bigl(\ket{0}\bra{0} \otimes \ket{0}\bra{0} \otimes \ket{0}\bra{0} \\
       &\qquad\qquad\quad\;\;\; + \ket{0}\bra{0} \otimes \ket{1}\bra{1} \otimes \ket{0}\bra{0} \\
       &\qquad\qquad\quad\;\;\; + \ket{1}\bra{1} \otimes \ket{0}\bra{1} \otimes \ket{0}\bra{0} \\
       &\qquad\qquad\quad\;\;\; + \ket{1}\bra{1} \otimes \ket{1}\bra{0} \otimes \ket{0}\bra{0} \\
       &\qquad\qquad\quad\;\;\; + \ket{0}\bra{1} \otimes \ket{0}\bra{0} \otimes \ket{1}\bra{1} \\
       &\qquad\qquad\quad\;\;\; + \ket{0}\bra{1} \otimes \ket{1}\bra{1} \otimes \ket{1}\bra{1} \\
       &\qquad\qquad\quad\;\;\; + \ket{1}\bra{0} \otimes \ket{0}\bra{1} \otimes \ket{1}\bra{1} \\
       &\qquad\qquad\quad\;\;\; + \ket{1}\bra{0} \otimes \ket{1}\bra{0} \otimes \ket{1}\bra{1}\bigr)\bigr] \\
       &= \trace_2\bigl[\ket{0}\bra{0} \otimes \ket{0}\bra{0} \otimes \ket{0}\bra{0} \\
       &\qquad\quad + \ket{0}\bra{0} \otimes \ket{0}\bra{1} \otimes \ket{1}\bra{0} \\
       &\qquad\quad + \ket{1}\bra{1} \otimes \ket{0}\bra{1} \otimes \ket{0}\bra{0} \\
       &\qquad\quad + \ket{1}\bra{1} \otimes \ket{0}\bra{0} \otimes \ket{1}\bra{0} \\
       &\qquad\quad + \ket{0}\bra{1} \otimes \ket{1}\bra{0} \otimes \ket{0}\bra{1} \\
       &\qquad\quad + \ket{0}\bra{1} \otimes \ket{1}\bra{1} \otimes \ket{1}\bra{1} \\
       &\qquad\quad + \ket{1}\bra{0} \otimes \ket{1}\bra{1} \otimes \ket{0}\bra{1} \\
       &\qquad\quad + \ket{1}\bra{0} \otimes \ket{1}\bra{0} \otimes \ket{1}\bra{1}\bigr] \\
       &= \ket{0}\bra{0} \otimes \ket{0}\bra{0} + \ket{1}\bra{1} \otimes \ket{0}\bra{1} + \ket{0}\bra{1} \otimes \ket{1}\bra{1} + \ket{1}\bra{0} \otimes \ket{1}\bra{0} \\
       &= \sqrt{2}\bigl(\bigl|\Phi^+\bigr\rangle\bra{0,0} + \bigl|\Psi^+\bigr\rangle\bra{1,1}\bigr).
   \end{aligned}

With this, we can easily determine the P-CTC CR state (corresponding to the input state :eq:`eq:unproven_input`) via its definition :eq:`eq:P-CTCs_CR`,

.. math::
   :label: eq:unproven_P-CTCs_CR

   \begin{aligned}
       \StateCR_\MapPCTCsCR &= \MapPCTCsCR_{\Unitary} [\StateCR ] \\
       &= \frac{\OperatorPCTC \ket{0}\bra{0} \otimes \ket{0}\bra{0} \OperatorPCTC^\dagger}{\trace\bigr[\OperatorPCTC \ket{0}\bra{0} \otimes \ket{0}\bra{0} \OperatorPCTC^\dagger\bigr]} \\
       &= \bigl|\Phi^+\bigr\rangle\bigl\langle\Phi^+\bigr|.
   \end{aligned}

Lastly, using the expression :eq:`eq:P-CTCs_CV`, we can compute the P-CTC CV state (via weak-measurement quantum state tomography) to be

.. math::
   :label: eq:unproven_P-CTCs_CV

   \begin{aligned}
       \StateCV_\MapPCTCsCR &= \frac{1}{2}\Identity \\
       &= \frac{1}{2}\bigl(\ket{0}\bra{0} + \ket{1}\bra{1}\bigr).
   \end{aligned}

Observe that the D-CTC resolution :eq:`eq:unproven_D-CTCs_CR` turns out not to be unique (with free parameter :math:`\ParameterFree`), while the P-CTC CR state :eq:`eq:unproven_P-CTCs_CR` is. The interpretation of these solutions is that, according the P-CTCs, the mathematician and the book will be in a superposition of both possessing the proof and neither possessing it, while according to D-CTCs, the two parties will be in a parametrized mixture of such possibilities. Additionally, it is easy to see that the P-CTC CV state is the maximally entropic form of its D-CTC counterpart, which means that the ECP end-state evolution (the "correct" D-CTC fixed point which resolves the uniqueness ambiguity) in this case :eq:`eq:unproven_D-CTCs_CV` coincidentally is exactly the P-CTC CV solution :eq:`eq:unproven_P-CTCs_CV`.

Implementation
--------------

.. raw:: latex

   \begin{codetitled}{Unproven-theorem paradox}{}

.. literalinclude:: /text/examples/ctcs/unproven.py
   :name: code:unproven
   :language: python

.. raw:: latex

   \end{codetitled}

Output
------

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> unproven.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.12cm 0 -0.15cm]{text_examples_ctcs_unproven.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_unproven-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_unproven-light.png
         :scale: 36 %
         :align: left
         :class: only-light

.. raw:: latex

   \end{code}

States
^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> unproven_DCTC_CR.print()
   ρ_D = g|0,0⟩⟨0,0| + (1 - g)|1,1⟩⟨1,1|

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> unproven_DCTC_CV.print()
   τ_D = g|0⟩⟨0| + (1 - g)|1⟩⟨1|

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> unproven_PCTC_CR.print()
   |ψ_P⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> unproven_PCTC_CV.print()
   τ_P = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage