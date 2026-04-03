.. _`eg:grandfather`:

Grandfather paradox
===================

Description
-----------

Probably the most prominent time-travel paradox is the *grandfather paradox*. Presented here is a simplified, quantum version of the paradox (based on :cite:p:`lloyd_closed_2011`), in which a qubit CV state has an apparently paradoxical influence on its past self (exterior to the CTC) via a CNOT operation. This is illustrated in :numref:`fig:circuit_ctc_grandfather`.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_grandfather-dark.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the grandfather paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_grandfather-light.png
      :scale: 34 %
      :alt: A quantum circuit diagram of the grandfather paradox.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_grandfather-light.png
   :name: fig:circuit_ctc_grandfather
   :scale: 34 %
   :alt: A quantum circuit diagram of the grandfather paradox.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum model of the grandfather paradox.

.. raw:: latex

   \vspace*{-\baselineskip}

Here, we have two systems: the first (upper) is the *chronology-respecting* (CR) system, while the second (lower) is the *chronology-violating* (CV) one. For simplicity, the Hilbert spaces of both are ordinary qubit spaces, which are sufficient for modelling the evolution of an observer through the time machine and its chronology-violating region. In the grandfather paradox, the sole (quantum) degree of freedom of the observer is their *vital status* ("aliveness"): whether they are alive or dead. Without loss of generality, we arbitrarily associate the level :math:`\ket{0}` with observer being dead, while :math:`\ket{1}` will denote their alive state. The circuit therefore describes a scenario in which an observer's state changes in accordance with their own future state in the time machine (due to the CNOT gate), after which they SWAP onto the CV system and experience the interaction from the other perspective. The combined unitary gate thus has the form

.. math::
   :label: eq:grandfather_unitary

   \begin{aligned}
       \Unitary = \Swap^{0,1} \cdot \Control^1 \NOT^0.
   \end{aligned}

As this is a quantum temporal paradox, there are multiple prescriptions (see :numref:`sec:literature_quantum` :ref:`sec:literature_quantum`) by which resolutions can be computed.

Solutions
---------

D-CTCs
^^^^^^

In Deutsch's model (D-CTCs), we necessarily have to calculate fixed-point solutions :math:`\StateCV` for the CV system. This is accomplished by first computing the standard evolution of the bipartite input state :math:`\StateCR \otimes \StateCV`,

.. math::

   \begin{aligned}
       \MapGeneral_{\Unitary} [\StateCR \otimes \StateCV] &= \Unitary (\StateCR \otimes \StateCV) \Unitary^\dagger \\
       &= \Swap^{0,1} \cdot \Control^1 \NOT^0 (\StateCR \otimes \StateCV) \Control^1 \NOT^{\dagger 0} \cdot \Swap^{\dagger 0,1} \\
       &= \Swap^{0,1} \bigl(\StateCR \otimes \ket{0}\bra{0}\StateCV\ket{0}\bra{0} \\
       & \qquad\quad\; + \StateCR\Pauli_x^\dagger \otimes \ket{0}\bra{0}\StateCV\ket{1}\bra{1} \\
       & \qquad\quad\; + \Pauli_x\StateCR \otimes \ket{1}\bra{1}\StateCV\ket{0}\bra{0} \\
       & \qquad\quad\; + \Pauli_x\StateCR\Pauli_x^\dagger \otimes \ket{1}\bra{1}\StateCV\ket{1}\bra{1}\bigr) \Swap^{\dagger 0,1} \\
       &= \ket{0}\bra{0}\StateCV\ket{0}\bra{0} \otimes \StateCR \\
       & \quad + \ket{0}\bra{0}\StateCV\ket{1}\bra{1} \otimes \StateCR\Pauli_x^\dagger \\
       & \quad + \ket{1}\bra{1}\StateCV\ket{0}\bra{0} \otimes \Pauli_x\StateCR \\
       & \quad + \ket{1}\bra{1}\StateCV\ket{1}\bra{1} \otimes \Pauli_x\StateCR\Pauli_x^\dagger.
   \end{aligned}

Subsequently tracing out the CR system yields the D-CTCs CV map,

.. math::

   \begin{aligned}
       \MapDCTCsCV_{\Unitary} [\StateCR,\StateCV] &= \trace_{0} \bigl[\Unitary (\StateCR \otimes \StateCV) \Unitary^\dagger\bigr] \\
       &= \bra{0}\StateCV\ket{0} \cdot \StateCR + \bra{1}\StateCV\ket{1} \cdot \Pauli_x\StateCR\Pauli_x^\dagger,
   \end{aligned}

while tracing out the CV system gives the CR map,

.. math::

   \begin{aligned}
       \MapDCTCsCR_{\Unitary} [\StateCR,\StateCV] &= \trace_{1} \bigl[\Unitary (\StateCR \otimes \StateCV) \Unitary^\dagger\bigr] \\
       &= \ket{0}\bra{0}\StateCV\ket{0}\bra{0} \\
       & \quad + \ket{0}\bra{0}\StateCV\ket{1}\bra{1} \cdot \bigl[\bra{0}\StateCR\ket{1} + \bra{1}\StateCR\ket{0}\bigr] \\
       & \quad + \ket{1}\bra{1}\StateCV\ket{0}\bra{0} \cdot \bigl[\bra{1}\StateCR\ket{0} + \bra{0}\StateCR\ket{1}\bigr] \\
       & \quad + \ket{1}\bra{1}\StateCV\ket{1}\bra{1}.
   \end{aligned}

Solutions for the CV system are then given as fixed points of the corresponding map, i.e., :math:`\StateCV_\MapDCTCsCR = \MapDCTCsCV_{\Unitary} \bigl[\StateCR,\StateCV_\MapDCTCsCR\bigr]`, and accordingly we find the unique state

.. math::
   :label: eq:grandfather_D-CTCs_CV

   \begin{aligned}
       \StateCV_\MapDCTCsCR &= \frac{1}{2}\StateCR + \frac{1}{2}\Pauli_x\StateCR\Pauli_x^\dagger \\
       &= \frac{1}{2}\Bigl[\ket{0}\bra{0} + \bigl(\bra{0}\StateCR\ket{1} + \bra{1}\StateCR\ket{0}\bigr)\bigl(\ket{0}\bra{1} + \ket{1}\bra{0}\bigr) + \ket{1}\bra{1}\Bigr].
   \end{aligned}

With this, the solution for the CR system can be computed to be

.. math::
   :label: eq:grandfather_D-CTCs_CR

   \begin{aligned}
       \StateCR_\MapDCTCsCR &= \frac{1}{2}\Bigl[\ket{0}\bra{0} + \bigl(\bra{0}\StateCR\ket{1} + \bra{1}\StateCR\ket{0}\bigr)^2\bigl(\ket{0}\bra{1} + \ket{1}\bra{0}\bigr) + \ket{1}\bra{1}\Bigr]
   \end{aligned}

which is similarly unique.

P-CTCs
^^^^^^

To compute the resolution to the grandfather paradox according to the postselected teleportation (P-CTCs) prescription of quantum time travel, we first calculate the reduced P-CTC operator,

.. math::
   :label: eq:grandfather_P-CTCs_operator

   \begin{aligned}
       \OperatorPCTC &\equiv \trace_\CV[\Unitary] \\
       &= \trace_1[\Swap^{0,1} \cdot \Control^1 \NOT^0] \\
       &= \trace_1\bigl[\Swap^{0,1} \bigl(\Identity \otimes \ket{0}\bra{0} + \Pauli_x \otimes \ket{1}\bra{1}\bigr)\bigr] \\
       &= \trace_1\bigl[\Swap^{0,1} \bigl((\ket{0}\bra{0} + \ket{1}\bra{1}) \otimes \ket{0}\bra{0} + (\ket{0}\bra{1} + \ket{1}\bra{0}) \otimes \ket{1}\bra{1}\bigr)\bigr] \\
       &= \trace_1\bigl[\ket{0}\bra{0} \otimes \ket{0}\bra{0} + \ket{0}\bra{1} \otimes \ket{1}\bra{0} + \ket{1}\bra{1} \otimes \ket{0}\bra{1} + \ket{1}\bra{0} \otimes \ket{1}\bra{1}\bigr] \\
       &= \ket{0}\bra{0} + \ket{1}\bra{0} \\
       &= \ket{+}\bra{0}.
   \end{aligned}

Using this, we can obtain the P-CTC CR state from its definition :eq:`eq:P-CTCs_CR`,

.. math::
   :label: eq:grandfather_P-CTCs_CR

   \begin{aligned}
       \StateCR_\MapPCTCsCR &= \MapPCTCsCR_{\Unitary} [\StateCR] \\
       &= \frac{\OperatorPCTC \StateCR \OperatorPCTC^\dagger}{\trace[\OperatorPCTC \StateCR \OperatorPCTC^\dagger]} \\
       &= \ket{+}\bra{+},
   \end{aligned}

where we have used the canonical form

.. math:: \ket{+} \equiv \frac{1}{\sqrt{2}}\bigl[\ket{0} + \ket{1}\bigr].

Finally, using the expression :eq:`eq:P-CTCs_CV`, we can compute the P-CTC CV state (via weak-measurement quantum state tomography) to be

.. math::
   :label: eq:grandfather_P-CTCs_CV

   \begin{aligned}
       \StateCV_\MapPCTCsCR &= \frac{1}{2}\StateCR + \frac{1}{2}\Pauli_x\StateCR\Pauli_x^\dagger \\
       &= \frac{1}{2}\Bigl[\ket{0}\bra{0} + \bigl(\bra{0}\StateCR\ket{1} + \bra{1}\StateCR\ket{0}\bigr)\bigl(\ket{0}\bra{1} + \ket{1}\bra{0}\bigr) + \ket{1}\bra{1}\Bigr].
   \end{aligned}

Note that this is identical to the D-CTC CV state :eq:`eq:grandfather_D-CTCs_CV`.

P-CTC restrictions on initial data
""""""""""""""""""""""""""""""""""

The grandfather paradox is particularly interesting because it exhibits pathological behaviour under the P-CTC prescription. Indeed, its antichronological effect on a general qubit can be observed by analyzing the evolution of the entangled state,

.. math:: \ket{\phi}_{\mathrm{rec},\CR} = \sqrt{\Omega} \ket{0}_\mathrm{rec} \otimes \ket{0}_\CR + \sqrt{1 - \Omega} \ket{1}_\mathrm{rec} \otimes \ket{1}_\CR,

where :math:`0 \leq \Omega \leq 1` controls the balance of the entanglement. Here, measurement of the first subsystem---the *record* subsystem---reveals (due to the entanglement) which CR state interacted with the P-CTC. Accordingly, by using the bipartite unitary

.. math:: \Identity_\mathrm{rec}\otimes\trace_\CV[\Unitary] = \Identity_\mathrm{rec}\otimes\ket{+}\bra{0}_\CR,

where :math:`\OperatorPCTC = \trace_\CV[\Unitary]` is the P-CTC operator, we obtain the evolution

.. math:: \bigl(\Identity_\mathrm{rec}\otimes\trace_\CV[\Unitary]\bigr)\ket{\phi} = \sqrt{2\Omega}\ket{0}_\mathrm{rec}\otimes\ket{+}_\CR.

Renormalization vanishes the coefficient :math:`\sqrt{2\Omega}`, leaving the record to consist of only the state :math:`\ket{0}` regardless of the value of :math:`\Omega`. This suggests that the CR input was likewise only :math:`\ket{0}` even if :math:`\Omega \neq 1`, indicating that the entanglement was broken.

Prior to the renormalization, a value of :math:`\Omega = 0` leads to a vanishing P-CTC evolution, and so the renormalization process merely serves to produce a physical output state for all :math:`\Omega`. In doing so however, the record reveals that a CR input of :math:`\ket{1}` was never prepared, even when :math:`\Omega \neq 1`. An input of :math:`\StateCR = \ket{1}\bra{1}` is thus forbidden under the P-CTC description of this simplified grandfather paradox. With the interpretation of :math:`\ket{1}` as corresponding to "alive", this result is curious, but is probably just an indication that this particular version of the grandfather paradox is overly simplistic. Additionally, in practice, the effects of quantum noise and decoherence would ensure that such an exact input state is not physically realizable. In any case, we conclude that although the grandfather paradox's interaction places theoretical constraints for certain input CR states, a (unique) P-CTC CV state :math:`\StateCV_{\MapPCTCsCR}` can *always* be determined via :eq:`eq:P-CTCs_CV`.

Implementation
--------------

.. raw:: latex

   \enlargethispage{-2\baselineskip}

.. raw:: latex

   \begin{codetitled}{Grandfather paradox}{}

.. literalinclude:: /text/examples/ctcs/grandfather.py
   :name: code:grandfather
   :language: python
   :caption:

.. raw:: latex

   \end{codetitled}

Output
------

Diagram
^^^^^^^

.. raw:: latex

   \begin{code}

.. code:: python

   >>> grandfather.diagram()

.. raw:: latex
   
   \includegraphics[scale=1.25, trim=-0.02cm -0.10cm 0 -0.15cm]{text_examples_ctcs_grandfather.pdf}
   \vspace{-1\baselineskip}

..

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_grandfather-dark.png
         :scale: 36 %
         :align: left
         :class: only-dark

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_grandfather-light.png
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

   >>> grandfather_DCTC_CR.print()
   ρ_D = 1/2|0⟩⟨0| + (ρ[0, 1] + ρ[1, 0])**2/2|0⟩⟨1| + (ρ[0, 1] + ρ[1, 0])**2/2|1⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> grandfather_DCTC_CV.print()
   τ_D = 1/2|0⟩⟨0| + (ρ[0, 1]/2 + ρ[1, 0]/2)|0⟩⟨1| + (ρ[0, 1]/2 + ρ[1, 0]/2)|1⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> grandfather_PCTC_CR.print()
   ρ_P = 1/2|0⟩⟨0| + 1/2|0⟩⟨1| + 1/2|1⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{code}

.. raw:: latex

   \begin{code}

.. code:: python

   >>> grandfather_PCTC_CV.print()
   τ_P = 1/2|0⟩⟨0| + (ρ[0, 1]/2 + ρ[1, 0]/2)|0⟩⟨1| + (ρ[0, 1]/2 + ρ[1, 0]/2)|1⟩⟨0| + 1/2|1⟩⟨1|

.. raw:: latex

   \end{code}

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage













