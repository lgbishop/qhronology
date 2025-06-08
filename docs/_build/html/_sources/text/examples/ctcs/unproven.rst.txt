.. _`eg:unproven`:

Unproven-theorem paradox
========================

Description
-----------

The *unproven-theorem paradox* :cite:p:`deutsch_quantum_1991,lloyd_closed_2011,allen_treating_2014` (depicted in :numref:`fig:circuit_ctc_unproven`) is, as we shall see, not as straightforward as other temporal paradoxes. Here, the CR system is comprised of two subsystems: the first (upper) is the *book*, and the second (lower) is the *mathematician*.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_unproven-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the unproven-theorem paradox under the D-CTCs prescription.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_unproven-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of the unproven-theorem paradox under the D-CTCs prescription.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_unproven-light.png
   :name: fig:circuit_ctc_unproven
   :scale: 36 %
   :alt: A quantum circuit diagram of the unproven-theorem paradox under the D-CTCs prescription.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum model of the unproven-theorem paradox under the D-CTCs prescription.

Described by the unitary

.. math:: \Unitary = \Swap^{1,2} \cdot \Control^0 \NOT^1 \cdot \Control^2 \NOT^0,
   :label: eq:unproven_unitary

the unproven-theorem paradox encapsulates the scenario in which the proof of a theorem that a mathematician reads in the past is the very same proof which they write down in the future book (with the book having travelled back in time). We therefore denote the absence and presence of the proof in each subsystem intuitively by :math:`\ket{0}` and :math:`\ket{1}`, respectively. Under this interpretation, when the mathematician and/or the book are in the state :math:`\ket{1}`, they possess a "correct" proof, while being in the state :math:`\ket{0}` means that they do not. (Alternatively, one can think of these qubit levels as denoting different answers to some problem the mathematician is working on. They can then encode their proof of some theorem into an :math:`\Number`-bit binary string by using :math:`\Number` copies of the circuit :cite:p:`allen_treating_2014`.) Thus, the CR input state

.. math:: \StateCR = \ket{0}\bra{0}\otimes\ket{0}\bra{0}

describes the situation in which both the book and mathematician do not initially possess the proof.

Solutions
---------

The D-CTC can be calculated to be

.. math::

   \begin{aligned}
      \StateCR_{\MapDCTCsCR} &= \ParameterFree\ket{0}\bra{0}\otimes\ket{0}\bra{0} + (1 - \ParameterFree)\ket{1}\bra{1}\otimes\ket{1}\bra{1},\\
      \StateCV_{\MapDCTCsCR} &= \ParameterFree\ket{0}\bra{0} + (1 - \ParameterFree)\ket{1}\bra{1}, \quad 0 \leq \ParameterFree \leq 1;
   \end{aligned}

while the P-CTC solutions are

.. math::

   \begin{aligned}
      \ket{\StatePure_{\MapPCTCsCR}} &= \ket{\Bell^+} = \frac{1}{\sqrt{2}}\bigl(\ket{0} \otimes \ket{0} + \ket{1} \otimes \ket{1}\bigr),\\
      \StateCV_{\MapPCTCsCR} &= \frac{1}{2}\Identity = \frac{1}{2}\bigl(\ket{0}\bra{0} + \ket{1}\bra{1}\bigr).
   \end{aligned}

Observe that the D-CTC solution turns out to be non-unique (with free parameter :math:`\ParameterFree`), while the P-CTC CV state is not. The interpretation of these solutions is that, according the P-CTCs, the mathematician and the book will be in a superposition of both possessing the proof and neither possessing it, while according to D-CTCs, the two parties will be in a parametrized mixture of such possibilities. Additionally, it is easy to see that the latter is the maximally entropic form of its D-CTC counterpart, which means that the ECP end-state evolution (the "correct" D-CTC fixed point which resolves the uniqueness ambiguity) in this case coincidentally is exactly the P-CTC CV solution.

Implementation
--------------

.. literalinclude:: /text/examples/ctcs/unproven.py
   :name: code:unproven
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> unproven.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_unproven-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_ctcs_unproven-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^

.. code:: python

   >>> unproven_DCTC_respecting.print()
   ρ_D = g|0,0⟩⟨0,0| + (1 - g)|1,1⟩⟨1,1|

.. code:: python

   >>> unproven_DCTC_violating.print()
   τ_D = g|0⟩⟨0| + (1 - g)|1⟩⟨1|

.. code:: python

   >>> unproven_PCTC_respecting.print()
   |ψ_P⟩ = sqrt(2)/2|0,0⟩ + sqrt(2)/2|1,1⟩

.. code:: python

   >>> unproven_PCTC_violating.print()
   τ_P = 1/2|0⟩⟨0| + 1/2|1⟩⟨1|

.. only:: html

   .. rst-class:: bibliography

      .. rubric:: :stylebibliography:`References`

      .. bibliography::
         :filter: docname in docnames

.. raw:: latex
   
   \newpage