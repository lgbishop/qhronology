.. _`eg:scattering`:

Probabilistic scattering with a time machine
============================================

Description
-----------

In this example, we explore a basic probabilistic scattering interaction near a CTC. Our specific analysis will concern the power-of-SWAP gate :eq:`eq:swap_probabilistic` where the parameter :math:`\ParameterPower` represents the finite probability for a pair of interacting particles to collide with each other. Recall that the action of this gate :eq:`eq:swap_power_action` is interpretable as the spontaneous, probabilistic diffusion of a pair of systems between two modes. Thus, despite not being a temporal paradox in the typical sense, the probabilistic scattering interaction makes for an interesting scenario as it perhaps has a more realistic physical interpretation than the previously studied interactions. Furthermore, as we will see, it provides an example where the CV states of D-CTCs and P-CTCs do not coincide.

.. only:: html

   .. figure:: /figures/output/circuit_ctc_scattering-dark.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a probabilistic scattering interaction near a CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-dark

   .. figure:: /figures/output/circuit_ctc_scattering-light.png
      :scale: 36 %
      :alt: A quantum circuit diagram of a probabilistic scattering interaction near a CTC.
      :align: center
      :figwidth: 100 %
      :figclass: only-light

.. figure:: /figures/output/circuit_ctc_scattering-light.png
   :name: fig:circuit_ctc_scattering
   :scale: 36 %
   :alt: A quantum circuit diagram of a probabilistic scattering interaction near a CTC.
   :align: center
   :figwidth: 100 %
   :figclass: light-dark hidden

   A quantum model of a probabilistic scattering interaction near a CTC.

In contrast with the relatively straightforward computations of the other examples, the D-CTC analysis for our probabilistic SWAP interaction here (illustrated in :numref:`fig:circuit_swap_D-CTCs`) is slightly more involved. With :eq:`eq:swap_probabilistic`) as our unitary interaction, i.e.,

.. math:: \Unitary = \Swap^\ParameterPower,
   :label: eq:unitary_scattering

we can compute the evolution of the input states as

.. math::

   \begin{aligned}
      \Swap^\ParameterPower(\StateCR \otimes \StateCV_{\MapDCTCsCR})\Swap^{\ParameterPower \dagger} &= \cos^2\left(\frac{\pi \ParameterPower}{2}\right)\StateCR \otimes \StateCV_{\MapDCTCsCR} -\frac{\eye}{2}\sin(\pi \ParameterPower)\left(\StateCR\otimes\StateCV_{\MapDCTCsCR}\right)\Swap \\
      &\quad +\frac{\eye}{2}\sin(\pi \ParameterPower)\Swap\left(\StateCR\otimes\StateCV_{\MapDCTCsCR}\right) + \sin^2\left(\frac{\pi \ParameterPower}{2}\right)\StateCV_{\MapDCTCsCR} \otimes \StateCR.
   \end{aligned}

From this, we use the identities

.. math::

   \begin{aligned}
      \trace_\CR\bigl[\left(\StateCR\otimes\StateCV_{\MapDCTCsCR}\right)\Swap\bigr] &= \StateCV_{\MapDCTCsCR}\StateCR, \\
      \trace_\CR\bigl[\Swap\left(\StateCR\otimes\StateCV_{\MapDCTCsCR}\right)\bigr] &= \StateCR\StateCV_{\MapDCTCsCR},
   \end{aligned}

to compute the D-CTC fixed point condition

.. math::
   :label: eq:consistency_swap

   \begin{aligned}
      \StateCV_{\MapDCTCsCR} &= \trace_\CR\bigl[\Swap^\ParameterPower\left(\StateCR\otimes\StateCV_{\MapDCTCsCR}\right)\Swap^{\ParameterPower\dagger}\bigr] \\
      &= \StateCR - \eye \cot\left(\frac{\pi \ParameterPower}{2}\right)\left[\StateCV_{\MapDCTCsCR},\StateCR\right]
   \end{aligned}

where :math:`\cot({}\cdot{})` is the cotangent function, and

.. math:: \left[A,B\right] = AB - BA

is the commutator. Prior to this computation, it is clear that for even-integer :math:`\ParameterPower`, the corresponding interaction :math:`\UnitaryInteraction = \Identity` is trivial. In this case, no restrictions are placed on the trapped state :math:`\StateCV_{\MapDCTCsCR}` (other than requiring :math:`\trace[\StateCV_{\MapDCTCsCR}] = 1`), and the output state is simply :math:`\StateCR_{\MapDCTCsCR} = \StateCR`. Conversely, when :math:`\ParameterPower` is not an even integer, computational symbolic algebra solvers find :math:`\StateCV_{\MapDCTCsCR} = \StateCR` to be the unique solution of :eq:`eq:consistency_swap`). The P-CTC states may be similarly computed, and to summarise,

.. math::
   :label: eq:D-CTCs_CV_swap

   \begin{aligned}
      \StateCR_{\MapDCTCsCR} &= \StateCR, \label{eq:D-CTCs_CR_swap}\\
      \StateCV_{\MapDCTCsCR} &= \StateCR, \quad (\ParameterPower \neq 2k, k\in\Integers);
   \end{aligned}


.. math::
   :label: eq:P-CTCs_CV_swap

   \begin{aligned}
      \StateCR_{\MapPCTCsCR} &= \StateCR, \label{eq:P-CTCs_CR_swap}\\
      \StateCV_{\MapPCTCsCR} &= \cos^2\left(\frac{\pi \ParameterPower}{2}\right)\frac{\Identity}{2} + \sin^2\left(\frac{\pi \ParameterPower}{2}\right)\StateCR.
   \end{aligned}



Implementation
--------------

.. literalinclude:: /text/examples/ctcs/scattering.py
   :name: code:scattering
   :language: python
   :caption:

Output
------

Diagram
^^^^^^^

.. code:: python

   >>> circuit.diagram()

..

   .. raw:: latex
      
      \vspace{1em}
      \begin{mdframed}[hidealllines=true,backgroundcolor=boxcolor,innerleftmargin=2em,innerrightmargin=2em,innertopmargin=1em,innerbottommargin=1em,leftmargin=-2em,rightmargin=-2em]

   .. only:: html

      .. image:: /figures/output/text_examples_ctcs_scattering-dark.png
         :scale: 40 %
         :align: left
         :class: only-dark

   .. only:: html or latex

      .. image:: /figures/output/text_examples_ctcs_scattering-light.png
         :scale: 40 %
         :align: left
         :class: only-light

   .. raw:: latex
      
      \end{mdframed}
      \vspace{1em}

States
^^^^^^



.. raw:: latex
   
   \newpage